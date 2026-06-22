import joblib

from pathlib import Path

from xgboost import XGBClassifier

from sklearn.model_selection import (
    TimeSeriesSplit
)

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score
)

from agents.ml_prediction_agent.feature_engineering import (
    get_training_data
)


def train_model(
    ticker: str = "AAPL"
):
    """
    Train an XGBoost model
    for next-day direction prediction.
    """

    df = get_training_data(
        ticker
    )

    X = df.drop(
        columns=[
            "date",
            "target"
        ]
    )

    y = df["target"]

    tscv = TimeSeriesSplit(
        n_splits=5
    )

    fold = 1

    scores = []

    model = None

    for train_idx, test_idx in tscv.split(X):

        X_train = X.iloc[train_idx]
        X_test = X.iloc[test_idx]

        y_train = y.iloc[train_idx]
        y_test = y.iloc[test_idx]

        model = XGBClassifier(
            n_estimators=100,
            max_depth=4,
            learning_rate=0.1,
            random_state=42,
            eval_metric="logloss"
        )

        model.fit(
            X_train,
            y_train
        )

        predictions = model.predict(
            X_test
        )

        accuracy = accuracy_score(
            y_test,
            predictions
        )

        precision = precision_score(
            y_test,
            predictions
        )

        recall = recall_score(
            y_test,
            predictions
        )

        f1 = f1_score(
            y_test,
            predictions
        )

        print(
            f"\nFold {fold}"
        )

        print(
            f"Accuracy: {accuracy:.4f}"
        )

        print(
            f"Precision: {precision:.4f}"
        )

        print(
            f"Recall: {recall:.4f}"
        )

        print(
            f"F1 Score: {f1:.4f}"
        )

        scores.append(
            {
                "accuracy": accuracy,
                "precision": precision,
                "recall": recall,
                "f1": f1
            }
        )

        fold += 1

    print("\nAverage Results")

    print(
        f"Accuracy: "
        f"{sum(s['accuracy'] for s in scores)/len(scores):.4f}"
    )

    print(
        f"Precision: "
        f"{sum(s['precision'] for s in scores)/len(scores):.4f}"
    )

    print(
        f"Recall: "
        f"{sum(s['recall'] for s in scores)/len(scores):.4f}"
    )

    print(
        f"F1 Score: "
        f"{sum(s['f1'] for s in scores)/len(scores):.4f}"
    )

    feature_importance = sorted(
        zip(
            X.columns,
            model.feature_importances_
        ),
        key=lambda x: x[1],
        reverse=True
    )

    print("\nTop Features:\n")

    for feature, importance in feature_importance[:10]:

        print(
            f"{feature}: {importance:.4f}"
        )

    model_dir = Path(
        "agents/ml_prediction_agent/model_store"
    )

    model_dir.mkdir(
        parents=True,
        exist_ok=True
    )

    model_path = (
        model_dir /
        "xgboost_model.pkl"
    )

    joblib.dump(
        model,
        model_path
    )

    print(
        f"\nModel saved to: {model_path}"
    )

    return model


if __name__ == "__main__":

    train_model(
        "AAPL"
    )