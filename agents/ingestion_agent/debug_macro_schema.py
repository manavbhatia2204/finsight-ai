import sys
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent.parent
sys.path.append(str(project_root))

from agents.ingestion_agent.tools.macro_tool import (
    get_latest_macro_indicator
)

print(get_latest_macro_indicator.name)
print(get_latest_macro_indicator.args)
print(get_latest_macro_indicator.description)