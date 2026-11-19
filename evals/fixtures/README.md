# Fixtures (fake LLM, fake judge, scripted agent)

These are **hand-written**, not model outputs. They exist so that every stage runs with zero
cost and deterministically (ADR-0003). Some are intentionally wrong (see `_note`) to show
that the evaluation catches the failure. Never report fixture-based numbers as model quality.
