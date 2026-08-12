from typing import TypedDict


class GraphState(
    TypedDict,
    total=False
):
    query: str

    route: str

    ticker: str

    ticker_b: str

    research_result: str

    prediction_result: dict

    financial_metrics_result: str

    risk_analysis_result: str

    comparison_result: str

    off_topic_result: str

    final_report: str