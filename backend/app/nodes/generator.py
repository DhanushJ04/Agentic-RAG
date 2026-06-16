from app.llm.ollama_client import get_llm
from app.prompts.generation_prompt import GENERATION_PROMPT


def generate_answer(question, documents):

    llm = get_llm()

    context = "\n\n".join(
        [doc.page_content for doc in documents]
    )

    prompt = GENERATION_PROMPT.format(
        context=context,
        question=question
    )

    response = llm.invoke(prompt)

    return response.content