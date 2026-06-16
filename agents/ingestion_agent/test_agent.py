import sys
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent.parent
sys.path.append(str(project_root))

from agents.ingestion_agent.agent import agent

while True:

    question = input("\nYou: ")

    if question.lower() in ["exit", "quit"]:
        break

    response = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": question
                }
            ]
        }
    )

    print(
        "\nFinSight AI:\n"
    )

    print(
        response["messages"][-1].content
    )