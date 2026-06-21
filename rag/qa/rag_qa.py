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

from agents.ingestion_agent.llm import llm

from rag.retrieval.retriever import (
    retrieve
)


def answer_question(
    question: str
) -> str:
    """
    Retrieve relevant document chunks and generate
    an answer using only the retrieved context.
    """

    results = retrieve(
        question,
        top_k=5
    )

    if not results:

        return (
            "I could not find any relevant "
            "information for that question."
        )

    context = "\n\n".join(
        [
            result["text"]
            for result in results
        ]
    )

    prompt = f"""
You are a financial research assistant.

IMPORTANT RULES:

1. Answer ONLY using the provided context.
2. Do NOT make up information.
3. If the answer is not contained in the context,
   say:
   "I could not find the answer in the provided documents."
4. Be concise and factual.
5. When possible, include key figures, percentages,
   dates, and financial metrics.

Question:
{question}

Context:
{context}
"""

    response = llm.invoke(
        prompt
    )

    sources = []

    for result in results:

        source_text = (
            f"- {result['source']} "
            f"(Chunk {result['chunk_id']})"
        )

        if source_text not in sources:

            sources.append(
                source_text
            )

    final_answer = (
        f"{response.content}\n\n"
        f"Sources:\n"
        f"{chr(10).join(sources)}"
    )

    return final_answer