from agents.orchestrator_agent.graph import (
    graph
)


def run_orchestrator(
    query: str
) -> str:
    """
    Main entry point for the FinSight
    orchestration layer.
    """

    result = graph.invoke(
        {
            "query": query
        }
    )

    return result[
        "final_report"
    ]