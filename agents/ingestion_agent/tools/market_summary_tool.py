from langchain.tools import tool

from api.database.session import SessionLocal
from api.models.macro_indicator import MacroIndicator


@tool
def get_market_summary(query: str) -> str:
    """
Get a complete market summary.

Use this tool whenever the user asks:

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

Do NOT call additional macroeconomic indicator tools after using this tool.

Pass the user's request as the query parameter.
"""

    db = SessionLocal()

    try:

        indicators = {
            "GDP": None,
            "CPIAUCSL": None,
            "FEDFUNDS": None,
            "UNRATE": None
        }

        for code in indicators.keys():

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

        summary = f"""
Market Summary

GDP: {indicators['GDP']}

Inflation (CPI): {indicators['CPIAUCSL']}

Federal Funds Rate: {indicators['FEDFUNDS']}%

Unemployment Rate: {indicators['UNRATE']}%
"""

        return summary

    finally:
        db.close()