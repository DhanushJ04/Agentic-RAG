from app.nodes.retriever import get_retriever


def retrieve_node(state):

    retriever = get_retriever()

    query = state.get("rewritten_query") or state["question"]

    documents = retriever.invoke(query)

    return {
        "documents": documents
    }