import sys
from pathlib import Path

project_root = (
    Path(__file__)
    .resolve()
    .parent.parent.parent
)

sys.path.append(
    str(project_root)
)

from agents.research_agent.tools.research_documents_tool import (
    research_documents
)

print(
    research_documents.invoke(
        {
            "question":
            "What did Apple say about iPhone revenue?"
        }
    )
)