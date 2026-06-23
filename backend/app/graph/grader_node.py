from app.nodes.grader import filter_relevant_documents


def grade_node(state):

    question = state.get("rewritten_query") or state["question"]

    documents = state["documents"]

    relevant_docs = filter_relevant_documents(question, documents)

    decision = "yes" if relevant_docs else "no"

    return {
        "decision": decision,
        "documents": relevant_docs if relevant_docs else documents
    }