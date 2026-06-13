"""
Robust parser for extracting yes/no decisions from LLM responses.

Small models like Llama 3.2:1B often ignore formatting instructions and
produce verbose responses. This parser handles those cases by scanning
for yes/no keywords and applying heuristics when the response is not a
clean "yes" or "no".
"""

import re


def parse_yes_no(response_text: str) -> str:
    """
    Parse an LLM response and extract a yes/no decision.

    Strategy (in priority order):
      1. Exact match after stripping whitespace/punctuation.
      2. Check if the response *starts with* yes or no (common when the
         model adds an explanation after the answer).
      3. Keyword scan — count occurrences of yes/no related words and
         pick the majority.
      4. Default to "no" (fail-safe: treat uncertain grading as
         irrelevant so the system falls back to web search, which is
         the safe CRAG behavior).

    Args:
        response_text: Raw text output from the LLM.

    Returns:
        "yes" or "no"
    """
    if not response_text:
        return "no"

    text = response_text.strip().lower()

    # ── 1. Exact match ────────────────────────────────────────────
    # Strip trailing punctuation like periods or quotes
    cleaned = re.sub(r"[^a-z]", "", text)
    if cleaned == "yes":
        return "yes"
    if cleaned == "no":
        return "no"

    # ── 2. Starts-with check ──────────────────────────────────────
    # The model often outputs "yes, because..." or "no. The document..."
    if re.match(r"^yes\b", text):
        return "yes"
    if re.match(r"^no\b", text):
        return "no"

    # ── 3. First-word on first line ───────────────────────────────
    first_line = text.split("\n")[0].strip()
    first_word = re.split(r"\W+", first_line)[0] if first_line else ""
    if first_word == "yes":
        return "yes"
    if first_word == "no":
        return "no"

    # ── 4. Keyword frequency scan ─────────────────────────────────
    yes_keywords = ["yes", "relevant", "related", "useful", "pertinent", "applicable"]
    no_keywords = ["no", "irrelevant", "unrelated", "not relevant", "not related", "not useful"]

    yes_count = sum(text.count(kw) for kw in yes_keywords)
    no_count = sum(text.count(kw) for kw in no_keywords)

    if yes_count > no_count:
        return "yes"
    if no_count > yes_count:
        return "no"

    # ── 5. Default: fail-safe to "no" ─────────────────────────────
    return "no"
