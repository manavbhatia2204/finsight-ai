# agents/financial_intelligence_agent/tool.py

from langchain.tools import tool
from agents.financial_intelligence_agent.fundamentals import get_fundamentals
from agents.financial_intelligence_agent.growth_metrics import calculate_growth_metrics
from agents.financial_intelligence_agent.risk_metrics import get_risk_metrics
from agents.financial_intelligence_agent.comparison import compare_companies, format_comparison

def _format_pct(value, is_ratio=True) -> str:
    """Format a number as a percentage string, handling None."""
    if value is None:
        return "N/A"
    if is_ratio:
        return f"{value * 100:.2f}%"
    return f"{value:.2f}%"


@tool(return_direct=True)
def get_financial_metrics(ticker: str) -> str:
    """
    Get fundamental financial metrics and growth data for a stock ticker.
    Use this when the user asks about a company's valuation (P/E, P/B),
    profitability (margins, ROE, ROA), financial health (debt/equity),
    or growth (revenue growth, earnings growth, CAGR).
    
    Example queries this tool answers:
    - "What is Apple's P/E ratio?"
    - "How profitable is Microsoft?"
    - "What is NVIDIA's revenue growth?"
    """
    ticker = ticker.upper()

    fundamentals = get_fundamentals(ticker)
    if "error" in fundamentals:
        return f"DONE: {fundamentals['error']}"

    growth = calculate_growth_metrics(ticker)

    report = f"""DONE: Financial metrics for {fundamentals['company_name']} ({ticker})

**Valuation**
- Current Price: ${fundamentals.get('current_price', 'N/A')}
- P/E Ratio: {fundamentals.get('pe_ratio', 'N/A')}
- Forward P/E: {fundamentals.get('forward_pe', 'N/A')}
- P/B Ratio: {fundamentals.get('pb_ratio', 'N/A')}
- EPS: {fundamentals.get('eps', 'N/A')}

**Profitability**
- ROE: {_format_pct(fundamentals.get('roe'))}
- ROA: {_format_pct(fundamentals.get('roa'))}
- Gross Margin: {_format_pct(fundamentals.get('gross_margin'))}
- Operating Margin: {_format_pct(fundamentals.get('operating_margin'))}
- Net Margin: {_format_pct(fundamentals.get('net_margin'))}

**Financial Health**
- Debt/Equity: {fundamentals.get('debt_to_equity', 'N/A')}
- Current Ratio: {fundamentals.get('current_ratio', 'N/A')}
- Free Cash Flow: ${fundamentals.get('free_cash_flow', 'N/A'):,} 

**Growth**
- Revenue Growth (YoY): {growth.get('revenue_growth_yoy_pct', 'N/A')}%
- Earnings Growth (YoY): {growth.get('earnings_growth_yoy_pct', 'N/A')}%
- Revenue CAGR ({growth.get('period_years', '?')}yr): {growth.get('revenue_cagr_pct', 'N/A')}%
"""
    return report

@tool(return_direct=True)
def get_risk_analysis(ticker: str) -> str:
    """
    Get risk analysis for a stock ticker, including volatility,
    maximum drawdown, Sharpe ratio, and beta relative to the S&P 500.
    Use this when the user asks about a stock's risk, volatility,
    how risky an investment is, or how it compares to the market.
    
    Example queries this tool answers:
    - "What is Tesla's volatility?"
    - "How risky is NVIDIA as an investment?"
    - "What is Apple's beta?"
    - "What is Microsoft's Sharpe ratio?"
    """
    ticker = ticker.upper()
    metrics = get_risk_metrics(ticker)

    vol = metrics["volatility"]
    dd = metrics["max_drawdown"]
    sharpe = metrics["sharpe_ratio"]
    beta = metrics["beta"]

    # Check if any sub-metric failed
    if "error" in vol:
        return f"DONE: {vol['error']}"

    report = f"""DONE: Risk Analysis for {ticker}

**Volatility**
- Annualized Volatility: {vol.get('annualized_volatility_pct', 'N/A')}%

**Drawdown**
- Maximum Drawdown: {dd.get('max_drawdown_pct', 'N/A')}% (on {dd.get('max_drawdown_date', 'N/A')})

**Risk-Adjusted Return**
- Sharpe Ratio: {sharpe.get('sharpe_ratio', 'N/A')}
- Annualized Return: {sharpe.get('annualized_return_pct', 'N/A')}%
- Risk-Free Rate Used: {sharpe.get('risk_free_rate_pct', 'N/A')}%

**Market Sensitivity**
- Beta (vs S&P 500): {beta.get('beta', 'N/A')}
"""
    return report


if __name__ == "__main__":
    result = get_risk_analysis.invoke({"ticker": "AAPL"})
    print(result)
if __name__ == "__main__":
    for test_ticker in ["MSFT", "NVDA", "TSLA", "GOOGL"]:
        print(f"\n{'='*60}")
        result = get_financial_metrics.invoke({"ticker": test_ticker})
        print(result)

@tool(return_direct=True)
def compare_stocks(ticker_a: str, ticker_b: str) -> str:
    """
    Compare two stocks side by side using fundamentals and risk metrics.
    Use this when the user asks to compare two companies, or asks
    which of two stocks is better on valuation, profitability, or risk.
    
    Example queries this tool answers:
    - "Compare Apple and Microsoft"
    - "Tesla vs NVIDIA, which is riskier?"
    - "Should I buy Google or Amazon?"
    """
    data = compare_companies(ticker_a, ticker_b)
    return format_comparison(data)


if __name__ == "__main__":
    result = compare_stocks.invoke({"ticker_a": "TSLA", "ticker_b": "NVDA"})
    print(result)