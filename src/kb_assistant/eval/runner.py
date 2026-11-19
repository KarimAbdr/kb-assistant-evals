"""Eval runner: (config, corpus, golden set) -> run artefact in runs/<timestamp>_<fingerprint>/.

Artefact = metrics.json (aggregates), per_query.jsonl (for error analysis), config.json.
Reports in reports/ are written FROM these artefacts, never by hand-typing numbers.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any


def run_retrieval_eval(golden_path: Path, k: int, experiment: Path | None = None) -> dict[str, Any]:
    """ingest -> chunk -> index -> retrieve each question -> metrics; write artefact. TODO(step-1.4)"""
    raise NotImplementedError("TODO(step-1.4)")


def run_triad_eval(golden_path: Path, experiment: Path | None = None) -> dict[str, Any]:
    """Full pipeline + RAG triad per question; write artefact. TODO(step-1.5)"""
    raise NotImplementedError("TODO(step-1.5)")


def compare_runs(before: Path, after: Path) -> str:
    """Markdown table of metric deltas + list of questions that flipped hit->miss and miss->hit. TODO(step-1.6)"""
    raise NotImplementedError("TODO(step-1.6)")
