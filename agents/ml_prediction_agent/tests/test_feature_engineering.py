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

from agents.ml_prediction_agent.feature_engineering import (
    get_training_data
)

df = get_training_data(
    "AAPL"
)

print(
    df[
        [
            "date",
            "close",
            "target"
        ]
    ].tail(10)
)
print("\nTarget Distribution:\n")

print(
    df["target"]
    .value_counts()
)

print("\nColumns:\n")

print(df.columns.tolist())

print("\nShape:")

print(df.shape)