from langchain.tools import tool

from agents.ingestion_agent.tools.check_last_updated_tool import (
    check_last_updated
)

from agents.ingestion_agent.tools.fetch_macro_data_tool import (
    fetch_macro_data
)


@tool(return_direct=True)
def refresh_macro_if_needed(
    indicator: str
) -> str:
    """
    Check whether macroeconomic data is current.
    Fetch only if needed.
    """

    status = check_last_updated.invoke(
        {
            "indicator": indicator
        }
    )

    if "up to date" in status.lower():
        return status

    return fetch_macro_data.invoke(
        {
            "indicator": indicator
        }
    )