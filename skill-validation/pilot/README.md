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
The [Claude adapter](../runner/README.md#claude) supplies the equivalent local workflow using its qualified macOS controls and existing subscription, with `.claude/skills/` fixture targets.
Claude’s [scoped local qualification](qualification/README.md#claude-qualification-checkpoint) passed; the same batch approval, freeze, evidence review and worksheet procedure applies within its recorded limits.
Both adapters produce raw traces and a separate final answer when available; inspect the full trace, not just `final.txt`.

## Bounded batches and approval

Before collection, present every fully expanded command, working directory, frozen input revision, provider/model/effort, count and order as one bounded batch for explicit owner approval.
An approved batch authorizes only those commands and repetitions; judgeable outcomes, including FAILs, do not require another conversational checkpoint before the next approved command.
Changed commands, inputs, model/effort, counts or order require renewed approval; failed controls, drift, compromised required evidence, unexpected execution failures or unresolved cleanup pause the batch under the recovery policy below.
Inspect unexpected diagnostics for those effects; their presence or log severity alone does not pause a completed, judgeable run.
Understood infrastructure-only retries retain the existing exact-unchanged-command rule. Host approval dialogs still apply.
This policy is not approval of a batch; completed pilot commands are historical records, not reusable launch permission.

Treat a bounded collection batch as one verification/commit unit, not each observation as a new implementation unit.
Before collection, require passing offline harness verification for the unchanged code/environment; run the runner suite once when that evidence is absent or invalidated, not after every model response.
At batch handoff, check records, protected inputs and changed documentation, run the repository-required hook suite once, and commit authorized repository changes together.
Rerun relevant tests after code/environment changes or a failure that invalidates prior verification; this cadence does not weaken per-run checks below.
Keep progress in scratch during collection so the worktree remains clean without per-observation status commits.

## Preparation and freeze

The completed pilot used `.worktrees/skilltest-input-isolation-spike` on `spike/skilltest-input-isolation`; that workspace is being retired under the [integration handoff](../../plans/2026-09-06-skilltest-sol-low-pilot.md).
Future collection must use the owner-designated checkout and newly approved absolute command paths; current testing development is on `main` in the primary checkout by owner instruction.
Historical workspace paths below are not launch instructions for a new batch.
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
Supply the task facts needed by the rubric before collection; if runnable verification is required, provide the test framework, command and working directory in the fixture unless selecting them is the explicit test purpose.
For a future LP variant, supply that toolchain context identically in both arms while keeping absent application source explicit; do not require a model to guess a framework or claim it executed unavailable tests.
This is a requirement for future fixture design, not permission to edit or rerun completed pilot inputs.
Declare whether the scenario tests behavior or discovery, following the [separate test-purpose contract](../../plans/specs/2026-09-06-skilltest-controlled-inputs-design.md#accepted-separation-setup-discovery-and-behavior).
Behavior prompts explicitly load the target/composed skills: common Superpowers directives stay the same, while no-DD omits DD directives and files.
Verify requested reads in the trace; retain ignored directives as fidelity failures without claiming loaded-skill behavior or silently excluding the observation.
Only dedicated discovery scenarios omit skill-loading hints and judge spontaneous selection; do not conflate either type with setup qualification.
DR-02 permits only its requested evidence-note write; LP-01 is response-only.
The clarified LP prompts explicitly say application source is not supplied; this post-pilot change applies only to future runs.
To inspect the four completed observations' exact prompts/configs/rubrics, use their recorded revision `e537c03909eb2b4f1986e4170a3f1b662d29a719`, not current source files.
Their retained evidence and judgments are unchanged.

## Execution record

Use one scratch summary with frozen provenance, qualification reference, one row per attempt and the exact approved command list.
Each row records approval/execution status and links its runner bundle, CLI capture and worksheet; include exclusions/retries and unresolved cleanup.
The bundle owns raw/mechanical evidence, the worksheet owns judgments and caveats, the summary owns attempt/approval tracking, and the active plan owns only the project checkpoint and scope.
Link these homes instead of copying verdict explanations or run narratives into the summary and plan; reuse existing commands and logs instead of rebuilding mechanical reports per observation.
Preserve raw evidence; add extra exception notes only when the worksheet/summary cannot explain the recovery safely.
Existing pilot evidence is retained through owner review, not deleted to conform to the simpler future layout.

The completed initial sequence used two qualification calls and four DR-02/LP-01 observations; its exact attempt labels, commands and evidence live in the original scratch summary linked by the active plan.
Every future batch freezes its own counts/order; retain judgeable FAILs and passing controls without increasing effort or adding repetitions to obtain a preferred verdict.

### Behavior extension inputs

These are the six completed extension configs, in their recorded order, not a new approved batch:

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

## CW purpose-separated inputs

These four configs implement three purposes; approval and collection status live in the active plan, not this reusable input table:

| Purpose / condition | Config | Prompt | Evaluator-only rubric |
|---|---|---|---|
| CW-01 loaded behavior / no-DD | [Config](cw-01/no-dd/test.json) | [Prompt](cw-01/no-dd/prompt.md) | [Rubric](cw-01/no-dd/rubric.md) |
| CW-01 loaded behavior / current-DD | [Config](cw-01/current-dd/test.json) | [Prompt](cw-01/current-dd/prompt.md) | [Rubric](cw-01/current-dd/rubric.md) |
| CW-01 native discovery / current-DD | [Config](cw-01/discovery/test.json) | [Prompt](cw-01/discovery/prompt.md) | [Rubric](cw-01/discovery/rubric.md) |
| CW-17 native non-trigger / current-DD | [Config](cw-17/discovery/test.json) | [Prompt](cw-17/discovery/prompt.md) | [Rubric](cw-17/discovery/rubric.md) |

Reuse the extension's frozen nine DD skills and four Superpowers files, with all DD omitted only in the behavioral control; no hooks or additional subject tools.
Task facts remain inline from CW-01 and CW-17, and no evaluator rubric or runbook is a fixture.
The behavior prompts differ only by the current-DD CW read directive; their rubrics are identical.
The positive discovery prompt is byte-identical to the no-DD behavior prompt but runs with the current-DD native fixtures and a separate selection rubric.
Neither discovery prompt names a skill, points at skill paths, pastes descriptions or requests a routing answer.
Current-DD is the discovery condition; no-DD is not a native-discovery failure for unavailable skills.

Discovery means observable model-initiated selection/body access under the declared composition, not independent routing or hidden method use.
The positive needs full CW loading before the answer; the non-trigger needs no observed selection/access on a completed task with complete trace coverage.
Disclose composition-mediated and other skill loads; catalog availability alone is not selection, and missing evidence cannot pass a negative test.
The withheld rubrics define the boundaries; do not use prose quality as a proxy for discovery or apply their expectations to completed historical runs.
CW-17 retains the charter's detailed-response exception despite its absence from the frozen current skill.

All configs specify Codex / gpt-5.6-sol / low for consistency with the current preparation path; no counts, order or commands are approved by these files.
Before collection, obtain prompt/rubric approval, freeze the recoverable revision, and reconcile affected qualification: native catalog/body availability and the trace coverage needed to observe selection or its absence under the same common inputs.
Qualification checks availability and observability, not whether CW chooses the expected route; an observed discovery FAIL is not itself a setup failure.
Do not add a read directive to a discovery prompt to make that qualification pass; explicit-load qualification stays a separate setup check.
Provider-free copying proves prepared bytes only; if the necessary trace/control boundary cannot be established, stop as inconclusive rather than infer hidden behavior.
Use the routine commands below only for an explicitly approved finite batch; completed commands are not reusable launch permission. No extra runner capability or paid qualification call is automatically authorized.

## Per-run commands and checks

From the feature-worktree root, set these path abbreviations from the approved summary row, not a newest-directory guess:
`PILOT_SCRATCH`, `PILOT_ATTEMPT` (a new attempt directory), `PILOT_CONFIG` (absolute config path), `PILOT_INPUT_REVISION` and `PILOT_REFERENCE` (fixed qualified CLI capture directory).
For the recorded pilot, scratch is `/private/tmp/skilltest-sol-low-pilot.Lunoau` and reference is its `preflight/` directory.
Verify that the approved scratch root, its `runs/` directory and the attempt parent directory exist before launch; otherwise stop and prepare those exact scratch paths before using the command.
An absent TMPDIR can redirect temporary allocation outside the intended scratch package; never rely on fallback allocation.
Before a first launch, create the attempt directory once with `mkdir "$PILOT_ATTEMPT"` (no `-p`); a collision means inspect/resume existing evidence, not overwrite it.
For an authorized unchanged-command infrastructure retry, preserve the prior captures under the recovery procedure and reuse the original attempt path; do not repeat directory creation.
Expand all abbreviations in the complete provider command shown for owner approval.
The frozen-input diff must cover every declared source and evaluator mapping, including linked guidance outside `pilot/`; extend the path list below for the selected batch.

Run each prelaunch check separately, require exit 0, and require Git status output to be empty:

```sh
git status --short
git diff --exit-code "$PILOT_INPUT_REVISION" -- skill-validation/pilot skill-validation/runner plans/specs/2026-09-06-skilltest-controlled-inputs-design.md
test -d "$PILOT_SCRATCH/runs" && test -d "$(dirname "$PILOT_ATTEMPT")"
test -d "$PILOT_ATTEMPT"
/opt/homebrew/bin/codex --version > "$PILOT_ATTEMPT/cli-version.txt" 2> "$PILOT_ATTEMPT/version-stderr.txt"
/usr/bin/shasum -a 256 /opt/homebrew/bin/codex > "$PILOT_ATTEMPT/cli-sha256.txt"
test -s "$PILOT_REFERENCE/cli-version.txt" && test -s "$PILOT_REFERENCE/cli-sha256.txt"
cmp "$PILOT_REFERENCE/cli-version.txt" "$PILOT_ATTEMPT/cli-version.txt"
cmp "$PILOT_REFERENCE/cli-sha256.txt" "$PILOT_ATTEMPT/cli-sha256.txt"
```

Inspect version-command stderr before launch; exit 0 is not evidence of empty stderr.
Inspect warnings against the required controls and retain the capture; unusable provenance or an unproved required control stops launch, not an unfamiliar message alone.
Never silence warnings or refresh references to hide drift; capture version/digest immediately before every invocation, including retries.
After the batch's explicit approval covers its fully expanded form, execute the row's one-run command:

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

Before collecting a new scenario or rubric revision, freeze a short evaluator-only table with one row per criterion: criterion/rubric reference, owning invariant and ledger, required observable evidence, and pass/fail boundary.
Prefer the existing rubric's location so its hash covers the mapping; a linked runbook section must also be frozen and included in the prelaunch diff. Do not add a scoring schema or duplicate the table in every worksheet.
Distinguish identifying a defect, explicitly accounting for each caller, and avoiding unsupported extra findings; include each only when that is a declared test obligation.
Specify whether evidence is an action in the trace, model-authored response, or saved artifact; a file appearing in tool output does not itself prove the response explains its contents.
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
Update the summary row and continue to the next approved command only after its required checks pass; stop for owner review at the batch boundary or a recovery gate.
Routine record: runner bundle + CLI/command evidence + completed worksheet + summary row.

## Failure and recovery

Apply the [failure/drift policy](../../plans/specs/2026-09-06-skilltest-controlled-inputs-design.md#accepted-failure-and-drift-policy):

- Nonfatal CLI diagnostics: retain stderr and note the diagnostic, supporting checks and uncertainty in the worksheet. Continue the approved batch without retry or renewed approval when runner/provider completion succeeds, the response is judgeable, required input/provenance/trace/cleanup checks pass, and there is no evidence of changed model/effort, contamination or compromised controls. A log labeled ERROR is not by itself a failed run; exit 0 alone is not sufficient either.
- Unexpected execution failure: retain evidence and stop to investigate; do not retry until it meets the understood infrastructure-only rule below.
- Required control, input or CLI provenance missing/drifted: stop; retain affected evidence and qualify the changed boundary before continuing.
- Post-run contamination: retain/explain and exclude from valid comparison evidence, without assigning automatic skill FAIL.
- Understood infrastructure-only failure with no evaluable response: record INFRA_RETRY; preserve all prior command/CLI captures in a unique retry-evidence directory and update their summary links before reusing the original attempt path. Verify the move succeeded and capture destinations are absent, then repeat all prelaunch checks and retry only the unchanged approved command, including redirections. Retain the prior bundle and a separate row for each attempt.
- Evaluable response plus cleanup failure: preserve it and stop for recovery/owner review; no automatic retry.
- Interruption: use the retained bundle's runner.log, not a newest-path guess, to resolve its exact private-runtime path beneath the approved scratch runs directory.

Inspect `rg -n 'private Codex runtime|cleanup' "$RUN_BUNDLE/runner.log"`.
After validating the logged path as this attempt's runtime, check `test ! -e "$PILOT_RUNTIME" && test ! -L "$PILOT_RUNTIME"` without reading credential-bearing contents.
An absent directory alone does not resolve an unknown process outcome or missing cleanup record.
The runner does not retain process-group IDs: if ownership is unknown, retain the runtime and request owner-assisted recovery; never infer ownership from a process name, broadly kill processes, or delete a leftover directory to manufacture cleanup success.
Resolve exact targets and obtain the required approval before manual destructive recovery.
Do not rerun a paid test to manufacture a recovery example; use retained/hypothetical evidence and label its limits.
