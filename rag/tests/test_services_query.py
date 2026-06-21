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

from rag.qa.rag_qa import (
    answer_question
)

print(
    answer_question(
        "Apple Services revenue"
    )
)