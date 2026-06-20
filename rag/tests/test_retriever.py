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

from rag.retrieval.retriever import (
    retrieve
)

print("FinSight AI RAG Retriever")
print("Type 'exit' to quit.")

while True:

    query = input("\nQuery: ")

    if query.lower() in [
        "exit",
        "quit",
        "bye"
    ]:
        print("\nGoodbye!")
        break

    results = retrieve(
        query,
        top_k=3
    )

    for i, result in enumerate(
        results,
        start=1
    ):

        print("\n" + "=" * 80)

        print(
            f"\nResult {i}"
        )

        print(
            f"\nSource: "
            f"{result['source']}"
        )

        print(
            f"\nChunk ID: "
            f"{result['chunk_id']}"
        )

        print(
            "\nText Preview:\n"
        )

        print(
            result["text"][:1500]
        )