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

from rag.qa.question_rewriter import (
    rewrite_question
)

history = [
    {
        "role": "user",
        "content":
        "What did Apple say about iPhone revenue?"
    }
]

question = "What about Mac?"

print(
    rewrite_question(
        history,
        question
    )
)