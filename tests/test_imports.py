"""Green from day one: every module imports (catches syntax/circular-import errors)."""

import importlib

import pytest

MODULES = [
    "kb_assistant", "kb_assistant.types", "kb_assistant.config", "kb_assistant.cli",
    "kb_assistant.ingest.loader", "kb_assistant.ingest.cleaner",
    "kb_assistant.chunking.splitter", "kb_assistant.chunking.baseline_splitter",
    "kb_assistant.retrieval.base", "kb_assistant.retrieval.tokenize", "kb_assistant.retrieval.bm25",
    "kb_assistant.retrieval.vector", "kb_assistant.retrieval.hybrid",
    "kb_assistant.generation.provider", "kb_assistant.generation.prompt", "kb_assistant.generation.pipeline",
    "kb_assistant.eval.golden_set", "kb_assistant.eval.retrieval_metrics", "kb_assistant.eval.rag_triad",
    "kb_assistant.eval.runner", "kb_assistant.eval.gate",
    "kb_assistant.judge.rubric", "kb_assistant.judge.judge", "kb_assistant.judge.agreement", "kb_assistant.judge.bias",
    "kb_assistant.labeling.cli",
    "kb_assistant.agent.tools", "kb_assistant.agent.loop", "kb_assistant.agent.trajectory",
]


@pytest.mark.parametrize("name", MODULES)
def test_module_imports(name: str) -> None:
    importlib.import_module(name)


def test_golden_example_is_valid_jsonl() -> None:
    import json
    from pathlib import Path

    lines = Path("evals/golden_set.example.jsonl").read_text().splitlines()
    items = [json.loads(line) for line in lines if line.strip()]
    assert len(items) == 5
    assert len({i["id"] for i in items}) == 5
