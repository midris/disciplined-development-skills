# Writing explicit rationale — study protocol

Format version: `1`
Study ID: `writing-explicit-rationale`
Status: inputs frozen. Both provider batches passed preparation and collection document checks. The installed shell and isolation probes passed. The replacement smoke qualified the reader. The owner accepted the reviewed application checkpoint. All eight native slots are retained. All 17 independent readings are sealed for joint review.
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

## Storage and accounting

Canonical checkout: `/Users/simon/work/personal/disciplined-development-skills`.
Durable store: `/Users/simon/work/personal/skill-study-private/writing-explicit-rationale/development/baseline-01`.
Preserve stopped subject bundles under `subjects/` using `docs retain` with the scheduled batch, local order, subject index and committed approval revision.
Keep every evaluator attempt under `evaluators/`, verify the complete bundle inventory and record its charge, config, authority, inventory digest and status in the [evaluator ledger](runs/baseline-01/evaluator-run-index.json).
Keep first-read eligibility, exclusions, mapping, payload/prompt/answer digests and seal times with private controller records.
Stop on an unresolved charge or inventory mismatch. A local copy preserves evidence after scratch cleanup. A verified copy of the constructed examples was restored to scratch and matched the original inventory.
The external `qualification.inventory.json` covers all 728 entries in `qualification/` and hashes to `d229e15631dc749d5a01edadea68d89c274d99d37706ac504b9fab9e0488385e`.
Host loss remains a recovery gap for WER. Include single-host retention in the owner’s allocation decision.

Proposed outer limits: 24 subject, 21 evaluator, 0 authoring and 1 retry invocations.
Dispatched calls are **24 subject, 18 evaluator, 0 authoring, 1 retry**; remaining outer capacity is **0 / 3 / 0 / 0** under the proposal. Both reader qualification calls are spent.
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
