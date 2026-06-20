from pathlib import Path

from pypdf import PdfReader


def load_pdf(
    pdf_path: str
) -> str:
    """
    Load a PDF and return all text.
    """

    reader = PdfReader(pdf_path)

    text = []

    for page in reader.pages:

        page_text = page.extract_text()

        if page_text:
            text.append(page_text)

    return "\n".join(text)


if __name__ == "__main__":

    pdf_file = (
        Path(__file__)
        .parent.parent
        / "data"
        / "documents"
        / "apple_10k.pdf"
    )

    document_text = load_pdf(
        str(pdf_file)
    )

    print(document_text[:2000])

    print("\n")
    print("=" * 50)
    print("\n")

    print(
        f"Total characters: "
        f"{len(document_text)}"
    )