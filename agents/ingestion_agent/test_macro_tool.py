import sys
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent.parent
sys.path.append(str(project_root))

from agents.ingestion_agent.tools.macro_tool import (
    get_latest_macro_indicator
)

for indicator in [
    "cpi",
    "gdp",
    "interest rates",
    "unemployment"
]:
    print("\n--------------------------------")
    print(
        get_latest_macro_indicator.invoke(
            {
                "indicator_name": indicator
            }
        )
    )