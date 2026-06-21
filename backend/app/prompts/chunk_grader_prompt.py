CHUNK_GRADER_PROMPT = """You are a strict relevance grader.
Determine if the provided chunk of text contains enough information to DIRECTLY answer the question.

Rules:
1. Reply with 'yes' ONLY if the chunk contains the actual information, facts, or definition needed to directly answer the user's question.
2. Reply with 'no' if the chunk contains document metadata, letters, circular numbers, headers, dates, list of banks, or generic intro text without actually answering the question.
3. Reply with 'no' if the chunk mentions similar keywords (e.g. "banking" or "loans") but does not explain or answer the specific question (e.g. "what is digital banking?").
4. Respond with only one word: yes or no.

Example 1:
Question: What is digital banking?
Chunk: RBI/2009-10/69 DBOD No. Dir. BC 13/13.03.00/2009-10 July 1, 2009 Master Circular- Loans and Advances – Statutory and Other Restrictions.
Answer: no

Example 2:
Question: What is digital banking?
Chunk: Commercial banks may offer traditional banking services, including checking accounts, business loans, and savings deposits. All banking activities must comply with the local banking regulations.
Answer: no

Example 3:
Question: What is digital banking?
Chunk: Digital banking is the digitization of all the traditional banking activities and programs that historically were only available to customers when physically inside of a bank branch.
Answer: yes

Example 4:
Question: What is mobile banking?
Chunk: Mobile banking lets users perform financial transactions via smartphone apps, including balance checks and transfers.
Answer: yes

Question: {question}
Chunk: {chunk}
Answer:"""