"""Shared fixtures: tiny in-memory corpus so unit tests never need the downloaded handbook."""

from __future__ import annotations

import pytest

from kb_assistant.types import Page


@pytest.fixture
def tiny_pages() -> list[Page]:
    """Two short synthetic pages with headings and a code block."""
    return [
        Page(
            doc_id="people-policies/demo-leave",
            url="https://handbook.gitlab.com/handbook/people-policies/demo-leave/",
            title="Demo leave",
            section="people-policies",
            text="# Leave\n\nIntro.\n\n## Parental leave\n\nEligible from day one.\n\n```\ncode block\n```\n",
        ),
        Page(
            doc_id="total-rewards/demo-benefit",
            url="https://handbook.gitlab.com/handbook/total-rewards/demo-benefit/",
            title="Demo benefit",
            section="total-rewards",
            text="# Benefit\n\n6 free sessions per year.\n",
        ),
    ]
