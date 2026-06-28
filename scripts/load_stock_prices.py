import sys
from pathlib import Path

project_root = (
    Path(__file__)
    .resolve()
    .parent.parent
)

sys.path.append(
    str(project_root)
)

import pandas as pd

from config.settings import CONFIG

from api.database.session import SessionLocal
from api.models.stock import Stock
from api.models.stock_price import StockPrice


STOCKS = []

for ticker in CONFIG["tickers"]:

    STOCKS.append(
        {
            "ticker": ticker["symbol"],
            "company_name": ticker["company"],
            "sector": ticker["sector"],
            "exchange": "NASDAQ"
        }
    )


def load_stock_prices():
    """
    Load stock metadata and historical
    prices into PostgreSQL.
    """

    db = SessionLocal()

    try:

        for stock_info in STOCKS:

            ticker = stock_info["ticker"]

            print(
                f"\nProcessing {ticker}..."
            )

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
                    company_name=stock_info["company_name"],
                    sector=stock_info["sector"],
                    exchange=stock_info["exchange"]
                )

                db.add(stock)

                db.commit()

                db.refresh(stock)

                print(
                    f"Inserted {ticker} into stocks table"
                )

            csv_path = (
                f"data/raw/"
                f"{ticker.lower()}_stock_data.csv"
            )

            csv_file = Path(csv_path)

            if not csv_file.exists():

                print(
                    f"⚠ Stock data not found for {ticker}. Skipping..."
                )

                continue

            df = pd.read_csv(
                csv_file
            )

            inserted_rows = 0

            for _, row in df.iterrows():

                existing = (
                    db.query(StockPrice)
                    .filter(
                        StockPrice.stock_id == stock.id,
                        StockPrice.date == row["date"]
                    )
                    .first()
                )

                if existing:
                    continue

                price = StockPrice(
                    stock_id=stock.id,
                    date=row["date"],
                    open=float(row["open"]),
                    high=float(row["high"]),
                    low=float(row["low"]),
                    close=float(row["close"]),
                    volume=int(row["volume"])
                )

                db.add(price)

                inserted_rows += 1

            db.commit()

            print(
                f"Inserted {inserted_rows} rows"
            )

    finally:

        db.close()


if __name__ == "__main__":

    load_stock_prices()