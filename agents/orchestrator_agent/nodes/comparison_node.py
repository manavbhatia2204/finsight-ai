from agents.financial_intelligence_agent.tool import (
    compare_stocks
)


def comparison_node(
    state
):
    print(
        "\nComparison Node Executed"
    )

    ticker_a = state.get(
        "ticker"
    )

    ticker_b = state.get(
        "ticker_b"
    )

    if (
        ticker_a is None
        or ticker_b is None
    ):

        return {
            "comparison_result": {
                "error": (
                    "Could not identify two companies to compare."
                )
            }
        }

    try:

        result = compare_stocks.invoke(
            {
                "ticker_a": ticker_a,
                "ticker_b": ticker_b
            }
        )

        return {
            "comparison_result": result
        }

    except Exception as e:

        return {
            "comparison_result": {
                "error": str(e)
            }
        }