import joblib

from pathlib import Path

from agents.ml_prediction_agent.feature_engineering import (
    get_training_data
)


def predict_stock(
    ticker: str = "AAPL"
):
    """
    Load trained model and predict
    next-day stock direction.
    """

    model_path = Path(
        f"agents/ml_prediction_agent/model_store/"
        f"xgboost_{ticker.upper()}.pkl"
    )

    if not model_path.exists():

        raise FileNotFoundError(
            f"No trained model found for {ticker}"
        )

    model = joblib.load(
        model_path
    )

    df = get_training_data(
        ticker
    )

    latest_row = (
        df
        .drop(
            columns=[
                "date",
                "target"
            ]
        )
        .tail(1)
    )

    prediction = model.predict(
        latest_row
    )[0]

    confidence = (
        model.predict_proba(
            latest_row
        )[0]
    )

    return {
        "ticker": ticker.upper(),
        "prediction": (
            "UP"
            if prediction == 1
            else "DOWN"
        ),
        "confidence_up": round(
            float(confidence[1]) * 100,
            2
        ),
        "confidence_down": round(
            float(confidence[0]) * 100,
            2
        )
    }


if __name__ == "__main__":

    result = predict_stock(
        "AAPL"
    )

    print(result)