# agents/orchestrator_agent/tests/test_routing.py

import pytest
from agents.orchestrator_agent.nodes.router_node import router_node


@pytest.mark.parametrize("query,expected_route", [
    ("What is Apple's P/E ratio?", "financial_metrics"),
    ("What is Tesla's volatility?", "risk_analysis"),
    ("Compare Apple and Microsoft", "comparison"),
    ("Will TSLA go up tomorrow?", "prediction"),
    ("What did the Fed say about rates?", "research"),
])
def test_router_selects_correct_route(query, expected_route):
    """
    Verify the router correctly classifies different query types
    without needing a real LLM call - this is pure keyword logic.
    """
    state = {"query": query}
    result = router_node(state)

    assert result["route"] == expected_route, (
        f"Query '{query}' expected route '{expected_route}' "
        f"but got '{result['route']}'"
    )


@pytest.mark.parametrize("query,expected_ticker", [
    ("What is Apple's P/E ratio?", "AAPL"),
    ("Analyze Tesla's risk profile", "TSLA"),
    ("How is NVIDIA performing?", "NVDA"),
])
def test_router_extracts_correct_ticker(query, expected_ticker):
    """Verify the router correctly identifies the company/ticker from a query."""
    state = {"query": query}
    result = router_node(state)

    assert result["ticker"] == expected_ticker


def test_router_extracts_two_tickers_for_comparison():
    """Comparison queries should extract both companies mentioned."""
    state = {"query": "Compare Tesla and NVIDIA"}
    result = router_node(state)

    assert result["route"] == "comparison"
    assert result["ticker"] is not None
    assert result["ticker_b"] is not None
    assert result["ticker"] != result["ticker_b"]


def test_router_handles_unknown_company_gracefully():
    """A query with no recognized company should not crash, ticker should be None."""
    state = {"query": "What is the weather today?"}
    result = router_node(state)

    assert result["ticker"] is None