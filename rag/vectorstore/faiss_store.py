from pathlib import Path

import faiss
import numpy as np


INDEX_PATH = (
    Path(__file__).parent
    / "faiss_index.bin"
)


def create_faiss_index(
    embeddings
):
    """
    Create FAISS index.
    """

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(
        dimension
    )

    index.add(
        np.array(
            embeddings,
            dtype=np.float32
        )
    )

    return index


def save_index(
    index
):
    """
    Save index to disk.
    """

    faiss.write_index(
        index,
        str(INDEX_PATH)
    )


def load_index():
    """
    Load index from disk.
    """

    return faiss.read_index(
        str(INDEX_PATH)
    )