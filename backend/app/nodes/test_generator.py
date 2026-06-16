from app.nodes.retriever import get_retriever
from app.nodes.generator import generate_answer

retriever = get_retriever()

query = input("Enter Query: ")

documents = retriever.invoke(query)

answer = generate_answer(query, documents)

print("\nAnswer: \n")
print(answer)