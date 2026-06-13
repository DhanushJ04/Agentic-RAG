from app.llm.ollama_client import get_grader_llm
from app.prompts.chunk_grader_prompt import CHUNK_GRADER_PROMPT
from app.utils.grader_parser import parse_yes_no


def grade_chunk(question, chunk):

    llm = get_grader_llm()

    prompt = CHUNK_GRADER_PROMPT.format(
        question=question,
        chunk=chunk.page_content
    )

    response = llm.invoke(prompt)

    raw_output = response.content.strip().lower()

    decision = parse_yes_no(raw_output)

    return decision