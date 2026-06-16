import sys
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent.parent
sys.path.append(str(project_root))

from agents.ingestion_agent.tools.fetch_stock_data_tool import (
    fetch_stock_data
)

print(fetch_stock_data.name)
print(fetch_stock_data.args)
print(fetch_stock_data.description)