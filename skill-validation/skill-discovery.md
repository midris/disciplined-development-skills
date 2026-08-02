# Shared all-nine skill discovery — active validation

Owner: Task 1 validation protocol.
Affected skills: all nine.
Protocol: [README.md](README.md).

These preservation and approved target scenarios route from the nine frontmatter descriptions at control commit `4296647f0dff48a9e77b979ef07e813bf1f66db2` and the immutable parent-routing target described below.
Evaluators receive the descriptions and one request, never skill bodies or scoring criteria.
All scenarios use five fresh `gpt-5.6-sol` high-effort evaluators through the probed read-only, no-subagents transport.

## Supplied description context

The following text is extracted from the immutable nine-skill control bundle whose archive SHA-256 is `8f21c8267d005c349702ec94d6aff26c13a09bfbe29f2b43efcfbb37304f16e3`:

```text
adversarial-review-loop: Use when an adversarial review surfaces findings — including when successive rounds keep surfacing new, surface-different findings (possible shared root), and always when a review loop enters its third cycle. Applies to both internal (self-review, mid-flight work, code review) and external (a different model, a CI reviewer bot, a required reviewer) reviews.

adversarial-review: Use when code-reviewing or self-reviewing code, specs, plans, or designs — especially same-family pairings where the default reviewer posture risks compounding over-engineering, accepting unverified rationale, or missing unenumerated edge cases.

concise-writing: Use when writing or revising reader-facing prose — docs, READMEs, plans, specs, design notes, commit bodies, or code comments — that risks being verbose, padded, repetitive, wordy, or bulky; also when asked to tighten, trim, shorten, or "get to the point". Excludes skill and reference authoring.

disciplined-development: Use when starting, resuming, or carrying out development work; writing code, plans, specs, designs, or documentation; fixing bugs or review findings; working from an active plan; delegating to subagents; or approaching verification, commit, review, PR, or completion boundaries.

disciplined-research: Use before stating any load-bearing fact in a commit, plan, spec, doc, PR body, code review comment, README, code edit, status update, or summary — project claims (schema, handlers, fixtures, file contents, git history, summaries, quotes, recaps) or external/web claims (library versions, framework features, CLI behavior, current public state). Especially when stating specifics another reader will quote downstream without re-verifying.

dispatching-development-subagents: Use when dispatching a development subagent whose code changes you will integrate — an implementation task, a fix for a review finding, or a parallel batch of changes. Triggers: "dispatch a subagent", "spawn an agent", delegating a fix, fanning a change out across files, or before trusting a subagent's commits or diff.

lean-plan-writing: Use with `superpowers:writing-plans` whenever the deliverable is a plan or spec — new plans, plan edits, spec drafts, spec amendments. Triggered by "write a plan for X", "draft a spec", "update the plan", "edit the design doc", "add a task to the plan".

sweeping-stale-references: Use when changing a load-bearing fact that appears in multiple places — renaming a symbol (rename refactor, find references, find usages), updating a documented behavior, changing a schema, amending a spec constraint, propagating a cascading change. Also when a reviewer flags ONE stale reference, before fixing it.

writing-explicit-rationale: Use when a plan, spec, design, or code choice could be mistaken for an oversight: descoping, deferring, taking a shortcut, making an exception, or choosing among defensible alternatives. Also use when review re-litigates a decision or its rationale would otherwise live only in chat, a commit message, or a PR description.
```

The target arm replaces only the `disciplined-development` line with:

```text
disciplined-development: Use when doing development work. If available, load this parent with every applicable companion. Triggers: starting/resuming work; writing/reviewing code, plans, specs, designs, or docs; researching project or external facts; bug/finding fixes; active-plan work; delegation; and verification, commit, review, PR, or completion boundaries.
```

All other descriptions are byte-identical to control.
The read-only target bundle’s canonical content-manifest SHA-256 is `52fd9eb8c411fcc5d42bfa4590992914c2f7a20a494f6dc7868f82c85691103b`; its changed parent file SHA-256 is `21a46fb9b80cf29862a5e8ee5953fc6a3b3271da044eca60ac75b7060f43562e`.

