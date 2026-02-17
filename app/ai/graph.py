from langgraph.graph import StateGraph, END
from typing import Dict

from app.ai.nodes import (
    extract_text_node,
    llm_extract_node,
    parse_json_node,
    validate_node,
    retry_node,
    fail_node,
)

MAX_RETRIES = 2


def retry_decision(state: Dict):
    if state.get("validation_passed"):
        return "success"

    if state.get("retry_count", 0) < MAX_RETRIES:
        return "retry"

    return "fail"


def build_document_graph():
    graph = StateGraph(dict)

    graph.add_node("extract_text", extract_text_node)
    graph.add_node("llm_extract", llm_extract_node)
    graph.add_node("parse_json", parse_json_node)
    graph.add_node("validate", validate_node)
    graph.add_node("retry", retry_node)
    graph.add_node("fail", fail_node)

    graph.set_entry_point("extract_text")

    graph.add_edge("extract_text", "llm_extract")
    graph.add_edge("llm_extract", "parse_json")
    graph.add_edge("parse_json", "validate")

    graph.add_conditional_edges(
        "validate",
        retry_decision,
        {
            "success": END,
            "retry": "retry",
            "fail": "fail",
        },
    )

    graph.add_edge("retry", "llm_extract")
    graph.add_edge("fail", END)

    return graph.compile()
