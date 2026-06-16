from app.nodes.query_rewriter import rewrite_query


def rewrite_node(state):

    question = state["question"]

    rewritten_query = rewrite_query(question)
    
    retry_count = state.get("retry_count", 0)

    return {
        "rewritten_query": rewritten_query,
        "retry_count": retry_count + 1
    }