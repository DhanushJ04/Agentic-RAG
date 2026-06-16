from typing import TypeDict, List


class GraphState(TypeDict):

    question: str

    rewritten_query: str

    documents: list

    answer: str

    decision: str