from agents.ml_prediction_agent.predict import (
    predict_stock
)


def prediction_node(
    state
):
    print(
        "\nPrediction Node Executed"
    )

    ticker = state.get(
        "ticker"
    )

    if ticker is None:

        return {
            "prediction_result": {
                "error": (
                    "Unsupported company or ticker."
                )
            }
        }

    try:

        result = predict_stock(
            ticker
        )

        return {
            "prediction_result": result
        }

    except Exception as e:

        return {
            "prediction_result": {
                "error": str(e)
            }
        }