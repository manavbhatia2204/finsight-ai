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

from api.database.session import SessionLocal
from api.models.stock import Stock
from api.models.macro_indicator import MacroIndicator

from scripts.create_tables import (
    create_all_tables
)

from scripts.load_stock_prices import (
    load_stock_prices
)

from scripts.load_macro_data import (
    load_macro_data
)


def initialize_database():

    print(
        "\n========================================"
    )

    print(
        "FinSight AI Database Initialization"
    )

    print(
        "========================================\n"
    )

    print(
        "Step 1/3 : Creating database tables..."
    )

    create_all_tables()

    db = SessionLocal()

    try:

        stock_count = (
            db.query(Stock)
            .count()
        )

        macro_count = (
            db.query(MacroIndicator)
            .count()
        )

    finally:

        db.close()

    if stock_count == 0:

        print(
            "\nNo stock data found."
        )

        print(
            "Loading stock metadata and prices..."
        )

        load_stock_prices()

    else:

        print(
            f"\nDatabase already contains "
            f"{stock_count} stocks."
        )

        print(
            "Skipping stock initialization."
        )

    if macro_count == 0:

        print(
            "\nNo macroeconomic data found."
        )

        print(
            "Loading macroeconomic indicators..."
        )

        load_macro_data()

    else:

        print(
            f"\nDatabase already contains "
            f"{macro_count} macro records."
        )

        print(
            "Skipping macro initialization."
        )

    print(
        "\n========================================"
    )

    print(
        "✅ Database initialization completed."
    )

    print(
        "========================================"
    )


if __name__ == "__main__":

    initialize_database()