## Exact evaluator prompt

For the control arm, replace `<SUPPLIED DESCRIPTION CONTEXT>` with the complete
nine-description control block above. For the target arm, byte-copy that complete
control block and replace only its `disciplined-development` line with the complete
target line above. Replace `<REQUEST>` with the scenario's exact request; make no
other change:

```text
You are a fresh, read-only skill-routing evaluator.
Do not inspect files, use skill bodies, edit anything, or dispatch agents.
Given the nine local skill descriptions below and one user request, select every local skill whose description directly applies now.
Do not select a skill merely because it might become useful later.
Return only a JSON array of selected local skill names in alphabetical order.

<SUPPLIED DESCRIPTION CONTEXT>

User request: <REQUEST>
```

## Active catalog definitions

Required names are positive routing, prohibited names are negative routing, and optional names record tolerated ambiguity without claiming positive protection.
The allowed-set column therefore maps each scenario to all nine descriptions: required, prohibited, or explicitly ambiguous.
All are discovery-type scenarios protecting each skill’s frontmatter `description`.
`DISC-01`, `DISC-03`, `DISC-05`, and `DISC-06` are approved targets for mandatory parent co-selection; the other five are preservation scenarios and target-arm regressions.
The supplied skill context is the description block above; no body, sibling procedure, or scoring rubric is supplied.

| ID | Exact request | Allowed output sets in the evaluator-withheld rubric | Primary protected promise | Rerun trigger |
|---|---|---|---|---|
| `DISC-01` | `Review only the API design text I provide for internal logical edge cases; do not inspect files, state repository or external facts, edit anything, or handle existing findings.` | Exactly `adversarial-review` and `disciplined-development`; no other skill | Initial text-bounded adversarial review routes to `adversarial-review`, not research, remediation, or implementation dispatch | Any candidate description, fixed prompt, request, or allowed set changes |
| `DISC-02` | `An external reviewer has already reported two defects. Help me handle those findings.` | Exactly `adversarial-review-loop` and `disciplined-development`; no other skill | Already-surfaced findings route to the loop, not a new review | Same |
| `DISC-03` | `Shorten this purely stylistic README sentence without adding or changing factual claims: "Our setup process is simple, straightforward, and easy to follow because it is not complicated."` | Exactly `concise-writing` and `disciplined-development`; no other skill | Ordinary padded reader-facing prose routes to concision without creating a research-composition cell | Same |
| `DISC-04` | `Resume implementation from the active plan and take the work through verification and commit.` | Must include `disciplined-development`; may also include `disciplined-research`; no other skill | Active-plan implementation and boundary discipline route to the parent | Same |
| `DISC-05` | `Check the repository and tell me which handler processes POST /orders.` | Exactly `disciplined-development` and `disciplined-research` | A downstream-quotable project fact routes to research within the parent development workflow | Same |
| `DISC-06` | `Spawn a development subagent to implement the pagination fix; I will integrate its diff.` | Exactly `disciplined-development` and `dispatching-development-subagents`; no other skill | Integrated implementation delegation routes to the dispatch companion | Same |
| `DISC-07` | `Write a plan to add CSV export.` | Must include `disciplined-development` and `lean-plan-writing`; may also include `concise-writing` and `disciplined-research`; no other skill | A plan deliverable routes to lean planning | Same |
| `DISC-08` | `Rename user_id to account_id everywhere it appears in code and documentation.` | Must include `disciplined-development` and `sweeping-stale-references`; may also include `disciplined-research`; no other skill | A cascading multi-surface rename routes to stale-reference sweeping | Same |
| `DISC-09` | `We are deliberately skipping retries as a temporary shortcut. Record that choice beside the code so it is not mistaken for an oversight.` | Must include `disciplined-development` and `writing-explicit-rationale`; may also include `concise-writing` and `disciplined-research`; no other skill | An intentional shortcut at risk of looking accidental routes to explicit rationale | Same |

