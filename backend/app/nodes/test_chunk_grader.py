from app.nodes.retriever import get_retriever
from app.nodes.chunk_grader import grade_chunk


retriever = get_retriever()

query = input("Enter Query: ")

documents = retriever.invoke(query)

relevant_docs = []

print("\nGrading Chunks...\n")

for idx, doc in enumerate(documents, start=1):

    decision = grade_chunk(
        query,
        doc
    )

    print(f"Chunk {idx}: {decision}")

    if decision == "yes":
        relevant_docs.append(doc)

print("\nSummary")
print("-" * 30)

print(f"Retrieved Chunks : {len(documents)}")
print(f"Relevant Chunks  : {len(relevant_docs)}")