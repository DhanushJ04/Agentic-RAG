from app.llm.ollama_client import get_llm
from app.prompts.grader_prompt import GRADER_PROMPT


def grade_documents(question, documents):

    llm = get_llm()

    docs_text = "\n\n".join(
        [doc.page_content for doc in documents]
    )

    prompt = GRADER_PROMPT.format(
        question=question,
        documents=docs_text
    )

    response = llm.invoke(prompt)

    return response.content.strip().lower()