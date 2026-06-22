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
        "agents/ml_prediction_agent/model_store/xgboost_model.pkl"
    )

    if not model_path.exists():

        raise FileNotFoundError(
            "Trained model not found. Run train_model.py first."
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
        "confidence_up": float(round(
            confidence[1],
            4
        )),
        "confidence_down": float(round(
            confidence[0],
            4
        ))
    }


if __name__ == "__main__":

    result = predict_stock(
        "AAPL"
    )

    print(result)