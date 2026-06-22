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

from agents.ml_prediction_agent.predict import (
    predict_stock
)

result = predict_stock(
    "AAPL"
)

print(result)