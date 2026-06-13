from langchain_ollama import ChatOllama


def get_llm():

    llm = ChatOllama(
        model="hf.co/LiquidAI/LFM2-1.2B-RAG-GGUF:Q8_0",
        temperature=0,
        num_predict=256
    )

    return llm


def get_grader_llm():
    """
    Returns an LLM instance tuned for grading tasks.

    Key differences from the general-purpose LLM:
      - num_predict=10: Forces the model to stop after a few tokens,
        preventing long rambling explanations.
      - temperature=0: Deterministic output for consistent grading.
    """
    llm = ChatOllama(
        model="hf.co/LiquidAI/LFM2-1.2B-RAG-GGUF:Q8_0",
        temperature=0,
        num_predict=10
    )

    return llm