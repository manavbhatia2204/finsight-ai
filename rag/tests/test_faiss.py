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

from rag.vectorstore.faiss_store import (
    create_faiss_index,
    save_index,
    load_index
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

index = create_faiss_index(
    embeddings
)

save_index(
    index
)

loaded_index = load_index()

print(
    f"Vectors stored: "
    f"{loaded_index.ntotal}"
)