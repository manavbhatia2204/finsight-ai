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

tickers = [
    "AAPL",
    "MSFT",
    "NVDA",
    "AMZN",
    "GOOGL",
    "META",
    "TSLA"
]

for ticker in tickers:

    result = predict_stock(
        ticker
    )

    print("\n" + "=" * 40)

    print(
        f"Ticker: {result['ticker']}"
    )

    print(
        f"Direction: {result['prediction']}"
    )

    print(
        f"Confidence UP: {result['confidence_up']}%"
    )

    print(
        f"Confidence DOWN: {result['confidence_down']}%"
    )