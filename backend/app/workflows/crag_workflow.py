from app.nodes.retriever import get_retriever
from app.nodes.grader import grade_documents
from app.nodes.query_rewriter import rewrite_query
from app.nodes.generator import generate_answer


def run_crag(question):

    retriever = get_retriever()

    print("\n[1] Retrieving Documents...")

    documents = retriever.invoke(question)

    print("[2] Grading Retrieved Documents...")

    decision = grade_documents(question, documents)

    print(f"\nGrader Decision: {decision}")


    # ------------------------------
    # Relevant Documents Found
    # ------------------------------
    if decision == "yes":

        print("\n[3] Documents are relevant.")

        answer = generate_answer(question, documents)

        return {
            "question": question,
            "rewritten": False,
            "answer": answer,
            "documents": documents
        }
    
    # ------------------------------
    # Documents Not Relevant
    # ------------------------------
    print("\n[3] Documents not relevant.")

    print("\n[4] Rewriting Query...")

    rewritten_query = rewrite_query(question)

    print(f"\nRewritten Query:\n{rewritten_query}")

    print("\n[5] Retrieving Again...")

    documents = retriever.invoke(rewritten_query)

    second_decision = grade_documents(rewritten_query, documents)

    print(f"\nSecond Grader Decision: {second_decision}")
    
    if second_decision == "yes":
        answer = generate_answer(rewritten_query, documents)

        return {
            "question": question,
            "rewritten": True,
            "rewritten_query": rewritten_query,
            "answer": answer,
            "documents": documents
        }

    else:
        answer = ("I cound not find relevant information in the provided documents.")

        return {
            "question": question,
            "rewritten": True,
            "rewritten_query": rewritten_query,
            "answer": answer,
            "documents": documents
        }