from app.nodes.retriever import get_retriever
from app.nodes.grader import grade_documents


retriever = get_retriever()

query = input("Enter Query: ")

documents = retriever.invoke(query)

print("\nRetrieved Documents:\n")

for i, doc in enumerate(documents, start=1):
    print(f"\n----- Chunk {i} -----")
    print(doc.page_content[:300])
    
decision = grade_documents(query, documents)

print("\nGrader Decision: ")
print(decision)