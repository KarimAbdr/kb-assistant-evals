"""Trajectory logging (JSONL, one line per step) and trajectory metrics.

Step record: {item_id, step, type: "llm"|"tool", tool_name, tool_args, output_preview, ts}
"""

from __future__ import annotations

from pathlib import Path


class TrajectoryLogger:
    """Append-only JSONL writer; one file per run in runs/<run_id>/trajectories.jsonl."""

    def __init__(self, path: Path) -> None:
        self.path = path

    def log_step(self, item_id: str, step: int, record: dict) -> None:
        """TODO(step-4.3)"""
        raise NotImplementedError("TODO(step-4.3)")


def load_trajectories(path: Path) -> dict[str, list[dict]]:
    """Group steps by item_id, sorted by step. TODO(step-4.3)"""
    raise NotImplementedError("TODO(step-4.3)")


def tool_call_correctness(steps: list[dict], expected_tool: str,
                          expected_section: str | None = None) -> float:
    """1.0 if the first tool call uses the expected tool (and section) else 0.0. TODO(step-4.4)"""
    raise NotImplementedError("TODO(step-4.4)")


def num_steps(steps: list[dict]) -> int:
    """Number of tool calls. TODO(step-4.4)"""
    raise NotImplementedError("TODO(step-4.4)")


def has_loop(steps: list[dict], window: int = 2) -> bool:
    """True if the same (tool_name, normalised args) repeats within the window. TODO(step-4.4)"""
    raise NotImplementedError("TODO(step-4.4)")
