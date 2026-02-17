from typing import Dict
from openai import OpenAI
import os
import json


MAX_RETRIES = 2


def extract_text_node(state: Dict) -> Dict:
    """
    Simulates extracted document text.
    """
    text = f"Document filename is {state['filename']}"
    state["text"] = text
    return state


def llm_extract_node(state: Dict) -> Dict:
    """
    Calls OpenAI to extract structured data.
    """

    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        state["error"] = "OPENAI_API_KEY not set"
        state["validation_passed"] = False
        return state

    try:
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

    except Exception as e:
        state["error"] = str(e)
        state["validation_passed"] = False

    return state


def parse_json_node(state: Dict) -> Dict:
    """
    Parses LLM output into JSON safely.
    """

    try:
        state["extracted_data"] = json.loads(state.get("raw_output", "{}"))
    except Exception:
        state["extracted_data"] = {
            "title": None,
            "summary": None,
            "keywords": [],
        }

    return state


def validate_node(state: Dict) -> Dict:
    """
    Validates required fields from extracted_data.
    """

    data = state.get("extracted_data", {})

    if data.get("title") and data.get("summary"):
        state["validation_passed"] = True
    else:
        state["validation_passed"] = False
        state["error"] = "Missing required fields"

    return state


def retry_node(state: Dict) -> Dict:
    """
    Increments retry counter.
    """

    state["retry_count"] = state.get("retry_count", 0) + 1
    return state


def fail_node(state: Dict) -> Dict:
    """
    Final failure state.
    """

    state["final_status"] = "failed"
    return state
