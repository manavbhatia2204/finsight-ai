from pathlib import Path
import sys
from sqlalchemy import text
from fastapi import (
    FastAPI,
    HTTPException
)

from pydantic import BaseModel
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


class QueryRequest(
    BaseModel
):
    query: str


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
def ask_finsight(
    request: QueryRequest
):

    try:

        result = run_orchestrator(
            request.query
        )

        return {
            "query": request.query,
            "report": result
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


@app.get("/predict/{ticker}")
def predict(
    ticker: str
):

    try:

        result = predict_stock(
            ticker.upper()
        )

        return result

    except FileNotFoundError as e:

        raise HTTPException(
            status_code=404,
            detail=str(e)
        )

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
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