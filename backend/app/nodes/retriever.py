from langchain_chroma import Chroma

from app.ingestion.embeddings import get_embedding_model


CHROMA_PATH = "backend/vectorstore"


def get_retriever():

    embedding_model = get_embedding_model()

    vector_store = Chroma(
        persist_directory=CHROMA_PATH,
        embedding_function=embedding_model
    )

    retriever = vector_store.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 5}
    )

    return retriever


if __name__ == "__main__":

    retriever = get_retriever()

    query = "What is a star topology?"

    results = retriever.invoke(query)

    print("\nRetrieved Documents:\n")

    for i, doc in enumerate(results, start=1):

        print(f"\n----- Chunk {i} -----\n")

        print(doc.page_content[:500])

        print("\nMetadata:")
        print(doc.metadata)