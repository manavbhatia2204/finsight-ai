import sys
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent.parent
sys.path.append(str(project_root))

from agents.ingestion_agent.llm import llm
from agents.ingestion_agent.tools.fetch_stock_data_tool import (
    fetch_stock_data
)

model = llm.bind_tools([fetch_stock_data])

response = model.invoke(
    "Fetch Apple stock data"
)

print(response)