# Writing explicit rationale — study protocol

Format version: `1`
Study ID: `writing-explicit-rationale`
Status: inputs frozen. Both provider batches passed preparation and collection document checks. The installed shell and isolation probes passed. Collection paused. The approved reader smoke failed its catalog check.
Plan: [current milestone](../../plans/2026-09-11-model-driven-skill-testing.md#wer-milestones)
General spec: [testing framework](../../plans/specs/2026-09-11-model-driven-skill-testing-framework.md)

## Sources and intended use

A future maintainer encounters a choice in a plan or in code without the original conversation. The study asks whether that person can recover the reason and accepted consequence from the edited tree. The [shipped WER skill](../../skills/writing-explicit-rationale/SKILL.md) was inspected at main revision `2a0e2499a39c2000fa2bab3152e12f41f26f038a`, SHA-256 `97eb06c649c194e8819b4dff68b808eda4ec7c948a6ead518da247daf31d6cfe`. Earlier scenarios supply fixture facts. All baseline results will come from fresh runs.

## Behavioral contract and consumers

WER should make consequential choices understandable at the decision site, preserve the supplied facts, and leave self-evident edits concise. Repeated review of the same decision should prompt an audit of related choices in the change. The subjects edit project artifacts. A fresh reader sees a single final project as a maintainer would.

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

## Suite and evidence

| Proposed case | Behavior under test | Distinguishing evidence |
| --- | --- | --- |
| Defer XML export | A deliberate omission remains intelligible in the plan. | A reader recovers the retained scope, deferral reason and customer impact from the affected item. |
| Preserve prior quota | A surprising code choice carries the reason and trade-off. | Timing tests verify the policy. The code explains what immediate reset would break and the bounded exposure it accepts. |
| Rename a private helper | Routine work preserves existing rationale and avoids invented justification. | The rename works, the nearby quota explanation survives, and the diff adds no misleading rationale. |
| Address repeated review | The editor examines the change for other unexplained decisions. | The tree explains both the flagged guard and a second consequential choice. The routine edit stays concise. |

The [four case cards and runnable fixtures](cases/README.md) have been exercised against [20 constructed outputs](cases/qualification.md). There are zero subject observations. They cover plans and code, explicit application, native selection and an explicitly conventional rename. The export and standalone quota requests explicitly supply the reason, so success can reflect good placement of supplied facts. A tie indicates no observed incremental benefit on these prompts. The rename is an easy negative. Repeated-review R2 measures recovery of a second decision; inspect the trace separately before attributing that recovery to a broader audit. Standalone spec writing and transfer to unfamiliar tasks remain outside this focused screen. The [case design](../../plans/specs/2026-11-08-wer-focused-baseline.md#cases-and-acceptance) supplies the task details for packaging.

## Execution scope and authorization

The two provider batches share a stage gate. Complete local orders 1–8 for Codex, then 1–8 for Claude. Inspect all 16 application outputs before releasing orders 9–12 for Codex and then Claude.
Run one slot at a time in a fresh session. Pause for an invalid setup, missing preservation or unresolved charge, a policy change, an incomplete guided task or a material invented rationale.
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
Use that catalog with the probe removed as the expected Claude control/reader catalog and with WER substituted for native. Compare actual names and provenance to the retained init records. Check actual Codex catalog and ordered loads on the first approved traces.
The single approved live reader smoke completed in 14.2 seconds. Its fresh read-only launch disabled persistence, the fixture contained only the Git boundary, the captured prompt matched the frozen bytes, and the full trace contained one turn and zero tool calls.
The init listed 17 skills. Compared with the 16 expected built-ins, it added `schedule` and removed none. The tools, three plugins and empty MCP list matched. WER was absent.
The frozen rule requires catalog agreement. The reading is unusable for qualification. The [evaluator ledger](runs/baseline-01/evaluator-run-index.json) pins the complete retained bundle inventory, private audit and authority.
Investigate the difference between the scripted and live catalogs offline before proposing a remedy. A replacement smoke requires a separate allocation and approval.

### Proposed batch: codex-baseline-01

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

## Storage and accounting

Canonical checkout: `/Users/simon/work/personal/disciplined-development-skills`.
Durable store: `/Users/simon/work/personal/skill-study-private/writing-explicit-rationale/development/baseline-01`.
Preserve stopped subject bundles under `subjects/` using `docs retain` with the scheduled batch, local order, subject index and committed approval revision.
Keep every evaluator attempt under `evaluators/`, verify the complete bundle inventory and record its charge, config, authority, inventory digest and status in the [evaluator ledger](runs/baseline-01/evaluator-run-index.json).
Keep first-read eligibility, exclusions, mapping, payload/prompt/answer digests and seal times with private controller records.
Stop on an unresolved charge or inventory mismatch. A local copy preserves evidence after scratch cleanup. A verified copy of the constructed examples was restored to scratch and matched the original inventory.
The external `qualification.inventory.json` covers all 728 entries in `qualification/` and hashes to `d229e15631dc749d5a01edadea68d89c274d99d37706ac504b9fab9e0488385e`.
Host loss remains a recovery gap for WER. Include single-host retention in the owner’s allocation decision.

Proposed outer limits: 24 subject, 21 evaluator, 0 authoring and 0 retry invocations.
Dispatched calls are **0 subject, 1 evaluator, 0 authoring, 0 retry**; remaining outer capacity is **24 / 20 / 0 / 0** under the proposal. The single approved evaluator invocation is spent.
Evaluators comprise one smoke, up to 18 eligible isolated positive-case readings and up to two provider-grouped reconciliations. Invalid readings consume their invocation. Any repeat needs a new allocation.

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
Zero subject observations. The constructed smoke failed qualification on catalog drift. Further dispatch awaits resolution and owner approval.
