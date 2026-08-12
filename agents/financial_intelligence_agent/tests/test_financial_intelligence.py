# agents/financial_intelligence_agent/tests/test_financial_intelligence.py

import pytest
from agents.financial_intelligence_agent.fundamentals import get_fundamentals
from agents.financial_intelligence_agent.risk_metrics import get_risk_metrics
from agents.financial_intelligence_agent.comparison import compare_companies


@pytest.mark.parametrize("ticker", ["AAPL", "MSFT", "TSLA"])
def test_get_fundamentals_returns_valid_data(ticker):
    """Fundamentals should return real numeric data, not errors, for known tickers."""
    result = get_fundamentals(ticker)

    assert "error" not in result
    assert result["ticker"] == ticker
    assert result["current_price"] is not None
    assert result["current_price"] > 0


@pytest.mark.parametrize("ticker", ["AAPL", "MSFT", "TSLA"])
def test_get_risk_metrics_returns_valid_data(ticker):
    """
    Risk metrics should return sane values.
    Volatility should always be positive - this is the kind of check
    that would have caught the stale-data bug from Week 3.
    """
    result = get_risk_metrics(ticker)

    assert "error" not in result["volatility"]
    assert result["volatility"]["annualized_volatility_pct"] > 0

    assert "error" not in result["max_drawdown"]
    assert result["max_drawdown"]["max_drawdown_pct"] <= 0  # drawdown is always negative or zero


def test_compare_companies_returns_both_tickers():
    """Comparison should return complete data for both companies."""
    result = compare_companies("AAPL", "MSFT")

    assert result["ticker_a"] == "AAPL"
    assert result["ticker_b"] == "MSFT"
    assert "error" not in result["fundamentals_a"]
    assert "error" not in result["fundamentals_b"]


def test_get_fundamentals_handles_invalid_ticker_gracefully():
    """An invalid ticker should return an error dict, not crash."""
    result = get_fundamentals("INVALIDTICKER123")

    assert "error" in result