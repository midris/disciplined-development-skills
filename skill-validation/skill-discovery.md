# Shared all-nine skill discovery — active validation

Owner: Task 1 validation protocol.
Affected skills: all nine.
Protocol: [README.md](README.md).

These preservation and approved target scenarios route from the nine frontmatter descriptions at control commit `4296647f0dff48a9e77b979ef07e813bf1f66db2` and the immutable parent-routing target described below.
Evaluators receive the descriptions and one request, never skill bodies or scoring criteria.
All scenarios use five fresh `gpt-5.6-sol` high-effort evaluators through the probed read-only, no-subagents transport.

Task 18A froze the pre-draft contracts without changing tracked descriptions and
completed the required repaired control backfills.
The exact universal trigger makes `disciplined-research` required in every
`DISC-01`–`DISC-10` request because each requested answer or artifact states at least
one factual claim; origin in supplied user text, mechanical transformation, and
private or scratch destination create no exemption.
The prior allowed sets and results below remain explicitly historical evidence under
their own rubrics; the Task 18A repaired allowed sets and final controls are the
active record.

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

### Historical pre-Task-18A allowed sets

The exact evaluator-withheld allowed sets that govern all prior `DISC-01`–`DISC-10`
results are preserved separately in
[the immutable historical rubric](fixtures/skill-discovery/rubrics/pre-task-18a-disc-01-10.md)
at SHA-256
`d0f9ff72188cc5af86ec238255da6e2615e8f8470e1f9a90aa980d5deda86da1`.
Those results are never rescored against the repaired contracts below.

| ID | Historical research classification |
|---|---|
| `DISC-01` | Optional |
| `DISC-02` | Prohibited |
| `DISC-03` | Prohibited |
| `DISC-04` | Optional |
| `DISC-05` | Required |
| `DISC-06` | Prohibited |
| `DISC-07` | Optional |
| `DISC-08` | Optional |
| `DISC-09` | Optional |
| `DISC-10` | Optional |

### Task 18A repaired allowed sets

Required names are positive routing, prohibited names are negative routing, and optional names record tolerated ambiguity without claiming positive protection.
The allowed-set column therefore maps each scenario to all nine descriptions: required, prohibited, or explicitly ambiguous.
All are discovery-type scenarios protecting each skill’s frontmatter `description`.
The final Task 18A role split is target RED for `DISC-01`, `DISC-02`, `DISC-03`,
`DISC-04`, `DISC-06`, `DISC-07`, `DISC-08`, `DISC-09`, and `DISC-11`;
preservation for `DISC-05` and `DISC-10`; `DISC-12` is the later target for the
non-development response/interaction boundary. Research remains required in every
case.
`DISC-04` is target behavior because research changed from optional to required;
its post-freeze 4/5 high result is a watched RED. `DISC-05` preserves the exact
research route after allowing response-only `concise-writing`; `DISC-10` preserves
its exact 5/5 Sol-high control. Sol-low is robustness evidence only.
The supplied skill context is the description block above; no body, sibling procedure, or scoring rubric is supplied.

