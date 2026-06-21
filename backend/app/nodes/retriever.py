from langchain_chroma import Chroma

from app.ingestion.embeddings import get_embedding_model
from app.utils.config import VECTOR_DB_DIR


_retriever = None
_vector_store = None


def get_retriever():

    global _retriever
    global _vector_store

    if _retriever is None:

        print("Loading Retriever...")

        embedding_model = get_embedding_model()

        _vector_store = Chroma(
            persist_directory=str(VECTOR_DB_DIR),
            embedding_function=embedding_model
        )

        _retriever = _vector_store.as_retriever(
            search_type="mmr",
            search_kwargs={
                "k": 5,
                "fetch_k": 20
            }
        )

    return _retriever


def reset_retriever():

    global _retriever
    global _vector_store

    if _vector_store is not None:
        try:
            if hasattr(_vector_store, "_client") and hasattr(_vector_store._client, "close"):
                _vector_store._client.close()
        except Exception as e:
            print(f"Error closing vector store: {e}")

    _retriever = None
    _vector_store = None
    import gc
    gc.collect()


if __name__ == "__main__":

    retriever = get_retriever()

    query = input("Enter Query: ")

    results = retriever.invoke(query)

    print(f"\nRetrieved Chunks: {len(results)}")

    for i, doc in enumerate(results, start=1):

        print(f"\n{'=' * 50}")
        print(f"Chunk {i}")
        print(f"{'=' * 50}")

        print(doc.page_content[:500])

        print("\nMetadata:")
        print(doc.metadata)