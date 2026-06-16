# test_fetch_agent_debug.py

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
                "content": "Fetch Apple stock data"
            }
        ]
    },
    {
        "recursion_limit": 2
    }
)

print(response)