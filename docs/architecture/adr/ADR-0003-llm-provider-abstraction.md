# ADR-0003: `LLMProvider` abstraction with fake implementations

- **Status**: Accepted
- **Date**: 2026-11-19

## Context
The project must cost nothing and run offline and in CI. It must also be ready to plug in a
real model (local Ollama or an API) later without touching the pipeline, eval or agent code.
LLM outputs are non-deterministic, which conflicts with reproducible evaluation.

## Decision
We will put every model call behind a minimal text-in/text-out protocol
`LLMProvider.generate(prompt, temperature, max_tokens) -> str`, chosen by
`configs/generation.yaml: provider`. Implementations:
- `FakeProvider`: fixture lookup (`evals/fixtures/fake_answers.jsonl`) or LangChain `FakeListLLM` for unit tests. A missing fixture raises an error;
- `OllamaProvider`: placeholder for a free local model;
- the judge (`LLMJudge`) is a client of the same protocol; `FakeJudge` reads fixture verdicts.
The agent uses LangChain's `FakeMessagesListChatModel`, because tool calling needs a chat-model interface.

## Consequences
- ➕ Zero cost, deterministic, no secrets in CI.
- ➕ Swapping the model is a one-line config change, and the eval harness becomes model-agnostic.
- ➖ Fixture answers are hand-written, so triad/judge **numbers reflect the fixtures, not model quality**. Every report must say so (RAID A-03).
- ➖ The minimal protocol drops features such as streaming and native structured output. They can be added as optional methods later.
- ⚖️ Two fake mechanisms (text provider, chat model for the agent) is a deliberate split.

## Alternatives considered
| Option | Pros | Cons | Why not |
|---|---|---|---|
| Call LangChain chat models directly everywhere | less code | provider leaks into every module, hard to fake consistently | coupling |
| Paid API with small budget | realistic outputs | cost, keys in CI, nondeterminism | violates constraints |
| Ollama from day one | real outputs, free | requires a local model; CI cannot run it | kept as an optional later step |
| LiteLLM proxy | many providers behind one API | extra dependency, still needs a backend | not needed yet |
