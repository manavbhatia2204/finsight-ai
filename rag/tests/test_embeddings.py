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

from rag.embeddings.embedding_generator import (
    generate_embeddings
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

embeddings = generate_embeddings(
    chunks
)

print(
    f"Chunks: {len(chunks)}"
)

print(
    f"Embedding shape: "
    f"{embeddings.shape}"
)

print(
    f"Single vector length: "
    f"{len(embeddings[0])}"
)