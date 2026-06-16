from app.nodes.generator import generate_answer


def generator_node(state):

    question = state["question"]

    documents = state["documents"]

    answer = generate_answer(question, documents)

    return {
        "answer": answer
    }