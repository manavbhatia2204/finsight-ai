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

from api.database.session import SessionLocal
from api.models.macro_indicator import MacroIndicator


def load_macro_data():

    """
    Load macroeconomic indicators
    into PostgreSQL.
    """

    csv_path = (
        "data/raw/macro_data.csv"
    )

    df = pd.read_csv(
        csv_path
    )

    db = SessionLocal()

    inserted_rows = 0

    try:

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

            macro = MacroIndicator(
                indicator_name=row["indicator_name"],
                indicator_code=row["indicator_code"],
                date=row["date"],
                value=float(row["value"])
            )

            db.add(
                macro
            )

            inserted_rows += 1

        db.commit()

        print(
            f"\nInserted {inserted_rows} macro records."
        )

    finally:

        db.close()


if __name__ == "__main__":

    load_macro_data()