import sys
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent.parent
sys.path.append(str(project_root))

from agents.ingestion_agent.ingestion_agent import (
    ingestion_agent
)

print("FinSight AI Ingestion Agent")
print("Type 'exit' to quit.")

while True:

    user_input = input("\nYou: ")

    if user_input.lower() in ["exit", "quit", "bye"]:
        print("\nFinSight AI: Goodbye!")
        break

    response = ingestion_agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": user_input
                }
            ]
        }
    )

    print("\nFinSight AI:\n")

    messages = response["messages"]

    if len(messages) > 0:
        #print(messages[-1].content)
        from pprint import pprint

        pprint(response)
    else:
        print("No response received.")