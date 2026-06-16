from langchain.tools import tool

from api.database.session import SessionLocal
from api.models.macro_indicator import MacroIndicator


@tool
def get_market_summary() -> str:
    """
    Get a complete market summary.

    Use whenever the user asks:

    - Give me a market summary
    - Market summary
    - Economic summary
    - Economy overview
    - How is the economy doing?

    This tool already includes:

    - GDP
    - Inflation (CPI)
    - Federal Funds Rate
    - Unemployment Rate

    IMPORTANT:

    This tool returns the COMPLETE market summary.

    After receiving the output from this tool,
    provide the answer directly to the user.

    Do NOT call get_market_summary again.

    Do NOT call any additional macroeconomic tools.
    """

    db = SessionLocal()

    try:
        #print("Running market summary tool...")

        indicators = {
            "GDP": None,
            "CPIAUCSL": None,
            "FEDFUNDS": None,
            "UNRATE": None
        }

        for code in indicators.keys():
            #print(f"Fetching {code}")

            result = (
                db.query(MacroIndicator)
                .filter(
                    MacroIndicator.indicator_code == code
                )
                .order_by(
                    MacroIndicator.date.desc()
                )
                .first()
            )

            if result:
                indicators[code] = result.value

        return f"""
MARKET SUMMARY COMPLETE

GDP: {indicators['GDP']}
Inflation (CPI): {indicators['CPIAUCSL']}
Federal Funds Rate: {indicators['FEDFUNDS']}%
Unemployment Rate: {indicators['UNRATE']}%

THIS IS THE FINAL MARKET SUMMARY.
NO FURTHER TOOL CALLS ARE REQUIRED.
RETURN THIS INFORMATION DIRECTLY TO THE USER.
"""

    finally:
        db.close()