# agents/ml_prediction_agent/tests/test_model_integrity.py

import pytest
from pathlib import Path
import joblib

MODEL_DIR = Path(__file__).resolve().parent.parent / "model_store"

TICKERS = ["AAPL", "MSFT", "NVDA", "AMZN", "GOOGL", "META", "TSLA"]


@pytest.mark.parametrize("ticker", TICKERS)
def test_model_file_exists(ticker):
    """Every configured ticker should have a trained model file."""
    model_path = MODEL_DIR / f"xgboost_{ticker}.pkl"
    assert model_path.exists(), f"Missing model file for {ticker}"


@pytest.mark.parametrize("ticker", TICKERS)
def test_model_loads_without_error(ticker):
    """
    The model file should load cleanly with joblib.
    This directly guards against the 'input stream corrupted'
    XGBoost version-mismatch bug found in Week 4.
    """
    model_path = MODEL_DIR / f"xgboost_{ticker}.pkl"

    if not model_path.exists():
        pytest.skip(f"Model file for {ticker} does not exist, skipping load test")

    try:
        model = joblib.load(model_path)
    except Exception as e:
        pytest.fail(f"Model for {ticker} failed to load: {str(e)}")

    assert model is not None


@pytest.mark.parametrize("ticker", TICKERS)
def test_model_can_predict(ticker):
    """
    A loaded model should be able to run .predict() and .predict_proba()
    without raising an error, using real feature data.
    """
    from agents.ml_prediction_agent.predict import predict_stock

    try:
        result = predict_stock(ticker)
    except FileNotFoundError:
        pytest.skip(f"No model found for {ticker}, skipping prediction test")

    assert "ticker" in result
    assert "prediction" in result
    assert result["prediction"] in ["UP", "DOWN"]
    assert 0 <= result["confidence_up"] <= 100
    assert 0 <= result["confidence_down"] <= 100