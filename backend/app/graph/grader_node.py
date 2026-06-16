from app.nodes.grader import grade_documents


def grade_node(state):

    question = state["question"]

    documents = state["documents"]

    decision = grade_documents(question, documents)

    return {
        "decision": decision
    }