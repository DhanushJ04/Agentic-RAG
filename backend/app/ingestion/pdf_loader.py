from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader

from app.utils.config import PDF_DIR


def load_pdfs(pdf_directory: Path = PDF_DIR):
    """
    Load all PDFs from the given directory.

    Returns:
        List of LangChain Document objects
    """

    documents = []

    pdf_path = Path(pdf_directory)

    print(f"\nPDF Directory: {pdf_path.resolve()}")

    if not pdf_path.exists():
        print("PDF directory does not exist!")
        return documents

    pdf_files = list(pdf_path.glob("*.pdf"))

    print(f"PDF Files Found: {len(pdf_files)}")

    for pdf_file in pdf_files:
        print(f"Loading: {pdf_file.name}")

        loader = PyPDFLoader(str(pdf_file))
        docs = loader.load()

        documents.extend(docs)

    print(f"\nPages Loaded: {len(documents)}")

    return documents


if __name__ == "__main__":

    docs = load_pdfs()

    print(f"\nTotal Pages Loaded: {len(docs)}")

    if docs:
        print("\nFirst Page Content:\n")
        print(docs[0].page_content[:500])

        print("\nMetadata:")
        print(docs[0].metadata)