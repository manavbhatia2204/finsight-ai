from pathlib import Path
import sys

project_root = (
    Path(__file__)
    .resolve()
    .parents[3]
)

sys.path.append(
    str(project_root)
)

from agents.orchestrator_agent.orchestrator_agent import (
    run_orchestrator
)

result = run_orchestrator(
    "Will TSLA stock go up?"
)

print(
    "\nOrchestrator Result\n"
)

print(result)