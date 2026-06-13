CHUNK_GRADER_PROMPT = """You are a relevance grader. Given a question and a chunk of text, decide if the chunk is relevant to the question. Reply with only yes or no.

Question: What is mobile banking?
Chunk: Mobile banking lets users do financial transactions via smartphone apps including balance checks and transfers.
Answer: yes

Question: What is quantum entanglement?
Chunk: Mobile banking lets users do financial transactions via smartphone apps including balance checks and transfers.
Answer: no

Question: {question}
Chunk: {chunk}
Answer:"""