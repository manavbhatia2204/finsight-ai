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
):
    results = retrieve(
        question,
        top_k=3
    )

    context = "\n\n".join(
        [
            result["text"]
            for result in results
        ]
    )

    prompt = f"""
You are a financial research assistant.

Answer ONLY using the provided context.

If the answer is not contained in the context,
say you could not find the answer.

Question:
{question}

Context:
{context}
"""

    response = llm.invoke(
        prompt
    )

    return response.content