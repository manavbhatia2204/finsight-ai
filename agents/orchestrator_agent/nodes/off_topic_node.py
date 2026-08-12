def off_topic_node(
    state
):
    print(
        "\nOff Topic Node Executed"
    )

    message = (
        "I'm FinSight AI, a specialized financial intelligence "
        "assistant. I can help with stock analysis, company "
        "fundamentals, risk metrics, comparisons, price predictions, "
        "and research from financial documents. Please rephrase your "
        "question in a financial context, or ask about one of the "
        "supported companies: Apple, Microsoft, NVIDIA, Amazon, "
        "Google, Meta, or Tesla."
    )

    return {
        "off_topic_result": message
    }