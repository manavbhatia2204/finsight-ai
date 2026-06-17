from datetime import date

from langchain.tools import tool

from api.database.session import SessionLocal
from api.models.stock import Stock
from api.models.stock_price import StockPrice
from api.models.macro_indicator import MacroIndicator


MACRO_FRESHNESS = {
    "UNRATE": 60,
    "CPIAUCSL": 60,
    "FEDFUNDS": 60,
    "GDP": 150,
}


@tool
def check_last_updated(
    ticker: str = "",
    indicator: str = ""
) -> str:
    """
    Check whether stock or macroeconomic data is already current.

    Examples:

    ticker="AAPL"

    indicator="UNRATE"
    """


    def finish(message: str) -> str:
        return message

    db = SessionLocal()

    try:

        # -----------------------------
        # STOCKS
        # -----------------------------
        if ticker:

            ticker = ticker.upper()

            stock = (
                db.query(Stock)
                .filter(Stock.ticker == ticker)
                .first()
            )

            if stock is None:
                return finish(
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
                return finish(
                    f"No price history found for {ticker}. "
                    f"Fetch recommended."
                )

            latest_date = latest_price.date

            days_old = (
                date.today() - latest_date
            ).days

            if days_old <= 1:

                return finish(
                    f"✅ {ticker} data is up to date.\n"
                    f"Last available record: {latest_date}."
                )

            return finish(
                f"{ticker} is {days_old} days old "
                f"(last record: {latest_date}). "
                f"Fetch recommended."
            )

        # -----------------------------
        # MACRO DATA
        # -----------------------------
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
                return finish(
                    f"No macro data found for {indicator}. "
                    f"Fetch recommended."
                )

            latest_date = latest_macro.date

            days_old = (
                date.today() - latest_date
            ).days

            allowed_age = MACRO_FRESHNESS.get(
                indicator,
                60
            )

            if days_old <= allowed_age:

                return finish(
                    f"✅ {indicator} data is up to date.\n"
                    f"Last available record: {latest_date}."
                )

            return finish(
                f"{indicator} is {days_old} days old "
                f"(last record: {latest_date}). "
                f"Fetch recommended."
            )

        else:

            return finish(
                "Provide either a ticker or an indicator."
            )

    finally:
        db.close()