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
from rag.loaders.pdf_loader import load_pdf
from rag.loaders.text_chunker import split_text

from rag.embeddings.embedding_generator import (
    generate_embeddings
)

from rag.vectorstore.faiss_store import (
    create_faiss_index,
    save_index
)

from rag.vectorstore.metadata_store import (
    save_metadata
)

from rag.utils.document_metadata import (
    get_company_name,
    get_document_type
)


DOCUMENTS_DIR = (
    Path(__file__)
    .parent.parent
    / "data"
    / "documents"
)


def build_vector_store():

    all_chunks = []

    metadata = []

    chunk_id = 0

    pdf_files = list(
        DOCUMENTS_DIR.glob("*.pdf")
    )

    print(
        f"Found {len(pdf_files)} PDFs"
    )

    for pdf_file in pdf_files:

        print(
            f"Processing {pdf_file.name}"
        )

        text = load_pdf(
            str(pdf_file)
        )

        chunks = split_text(
            text
        )

        for chunk in chunks:

            all_chunks.append(
                chunk
            )

            metadata.append(
                {
                    "chunk_id": chunk_id,
                    "source": pdf_file.name,
                    "company": get_company_name(pdf_file.name),
                    "document_type": get_document_type(pdf_file.name),
                    "text": chunk
                }
            )

            chunk_id += 1

    print(
        f"Total chunks: {len(all_chunks)}"
    )

    embeddings = generate_embeddings(
        all_chunks
    )

    index = create_faiss_index(
        embeddings
    )

    save_index(
        index
    )

    save_metadata(
        metadata
    )

    print(
        "\nVector store built successfully."
    )


if __name__ == "__main__":

    build_vector_store()