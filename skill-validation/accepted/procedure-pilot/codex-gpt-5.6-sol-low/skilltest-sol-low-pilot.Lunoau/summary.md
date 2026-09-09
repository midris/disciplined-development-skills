# Sol-low procedure pilot — owner review

Status: four approved observations completed and scored; STOP for owner review.
No further provider calls, repetitions, candidate edits, evidence promotion or cleanup are authorized by completion.

PILOT_INPUT_REVISION: `e537c03909eb2b4f1986e4170a3f1b662d29a719`.
All four observations executed that clean feature revision on `spike/skilltest-input-isolation`.
Handoff documentation is committed as `d6ba84546e4e5547b457a8ed6f1982af75944c73`; the feature worktree is clean and two commits ahead of origin (not pushed). Main remains clean at ca14bbe24f8aea957dbcfeece3511226e929243d.
DD source main revision: `ca14bbe24f8aea957dbcfeece3511226e929243d`; actual subject inputs/production code remain unchanged from the prepared pilot.
Provider/model/effort: Codex / gpt-5.6-sol / low.
Per-run CLI version: codex-cli 0.153.4; all four captures matched the fixed executable digest `b973d440acac501fd2594a43e7ca9ce41e0a65b9dfb28d0d7a7837c99e1261e3`.
[Exact commands and explicit owner approval](observation-approval-request.md) identify working directory, config, output paths and unchanged host/sandbox requirements.

## Observations

| Attempt | Scenario / condition | Overall verdict | Task fidelity / finding | Seconds | Evidence |
|---|---|---|---|---|---|
| dr-01 | DR-02 / no-DD | PASS | Correct deadline, source and saved note | 38.742 | [Result](attempts/dr-01/result.md), [worksheet](attempts/dr-01/worksheet.md) |
| dr-02 | DR-02 / current-DD | PASS | Extra progress narration: non-blocking fidelity FAIL; final/note correct | 40.013 | [Result](attempts/dr-02/result.md), [worksheet](attempts/dr-02/worksheet.md) |
| lp-01 | LP-01 / no-DD | FAIL | Implementation/test bodies fail LP-I1/LP-I3; explicit PR boundary absent | 69.135 | [Result](attempts/lp-01/result.md), [worksheet](attempts/lp-01/worksheet.md) |
| lp-02 | LP-01 / current-DD | PASS | Prose contract and one-PR boundary; response-only task preserved | 65.489 | [Result](attempts/lp-02/result.md), [worksheet](attempts/lp-02/worksheet.md) |

Each result links the run ID, raw bundle, CLI capture, prelaunch checks, complete trace/hash audit and exact cleanup path.
All four runner/provider exits were 0, infrastructure COMPLETED, with no retries, exclusions, observed contamination or unresolved cleanup.
All declared input bytes and prelaunch hashes matched; all four private runtimes are absent.
DR-02 wrote only the authorized note in each condition; both LP-01 runs made no file changes.
The two separately approved qualifications are not behavioral observations: [q-no-dd](attempts/q-no-dd/result.md), [q-current-dd](attempts/q-current-dd/result.md), each passed once.
Qualification executed earlier revisions retained in those records; do not relabel them as e537c03.

## Procedure findings

The existing config, runner and worksheet commands supported preparation, four one-run invocations, separate scoring, CLI provenance and reviewable handoff.
No new runner capability was needed.
Semantic judgment remained model-led; [scoring-verification.json](scoring-verification.json) checks preserved generated fields, frozen rubric hashes, filled assessment sections and evidence links, not semantic correctness.

Both LP-01 subjects tried to read src/report_cli.py, which is not supplied for this response-only scenario; the lookup failed and each continued.
This is a disclosed subject tool failure, not missing declared inputs or provider infrastructure failure.
The resulting plans remain judgeable for prose/code and composition.
For a later fixture, consider explicitly saying only task facts are supplied; no current prompt, rubric or result was changed.
Both plans also name unverified tooling assumptions; do not mistake those for inspected application facts or claim implementation/tests were executed.

The current-DD research trace contains commentary even though its final answer is exactly two lines.
Record conversational narration separately from final-artifact shape and supported research behavior; do not discard the trace or turn this into a semantic FAIL.
Inline scoring review removed an overextended additional LP-I2 failure from the draft no-DD worksheet: its behavioral contract is concrete; its embedded code bodies independently and decisively fail LP-I1/LP-I3.
The overall verdict was unchanged. All pilot judgments remain advisory pending owner review.

[Recovery/handoff walkthrough](recovery-handoff-walkthrough.md) covers interruption, infrastructure retry, evaluable cleanup failure, version drift and later edit bookkeeping with retained or hypothetical evidence.
It is not a claim of live interruption recovery or candidate testing.
[Preparation checks](preparation-checks.json) retain four explicitly synthetic worksheet commands separately from real observations.

## Validity and limits

[Qualification reconciliation](preflight/reconciliation.md) records common inputs and four contamination controls.
The common native catalog has six entries without DD and fifteen with DD; 60 common bootstrap file hashes match under the documented exact normalization.
Actual source/required skill reads and artifact writes are visible in the retained traces.
No unexpected outside read, permission denial or Git mutation was observed.
Neither traces nor matching CLI versions prove automatic shell-startup reads or hidden provider inputs absent.

These are one observation per condition/scenario, useful for exercising the procedure only.
No effectiveness estimate, repeatability claim, formal candidate GREEN, or official campaign RED acceptance follows.
The no-DD research pass does not establish RED; the no-DD planning failure demonstrates an observable target failure but is not promoted into a later campaign.

## Next action

Owner reviews this report and the four worksheets, then decides whether to accept the minimal procedure and any small runbook/fixture clarification.
[Inline handoff review](pilot-handoff-review.md) has no remaining material findings; verification passed 231 runner tests, 263 hook tests with three skips, and 101 local links/anchors.
Only after that checkpoint should a separately agreed baseline/edit runbook define fresh runs, repetitions and models.
Claude integration, Sol high/medium/low effectiveness runs, possible Terra comparison, hooks work and rewritten-skill comparisons remain deferred.
Retain this entire scratch package through review; the 105 accepted historical observations and unrelated worktree remain untouched.
