from typing import TypedDict


class GraphState(TypedDict):
    question: str
    chat_history: str

    rewritten_query: str
    documents: list
    decision: str
    answer: str
    retry_count: int