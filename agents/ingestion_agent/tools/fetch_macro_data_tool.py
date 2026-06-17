import os

from dotenv import load_dotenv
from fredapi import Fred
from langchain.tools import tool

from api.database.session import SessionLocal
from api.models.macro_indicator import MacroIndicator

load_dotenv()

FRED_API_KEY = os.getenv("FRED_API_KEY")

INDICATORS = {
    "CPIAUCSL": "Consumer Price Index",
    "GDP": "Gross Domestic Product",
    "FEDFUNDS": "Federal Funds Rate",
    "UNRATE": "Unemployment Rate"
}


@tool(return_direct=True)
def fetch_macro_data(
    indicator: str
) -> str:
    """
    Fetch macroeconomic data from FRED and store it
    in the macro_indicators table.

    Common indicators:

    - CPIAUCSL (Inflation)
    - GDP
    - FEDFUNDS
    - UNRATE

    Example:

    indicator="UNRATE"
    """

    db = SessionLocal()

    try:

        print("Running fetch_macro_data tool...")

        indicator = indicator.upper()

        if indicator not in INDICATORS:

            return (
                f"Unsupported indicator: {indicator}. "
                f"Supported indicators: "
                f"{', '.join(INDICATORS.keys())}"
            )

        print(f"Downloading {indicator}...")

        fred = Fred(
            api_key=FRED_API_KEY
        )

        series = fred.get_series(
            indicator
        )

        if series.empty:

            return (
                f"No data found for "
                f"{indicator}"
            )

        inserted_rows = 0

        for data_date, value in series.items():

            existing = (
                db.query(MacroIndicator)
                .filter(
                    MacroIndicator.indicator_code
                    == indicator,
                    MacroIndicator.date
                    == data_date.date()
                )
                .first()
            )

            if existing:
                continue

            record = MacroIndicator(
                indicator_name=INDICATORS[indicator],
                indicator_code=indicator,
                date=data_date.date(),
                value=float(value)
            )

            db.add(record)
            inserted_rows += 1

        db.commit()

        latest_value = float(
            series.iloc[-1]
        )

        latest_date = (
            series.index[-1]
            .date()
        )

        return f"""
FETCH COMPLETE

Indicator: {indicator}
Rows inserted: {inserted_rows}
Latest value: {latest_value}
Latest date: {latest_date}

THIS TASK IS COMPLETE.
DO NOT CALL fetch_macro_data AGAIN.
RETURN THIS RESULT DIRECTLY TO THE USER.
"""

    except Exception as e:

        db.rollback()

        return (
            f"Error fetching "
            f"{indicator}: {str(e)}"
        )

    finally:

        db.close()