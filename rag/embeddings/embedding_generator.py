from sentence_transformers import (
    SentenceTransformer
)

MODEL_NAME = (
    "sentence-transformers/all-MiniLM-L6-v2"
)

model = SentenceTransformer(
    MODEL_NAME
)


def generate_embeddings(
    chunks: list[str]
):
    """
    Generate embeddings for chunks.
    """

    embeddings = model.encode(
        chunks,
        show_progress_bar=True
    )

    return embeddings