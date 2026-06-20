from langchain_text_splitters import (
    RecursiveCharacterTextSplitter
)


def split_text(
    text: str
):
    """
    Split text into chunks.
    """

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=3000,
        chunk_overlap=300
    )

    chunks = splitter.split_text(
        text
    )

    return chunks