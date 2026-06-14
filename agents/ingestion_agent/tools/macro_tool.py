from langchain.tools import tool

from api.database.session import SessionLocal
from api.models.macro_indicator import MacroIndicator


@tool
def get_latest_macro_indicator(indicator_name: str) -> str:
    """
    Get the latest value of a macroeconomic indicator.

    Supported indicators:
    - inflation
    - cpi
    - gdp
    - interest rates
    - federal funds rate
    - unemployment
    - unemployment rate
    """

    indicator_name = indicator_name.lower().strip()

    mapping = {
        "inflation": "CPIAUCSL",
        "cpi": "CPIAUCSL",
        "gdp": "GDP",
        "interest rates": "FEDFUNDS",
        "federal funds rate": "FEDFUNDS",
        "unemployment": "UNRATE",
        "unemployment rate": "UNRATE"
    }

    indicator_code = mapping.get(indicator_name)

    if not indicator_code:
        return f"Unsupported indicator: {indicator_name}"

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