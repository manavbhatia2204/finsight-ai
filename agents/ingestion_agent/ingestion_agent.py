from langchain.agents import create_agent

from agents.ingestion_agent.llm import llm
from agents.ingestion_agent.tools.fetch_stock_data_tool import (
    fetch_stock_data
)
from agents.ingestion_agent.tools.check_last_updated_tool import (
    check_last_updated
)

ingestion_agent = create_agent(
    model=llm,
    tools=[
        check_last_updated,
        fetch_stock_data
    ],
    system_prompt="""
You are an ingestion agent.

Your job is to fetch and store financial data.

Rules:
- First check if data is up to date.
- If data is already current, do not fetch again.
- Only fetch when data is stale or missing.
- Never call the same tool twice.
- Stop after the task is complete.
"""
)