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

from rag.vectorstore.metadata_store import (
    save_metadata
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

metadata = []

for i, chunk in enumerate(chunks):

    metadata.append(
        {
            "chunk_id": i,
            "source": "apple_10k.pdf",
            "text": chunk
        }
    )

save_metadata(
    metadata
)

print(
    f"Metadata records: {len(metadata)}"
)

print(
    metadata[0]["source"]
)

print(
    metadata[0]["chunk_id"]
)