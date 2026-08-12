from pathlib import Path
import sys
import traceback
from sqlalchemy import text
from fastapi import (
    FastAPI,
    HTTPException,
    Request
)
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from prometheus_fastapi_instrumentator import Instrumentator
from api.database.connection import engine

project_root = (
    Path(__file__)
    .resolve()
    .parent.parent
)
sys.path.append(
    str(project_root)
)

from agents.orchestrator_agent.orchestrator_agent import (
    run_orchestrator
)
from agents.ml_prediction_agent.predict import (
    predict_stock
)
from api.database.session import (
    SessionLocal
)
from api.models.stock import (
    Stock
)
from api.models.stock_price import (
    StockPrice
)

app = FastAPI(
    title="FinSight AI API",
    version="1.0.0"
)

# --- Rate limiting setup ---
limiter = Limiter(
    key_func=get_remote_address
)
app.state.limiter = limiter
app.add_exception_handler(
    RateLimitExceeded,
    _rate_limit_exceeded_handler
)

# --- CORS setup ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://finsight-ai-manav.streamlit.app",
        "http://localhost:8501",
    ],
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)


class QueryRequest(
    BaseModel
):
    query: str

# --- Observability setup ---
Instrumentator().instrument(app).expose(app, endpoint="/metrics")

@app.get("/")
def root():
    return {
        "status": "running",
        "service": "FinSight AI"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "FinSight AI API"
    }


@app.get("/ready")
def readiness():
    try:
        with engine.connect() as connection:
            connection.execute(
                text("SELECT 1")
            )
        return {
            "status": "ready",
            "database": "connected"
        }
    except Exception as e:
        raise HTTPException(
            status_code=503,
            detail={
                "status": "not ready",
                "database": "disconnected",
                "error": str(e)
            }
        )


@app.post("/ask")
@limiter.limit("10/minute")
def ask_finsight(
    request: Request,
    body: QueryRequest
):
    try:
        result = run_orchestrator(
            body.query
        )
        return {
            "query": body.query,
            "report": result
        }
    except Exception as e:
        print("ASK ERROR:", str(e))
        traceback.print_exc()
        raise HTTPException(
            status_code=500,
            detail="Something went wrong processing your request. Please try again."
        )


@app.get("/predict/{ticker}")
@limiter.limit("20/minute")
def predict(
    request: Request,
    ticker: str
):
    try:
        result = predict_stock(
            ticker.upper()
        )
        return result
    except FileNotFoundError:
        raise HTTPException(
            status_code=404,
            detail=f"No prediction model available for {ticker.upper()}."
        )
    except Exception as e:
        print("PREDICT ERROR:", str(e))
        traceback.print_exc()
        raise HTTPException(
            status_code=500,
            detail="Something went wrong generating the prediction. Please try again."
        )


@app.get("/stocks/{ticker}/history")
def get_stock_history(
    ticker: str,
    limit: int = 30
):
    db = SessionLocal()
    try:
        stock = (
            db.query(Stock)
            .filter(
                Stock.ticker == ticker.upper()
            )
            .first()
        )
        if stock is None:
            raise HTTPException(
                status_code=404,
                detail=(
                    f"Ticker {ticker.upper()} "
                    f"not found"
                )
            )
        prices = (
            db.query(StockPrice)
            .filter(
                StockPrice.stock_id == stock.id
            )
            .order_by(
                StockPrice.date.desc()
            )
            .limit(limit)
            .all()
        )
        return {
            "ticker": stock.ticker,
            "company_name": stock.company_name,
            "records": [
                {
                    "date": str(
                        price.date
                    ),
                    "open": price.open,
                    "high": price.high,
                    "low": price.low,
                    "close": price.close,
                    "volume": price.volume
                }
                for price in prices
            ]
        }
    finally:
        db.close()