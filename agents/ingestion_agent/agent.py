from langchain.agents import create_agent

from agents.ingestion_agent.llm import llm
from agents.ingestion_agent.tools.database_tool import get_stock_count
from agents.ingestion_agent.tools.stock_tool import get_stock_price
from agents.ingestion_agent.tools.macro_tool import (
    get_latest_macro_indicator
)

agent = create_agent(
    model=llm,
    tools=[
        get_stock_price,
        get_stock_count,
        get_latest_macro_indicator
    ]
)