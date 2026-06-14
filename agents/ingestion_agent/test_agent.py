import sys
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent.parent
sys.path.append(str(project_root))

from agents.ingestion_agent.agent import agent

response = agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": "How many stocks are currently stored in the database?"
            }
        ]
    }
)

print("\nFinal Answer:")
print(response["messages"][-1].content)