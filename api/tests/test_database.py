# api/tests/test_database.py

from sqlalchemy import text
from api.database.connection import engine


def test_database_connection_is_reachable():
    """The app should be able to connect to Supabase and run a basic query."""
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        assert result.fetchone()[0] == 1


def test_stocks_table_has_data():
    """The stocks table should contain the 7 configured tickers."""
    with engine.connect() as connection:
        result = connection.execute(text("SELECT COUNT(*) FROM stocks"))
        count = result.fetchone()[0]
        assert count >= 7


def test_stock_prices_table_has_recent_data():
    """
    Stock prices should not be stale.
    This directly guards against the 45-day-stale-data bug found in Week 3.
    """
    with engine.connect() as connection:
        result = connection.execute(
            text("SELECT MAX(date) FROM stock_prices")
        )
        latest_date = result.fetchone()[0]

    assert latest_date is not None

    from datetime import date
    days_stale = (date.today() - latest_date).days
    assert days_stale <= 8, (
        f"Stock price data is {days_stale} days stale. "
        f"Check the weekly data refresh workflow."
    )