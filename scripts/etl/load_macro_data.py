import sys
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent.parent
sys.path.append(str(project_root))

import pandas as pd

from api.database.session import SessionLocal
from api.models.macro_indicator import MacroIndicator

db = SessionLocal()

try:
    df = pd.read_csv("data/raw/cpi_data.csv")

    inserted_rows = 0

    for _, row in df.iterrows():

        existing = (
            db.query(MacroIndicator)
            .filter(
                MacroIndicator.indicator_code == row["indicator_code"],
                MacroIndicator.date == row["date"]
            )
            .first()
        )

        if existing:
            continue

        record = MacroIndicator(
            indicator_name=row["indicator_name"],
            indicator_code=row["indicator_code"],
            date=row["date"],
            value=float(row["value"])
        )

        db.add(record)
        inserted_rows += 1

    db.commit()

    print(f"✅ Inserted {inserted_rows} macro records")

finally:
    db.close()