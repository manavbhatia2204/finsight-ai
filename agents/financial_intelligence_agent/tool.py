# agents/financial_intelligence_agent/tool.py

from langchain.tools import tool
from agents.financial_intelligence_agent.fundamentals import get_fundamentals
from agents.financial_intelligence_agent.growth_metrics import calculate_growth_metrics


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


if __name__ == "__main__":
    for test_ticker in ["MSFT", "NVDA", "TSLA", "GOOGL"]:
        print(f"\n{'='*60}")
        result = get_financial_metrics.invoke({"ticker": test_ticker})
        print(result)