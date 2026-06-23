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

    ticker = None

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

    for company_name, symbol in (
        COMPANY_TO_TICKER.items()
    ):

        if company_name in query:

            ticker = symbol

            break

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

    has_prediction = any(
        word in query
        for word in prediction_keywords
    )

    has_research = any(
        word in query
        for word in research_keywords
    )

    # Investment-style questions should use both agents
    if (
        ticker is not None
        and has_research
    ):
        route = "both"

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

    return {
        "route": route,
        "ticker": ticker
    }