| ID | Exact request | Allowed output sets in the evaluator-withheld rubric | Primary protected promise | Rerun trigger |
|---|---|---|---|---|
| `DISC-01` | `Review only the API design text I provide for internal logical edge cases; do not inspect files, state repository or external facts, edit anything, or handle existing findings.` | Must include `adversarial-review`, `disciplined-development`, and `disciplined-research`; may also include `concise-writing`; no other skill | The review's findings are factual claims about supplied source text, so supplied-text acquisition does not make research optional | Any candidate description, fixed prompt, request, or allowed set changes |
| `DISC-02` | `An external reviewer has already reported two defects. Remediate those reported findings; do not perform a new review.` | Must include `adversarial-review-loop`, `disciplined-development`, and `disciplined-research`; may also include `concise-writing`; no other skill | Remediating the reported defects states claims about the findings and affected work; the reviewer report is a source, not an exemption; a new review is not the requested action | Same |
| `DISC-03` | `Shorten this purely stylistic README sentence without adding or changing factual claims: "Our setup process is simple, straightforward, and easy to follow because it is not complicated."` | Exactly `concise-writing`, `disciplined-development`, and `disciplined-research`; no other skill | The rewritten sentence still states the supplied setup-ease claim even though it adds or changes no factual content | Same |
| `DISC-04` | `Resume implementation from the active plan and take the work through verification and commit.` | Must include `disciplined-development` and `disciplined-research`; may also include `concise-writing`; no other skill | Implementation, verification, and commit outputs state current-project and completion claims | Same |
| `DISC-05` | `Check the repository and tell me which handler processes POST /orders.` | Must include `disciplined-development` and `disciplined-research`; may also include `concise-writing`; no other skill | A downstream-quotable project fact routes to research within the parent development workflow | Same |
| `DISC-06` | `Spawn a development subagent to implement the pagination fix; I will integrate its diff.` | Exactly `disciplined-development`, `disciplined-research`, and `dispatching-development-subagents`; no other skill | The dispatch states factual scope, finding, and governing-context claims before the subagent can act | Same |
| `DISC-07` | `Write a plan to add CSV export.` | Must include `disciplined-development`, `disciplined-research`, and `lean-plan-writing`; may also include `concise-writing`; no other skill | The plan artifact states factual premises and current/future decision boundaries; plan destination does not lower the trigger | Same |
| `DISC-08` | ``Perform only a mechanical identifier replacement: rename the exact identifier `user_id` to `account_id` everywhere it occurs in code and documentation. Do not rewrite, tighten, or otherwise revise surrounding prose.`` | Must include `disciplined-development`, `disciplined-research`, and `sweeping-stale-references`; may also include `concise-writing`; no other skill | Search results, occurrence coverage, edits, and completion are factual claims even when the replacement is mechanical; the concise-writing description also literally permits revision of reader-facing docs | Same |
| `DISC-09` | `We are deliberately skipping retries as a temporary shortcut. Record that choice beside the code so it is not mistaken for an oversight.` | Must include `disciplined-development`, `disciplined-research`, and `writing-explicit-rationale`; may also include `concise-writing`; no other skill | Recording the user-originated retry decision still states a fact about project behavior and intent | Same |
| `DISC-10` | `Update the launch plan to defer multilingual invoices. The billing vendor's locale API remains unstable, so launch accepts English-only invoices until the API stabilizes. That rationale currently exists only in the PR description.` | Must include `disciplined-development`, `disciplined-research`, `lean-plan-writing`, and `writing-explicit-rationale`; may also include `concise-writing` and `sweeping-stale-references`; no other skill | The plan repeats vendor-state, launch-scope, and rationale-location claims supplied by the user; source origin does not exempt them | Same |
| `DISC-11` | ``Privately note for yourself in an uncommitted software-development scratch file: `The checkout service retries declined authorizations three times.` Do not share or publish the note.`` | Must include `disciplined-development` and `disciplined-research`; may also include `concise-writing`; no other skill | A private scratch note that states a factual software claim routes to research exactly like a public artifact | Same |
| `DISC-12` | ``This is a personal visitor-hours conversation unrelated to software, a repository, or project work. Repeat the claim `The North Annex closes at 6:00 p.m.` and rely on it to tell my friend whether arriving at 5:30 p.m. leaves thirty minutes.`` | Must include `disciplined-research`; may also include `concise-writing`; no other skill | A response-only factual interaction outside development still routes to the universal research companion; the user-supplied premise is not verified support | Any final research description, request, or allowed-set change |

## Task 18A reclassification and contract freeze (2026-08-09)

