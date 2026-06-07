from langchain_community.embeddings import HuggingFaceEmbeddings


def get_embedding_model():
    """
    Load embedding model.
    """

    embeddings = HuggingFaceEmbeddings(
        model_name="BAAI/bge-small-en-v1.5"
    )

    return embeddings


if __name__ == "__main__":

    embedding_model = get_embedding_model()

    sample_text = "What is Lemmatization?"

    vector = embedding_model.embed_query(sample_text)

    print(f"Vector Length: {len(vector)}")

    print("\nFirst 10 Values:")
    print(vector[:10])
