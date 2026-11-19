"""Two agent tools (LangChain @tool):

1. search_kb(query)                 -> top-k chunks from the retriever (full-text search)
2. search_by_section(section, query) -> same, but filtered to one handbook section
                                       (metadata filter: people-policies / total-rewards / ...)
Why two: the interesting failure mode is choosing the wrong tool or wrong section.
"""

from __future__ import annotations

from kb_assistant.retrieval.base import Retriever


def make_tools(retriever: Retriever, sections: list[str]) -> list:
    """Return [search_kb, search_by_section] as LangChain tools with clear docstrings
    (the docstring IS the tool description the model sees). TODO(step-4.1)"""
    raise NotImplementedError("TODO(step-4.1)")
