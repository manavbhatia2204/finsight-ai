import sys
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent.parent
sys.path.append(str(project_root))

from agents.ingestion_agent.ingestion_agent import (
    ingestion_agent
)

response = ingestion_agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": "Fetch Apple stock data"
            }
        ]
    },
    {
        "recursion_limit": 3
    }
)

print(response)