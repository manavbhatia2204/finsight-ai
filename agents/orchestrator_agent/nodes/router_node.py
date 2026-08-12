def router_node(
    state
):
    query = (
        state["query"]
        .upper()
    )

    print(
        "\nRouter Node Executed"
    )

    COMPANY_TO_TICKER = {
        "APPLE": "AAPL",
        "AAPL": "AAPL",

        "MICROSOFT": "MSFT",
        "MSFT": "MSFT",

        "NVIDIA": "NVDA",
        "NVDA": "NVDA",

        "AMAZON": "AMZN",
        "AMZN": "AMZN",

        "GOOGLE": "GOOGL",
        "ALPHABET": "GOOGL",
        "GOOGL": "GOOGL",

        "META": "META",
        "FACEBOOK": "META",

        "TESLA": "TSLA",
        "TSLA": "TSLA"
    }

    found_tickers = []

    for company_name, symbol in (
        COMPANY_TO_TICKER.items()
    ):

        if company_name in query:

            if symbol not in found_tickers:

                found_tickers.append(
                    symbol
                )

    ticker = (
        found_tickers[0]
        if found_tickers
        else None
    )

    ticker_b = (
        found_tickers[1]
        if len(found_tickers) > 1
        else None
    )

    prediction_keywords = [
        "PREDICT",
        "PREDICTION",
        "STOCK",
        "PRICE",
        "UP",
        "DOWN"
    ]

    research_keywords = [
        "ANALYZE",
        "ANALYSIS",
        "RESEARCH",
        "INVESTMENT",
        "GOOD INVESTMENT"
    ]

    financial_metrics_keywords = [
        "P/E",
        "PE RATIO",
        "VALUATION",
        "FUNDAMENTALS",
        "FUNDAMENTAL",
        "MARGIN",
        "PROFITABILITY",
        "GROWTH",
        "REVENUE",
        "EARNINGS",
        "ROE",
        "ROA",
        "DEBT",
        "CAGR"
    ]

    risk_keywords = [
        "RISK",
        "VOLATILITY",
        "VOLATILE",
        "SHARPE",
        "BETA",
        "DRAWDOWN",
        "RISKY",
        "STANDARD DEVIATION"
    ]

    comparison_keywords = [
        "COMPARE",
        "COMPARISON",
        "VS",
        "VERSUS",
        "OR",
        "BETTER",
        "WHICH IS"
    ]

    has_risk = any(
        word in query
        for word in risk_keywords
    )

    has_prediction = any(
        word in query
        for word in prediction_keywords
    )

    has_research = any(
        word in query
        for word in research_keywords
    )

    has_financial_metrics = any(
        word in query
        for word in financial_metrics_keywords
    )

    has_comparison = any(
        word in query
        for word in comparison_keywords
    )

    if ticker_b is not None:
        route = "comparison"

    elif (
        ticker is not None
        and has_research
    ):
        route = "both"

    elif has_risk:
        route = "risk_analysis"

    elif has_financial_metrics:
        route = "financial_metrics"

    elif has_prediction:
        route = "prediction"

    else:
        route = "research"

    print(
        f"Route Selected: {route}"
    )

    print(
        f"Ticker Found: {ticker}"
    )

    print(
        f"Ticker B Found: {ticker_b}"
    )

    return {
        "route": route,
        "ticker": ticker,
        "ticker_b": ticker_b
    }