def route_after_grading(state):

    decision = state["decision"]

    if decision == "yes":
        return "generate"

    return "rewrite"