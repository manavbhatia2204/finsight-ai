from langchain.tools import tool

from rag.qa.rag_qa import (
    answer_question
)


@tool
def research_documents(
    question: str
) -> str:
    """
    Search financial documents and answer questions
    using the RAG pipeline.

    Use this tool whenever the user asks about:

    - Company financials
    - Annual reports
    - Earnings
    - Risks
    - Revenue
    - AI demand
    - Inflation
    - Federal Reserve policy
    - Information contained in indexed documents
    """

    print(
        "RESEARCH_DOCUMENTS TOOL CALLED"
    )

    return answer_question(
        question
    )