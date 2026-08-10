# agents/financial_intelligence_agent/risk_metrics.py

import numpy as np
import yfinance as yf
import pandas as pd
from sqlalchemy import text

from api.database.connection import engine

TRADING_DAYS_PER_YEAR = 252


def _get_price_history(ticker: str, lookback_days: int = 365) -> pd.DataFrame:
    """
    Pull historical close prices for a ticker from stock_prices,
    joined against stocks to resolve the ticker symbol.
    Returns a DataFrame sorted by date ascending.
    """
    ticker = ticker.upper()

    query = text("""
        SELECT sp.date, sp.close
        FROM stock_prices sp
        JOIN stocks s ON sp.stock_id = s.id
        WHERE s.ticker = :ticker
        AND sp.date >= NOW() - make_interval(days => :lookback_days)
        ORDER BY sp.date ASC
    """)

    with engine.connect() as conn:
        df = pd.read_sql(query, conn, params={"ticker": ticker, "lookback_days": lookback_days})

    return df


def calculate_volatility(ticker: str, lookback_days: int = 365) -> dict:
    """
    Calculate annualized volatility from daily returns.
    Volatility = standard deviation of daily returns, annualized.
    """
    ticker = ticker.upper()
    df = _get_price_history(ticker, lookback_days)

    if df.empty or len(df) < 30:
        return {
            "ticker": ticker,
            "error": f"Not enough price history for {ticker} to calculate volatility (need at least 30 days)."
        }

    df["daily_return"] = df["close"].pct_change()
    df = df.dropna()

    daily_volatility = df["daily_return"].std()
    annualized_volatility = daily_volatility * np.sqrt(TRADING_DAYS_PER_YEAR)

    return {
        "ticker": ticker,
        "daily_volatility_pct": round(daily_volatility * 100, 2),
        "annualized_volatility_pct": round(annualized_volatility * 100, 2),
        "data_points": len(df),
    }

def calculate_max_drawdown(ticker: str, lookback_days: int = 365) -> dict:
    """
    Calculate maximum drawdown — the largest peak-to-trough decline
    in price over the lookback period.
    """
    ticker = ticker.upper()
    df = _get_price_history(ticker, lookback_days)

    if df.empty or len(df) < 30:
        return {
            "ticker": ticker,
            "error": f"Not enough price history for {ticker} to calculate max drawdown."
        }

    df["running_max"] = df["close"].cummax()
    df["drawdown"] = (df["close"] - df["running_max"]) / df["running_max"]

    max_drawdown_pct = df["drawdown"].min() * 100
    max_drawdown_date = df.loc[df["drawdown"].idxmin(), "date"]

    return {
        "ticker": ticker,
        "max_drawdown_pct": round(max_drawdown_pct, 2),
        "max_drawdown_date": str(max_drawdown_date),
        "data_points": len(df),
    }
def _get_risk_free_rate() -> float:
    """
    Get the latest risk-free rate proxy (Fed Funds Rate) from
    the macro_indicators table. Falls back to a hardcoded estimate
    if no data is available.
    """
    query = text("""
        SELECT value
        FROM macro_indicators
        WHERE indicator_code = 'FEDFUNDS'
        ORDER BY date DESC
        LIMIT 1
    """)

    with engine.connect() as conn:
        result = conn.execute(query).fetchone()

    if result is None:
        return 4.5  # fallback estimate if no data found

    return float(result[0])


def calculate_sharpe_ratio(ticker: str, lookback_days: int = 365) -> dict:
    """
    Calculate the Sharpe ratio — risk-adjusted return.
    Sharpe = (annualized return - risk-free rate) / annualized volatility
    """
    ticker = ticker.upper()
    df = _get_price_history(ticker, lookback_days)

    if df.empty or len(df) < 30:
        return {
            "ticker": ticker,
            "error": f"Not enough price history for {ticker} to calculate Sharpe ratio."
        }

    df["daily_return"] = df["close"].pct_change()
    df = df.dropna()

    mean_daily_return = df["daily_return"].mean()
    annualized_return = mean_daily_return * TRADING_DAYS_PER_YEAR

    daily_volatility = df["daily_return"].std()
    annualized_volatility = daily_volatility * np.sqrt(TRADING_DAYS_PER_YEAR)

    risk_free_rate_pct = _get_risk_free_rate()
    risk_free_rate = risk_free_rate_pct / 100  # convert from % to decimal

    if annualized_volatility == 0:
        return {
            "ticker": ticker,
            "error": "Volatility is zero, cannot calculate Sharpe ratio."
        }

    sharpe_ratio = (annualized_return - risk_free_rate) / annualized_volatility

    return {
        "ticker": ticker,
        "sharpe_ratio": round(sharpe_ratio, 2),
        "annualized_return_pct": round(annualized_return * 100, 2),
        "risk_free_rate_pct": round(risk_free_rate_pct, 2),
        "data_points": len(df),
    }

def calculate_beta(ticker: str, lookback_days: int = 365) -> dict:
    """
    Calculate beta — how much the stock moves relative to the market (S&P 500).
    Beta > 1: more volatile than market. Beta < 1: less volatile.
    """
    ticker = ticker.upper()
    stock_df = _get_price_history(ticker, lookback_days)

    if stock_df.empty or len(stock_df) < 30:
        return {
            "ticker": ticker,
            "error": f"Not enough price history for {ticker} to calculate beta."
        }

    # Pull S&P 500 data live via yfinance for the same period
    try:
        spy = yf.Ticker("SPY")
        spy_history = spy.history(period=f"{lookback_days}d")
        spy_df = spy_history.reset_index()[["Date", "Close"]]
        spy_df.columns = ["date", "close"]
        spy_df["date"] = pd.to_datetime(spy_df["date"]).dt.tz_localize(None).dt.date
    except Exception as e:
        return {
            "ticker": ticker,
            "error": f"Failed to fetch S&P 500 benchmark data: {str(e)}"
        }

    stock_df["date"] = pd.to_datetime(stock_df["date"]).dt.date

    # Merge on date so we're comparing the same trading days
    merged = pd.merge(stock_df, spy_df, on="date", suffixes=("_stock", "_market"))

    if len(merged) < 30:
        return {
            "ticker": ticker,
            "error": "Not enough overlapping trading days between stock and market data."
        }

    merged["stock_return"] = merged["close_stock"].pct_change()
    merged["market_return"] = merged["close_market"].pct_change()
    merged = merged.dropna()

    covariance = merged["stock_return"].cov(merged["market_return"])
    market_variance = merged["market_return"].var()

    if market_variance == 0:
        return {
            "ticker": ticker,
            "error": "Market variance is zero, cannot calculate beta."
        }

    beta = covariance / market_variance

    return {
        "ticker": ticker,
        "beta": round(beta, 2),
        "benchmark": "SPY (S&P 500)",
        "overlapping_data_points": len(merged),
    }
def get_risk_metrics(ticker: str, lookback_days: int = 365) -> dict:
    """
    Combine all risk metrics into a single result for a ticker.
    """
    ticker = ticker.upper()

    volatility = calculate_volatility(ticker, lookback_days)
    drawdown = calculate_max_drawdown(ticker, lookback_days)
    sharpe = calculate_sharpe_ratio(ticker, lookback_days)
    beta = calculate_beta(ticker, lookback_days)

    return {
        "ticker": ticker,
        "volatility": volatility,
        "max_drawdown": drawdown,
        "sharpe_ratio": sharpe,
        "beta": beta,
    }
if __name__ == "__main__":
    import json
    print("Combined Risk Metrics:")
    print(json.dumps(get_risk_metrics("AAPL"), indent=2))