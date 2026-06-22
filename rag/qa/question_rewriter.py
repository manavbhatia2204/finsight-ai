from agents.ingestion_agent.llm import llm


def rewrite_question(
    chat_history,
    question
) -> str:
    """
    Convert follow-up questions into
    standalone questions.
    """

    if not chat_history:
        return question

    history_text = "\n".join(
        [
            f"{msg['role']}: {msg['content']}"
            for msg in chat_history[-6:]
        ]
    )

    prompt = f"""
You are a retrieval query rewriter.

Conversation History:
{history_text}

Current Question:
{question}

Rewrite the question into a short standalone search query.

Rules:
1. Preserve company names and financial terms.
2. Do not add explanations.
3. Do not use phrases like:
   - "statement regarding"
   - "revenue generated from"
   - "according to"
4. Keep the query under 10 words.
5. Return only the rewritten query.
6. If the current question already contains a company name,
   return it unchanged.

Examples:

Apple iPhone revenue
Apple Mac revenue
Federal Reserve inflation target
Microsoft cloud revenue
Nvidia AI demand
"""
    


    response = llm.invoke(
        prompt
    )

    return response.content.strip()