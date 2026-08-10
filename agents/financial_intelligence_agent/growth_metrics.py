# agents/financial_intelligence_agent/growth_metrics.py

import math
import yfinance as yf
from typing import Optional


def _safe_pct_change(new, old) -> Optional[float]:
    """Calculate percentage change, guarding against zero/None/NaN."""
    if old is None or new is None or old == 0:
        return None
    if isinstance(old, float) and math.isnan(old):
        return None
    if isinstance(new, float) and math.isnan(new):
        return None
    try:
        return round(((new - old) / abs(old)) * 100, 2)
    except (TypeError, ZeroDivisionError):
        return None


def calculate_growth_metrics(ticker: str) -> dict:
    """
    Calculate YoY revenue growth, YoY earnings growth, and CAGR
    using yfinance's annual financial statements.
    """
    ticker = ticker.upper()
    stock = yf.Ticker(ticker)

    try:
        financials = stock.financials  # annual income statement
        if financials.empty or financials.shape[1] < 2:
            return {
                "ticker": ticker,
                "error": "Not enough historical data for growth calculation."
            }

        # Columns are years, most recent first
        years = financials.columns
        latest_year = years[0]
        prior_year = years[1]

        # Revenue growth YoY
        revenue_latest = financials.loc["Total Revenue", latest_year] \
            if "Total Revenue" in financials.index else None
        revenue_prior = financials.loc["Total Revenue", prior_year] \
            if "Total Revenue" in financials.index else None
        revenue_growth_yoy = _safe_pct_change(revenue_latest, revenue_prior)

        # Net income growth YoY
        income_latest = financials.loc["Net Income", latest_year] \
            if "Net Income" in financials.index else None
        income_prior = financials.loc["Net Income", prior_year] \
            if "Net Income" in financials.index else None
        earnings_growth_yoy = _safe_pct_change(income_latest, income_prior)

        # CAGR — find the oldest year that actually has valid revenue data
        # (yfinance sometimes returns NaN for the oldest column)
        revenue_oldest = None
        oldest_year = None
        for year in reversed(years):  # walk from oldest to newest
            val = financials.loc["Total Revenue", year] if "Total Revenue" in financials.index else None
            if val is not None and not (isinstance(val, float) and math.isnan(val)):
                revenue_oldest = val
                oldest_year = year
                break

        num_years = None
        cagr = None
        if oldest_year is not None:
            num_years = list(years).index(oldest_year)  # how many years back
            if revenue_latest and revenue_oldest and revenue_oldest > 0 and num_years > 0:
                cagr = round((((revenue_latest / revenue_oldest) ** (1 / num_years)) - 1) * 100, 2)

        return {
            "ticker": ticker,
            "revenue_growth_yoy_pct": revenue_growth_yoy,
            "earnings_growth_yoy_pct": earnings_growth_yoy,
            "revenue_cagr_pct": cagr,
            "period_years": num_years,
            "latest_year": str(latest_year.date()) if hasattr(latest_year, "date") else str(latest_year),
        }

    except Exception as e:
        return {
            "ticker": ticker,
            "error": f"Error calculating growth metrics: {str(e)}"
        }


if __name__ == "__main__":
    import json
    result = calculate_growth_metrics("AAPL")
    print(json.dumps(result, indent=2))