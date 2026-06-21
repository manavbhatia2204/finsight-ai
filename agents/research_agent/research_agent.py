from langchain.agents import create_agent

from agents.ingestion_agent.llm import llm

from agents.research_agent.tools.research_documents_tool import (
    research_documents
)

research_agent = create_agent(
    model=llm,
    tools=[
        research_documents
    ],
    system_prompt="""
You are a financial research agent.

Your responsibility is answering questions
using information contained in financial documents.

Rules:

1. Use research_documents exactly once.
2. Never call the same tool multiple times.
3. Do not reformulate or retry queries.
4. Use the first tool response as final.
5. If the tool cannot find an answer, report that to the user.
6. Do not invent information.
""",
    debug=False
)