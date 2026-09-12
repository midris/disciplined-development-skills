# Claude skill testing: Codex capability parity

> **Abandoned testing process — historical reference only (2026-09-11).**
> Testing-framework instructions, approvals and pending work below are no longer current. Follow the [new framework spec](../../specs/2026-09-11-model-driven-skill-testing-framework.md) and [new testing plan](../../2026-09-11-model-driven-skill-testing.md).
> The original text is preserved as history; this notice does not retire existing runner tooling or core skills.


**Status:** Completed on `main`; offline verification and scoped live qualification passed.
Owner implementation approval was received on 2026-09-09; one separately requested live CW-01 smoke passed using Sonnet low.
The approved remaining A/B qualification batch passed; its scratch evidence remains available for owner review.
Work stays on `main` in the primary checkout.
The accepted CW evidence and methodology consolidation are integrated separately on `main`; this qualification does not alter their judgments.

## Purpose and compatibility

Support Claude through the same testing tools and workflow already used with the Codex CLI.
Keep `skilltest run CONFIG`, `skilltest worksheet`, configuration schema `"0.2"`, result fields and schema version, bundle paths, worksheets, rubrics and manual scoring unchanged.
Provider, model, effort and provider-native fixture paths are supplied through the existing configuration fields.
Claude skills use `.claude/skills/`; Codex skills use `.agents/skills/`.
Declared companion skills and project instructions remain ordinary explicit fixtures; the installer is not used to populate test conditions from ambient installed skills.

Changes are confined to provider integration, necessary shared plumbing, focused tests and existing operator documentation.
Two existing result-validation restrictions must admit Claude's equivalent lifecycle outcomes: a timed-out child whose exit code is unavailable, and cleanup failure after an otherwise successful invocation.
This is an internal compatibility correction using existing fields and error codes, not a new testing interface.
Existing Codex behavior and retained records must continue to pass the same consumers.

