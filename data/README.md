# Corpus: GitLab Handbook subset

- **Source**: https://gitlab.com/gitlab-com/content-sites/handbook (Hugo site, Markdown under `content/handbook/`)
- **License**: content is CC BY-SA 4.0 (badge in the footer of https://handbook.gitlab.com). Keep attribution;
  the repository's `LICENSE` file (MIT) covers GitLab *software*, not the handbook text.
- **Not committed**: everything under `data/raw/`, `data/processed/`, `data/index/` is git-ignored.

## Subset (~130–200 pages)

| Section | Path in repo | Approx. files (Nov 2026) |
|---|---|---|
| People policies | `content/handbook/people-policies/` | ~13 |
| People group | `content/handbook/people-group/` | ~89 |
| Total rewards | `content/handbook/total-rewards/` | ~30 |
| Optional: engineering onboarding/workflow | `content/handbook/engineering/workflow/` etc. | pick to reach ~200 |

Counts are from the GitLab API at the time of writing and will drift.

## Download (sparse checkout, pinned commit)

```bash
mkdir -p data/raw && cd data/raw
git clone --depth 1 --filter=blob:none --sparse https://gitlab.com/gitlab-com/content-sites/handbook.git
cd handbook
git sparse-checkout set content/handbook/people-policies content/handbook/people-group content/handbook/total-rewards
git rev-parse HEAD > ../../CORPUS_COMMIT   # pin the snapshot: golden set is only valid for this commit
```

Or run `python scripts/download_corpus.py` (stub, step 0.2 in TODO.md).

## Why pin the commit

The golden set (`evals/golden_set.jsonl`) references documents and evidence quotes. If the handbook
changes, evidence may disappear and retrieval metrics drop for reasons unrelated to our code.
`data/CORPUS_COMMIT` is the corpus version; see RAID item D-01.
