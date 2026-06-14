import sys
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent.parent
sys.path.append(str(project_root))

from agents.ingestion_agent.llm import llm

response = llm.invoke(
    "What is FinSight AI in one sentence?"
)

print("\nResponse:")
print(response.content)