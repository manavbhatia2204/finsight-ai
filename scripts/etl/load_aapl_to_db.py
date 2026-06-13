import sys
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent.parent
sys.path.append(str(project_root))

import pandas as pd

from api.database.session import SessionLocal
from api.models.stock import Stock
from api.models.stock_price import StockPrice

db = SessionLocal()

try:
    # Check if AAPL exists
    stock = (
        db.query(Stock)
        .filter(Stock.ticker == "AAPL")
        .first()
    )

    if stock is None:
        stock = Stock(
            ticker="AAPL",
            company_name="Apple Inc.",
            sector="Technology",
            exchange="NASDAQ"
        )

        db.add(stock)
        db.commit()
        db.refresh(stock)

        print("✅ AAPL inserted into stocks table")

    else:
        print("ℹ️ AAPL already exists")

    # Load CSV
    df = pd.read_csv("data/raw/aapl_stock_data.csv")

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

    print(f"✅ Inserted {inserted_rows} price records")

finally:
    db.close()