The rubric first requires a JSON array whose names are in ascending alphabetical
order, then compares its selected-name set with the allowed sets above.
A missing primary skill, any non-allowed skill, non-alphabetical order, prose outside
the JSON array, or malformed output fails that repetition.

An external cadence review later found that the recorded rubric ignored the prompt's
alphabetical-order constraint. That scoring-contract repair invalidated every control
and target result below; both complete arms restarted at zero without changing the
descriptions, requests, or evaluator prompt.

The first run exposed a flawed-rubric gate rather than a skill inconsistency: the evaluator instruction required every directly applicable description, while the initial rubric rejected reasonable cross-cutting `disciplined-research` and `concise-writing` selections in `DISC-04`, `DISC-07`, `DISC-08`, and `DISC-09`.
A fresh Sol-high validation-design review confirmed the classification and the scenario-specific optional sets above.
The requests did not change; all four affected scenarios restarted at zero, and the superseded outputs remain scratch-only.
That restart exposed one remaining `DISC-09` rubric miss when an evaluator selected `disciplined-research` for the code-adjacent load-bearing choice.
A second fresh Sol-high review again classified the rubric as flawed, added `disciplined-research` to `DISC-09`'s optional set, and required `DISC-09` alone to restart at zero.
A later cadence review found a second rubric class: `disciplined-development` was optional even where its description directly names review, findings, documentation, delegation, plans, or code changes.
The prior results for `DISC-01`, `DISC-02`, `DISC-03`, `DISC-06`, `DISC-07`, `DISC-08`, and `DISC-09` were therefore superseded, their rubrics now require the parent, and all seven control baselines restarted at zero without changing their requests or evaluator prompt.
The approved parent-routing target then exposed that the original `DISC-01` request necessarily produced factual review findings, making `disciplined-research` directly applicable despite a rubric that prohibited it.
A fresh Sol-high classification called that scenario/rubric flawed.
To preserve an atomic review-routing cell instead of creating a three-skill composition test, `DISC-01` was narrowed to supplied-text logic, its earlier repetitions were superseded, and it restarted at zero.
The first parent-target full-suite attempt exposed the same problem in `DISC-03`: an unspecified README paragraph could contain load-bearing facts, so several evaluators reasonably selected `disciplined-research`.
`DISC-03` was repaired to supply a purely stylistic sentence and forbid factual changes, and its prior repetitions were superseded before restart.
After the first complete target passed, a user-approved description compression replaced
the action-specific research trigger with `project/external research`. Its fresh full
target arm scored 44/45: `DISC-01` added prohibited `disciplined-research` once.
A fresh Sol-high classification identified a compact-wording regression, not a rubric
flaw or infrastructure error. The research trigger was restored to action-specific
wording, all 45 compact-candidate results were superseded, and the complete target arm
restarted at zero.

## Control and target results

Control is full commit `4296647f0dff48a9e77b979ef07e813bf1f66db2` and archive SHA-256 `8f21c8267d005c349702ec94d6aff26c13a09bfbe29f2b43efcfbb37304f16e3`.
Target is the immutable bundle with content-manifest SHA-256 `52fd9eb8c411fcc5d42bfa4590992914c2f7a20a494f6dc7868f82c85691103b`.

