import sys
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent.parent
sys.path.append(str(project_root))

from langchain.agents import create_agent
from agents.ingestion_agent.llm import llm
from agents.ingestion_agent.tools.macro_tool import (
    get_latest_macro_indicator
)

agent = create_agent(
    model=llm,
    tools=[get_latest_macro_indicator]
)

response = agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": "What is the current unemployment rate?"
            }
        ]
    }
)

print(response)