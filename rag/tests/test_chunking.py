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

from rag.loaders.text_chunker import (
    split_text
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

chunks = split_text(
    text
)

print(
    f"Total chunks: {len(chunks)}"
)

print("\nFIRST CHUNK:\n")

print(
    chunks[0][:1000]
)

print("\n")

print(
    f"Chunk length: {len(chunks[0])}"
)