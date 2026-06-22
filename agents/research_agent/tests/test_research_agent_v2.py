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

from agents.research_agent.research_agent_v2 import (
    ask_research_agent
)

from agents.research_agent.memory.chat_history import (
    chat_history
)

while True:

    question = input(
        "\nQuestion: "
    ).strip()

    if question.lower() == "exit":
        break

    chat_history.append(
        {
            "role": "user",
            "content": question
        }
    )

    answer = ask_research_agent(
        question
    )

    print(
        "\nAnswer:\n"
    )

    print(answer)

    chat_history.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

    print(
        f"\nMemory Length: {len(chat_history)}"
    )