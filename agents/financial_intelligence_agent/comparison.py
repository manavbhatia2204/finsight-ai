# agents/financial_intelligence_agent/comparison.py

from agents.financial_intelligence_agent.fundamentals import get_fundamentals
from agents.financial_intelligence_agent.risk_metrics import get_risk_metrics


def compare_companies(ticker_a: str, ticker_b: str) -> dict:
    """
    Compare two companies side by side using fundamentals and risk metrics.
    Reuses existing functions from Week 1 and Week 2 - no new calculations.
    """
    ticker_a = ticker_a.upper()
    ticker_b = ticker_b.upper()

    fundamentals_a = get_fundamentals(ticker_a)
    fundamentals_b = get_fundamentals(ticker_b)

    risk_a = get_risk_metrics(ticker_a)
    risk_b = get_risk_metrics(ticker_b)

    return {
        "ticker_a": ticker_a,
        "ticker_b": ticker_b,
        "fundamentals_a": fundamentals_a,
        "fundamentals_b": fundamentals_b,
        "risk_a": risk_a,
        "risk_b": risk_b,
    }


if __name__ == "__main__":
    import json
    result = compare_companies("AAPL", "MSFT")
    print(json.dumps(result, indent=2))