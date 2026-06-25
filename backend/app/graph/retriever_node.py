from app.nodes.retriever import get_retriever


def retrieve_node(state):

    retriever = get_retriever()

    question = (
        state.get("rewritten_query")
        or state["question"]
    )

    history = state.get(
        "chat_history",
        ""
    )

    query = (
        history + "\nCurrent Question: " + question
    )

    documents = retriever.invoke(query)

    return {
        "documents": documents
    }