`disciplined-research` is **required** for `DISC-01` through `DISC-12`; none is optional or prohibited.
The reasoning is recorded per row above against the complete requested output, not a sentence-local keyword test.
Except for the final `DISC-02` ambiguity repair recorded below, the
`DISC-01`–`DISC-10` requests and evaluator wrapper remain unchanged;
the target supplied context carries the current complete research and dispatch
descriptions, and the allowed sets are the repaired table above.
The combined exact withheld rubric is
[frozen here](fixtures/skill-discovery/rubrics/task-18a-disc-01-10.md) at SHA-256
`ee576e900573e9e03936dfbd91ef0651fa0a5906e8f7a16ee15a069293d7d964`.
The immutable historical rubric remains unchanged because its own contract was not
defective; Task 18A repairs only the active rubric. Pre-run deterministic rescoring
of historical bytes gave `DISC-02` 0/5 at both efforts, `DISC-04` 5/5 high and
4/5 low, and `DISC-05` 5/5 at both efforts. The required fresh post-freeze arm is
now complete: `DISC-02` is 0/5 high and low, `DISC-04` is 4/5 high and 3/5 low,
and `DISC-05` is 5/5 high and low. High is the preservation gate; low is recorded
robustness only. The shared table-file hash does not invalidate the other eight
accepted row contracts.

The later `DISC-01` behavioral failure made internal logical review explicit in
the shipped research description. Every current target prompt below was therefore
refrozen with that exact clause. Earlier current-target results remain history;
only the final zeroed union accepts these exact target prompt bytes.

All twelve scenarios have separately materialized complete control and target prompts.
Within each scenario, the prompts differ only in the research and dispatch
description lines and have no separate skill-body bundle.

| ID | Control prompt SHA-256 | Target prompt SHA-256 | Withheld rubric SHA-256 | Supplied-file manifest SHA-256 |
|---|---|---|---|---|
| `DISC-01` | `ef0250336996e79b4d0e49eb3fa0a34aacc85d245e78bb97279fa70da6dc5e5a` | `2f175787e2a45f998f44fbe4f13d3801425e82cca26537f504bac820dba60012` | `ee576e900573e9e03936dfbd91ef0651fa0a5906e8f7a16ee15a069293d7d964` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `DISC-02` | `3dcebec6b967ccd13e025673a4ce65f34eedbacc7bc8d74e18d4b32a363731ab` | `16506525e0f9ec43e2d5099aa411564492880a9ed8c5230c1407a20be7bc7682` | `ee576e900573e9e03936dfbd91ef0651fa0a5906e8f7a16ee15a069293d7d964` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `DISC-03` | `d31bd9df45b6751f0bf4c9e6892f79d04a4ff5652e6382418ac5676f62455d46` | `dfa7e97c41e92c4583ae3efe9e79160eef984518f94e7bee09a75d59c786348c` | `ee576e900573e9e03936dfbd91ef0651fa0a5906e8f7a16ee15a069293d7d964` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `DISC-04` | `3dd86c235bf61cd775d87bbb774194f72a2228b41f047966ea348a912e3e1a9a` | `aa9f3db4df0f178be34092c8b9b8d5968f73966f0aba9f0eb9d92c7502e56560` | `ee576e900573e9e03936dfbd91ef0651fa0a5906e8f7a16ee15a069293d7d964` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `DISC-05` | `0aee44238d72bf7eba0187228afc1ed9580b2eadb25a5867c1d82ed65c4f6b43` | `d5c5f4be0b5c646b7a6f93785a013fc0d23b104e296eca6e1edcc4287f8dfdbe` | `ee576e900573e9e03936dfbd91ef0651fa0a5906e8f7a16ee15a069293d7d964` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `DISC-06` | `93586a275c7db13a2d616e426970b3325d15fd1222a233a6e66dca09e817f8e0` | `9b8fcb5893499e0a6de6cba0b39c121195231c5f393f9aba74c9f0c6718047c3` | `ee576e900573e9e03936dfbd91ef0651fa0a5906e8f7a16ee15a069293d7d964` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `DISC-07` | `02c511a46a6da89090079d03fc97f0365f6ab1c02289f405f5ce276e1b3d453a` | `35d770d897461b3a2d5040da74436d8ea3f96465575e17a60c31631b85d9a04e` | `ee576e900573e9e03936dfbd91ef0651fa0a5906e8f7a16ee15a069293d7d964` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `DISC-08` | `c59a4eda7251caf1dd476f529f96963e2688f6359cdcff3d565846273d44321c` | `bcd2cf2514404899f202177273af766271652688b41dcef44db7e7462177aecc` | `ee576e900573e9e03936dfbd91ef0651fa0a5906e8f7a16ee15a069293d7d964` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `DISC-09` | `251ee53d13297d00cc5b4dc9b9fb1e9e55afcfa27ce6dcc00788f0a286d4840a` | `3c31604d3575e4c9310f13c69f32bfadc27d91d1d0ed19995f8d7a17cfb02395` | `ee576e900573e9e03936dfbd91ef0651fa0a5906e8f7a16ee15a069293d7d964` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `DISC-10` | `fc31b37281d557f662d811962bb2757bafb2b20850110668b1deff98ea6bbaed` | `a265e73f8c3043e06c35a6d67eb11cf3d04495f5e7a96826f67e0855caf40ec6` | `ee576e900573e9e03936dfbd91ef0651fa0a5906e8f7a16ee15a069293d7d964` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `DISC-11` | `d81f9df5eb63441ed4fb97a3a53fbd20903345703501020f6fe67bb52b9fa402` | `f91713e4b75334486ceb6b625f6fdb432963659d8d8302042cb71e2c8a6d3f5f` | `200b06fcd313fc0f911a24f11c0a78be7696e8e5ad9c03c7c05070e81001c866` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `DISC-12` | `11e06edee0e08a07bf25e5dd71ae87cdc47f62e70f57d95acf407f1f0d8e4cd5` | `5a3c869dcf3307459fb548effeb4d4d015188fbd3a358a9f2fe312a800484b1c` | `a17e7937d27723947239247831e08f6064cfb4b7cb35159dc38bc3014c18c066` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |

