import os
import sys
from pathlib import Path

from dotenv import load_dotenv
from langchain_groq import ChatGroq

project_root = (
    Path(__file__)
    .resolve()
    .parent.parent.parent
)

sys.path.append(
    str(project_root)
)

load_dotenv(
    project_root / ".env"
)

from rag.retrieval.retriever import (
    retrieve
)

qa_llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0
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
2. If relevant financial figures appear in the context,
   extract and report them.
3. Do NOT ignore tables or financial data.
4. Do NOT say the answer is unavailable if relevant
   information exists in the context.
5. If the answer truly does not exist in the context,
   say:
   "I could not find the answer in the provided documents."
6. Be concise and factual.
7. Include key figures, percentages, dates, and
   financial metrics whenever available.

Question:
{question}

Context:
{context}
"""

    response = qa_llm.invoke(
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