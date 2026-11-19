"""Command-line entry point: `kb <command>`.

Commands (each one is wired in the step that implements it):
    kb ingest                      -> step 0.4  (pages -> data/processed/pages.jsonl)
    kb index                       -> step 0.6  (chunks + BM25 index)
    kb ask "question"              -> step 0.8  (one RAG answer with citations)
    kb eval retrieval [--exp FILE] -> step 1.4  (recall@k, MRR, hit rate -> runs/)
    kb eval triad                  -> step 1.5  (RAG triad via judge)
    kb label                       -> step 2.2  (human labelling CLI)
    kb judge validate              -> step 2.4  (kappa / accuracy / bias tests)
    kb gate                        -> step 3.1  (exit 1 if metrics below thresholds)
    kb agent run                   -> step 4.2  (agent on golden questions, JSONL trajectories)
"""

from __future__ import annotations

import argparse


def build_parser() -> argparse.ArgumentParser:
    """Build the argparse tree. TODO(step-0.8): add sub-commands as listed in the module doc."""
    parser = argparse.ArgumentParser(prog="kb", description="KB assistant + evals")
    parser.add_subparsers(dest="command")
    return parser


def main(argv: list[str] | None = None) -> int:
    """Parse args and dispatch. Returns a process exit code (the gate relies on it)."""
    args = build_parser().parse_args(argv)
    if args.command is None:
        build_parser().print_help()
        return 0
    raise NotImplementedError("TODO(step-0.8)")