`DISC-02`, `DISC-04`, and `DISC-05` completed five fresh `gpt-5.6-sol` processes
at high effort and five at low effort, maximum concurrency three, under the shared
read-only/no-agents transport (30 slots). The accepted root is
`/private/tmp/dd-task18a-control-postfreeze-f59608a`; freeze SHA-256 is
`0119bdb403fdb89978ed6c2f34bae8de5db13c392071b97b06687d81f9be0210`
and plan SHA-256 is
`4de14a3e7531c8cf0e6258f82c9c8050b849ca9d0f0f8c1c633248dafcd81b4b`.
All selected a1 with zero retries/errors. The other eight accepted controls remain
exact evidence from prior full-matrix root
`/private/tmp/dd-task18a-control-backfill-bd60966-escalated`, surviving freeze
SHA-256 `4671cfef15368088eaa554fdb67e5bea115d7a4a9a9610f7e07d16b160539b2d`,
accepted plan SHA-256
`60b753fe17539876893f367763d59bbd53b7f584a9001217ffe07bbd607c2ce3`.
Target REDs are `DISC-01`, `DISC-02`, `DISC-03`, `DISC-06`, `DISC-07`,
`DISC-04`, `DISC-08`, `DISC-09`, and `DISC-11`; their Sol-high controls are RED
and their later candidates must reach 5/5. `DISC-05` and `DISC-10` are
preservation at 5/5 high. Low scores are robustness evidence, not separate gates.

The final 45-scenario union initially produced one `DISC-02` current response that
also selected `adversarial-review`. That is a routing action, not a rendering
difference, and exposed ambiguity between reviewing and remediating already-reported
findings. The request-only repair above restarted both controls and current at zero:
high control 0/5, low control 0/5, current 5/5, all attempt 1. The earlier current
4/5 row is superseded rather than averaged or discarded. Complete hashes and every
accepted verdict are in [the Task 18A provenance manifest](task-18a-provenance.json).
The accepted final discovery denominator is therefore **60/60**.

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

The Task 17 candidate-description rerun exposed a stale `DISC-01` prohibition. Its
prompt forbids repository and external facts but still asks for load-bearing logical
findings about supplied source text; the unchanged `disciplined-research`
description covers such downstream-quotable review claims. A fresh Sol-high
classification therefore made `disciplined-research` optional rather than
prohibited. The same Task 17 description also makes ordinary response prose a
valid optional `concise-writing` route. The prompt did not change. The first 4/5
arm remains superseded under its old rubric, and only `DISC-01` restarted at zero.

## Historical pre-Task-18A control and target results

