from agents.financial_intelligence_agent.tool import (
    get_risk_analysis
)


def risk_analysis_node(
    state
):
    print(
        "\nRisk Analysis Node Executed"
    )

    ticker = state.get(
        "ticker"
    )

    if ticker is None:

        return {
            "risk_analysis_result": {
                "error": (
                    "Unsupported company or ticker."
                )
            }
        }

    try:

        result = get_risk_analysis.invoke(
            {
                "ticker": ticker
            }
        )

        return {
            "risk_analysis_result": result
        }

    except Exception as e:

        return {
            "risk_analysis_result": {
                "error": str(e)
            }
        }