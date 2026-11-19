# Architecture review

Part A is a reusable template. Part B is the filled review of this project at scaffold stage (2026-11-19).

## Part A: template

**Review metadata**: system, version/commit, reviewers, date, documents reviewed (HLD, ADRs, RAID).

| Area | Checklist questions | Rating (🟢/🟡/🔴) | Notes |
|---|---|---|---|
| Security | secrets handling? authn/authz? data exfiltration paths (LLM calls)? prompt injection? dependency vulnerabilities? | | |
| Scalability | data volume growth? index rebuild time? concurrency? stateless services? | | |
| Reliability | failure modes defined? timeouts/retries? graceful refusal? regression protection? | | |
| Observability | logs/metrics/traces? per-request traceability (question → chunks → answer)? eval run artefacts? | | |
| Data governance | data source licence? lineage/versioning? PII? retention? access control on documents? | | |
| Cost | cost per query? CI cost? model choice vs budget? | | |
| Maintainability | module boundaries? config vs code? tests? ADRs up to date? | | |

Findings: ID, severity (High/Medium/Low), finding, recommendation, owner, due.
Outcome: Approved / Approved with conditions / Not approved.

## Part B: review of kb-assistant-evals (scaffold)

| Area | Rating | Notes |
|---|---|---|
| Security | 🟡 | no secrets, no external calls ✔; no ACL model (out of scope); prompt injection not addressed |
| Scalability | 🟢 (scope) | ~200 pages in-memory BM25 fine; full handbook (~thousands of pages) would need a persisted index |
| Reliability | 🟡 | refusal + citations designed; gate covers retrieval only; judge unvalidated yet |
| Observability | 🟢 | per-query JSONL, trajectories, config fingerprint planned; no runtime tracing (no service) |
| Data governance | 🟢 | CC BY-SA attribution, pinned commit, data not committed; HR corpus is public (no PII) |
| Cost | 🟢 | 0 € by design (ADR-0003) |
| Maintainability | 🟢 | typed contracts, factories, ADRs, standards; risk: LangChain churn (D-02) |

### Findings

| ID | Severity | Finding | Recommendation | Owner | Due |
|---|---|---|---|---|---|
| F-01 | High | Gate does not detect generation regressions (prompt / model changes) | add non-blocking triad job; require report 01 rerun for prompt changes | me | after stage 02 |
| F-02 | High (prod) | No document permission model | design ACL-aware retrieval (filter before ranking, pass user claims) before any real deployment | — | prod only |
| F-03 | Medium | Golden set size limits statistical power | grow to 60–100 items; add held-out split | me | stage 01 end |
| F-04 | Medium | Single annotator for judge validation | add a second annotator for a subset and report inter-annotator kappa | me | optional |
| F-05 | Low | Character-based chunk sizing | revisit with tokenizer of the chosen model | me | when real LLM |
| F-06 | Low | Agent evaluated only with scripted trajectories | rerun stage 04 with a real local model | me | beyond |

### Outcome
**Approved with conditions**: F-01 and F-03 to be addressed during stages 01–03. F-02 is a precondition for any production use.
