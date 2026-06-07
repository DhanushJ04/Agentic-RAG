from langchain_chroma import Chroma

from app.ingestion.embeddings import get_embedding_model
from app.ingestion.chunker import create_chunks
from app.ingestion.pdf_loader import load_pdfs
from app.utils.config import PDF_DIR, VECTOR_DB_DIR


def create_vector_store():

    print("Loading PDFs...")
    docs = load_pdfs(PDF_DIR)

    print("\nCreating Chunks...")
    chunks = create_chunks(docs)

    print(f"Total Chunks: {len(chunks)}")

    embedding_model = get_embedding_model()

    print("\nCreating ChromaDB...")

    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
        persist_directory=str(VECTOR_DB_DIR)
    )

    print("\nVector Store Created Successfully")

    return vector_store


if __name__ == "__main__":
    create_vector_store()