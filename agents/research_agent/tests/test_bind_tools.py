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

from agents.ingestion_agent.llm import llm

from agents.research_agent.tools.research_documents_tool import (
    research_documents
)

llm_with_tools = llm.bind_tools(
    [research_documents]
)

response = llm_with_tools.invoke(
    "What did Apple say about Services revenue?"
)

print("\nCONTENT:")
print(response.content)

print("\nTOOL CALLS:")
print(response.tool_calls)