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
            "What did Apple say about Services revenue?"
        )
    }
)

print(
    "\nFinal State:"
)

print(result)

print(
    "\nFinal Report:\n"
)

print(
    result["final_report"]
)