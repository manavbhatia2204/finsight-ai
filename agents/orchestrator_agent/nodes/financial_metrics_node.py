from agents.financial_intelligence_agent.tool import (
    get_financial_metrics
)


def financial_metrics_node(
    state
):
    print(
        "\nFinancial Metrics Node Executed"
    )

    ticker = state.get(
        "ticker"
    )

    if ticker is None:

        return {
            "financial_metrics_result": {
                "error": (
                    "Unsupported company or ticker."
                )
            }
        }

    try:

        result = get_financial_metrics.invoke(
            {
                "ticker": ticker
            }
        )

        return {
            "financial_metrics_result": result
        }

    except Exception as e:

        return {
            "financial_metrics_result": {
                "error": str(e)
            }
        }