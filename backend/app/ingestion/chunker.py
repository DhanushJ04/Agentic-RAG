from langchain_text_splitters import RecursiveCharacterTextSplitter
from app.ingestion.pdf_loader import load_pdfs


def create_chunks(documents):
    """
    Split documents into smaller chunks.
    """

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = text_splitter.split_documents(documents)

    return chunks


if __name__ == "__main__":

    docs = load_pdfs()

    chunks = create_chunks(docs)

    print(f"\nTotal Chunks Created: {len(chunks)}")

    print("\nFirst Chunk:\n")
    print(chunks[0].page_content[:500])

    print("\nChunk Metadata:")
    print(chunks[0].metadata)