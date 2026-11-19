# Report 04: Agent trajectory evaluation (stage 2)

> Template. Fill from `runs/<id>/trajectories.jsonl` via `kb agent run`.

## Setup

| Item | Value |
|---|---|
| Tools | `search_kb(query)`, `search_by_section(section, query)` |
| Model | scripted `FakeMessagesListChatModel` (`evals/fixtures/agent_scripts.jsonl`) |
| Items | `{TBD}` golden questions with `expected_tool` / `expected_section` |
| Step budget | `{TBD}` |

## Metrics

| Metric | Before | After |
|---|---|---|
| Tool-call correctness (first call) | {TBD} | {TBD} |
| Mean steps per question | {TBD} | {TBD} |
| Loop rate (same call repeated) | {TBD} | {TBD} |
| Budget exhausted | {TBD} | {TBD} |
| Final answer hit (reuses stage 01 checks) | {TBD} | {TBD} |

## Failure mode → fix

- Failure mode: `{TBD}` (e.g. "agent repeats search_kb with the same query when the first result is weak")
- Example trajectory (trimmed JSONL): `{TBD}`
- Fix: `{TBD}` (e.g. loop guard: duplicate call → return "already searched, try search_by_section")
- Result: see the "After" column

## Limits

Scripted model trajectories validate the *metrics and logging*, not a real model's behaviour: `{TBD}`
