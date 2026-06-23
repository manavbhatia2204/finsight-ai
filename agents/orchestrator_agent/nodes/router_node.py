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

    supported_tickers = [
        "AAPL",
        "MSFT",
        "NVDA",
        "AMZN",
        "GOOGL",
        "META",
        "TSLA"
    ]

    for symbol in supported_tickers:

        if symbol in query:

            ticker = symbol

            break

    if any(
        word in query
        for word in [
            "PREDICT",
            "PREDICTION",
            "STOCK",
            "PRICE",
            "UP",
            "DOWN"
        ]
    ):

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