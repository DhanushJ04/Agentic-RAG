import shutil
from pathlib import Path
from langchain_chroma import Chroma

from app.ingestion.embeddings import get_embedding_model
from app.ingestion.chunker import create_chunks
from app.ingestion.pdf_loader import load_pdfs
from app.utils.config import PDF_DIR, VECTOR_DB_DIR
from app.nodes.retriever import reset_retriever


def create_vector_store():

    # Close old retriever first
    reset_retriever()

    vector_path = Path(VECTOR_DB_DIR)

    if vector_path.exists():
        print("Removing old vector store...")
        shutil.rmtree(vector_path)

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

    try:
        if hasattr(vector_store, "_client") and hasattr(vector_store._client, "close"):
            vector_store._client.close()
    except Exception as e:
        print(f"Error closing created vector store: {e}")

    import gc
    gc.collect()

    return vector_store


if __name__ == "__main__":
    create_vector_store()