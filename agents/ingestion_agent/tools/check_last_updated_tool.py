from datetime import date

from langchain.tools import tool

from api.database.session import SessionLocal
from api.models.stock import Stock
from api.models.stock_price import StockPrice
from api.models.macro_indicator import MacroIndicator


@tool
def check_last_updated(
    ticker: str = "",
    indicator: str = ""
) -> str:
    """
Check whether stock or macroeconomic data is already current.

ALWAYS use this tool FIRST when the user asks:

- Is AAPL data up to date?
- When was AAPL last updated?
- Do we already have Apple data?
- Should I fetch Apple data?
- Is Apple data current?
- Check if data needs refreshing

Before calling fetch_stock_data, call this tool to determine
whether new data is actually required.

If this tool says the data is up to date,
DO NOT call fetch_stock_data.

Examples:

ticker="AAPL"

indicator="CPIAUCSL"
"""

    db = SessionLocal()

    try:

        # STOCK CHECK
        if ticker:

            ticker = ticker.upper()

            stock = (
                db.query(Stock)
                .filter(
                    Stock.ticker == ticker
                )
                .first()
            )

            if stock is None:
                return (
                    f"No stock record found for {ticker}. "
                    f"Fetch recommended."
                )

            latest_price = (
                db.query(StockPrice)
                .filter(
                    StockPrice.stock_id == stock.id
                )
                .order_by(
                    StockPrice.date.desc()
                )
                .first()
            )

            if latest_price is None:
                return (
                    f"No price history found for {ticker}. "
                    f"Fetch recommended."
                )

            latest_date = latest_price.date

        # MACRO CHECK
        elif indicator:

            indicator = indicator.upper()

            latest_macro = (
                db.query(MacroIndicator)
                .filter(
                    MacroIndicator.indicator_code == indicator
                )
                .order_by(
                    MacroIndicator.date.desc()
                )
                .first()
            )

            if latest_macro is None:
                return (
                    f"No macro data found for {indicator}. "
                    f"Fetch recommended."
                )

            latest_date = latest_macro.date

        else:

            return (
                "Provide either a ticker "
                "or an indicator."
            )

        days_old = (
            date.today() - latest_date
        ).days

        if days_old == 0:

            return (
                f"{ticker or indicator} is up to date. "
                f"Last record: today."
            )

        elif days_old == 1:

            return (
                f"{ticker or indicator} was last updated "
                f"yesterday ({latest_date}). "
                f"Consider re-fetching."
            )

        else:

            return (
                f"{ticker or indicator} is "
                f"{days_old} days old "
                f"(last record: {latest_date}). "
                f"Fetch recommended."
            )

    finally:
        db.close()