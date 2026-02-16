from langgraph.graph import StateGraph
from typing import Dict

from app.ai.nodes import (
    extract_text_node,
    llm_extract_node,
    parse_json_node,
)


def build_document_graph():
    graph = StateGraph(dict)

    graph.add_node("extract_text", extract_text_node)
    graph.add_node("llm_extract", llm_extract_node)
    graph.add_node("parse_json", parse_json_node)

    graph.set_entry_point("extract_text")
    graph.add_edge("extract_text", "llm_extract")
    graph.add_edge("llm_extract", "parse_json")
    graph.set_finish_point("parse_json")

    return graph.compile()
