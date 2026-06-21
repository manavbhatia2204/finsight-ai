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

print("=" * 60)
print("FinSight AI RAG Research Assistant")
print("Type 'exit' to quit.")
print("=" * 60)

while True:

    question = input("\nQuestion: ").strip()

    if question.lower() in [
        "exit",
        "quit",
        "bye"
    ]:
        print("\nGoodbye!")
        break

    if not question:
        print("Please enter a question.")
        continue

    try:

        answer = answer_question(
            question
        )

        print("\n" + "=" * 60)
        print("ANSWER")
        print("=" * 60)
        print(answer)

    except Exception as e:

        print(
            f"\nError: {str(e)}"
        )