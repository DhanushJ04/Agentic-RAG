from app.llm.ollama_client import get_llm

llm = get_llm()

response = llm.invoke("What is RAG?")

print(response.content)
