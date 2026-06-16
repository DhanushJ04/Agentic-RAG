from app.llm.ollama_client import get_llm
from app.prompts.rewriter_prompt import REWRITER_PROMPT


def rewrite_query(question):

    llm = get_llm()

    prompt = REWRITER_PROMPT.format(question=question)

    response = llm.invoke(prompt)

    return response.content.strip()
    