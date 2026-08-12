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
def format_comparison(comparison_data: dict) -> str:
    """
    Format the raw comparison data into a clean, readable side-by-side report.
    """
    ticker_a = comparison_data["ticker_a"]
    ticker_b = comparison_data["ticker_b"]

    fa = comparison_data["fundamentals_a"]
    fb = comparison_data["fundamentals_b"]

    ra = comparison_data["risk_a"]
    rb = comparison_data["risk_b"]

    if "error" in fa or "error" in fb:
        return f"DONE: Could not complete comparison. Check that both tickers are valid."

    def pct(val):
        return f"{val * 100:.2f}%" if val is not None else "N/A"

    def num(val):
        return f"{val}" if val is not None else "N/A"

    report = f"""DONE: Comparison: {fa['company_name']} ({ticker_a}) vs {fb['company_name']} ({ticker_b})

**Valuation**
                    {ticker_a:<12}{ticker_b:<12}
P/E Ratio           {num(fa.get('pe_ratio')):<12}{num(fb.get('pe_ratio')):<12}
Forward P/E         {num(fa.get('forward_pe')):<12}{num(fb.get('forward_pe')):<12}
P/B Ratio           {num(fa.get('pb_ratio')):<12}{num(fb.get('pb_ratio')):<12}

**Profitability**
                    {ticker_a:<12}{ticker_b:<12}
ROE                 {pct(fa.get('roe')):<12}{pct(fb.get('roe')):<12}
Gross Margin        {pct(fa.get('gross_margin')):<12}{pct(fb.get('gross_margin')):<12}
Net Margin          {pct(fa.get('net_margin')):<12}{pct(fb.get('net_margin')):<12}

**Risk Profile**
                    {ticker_a:<12}{ticker_b:<12}
Volatility (ann.)   {num(ra['volatility'].get('annualized_volatility_pct'))}%{'':<7}{num(rb['volatility'].get('annualized_volatility_pct'))}%
Max Drawdown        {num(ra['max_drawdown'].get('max_drawdown_pct'))}%{'':<7}{num(rb['max_drawdown'].get('max_drawdown_pct'))}%
Sharpe Ratio        {num(ra['sharpe_ratio'].get('sharpe_ratio')):<12}{num(rb['sharpe_ratio'].get('sharpe_ratio')):<12}
Beta                {num(ra['beta'].get('beta')):<12}{num(rb['beta'].get('beta')):<12}
"""
    return report


if __name__ == "__main__":
    data = compare_companies("AAPL", "MSFT")
    print(format_comparison(data))