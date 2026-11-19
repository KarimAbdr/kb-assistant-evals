"""Agent loop with a step budget.

LLM: FakeMessagesListChatModel with scripted AIMessage(tool_calls=...) per golden question
(evals/fixtures/agent_scripts.jsonl) -> deterministic trajectories, zero cost.
Hand-written loop (not a prebuilt agent) on purpose: every step is visible and loggable.
"""

from __future__ import annotations

from kb_assistant.agent.trajectory import TrajectoryLogger


def run_agent(question: str, item_id: str, tools: list, chat_model: object,
              logger: TrajectoryLogger, max_steps: int = 6) -> str:
    """model -> tool calls -> tool results -> model ... until a final answer or max_steps.
    Every step is logged. Returns the final answer (or a "step budget exhausted" marker). TODO(step-4.2)"""
    raise NotImplementedError("TODO(step-4.2)")
