from langchain.tools import tool

from agents.ml_prediction_agent.predict import (
    predict_stock
)


@tool
def predict_stock_tool(
    ticker: str
) -> str:
    """
    Predict next-day stock direction.

    Args:
        ticker: Stock ticker symbol.

    Returns:
        Prediction and confidence score.
    """

    result = predict_stock(
        ticker
    )

    return (
        f"Prediction for {result['ticker']}:\n\n"
        f"Direction: {result['prediction']}\n"
        f"Confidence UP: {result['confidence_up']:.2%}\n"
        f"Confidence DOWN: {result['confidence_down']:.2%}"
    )