from langchain.agents import create_agent

from agents.ingestion_agent.llm import llm
from agents.ingestion_agent.tools.fetch_stock_data_tool import (
    fetch_stock_data
)
from agents.ingestion_agent.tools.check_last_updated_tool import (
    check_last_updated
)
from agents.ingestion_agent.tools.fetch_macro_data_tool import (
    fetch_macro_data
)

ingestion_agent = create_agent(
    model=llm,
    tools=[
        check_last_updated,
        fetch_stock_data,
        fetch_macro_data
    ],
    system_prompt="""
You are an ingestion agent.

Your only responsibility is fetching and storing financial data.

Available tools:

- check_last_updated
- fetch_stock_data
- fetch_macro_data

Rules:

- Always check freshness before fetching.
- If data is already current, do not fetch.
- Only fetch when data is stale or missing.
- Never call the same tool twice.
- Stop after task completion.

Stock examples:

- Fetch Apple stock data
- Fetch AAPL stock data

Macro examples:

- Fetch unemployment data
- Fetch inflation data
- Fetch GDP data
- Fetch FEDFUNDS data
"""
)