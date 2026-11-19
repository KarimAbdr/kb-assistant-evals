"""Grounded-answer prompt with numbered context and citation markers.

Base design: LocalSmartRAG core/rag_chain.py (MIT): context blocks are numbered [1..n] in
the same order as retrieved chunks, the model must cite [n], and must answer
"I could not find this in the documentation." when context is insufficient.
"""

from __future__ import annotations

from kb_assistant.types import Citation, RetrievedChunk

REFUSAL_TEXT = "I could not find this in the documentation."

SYSTEM_PROMPT = (
    "You are an internal knowledge assistant. Answer ONLY from the numbered context.\n"
    "Rules: 1) cite sources as [n] after each claim; 2) do not use prior knowledge;\n"
    f"3) if the context does not contain the answer, reply exactly: \"{REFUSAL_TEXT}\""
)


def format_context(chunks: list[RetrievedChunk]) -> str:
    """"[1] (source: <url>, section: <heading_path>)\n<text>" blocks joined by blank lines. TODO(step-0.7)"""
    raise NotImplementedError("TODO(step-0.7)")


def build_prompt(question: str, chunks: list[RetrievedChunk]) -> str:
    """SYSTEM_PROMPT + context + question as one string (LLMProvider is text-in/text-out). TODO(step-0.7)"""
    raise NotImplementedError("TODO(step-0.7)")


def parse_citations(answer: str, chunks: list[RetrievedChunk]) -> list[Citation]:
    """Extract [n] markers, map to chunks; ignore out-of-range markers but log them
    (an out-of-range citation is a groundedness red flag). TODO(step-0.7)"""
    raise NotImplementedError("TODO(step-0.7)")
