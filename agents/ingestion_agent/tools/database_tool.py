from langchain.tools import tool

from api.database.session import SessionLocal
from api.models.stock import Stock


@tool
def get_stock_count() -> str:
    """
    Get the number of stocks stored in the database.
    """

    db = SessionLocal()

    try:
        count = db.query(Stock).count()

        return f"There are {count} stocks in the database."

    finally:
        db.close()