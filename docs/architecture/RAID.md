# RAID log

Scale: Impact / Likelihood = H / M / L. Owner = me unless stated. Review at the end of every stage.

## Risks

| ID | Description | Impact | Likelihood | Mitigation | Owner | Status |
|---|---|---|---|---|---|---|
| R-01 | Golden set too small (~30) → metric deltas are noise | H | H | report n and "1 question = x pp"; strict regression rule; grow set over time | me | Open |
| R-02 | Judge disagrees with humans but is trusted anyway | H | M | stage 02 kappa + bias probes before any judge-based decision; triad non-blocking | me | Open |
| R-03 | Flaky CI from nondeterminism (dense retrieval, LLM) | H | M | gate uses BM25 only; deterministic tie-break; determinism check in report 03 | me | Mitigated by design |
| R-04 | Generation-only regressions not caught by gate | M | M | non-blocking triad job later; prompt changes require report 01 rerun | me | Accepted |
| R-05 | Overfitting config to the golden set | M | M | held-out subset (≈20%) never used for tuning; paraphrase items | me | Open |
| R-06 | No document-level access control: in a real company the assistant could leak restricted docs | H (prod) | H (prod) | out of scope; documented production requirement: ACL filter before ranking | — | Accepted (learning scope) |
| R-07 | Prompt injection via documents | M | L (public corpus) | out of scope; listed in architecture review | — | Accepted |
| R-08 | Fixture-based numbers mistaken for model quality | M | M | every report states provider = fake; fixtures README | me | Open |
| R-09 | Base repo (LocalSmartRAG) design assumptions (Chinese text) don't transfer | L | M | re-validate chunk sizes in stage 01; own tests | me | Open |

## Assumptions

| ID | Assumption | Validation |
|---|---|---|
| A-01 | GitLab Handbook HR/benefits pages are a realistic stand-in for internal enterprise docs | structure: policies, country-specific rules, cross-links ✔ |
| A-02 | ~130–200 pages are enough to show retrieval failure modes | stage 01 error analysis |
| A-03 | Hand-written fixtures are sufficient to build and test the harness | yes for mechanics; not for quality claims (R-08) |
| A-04 | A single annotator (me) is acceptable for a learning project | documented as a limit in report 02 |
| A-05 | Characters approximate tokens well enough for chunk sizing | revisit when a real LLM is attached |

## Issues

| ID | Issue | Impact | Action | Status |
|---|---|---|---|---|
| I-01 | Handbook pages contain Hugo shortcodes (`{{% panel %}}`) and HTML (iframes) that pollute text | M | cleaner step 0.4 + test | Open |
| I-02 | Some policies live in `people-group/` while `people-policies/` only links to them (e.g. parental leave) | M | include both sections in subset; `multi-fact` items | Open |

## Dependencies

| ID | Dependency | Type | Risk if it changes | Mitigation |
|---|---|---|---|---|
| D-01 | GitLab Handbook content (CC BY-SA 4.0) | data | pages edited → evidence quotes disappear | pinned `data/CORPUS_COMMIT`; `validate_against_corpus` |
| D-02 | LangChain (`langchain-core`, `langchain-community`) | library | frequent breaking changes | version ranges in pyproject; small surface used |
| D-03 | `rank_bm25` | library | low activity upstream | tiny, pure Python; could vendor |
| D-04 | GitHub Actions + `astral-sh/setup-uv` | CI | action versions | pinned major versions |
| D-05 | `BAAI/bge-small-en-v1.5` from Hugging Face (optional) | model | availability, licence | optional path only; not in CI |
| D-06 | LocalSmartRAG (MIT) as design reference | design | none at runtime | not a runtime dependency |
