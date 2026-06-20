import sys
from pathlib import Path

project_root = (
    Path(__file__)
    .resolve()
    .parent.parent.parent
)

sys.path.append(
    str(project_root)
)

from rag.qa.rag_qa import (
    answer_question
)

print(
    "FinSight AI RAG QA"
)

print(
    "Type exit to quit"
)

while True:

    question = input(
        "\nQuestion: "
    )

    if question.lower() in [
        "exit",
        "quit"
    ]:
        break

    answer = answer_question(
        question
    )

    print(
        "\nAnswer:\n"
    )

    print(answer)