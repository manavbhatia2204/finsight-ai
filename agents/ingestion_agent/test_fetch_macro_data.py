import sys
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent.parent
sys.path.append(str(project_root))

from langchain.agents import create_agent

from agents.ingestion_agent.llm import llm
from agents.ingestion_agent.tools.fetch_macro_data_tool import (
    fetch_macro_data
)

agent = create_agent(
    model=llm,
    tools=[
        fetch_macro_data
    ]
)

response = agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": "Fetch unemployment data"
            }
        ]
    }
)

print(response)