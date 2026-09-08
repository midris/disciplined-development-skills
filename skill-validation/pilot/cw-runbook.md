# CW baseline and edit runbook

**The owner approved the full-CW catalog mapping, and qualification/reuse checks pass; clean input freeze and provider-command approval remain pending.**
The earlier 18 medium observations are collected and scored, pending owner acceptance; their command approvals are exhausted.
The [CW design](../../plans/specs/2026-09-07-cw-validation-design.md) owns scope and checkpoints, and the [catalog mapping](cw-catalog.md) owns exact inputs, purpose separation, counts and order.
This is an agent-followed procedure using `skilltest`, not a new program.
Reuse the [routine scoring](README.md#scoring-and-handoff), [recovery policy](README.md#failure-and-recovery) and [qualification reference](qualification/README.md); this page supplies CW-specific inputs and baseline/edit decisions.
The existing `pilot/` location avoids a migration; it does not make future observations repetitions of the completed procedure pilot.

## Test set

Use the [catalog mapping](cw-catalog.md#source-to-variant-map): each condition links its exact prompt, evaluator-only rubric and medium config.
The worksheet scenario is the directory containing that prompt/rubric, not `efforts/medium/`.
Read the complete rubric and linked sources before scoring.
Keep source IDs and variant purposes distinct; a discovery observation cannot stand in for the source's loaded behavior or contract quiz.

The proposed schedule is 33 conditions × three repetitions = 99 observations, including 66 current-DD and 33 no-DD.
The [record-by-record checks](cw-catalog.md#counts-order-and-reuse) support reuse of 18 completed observations, leaving 81 new calls.
The exact command list requires approval before launch; drift requires affected requalification and a revised count, not automatic recollection.
No other models/efforts, other catalogs or candidate evaluation are included.
Run serially in the map's fixed order, skipping only explicitly recorded reused observations.
Use fresh runtimes and distinct attempt directories; do not add repetitions to improve verdicts.
Any required live qualification is separately approved and reported, never counted as effectiveness.
Understood infrastructure-only retries retain the routine unchanged-command policy.

Report each purpose/condition separately with criterion judgments, PASS/FAIL/INCONCLUSIVE counts, evaluable denominator and fidelity/readability/validity caveats.
Retain all judgeable FAILs and passing no-DD controls.
Three runs expose some variation, not a precise reliability estimate, automatic GREEN or deployment acceptance.
Disclose fixed-order and noncontemporaneous-reuse limits.
Historical low/high procedure observations are not medium baseline repetitions.

## Fixture setup and freeze

Work from the root of `.worktrees/cw-validation-design` on `feature/cw-validation-design`; any future workspace change must be reflected in the next approved command list.
Use the existing runner environment; if absent, run `uv sync --frozen` from `skill-validation/runner/`, then return to the worktree root.
Dependency or harness changes require relevant offline verification before collection.

The configs are the exact file/target inventory; the [mapping](cw-catalog.md#fixture-groups-and-evidence-boundaries) defines ordinary, authoring and description-only groups.
Do not add authoring dependencies to ordinary cases: that would change the surrounding inputs of the completed observations.
Within each behavior pair, common Superpowers/task files stay identical and no-DD omits all DD bodies/directives.
Description diagnostics expose the declared description texts, not the nine DD bodies.
No-DD is N/A for these inspected-contract/description tasks and unavailable-target discovery.

All tests are read-only except CW-18 discovery, which may create only `fixture/clothing-swap-guide.md`.
All pre-existing fixture files remain protected; operational shell commands quoted in source prose are never executable tasks.
No Git mutation, outside-fixture inspection, network task calls or dispatch is permitted.
Do not supply rubrics, runbooks, charter text, accepted answers, credentials or evaluator guidance as fixtures.
The runner owns private HOME/CODEX_HOME/TMPDIR, fixture copying, Git boundary, authentication preflight and cleanup; do not provision a second runtime around it.

Before collection:

1. Audit each config with the existing `load_config` and `prepare_workspace` helpers in disposable scratch, without invoking a provider; inspect rendered prompts and compare every prepared file to its declared source. These internal helpers are the existing provider-free preparation path, not a new public CLI. Check for symlinked sources/ancestors and undeclared files too.
2. Verify behavior-pair task/rubric equality, with only the current-DD CW-loading prefix and DD files differing; authoring pairs retain identical common loading directives. Verify discovery prompts have no loading hints and description diagnostics cannot be mistaken for native-discovery tests. Confirm all requested body paths resolve inside their prepared fixture.
3. Commit the reviewed inputs, rubrics, this runbook and linked scoring guidance; record the full recoverable revision in one scratch summary. Require a clean worktree, including no untracked inputs.
4. Reconcile relevant qualification against the [retained CW/extension evidence](../../plans/2026-09-06-skilltest-sol-low-pilot.md#task-9-qualify-and-exercise-the-cw-purposes). Reuse only demonstrably unchanged controls; a new prose task does not automatically require another paid setup probe. Reconcile the added authoring group, description-only inputs and CW-18's file-creation/retention path explicitly. Missing evidence or changed CLI/catalog/tool controls must be resolved before launch.
5. Record the selected CLI executable and fixed qualified version/digest capture directory. Do not treat an old version pin or a current version command as historical run provenance.
6. Create a fresh scratch root with `mktemp -d /private/tmp/skilltest-cw-baseline.XXXXXX`, then its `runs/` and `attempts/` directories. Put the frozen revision, qualified-control reference, ordered condition/repetition rows and command list in its `summary.md`.

Scratch paths and the frozen revision are allocated at freeze time, not guessed here.
Present all fully expanded commands, cwd, provider/model/effort, counts and order for explicit owner approval before any model call.
Historical command approvals do not transfer to this runbook.

## Execute one approved row

From the frozen worktree root, set `CW_ROOT` to that absolute root and `CW_SCRATCH`, `CW_ATTEMPT`, `CW_REFERENCE`, `CW_REVISION` to the exact approved summary values.
Set `CW_SCENARIO` to the repository-relative directory containing the mapping's linked prompt/rubric, and `CW_CONFIG` to its linked medium config's absolute path.
The medium config directory is not the worksheet scenario directory; use the mapped shared rubric rather than looking for a rubric under `efforts/`.
`CW_REFERENCE` is the fixed qualified CLI capture directory, not the new attempt directory.
For a first attempt, create `CW_ATTEMPT` once with `mkdir` without `-p`; a collision requires inspection, never overwrite.
Require the scratch `runs/` directory and attempt parents to exist.
On an approved infrastructure retry, preserve captures and reuse the original command paths as specified by the recovery policy.

Run these checks individually and stop on nonzero exit; Git status must also be empty:

```sh
git status --short
git diff --exit-code "$CW_REVISION" -- skill-validation/pilot skill-validation/runner skill-validation/charter/core-contracts.md skill-validation/scenarios/concise-writing plans/specs/2026-09-07-cw-validation-design.md plans/specs/2026-09-06-skilltest-controlled-inputs-design.md plans/completed/specs/2026-09-02-skill-testing-methodology-design.md
test -d "$CW_SCRATCH/runs" && test -d "$CW_ATTEMPT"
/opt/homebrew/bin/codex --version > "$CW_ATTEMPT/cli-version.txt" 2> "$CW_ATTEMPT/version-stderr.txt"
/usr/bin/shasum -a 256 /opt/homebrew/bin/codex > "$CW_ATTEMPT/cli-sha256.txt"
test -s "$CW_REFERENCE/cli-version.txt" && test -s "$CW_REFERENCE/cli-sha256.txt"
cmp "$CW_REFERENCE/cli-version.txt" "$CW_ATTEMPT/cli-version.txt"
cmp "$CW_REFERENCE/cli-sha256.txt" "$CW_ATTEMPT/cli-sha256.txt"
```

Inspect version stderr and confirm the config still specifies the approved provider/model/effort.
These command shapes assume the qualified executable remains `/opt/homebrew/bin/codex`; a different executable needs corresponding provenance, qualification and newly approved launch paths.
The frozen diff must include any newly linked evaluator guidance or candidate fixture sources outside the listed paths.
Launch only after approval of this command's fully expanded form, using required host permission while retaining the subject's workspace-write sandbox:

```sh
/usr/bin/env TMPDIR="$CW_SCRATCH/runs" PATH=/opt/homebrew/bin:/usr/bin:/bin:/usr/sbin:/sbin "$CW_ROOT/skill-validation/runner/.venv/bin/skilltest" run "$CW_CONFIG" > "$CW_ATTEMPT/command-stdout.txt" 2> "$CW_ATTEMPT/command-stderr.txt"
```

Record exit status and stdout's exact bundle path as `RUN_BUNDLE`; never select the newest directory by timestamp.
Apply the linked recovery policy if execution or required controls fail.
Inspect result.json, runner.log, stdout/stderr, the entire model response trace, final.txt and final fixture/evidence inventories.
Verify exact invocation, prelaunch hashes against frozen inputs, protected-file preservation, body-loading evidence and recorded owned-process/runtime cleanup.
For CW-18 discovery, independently read the retained fixture/clothing-swap-guide.md and require it to be the only added task file; no existing input may change.
Do not apply the read-only variants' no-new-file check to that permitted output or accept a completion notice without the artifact.
Check that the exact logged runtime path is absent without reading its credential-bearing contents; missing ownership/cleanup evidence is unresolved, not a successful cleanup claim.
Only then render the worksheet from the matching frozen rubric:

```sh
"$CW_ROOT/skill-validation/runner/.venv/bin/skilltest" worksheet "$CW_SCENARIO" "$RUN_BUNDLE" --output "$CW_ATTEMPT/worksheet.md"
```

Fill every assessment and the provider CLI-version cell with its tied capture reference; preserve generated mechanical fields.
Score the full response trace, including narration, not just final.txt; tool output proves reads/actions, not model-authored prose quality.
Judge prose behavior, transport, composition decisions, description/contract diagnostics, native discovery, fidelity, readability and infrastructure under their separate contracts; deterministic protocol is N/A for this set.
Retain all judgeable results, including FAILs and passing no-DD controls, then update the summary row and continue through the approved batch when required checks pass.
Nonfatal diagnostics are non-blocking only under the linked recovery policy's evidence checks; neither an ERROR label nor exit 0 alone decides validity.

## Use the baseline for an edit

Finish the full-CW baseline and owner review before evaluating the existing rewrite or authoring an edit.
Testing an existing candidate can compare its frozen bytes, but cannot establish a prior RED-before-authoring chronology.

1. Review the relevant behavior pairs for a targeted, judgeable no-DD failure before authoring. If the control passes, retain that result; select or design a separately approved diagnostic rather than declaring RED, weakening criteria or repeating until failure. A current-DD failure alone is not the required no-DD control.
2. Agree the edit hypothesis, required RED/GREEN repetitions, regression coverage and acceptance rule under `superpowers:writing-skills` before authoring or collecting candidate evidence. This baseline schedule does not waive that skill's applicable requirements. The original conditional charter schedule is not activated automatically.
3. After owner approval of candidate preparation, freeze current-DD and snapshot the existing candidate or authorized new edit into separately named inputs. For a CW-only change, replace only CW source bytes in body-based configs; for CW-09/11, replace only the CW description with the candidate's exact frontmatter value. Keep native targets, other DD inputs, common Superpowers, task prompt and rubric unchanged. Separate candidate IDs/source paths record the condition; never overwrite frozen current inputs. A new dedicated tool is a separately approved skill-plus-tool change.
4. Agree candidate coverage against the full catalog before collection. Keep discovery separate from behavior and retain relevant regressions; an existing-candidate catalog comparison and a targeted new edit need not have identical scope. Loaded contract/decision diagnostics do not prove executed prose-method application or an authoring lifecycle; do not broaden claims beyond their evidence.
5. Reuse prior no-DD/current observations only when their recoverable inputs, model/effort, actual CLI/version/digest, required qualification, scoring rules and agreed sampling remain comparable. Otherwise propose fresh affected controls; do not stitch mismatched observations into a comparison or automatically rerun the entire historical catalog.
6. Present the complete candidate/control/regression command batch for approval, with its fixed counts/order. Collect and score under the same procedure; any test-contract change needs fresh affected comparison evidence. Report targeted improvement and regressions separately, without pooling discovery into prose effectiveness or attributing a composition-wide result solely to CW.

## Handoff and retention

Keep one summary linking each bundle, CLI/command captures and completed worksheet; criterion detail belongs in worksheets, not duplicate reports.
At handoff, verify records, frozen inputs and changed links, run the repository-required hook suite once and report gaps for owner review.
Rerun offline runner tests when harness code/environment or failed verification invalidates the existing evidence, not after each observation.
Scratch remains scratch until owner acceptance; this runbook does not choose a new accepted-results directory or authorize replacing any of the 105 historical records.
When a new accepted set is authorized, retain the complete scenario/provider/model/effort set, including declared conditions, repetitions and failures, under the [whole-set/Git-history policy](../../plans/specs/2026-09-06-skilltest-controlled-inputs-design.md#working-requirements-inventory).
Commit accepted evidence and recoverable provenance before a later whole-set replacement; do not accumulate dated checked-out archives or delete scratch still needed for review.