| ID | Sol-high control | Exact control misses | Target GREEN | Target route summary | Infrastructure errors | Sol-low control | Cleaned Sol-high | Cleaned Sol-low |
|---|---|---|---|---|---:|---|---|---|
| `DISC-01` | **1/5 watched RED** | Parent omitted 4/5 | **5/5 PASS** | 5 exact | 0 | Task 11 | Task 26 | Task 27 |
| `DISC-02` | **5/5 PASS** | None; 5 exact | **5/5 PASS** | 5 exact | 0 | Task 11 | Task 26 | Task 27 |
| `DISC-03` | **1/5 watched RED** | Parent omitted 4/5 | **5/5 PASS** | 5 exact | 0 | Task 11 | Task 26 | Task 27 |
| `DISC-04` | **5/5 PASS** | None; 5 parent-only | **5/5 PASS** | 2 required-only, 3 with optional research | 0 | Task 11 | Task 26 | Task 27 |
| `DISC-05` | **0/5 watched RED** | Parent omitted 5/5 | **5/5 PASS** | 5 exact | 0 | Task 11 | Task 26 | Task 27 |
| `DISC-06` | **4/5 watched RED** | Parent omitted 1/5 | **5/5 PASS** | 5 exact | 0 | Task 11 | Task 26 | Task 27 |
| `DISC-07` | **5/5 PASS** | None; 1 required-only, 4 with allowed optional variation | **5/5 PASS** | 4 required-only, 1 with optional research | 0 | Task 11 | Task 26 | Task 27 |
| `DISC-08` | **5/5 PASS** | None; 2 required-only, 3 with optional research | **5/5 PASS** | 3 required-only, 2 with optional research | 0 | Task 11 | Task 26 | Task 27 |
| `DISC-09` | **5/5 PASS** | None; 1 required-only, 4 with allowed optional variation | **5/5 PASS** | 1 required-only, 4 with allowed optional variation | 0 | Task 11 | Task 26 | Task 27 |

Run metadata for both active arms: Codex CLI 0.146.0; `gpt-5.6-sol`; high reasoning effort; Superpowers 6.2.0; five fresh processes per scenario; maximum concurrency three; immutable description context as identified above; no skill bodies or sibling skills available; rubric withheld; every result manually scored, including JSON shape and alphabetical order; zero counted infrastructure errors; run date 2026-08-01.

Normalized per-repetition codes below preserve the manually scored outcomes without
committing evaluator transcripts. `E` is the exact required set; `R` is the
required-only set where optional skills are allowed; `+Q`, `+C`, and `+CQ` add
`disciplined-research`, `concise-writing`, or both. `F-parent` is FAIL because the
required parent was omitted. Every listed response was a JSON array in ascending
alphabetical order, so no cell has an additional shape, prose, or order miss.

| ID | Control R1 | R2 | R3 | R4 | R5 | Target R1 | R2 | R3 | R4 | R5 |
|---|---|---|---|---|---|---|---|---|---|---|
| `DISC-01` | F-parent | E | F-parent | F-parent | F-parent | E | E | E | E | E |
| `DISC-02` | E | E | E | E | E | E | E | E | E | E |
| `DISC-03` | E | F-parent | F-parent | F-parent | F-parent | E | E | E | E | E |
| `DISC-04` | R | R | R | R | R | +Q | R | R | +Q | +Q |
| `DISC-05` | F-parent | F-parent | F-parent | F-parent | F-parent | E | E | E | E | E |
| `DISC-06` | E | E | E | F-parent | E | E | E | E | E | E |
| `DISC-07` | +Q | +CQ | +CQ | +CQ | R | +Q | R | R | R | R |
| `DISC-08` | R | R | +Q | +Q | +Q | +Q | R | +Q | R | R |
| `DISC-09` | +C | +Q | +CQ | R | +C | +C | +Q | +Q | R | +C |

Superseded wording and rubric experiments and focused implementation-feedback runs
remain scratch-only because their changed contracts restarted the affected scenarios
at zero. Three full target attempts were terminated after evaluable failures, and
none used the final contract: `target-green-v4` used superseded parent wording that
did not name reviewing; `target-green-v5-full` used superseded parent wording that
did not name research and the ambiguous original `DISC-03` request; and
`target-green-v6-full` used the final parent wording but the same ambiguous
`DISC-03` request. Their failures caused the documented wording or prompt repairs;
their later termination errors are not behavioral results or counted infrastructure
errors. Both final complete arms restarted at zero after those repairs. The later
44/45 compact target is likewise preserved only as a superseded wording experiment;
the action-specific repair's complete target restart is the active result above.
