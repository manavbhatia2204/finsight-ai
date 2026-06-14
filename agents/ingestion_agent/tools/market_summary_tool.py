from langchain.tools import tool

from api.database.session import SessionLocal
from api.models.macro_indicator import MacroIndicator


@tool
def get_market_summary(summary_type: str) -> str:
    """
Generate a summary of current macroeconomic conditions.

Use summary_type="market" for a general market summary.
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