Control is full commit `4296647f0dff48a9e77b979ef07e813bf1f66db2` and archive SHA-256 `8f21c8267d005c349702ec94d6aff26c13a09bfbe29f2b43efcfbb37304f16e3`.
Target is the immutable bundle with content-manifest SHA-256 `52fd9eb8c411fcc5d42bfa4590992914c2f7a20a494f6dc7868f82c85691103b`.

| ID | Sol-high control | Exact control misses | Target GREEN | Target route summary | Earlier-arm infrastructure errors | Sol-low control | Cleaned Sol-high | Cleaned Sol-low |
|---|---|---|---|---|---:|---|---|---|
| `DISC-01` | **1/5 watched RED** | Parent omitted 4/5 | **5/5 PASS** | 5 exact | 0 | [Task 11 detail](#task-11-sol-low-control-results-2026-08-07) | **5/5 PASS** (Task 17 repaired arm) | Task 27 |
| `DISC-02` | **5/5 PASS** | None; 5 exact | **5/5 PASS** | 5 exact | 0 | [Task 11 detail](#task-11-sol-low-control-results-2026-08-07) | **5/5 PASS** (Task 17) | Task 27 |
| `DISC-03` | **1/5 watched RED** | Parent omitted 4/5 | **5/5 PASS** | 5 exact | 0 | [Task 11 detail](#task-11-sol-low-control-results-2026-08-07) | **5/5 PASS** (Task 17) | Task 27 |
| `DISC-04` | **5/5 PASS** | None; 5 parent-only | **5/5 PASS** | 2 required-only, 3 with optional research | 0 | [Task 11 detail](#task-11-sol-low-control-results-2026-08-07) | **5/5 PASS** (Task 17) | Task 27 |
| `DISC-05` | **0/5 watched RED** | Parent omitted 5/5 | **5/5 PASS** | 5 exact | 0 | [Task 11 detail](#task-11-sol-low-control-results-2026-08-07) | **5/5 PASS** (Task 17) | Task 27 |
| `DISC-06` | **4/5 watched RED** | Parent omitted 1/5 | **5/5 PASS** | 5 exact | 0 | [Task 11 detail](#task-11-sol-low-control-results-2026-08-07) | **5/5 PASS** (Task 17) | Task 27 |
| `DISC-07` | **5/5 PASS** | None; 1 required-only, 4 with allowed optional variation | **5/5 PASS** | 4 required-only, 1 with optional research | 0 | [Task 11 detail](#task-11-sol-low-control-results-2026-08-07) | **5/5 PASS** (Task 17) | Task 27 |
| `DISC-08` | **5/5 PASS** | None; 3 required-only, 2 with optional research | **5/5 PASS** | 3 required-only, 2 with optional research | 0 | [Task 11 detail](#task-11-sol-low-control-results-2026-08-07) | **5/5 PASS** (Task 17) | Task 27 |
| `DISC-09` | **5/5 PASS** | None; 1 required-only, 4 with allowed optional variation | **5/5 PASS** | 1 required-only, 4 with allowed optional variation | 0 | [Task 11 detail](#task-11-sol-low-control-results-2026-08-07) | **5/5 PASS** (Task 17) | Task 27 |
| `DISC-10` | **5/5 PASS** | None; 1 with optional research, 4 with optional research and sweeping | **5/5 PASS** | 4 with optional research and sweeping, 1 also with optional concise writing | 0 | [Task 11 detail](#task-11-sol-low-control-results-2026-08-07) | **5/5 PASS** (Task 17) | Task 27 |

Run metadata for both completed `DISC-01`–`DISC-09` arms: Codex CLI 0.146.0; `gpt-5.6-sol`; high reasoning effort; Superpowers 6.2.0; five fresh processes per scenario; maximum concurrency three; immutable description context as identified above; no skill bodies or sibling skills available; rubric withheld; every result manually scored, including JSON shape and alphabetical order; zero counted infrastructure errors; run date 2026-08-01 except the repaired `DISC-08` control and parent-target arms, which ran 2026-08-02.
`DISC-10` used the same configuration for all three arms on 2026-08-03 with zero
infrastructure errors.

## Task 11 Sol-low control results (2026-08-07)

**Historical evidence.** These are the frozen low-effort control outcomes. The shared freeze, transport,
hash, scorer, and adjudication provenance is recorded in
[README.md](README.md#task-11-sol-low-control-freeze-and-results).
Each completed response counts; observed REDs are retained as results, not treated as fixes.

| ID | Status | R1 | R2 | R3 | R4 | R5 | Score | Exact missed criteria / adjudication |
|---|---|---|---|---|---|---|---:|---|
| `DISC-01` | target | F | F | F | F | F | **0/5** | All omitted required `disciplined-development`. |
| `DISC-02` | preservation | P | P | P | P | P | **5/5** | Exact allowed set. |
| `DISC-03` | target | F | F | F | F | F | **0/5** | All omitted required `disciplined-development`. |
| `DISC-04` | preservation | P | P | P | P | P | **5/5** | Exact allowed set; optional `research` absent. |
| `DISC-05` | target | F | F | F | F | F | **0/5** | All omitted required `disciplined-development`. |
| `DISC-06` | target | F | F | P | P | P | **3/5** | R1-R2 omitted required `disciplined-development`; R3-R5 exact. |
| `DISC-07` | preservation | P | P | P | P | P | **5/5** | Exact allowed set. |
| `DISC-08` | preservation | P | P | P | P | P | **5/5** | Exact allowed set. |
| `DISC-09` | preservation | P | P | P | P | P | **5/5** | Exact allowed set. |
| `DISC-10` | preservation | P | P | P | P | P | **5/5** | Exact allowed set. |

Owned Task 11 Sol-low aggregate: **33/50**.

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

### Task 17 concise-writing candidate-description rerun (2026-08-08)

The candidate prompts embed all nine current descriptions, including candidate
`concise-writing` skill SHA-256
`f763b43e88c56d6fdc2a96457bc2415cba60b75a1e7cb59cd1b0ebaa3fb199ba`;
no separate skill-body bundle is supplied. The accepted roots are
`/private/tmp/dd-task17-integrated-final` for `DISC-02`–`DISC-10` and the
superseded first `DISC-01` arm, and
`/private/tmp/dd-task17-disc01-repaired-final` for the fresh repaired `DISC-01`
arm. Both froze `gpt-5.6-sol` at high effort, five fresh processes per scenario,
maximum concurrency three, read-only sandboxing, and disabled agents. Every
accepted response completed on attempt 1 with zero infrastructure errors and was
manually scored by the orchestrator.

| ID | Prompt SHA-256 | Active rubric SHA-256 | R1 | R2 | R3 | R4 | R5 | Result |
|---|---|---|---|---|---|---|---|---:|
| `DISC-01` | `ef0250336996e79b4d0e49eb3fa0a34aacc85d245e78bb97279fa70da6dc5e5a` | `1fc2931e121df7e9c8076ef4601b5392b1657e326f4e46e937ab64cab2391e9d` | P | P | P | P | P | **5/5 PASS** |
| `DISC-02` | `1e65dec2c779064162e495d8fc4ff76f1a92bb0bfeff427615a82a5d34aa8b88` | `a19be18831e7e7addf0da89285ec28ffa0b798757da28d892cae574c82ef3837` | P | P | P | P | P | **5/5 PASS** |
| `DISC-03` | `d31bd9df45b6751f0bf4c9e6892f79d04a4ff5652e6382418ac5676f62455d46` | `97094131be395e1d8574408433635604e422770d5fead21844e0217dce15a5bd` | P | P | P | P | P | **5/5 PASS** |
| `DISC-04` | `3dd86c235bf61cd775d87bbb774194f72a2228b41f047966ea348a912e3e1a9a` | `7745e5a0f2a71d25f5cf058419c5de55a422f6e1ba76a107a9617f3513cdced9` | P | P | P | P | P | **5/5 PASS** |
| `DISC-05` | `0aee44238d72bf7eba0187228afc1ed9580b2eadb25a5867c1d82ed65c4f6b43` | `4fa092c91db3bca591c3aae979b463bf59a4e30ca8802df59dfe2a64ab281512` | P | P | P | P | P | **5/5 PASS** |
| `DISC-06` | `93586a275c7db13a2d616e426970b3325d15fd1222a233a6e66dca09e817f8e0` | `4ec85c590c9be45e38dd23eabc592ed4487f970326392fd4910364b79bfeb774` | P | P | P | P | P | **5/5 PASS** |
| `DISC-07` | `02c511a46a6da89090079d03fc97f0365f6ab1c02289f405f5ce276e1b3d453a` | `6ee4d3463d21f7328841bdca93437f6b281346d11f0e569e2998f83ac356d91e` | P | P | P | P | P | **5/5 PASS** |
| `DISC-08` | `c59a4eda7251caf1dd476f529f96963e2688f6359cdcff3d565846273d44321c` | `7751a753e6866a3ba939508738e90609d5d86202cacdf2b245d6a52c409dd8c6` | P | P | P | P | P | **5/5 PASS** |
| `DISC-09` | `251ee53d13297d00cc5b4dc9b9fb1e9e55afcfa27ce6dcc00788f0a286d4840a` | `f9256db717a82a93e0e3ca5342552dd675814351b10a541cbd8fda65882baca4` | P | P | P | P | P | **5/5 PASS** |
| `DISC-10` | `fc31b37281d557f662d811962bb2757bafb2b20850110668b1deff98ea6bbaed` | `879a2099b33246ae8faecdfcfc61544d676f54de07d18fff628a4fed317cf329` | P | P | P | P | P | **5/5 PASS** |

The first `DISC-01` arm used old rubric SHA-256
`3ce6627c5464ff10ccacb846add39ac29930e05af320ae1077ef1b094df1983d`
and scored F/P/P/P/P, **4/5**. R1 selected both allowed Task 17
`concise-writing` and then-prohibited `disciplined-research`; R2–R5 passed. That
arm is superseded, not rescored. The fresh repaired arm kept the prompt unchanged,
allowed both cross-cutting companions optionally, and all five outputs selected
`adversarial-review`, `concise-writing`, and `disciplined-development`; each had
output SHA-256
`82d1b42f5ef72c637e19556395073c16ba6cb49c65e89790f70c95feb960110c`.

#### Task 17 repaired-definition control backfill (2026-08-08)

The active `DISC-01` definition also received the protocol-required fresh control
backfill at `/private/tmp/dd-task17-repaired-definition-controls`. The arm froze
the original control descriptions directly in prompt SHA-256
`803da9b9404330d5f2dd6b35040b8fd7903da025e368015efa290a6004c819be`;
because no separate discovery files were supplied, its discovery manifest is the
empty manifest SHA-256
`e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`.
It used active rubric SHA-256
`1fc2931e121df7e9c8076ef4601b5392b1657e326f4e46e937ab64cab2391e9d`,
five fresh `gpt-5.6-sol` processes at each of high and low effort, read-only
sandboxing, disabled agents, maximum concurrency three, attempt 1, and zero
infrastructure errors.

| Arm | R1 | R2 | R3 | R4 | R5 | Result | Exact output |
|---|---|---|---|---|---|---:|---|
| Original-description control, Sol high | F | F | F | F | F | **0/5 watched RED** | Every repetition selected only `adversarial-review` |
| Original-description control, Sol low | F | F | F | F | F | **0/5 watched RED** | Every repetition selected only `adversarial-review` |
| Current candidate, Sol high | P | P | P | P | P | **5/5 GREEN** | Every repetition included required `adversarial-review` and `disciplined-development`; allowed companions varied only within the rubric |

All ten control outputs were byte-identical
`["adversarial-review"]` at output SHA-256
`56086798eaf0891b5c64c1404e8c705b9c3f9088a26c7f55f4adb9a076edb505`.
They fail the active rubric because they omit required `disciplined-development`.
This repaired-definition 0/5 + 0/5 control is the active Task 17 target RED; the
older control scores above remain historical under their own definitions. Paired
with the fresh candidate 5/5 arm, it closes `DISC-01` without changing the
candidate-description total of 50/50.

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
