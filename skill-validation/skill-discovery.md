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
`DISC-01`, `DISC-03`, `DISC-05`, and `DISC-06` are approved targets for mandatory parent co-selection; the other five completed cells are preservation scenarios and target-arm regressions.
`DISC-10` is preservation coverage and also exercises the already approved
parent-co-selection behavior on the parent and Task 2A target arms.
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
| `DISC-08` | ``Perform only a mechanical identifier replacement: rename the exact identifier `user_id` to `account_id` everywhere it occurs in code and documentation. Do not rewrite, tighten, or otherwise revise surrounding prose.`` | Must include `disciplined-development` and `sweeping-stale-references`; may also include `disciplined-research`; no other skill | A cascading multi-surface rename routes to stale-reference sweeping | Same |
| `DISC-09` | `We are deliberately skipping retries as a temporary shortcut. Record that choice beside the code so it is not mistaken for an oversight.` | Must include `disciplined-development` and `writing-explicit-rationale`; may also include `concise-writing` and `disciplined-research`; no other skill | An intentional shortcut at risk of looking accidental routes to explicit rationale | Same |
| `DISC-10` | `Update the launch plan to defer multilingual invoices. The billing vendor's locale API remains unstable, so launch accepts English-only invoices until the API stabilizes. That rationale currently exists only in the PR description.` | Must include `disciplined-development`, `lean-plan-writing`, and `writing-explicit-rationale`; may also include `concise-writing`, `disciplined-research`, and `sweeping-stale-references`; no other skill | A plan deferral whose reasoning is non-durable routes to explicit rationale and lean planning within the parent development workflow | Same |

The rubric first requires a JSON array whose names are in ascending alphabetical
order, then compares its selected-name set with the allowed sets above.
A missing primary skill, any non-allowed skill, non-alphabetical order, prose outside
the JSON array, or malformed output fails that repetition.

The first frozen `DISC-10` scoring pass prohibited `sweeping-stale-references`,
although changing the launch deferral is a load-bearing plan change.
A fresh Sol-high failure classification marked that omission a rubric defect.
The allowed optional set was repaired, and the unchanged 15 outputs were rescored.

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

The Task 2A concise-authoring target's first complete shared arm scored 44/45 because
one `DISC-08` evaluator selected `concise-writing` for the original “rename … in code
and documentation” request. A fresh Sol-high validation-design review classified the
request as flawed: it did not distinguish mechanical replacement from prose revision.
The exact request above now forbids surrounding-prose changes. `DISC-08` alone
restarted at zero for the control, parent-target, and Task 2A target arms; all three
repaired arms passed 5/5. A later staged adversarial review found that the Task 2A
description extractor had also dropped the apostrophe from `subagent's commits` in
the unrelated dispatch description. Because that changed supplied context for every
Task 2A cell, all 45 results—including the repaired `DISC-08` target—were superseded.
The complete Task 2A arm restarted at zero with the byte-identical description and
passed 45/45. Neither the earlier 44/45 arm nor the malformed-context results are
active.

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
| `DISC-08` | **5/5 PASS** | None; 3 required-only, 2 with optional research | **5/5 PASS** | 3 required-only, 2 with optional research | 0 | Task 11 | Task 26 | Task 27 |
| `DISC-09` | **5/5 PASS** | None; 1 required-only, 4 with allowed optional variation | **5/5 PASS** | 1 required-only, 4 with allowed optional variation | 0 | Task 11 | Task 26 | Task 27 |
| `DISC-10` | **5/5 PASS** | None; 1 with optional research, 4 with optional research and sweeping | **5/5 PASS** | 4 with optional research and sweeping, 1 also with optional concise writing | 0 | Task 11 | Task 26 | Task 27 |

Run metadata for both completed `DISC-01`–`DISC-09` arms: Codex CLI 0.146.0; `gpt-5.6-sol`; high reasoning effort; Superpowers 6.2.0; five fresh processes per scenario; maximum concurrency three; immutable description context as identified above; no skill bodies or sibling skills available; rubric withheld; every result manually scored, including JSON shape and alphabetical order; zero counted infrastructure errors; run date 2026-08-01 except the repaired `DISC-08` control and parent-target arms, which ran 2026-08-02.
`DISC-10` used the same configuration for all three arms on 2026-08-03 with zero
infrastructure errors.

