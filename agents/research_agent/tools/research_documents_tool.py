from langchain.tools import tool

from rag.qa.rag_qa import (
    answer_question
)

from rag.qa.question_rewriter import (
    rewrite_question
)

from agents.research_agent.memory.chat_history import (
    chat_history
)


@tool
def research_documents(
    question: str
) -> str:
    """
    Search indexed financial documents.

    Args:
        question: User question.

    Returns:
        Answer from retrieved documents.
    """

    rewritten_question = rewrite_question(
        chat_history,
        question
    )

    

    return answer_question(
        rewritten_question
    )