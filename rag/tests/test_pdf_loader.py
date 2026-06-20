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

from rag.loaders.pdf_loader import (
    load_pdf
)


pdf_path = (
    project_root
    / "rag"
    / "data"
    / "documents"
    / "apple_10k.pdf"
)

text = load_pdf(
    str(pdf_path)
)

print(text[:2000])

print("\n")
print("=" * 50)
print("\n")

print(
    f"Total characters: "
    f"{len(text)}"
)