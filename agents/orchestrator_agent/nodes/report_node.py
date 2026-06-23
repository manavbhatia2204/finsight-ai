def report_node(
    state
):
    print(
        "\nReport Node Executed"
    )

    research_result = state.get(
        "research_result"
    )

    prediction_result = state.get(
        "prediction_result"
    )

    # RESEARCH ERROR
    if (
        isinstance(
            research_result,
            dict
        )
        and "error" in research_result
    ):
        return {
            "final_report":
            (
                "Research Error\n\n"
                f"{research_result['error']}"
            )
        }

    # PREDICTION ERROR
    if (
        prediction_result
        and isinstance(
            prediction_result,
            dict
        )
        and "error" in prediction_result
    ):
        return {
            "final_report":
            (
                "Prediction Error\n\n"
                f"{prediction_result['error']}"
            )
        }

    # BOTH AGENTS
    if (
        research_result
        and prediction_result
    ):
        report = (
            "Investment Analysis Report\n\n"
            "Research Findings\n"
            "-------------------\n"
            f"{research_result}\n\n"
            "Prediction Findings\n"
            "-------------------\n"
            f"Ticker: "
            f"{prediction_result['ticker']}\n"
            f"Direction: "
            f"{prediction_result['prediction']}\n"
            f"Confidence UP: "
            f"{prediction_result['confidence_up']}%\n"
            f"Confidence DOWN: "
            f"{prediction_result['confidence_down']}%"
        )

    # RESEARCH ONLY
    elif research_result:

        report = research_result

    # PREDICTION ONLY
    elif prediction_result:

        report = (
            "Prediction Report\n\n"
            f"Ticker: "
            f"{prediction_result['ticker']}\n"
            f"Direction: "
            f"{prediction_result['prediction']}\n"
            f"Confidence UP: "
            f"{prediction_result['confidence_up']}%\n"
            f"Confidence DOWN: "
            f"{prediction_result['confidence_down']}%"
        )

    else:

        report = (
            "No report available."
        )

    return {
        "final_report": report
    }