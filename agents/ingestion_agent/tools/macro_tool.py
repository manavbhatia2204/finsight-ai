from langchain.tools import tool

from api.database.session import SessionLocal
from api.models.macro_indicator import MacroIndicator


@tool
def get_latest_macro_indicator(indicator_code: str) -> str:
    """
Get the latest value for a macroeconomic indicator.

Supported indicators:

CPIAUCSL = Consumer Price Index (CPI)
GDP = Gross Domestic Product
FEDFUNDS = Federal Funds Rate

Use CPIAUCSL when the user asks about inflation or CPI.
Use FEDFUNDS when the user asks about interest rates.
"""

    db = SessionLocal()

    try:
        result = (
            db.query(MacroIndicator)
            .filter(
                MacroIndicator.indicator_code == indicator_code
            )
            .order_by(
                MacroIndicator.date.desc()
            )
            .first()
        )

        if result is None:
            return f"No data found for {indicator_code}"

        return (
            f"{result.indicator_name} "
            f"({result.indicator_code}) "
            f"latest value: {result.value} "
            f"on {result.date}"
        )

    finally:
        db.close()