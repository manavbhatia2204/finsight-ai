import sys
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent.parent
sys.path.append(str(project_root))

from langchain.agents import create_agent

from agents.ingestion_agent.llm import llm
from agents.ingestion_agent.tools.stock_tool import (
    get_stock_price
)

agent = create_agent(
    model=llm,
    tools=[get_stock_price]
)

response = agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": "What is Apple's latest stock price?"
            }
        ]
    }
)

print(response)