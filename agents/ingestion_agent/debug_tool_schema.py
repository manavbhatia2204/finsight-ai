import sys
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent.parent
sys.path.append(str(project_root))

from agents.ingestion_agent.tools.market_summary_tool import (
    get_market_summary
)

print(get_market_summary.name)
print(get_market_summary.description)

try:
    print(get_market_summary.args)
except Exception as e:
    print("ARGS ERROR:", e)