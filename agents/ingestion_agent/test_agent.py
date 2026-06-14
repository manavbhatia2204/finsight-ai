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
                "content": "What is Apple's latest stock price and what is the latest CPI value?"
            }
        ]
    }
)

print("\nFinal Answer:")
print(response["messages"][-1].content)