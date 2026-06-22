import sys

from pathlib import Path

project_root = (
    Path(__file__)
    .resolve()
    .parent.parent.parent
)

sys.path.append(
    str(project_root)
)

from agents.ml_prediction_agent.train_model import (
    train_model
)

TICKERS = [
    "AAPL",
    "MSFT",
    "NVDA",
    "AMZN",
    "GOOGL",
    "META",
    "TSLA"
]

for ticker in TICKERS:

    print(
        f"\n{'=' * 60}"
    )

    print(
        f"TRAINING {ticker}"
    )

    print(
        f"{'=' * 60}"
    )

    try:

        train_model(
            ticker
        )

        print(
            f"\nSUCCESS: {ticker}"
        )

    except Exception as e:

        print(
            f"\nFAILED: {ticker}"
        )

        print(
            str(e)
        )