Use the [accepted Claude feasibility findings](../2026-09-06-skilltest-claude-controlled-inputs.md#accepted-scope-and-next-checkpoint).
No new testing tool, campaign manager, scorer, scenario catalog, behavioral criterion or provider/model matrix is included.

## Provider integration

Run Claude from `workspace/fixture/` and grant access to sibling `workspace/evidence/`.
Apply the existing pre-launch prompt/fixture byte checks.
Prepare a fresh, template-free Git repository in the fixture root, as Codex does.
Suppress inherited user/system Git settings during both preparation and Claude's shell operations; normal HOME is retained for Claude authentication only.
Reject declared or existing fixture-root `.git` entries before initialization; never replace supplied content.
Fixtures needing commits supply their own test identity rather than relying on the owner's Git configuration.

Use the accepted macOS launch controls: explicit environment, project-only settings, empty MCP configuration, disabled persistence/memory/Chrome integration, checked instruction ancestry and the child-only policy blocking the recorded host semantic-input roots and home writes.
Reuse the existing subscription with normal HOME/USER; the spike established that private HOME prevented authentication.
Derive paths from the invoking environment, resolve the executable once, and use that executable for preparation and execution.
Keep temporary runtime files outside retained evidence and secrets out of logs.
Never extract/copy credentials, log out, alter shared settings or manipulate existing sessions.
Unavailable required controls or authentication fail preparation; there is no uncontrolled fallback.

Keep native discovery enabled and supply the fixed local tools Read, Skill, Glob, Grep, Write, Edit and Bash with noninteractive permissions and no permission-bypass mode.
Replace the old simple-system-prompt/bundled-skill suppression baseline with the accepted spike's controls.
Retain provider-supplied common features as recorded experimental inputs, subject to the existing drift checks.
The policy establishes scoped contamination controls, not exhaustive filesystem isolation or complete visibility into real provider requests.
Shell startup and file-writing behavior require qualification beyond the spike's Read/Skill observations.

Reuse the existing owned-process lifecycle: 30-second setup limits, 900-second model timeout, bounded termination and cleanup of only the invocation's process group and temporary runtime.
Extract shared mechanics only where both adapters actually need them.
Earlier failures remain primary when cleanup also fails; preserve raw outputs and the actual exit code, including null when unavailable.
Retain unresolved runtime paths for manual handling under the existing cleanup policy.

## Evidence and result handling

Keep complete Claude `stream-json` stdout in `stdout.txt` and raw stderr in `stderr.txt`.
Extract the unambiguously reported successful terminal answer into `final.txt`; do not substitute serialized trace events or synthesize an answer.
Retain initialization metadata and tool calls for the existing full-trace manual review.

Use the existing mechanical result categories and error precedence for preparation, launch, timeout, nonzero exit, artifact-write and cleanup failures.
Remove the earlier proposal to add automatic output-validity classification: that would exceed Codex parity and require a new result policy.
Empty, malformed, missing or provider-reported error output does not by itself change a zero process exit into an invented nonzero exit or an artifact-write error.
If no reliable successful terminal answer is extractable, leave `final.txt` absent and record the extraction limitation in `runner.log` while retaining the raw trace.
An explicitly reported empty successful answer may produce an empty final file.
A mechanically `COMPLETED` invocation is not a claim that its evidence is valid or scoreable; the existing manual evidence review handles that distinction for both providers.
Real file-write failures still use `ARTIFACT_WRITE_FAILED`.

## Parity acceptance checks

Use this checklist inside the spec and the existing test/runbook structure; do not create another tracking system.

| Existing capability | Required Claude result | Verification |
|---|---|---|
| Same invocation and configuration | Existing provider/model/effort and fixture fields select Claude; no new command or config key. | Existing CLI process smoke with a dummy provider. |
| Declared inputs | Prompt and fixture hashes match their frozen sources; evaluator-only material is not supplied. | Offline preparation tests and the existing input audit. |
| No-skill control | Assigned DD skills are absent; declared common dependencies/provider inputs remain recorded. | Native catalog qualification and trace review; this means no assigned DD skill, not an empty provider catalog. |
| Assigned skill A/B | Each fresh condition discovers and can load only its supplied version; other observed inputs remain controlled. | Reuse applicable contamination evidence, then affected native catalog/loading qualification. |
| Composition | Declared parent/companion/dependency skills remain discoverable and readable together. | Qualification using supplied companion fixtures; no new behavioral rubric. |
| File, shell and Git work | Read/search fixtures, write/edit evidence, execute required local shell commands and use the fresh Git repository with fixture-owned identity. | Dummy-provider process smoke plus representative live tool qualification. No claim about unexercised external services or delegation. |
| Retained evidence | Raw trace, final answer when available, source provenance and final artifact inventories occupy the existing bundle paths. | Offline result/artifact checks and manual qualification trace inspection. |
| Lifecycle failures | Setup, launch, nonzero exit, timeout, interruption and cleanup preserve the same mechanical distinctions as Codex. | Existing unit/process-smoke structure; validate both providers against the narrowly updated result schema. |
| Unchanged scoring tools | Existing worksheet generation consumes Claude success/failure bundles; scoring still uses the same ledgers and rubrics. | Existing worksheet command on dummy Claude bundles, plus Codex regression coverage. |

These checks establish parity for the currently supported local testing workflow, not identical provider tool names, hidden prompts or model behavior.
Discoverability, effectiveness and composition assessments remain scenario responsibilities; forced loading during qualification is not an effectiveness result.

## Order and approval boundaries

1. Owner approval of this revised spec was received on 2026-09-09.
2. Implement test-first in the existing runner unit tests and process-smoke group using dummy providers, then run the Codex regression checks and required repository checks.
3. Update the runner README and existing qualification/runbook guidance for the Claude adapter and fixed compatibility limits.
4. Prepare and review only the affected qualification checks before proposing any live calls.
   Local inspection found Claude Code `2.1.266`; the accepted spike used `2.1.261`.
   Reuse retained evidence where supported, but do not treat the newer CLI or expanded tool set as already qualified.
5. Present exact commands, prompts, model, effort and call count for a finite live qualification batch, with separate owner approval before execution.
   Cover the parity conditions above with as few calls as demonstrate the needed capabilities; do not begin an effectiveness campaign.

## Review record

Round 1 found two issues: proposed output/lifecycle handling did not fit the existing result contract, and verification omitted parts of Codex capability parity.
The revision removes the extra output-validity policy, identifies the two necessary provider-neutral lifecycle validation changes, and adds fresh Git preparation plus the parity checklist above.
Review sources are the current provider/runtime/orchestration code, result schema and tests, worksheet consumer, runner README, qualification reference and accepted Claude feasibility findings.
Installed CLI help and the official [CLI reference](https://code.claude.com/docs/en/cli-reference) and [programmatic usage guide](https://code.claude.com/docs/en/headless) support the selected command surfaces; they do not prove isolation or qualification.
Round 2 rechecked the full revised spec against both findings and the current consumers: existing fields/error codes cover lifecycle parity, output extraction adds no new validity verdict, and every listed capability has an offline or separately approved live check.
The review also confirmed that normal HOME must not reintroduce user Git settings during shell operations; the provider contract makes that suppression explicit.
No remaining P0/P1/P2/P3 findings.
Spec review verdict: PASS; this is not implementation approval or provider qualification.
No provider call is authorized by implementation approval.

## Implementation progress

- [x] Retain Claude trace/final output and accept equivalent lifecycle results through existing consumers.
- [x] Integrate controlled Claude runtime and shared owned-process mechanics; verify with dummy-provider unit and process tests.
- [x] Reconcile current runner/operator guidance and review the change; run required checks.
- [x] Document affected qualification checks in the existing [qualification reference](../../../skill-validation/pilot/qualification/README.md#claude-qualification-checkpoint).
- [x] Prepare and audit the exact remaining qualification batch using provider-free checks.
- [x] Obtain approval and execute the two prepared live calls; inspect evidence before closing qualification.

## Implementation verification

Output/lifecycle tests first failed in eight cases against the old adapter/result handling; controlled invocation tests then failed in eight cases against the inherited Claude launch path.
Focused runtime tests covered missing controls/authentication, ancestry and Git collisions, explicit environment, temporary state and protected host inputs.
The complete offline runner suite passed **266 tests** with host permission, using executable dummy providers and surrogate profiles only.
The controller sandbox denies even an allow-default `sandbox-exec /usr/bin/true` probe; the first sandboxed suite consequently had six Claude process-smoke failures while 260 tests passed.
Host execution permitted the real macOS child-policy checks without weakening that policy or contacting a real provider.
The final unit-only rerun passed **254 tests**, with 12 process-smoke cases deselected.

Process smokes exercised actual `skilltest run` and `skilltest worksheet` commands for no-DD, A, B and composition fixture layouts, plus real local Git/evidence writes and surrogate read/write denial.
Dummy processes do not establish Claude's native catalog or model behavior; those remain explicit qualification requirements.
The hook suite passed **263 tests, 3 skipped**; changed navigation links and `git diff --check` passed.
Scratch test output is retained under `/private/tmp/dd-claude-*-tests.txt` and `/private/tmp/dd-claude-unit-final.txt`; RED outputs remain under `/private/tmp/dd-claude-*-red.txt`.

Final inline implementation review checked the approved scope, Codex regression behavior, result/worksheet compatibility, status-output privacy, shared process ownership, extraction limits and operator guidance.
No remaining findings.
No skill bodies, scenario prompts/rubrics, accepted evidence, installed consumer files or shared authentication were changed during offline implementation, and that phase made no real model calls.

## First live smoke

The owner subsequently requested one real call using Opus medium or Sonnet low; the selected CW-01 pilot current-DD scenario ran once with Sonnet low through the existing runner.
Claude Code `2.1.266` resolved `sonnet` to `claude-sonnet-5`; the invocation completed in 3.036 seconds with exit 0 and no retry.
Scratch preparation preserved the existing pilot inputs and rubric, adapting only the native `.agents/skills/` path to `.claude/skills/`.
The historical pilot skill snapshot was used, not the comprehensive rewrite candidate.
The trace shows native `Skill` loading of the entire supplied CW body and a revision passing all existing semantic and task-fidelity criteria.
The unchanged worksheet command consumed the live bundle; fixture hashes and runtime cleanup were verified.
The complete command, recoverable uncommitted implementation freeze, provenance, trace and scored worksheet are linked from `/private/tmp/skilltest-claude-live-_0vbhnxg/summary.md`.

This is a successful exploratory smoke, not an accepted controlled comparison or complete qualification.
The read-only scenario did not exercise file writes, edits, shell/Git operations, no-DD/A/B conditions or companion loading.
Its common native skill names matched the prior real spike; full request equality and broader provider parity remain unproved.
The single-call authorization is exhausted; further calls need a separately approved scope.

## Remaining qualification preparation

The owner authorized preparing the remaining checks and presenting the live batch before execution.
The proposed batch is two Sonnet-low calls using the same task and companion fixtures, changing only the historical synthetic probe from A to B.
Both calls require native body loading, file search/read/write/edit and one fixture-local Git commit with explicit test identity.
Combining these operations keeps the batch small while preserving comparable A/B inputs; it does not assess skill effectiveness.
No-DD catalog inspection and a competing-user-skill positive control use initialization-only diagnostics with surrogate profiles, dummy authentication and verified network denial.
The preparation and exact proposed commands are retained in `/private/tmp/skilltest-claude-qualification-6khgqirh/summary.md`.
Provider-free preparation passed with unchanged Claude Code `2.1.266`: A/B initialization metadata matches after PID/assigned-marker normalization; no-DD differs only by the 12 supplied skills, with 40 common command entries unchanged.
The user-enabled positive/denied pair verifies suppression of a competing surrogate user skill; actual preparation rejects a surrogate ancestor instruction before authentication.
All initialization diagnostics used verified network denial, remained idle without model messages and removed their temporary runtimes.
The scratch record retains the initial network-probe cwd correction and non-discriminating project-only positive control, plus their successful follow-up checks.
Inline preparation review found no remaining issues; no runner or skill code changes were needed.
The owner approved both exact commands; each completed once without retry.
The comprehensive rewrite and accepted CW evidence are unchanged.

## Qualification completion

The A/B calls both passed on Claude Code `2.1.266`, model `claude-sonnet-5`, low effort: A completed in 46.649 seconds and B in 41.808 seconds, both exit 0.
Each trace contains the correct synthetic probe body plus complete DD/CW/WER/writing-plans bodies, support/task reads and all seven configured tools.
Independent inspection confirmed the requested evidence write/edit, all original fixture bytes unchanged, and one fixture-local commit with explicit identity containing only `fixture/allowed.txt`.
The existing worksheet command consumed both live bundles without modification.
Provider stderr and permission-denial lists were empty; owned runtimes and recorded process-specific sockets were removed.
The live catalogs match; full initialization metadata differs only by cwd, session ID, event UUID and messaging-socket path.

Together with the recorded offline tests, no-DD/A/B catalog controls, user/ancestor controls and earlier CW smoke, this completes the listed local-workflow parity checks.
No further tooling changes were needed.
The finding remains conditional on the pinned setup and exercised local operations; hidden provider requests, automatic shell-startup reads and broader filesystem isolation retain their documented limits.
New skill/dependency/tool or CLI changes use the existing affected-control requalification rule rather than inheriting universal coverage.
The B subject used a weak relative-path check for the evidence location; its actual file-tool paths and independent Git-root inspection establish the required state, with the limitation retained in its worksheet.
The scratch summary links both full traces, worksheets, artifact/Git audits, prepared commands and input provenance: `/private/tmp/skilltest-claude-qualification-6khgqirh/summary.md`.
The two-call approval is exhausted; no effectiveness campaign or accepted-evidence promotion is implied.
