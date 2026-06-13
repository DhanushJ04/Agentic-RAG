GRADER_PROMPT = """You are a retrieval grader. Given a question and retrieved documents, decide if the documents are relevant.

Question: What is mobile banking?
Documents: Mobile banking allows users to perform financial transactions using a smartphone app. Features include balance checks, fund transfers, and bill payments.
Answer: yes

Question: What is quantum entanglement?
Documents: Mobile banking allows users to perform financial transactions using a smartphone app. Features include balance checks, fund transfers, and bill payments.
Answer: no

Question: {question}
Documents: {documents}
Answer:"""