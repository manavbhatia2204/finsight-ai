import numpy as np

from rag.embeddings.embedding_generator import (
    model
)

from rag.vectorstore.faiss_store import (
    load_index
)

from rag.vectorstore.metadata_store import (
    load_metadata
)


def retrieve(
    query: str,
    top_k: int = 5
):
    """
    Retrieve top matching chunks.
    """

    index = load_index()

    metadata = load_metadata()

    query_embedding = model.encode(
        [query]
    )

    distances, indices = index.search(
        np.array(
            query_embedding,
            dtype=np.float32
        ),
        top_k
    )

    results = []

    for idx in indices[0]:

        results.append(
            metadata[idx]
        )

    return results