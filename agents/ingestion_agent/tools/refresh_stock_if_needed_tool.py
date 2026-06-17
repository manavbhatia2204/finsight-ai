from langchain.tools import tool

from agents.ingestion_agent.tools.check_last_updated_tool import (
    check_last_updated
)
from agents.ingestion_agent.tools.fetch_stock_data_tool import (
    fetch_stock_data
)


@tool(return_direct=True)
def refresh_stock_if_needed(
    ticker: str
) -> str:
    """
    Check whether stock data is current.
    Fetch only if needed.
    """


    status = check_last_updated.invoke(
        {
            "ticker": ticker
        }
    )


    if "up to date" in status.lower():
        return status

    return fetch_stock_data.invoke(
        {
            "ticker": ticker
        }
    )