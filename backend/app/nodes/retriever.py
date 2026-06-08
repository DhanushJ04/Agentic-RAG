from langchain_chroma import Chroma

from app.ingestion.embeddings import get_embedding_model
from app.utils.config import VECTOR_DB_DIR


def get_retriever():

    embedding_model = get_embedding_model()

    vector_store = Chroma(
        persist_directory=str(VECTOR_DB_DIR),
        embedding_function=embedding_model
    )

    retriever = vector_store.as_retriever(
        search_type="mmr",
        search_kwargs={
            "k": 5,
            "fetch_k": 20
        }
    )

    return retriever


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