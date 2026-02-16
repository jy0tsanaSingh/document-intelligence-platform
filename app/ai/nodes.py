from typing import Dict
from openai import OpenAI
import os
import json


def extract_text_node(state: Dict) -> Dict:
    """
    Phase 4 simplification:
    For now we simulate extracted text.
    Later we will replace this with real PDF parsing.
    """
    text = f"Document filename is {state['filename']}"
    state["text"] = text
    return state


def llm_extract_node(state: Dict) -> Dict:
    """
    Calls OpenAI to extract structured data.
    Requires OPENAI_API_KEY to be set in environment.
    """

    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        raise ValueError(
            "OPENAI_API_KEY is not set. Please export it before running the server."
        )

    client = OpenAI(api_key=api_key)

    prompt = f"""
    Extract structured information from the text below.
    Return strictly valid JSON with keys:
    - title (string)
    - summary (string)
    - keywords (array of strings)

    TEXT:
    {state['text']}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0,
    )

    state["raw_output"] = response.choices[0].message.content
    return state


def parse_json_node(state: Dict) -> Dict:
    """
    Parses LLM output into JSON safely.
    """

    try:
        state["extracted_data"] = json.loads(state["raw_output"])
    except Exception:
        # Fallback if model returns non-strict JSON
        state["extracted_data"] = {
            "title": None,
            "summary": None,
            "keywords": [],
        }

    return state
