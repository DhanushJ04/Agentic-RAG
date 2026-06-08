GRADER_PROMPT = """
You are a retrieval grader.

Your task is to determine whether the retrieved documents contain information relevant to answering the user's question.

Question:
{question}

Retrieved Documents:
{documents}

If the documents contain information relevant to answering the question, respond with:

yes

Otherwise respond with:

no

Only return yes or no.
"""