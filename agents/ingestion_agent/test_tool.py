import sys
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent.parent
sys.path.append(str(project_root))

from agents.ingestion_agent.tools.stock_tool import get_stock_price

result = get_stock_price.invoke(
    {"ticker": "AAPL"}
)

print(result)