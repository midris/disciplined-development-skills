# Skill Test Worksheet

## Run identity

| Field | Value |
|---|---|
| Scenario path | skill-validation/scenarios/concise-writing/cw-19 |
| Scenario ID | cw-19 |
| Scenario purpose | Tighten a coupled cutover runbook without losing actors, exact thresholds and complements, ordering, boundaries, or rationales. |
| Run ID | 20260906T073902636Z-cw-19-39caf899-4c6d-4a53-8221-bedd27e1e72e-45hnb_z3 |
| Provider | codex |
| Provider CLI version | Unknown — no contemporaneous CLI-version evidence found in the accepted record or matching retained scratch logs. |
| Model | gpt-5.6-sol |
| Effort | high |
| Started | 2026-09-06T07:39:02.636Z |
| Finished | 2026-09-06T07:39:22.358Z |
| Duration seconds | 19.722 |

## Infrastructure

| Field | Value |
|---|---|
| Status | COMPLETED |
| Error code |  |
| Error message |  |

## Executed inputs

| Kind | Path | SHA-256 |
|---|---|---|
| Configuration | config.json | e74ddd95b9b27d869cb6484b2aafe4d0f3a555631d3f48354892391b6a56deaf |
| Prompt template | prompt-template.txt | df33a3add2dc4ad6445076a381e35be307c35fdfbc50426fd0db4072a10b26b3 |
| Rendered prompt | prompt.txt | 9970058127b94579eac89d423f2ccdd57864af4f20bcee346112b16c5c9948c2 |
| Fixture | skills/concise-writing/SKILL.md | 4d12a2eb475c6b2ef57e2300c8c07af3f59c1e07b2b82695a3b7669eee1d6d72 |

## Withheld evaluation input

| Kind | Path | SHA-256 |
|---|---|---|
| Rubric | skill-validation/scenarios/concise-writing/cw-19/rubric.md | 8c7ae23faa8adaa35090b9f78e8b40eaf245687982378b19fd8873b2aa646c07 |

## Semantic behavior

| Invariant | Criterion | Score | Evidence | Notes |
|---|---|---|---|---|
| Padding removal | Remove the meta-framing opener and state the readiness and `GO`-before-promotion rules once without cutting protected information. | PASS | final.txt:1-27 | The opener and explanatory restatements are gone. The readiness rule and authorization sequence each have one operational home; the required `GO` mention in the `--force` rationale is protected information rather than redundant instruction. |
| Preflight dependency | Preserve the release engineer's first exact preflight command, attachment of its JSON output to `CHG-4821`, and recording of the pre-cutover snapshot ID before promotion. | PASS | final.txt:3-9 | Standard operator imperatives preserve the release-engineer actor; the exact command, JSON artifact, ticket, snapshot content, and pre-promotion position all remain. |
| Combined readiness | Require replica lag at most 2 seconds and mismatch strictly below 0.1% together throughout the same uninterrupted 15-minute window before promotion. | PASS | final.txt:7-9,15-19 | Both inclusive/strict readiness thresholds, their conjunction, continuity, shared window, duration, and promotion dependency are explicit. |
| Failure escalation complements | On preflight failure, lag above 2 seconds, or mismatch at or above 0.1% before promotion, stop and post the exact blocked notice, ticket link, channel, and tagged recipient. | FAIL | final.txt:11 | The actions and recipients are preserved, but “either threshold is breached” leaves mismatch equality implicit. The rubric expressly rejects generic breach wording when `0.1%` equality is not explicit. |
| Promotion authorization | After readiness, post the ticket link, wait for the database incident commander to reply `GO`, and only then run the exact promotion command. | PASS | final.txt:15-19 | The actor-preserving imperatives retain the exact order, commander, reply literal, channel, ticket, and command. |
| Prohibited shortcut | Prohibit `--force` and preserve that it skips readiness and `GO` checks and can expose partially backfilled rows. | PASS | final.txt:21 | The prohibition and both reasons remain explicit; “bypasses” is semantically equivalent to “skips.” |
| Irreversible boundary | Identify the first accepted `orders-v3`-only application write as the in-place rollback boundary and prohibit the exact rollback command afterward because the old schema cannot represent the write. | PASS | final.txt:23-27 | The boundary, prohibition, exact command, and data-representation rationale are preserved. |
| Recovery ownership | After the boundary, reserve the continue-forward versus recorded-snapshot-restore decision exclusively for the database incident commander, not the release engineer. | PASS | final.txt:27 | The exclusive owner, excluded actor, both options, and `CHG-4821` snapshot are explicit. |

## Deterministic protocol

| Requirement | Score | Evidence | Notes |
|---|---|---|---|
| No authenticated deterministic consumer | N/A | rubric.md; final.txt:1-27 | The runbook's exact command literals are semantic requirements, but no authenticated renderer, validator, parser, or production consumer processes this response. |

## Task fidelity

| Requirement | Score | Evidence | Notes |
|---|---|---|---|
| Revised runbook only | PASS | final.txt:1-27 | The response contains only the tightened runbook, with no preface, postscript, procedural narration, unsupported fact, advice, or assumption. |
| Read the directly invoked skill completely | PASS | stdout.txt | The provider reads lines 1-240 of the 91-line supplied concise-writing skill before answering. |
| Preserve evaluator scope | PASS | stdout.txt; final.txt:1-27 | The provider revises only the supplied prose and performs no real cutover action. |
| Read-only evaluator boundary | PASS | stdout.txt; result.json | The provider performs one `sed` read and no edits, Git mutations, network calls, or agent dispatches; retained evidence is empty. |
| Fixture-only execution inputs | PASS | stdout.txt; result.json | The sole provider read targets the declared run-workspace fixture; no ambient skill or repository file is accessed. |

## Readability

| Observation | Evidence |
|---|---|
| Phase headings, numbered operator steps, and compact boundary prose make the runbook easy to execute; only the compressed failure predicate requires interpretation. | final.txt:1-27 |

## Verdict

| Field | Value |
|---|---|
| Overall verdict | FAIL |
| Rationale | Seven of eight semantic criteria pass, along with all task-fidelity checks. The result loses one safety-critical edge: the generic “either threshold is breached” escalation condition does not explicitly preserve that mismatch equality at `0.1%` triggers `BLOCKED`, which the rubric identifies as a required exact complement. |
| Disposition | Accepted by owner on 2026-09-06. |

## Methodology notes

| Field | Value |
|---|---|
| Ambiguities | None material. The rubric explicitly says generic threshold-breach wording fails when mismatch equality is ambiguous, so the otherwise plausible compression has a determinate score. |
| Scenario defects | None observed. The scenario supplies one complete skill, a self-contained runbook, explicit actor rules, and clause-level criteria for every protected relationship. The transcript remains fixture-only. |
| Proposed methodology changes | None. |
