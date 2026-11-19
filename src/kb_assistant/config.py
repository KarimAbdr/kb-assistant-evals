"""Config loading: YAML files in configs/ + optional experiment override.

Why: every tunable (chunk size, top_k, thresholds) lives in config, never in code, so an
experiment or a CI gate run is fully described by (code commit, config, corpus commit).
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

CONFIG_DIR = Path("configs")


def load_config(name: str, override: Path | None = None) -> dict[str, Any]:
    """Load configs/<name>.yaml and deep-merge an optional experiment override on top.

    Input:  name like "chunking"; override path like configs/experiments/chunk_small.yaml.
    Output: merged dict.
    TODO(step-0.1): implement with yaml.safe_load + a small recursive deep_merge.
    """
    raise NotImplementedError("TODO(step-0.1)")


def config_fingerprint(cfg: dict[str, Any]) -> str:
    """Short stable hash of a config dict, written into every run artefact for reproducibility.

    TODO(step-1.4): json.dumps(sort_keys=True) -> sha256 -> first 12 hex chars.
    """
    raise NotImplementedError("TODO(step-1.4)")
