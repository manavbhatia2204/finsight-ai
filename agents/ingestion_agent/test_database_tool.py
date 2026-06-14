import sys
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent.parent
sys.path.append(str(project_root))

from agents.ingestion_agent.tools.database_tool import get_stock_count

result = get_stock_count.invoke(
    {
        "request": "stock count"
    }
)

print(result)