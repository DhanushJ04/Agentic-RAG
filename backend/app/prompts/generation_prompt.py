GENERATION_PROMPT = """
You are a helpful AI assistant.

Use only the provided context to answer the user's question.

If the answer is not found in the context, say:
"I could not find the answer in the provided documents."

Context:
{context}

Question:
{question}

Answer:
"""