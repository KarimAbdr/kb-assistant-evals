"""End-to-end RAG pipeline: retrieve -> prompt -> generate -> parse citations."""

from __future__ import annotations

from kb_assistant.generation.provider import LLMProvider
from kb_assistant.retrieval.base import Retriever
from kb_assistant.types import RagAnswer


class RagPipeline:
    """Stateless orchestration; all dependencies injected (easy to test with fakes)."""

    def __init__(self, retriever: Retriever, llm: LLMProvider, top_k: int = 5) -> None:
        self.retriever, self.llm, self.top_k = retriever, llm, top_k

    def answer(self, question: str) -> RagAnswer:
        """TODO(step-0.7): retrieve(top_k) -> build_prompt -> llm.generate -> parse_citations;
        set refused=True when the answer equals REFUSAL_TEXT."""
        raise NotImplementedError("TODO(step-0.7)")