Normalized per-repetition codes below preserve the manually scored outcomes without
committing evaluator transcripts. `E` is the exact required set; `R` is the
required-only set where optional skills are allowed; `+Q`, `+C`, `+S`, and their
combinations add `disciplined-research`, `concise-writing`, and
`sweeping-stale-references`. `F-parent` is FAIL because the
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
| `DISC-08` | R | +Q | +Q | R | R | +Q | R | +Q | R | R |
| `DISC-09` | +C | +Q | +CQ | R | +C | +C | +Q | +Q | R | +C |
| `DISC-10` | +Q | +QS | +QS | +QS | +QS | +QS | +CQS | +QS | +QS | +QS |

### Task 2A concise-authoring target

The immutable Task 2A description bundle uses the approved parent-target line and
replaces only the `concise-writing` line with:

```text
concise-writing: Use when writing or revising reader-facing prose — docs, READMEs, plans, specs, design notes, commit bodies, or code comments — that risks being verbose, padded, repetitive, wordy, or bulky; also when asked to tighten, trim, shorten, or "get to the point".
```

Its nine-file archive SHA-256 is
`3bd1eee765a64c6d239f50ee15ae13b77509f4542fe66bb19efa2bbea73f7cee`;
its canonical content-manifest SHA-256 is
`87e221b188180735c028efbc3681745741a2459eda1268bfe06ed62fe2545dca`;
and the changed concise-description file SHA-256 is
`e6b0a334c5288a0f2e80ecf84e9e502d86169fbbac31f96c1af203df4c6034b4`.
All other description files are byte-identical to the active parent-target bundle.

Every supplied Task 2A description is independently replayable from this manifest:

| Source kind | Full revision | Source path | Bundle path | Extracted file SHA-256 |
|---|---|---|---|---|
| Repository | `bef0398689d6911d1b9baf95d8ad8ea123b263b4` | `skills/adversarial-review-loop/SKILL.md` | `descriptions/adversarial-review-loop.txt` | `38843f7718501f52116bfd4f95a6640cb16b560851767df540c808a1ed18cefa` |
| Repository | `bef0398689d6911d1b9baf95d8ad8ea123b263b4` | `skills/adversarial-review/SKILL.md` | `descriptions/adversarial-review.txt` | `509c3947e1e3f8241592f8799c4875180dd5acf9eb5d9a901c52fed1f08783ce` |
| Approved candidate | base `bef0398689d6911d1b9baf95d8ad8ea123b263b4`; file `6c3a838297da8b0a17a3f3978dd6e46c7e5794f9e7e34c4e6db760e941c942aa` | `skills/concise-writing/SKILL.md` | `descriptions/concise-writing.txt` | `e6b0a334c5288a0f2e80ecf84e9e502d86169fbbac31f96c1af203df4c6034b4` |
| Repository | `bef0398689d6911d1b9baf95d8ad8ea123b263b4` | `skills/disciplined-development/SKILL.md` | `descriptions/disciplined-development.txt` | `9d4593d761fcba9d3ec1e307b6133b531cd9cb1fc55c71ad3d6ad77a55f5aa7f` |
| Repository | `bef0398689d6911d1b9baf95d8ad8ea123b263b4` | `skills/disciplined-research/SKILL.md` | `descriptions/disciplined-research.txt` | `08db6253e8f468b5d193b8cf70e9c206ff8e4b1bebd037c3c598dbc2d7c56940` |
| Repository | `bef0398689d6911d1b9baf95d8ad8ea123b263b4` | `skills/dispatching-development-subagents/SKILL.md` | `descriptions/dispatching-development-subagents.txt` | `2cb085e9508cde5e40c199c4e209783b361e12b5db67715dda15641c6d9fa59e` |
| Repository | `bef0398689d6911d1b9baf95d8ad8ea123b263b4` | `skills/lean-plan-writing/SKILL.md` | `descriptions/lean-plan-writing.txt` | `b5b161c227f0571a586942242e727d53af678e7812cdfbdac58dd538d124160e` |
| Repository | `bef0398689d6911d1b9baf95d8ad8ea123b263b4` | `skills/sweeping-stale-references/SKILL.md` | `descriptions/sweeping-stale-references.txt` | `ef82cf69a782af1001fdd531532847008eb33083d298b487d6b08a2793f9c4fc` |
| Repository | `bef0398689d6911d1b9baf95d8ad8ea123b263b4` | `skills/writing-explicit-rationale/SKILL.md` | `descriptions/writing-explicit-rationale.txt` | `59b38bed4aa9eee7aaaf93c25d109d87b6f77c00d3dcb9b7cdcc66ca7e1f9711` |

