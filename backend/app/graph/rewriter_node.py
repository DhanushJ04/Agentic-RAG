from app.nodes.query_rewriter import rewrite_query


def rewrite_node(state):

    question = state["question"]

    rewritten_query = rewrite_query(question)

    return {
        "rewritten_query": rewritten_query
    }