"""CI eval gate (stage 03, ADR-0005).

Fails (exit code 1) when a retrieval metric is below its absolute threshold OR dropped more
than max_regression vs evals/baseline.json. Retrieval-only => deterministic => no flaky CI.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class GateResult:
    passed: bool
    metrics: dict[str, float]
    failures: list[str]  # e.g. "recall_at_k 0.61 < threshold 0.70"


def check(metrics: dict[str, float], baseline: dict[str, float], thresholds: dict[str, float],
          max_regression: dict[str, float]) -> GateResult:
    """Pure decision function (unit-test it with hand-made dicts). TODO(step-3.1)"""
    raise NotImplementedError("TODO(step-3.1)")


def run_gate(config_path: Path = Path("configs/gate.yaml")) -> int:
    """Run retrieval eval, call check(), print a Markdown summary (also to $GITHUB_STEP_SUMMARY
    if set), return 0/1. TODO(step-3.1)"""
    raise NotImplementedError("TODO(step-3.1)")


def update_baseline(metrics: dict[str, float], path: Path) -> None:
    """Write a new baseline. Only on purpose, in a reviewed commit (never automatically in CI). TODO(step-3.2)"""
    raise NotImplementedError("TODO(step-3.2)")
