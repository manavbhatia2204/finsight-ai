from agents.ml_prediction_agent.predict import (
    predict_stock
)


def prediction_node(
    state
):
    print(
        "\nPrediction Node Executed"
    )

    ticker = (
        state.get(
            "ticker"
        )
        or "AAPL"
    )

    result = predict_stock(
        ticker
    )

    return {
        "prediction_result": result
    }