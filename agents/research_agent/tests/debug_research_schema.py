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

from agents.research_agent.tools.research_documents_tool import (
    research_documents
)

print("\nTOOL NAME:\n")
print(
    research_documents.name
)

print("\nTOOL DESCRIPTION:\n")
print(
    research_documents.description
)

print("\nTOOL ARGS:\n")
print(
    research_documents.args
)