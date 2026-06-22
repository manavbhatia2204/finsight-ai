from agents.research_agent.tools.research_documents_tool import (
    research_documents
)


def ask_research_agent(
    question: str
) -> str:

    return research_documents.invoke(
        {
            "question": question
        }
    )