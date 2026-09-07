# Skill-test pilot runbook

[Current status, approval boundaries and next action](../../plans/2026-09-06-skilltest-sol-low-pilot.md) live in the active plan.
The [charter](../charter/core-contracts.md) and [methodology](../../plans/completed/specs/2026-09-02-skill-testing-methodology-design.md) govern judgment.
This is a procedure for an agent, not a campaign program; configs declare inputs and the runner owns runtime setup.
Do not rerun a completed attempt or invoke a proposed config merely because it appears in a document.

## Qualification versus routine execution

Use the [qualification reference](qualification/README.md) for new or changed discovery, dependencies, harness controls or tools.
Reuse its evidence only for controls demonstrably unchanged; unproved controls stop launch.
For a qualified setup the routine path is: check inputs/version → run → inspect evidence/cleanup → score → update the summary.
Do not repeat canaries, dummy profile setup, synthetic worksheet exercises or paid qualification calls per observation.
The [Codex adapter](../runner/README.md#codex) owns private HOME/CODEX_HOME/TMPDIR, auth preflight, template-free Git boundary, input checks, exact invocation and cleanup; never duplicate that setup around a real run.

## Preparation and freeze

Work in `/Users/simon/work/personal/disciplined-development-skills/.worktrees/skilltest-input-isolation-spike` on `spike/skilltest-input-isolation`.
Preserve main, the unrelated rewrite worktree and all 105 accepted historical records.
Before collection, audit and commit the prompt, rubric, config, scoring interpretation and declared fixture/dependency files; record that full revision in the scratch summary.
Require a clean worktree and retain a recoverable input revision plus the qualification decision.
A changed prompt is a new input revision, never a relabeling of prior observations.

The initial pilot's nine DD skills are frozen from main `ca14bbe24f8aea957dbcfeece3511226e929243d` and match the pre-rewrite skill baseline `ac45ab2`.
Its common Superpowers subset is 6.3.0 writing-plans plus plan-document-reviewer-prompt.md; its MIT notice stays outside subject fixtures.
Configs are the single file/target inventory: inspect their source paths and native `.agents/skills/` targets instead of maintaining another manifest.
Current-DD supplies all nine DD skills, no-DD supplies none; both retain the same declared Superpowers/task tools and no DD hooks.
Keep evaluator instructions, rubrics, accepted outputs and credentials out of subject inputs; reject undeclared sources and symlinks.

Audit prompt pairs for equal task/output boundaries and only intended treatment differences.
Declare whether the scenario tests behavior or discovery, following the [separate test-purpose contract](../../plans/specs/2026-09-06-skilltest-controlled-inputs-design.md#accepted-separation-setup-discovery-and-behavior).
Behavior prompts explicitly load the target/composed skills: common Superpowers directives stay the same, while no-DD omits DD directives and files.
Verify requested reads in the trace; retain ignored directives as fidelity failures without claiming loaded-skill behavior or silently excluding the observation.
Only dedicated discovery scenarios omit skill-loading hints and judge spontaneous selection; do not conflate either type with setup qualification.
DR-02 permits only its requested evidence-note write; LP-01 is response-only.
The clarified LP prompts explicitly say application source is not supplied; this post-pilot change applies only to future runs.
To inspect the four completed observations' exact prompts/configs/rubrics, use their recorded revision `e537c03909eb2b4f1986e4170a3f1b662d29a719`, not current source files.
Their retained evidence and judgments are unchanged.

## Execution record

Use one scratch summary with the frozen revision, qualification reference, provider/model/effort, ordered attempt table and exact approved commands.
Link the active plan for the next project action; keep attempt-specific recovery instructions with their evidence.
Each row links its runner bundle, CLI capture and completed worksheet; record exclusions/retries and unresolved cleanup there.
Do not routinely create a second per-run result narrative or rewrite the runner's logs into a custom audit report.
Preserve required raw evidence and verification outcomes; add a separate note only when an exception needs explanation.
Existing pilot evidence is retained through owner review, not deleted to conform to the simpler future layout.

The initial sequence below specifies Codex / gpt-5.6-sol / low, fresh runtime each time; consult the active plan for completion and approval status:

| Label | Config beneath this directory | Role |
|---|---|---|
| q-no-dd | qualification/no-dd/test.json | Qualification |
| q-current-dd | qualification/current-dd/test.json | Qualification |
| dr-01 | dr-02/no-dd/test.json | No-DD observation |
| dr-02 | dr-02/current-dd/test.json | Current-DD observation |
| lp-01 | lp-01/no-dd/test.json | No-DD observation |
| lp-02 | lp-01/current-dd/test.json | Current-DD observation |

Counts and order for any extension must be approved and frozen before collection.
Keep every planned judgeable result, including FAILs; do not increase effort or add repetitions to obtain a preferred verdict.
Medium diagnostics and all new provider commands require separate exact-command approval.

### Behavior extension inputs

Use the same routine with these six input configs, in the listed order; preparation does not authorize their provider commands:

| Attempt label | Config beneath this directory |
|---|---|
| dr05-no-dd | `dr-05/no-dd/test.json` |
| dr05-current-dd | `dr-05/current-dd/test.json` |
| lp05-no-dd | `lp-05/no-dd/test.json` |
| lp05-current-dd | `lp-05/current-dd/test.json` |
| ar03-no-dd | `ar-03/no-dd/test.json` |
| ar03-current-dd | `ar-03/current-dd/test.json` |

All use Codex / gpt-5.6-sol / low, once per condition; no discovery tests or repetitions are included.
The eight task files are byte-preserving copies from the corresponding source scenarios at `d6ba84546e4e5547b457a8ed6f1982af75944c73`, under `inputs/tasks/{dr-05,lp-05,ar-03}/`.
Both arms supply the same four Superpowers files: existing 6.3.0 writing-plans/guidance plus requesting-code-review/SKILL.md and code-reviewer.md from the installed package's verified 6.3.0 manifest.
The existing MIT notice remains outside subject fixtures; all nine DD copies are unchanged.
Source/target inventories live in the configs; audit their copied bytes and retain tied hashes in scratch before collection.
The added review skill changes the common catalog: complete affected catalog/common-input qualification and check the CLI version/digest before inheriting the original pilot's controls.

The [extension scoring mapping](../../plans/specs/2026-09-06-skilltest-controlled-inputs-design.md#proposed-pilot-extension-explicitly-loaded-behavior-under-pressure) and paired rubrics are evaluator-only.
DR-05/LP-05 rubrics preserve their source bytes; AR-03 permits equivalent material severity and blocking-conclusion wording instead of requiring DD marker syntax.
For every extension run, record all requested full skill reads and their order as loading fidelity; keep it separate from semantic task behavior and native discovery.
There are no permitted fixture/evidence edits, network task calls or agent dispatches. These are fidelity checks, not new skill invariants; ordinary answer formatting has no authenticated consumer, so deterministic protocol is N/A.
AR-03 uses the supplied reviewer criteria directly, not a Git-range or delegated review. LP-05 supplies task facts only, not application source/tests.
Compare results only within each frozen pair; the completed original four observations are not matching-input repetitions.

## Per-run commands and checks

From the feature-worktree root, set these path abbreviations from the approved summary row, not a newest-directory guess:
`PILOT_SCRATCH`, `PILOT_ATTEMPT` (a new attempt directory), `PILOT_CONFIG` (absolute config path), `PILOT_INPUT_REVISION` and `PILOT_REFERENCE` (fixed qualified CLI capture directory).
For the recorded pilot, scratch is `/private/tmp/skilltest-sol-low-pilot.Lunoau` and reference is its `preflight/` directory.
Verify that the approved scratch root, its `runs/` directory and the attempt parent directory exist before launch; otherwise stop and prepare those exact scratch paths before using the command.
An absent TMPDIR can redirect temporary allocation outside the intended scratch package; never rely on fallback allocation.
Create the attempt directory once without `-p`; a collision means inspect/resume existing evidence, not overwrite it.
Expand all abbreviations in the complete provider command shown for owner approval.

Run each prelaunch check separately, require exit 0, and require status output to be empty:

```sh
git status --short
git diff --exit-code "$PILOT_INPUT_REVISION" -- skill-validation/pilot skill-validation/runner
test -d "$PILOT_SCRATCH/runs" && test -d "$(dirname "$PILOT_ATTEMPT")"
mkdir "$PILOT_ATTEMPT"
/opt/homebrew/bin/codex --version > "$PILOT_ATTEMPT/cli-version.txt" 2> "$PILOT_ATTEMPT/version-stderr.txt"
/usr/bin/shasum -a 256 /opt/homebrew/bin/codex > "$PILOT_ATTEMPT/cli-sha256.txt"
test -s "$PILOT_REFERENCE/cli-version.txt" && test -s "$PILOT_REFERENCE/cli-sha256.txt"
cmp "$PILOT_REFERENCE/cli-version.txt" "$PILOT_ATTEMPT/cli-version.txt"
cmp "$PILOT_REFERENCE/cli-sha256.txt" "$PILOT_ATTEMPT/cli-sha256.txt"
```

Do not replace fixed references to hide drift; capture version/digest immediately before every invocation, including retries.
After explicit approval of its fully expanded form, execute the row's one-run command:

```sh
/usr/bin/env TMPDIR="$PILOT_SCRATCH/runs" PATH=/opt/homebrew/bin:/usr/bin:/bin:/usr/sbin:/sbin /Users/simon/work/personal/disciplined-development-skills/.worktrees/skilltest-input-isolation-spike/skill-validation/runner/.venv/bin/skilltest run "$PILOT_CONFIG" > "$PILOT_ATTEMPT/command-stdout.txt" 2> "$PILOT_ATTEMPT/command-stderr.txt"
```

Record command, cwd, exit status and stdout's exact bundle path in the summary.
Host/network permission may be needed for the same approved command; keep the subject's workspace-write sandbox.
Never print credentials, change authentication or broaden flags to make a run succeed.
Inspect result.json, runner.log, raw trace, final answer and produced files before scoring.
Verify the resolved executable/options, prelaunch hashes and protected fixture bytes; confirm permitted writes and exact runtime cleanup.
Final fixture inventories are not prelaunch evidence, and absence of a visible violation does not prove hidden provider inputs absent.

## Scoring and handoff

Before collecting a new scenario or rubric revision, record a short evaluator-only mapping from its existing criteria to charter invariants, ledgers and observable evidence.
Use the same interpretation across conditions; do not invent extra requirements while scoring.
The mapping is part of frozen evaluation input, not supplied to the subject.
For this pilot's task families:

| Criterion | Ledger and evidence |
|---|---|
| DR-02 correct date, controlling authority, precise support and no invented facts | Semantic DR-I1–DR-I4; actual source reads, final answer and supplied documents. |
| DR-02 two-line shape, full time/zone, no narration and matching saved note | Task fidelity; distinguish final artifact from conversational messages and directly inspect the note. |
| LP prose rather than implementation/test bodies or unnecessary illustrations | Semantic LP-I1/LP-I3; plan content, not whether the subject executed the proposed work. |
| LP concrete behavioral contract, relevant edges and coherent green change boundary | Semantic LP-I2/LP-I4; supplied task facts and plan. Do not invent missing implementation facts. |
| LP scaffold/headers, specified output form and other rubric presentation requirements | Task fidelity; judge only stated requirements. |
| Exact prose/Markdown/JSON presentation with no authenticated consumer | Deterministic protocol N/A; do not introduce a parser requirement. |

These interpretations guide future freezes; completed worksheets retain their recorded judgments.
The original DR-02 and LP-01 pilot rubrics remain unchanged; new variants freeze their own task-specific mappings rather than inheriting this whole table.
An unavailable declared input is setup failure; an optional lookup of an unsupplied application file is a subject tool result, not automatically infrastructure failure.
A skill not loaded despite being available is an observation to judge, not failed isolation.

Set `PILOT_SCENARIO` to the corresponding repository-relative scenario directory and `RUN_BUNDLE` to its verified retained bundle, then generate once:

```sh
skill-validation/runner/.venv/bin/skilltest worksheet "$PILOT_SCENARIO" "$RUN_BUNDLE" --output "$PILOT_ATTEMPT/worksheet.md"
```

Check the rubric hash; fill all assessment sections and the CLI-version field with its tied capture reference while preserving generated mechanical values.
Use source/trace/file evidence, not the subject's self-reported success.
Inspect the complete response trace, including model-authored progress messages, not just `final.txt`; a compliant final artifact can coexist with a response-level fidelity failure such as prohibited narration.
Use tool calls and outputs as evidence of reads/actions, not as model-authored answer prose; apply each frozen criterion to its stated response or artifact boundary.
Score all judgeable results, including failures, with separate semantic, protocol, fidelity and readability judgments; no pooled effectiveness score.
Update the summary row, retain evidence through owner review, and stop at the agreed handoff.
Routine record: runner bundle + CLI/command evidence + completed worksheet + summary row.

## Failure and recovery

Apply the [failure/drift policy](../../plans/specs/2026-09-06-skilltest-controlled-inputs-design.md#accepted-failure-and-drift-policy):

- Required control, input or CLI provenance missing/drifted: stop; retain affected evidence and qualify the changed boundary before continuing.
- Post-run contamination: retain/explain and exclude from valid comparison evidence, without assigning automatic skill FAIL.
- Understood infrastructure-only failure with no evaluable response: record INFRA_RETRY; move prior captures into a unique retry-evidence directory, update references, capture fresh CLI provenance, then retry only the unchanged approved command, including redirections.
- Evaluable response plus cleanup failure: preserve it and stop for recovery/owner review; no automatic retry.
- Interruption: use the retained bundle's runner.log, not a newest-path guess, to resolve its exact private-runtime path beneath the approved scratch runs directory.

Inspect `rg -n 'private Codex runtime|cleanup' "$RUN_BUNDLE/runner.log"`.
After validating the logged path as this attempt's runtime, check `test ! -e "$PILOT_RUNTIME" && test ! -L "$PILOT_RUNTIME"` without reading credential-bearing contents.
An absent directory alone does not resolve an unknown process outcome or missing cleanup record.
The runner does not retain process-group IDs: if ownership is unknown, retain the runtime and request owner-assisted recovery; never infer ownership from a process name, broadly kill processes, or delete a leftover directory to manufacture cleanup success.
Resolve exact targets and obtain the required approval before manual destructive recovery.
Do not rerun a paid test to manufacture a recovery example; use retained/hypothetical evidence and label its limits.
