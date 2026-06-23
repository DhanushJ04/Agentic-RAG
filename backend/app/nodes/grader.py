from app.nodes.chunk_grader import grade_chunk


def grade_documents(question, documents):
    """
    Grade each document chunk individually against the question.

    Returns "yes" if at least one chunk is relevant, "no" otherwise.
    This per-chunk approach avoids confusing the small LLM with a
    large concatenated context that mixes relevant and irrelevant text.
    """

    question = question.strip()

    for doc in documents:

        decision = grade_chunk(question, doc)

        if decision == "yes":
            return "yes"

    return "no"


def filter_relevant_documents(question, documents):
    """
    Grade each chunk and return only the relevant ones.
    """

    question = question.strip()
    relevant = []

    for doc in documents:

        decision = grade_chunk(question, doc)

        if decision == "yes":
            relevant.append(doc)

    return relevant