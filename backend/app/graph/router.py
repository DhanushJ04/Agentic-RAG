def route_after_grading(state):

    decision = state["decision"]

    retry_count = state.get("retry_count", 0)

    if decision == "yes":
        return "generate"

    if retry_count >= 2:
        return "not_found"
        
    return "rewrite"