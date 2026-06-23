from typing import TypedDict


class GraphState(
    TypedDict,
    total=False
):
    query: str

    route: str

    ticker: str

    research_result: str

    prediction_result: dict

    final_report: str