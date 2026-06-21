import sys
from pathlib import Path

project_root = (
    Path(__file__)
    .resolve()
    .parent.parent.parent.parent
)

sys.path.append(
    str(project_root)
)

from agents.research_agent.research_agent import (
    research_agent
)

from agents.research_agent.memory.chat_history import (
    chat_history
)

print("FinSight AI Research Agent")
print("Type 'exit' to quit.")

while True:

    query = input("\nQuestion: ").strip()

    if query.lower() in [
        "exit",
        "quit"
    ]:
        print("\nGoodbye!")
        break

    if not query:
        print("Please enter a question.")
        continue

    try:

        # Store user message in memory
        chat_history.append(
            {
                "role": "user",
                "content": query
            }
        )

        # Send ONLY current question to agent
        response = research_agent.invoke(
            {
                "messages": [
                    {
                        "role": "user",
                        "content": query
                    }
                ]
            }
        )

        answer = response["messages"][-1].content

        print("\nAnswer:\n")
        print(answer)

        # Store assistant response in memory
        chat_history.append(
            {
                "role": "assistant",
                "content": answer
            }
        )

        print(
            f"\nMemory Length: {len(chat_history)}"
        )

    except Exception as e:

        print(
            f"\nError: {str(e)}"
        )