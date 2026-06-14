import sys
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent.parent
sys.path.append(str(project_root))

from agents.ingestion_agent.llm import llm
from agents.ingestion_agent.tools.stock_tool import get_stock_price
from agents.ingestion_agent.tools.database_tool import get_stock_count

print("\n=== TOOL RESULTS ===")

print(
    get_stock_price.invoke(
        {"ticker": "AAPL"}
    )
)

print(
    get_stock_count.invoke({})
)

print("\n=== LLM RESPONSE ===")

response = llm.invoke(
    """
    FinSight AI currently has:
    - One stock in the database
    - Access to live stock prices

    Explain why these capabilities are useful.
    """
)

print(response.content)