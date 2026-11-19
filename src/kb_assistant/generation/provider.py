"""LLMProvider: the only place that knows which LLM is behind the system (ADR-0003).

Today: FakeProvider (LangChain FakeListLLM / fixture lookup), zero cost, deterministic.
Later: OllamaProvider or an API provider, switched by one line in configs/generation.yaml.
"""

from __future__ import annotations

from typing import Protocol


class LLMProvider(Protocol):
    """Minimal text-in/text-out contract. Keep it small: easier to fake, easier to swap."""

    name: str

    def generate(self, prompt: str, *, temperature: float = 0.0, max_tokens: int = 512) -> str:
        """Return the completion text for a fully rendered prompt."""
        ...


class FakeProvider:
    """Deterministic provider for development and CI.

    Two modes:
      - fixtures: look up a pre-recorded answer by question id / prompt hash
        (evals/fixtures/fake_answers.jsonl) -> realistic answers for eval demos;
      - list: cycle through a fixed list (langchain_core.language_models.FakeListLLM) -> unit tests.
    """

    name = "fake"

    def __init__(self, responses: list[str] | None = None, fixtures_path: str | None = None) -> None:
        self.responses = responses
        self.fixtures_path = fixtures_path

    def generate(self, prompt: str, *, temperature: float = 0.0, max_tokens: int = 512) -> str:
        """TODO(step-0.7): fixtures lookup first, then FakeListLLM; raise KeyError on a missing fixture
        (a silent default answer would hide eval bugs)."""
        raise NotImplementedError("TODO(step-0.7)")


class OllamaProvider:
    """Placeholder for a free local model (langchain-ollama). Not required for any stage."""

    name = "ollama"

    def __init__(self, model: str, base_url: str, temperature: float = 0.0) -> None:
        self.model, self.base_url, self.temperature = model, base_url, temperature

    def generate(self, prompt: str, *, temperature: float = 0.0, max_tokens: int = 512) -> str:
        """TODO(step-beyond): ChatOllama(model, base_url).invoke(prompt).content"""
        raise NotImplementedError("TODO(step-beyond)")


def build_provider(cfg: dict) -> LLMProvider:
    """Factory from configs/generation.yaml or configs/judge.yaml. TODO(step-0.7)"""
    raise NotImplementedError("TODO(step-0.7)")
