import yfinance as yf
from langchain.tools import tool

from api.database.session import SessionLocal
from api.models.stock import Stock
from api.models.stock_price import StockPrice


@tool(return_direct=True)
def fetch_stock_data(
    ticker: str,
    period: str = "1mo"
) -> str:
    """
    Fetch stock price data from Yahoo Finance
    and store it in the database.

    Supported periods:
    - 5d
    - 1mo
    - 3mo
    - 6mo
    - 1y
    - 2y

    This tool stores historical stock prices.

    After receiving a successful result from this tool,
    do NOT call fetch_stock_data again.

    Return the result directly to the user.
    """

    db = SessionLocal()

    try:

        ticker = ticker.upper()

        print(f"Downloading data for {ticker}...")

        df = yf.download(
            ticker,
            period=period,
            auto_adjust=True,
            progress=False
        )

        if df.empty:
            return f"No data found for {ticker}"

        # Handle MultiIndex columns
        if hasattr(df.columns, "levels"):
            df.columns = df.columns.get_level_values(0)

        df = df.reset_index()
        df.columns = [col.lower() for col in df.columns]

        stock = (
            db.query(Stock)
            .filter(
                Stock.ticker == ticker
            )
            .first()
        )

        if stock is None:

            stock = Stock(
                ticker=ticker,
                company_name=ticker,
                sector="Unknown",
                exchange="Unknown"
            )

            db.add(stock)
            db.commit()
            db.refresh(stock)

            print(f"Created stock record for {ticker}")

        inserted_rows = 0

        for _, row in df.iterrows():

            existing = (
                db.query(StockPrice)
                .filter(
                    StockPrice.stock_id == stock.id,
                    StockPrice.date == row["date"].date()
                )
                .first()
            )

            if existing:
                continue

            price = StockPrice(
                stock_id=stock.id,
                date=row["date"].date(),
                open=float(row["open"]),
                high=float(row["high"]),
                low=float(row["low"]),
                close=float(row["close"]),
                volume=int(row["volume"])
            )

            db.add(price)
            inserted_rows += 1

        db.commit()

        latest_close = round(
            float(df["close"].iloc[-1]),
            2
        )

        return (
    f"✅ Stock data updated successfully.\n\n"
    f"Ticker: {ticker}\n"
    f"Latest Close: ${latest_close}\n"
    f"New Records Added: {inserted_rows}"
)

    except Exception as e:

        db.rollback()

        return (
            f"Error fetching stock data "
            f"for {ticker}: {str(e)}"
        )

    finally:
        db.close()