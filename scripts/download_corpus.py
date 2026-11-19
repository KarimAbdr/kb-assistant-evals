"""Download the GitLab Handbook subset into data/raw/ (sparse git checkout).

TODO(step-0.2): implement with subprocess calls to git (see data/README.md):
  1. sparse clone into data/raw/handbook
  2. `git sparse-checkout set` the sections from configs (people-policies, people-group, total-rewards)
  3. if data/CORPUS_COMMIT exists -> fetch and checkout exactly that commit (pinned snapshot,
     used by CI); otherwise checkout HEAD and write its SHA to data/CORPUS_COMMIT
  4. idempotent: if data/raw/handbook already at that commit, do nothing (CI cache hit)
  5. print the number of .md files downloaded
"""

from __future__ import annotations

SECTIONS: list[str] = [
    "content/handbook/people-policies",
    "content/handbook/people-group",
    "content/handbook/total-rewards",
]


def main() -> None:
    raise NotImplementedError("TODO(step-0.2)")


if __name__ == "__main__":
    main()
