from langgraph.graph import StateGraph, END

from app.graph.state import GraphState

from app.graph.retriever_node import retrieve_node
from app.graph.grader_node import grade_node
from app.graph.rewriter_node import rewrite_node
from app.graph.generator_node import generator_node

from app.graph.router import route_after_grading
from app.graph.not_found_node import not_found_node

workflow = StateGraph(GraphState)


# -------------------------
# Add Nodes
# -------------------------

workflow.add_node(
    "retrieve",
    retrieve_node
)

workflow.add_node(
    "grade",
    grade_node
)

workflow.add_node(
    "rewrite",
    rewrite_node
)

workflow.add_node(
    "generate",
    generator_node
)

workflow.add_node(
    "not_found",
    not_found_node
)


# -------------------------
# Entry Point
# -------------------------

workflow.set_entry_point("retrieve")


# -------------------------
# Edges
# -------------------------

workflow.add_edge(
    "retrieve",
    "grade"
)


# Conditional Routing
workflow.add_conditional_edges(
    "grade",
    route_after_grading,
    {
        "generate": "generate",
        "rewrite": "rewrite",
        "not_found": "not_found"
    }
)


workflow.add_edge(
    "generate",
    END
)


workflow.add_edge(
    "rewrite",
    "retrieve"
)

workflow.add_edge(
    "not_found",
    END
)


graph = workflow.compile()
