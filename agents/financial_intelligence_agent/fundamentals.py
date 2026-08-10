# agents/financial_intelligence_agent/fundamentals.py

import yfinance as yf
from typing import Optional


def _safe_get(info: dict, key: str, decimals: int = 4) -> Optional[float]:
    """
    Safely extract a field from yfinance's info dict.
    Returns None if missing — never crashes, never returns garbage.
    """
    value = info.get(key)
    if value is None:
        return None
    try:
        return round(float(value), decimals)
    except (ValueError, TypeError):
        return None


def get_fundamentals(ticker: str) -> dict:
    """
    Fetch core fundamental metrics for a ticker using yfinance.
    Returns a dict with None for any field yfinance doesn't provide.
    """
    ticker = ticker.upper()
    stock = yf.Ticker(ticker)
    info = stock.info

    if not info or info.get("regularMarketPrice") is None:
        return {
            "ticker": ticker,
            "error": f"No data found for {ticker}. Check the ticker symbol."
        }

    fundamentals = {
        "ticker": ticker,
        "company_name": info.get("longName", ticker),
        "sector": info.get("sector"),
        "current_price": _safe_get(info, "currentPrice", 2),

        # Valuation
        "pe_ratio": _safe_get(info, "trailingPE"),
        "forward_pe": _safe_get(info, "forwardPE"),
        "pb_ratio": _safe_get(info, "priceToBook"),
        "eps": _safe_get(info, "trailingEps", 2),

        # Profitability
        "roe": _safe_get(info, "returnOnEquity"),
        "roa": _safe_get(info, "returnOnAssets"),
        "gross_margin": _safe_get(info, "grossMargins"),
        "operating_margin": _safe_get(info, "operatingMargins"),
        "net_margin": _safe_get(info, "profitMargins"),

        # Financial health
        "debt_to_equity": _safe_get(info, "debtToEquity"),
        "free_cash_flow": info.get("freeCashflow"),  # large number, no rounding
        "current_ratio": _safe_get(info, "currentRatio"),
    }

    return fundamentals


if __name__ == "__main__":
    # Quick manual test
    import json
    result = get_fundamentals("AAPL")
    print(json.dumps(result, indent=2))