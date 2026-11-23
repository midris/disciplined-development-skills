# Writing explicit rationale — study protocol

Format version: `1`
Study ID: `writing-explicit-rationale`
Status: fresh shipped application benchmark prepared; dispatch awaits owner allocation. [Benchmark freeze](#shipped-application-benchmark-freeze)
Plan: [current milestone](../../plans/2026-09-11-model-driven-skill-testing.md#wer-milestones)
General spec: [testing framework](../../plans/specs/2026-09-11-model-driven-skill-testing-framework.md)

## Sources and intended use

A future maintainer encounters a choice in a plan or in code without the original conversation. The study asks whether that person can recover the reason and accepted consequence from the edited tree. The [shipped WER skill](../../skills/writing-explicit-rationale/SKILL.md) was inspected at main revision `2a0e2499a39c2000fa2bab3152e12f41f26f038a`, SHA-256 `97eb06c649c194e8819b4dff68b808eda4ec7c948a6ead518da247daf31d6cfe`. Earlier scenarios supply fixture facts. All baseline results will come from fresh runs.

## Behavioral contract and consumers

WER should make consequential choices understandable at the decision site, preserve the supplied facts, and leave self-evident edits concise. Repeated review of the same decision should prompt an audit of related choices in the change. The subjects edit project artifacts. A fresh reader sees a single final project as a maintainer would.

The owner wants the artifact to carry all the context and reasoning a reader needs to understand a decision and act on it without asking the author or guessing their intent.
Relevant details can include the constraint that drove the choice, who bears its cost, or what would justify revisiting it.
When the original inputs leave a consequential question open, the artifact should preserve that uncertainty.

## Assessment policy

Separate task correctness, rationale placement, factual accuracy and timely native loading. Record what the reviewer could recover from the final tree before releasing the source facts, conversation, diff and final response. Use code replays to check behavior and human or agent judgment to evaluate meaning. Freeze criterion-level evidence rules and ambiguous examples before collection. [Reader-first procedure](../../plans/specs/2026-11-08-wer-focused-baseline.md#reader-first-output-check)

Judge the complete artifact against each applicable criterion on the case card.
Record met, not met or insufficient evidence with a specific artifact, replay or trace reference.
A valid execution succeeds functionally when all functional criteria are met, fails if any is not met, and otherwise has an unknown outcome.
Record native selection separately and explain shared causes once.
Record each positive output’s eligibility before reader scores are available.
Follow the reader-first procedure in the focused design and case package guide, seal first readings before full-evidence reconciliation, and report skips, gaps and invalid attempts separately.
Include every valid-setup execution, including control failures, with one descriptive observation per cell.

Policy snapshot: [WER assessment policy v1](runs/baseline-01/assessment-policy.txt).

### Whole-output interpretation

Apply the [whole-output assessment guidance](../../plans/specs/2026-09-11-model-driven-skill-testing-framework.md#6-assess-observations-and-establish-the-baseline) to the criterion evidence above.
In the isolated reading, ask what the complete final project tells a maintainer and seal the answer before showing the original inputs.
For the subsequent full-evidence review, append the [neutral context instructions](runs/baseline-01/reconciliation-context.txt) to the frozen reconciliation question and pin the composed reviewer prompt before dispatch.
Compare the source message, original project, complete final project and full response. Check where the rationale survives and whether a disputed phrase materially changes the reader’s decision, reason, accepted consequence or next action.
Use the same materiality test across all guided and control cases during reconciliation, including plausible explanations added beyond the supplied facts.
Record a shared precision concern once even when the plan and handoff repeat it.
Keep case-specific examples, this checkpoint discussion and prior scores outside the independent judgment packet.
The frozen criteria, evidence boundaries and per-run aggregation rule continue to apply.

## Suite and evidence

| Proposed case | Behavior under test | Distinguishing evidence |
| --- | --- | --- |
| Defer XML export | A deliberate omission remains intelligible in the plan. | A reader recovers the retained scope, deferral reason and customer impact from the affected item. |
| Preserve prior quota | A surprising code choice carries the reason and trade-off. | Timing tests verify the policy. The code explains what immediate reset would break and the bounded exposure it accepts. |
| Rename a private helper | Routine work preserves existing rationale and avoids invented justification. | The rename works, the nearby quota explanation survives, and the diff adds no misleading rationale. |
| Address repeated review | The editor examines the change for other unexplained decisions. | The tree explains both the flagged guard and a second consequential choice. The routine edit stays concise. |

The [four case cards and runnable fixtures](cases/README.md) have been exercised against [20 constructed outputs](cases/qualification.md). The application checkpoint below covers 16 subject observations. They cover plans and code, explicit application, native selection and an explicitly conventional rename. The export and standalone quota requests explicitly supply the reason, so success can reflect good placement of supplied facts. A tie indicates no observed incremental benefit on these prompts. The rename is an easy negative. Repeated-review R2 measures recovery of a second decision; inspect the trace separately before attributing that recovery to a broader audit. Standalone spec writing and transfer to unfamiliar tasks remain outside this focused screen. The [case design](../../plans/specs/2026-11-08-wer-focused-baseline.md#cases-and-acceptance) supplies the task details for packaging.

## Execution scope and authorization

The two provider batches share a stage gate. Complete local orders 1–8 for Codex, then 1–8 for Claude. Inspect all 16 application outputs before releasing orders 9–12 for Codex and then Claude.
Run one slot at a time in a fresh session. Pause for an invalid setup, missing preservation or unresolved charge, a policy change, an incomplete guided task or a material invented rationale.
For the material-invention stop, identify the added claim in the complete deliverable and state how relying on it would materially change the intended reader’s understanding or action under the whole-output rule above.
Record a nonmaterial overstatement once as a fidelity observation and continue under the remaining stop rules.
Use the [focused design](../../plans/specs/2026-11-08-wer-focused-baseline.md#reader-first-output-check) for the checkpoint and reading rules. Record approval in this protocol at a new revision before using any command below.

From the canonical checkout, each proposed subject or evaluator command is `TMPDIR=/private/var/folders/55/6jqr25v5211fn00wych8b1jm0000gn/T/wer-baseline-01 skill-validation/runner/.venv/bin/skilltest run CONFIG` with the exact scheduled config. Host permission enables provider initialization under the runner’s permission policy. Recheck binaries and input identities before dispatch. The runner timeout is 900 seconds.
Original mounts the shipped bytes at GUIDANCE.md and requests a complete read before the task. Control and native share the ordinary prompt. Only native mounts the shipped skill in the provider catalog. Verify actual init, catalog and ordered full delivery from retained evidence.
On 2026-11-09 the owner answered “approved” to one Claude reader smoke using the constructed project. This grants one evaluator invocation, with zero retries. Subject runs and further readings await separate approval.
The approved call uses the [constructed smoke config](runs/baseline-01/reader-smoke/config.json) with Claude Opus 5.5 medium, read-only and zero fixtures. Verify exact prompt, fresh init, workspace, catalog, persistence and zero tool calls before releasing any positive-case readings. Subjects use low effort and workspace-write. The two reconciliations also use fresh read-only Opus medium sessions.

#### Qualification on 2026-11-09

Materialized all 24 configs with the existing runner and compared the full fixture file sets, bytes and rendered prompts against the task, starting project, assigned skill exposure and review attachment.
The packet builder recovered the original project files from every starting workspace. Sixteen paired comparisons allowed only the explicit instruction and GUIDANCE.md for original/control, and only the provider-specific SKILL.md for native/control.
All subject configs use the same neutral run ID prefix because the provider sees its workspace path.
The zero-fixture smoke prompt uses the complete constructed export repair. Its serialized payload SHA-256 is `dac3c74ef3c81477019d75156369a0385d6f43773f5b9582b6d6737bb3d711ab` and its composed prompt SHA-256 is `1f727ee00b085ac2b0c1724112f8c1f9c2a5aed771406e1d9b8fca8383bb83f4`.

The runner at `a67b262acb71aface2fa18f02a03b91a987fe624` supplied the preparation and installed-policy checks.
Codex CLI 0.167.0 at `/opt/homebrew/bin/codex` hashed to `030316ecfbb41f4e7946e584b0063ef333b7a36cd312ba349f2f6869e39b62cc`.
Claude Code 2.1.319 at `/opt/homebrew/bin/claude` hashed to `1f53587e92dee8e089fa349188a4cda64fa34ace6e7b0ca2ee278ddaa3cc2ebd`.
Seven installed-policy probes passed: both providers in both modes denied undeclared inputs, both read-only policies denied mutations and the writable Codex Git/network probe passed.
Both Codex login-shell probes and both local scripted Claude CLI probes failed the shell-runtime checks. Both providers initially selected Apple Python 3.9.6, below the required 3.11 minimum. Apple’s launcher also emits cache-write errors under the sandbox.
Runner revision `2637312fd6877e821c70625a75204e043998a82f` adds Homebrew’s Python directory to the prepared PATH for both adapters.
All 11 installed probes passed at these CLI identities, including the four shell probes and seven isolation, read-only and Git/network checks.
In both modes both providers selected Python 3.14.10 and Git 2.56.0.
Use this runner revision for the proposed smoke and subjects, with the existing frozen task inputs.
The verified external inventory `python-requalification.inventory.json` beside the original inventory records 582 entries and hashes to `c0c11fcc011eb555b8ae5de459ef0736272ac0642bcc5b94b1a8728fcde35bc3`.
The scripted Claude traces show the declared probe skill, 16 bundled skills, three built-in plugins and zero MCP servers in both modes.
The initial smoke used that catalog with the probe removed. The subscription amendment below governs subsequent live launches. Compare actual names and provenance to the retained init records. Check actual Codex catalog and ordered loads on the first approved traces.
The single approved live reader smoke completed in 14.2 seconds. Its fresh read-only launch disabled persistence, the fixture contained only the Git boundary, the captured prompt matched the frozen bytes, and the full trace contained one turn and zero tool calls.
The init listed 17 skills. Compared with the 16 expected built-ins, it added `schedule` and removed none. The tools, three plugins and empty MCP list matched. WER was absent.
The frozen rule requires catalog agreement. The reading is unusable for qualification. The [evaluator ledger](runs/baseline-01/evaluator-run-index.json) pins the complete retained bundle inventory, private audit and authority.
#### Offline catalog diagnosis

The installed Claude Code 2.1.319 binary matches the qualified SHA-256. Its bundled `registerScheduleRemoteAgentsSkill` registers `schedule` (alias `routines`) and checks the first-party provider, Claude.ai OAuth scope, local session and effective `allow_routines` policy before exposing it.
The [scripted qualification](../../skill-validation/runner/acceptance/test_claude_cli.py) uses a surrogate home, API key and localhost service. The [production adapter](../../skill-validation/runner/src/skilltest/claude_runtime.py) requires a Claude.ai login. Both inventoried scripted init records identify API-key authentication. The inventoried live init has the same CLI version and three built-in plugins, with no API key, project skills or MCP servers.
A separate offline startup check used the installed CLI with Opus 5.5 medium, read-only permissions, an empty fixture, persistence disabled and an added sandbox network denial. Only a stream-JSON SDK `initialize` control request was supplied, with no user message. The returned command catalog included `schedule` under the existing subscription profile. A surrogate home with a synthetic API key omitted it, as did a synthetic OAuth token alone. This command listing corroborates the live skill init. It does not identify the individual account-policy value responsible for each synthetic result.
The original 16-skill expectation came from a different authentication and policy context. The observed extra entry has built-in provenance; the smoke trace records zero invocations.

**Subscription amendment effective before the replacement.** The [frozen subscription catalog](runs/baseline-01/reader-smoke/subscription-catalog.json) lists the exact 17 expected built-ins, read-only tools, plugin provenance, MCP list and empty-project startup command names. Retain the scripted API-key expectation separately. Apply the subscription expectation to the reader and relevant subject arms, adding WER only for native. Keep exact tool, plugin and MCP checks, fresh read-only session, prompt identity, zero tool calls and the stop on any other catalog difference. Keep the first smoke unusable under its original rule.
On 2026-11-09 the owner approved any further allocations needed to fix this issue. Allocate one retry invocation for the replacement reader smoke with the identical config and prompt, after verifying the CLI and startup catalog. Record its parent in the evaluator ledger. Subject collection requires separate approval.

### Proposed batch: codex-baseline-01

Authority on 2026-11-09: the owner approved the 16 application runs and requested checkpoint results before native discovery. Orders 1–8 of this batch are authorized once each under the stated stop rules.
Native authority on 2026-11-10: the owner approved orders 9–12 once per provider, with all results including behavioral failures retained for joint review. Run Codex then Claude, with the frozen inputs and no automatic replacement.
Scope: Four cases, three conditions, one repetition each on `gpt-5.6-sol`. Include every valid-setup execution. No automatic retry.
Actual attempts: [subject index](runs/baseline-01/codex/run-index.json).

[export-deferral](runs/baseline-01/codex/export-deferral-manifest.json) [quota-grace](runs/baseline-01/codex/quota-grace-manifest.json) [helper-rename](runs/baseline-01/codex/helper-rename-manifest.json) [repeated-review](runs/baseline-01/codex/repeated-review-manifest.json)

| Order | Case | Condition | Repetition | CONFIG |
| --- | --- | --- | --- | --- |
| 1 | export-deferral | original | 1 | `skill-studies/writing-explicit-rationale/runs/baseline-01/codex/export-deferral-original.json` |
| 2 | export-deferral | control | 1 | `skill-studies/writing-explicit-rationale/runs/baseline-01/codex/export-deferral-control.json` |
| 3 | quota-grace | control | 1 | `skill-studies/writing-explicit-rationale/runs/baseline-01/codex/quota-grace-control.json` |
| 4 | quota-grace | original | 1 | `skill-studies/writing-explicit-rationale/runs/baseline-01/codex/quota-grace-original.json` |
| 5 | helper-rename | original | 1 | `skill-studies/writing-explicit-rationale/runs/baseline-01/codex/helper-rename-original.json` |
| 6 | helper-rename | control | 1 | `skill-studies/writing-explicit-rationale/runs/baseline-01/codex/helper-rename-control.json` |
| 7 | repeated-review | control | 1 | `skill-studies/writing-explicit-rationale/runs/baseline-01/codex/repeated-review-control.json` |
| 8 | repeated-review | original | 1 | `skill-studies/writing-explicit-rationale/runs/baseline-01/codex/repeated-review-original.json` |
| 9 | export-deferral | native | 1 | `skill-studies/writing-explicit-rationale/runs/baseline-01/codex/export-deferral-native.json` |
| 10 | quota-grace | native | 1 | `skill-studies/writing-explicit-rationale/runs/baseline-01/codex/quota-grace-native.json` |
| 11 | helper-rename | native | 1 | `skill-studies/writing-explicit-rationale/runs/baseline-01/codex/helper-rename-native.json` |
| 12 | repeated-review | native | 1 | `skill-studies/writing-explicit-rationale/runs/baseline-01/codex/repeated-review-native.json` |

### Proposed batch: claude-baseline-01

Resumption on 2026-11-09: the owner requested completion of orders 3–8 with all outcomes, including failures, retained for joint review after collection. Record behavioral misses and continue through order 8. Setup, preservation and charge checks still apply. No additional calls or retries are allocated.

Authority on 2026-11-09: the owner approved the 16 application runs and requested checkpoint results before native discovery. Orders 1–8 of this batch are authorized once each under the stated stop rules.
Native authority on 2026-11-10: the owner approved orders 9–12 once per provider, with all results including behavioral failures retained for joint review. Run Codex then Claude, with the frozen inputs and no automatic replacement.
Scope: Four cases, three conditions, one repetition each on `claude-opus-5-5`. Include every valid-setup execution. No automatic retry.
Actual attempts: [subject index](runs/baseline-01/claude/run-index.json).

[export-deferral](runs/baseline-01/claude/export-deferral-manifest.json) [quota-grace](runs/baseline-01/claude/quota-grace-manifest.json) [helper-rename](runs/baseline-01/claude/helper-rename-manifest.json) [repeated-review](runs/baseline-01/claude/repeated-review-manifest.json)

| Order | Case | Condition | Repetition | CONFIG |
| --- | --- | --- | --- | --- |
| 1 | export-deferral | control | 1 | `skill-studies/writing-explicit-rationale/runs/baseline-01/claude/export-deferral-control.json` |
| 2 | export-deferral | original | 1 | `skill-studies/writing-explicit-rationale/runs/baseline-01/claude/export-deferral-original.json` |
| 3 | quota-grace | original | 1 | `skill-studies/writing-explicit-rationale/runs/baseline-01/claude/quota-grace-original.json` |
| 4 | quota-grace | control | 1 | `skill-studies/writing-explicit-rationale/runs/baseline-01/claude/quota-grace-control.json` |
| 5 | helper-rename | control | 1 | `skill-studies/writing-explicit-rationale/runs/baseline-01/claude/helper-rename-control.json` |
| 6 | helper-rename | original | 1 | `skill-studies/writing-explicit-rationale/runs/baseline-01/claude/helper-rename-original.json` |
| 7 | repeated-review | original | 1 | `skill-studies/writing-explicit-rationale/runs/baseline-01/claude/repeated-review-original.json` |
| 8 | repeated-review | control | 1 | `skill-studies/writing-explicit-rationale/runs/baseline-01/claude/repeated-review-control.json` |
| 9 | export-deferral | native | 1 | `skill-studies/writing-explicit-rationale/runs/baseline-01/claude/export-deferral-native.json` |
| 10 | quota-grace | native | 1 | `skill-studies/writing-explicit-rationale/runs/baseline-01/claude/quota-grace-native.json` |
| 11 | helper-rename | native | 1 | `skill-studies/writing-explicit-rationale/runs/baseline-01/claude/helper-rename-native.json` |
| 12 | repeated-review | native | 1 | `skill-studies/writing-explicit-rationale/runs/baseline-01/claude/repeated-review-native.json` |

### Proposed batch: codex-functional-pilot-01

Scope: Two pilot cases, shipped and control, one repetition per cell. Include every valid-setup execution. No automatic retry. Owner approval on 2026-11-23 covers orders 1–4 once each in this batch.
Actual attempts: [subject index](runs/functional-pilot-01/codex/run-index.json).

[catalog-review](runs/functional-pilot-01/codex/catalog-review-manifest.json)
[dispatch-hold](runs/functional-pilot-01/codex/dispatch-hold-manifest.json)

| Order | Case | Condition | Repetition | CONFIG |
| --- | --- | --- | --- | --- |
| 1 | catalog-review | original | 1 | `skill-studies/writing-explicit-rationale/runs/functional-pilot-01/codex/catalog-review-original.json` |
| 2 | catalog-review | control | 1 | `skill-studies/writing-explicit-rationale/runs/functional-pilot-01/codex/catalog-review-control.json` |
| 3 | dispatch-hold | control | 1 | `skill-studies/writing-explicit-rationale/runs/functional-pilot-01/codex/dispatch-hold-control.json` |
| 4 | dispatch-hold | original | 1 | `skill-studies/writing-explicit-rationale/runs/functional-pilot-01/codex/dispatch-hold-original.json` |

### Proposed batch: claude-functional-pilot-01

Scope: Two pilot cases, shipped and control, one repetition per cell. Include every valid-setup execution. No automatic retry. Owner approval on 2026-11-23 covers orders 1–4 once each in this batch.
Actual attempts: [subject index](runs/functional-pilot-01/claude/run-index.json).

[catalog-review](runs/functional-pilot-01/claude/catalog-review-manifest.json)
[dispatch-hold](runs/functional-pilot-01/claude/dispatch-hold-manifest.json)

| Order | Case | Condition | Repetition | CONFIG |
| --- | --- | --- | --- | --- |
| 1 | catalog-review | control | 1 | `skill-studies/writing-explicit-rationale/runs/functional-pilot-01/claude/catalog-review-control.json` |
| 2 | catalog-review | original | 1 | `skill-studies/writing-explicit-rationale/runs/functional-pilot-01/claude/catalog-review-original.json` |
| 3 | dispatch-hold | original | 1 | `skill-studies/writing-explicit-rationale/runs/functional-pilot-01/claude/dispatch-hold-original.json` |
| 4 | dispatch-hold | control | 1 | `skill-studies/writing-explicit-rationale/runs/functional-pilot-01/claude/dispatch-hold-control.json` |

### Proposed batch: codex-application-benchmark-01

Scope: 52 fresh subjects, explicitly shipped and control. Include every valid-setup execution. No automatic retry. Pending owner allocation.
Actual attempts: [subject index](runs/application-benchmark-01/codex/run-index.json).

[export-deferral](runs/application-benchmark-01/codex/export-deferral-manifest.json) [quota-grace](runs/application-benchmark-01/codex/quota-grace-manifest.json) [repeated-review](runs/application-benchmark-01/codex/repeated-review-manifest.json) [catalog-review](runs/application-benchmark-01/codex/catalog-review-manifest.json) [helper-rename](runs/application-benchmark-01/codex/helper-rename-manifest.json) [scope-trim](runs/application-benchmark-01/codex/scope-trim-manifest.json) [dispatch-hold](runs/application-benchmark-01/codex/dispatch-hold-manifest.json)

| Order | Case | Condition | Repetition | CONFIG |
| --- | --- | --- | --- | --- |
| 1 | export-deferral | original | 1 | `skill-studies/writing-explicit-rationale/runs/application-benchmark-01/codex/export-deferral-original.json` |
| 2 | export-deferral | control | 1 | `skill-studies/writing-explicit-rationale/runs/application-benchmark-01/codex/export-deferral-control.json` |
| 3 | quota-grace | control | 1 | `skill-studies/writing-explicit-rationale/runs/application-benchmark-01/codex/quota-grace-control.json` |
| 4 | quota-grace | original | 1 | `skill-studies/writing-explicit-rationale/runs/application-benchmark-01/codex/quota-grace-original.json` |
| 5 | repeated-review | original | 1 | `skill-studies/writing-explicit-rationale/runs/application-benchmark-01/codex/repeated-review-original.json` |
| 6 | repeated-review | control | 1 | `skill-studies/writing-explicit-rationale/runs/application-benchmark-01/codex/repeated-review-control.json` |
| 7 | catalog-review | control | 1 | `skill-studies/writing-explicit-rationale/runs/application-benchmark-01/codex/catalog-review-control.json` |
| 8 | catalog-review | original | 1 | `skill-studies/writing-explicit-rationale/runs/application-benchmark-01/codex/catalog-review-original.json` |
| 9 | helper-rename | original | 1 | `skill-studies/writing-explicit-rationale/runs/application-benchmark-01/codex/helper-rename-original.json` |
| 10 | helper-rename | control | 1 | `skill-studies/writing-explicit-rationale/runs/application-benchmark-01/codex/helper-rename-control.json` |
| 11 | scope-trim | control | 1 | `skill-studies/writing-explicit-rationale/runs/application-benchmark-01/codex/scope-trim-control.json` |
| 12 | scope-trim | original | 1 | `skill-studies/writing-explicit-rationale/runs/application-benchmark-01/codex/scope-trim-original.json` |
| 13 | dispatch-hold | original | 1 | `skill-studies/writing-explicit-rationale/runs/application-benchmark-01/codex/dispatch-hold-original.json` |
| 14 | dispatch-hold | control | 1 | `skill-studies/writing-explicit-rationale/runs/application-benchmark-01/codex/dispatch-hold-control.json` |
| 15 | export-deferral | control | 2 | `skill-studies/writing-explicit-rationale/runs/application-benchmark-01/codex/export-deferral-control.json` |
| 16 | export-deferral | original | 2 | `skill-studies/writing-explicit-rationale/runs/application-benchmark-01/codex/export-deferral-original.json` |
| 17 | quota-grace | original | 2 | `skill-studies/writing-explicit-rationale/runs/application-benchmark-01/codex/quota-grace-original.json` |
| 18 | quota-grace | control | 2 | `skill-studies/writing-explicit-rationale/runs/application-benchmark-01/codex/quota-grace-control.json` |
| 19 | repeated-review | control | 2 | `skill-studies/writing-explicit-rationale/runs/application-benchmark-01/codex/repeated-review-control.json` |
| 20 | repeated-review | original | 2 | `skill-studies/writing-explicit-rationale/runs/application-benchmark-01/codex/repeated-review-original.json` |
| 21 | catalog-review | original | 2 | `skill-studies/writing-explicit-rationale/runs/application-benchmark-01/codex/catalog-review-original.json` |
| 22 | catalog-review | control | 2 | `skill-studies/writing-explicit-rationale/runs/application-benchmark-01/codex/catalog-review-control.json` |
| 23 | helper-rename | control | 2 | `skill-studies/writing-explicit-rationale/runs/application-benchmark-01/codex/helper-rename-control.json` |
| 24 | helper-rename | original | 2 | `skill-studies/writing-explicit-rationale/runs/application-benchmark-01/codex/helper-rename-original.json` |
| 25 | scope-trim | original | 2 | `skill-studies/writing-explicit-rationale/runs/application-benchmark-01/codex/scope-trim-original.json` |
| 26 | scope-trim | control | 2 | `skill-studies/writing-explicit-rationale/runs/application-benchmark-01/codex/scope-trim-control.json` |
| 27 | dispatch-hold | control | 2 | `skill-studies/writing-explicit-rationale/runs/application-benchmark-01/codex/dispatch-hold-control.json` |
| 28 | dispatch-hold | original | 2 | `skill-studies/writing-explicit-rationale/runs/application-benchmark-01/codex/dispatch-hold-original.json` |
| 29 | export-deferral | original | 3 | `skill-studies/writing-explicit-rationale/runs/application-benchmark-01/codex/export-deferral-original.json` |
| 30 | export-deferral | control | 3 | `skill-studies/writing-explicit-rationale/runs/application-benchmark-01/codex/export-deferral-control.json` |
| 31 | quota-grace | control | 3 | `skill-studies/writing-explicit-rationale/runs/application-benchmark-01/codex/quota-grace-control.json` |
| 32 | quota-grace | original | 3 | `skill-studies/writing-explicit-rationale/runs/application-benchmark-01/codex/quota-grace-original.json` |
| 33 | repeated-review | original | 3 | `skill-studies/writing-explicit-rationale/runs/application-benchmark-01/codex/repeated-review-original.json` |
| 34 | repeated-review | control | 3 | `skill-studies/writing-explicit-rationale/runs/application-benchmark-01/codex/repeated-review-control.json` |
| 35 | catalog-review | control | 3 | `skill-studies/writing-explicit-rationale/runs/application-benchmark-01/codex/catalog-review-control.json` |
| 36 | catalog-review | original | 3 | `skill-studies/writing-explicit-rationale/runs/application-benchmark-01/codex/catalog-review-original.json` |
| 37 | export-deferral | control | 4 | `skill-studies/writing-explicit-rationale/runs/application-benchmark-01/codex/export-deferral-control.json` |
| 38 | export-deferral | original | 4 | `skill-studies/writing-explicit-rationale/runs/application-benchmark-01/codex/export-deferral-original.json` |
| 39 | quota-grace | original | 4 | `skill-studies/writing-explicit-rationale/runs/application-benchmark-01/codex/quota-grace-original.json` |
| 40 | quota-grace | control | 4 | `skill-studies/writing-explicit-rationale/runs/application-benchmark-01/codex/quota-grace-control.json` |
| 41 | repeated-review | control | 4 | `skill-studies/writing-explicit-rationale/runs/application-benchmark-01/codex/repeated-review-control.json` |
| 42 | repeated-review | original | 4 | `skill-studies/writing-explicit-rationale/runs/application-benchmark-01/codex/repeated-review-original.json` |
| 43 | catalog-review | original | 4 | `skill-studies/writing-explicit-rationale/runs/application-benchmark-01/codex/catalog-review-original.json` |
| 44 | catalog-review | control | 4 | `skill-studies/writing-explicit-rationale/runs/application-benchmark-01/codex/catalog-review-control.json` |
| 45 | export-deferral | original | 5 | `skill-studies/writing-explicit-rationale/runs/application-benchmark-01/codex/export-deferral-original.json` |
| 46 | export-deferral | control | 5 | `skill-studies/writing-explicit-rationale/runs/application-benchmark-01/codex/export-deferral-control.json` |
| 47 | quota-grace | control | 5 | `skill-studies/writing-explicit-rationale/runs/application-benchmark-01/codex/quota-grace-control.json` |
| 48 | quota-grace | original | 5 | `skill-studies/writing-explicit-rationale/runs/application-benchmark-01/codex/quota-grace-original.json` |
| 49 | repeated-review | original | 5 | `skill-studies/writing-explicit-rationale/runs/application-benchmark-01/codex/repeated-review-original.json` |
| 50 | repeated-review | control | 5 | `skill-studies/writing-explicit-rationale/runs/application-benchmark-01/codex/repeated-review-control.json` |
| 51 | catalog-review | control | 5 | `skill-studies/writing-explicit-rationale/runs/application-benchmark-01/codex/catalog-review-control.json` |
| 52 | catalog-review | original | 5 | `skill-studies/writing-explicit-rationale/runs/application-benchmark-01/codex/catalog-review-original.json` |

### Proposed batch: claude-application-benchmark-01

Scope: 52 fresh subjects, explicitly shipped and control. Include every valid-setup execution. No automatic retry. Pending owner allocation.
Actual attempts: [subject index](runs/application-benchmark-01/claude/run-index.json).

[export-deferral](runs/application-benchmark-01/claude/export-deferral-manifest.json) [quota-grace](runs/application-benchmark-01/claude/quota-grace-manifest.json) [repeated-review](runs/application-benchmark-01/claude/repeated-review-manifest.json) [catalog-review](runs/application-benchmark-01/claude/catalog-review-manifest.json) [helper-rename](runs/application-benchmark-01/claude/helper-rename-manifest.json) [scope-trim](runs/application-benchmark-01/claude/scope-trim-manifest.json) [dispatch-hold](runs/application-benchmark-01/claude/dispatch-hold-manifest.json)

| Order | Case | Condition | Repetition | CONFIG |
| --- | --- | --- | --- | --- |
| 1 | export-deferral | control | 1 | `skill-studies/writing-explicit-rationale/runs/application-benchmark-01/claude/export-deferral-control.json` |
| 2 | export-deferral | original | 1 | `skill-studies/writing-explicit-rationale/runs/application-benchmark-01/claude/export-deferral-original.json` |
| 3 | quota-grace | original | 1 | `skill-studies/writing-explicit-rationale/runs/application-benchmark-01/claude/quota-grace-original.json` |
| 4 | quota-grace | control | 1 | `skill-studies/writing-explicit-rationale/runs/application-benchmark-01/claude/quota-grace-control.json` |
| 5 | repeated-review | control | 1 | `skill-studies/writing-explicit-rationale/runs/application-benchmark-01/claude/repeated-review-control.json` |
| 6 | repeated-review | original | 1 | `skill-studies/writing-explicit-rationale/runs/application-benchmark-01/claude/repeated-review-original.json` |
| 7 | catalog-review | original | 1 | `skill-studies/writing-explicit-rationale/runs/application-benchmark-01/claude/catalog-review-original.json` |
| 8 | catalog-review | control | 1 | `skill-studies/writing-explicit-rationale/runs/application-benchmark-01/claude/catalog-review-control.json` |
| 9 | helper-rename | control | 1 | `skill-studies/writing-explicit-rationale/runs/application-benchmark-01/claude/helper-rename-control.json` |
| 10 | helper-rename | original | 1 | `skill-studies/writing-explicit-rationale/runs/application-benchmark-01/claude/helper-rename-original.json` |
| 11 | scope-trim | original | 1 | `skill-studies/writing-explicit-rationale/runs/application-benchmark-01/claude/scope-trim-original.json` |
| 12 | scope-trim | control | 1 | `skill-studies/writing-explicit-rationale/runs/application-benchmark-01/claude/scope-trim-control.json` |
| 13 | dispatch-hold | control | 1 | `skill-studies/writing-explicit-rationale/runs/application-benchmark-01/claude/dispatch-hold-control.json` |
| 14 | dispatch-hold | original | 1 | `skill-studies/writing-explicit-rationale/runs/application-benchmark-01/claude/dispatch-hold-original.json` |
| 15 | export-deferral | original | 2 | `skill-studies/writing-explicit-rationale/runs/application-benchmark-01/claude/export-deferral-original.json` |
| 16 | export-deferral | control | 2 | `skill-studies/writing-explicit-rationale/runs/application-benchmark-01/claude/export-deferral-control.json` |
| 17 | quota-grace | control | 2 | `skill-studies/writing-explicit-rationale/runs/application-benchmark-01/claude/quota-grace-control.json` |
| 18 | quota-grace | original | 2 | `skill-studies/writing-explicit-rationale/runs/application-benchmark-01/claude/quota-grace-original.json` |
| 19 | repeated-review | original | 2 | `skill-studies/writing-explicit-rationale/runs/application-benchmark-01/claude/repeated-review-original.json` |
| 20 | repeated-review | control | 2 | `skill-studies/writing-explicit-rationale/runs/application-benchmark-01/claude/repeated-review-control.json` |
| 21 | catalog-review | control | 2 | `skill-studies/writing-explicit-rationale/runs/application-benchmark-01/claude/catalog-review-control.json` |
| 22 | catalog-review | original | 2 | `skill-studies/writing-explicit-rationale/runs/application-benchmark-01/claude/catalog-review-original.json` |
| 23 | helper-rename | original | 2 | `skill-studies/writing-explicit-rationale/runs/application-benchmark-01/claude/helper-rename-original.json` |
| 24 | helper-rename | control | 2 | `skill-studies/writing-explicit-rationale/runs/application-benchmark-01/claude/helper-rename-control.json` |
| 25 | scope-trim | control | 2 | `skill-studies/writing-explicit-rationale/runs/application-benchmark-01/claude/scope-trim-control.json` |
| 26 | scope-trim | original | 2 | `skill-studies/writing-explicit-rationale/runs/application-benchmark-01/claude/scope-trim-original.json` |
| 27 | dispatch-hold | original | 2 | `skill-studies/writing-explicit-rationale/runs/application-benchmark-01/claude/dispatch-hold-original.json` |
| 28 | dispatch-hold | control | 2 | `skill-studies/writing-explicit-rationale/runs/application-benchmark-01/claude/dispatch-hold-control.json` |
| 29 | export-deferral | control | 3 | `skill-studies/writing-explicit-rationale/runs/application-benchmark-01/claude/export-deferral-control.json` |
| 30 | export-deferral | original | 3 | `skill-studies/writing-explicit-rationale/runs/application-benchmark-01/claude/export-deferral-original.json` |
| 31 | quota-grace | original | 3 | `skill-studies/writing-explicit-rationale/runs/application-benchmark-01/claude/quota-grace-original.json` |
| 32 | quota-grace | control | 3 | `skill-studies/writing-explicit-rationale/runs/application-benchmark-01/claude/quota-grace-control.json` |
| 33 | repeated-review | control | 3 | `skill-studies/writing-explicit-rationale/runs/application-benchmark-01/claude/repeated-review-control.json` |
| 34 | repeated-review | original | 3 | `skill-studies/writing-explicit-rationale/runs/application-benchmark-01/claude/repeated-review-original.json` |
| 35 | catalog-review | original | 3 | `skill-studies/writing-explicit-rationale/runs/application-benchmark-01/claude/catalog-review-original.json` |
| 36 | catalog-review | control | 3 | `skill-studies/writing-explicit-rationale/runs/application-benchmark-01/claude/catalog-review-control.json` |
| 37 | export-deferral | original | 4 | `skill-studies/writing-explicit-rationale/runs/application-benchmark-01/claude/export-deferral-original.json` |
| 38 | export-deferral | control | 4 | `skill-studies/writing-explicit-rationale/runs/application-benchmark-01/claude/export-deferral-control.json` |
| 39 | quota-grace | control | 4 | `skill-studies/writing-explicit-rationale/runs/application-benchmark-01/claude/quota-grace-control.json` |
| 40 | quota-grace | original | 4 | `skill-studies/writing-explicit-rationale/runs/application-benchmark-01/claude/quota-grace-original.json` |
| 41 | repeated-review | original | 4 | `skill-studies/writing-explicit-rationale/runs/application-benchmark-01/claude/repeated-review-original.json` |
| 42 | repeated-review | control | 4 | `skill-studies/writing-explicit-rationale/runs/application-benchmark-01/claude/repeated-review-control.json` |
| 43 | catalog-review | control | 4 | `skill-studies/writing-explicit-rationale/runs/application-benchmark-01/claude/catalog-review-control.json` |
| 44 | catalog-review | original | 4 | `skill-studies/writing-explicit-rationale/runs/application-benchmark-01/claude/catalog-review-original.json` |
| 45 | export-deferral | control | 5 | `skill-studies/writing-explicit-rationale/runs/application-benchmark-01/claude/export-deferral-control.json` |
| 46 | export-deferral | original | 5 | `skill-studies/writing-explicit-rationale/runs/application-benchmark-01/claude/export-deferral-original.json` |
| 47 | quota-grace | original | 5 | `skill-studies/writing-explicit-rationale/runs/application-benchmark-01/claude/quota-grace-original.json` |
| 48 | quota-grace | control | 5 | `skill-studies/writing-explicit-rationale/runs/application-benchmark-01/claude/quota-grace-control.json` |
| 49 | repeated-review | control | 5 | `skill-studies/writing-explicit-rationale/runs/application-benchmark-01/claude/repeated-review-control.json` |
| 50 | repeated-review | original | 5 | `skill-studies/writing-explicit-rationale/runs/application-benchmark-01/claude/repeated-review-original.json` |
| 51 | catalog-review | original | 5 | `skill-studies/writing-explicit-rationale/runs/application-benchmark-01/claude/catalog-review-original.json` |
| 52 | catalog-review | control | 5 | `skill-studies/writing-explicit-rationale/runs/application-benchmark-01/claude/catalog-review-control.json` |

## Storage and accounting

Canonical checkout: `/Users/simon/work/personal/disciplined-development-skills`.
Durable store: `/Users/simon/work/personal/skill-study-private/writing-explicit-rationale/development/baseline-01`.
Preserve stopped subject bundles under `subjects/` using `docs retain` with the scheduled batch, local order, subject index and committed approval revision.
Keep every evaluator attempt under `evaluators/`, verify the complete bundle inventory and record its charge, config, authority, inventory digest and status in the [evaluator ledger](runs/baseline-01/evaluator-run-index.json).
Keep first-read eligibility, exclusions, mapping, payload/prompt/answer digests and seal times with private controller records.
Stop on an unresolved charge or inventory mismatch. A local copy preserves evidence after scratch cleanup. A verified copy of the constructed examples was restored to scratch and matched the original inventory.
The external `qualification.inventory.json` covers all 728 entries in `qualification/` and hashes to `d229e15631dc749d5a01edadea68d89c274d99d37706ac504b9fab9e0488385e`.
Host loss remains a recovery gap for WER. Include single-host retention in the owner’s allocation decision.

The runner totals below cover its linked subject and evaluator run indexes: the original baseline, the eight functional-pilot subjects and the proposed application benchmark. The original baseline used 24 subjects, 20 evaluators and one retry. The eight pilot subjects are fully spent. Historical comparison batches and the ten pilot/contrast readers use separate ledgers in their checkpoints and do not enter this runner subtotal. No historical capacity carries forward.
Proposed outer limits for the linked indexes: 136 subject, 54 evaluator, 0 authoring and 1 retry invocations.
Dispatched calls are **32 subject, 20 evaluator, 0 authoring, 1 retry**; remaining outer capacity is **104 / 34 / 0 / 0** pending application benchmark approval.
Record benchmark evaluator attempts with distinct run IDs, evaluator role, allocation pool and launcher charge in the version-1 evaluator ledger.

0 active minutes booked; 260 minutes below the 260-minute planning guideline. This is an opening budget ledger for the proposed run sequence. Earlier case development has no measured time entry.
The original end-to-end estimate is 160–260 active minutes. Remaining planning estimates assume a passing checkpoint.

| Work | Estimate | Basis |
| --- | --- | --- |
| Runtime qualification and smoke audit | 25 | Original allowance includes shell qualification and isolated reader inspection |
| Subject collection and retention | 60 | Up to 24 sequential attempts |
| Replay and scoring | 65 | Complete projects, diffs and ordered traces |
| Readings and reconciliation | 65 | Eligibility, sealed packets and two grouped reviews |
| **Total** | **215** | Active minutes, excluding unattended wait time |

## Results and decision

The eight frozen manifests pin input revision `37d66bb9`. Both 12-slot schedules passed the runner’s preparation and collection document checks. Both subject indexes passed structural validation.
The first smoke failed its original catalog rule. The replacement passed under the subscription amendment frozen at `7c63d02b`. The fresh read-only session received the exact frozen prompt, offered all 17 expected skills and the expected tools, plugins and MCP list, and returned an answer in one turn with zero tool calls. The evaluator ledger links both audits and inventories.

### Completed application checkpoint

The [Codex index](runs/baseline-01/codex/run-index.json) and [Claude index](runs/baseline-01/claude/run-index.json) link each valid setup to its verified bundle, criterion record and replay evidence.
The active assessor inspected the final projects, supplied decisions, delivered responses and ordered traces. All eight guided traces delivered the full skill before editing. Both providers used their expected application exposure. The original project tests passed in all 12 code runs, and the private quota replay passed in all eight applicable runs.
The table reports whole-case functional judgments under the frozen policy. One run per cell supports diagnosis only.

| Case | Codex guided | Codex control | Claude guided | Claude control |
| --- | --- | --- | --- | --- |
| Export deferral | Met | Missed the instability reason and customer wait | Met, with certainty caveat | Met |
| Quota grace | Met | Correct timing, missing admitted-work reason | Met | Correct timing, missing admitted-work reason |
| Helper rename | Met | Met | Met | Met |
| Repeated review | Met, with wording caveat | Guard reversal unexplained and second reason absent | Met, with wording caveat | Reply only; both reasons absent from the tree |

In Codex repeated review, both subjects inspected the submitted change. The guided project explained both decisions and left the routine helper alone. It preserved the third-caller trigger but said to factor at that point, a stronger instruction than the agreement to reconsider. The control centralized the guard, passing a constant approval for batches. Its tests passed, but the tree explained neither that reversal nor the quota decision.
The Claude control captured the partner gate and customer wait in the release plan. The guided subject also captured them, then stated that shipping against the moving schema would break XML customers on each revision. The supplied decision gives no compatibility guarantee or failure history. The same categorical claim appeared in the PR summary. The original assessment failed both criteria on that wording.
The complete skill was delivered through Bash before the edit, the catalog matched and the frozen task contained only the supplied team message. This is a valid behavioral observation. One paired result cannot establish that the skill caused the invention.
Collection paused on that initial judgment at slot 10. The owner resumed the six remaining Claude slots for review together, including failures.
Both resumed quota implementations passed the timing replay. Only the guided version explained the risk to already-admitted work and the accepted extra quota at the decision site. Both helper renames preserved the billing explanation verbatim.
In repeated review, both Claude subjects opened the submitted patch. The guided version documented both decisions. Its code says “Revisit by factoring out a shared interactive guard,” retaining the revisit point while leaning toward a solution. Its suggested reply goes further and promises to factor the guard. Codex puts the firmer commitment directly in the code, making its decision-site judgment the closer call. The control supplied a reviewer reply and left the project byte-identical to the fixture; both decision sites still lack rationale.

During owner review the active assessor reread all four export plans and their full PR summaries against the supplied message and starting plan under the same case card.
The Claude guided output accurately communicates retained scope, partner instability, the stable-schema approval gate, customer wait and unaffected milestones in both deliverables.
The task states that the schema is changing. Compatibility risk is a reasonable inference; “every time” presents it as certain on each revision. “No export” can also be read more broadly than waiting for XML, although the surrounding v1 item explicitly preserves CSV and JSON. It leaves the release decision and its condition intact, so T1 and R1 both meet their criteria with one precision observation.
The other three export judgments stand. In particular, the Codex control names the approval gate but leaves the partner’s continuing changes unexplained in both the plan and the handoff.
The original Claude result remains preserved at its original evidence path and in the index at revision `7dd74a9b`. The current index links a separate reassessment of the same run.
The first checkpoint counted 7 of 8 guided runs and 3 of 8 controls meeting all criteria. On 2026-11-10 the owner accepted the reviewed counts of 8 of 8 guided and 3 of 8 controls. The owner-supplied Claude review recorded its export judgments before consulting the checkpoint, agreed on all four and checked both guided repeated-review caveats. Its full text is retained at `application-checkpoint/owner-review/claude-review.txt` in the durable store. There were no subject retries.
Of 12 positive-case outputs, 11 are eligible for independent first readings. The Claude repeated-review control was skipped under the unchanged-site rule; the four routine renames were assessed by diff. Controller-only eligibility, exclusions and packet identities are stored under `application-checkpoint/` in the durable store.
Owner review of the application checkpoint is complete. Independent first readings and full-evidence reconciliation remain pending. Reconciliation will examine whether unsupported elaboration recurs across cases before a skill change is considered.

### Native discovery checkpoint

All eight native attempts had valid setups and verified inventories; each provider received the ordinary request and its native WER catalog entry.
The [Codex index](runs/baseline-01/codex/run-index.json) and [Claude index](runs/baseline-01/claude/run-index.json) link orders 9–12 to the raw evidence, ordered trace judgments and per-criterion assessment.

| Case | Codex selection | Claude selection | Codex artifact | Claude artifact |
| --- | --- | --- | --- | --- |
| Export deferral | Timely read | Timely invocation | T1 met; R1 missed schema instability | Met |
| Quota grace | Timely read | Timely invocation | Met | Met |
| Helper rename | Correct non-use | Correct non-use | Met | Met |
| Repeated review | Timely read | Timely invocation | Met with a wording caveat | Met |

All six positive traces delivered the complete WER body before the case deadline. Both rename traces showed no targeted read or invocation, and both edits preserved the billing explanation.
Codex’s export plan says the partner must approve a stable XML schema and XML customers must wait. The plan and handoff omit that the partner is still changing the schema, leaving open whether the only outstanding action is sign-off. This omission accounts for the recorded R1 miss.

At the 2026-11-22 owner review, the owner judged the omission minor and non-blocking. Taken as a whole, the plan supports both intended actions. The team can ship CSV and JSON on the v1 schedule, and Support can tell XML customers to wait for partner approval without promising a date. The ongoing revisions would give a maintainer more context for a follow-up with the partner.

Both repeated-review projects explain the guards and quota decision at their sites. Codex again instructs maintainers to factor when a third caller appears, a stronger commitment than reconsideration. Claude preserves the revisit condition in the code.
All six code projects passed the original fixture tests; all four applicable private quota replays passed.
Selection met D1 in 8 of 8 observed cells; 7 of 8 projects met all functional criteria under the active assessor’s whole-output reading. One observation per cell limits reliability claims.
All six native positive projects qualify for isolated readings. Together with the application stage there are 17 eligible projects, one unchanged positive control skipped and six routine renames assessed by diff. Native controller packets and eligibility records live under `native-checkpoint/` in the private store. No new readers, reconciliations or subject retries were dispatched.

### Independent reader authority

On 2026-11-22 the owner approved one independent first reading for each of the 17 eligible packets. Retain every attempt, including failures, and report the readings for joint review before reconciliation.

### Independent reader checkpoint

All 17 eligible projects received one fresh Opus medium reading. All 11 application and six native readings completed in one turn with zero tool calls. The evaluator ledger maps each packet to the retained answer, verified bundle inventory and seal. The host CLI had advanced to 2.1.330. A temporary copy of 2.1.319 matched the qualified executable digest before use. All 17 initializations matched the qualified catalog.

The Codex native export reader recovered the v1 scope, partner approval condition, XML customer wait and unaffected release schedule. The reader gave approval as the reason for deferral and supplied no claim about active revisions. The Claude guided export reader recovered the active schema changes and repeated the artifact's claim about breakage on every change.

Both standalone quota controls yielded the timing rule. Their readers treated the motivation as uncertain. The guided and native readings connected the window to previously admitted work. On the native repeated-review projects, the Codex reader described a commitment to factor the guards on another interactive caller. The Claude reader described a condition for considering a shared guard.

These are observations from the sealed readings. Joint review and full-evidence reconciliation are pending.

### Reconciliation authority

On 2026-11-22 the owner approved two read-only Opus medium reconciliations, one per provider's 12 subject outputs. Judge each complete output against the original inputs, retain all results including failures, and return both reviews to the owner. The independent reviewer packets include the applicable sealed first readings and omit prior judgments. The composed prompt SHA-256 values are `80428240961cc519eb16382f077c541d2525a74d3d000a70dd34931b785daa6e` for Codex outputs and `752cca44eb02e2d9ffd1a5288f93f0fcb25042984a2f11a3b70c0e4a4afed217` for Claude outputs.

### Reconciliation checkpoint

Two fresh Claude Opus 5.5 medium reviewers independently assessed 12 outputs each, one reviewer per subject provider. Both completed in one turn with zero tool calls after the 17 first readings were sealed. The [evaluator ledger](runs/baseline-01/evaluator-run-index.json) links the complete prompts, answers, audits and verified inventories. All 24 subject outputs, including failures, were covered. The ordered subject traces supply the native selection judgments.

The reviewers agreed with the active assessor on 59 of 60 functional criterion judgments. Their whole-output counts were 8/8 explicitly guided, 3/8 controls and 8/8 native. The sole difference from the recorded 7/8 native checkpoint was Codex export R1. The reviewer judged it met with uncertainty. The plan conveys the dependency, approver, customer wait and unaffected v1 schedule. Ongoing schema changes are implicit. That is consistent with the owner's assessment of a minor omission. The original score and independent judgment are retained for joint review.

Both standalone quota controls implemented the policy and omitted its reason. All four guided and native projects conveyed why old tokens receive grace and the accepted bounded exposure. Both repeated-review controls missed the guard and quota rationale in the project. All six routine renames met their criteria.

The Claude guided export review treated breakage as a plausible risk and passed the whole output. The isolated reader repeated the stronger claim about every revision. The repeated-review passes also retain a qualification. The agreement was to reconsider at a third caller. Both Codex skill-exposed outputs commit to factoring there. The Claude native comment preserves discretion, while its suggested reply offers earlier factoring if the reviewer still prefers it. The offer is conditional. These observations concern fidelity to the handoff and future decision and remain available alongside the criterion scores.

### Compact rewrite candidate

The owner's comparison objective is better decision-site rationale or equivalent work with a smaller loaded skill. The [first draft](drafts/compact-01/SKILL.md) condenses the [preserved original](cases/skill-original/SKILL.md) from 1,426 to 286 whitespace-delimited words including frontmatter. Its catalog description is byte-identical. The saving applies when the full skill loads. All four development cases informed authoring.

The quota and repeated-review controls exposed a concrete failure to preserve reasons in the project. The guided runs establish the behavior to preserve. The rewrite combines repeated instructions and replaces the rationalizations table and five worked examples with one short plan example. The fidelity guidance distinguishes possible consequences and open reconsideration from commitments. The passing rename controls provide a restraint check. The candidate's effectiveness remains unmeasured.

Proposed first comparison allocation: eight candidate application subjects, one per frozen case per provider, explicitly loading the draft. Compare each result with its retained original and control, using the same whole-output criteria and replays. Report any runtime drift and material regression per case. If the first comparison supports the draft, evaluate native use and independent reader recovery of the exact finalist before adoption. Model dispatch requires a separate comparison allocation.

The drafting review used the shipped concise-writing skill's clause-level and whole-document passes and Superpowers writing-skills 7.0.2. The control failures were missing decision-site explanations, so the draft gives placement instructions and one example outside the four fixtures. The 372-word comprehensive rewrite at `13599fb7d3127334b0d07bfe468767e586ec5f9c:skills/writing-explicit-rationale/SKILL.md` contributed the instruction to reference a shared explanation from related sites. Its requirement to always document what was decided and how it works would broaden routine edits. The candidate retains the shipped reader-uncertainty trigger and the catalog description exercised in baseline discovery.

### Three-candidate application comparison

The owner requested testing the unchanged comprehensive rewrite, compact-01 and a separate edit of the shipped baseline. The [schedule](runs/comparison-01/schedule.json) expands the previously proposed eight application subjects per candidate to 24 total, one per provider and frozen case. It records all mounted input hashes. Retain all attempts and compare whole outputs using the original case cards. No retries, new controls or evaluator calls are allocated in this screen.

The [comprehensive candidate](drafts/comprehensive/SKILL.md) is the exact Git blob from branch revision `13599fb7`. The [baseline edit](drafts/baseline-edit/SKILL.md) derives its trigger, decision-site structure and repeated-review audit directly from the preserved shipped skill. Concise-writing removed duplicated cautions. Superpowers writing-skills informed its positive examples and the instruction to check the other decisions in the change. All four cases are development cases.

The four cases give paired evidence on rationale placement, scope and customer impact, preserving an accepted trade-off, recovering a second decision during review and restraint on a conventional rename. Before adopting a finalist, test a spec or policy edit with existing authoritative reasoning shared across sites. It should exercise whether a reader can follow the explanation, whether copies drift, and whether a plausible but immaterial alternative receives excessive explanation. The current application comparison cannot establish those behaviors, native discovery with a changed description, or reliability across repetitions.

The owner approved one replacement of comparison slot 1 after Codex failed to create its session from the temporary executable path. Preserve the charged launch failure. Run the replacement after the scheduled cells using the hash-identical CLI in the original versioned Homebrew location.
The owner also approved one replacement each for slots 3, 5 and 7. Their Codex sessions returned a final response reporting an absent code-mode host before they could read the candidate or perform the task. The runner marked those sessions complete. Treat them as invalid setups and retain them separately from behavioral outcomes. Verify a successful full skill read after restoring both version-matched helpers before using these replacements.

#### Worked examples, rationalizations and red flags

During collection the owner clarified that compression should preserve the practical value of worked examples, rationalizations and red flags. The [baseline edit with examples](drafts/baseline-edit-with-examples/SKILL.md) is a follow-up to the frozen baseline edit. Its five examples cover test deferral, residual risk, a rule exception, a capacity limit and a code choice. It groups the original rationalizations by the pressure an editor faces and uses concrete warning signs at handoff. Both texts remain inspectable. The 599-word revision has no subject observations.

Two additions would make the suite more informative before adoption:

1. **A shared decision in a spec and its consumers.** Start with current reasoning in a policy document. Ask for an ordinary change affecting two consumers, including one conventional choice. A reader starting at either consequential site should be able to recover the applicable reason and exception. Accept a precise reference or an equivalent concise local explanation. Inspect the whole change for contradictory copies and disproportionate commentary.
2. **A scope cut under brevity pressure.** Ask for a shorter handoff-ready plan containing several superficially similar requirements, only some of which the source actually defers. Include a conditional consequence and a reason recorded outside the plan. Check that a reader can identify the affected items, why they moved and what remains open. Accept any wording or placement that preserves that meaning. This directly exercises the pressure addressed by the shipped examples and warnings.

Freeze these as new cases and exercise the preserved original as well as the exact finalist before interpreting differences. The four existing cases informed authoring and support a development comparison.

#### Application comparison results

All 24 scheduled cells have a valid output with verified full candidate exposure. The [attempt index](runs/comparison-01/attempts.json) includes four additional charged invalid setups and links the four approved replacements to their originals. The [verification record](runs/comparison-01/verification.json) covers the complete retained inventories, full-text exposure and replay outcomes. The first failed launch's unused private runtime was removed after checking it had no session or open handles. The failed run bundle is preserved. The restored Codex 0.167.0 binary and matching helpers live alongside the host default. Both provider CLI hashes match the baseline.

| Explicitly loaded version | Words | Codex outputs meeting all functional criteria | Claude outputs meeting all functional criteria |
| --- | ---: | ---: | ---: |
| Shipped, retained application baseline | 1,426 | 4/4 | 4/4 |
| Comprehensive branch, unchanged | 372 | 3/4 | 4/4 |
| Compact-01 | 286 | 3/4 | 4/4 |
| Baseline edit | 344 | 3/4 | 4/4 |

Active assessor judgments against the frozen case cards:

- **Export.** T1 and R1 met in all six. The comprehensive and baseline-edit Codex plans identify the moving schema and approval gate. Readers have to infer the XML customer wait from the deferred publication. The compact Codex plan names that impact directly. The Claude baseline edit describes breakage as a risk. The Claude comprehensive wording about “no export path” is broader in isolation, but its plan explicitly retains CSV and JSON. All handoffs convey the v1 decision.
- **Quota.** T1 and R1 met in all six. At the branch or its referenced constant, the explanation and surrounding code establish the old-token scope, admitted-work reason and accepted bounded exposure. All six passed original tests and the private boundary replay.
- **Rename.** T1 and R1 met in all six. Every complete project was byte-identical to the expected private rename, including the billing comment. All original tests passed.
- **Repeated review.** T1, R1 and R3 met in all six. All three Codex projects explain the approved-batch reason and guard placement, but turn reconsideration at a third caller into a firmer factoring commitment. Each leaves the quota file byte-identical to the original and misses R2, although the submitted patch and quota source were inspected. All three Claude projects explain the quota decision and meet R2. Claude compact-01 and comprehensive give stronger factoring commitments in the suggested handoff. Claude baseline-edit preserves reconsideration in both project and handoff. The repeated pointers to the shared explanation in the other two Claude projects are a density caveat. All original service tests and private quota replays passed.

These are whole-output judgments by the active assessor on development cases. One run per cell and a historical original leave the cause of the Codex regression uncertain. No independent evaluator, native comparison or held-out test was run in this allocation. Keep the shipped version in place pending review. A targeted comparison of the examples-and-warnings revision and the shipped original on repeated review would test whether the follow-up restores the missed behavior under current conditions.

### Suite extension

[Dispatch hold](cases/dispatch-hold/assessment.md) and [Scope trim](cases/scope-trim/assessment.md) are additional development cases for a future original-versus-finalist comparison. The four original cases retain their previous scores and denominators. The initial extension had ten constructed outputs with offline replay and reader-packet checks. Its [qualification notes](cases/qualification.md#suite-extension) identify the distinctions that need judgment. Independent review of the case design precedes any model allocation.

#### Independent design review

Version 2 of both cards includes a no-skill control. Dispatch hold primarily measures preservation and restraint in a project with a discoverable policy. A bare correct implementation passes. Scope trim tests whether the explanation and conditional obligation survive compression. Its corrected worked example separates the first-month review from the decision to reconsider delivery. See the [extension walkthrough](cases/qualification.md#extension-scoring-walkthrough).

The owner-supplied Claude review proposed 24 calls. A staged allocation would use six fresh Codex repeated-review subjects first (shipped and 599-word revision, three each, interleaved), then twelve scope-trim subjects (two providers, three arms, two each) and six dispatch-hold subjects (two providers, three arms, one each). Compare whole outputs and preserve all failures. The shipped example resembles the guard fixture and the revision was informed by it. This first stage can establish repeatability here. Before adoption, confirm recovery of the second reason on a different task. This proposal has no live allocation.

#### Fable review and proposed first-stage scoring

Fable had seen the earlier cards and independently reran the offline qualification. Version 3 of the extension cards credits accurate policy copies, rules collective deferral wording by recoverable item status and judges compression by removal of redundant prose. The retained comparison record for Codex compact-01 also warrants a precision observation: “third caller” omits “interactive”. The batch caller already exists. The guard context supports the intended reading, but the comment could prompt premature factoring.

For a prospective six-run repeatability check, explicitly mount the exact candidate wherever the frozen repeated-review application setup mounts the shipped skill. Apply its T1, R1, R2 and R3 identically to both arms. Keep the historical card and scores pinned. For each output record whether the trace delivered the submitted commit message, whether the handoff mentions quota, and what a maintainer can recover at the quota decision site or by following a project reference. Record test and replay outcomes separately. A chat explanation, file modification or passing replay alone cannot establish R2. Record the interactive-caller qualifier and distinguish reconsideration from a promise to factor.

Score the project-only R2 reading under opaque labels before opening the arm mapping, subject handoff or trace. Use the complete project projection with GUIDANCE.md and review correspondence excluded. Record the provisional judgment and supporting text, then reconcile against the full original inputs and record any correction. The quota explanation must connect the pre-change tokens to work already admitted that an immediate cut could reject, and convey the bounded elevated quota. A restatement of timing alone misses. Credit an explanation in another project file or test if it clearly identifies this quota decision and a maintainer can find it from the implementation by a reference, shared identifier or other concrete route. Record that route and any discoverability caveat.

The [six-slot schedule](runs/repeated-review-01/schedule.json) pins three interleaved pairs, all using the baseline prompt, project and attachment. Each shipped slot mounts the preserved study copy. Six valid subjects are proposed. Also proposed is a reserve of one replacement total for a verified invalid setup, in the same arm. Determine invalidity from setup evidence before behavioral scoring. Preserve the original attempt and charge. A valid behavioral miss consumes its slot. If the reserve is exhausted, report the individual outcomes and seek a new allocation for missing evidence.

Apply the count rules only with three valid, assessable R2 outcomes per arm. Report all individual results. If shipped meets R2 at most once, flag weak reproduction of the historical result. Advance the revision to further study if it meets R2 at least twice and preserves the other criteria. Carry forward the actual counts, including any advantage for shipped. If both arms meet R2 at most once, investigate both and make no advancement decision on this case. For shipped 3 and revision 0, retain shipped and revisit the draft. Treat the remaining splits as unresolved. Both texts contain fixture-specific cues. Scope trim addresses a separate fidelity question. A different second-decision task is needed before adoption. Allocation awaits owner approval.

Fable’s follow-up confirmed the earlier fixes. Its scope judgments followed inspection of a diff containing the expected verdicts and count as informed design review.

On 2026-11-23 the owner approved the six scheduled Codex subjects and one reserve subject for a verified invalid setup. Retain every attempt and report the checkpoint for joint review before scope-trim.

#### Six-run repeated-review checkpoint

Six approved subjects completed in the scheduled order with valid setups. All six inventory copies and full skill exposures were verified, and all twelve original service and private quota checks passed. Six calls were charged. The reserve was unused. The [attempt ledger](runs/repeated-review-01/attempts.json) preserves every output, including the behavioral failure.

The active assessor recorded the [project-only R2 judgments](runs/repeated-review-01/project-only.json) under shuffled labels before opening the mapping and handoffs. Reconciliation against the original task and submitted commit produced the [per-run assessment](runs/repeated-review-01/assessment.json). All six traces delivered the submitted quota reason. Shipped recovered it at the decision site in two of three runs (slots 3 and 5). Slot 1 explained only the admission guard, and the handoff also omitted quota. The 599-word revision recovered it in all three runs (slots 2, 4 and 6). The five successful handoffs also mentioned quota. All six met T1, R1 and R3. Guard precision varied: several outputs strengthened reconsideration into a commitment, and slot 4's code omitted the interactive qualifier. Slot 6 kept both the qualifier and the open decision.

The revision meets the prospective threshold to advance for further study. Both texts contain cues specific to this fixture. Three observations per arm do not establish a reliable difference in rates or which wording produced the result. Owner review of this checkpoint precedes scope-trim.

#### Scope-trim authority

The owner approved the [12 scope-trim subjects](runs/scope-trim-01/schedule.json), two fresh sessions per provider and arm (preserved shipped, examples-and-warnings revision and no-skill control). Apply the version 4 scope-trim card. Read each complete projected plan under a shuffled label before comparing the original and the delivered handoff. Preserve every attempt and report the checkpoint before dispatch-hold. This allocation contains no replacements or evaluator calls.

#### Scope-trim checkpoint

All 12 approved subjects completed with valid setups. The [attempt ledger](runs/scope-trim-01/attempts.json) retains the full outputs and inventories. All actual launch inputs matched the frozen schedule. Guided traces delivered the assigned skill and control workspaces received only the task and starting plan. The active assessor sealed [project-only judgments](runs/scope-trim-01/project-only.json) under shuffled labels before comparing each plan with the source request and handoff. The [reconciled judgments](runs/scope-trim-01/assessment.json) preserve the only functional miss.

| Arm | Codex T1 / R1 | Claude T1 / R1 |
| --- | --- | --- |
| Shipped | 2/2 and 2/2 | 2/2 and 2/2 |
| Examples-and-warnings revision | 2/2 and 2/2 | 2/2 and 2/2 |
| No-skill control | 1/2 and 2/2 | 2/2 and 2/2 |

All plans preserve the daily and weekly decisions, Finance dependency, possible manual comparison for an affected week, guide handoff and adoption review. In Codex control slot 3 the heading “Monday launch” introduces rollout timing unsupported by the request. Its accurate chat reference to a Monday handoff leaves Operations with conflicting timing in the plan. T1 misses for schedule fidelity and R1 passes. Codex revision slot 7 names Finance agreement as a prerequisite and leaves reconsideration implicit, a precision caveat. Claude revision slot 12 says “come back” in the handoff while the plan clearly says to revisit.

The 599-word revision preserved the target behavior in these four observations. The no-skill controls also conveyed the rationale in all four, so this case showed no incremental rationale benefit. One control timing error and two repetitions per provider and arm give limited evidence for broader claims. No independent evaluator calls or replacements were used. Owner review of this checkpoint precedes dispatch-hold.

### Coverage before the shipped benchmark

The owner selected suite qualification, then a fresh shipped baseline, then a separate rewrite decision.
This supersedes the proposed dispatch-hold candidate allocation.
The original four-case screen and later experiments remain development evidence with their original denominators.

For the fresh benchmark, judge the importance of missing context by the decision it informs.
Identify who would face the choice, what they would reasonably be likely to do on the evidence in the project, and why the omitted fact would materially change that decision.
A merely imaginable misunderstanding or an omitted background detail is insufficient grounds for a rationale failure.
A targeted comment or a discoverable reference is sufficient when the surrounding artifact already explains the rest.
An informed reader can still choose to reverse the original decision.
For example, assess export deferral in light of whether the plan gives a maintainer the right v1 scope, dependency and customer expectation; the exact description of schema churn can be a precision observation if those are clear.
For the fresh benchmark, ask the assessor to identify the project evidence for each consequential reason a reader reports.
A reader who correctly guesses a reason known from the original request can still be missing that reason on the page.
Credit meaning conveyed by the whole artifact, including nearby text, code and discoverable project references.
For a disputed omission, identify what the source established, what the project communicates, and what the reader would still have to assume about the decision, its rationale or its implications.

| Maintainer outcome | Development cases | Evidence and limits |
| --- | --- | --- |
| Recover what a plan deliberately leaves out, why and what happens until reconsideration | Export deferral, scope trim | Both exercised live. Export tests a single customer dependency. Scope trim tests collective wording, similar retained items and a conditional workload. Its controls also recovered the rationale. |
| Understand an active design choice and the cost of reversing it | Quota grace | Live and replayed. Separates a working implementation from one that also explains why admitted work needs protection. |
| Preserve useful explanations during routine work | Helper rename, dispatch hold | Rename exercised live. Dispatch hold is offline-qualified only. It tests a harder boundary where a discoverable spec already explains the policy and a bare implementation can pass. |
| Resolve repeated review and make a second consequential choice understandable | Repeated review, catalog proof review | The live guard case resembles a shipped example and reuses quota. The new [catalog card](cases/catalog-review/assessment.md) tests two independent editorial decisions in a spec. Offline only. An explained second site supports recovery; a claim about the editor's process needs trace evidence. |
| Select WER in ordinary use and exercise restraint | Original four native case cards | One historical native observation per case and provider. Distinguish selection from output quality. The conventional rename is the negative in a module with a real policy comment. |

The seven cases span plans, specs and code, incidental and flagged decisions, useful silence, and rationale trapped in correspondence.
The suite is ready for owner review as a development benchmark of these outcomes.
It does not establish performance on unseen tasks, ground-up spec authoring, long-running change histories or untested providers.
The catalog case is visible development material. A claim about a future rewrite transferring to unseen work requires separately reserved evidence.

The positive cases give the subject the underlying reasons in the task, project or supporting material.
Decisions whose reasons the subject must originate remain unmeasured.
Apply the materiality rule to the guard's third-interactive-caller trigger and the quota grace window: credit context and readable behavior, and record a precision observation when the omission leaves the maintainer's decision intact.
A change that moves admission onto the batch path or hides why admitted work needs protection remains consequential.

### Proposed pilot before benchmark freeze

First propose eight fresh application subjects: catalog proof review and dispatch hold, each with shipped and control on Codex and Claude once.
For all four catalog outputs, propose one isolated maintenance reader each, including outputs missing the rationale.
Inspect packet isolation, task realism and whether the reader decisions reveal anything beyond the subject score.
Preserve every attempt, pause on invalid setup and allow no automatic replacements.
If design or scoring changes, retain pilot evidence separately and start the affected benchmark cells fresh.
The proposed pilot needs its own frozen inputs, manifests and owner allocation.

The previous uniform proposal was 140 application subjects plus 40 native subjects and up to 20 catalog decision readers.
A smaller option is five repetitions on quota, repeated review, catalog and export, and two on rename, scope trim and dispatch hold: 104 application subjects across both providers and arms.
Decide repetitions, native scope and evaluator allocation after the pilot, including the required cross-model review.
Keep historical scope-trim results separate from a fresh benchmark. Any pooling of unchanged pilot cells must be declared before collection.
If all four catalog projects explain the room-sheet dependency, record the missing-rationale branch as untested and propose six fresh readers, three per constructed complete and credit-only packet, for separate approval.
Likewise report any unmeasured reader slots separately before interpreting pilot coverage.
The owner approved the functional pilot only.


### Functional pilot freeze

The [schedule](runs/functional-pilot-01/schedule.json) interleaves providers, reverses arm order within each provider on the second case, and maps subject slots to four isolated catalog decisions.
The [runtime pin](runs/functional-pilot-01/runtime.json) includes both Codex helpers. Prepend the pinned Codex directory followed by the pinned Claude directory to PATH, verify selected executable paths, execute permissions and hashes before launch, and use a fresh directory under the user temporary root.
Recheck provider init, tool use and complete task and assigned skill delivery in each trace. Preserve invalid setups and pause on a mismatch.
Use the existing subject retention command with each provider's local order, committed authorization and run index. The private store is `/Users/simon/work/personal/skill-study-private/writing-explicit-rationale/development/functional-pilot-01`, with subjects, evaluators and controller directories. Retention is on this host.
Before each invocation record its scheduled slot privately, reconcile the runner's invocation-started flag and preserve the stopped bundle with verified inventory before continuing. Stop on uncertainty or missing evidence.
For all catalog outputs, including behavioral failures, retain the full inventory and file-role classification and seal the project reading under opaque labels before full-evidence assessment.
For each decision reader concatenate the exact question bytes with the canonical catalog payload bytes; classify additions using the case card. Preserve exclusions and hash the payload and complete prompt before dispatch.
Copy the pinned reader config to isolated controller staging beside that prompt as prompt.txt. Reader config bytes must match the pinned config, with no fixtures. Require a fresh read-only session, the qualified subscription catalog, zero tool calls, one recommendation and retained prompt, answer, bundle inventory and charge in the [reader ledger](runs/functional-pilot-01/evaluator-index.json).
The final prompt hashes depend on the subjects' future projects. Record unmeasured reader slots and their reason. No automatic replacements or additional diagnostic readers. Owner approval on 2026-11-23 covers the eight frozen subject slots and up to four scheduled decision readers. Preserve failures, pause on invalid setup, and report before any additional allocation.

Installed qualification retained both original Claude scripted-probe failures: the Apple Git launcher emitted cache-write diagnostics under the sandbox.
The pinned Claude directory selects the direct Xcode Git executable. Both scripted CLI modes passed with this path and the same filesystem policy.
The first Codex Git probe exceeded its 60-second harness limit; the isolated repeat passed, and the original scratch evidence was copied to the private controller store.
Subject slots and reader calls remain unused.

### Functional pilot checkpoint

All eight subject sessions completed with valid setups, and all four decision readers produced sealed single-turn recommendations with zero tool calls.
The [assessments](runs/functional-pilot-01/assessment.json) link the complete execution results, reader answers and qualifications.
Both subject indexes validate, all twelve inventories matched the retained bundles, and no replacements were used.

| Case | Codex shipped / control | Claude shipped / control | Outcome |
| --- | --- | --- | --- |
| Catalog proof review | Pass / pass | Pass / pass | All four specs preserve lender amendment authority and the proof-desk reason for room order. |
| Dispatch hold | Pass / pass | Pass / pass | All four private replays passed, both consumers led to the policy, and the routine title stayed proportionate. |

The [opaque project readings](runs/functional-pilot-01/project-only.json) were sealed before reconciliation.
Codex control saved its short editorial reply separately. The delivered handoff linked the file; it counted for the reply task and was excluded from both reader projections.
All four catalog readers recommended keeping accession order for the next proof and grounded that decision in matching corrections to room sheets. They also mentioned the title index.
That establishes informed use of all four artifacts, including both controls. The exercise did not observe how a reader acts when the reason is missing.
The first reader's offline audit initially compared two macOS spellings of the same workspace path; canonical path verification sealed the same retained answer without another call.

All four dispatch plans retained the distinction between excluding new trips and allowing dispatchers to redirect already-loaded parcels.
Both controls used bare lookup functions. Claude shipped introduced a shared status set and a reference to the spec. Codex shipped repeated part of the existing exception in the spec.
All four specs attributed both status values to the carrier, while the starting spec identified the carrier only for manual_hold. This had no effect on the requested routing decision.

The pilot yielded no observed incremental shipped-skill benefit on these two cases. It exercised the packet boundary with actual correspondence and the private replays on three different implementation forms.
Proposal for owner review: use six fresh decision readers on the constructed complete and credit-only specs, three each, with the same printer request and reader settings.
That diagnostic directly tests the missing-context question without buying more subject outputs that may all include the reason.
Its six calls and the full benchmark remain unallocated. Keep these pilot executions outside the fresh benchmark denominators.

### Catalog decision contrast authority

The owner approved six fresh decision readers, three on each constructed catalog project.
The [frozen order and hashes](runs/catalog-contrast-01/schedule.json) pin the previous qualification packets and printer question.
Credit-only keeps the order rule and lender authority. Complete adds the proof-sheet dependency and title-index alternative together, so the contrast measures their combined context.
Use the pilot's pinned Claude runtime, read-only settings, isolation checks and retention procedure. Preserve all outcomes, stop on invalid setup, and allocate no replacements.
Classify the recommended action and the grounds available in the project under the existing catalog card. Separate an inferred purpose from a fact the reader can substantiate. These are diagnostic reader calls outside subject and benchmark counts.

### Catalog decision contrast checkpoint

Six fresh one-turn Claude readers completed the approved diagnostic with zero tool calls. All six bundles, inventories and answers were verified. No replacements were used.
The [individual assessments](runs/catalog-contrast-01/assessment.json) and [evaluator ledger](runs/catalog-contrast-01/evaluator-index.json) preserve all recommendations.

All six kept accession order for the next proof. The three complete-packet readers identified the proof-sheet dependency and pointed to the existing title index.
Of the three credit-only readers, one explicitly recognized the missing reason and labeled its guesses, one deferred to spec-owner approval, and one gave unsupported weight to the cost of changing versus waiting.
All three suggested adding a title index. This was reasonable on their incomplete information and would duplicate something the complete spec already describes.
Both the ordering reason and the index differed between packets. The diagnostic supports a difference in grounded reasoning and follow-up advice; it observed no difference in the immediate printer instruction.
Keep the action and its evidential basis as separate outcomes in the benchmark. These constructed-project readings do not measure the effect of loading WER.

### Shipped application benchmark freeze

The [schedule](runs/application-benchmark-01/schedule.json) assigns 104 new subject sessions, 52 per provider and 52 per condition. Run sequentially by global order, interleaving providers and rotating arm order across repetitions. The first 28 slots cover every case/provider/condition once.
Five repetitions per cell cover export deferral, quota grace, repeated review and catalog review. Two cover helper rename, scope trim and dispatch hold. The smaller strata check restraint and regressions with limited repeatability evidence. Report each provider, case and condition separately.

Use the preserved shipped bytes, pilot runtime pin and its PATH order, subject models at low effort with workspace-write, and fresh isolated sessions. Verify binary identities, config, task, project and supplied attachment hashes and actual exposure from runner logs and traces. Only the shipped arm receives GUIDANCE.md and the explicit read instruction. Keep case cards, evaluator prompts, replays and prior results in the controller. Five cards use application-only projections that retain the functional criteria and boundary rulings. Baseline attempts belong only to this batch.
Seal the [whole-output scoring policy](runs/application-benchmark-01/scoring-policy.txt) with the case definitions. The active assessor conducts opaque project-first readings for all cases; the independent decision readers are the catalog-only sample. After sealing first readings, reconcile against complete original inputs, project, diff, handoff and applicable mechanical checks. Record valid misses and continue. Pause on invalid setup, missing retention, unverified exposure, unresolved charge or a collection-boundary breach. No retries or reserve.
Retain every launched attempt, failures included, using docs retain with the provider batch, local order, run index and committed approval revision. Store inventories, mappings, roles, projections, full prompts, answers, read times, checks and result records under the private single-host development/application-benchmark-01 store. Recheck evidence hashes and record each charge before continuing.

Allocate up to 20 fresh Claude Opus 5.5 medium decision readers, one for each eligible catalog subject regardless of score. Use the pilot read-only configuration, exact printer question and verified catalog projection. Classify added files before composing either reading; unresolved roles or empty projections leave a slot unmeasured. Record action and grounded reasoning separately. Seal these decisions before cross-model review.
Allocate 14 fresh read-only Claude Opus 5.5 medium review calls, one per case and subject provider, covering both arms and every repetition (4 or 10 slots per group). Claude supplies a different family from the active Codex assessor and shares a family with Claude subjects. Use the [review question](runs/application-benchmark-01/review-question.txt) followed by a UTF-8 JSON object containing the task, original fixture, declared review attachment, the frozen materiality rules, applicable criterion text and boundary rulings, and an opaque-labeled array of outputs. Supply whole final project, full handoff including correspondence, diff, replay evidence and raw catalog reader answer when available; identify unavailable evidence and invalid slots. Keep active scores, pilot verdicts, historical examples, conditions and identity mapping outside the review packet. Outputs can themselves reveal exposure; disclose any such clues. Seal the reviewers' own judgments before comparing with active results. Record disagreements separately for owner review.
For both evaluator roles stage the pinned reader config beside prompt.txt, with zero fixtures, fresh init, qualified Claude catalog, no persistence, one response and zero tool calls. Hash composed prompts before dispatch; they depend on future outputs. Preserve failed calls, incomplete group coverage and all bundle inventories in the [evaluator ledger](runs/application-benchmark-01/evaluator-run-index.json). An unusable packet or review cannot silently consume another slot.
The proposed ceiling is 138 model invocations: 104 subjects, up to 20 decision readers and 14 cross-model reviews, zero replacements. No native discovery, rewrite work or live dispatch is allocated by this freeze.

For planning, applying the eight pilot subject durations to 52 calls per provider gives about 73 minutes of serial subject runtime. The six-reader contrast suggests about three minutes for 20 decision readers; the two prior reconciliations suggest about 16 minutes for 14 group reviews. These are approximate CLI runtimes. Packet preparation, replay, assessment and any pauses add time. The historical samples cover different task mixes and group sizes.
