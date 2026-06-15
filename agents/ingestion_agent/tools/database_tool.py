from langchain.tools import tool

from api.database.session import SessionLocal
from api.models.stock import Stock


@tool
def get_stock_count() -> str:
    """
    Returns the number of stock records stored in the database.

    Use ONLY when the user asks:
    - How many stocks are stored?
    - Stock count
    - Number of stocks in database
    """

    db = SessionLocal()

    try:
        count = db.query(Stock).count()
        return f"There are {count} stocks in the database."

    finally:
        db.close()