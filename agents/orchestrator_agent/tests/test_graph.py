import sys

from pathlib import Path

project_root = (
    Path(__file__)
    .resolve()
    .parent.parent.parent.parent
)

sys.path.append(
    str(project_root)
)

from agents.orchestrator_agent.graph import (
    graph
)

result = graph.invoke(
    {
        "query": (
            "Will TSLA stock go up?"
        )
    }
)

print(
    "\nFinal State:"
)

print(result)

if "research_result" in result:

    print(
        "\nResearch Result:\n"
    )

    print(
        result["research_result"]
    )

if "prediction_result" in result:

    print(
        "\nPrediction Result:\n"
    )

    print(
        result["prediction_result"]
    )