| ID | Task 2A target GREEN | Route summary | Infrastructure errors |
|---|---|---|---:|
| `DISC-01` | **5/5 PASS** | 5 exact | 0 |
| `DISC-02` | **5/5 PASS** | 5 exact | 0 |
| `DISC-03` | **5/5 PASS** | 5 exact | 0 |
| `DISC-04` | **5/5 PASS** | 1 required-only, 4 with optional research | 0 |
| `DISC-05` | **5/5 PASS** | 5 exact | 0 |
| `DISC-06` | **5/5 PASS** | 5 exact | 0 |
| `DISC-07` | **5/5 PASS** | 1 required-only, 4 with optional research | 0 |
| `DISC-08` | **5/5 PASS** | 4 required-only, 1 with optional research | 0 |
| `DISC-09` | **5/5 PASS** | 3 required-only, 2 with allowed optional variation | 0 |
| `DISC-10` | **5/5 PASS** | 1 with optional research, 4 with optional research and sweeping | 0 |

Run metadata for completed `DISC-01`–`DISC-09`: Codex CLI 0.146.0;
`gpt-5.6-sol`; high reasoning effort; Superpowers 6.2.0; five fresh processes per scenario; maximum concurrency three;
immutable descriptions-only context above; rubric withheld; every result manually
scored for membership, JSON shape, and alphabetical order; zero infrastructure
errors; run date 2026-08-02.
The `DISC-10` Task 2A arm ran on 2026-08-03 with zero infrastructure errors.

| ID | Task 2A R1 | R2 | R3 | R4 | R5 |
|---|---|---|---|---|---|
| `DISC-01` | E | E | E | E | E |
| `DISC-02` | E | E | E | E | E |
| `DISC-03` | E | E | E | E | E |
| `DISC-04` | R | +Q | +Q | +Q | +Q |
| `DISC-05` | E | E | E | E | E |
| `DISC-06` | E | E | E | E | E |
| `DISC-07` | +Q | R | +Q | +Q | +Q |
| `DISC-08` | R | R | R | +Q | R |
| `DISC-09` | +CQ | R | R | +Q | R |
| `DISC-10` | +QS | +Q | +QS | +QS | +QS |

### Task 6 explicit-rationale target

The Task 6 target uses the Task 2A description bundle above and replaces only the
`writing-explicit-rationale` description with:

```text
writing-explicit-rationale: Use when a plan, spec, policy, design, or code choice needs durable reasoning to understand correctness or guide a future decision; especially for descopes, deferrals, exceptions, defensible alternatives, repeated re-litigation, or rationale that exists only in chat, a commit, or a PR.
```

The target skill file SHA-256 is
`a41d59faaea4be81e6cff5b2e35154f8b4b6d077afce6c0c6cd9a3d8cb82c3e6`;
the extracted description file SHA-256 is
`49f9ddd7c23538e308f713035a298a127bf4e346e41ab3269468680cbb572732`;
and the resulting nine-description canonical content-manifest SHA-256 is
`fde2cbadeffc7bf98b3428ac66de8aa2db90bb4e05cef89fda16788fb0a21c51`.
All other description files are byte-identical to the Task 2A manifest.

The complete ten-scenario target passed **50/50** on 2026-08-03 with zero
infrastructure errors.
Every response contained each required skill, no prohibited skill, a JSON array in
ascending alphabetical order, and no prose outside the array.

| ID | R1 | R2 | R3 | R4 | R5 |
|---|---|---|---|---|---|
| `DISC-01` | E | E | E | E | E |
| `DISC-02` | E | E | E | E | E |
| `DISC-03` | E | E | E | E | E |
| `DISC-04` | +Q | +Q | +Q | +Q | +Q |
| `DISC-05` | E | E | E | E | E |
| `DISC-06` | E | E | E | E | E |
| `DISC-07` | +CQ | R | R | +Q | +CQ |
| `DISC-08` | R | R | R | R | R |
| `DISC-09` | +C | +CQ | +C | +Q | +CQ |
| `DISC-10` | +Q | +QS | +CQS | +QS | +QS |

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
