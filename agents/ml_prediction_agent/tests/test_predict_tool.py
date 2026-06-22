import sys
from pathlib import Path

project_root = (
    Path(__file__)
    .resolve()
    .parent.parent.parent.parent
)

sys.path.append(
    str(project_root)
)

from agents.ml_prediction_agent.tools.predict_stock_tool import (
    predict_stock_tool
)

result = predict_stock_tool.invoke(
    {
        "ticker": "AAPL"
    }
)

print(result)