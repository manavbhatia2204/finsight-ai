import yfinance as yf
from langchain.tools import tool


@tool
def get_stock_price(ticker: str) -> str:
    """
    Get the latest stock closing price for a ticker symbol.
    """

    data = yf.download(
        ticker,
        period="5d",
        progress=False,
        auto_adjust=True
    )

    # Handle MultiIndex columns
    if hasattr(data.columns, "levels"):
        data.columns = data.columns.get_level_values(0)

    latest_price = round(float(data["Close"].iloc[-1]), 2)

    return f"{ticker} latest closing price: ${latest_price}"