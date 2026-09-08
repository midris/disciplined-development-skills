# CW baseline and edit runbook

**Portfolio and 54-run schedule approved; exact provider commands await approval.**
The [CW design](../../plans/specs/2026-09-07-cw-validation-design.md) owns this increment's scope and checkpoint.
This is an agent-followed procedure using `skilltest`, not a new program.
Reuse the [routine scoring](README.md#scoring-and-handoff), [recovery policy](README.md#failure-and-recovery) and [qualification reference](qualification/README.md); this page supplies CW-specific inputs and baseline/edit decisions.
The existing `pilot/` location avoids a migration; it does not make future observations repetitions of the completed procedure pilot.

## Test set

The low-effort scenario directories contain the shared prompts and evaluator-only rubrics.
Medium/high configs reference those same prompt and fixture sources; they do not duplicate or modify the task or scoring inputs.
Read them, the [charter](../charter/core-contracts.md#concise-writing) and any rubric-linked source before proposing collection.

| Row | Purpose / condition | Low config | Medium config | High config | Worksheet scenario beneath pilot/ |
|---|---|---|---|---|---|
| 1 | CW-08 policy rewrite / no-DD | [Low](cw-08/no-dd/test.json) | [Medium](efforts/medium/cw08-no-dd.json) | [High](efforts/high/cw08-no-dd.json) | `cw-08/no-dd` |
| 2 | CW-08 policy rewrite / current-DD | [Low](cw-08/current-dd/test.json) | [Medium](efforts/medium/cw08-current-dd.json) | [High](efforts/high/cw08-current-dd.json) | `cw-08/current-dd` |
| 3 | CW-19 complex conservation / no-DD | [Low](cw-19/no-dd/test.json) | [Medium](efforts/medium/cw19-no-dd.json) | [High](efforts/high/cw19-no-dd.json) | `cw-19/no-dd` |
| 4 | CW-19 complex conservation / current-DD | [Low](cw-19/current-dd/test.json) | [Medium](efforts/medium/cw19-current-dd.json) | [High](efforts/high/cw19-current-dd.json) | `cw-19/current-dd` |
| 5 | CW-01 positive native discovery / current-DD | [Low](cw-01/discovery/test.json) | [Medium](efforts/medium/cw01-discovery.json) | [High](efforts/high/cw01-discovery.json) | `cw-01/discovery` |
| 6 | CW-17 native non-trigger / current-DD | [Low](cw-17/discovery/test.json) | [Medium](efforts/medium/cw17-discovery.json) | [High](efforts/high/cw17-discovery.json) | `cw-17/discovery` |

**Approved schedule:** Codex / gpt-5.6-sol at low, medium and high, three repetitions of each row at each effort: 18 runs per effort, 54 total (36 behavior, 18 discovery).
Execute serially: low, then medium, then high; within each effort, repetitions 1–3 each visit rows 1–6 in order.
This fixed order is simple to audit, not randomized or fully counterbalanced; retain timestamps and harness provenance rather than attributing any observed difference solely to effort.
Use fresh runtimes for every repetition and distinct attempt directories; no parallel subject runs or adaptive stopping on skill verdicts.
No extra qualification model call or retry is included in the count; only understood infrastructure-only retries follow the linked unchanged-command policy.
No Terra, Claude, remaining-CW collection or candidate skill edit is included.
Report PASS/FAIL/INCONCLUSIVE counts and the evaluable denominator for each scenario/condition/effort, with criterion-level judgments and separate fidelity/readability/validity caveats.
Disclose excluded infrastructure/contamination attempts separately; never discard judgeable FAILs or pool discovery into behavior.
Three repetitions provide an initial view of variation, not a precise reliability estimate or automatic GREEN/acceptance threshold; owner review decides baseline acceptance, and later authoring criteria/repetitions require separate agreement.
Do not use old pilot observations as fresh baseline repetitions or rerun CW-01 behavior routinely.

## Fixture setup and freeze

Work from the root of `.worktrees/cw-validation-design` on `feature/cw-validation-design`; any future workspace change must be reflected in the next approved command list.
Use the existing runner environment; if absent, run `uv sync --frozen` from `skill-validation/runner/`, then return to the worktree root.
Dependency or harness changes require relevant offline verification before collection.

The configs are the exact fixture inventory: four common Superpowers 6.3.0 files at native `.agents/skills/` targets; current-DD adds the nine frozen DD bodies from `inputs/dd/`.
No-DD supplies none of those DD bodies.
Keep their existing source bytes, target names and supporting files fixed across the selected configs; the [input provenance](README.md#behavior-extension-inputs) records their origin.
No new task files are needed: the prose is inline, and CW-19's shell commands are text to preserve, not commands to execute.
All six tasks prohibit file edits, Git changes, outside-fixture inspection, network and dispatch.
Do not supply rubrics, runbooks, charter text, accepted answers, credentials or other evaluator guidance as fixtures.
The runner owns private HOME/CODEX_HOME/TMPDIR, native fixture copying, the Git boundary, authentication preflight and cleanup; do not provision a second runtime around it.

Before collection:

1. Audit each config with the existing `load_config` and `prepare_workspace` helpers in disposable scratch, without invoking a provider; inspect rendered prompts and compare every prepared file to its declared source. These internal helpers are the existing provider-free preparation path, not a new public CLI. Check for symlinked sources/ancestors and undeclared files too.
2. Verify behavior-pair task/rubric equality, with only the current-DD CW-loading prefix and DD files differing; verify discovery prompts have no loading hints. Confirm all requested body paths resolve inside their prepared fixture.
3. Commit the reviewed inputs, rubrics, this runbook and linked scoring guidance; record the full recoverable revision in one scratch summary. Require a clean worktree, including no untracked inputs.
4. Reconcile relevant qualification against the [retained CW/extension evidence](../../plans/2026-09-06-skilltest-sol-low-pilot.md#task-9-qualify-and-exercise-the-cw-purposes). Reuse only demonstrably unchanged controls; a new prose task does not automatically require another paid setup probe. Missing evidence or changed CLI/catalog/tool controls must be resolved before launch.
5. Record the selected CLI executable and fixed qualified version/digest capture directory. Do not treat an old version pin or a current version command as historical run provenance.
6. Create a fresh scratch root with `mktemp -d /private/tmp/skilltest-cw-baseline.XXXXXX`, then its `runs/` and `attempts/` directories. Put the frozen revision, qualified-control reference, ordered condition/repetition rows and command list in its `summary.md`.

Scratch paths and the frozen revision are allocated at freeze time, not guessed here.
Present all fully expanded commands, cwd, provider/model/effort, counts and order for explicit owner approval before any model call.
Historical command approvals do not transfer to this runbook.

## Execute one approved row

From the frozen worktree root, set `CW_ROOT` to that absolute root and `CW_SCRATCH`, `CW_ATTEMPT`, `CW_REFERENCE`, `CW_REVISION` to the exact approved summary values.
Set `CW_SCENARIO` to `skill-validation/pilot/` plus the table's worksheet-scenario path, and `CW_CONFIG` to the selected effort config's absolute path.
For medium/high, the config directory is not the worksheet scenario directory; use the mapped shared rubric rather than looking for a rubric under `efforts/`.
`CW_REFERENCE` is the fixed qualified CLI capture directory, not the new attempt directory.
For a first attempt, create `CW_ATTEMPT` once with `mkdir` without `-p`; a collision requires inspection, never overwrite.
Require the scratch `runs/` directory and attempt parents to exist.
On an approved infrastructure retry, preserve captures and reuse the original command paths as specified by the recovery policy.

Run these checks individually and stop on nonzero exit; Git status must also be empty:

```sh
git status --short
git diff --exit-code "$CW_REVISION" -- skill-validation/pilot skill-validation/runner skill-validation/charter/core-contracts.md skill-validation/scenarios/concise-writing/cw-08 skill-validation/scenarios/concise-writing/cw-19 plans/specs/2026-09-07-cw-validation-design.md plans/specs/2026-09-06-skilltest-controlled-inputs-design.md plans/completed/specs/2026-09-02-skill-testing-methodology-design.md
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
Check that the exact logged runtime path is absent without reading its credential-bearing contents; missing ownership/cleanup evidence is unresolved, not a successful cleanup claim.
Only then render the worksheet from the matching frozen rubric:

```sh
"$CW_ROOT/skill-validation/runner/.venv/bin/skilltest" worksheet "$CW_SCENARIO" "$RUN_BUNDLE" --output "$CW_ATTEMPT/worksheet.md"
```

Fill every assessment and the provider CLI-version cell with its tied capture reference; preserve generated mechanical fields.
Score the full response trace, including narration, not just final.txt; tool output proves reads/actions, not model-authored prose quality.
Judge behavior, discovery, fidelity, readability and infrastructure under their separate contracts; deterministic protocol is N/A for this set.
Retain all judgeable results, including FAILs and passing no-DD controls, then update the summary row and continue through the approved batch when required checks pass.
Nonfatal diagnostics are non-blocking only under the linked recovery policy's evidence checks; neither an ERROR label nor exit 0 alone decides validity.

## Use the baseline for an edit

1. Review both behavior pairs for a targeted, judgeable no-DD failure before authoring. If the control passes, retain that result; select or design a separately approved diagnostic rather than declaring RED, weakening criteria or repeating until failure. A current-DD failure alone is not the required no-DD control.
2. Agree the edit hypothesis, required RED/GREEN repetitions, regression coverage and acceptance rule under `superpowers:writing-skills` before authoring or collecting candidate evidence. This baseline schedule does not waive that skill's applicable requirements. The original conditional charter schedule is not activated automatically.
3. Freeze current-DD; prepare candidate copies in separately named directories after authoring is authorized. For a CW-only edit, replace only the CW source bytes in candidate configs, keeping its native target, the other eight DD bodies, common Superpowers, task prompt and rubric unchanged. Separate candidate IDs/source paths record the condition; do not overwrite frozen current inputs. A new dedicated tool is a separately approved skill-plus-tool change.
4. Default regression coverage is both loaded-behavior tasks plus both discovery tasks for the candidate. A behavior-only edit can still change native selection, so do not silently drop discovery. This portfolio cannot support claims about the deferred detailed-response application, durable-file or authoring-composition boundaries; add the necessary focused tests before editing those contracts.
5. Reuse prior no-DD/current observations only when their recoverable inputs, model/effort, actual CLI/version/digest, required qualification, scoring rules and agreed sampling remain comparable. Otherwise propose fresh affected controls; do not stitch mismatched observations into a comparison or automatically rerun the entire historical catalog.
6. Present the complete candidate/control/regression command batch for approval, with its fixed counts/order. Collect and score under the same procedure; any test-contract change needs fresh affected comparison evidence. Report targeted improvement and regressions separately, without pooling discovery into prose effectiveness or attributing a composition-wide result solely to CW.

## Handoff and retention

Keep one summary linking each bundle, CLI/command captures and completed worksheet; criterion detail belongs in worksheets, not duplicate reports.
At handoff, verify records, frozen inputs and changed links, run the repository-required hook suite once and report gaps for owner review.
Rerun offline runner tests when harness code/environment or failed verification invalidates the existing evidence, not after each observation.
Scratch remains scratch until owner acceptance; this runbook does not choose a new accepted-results directory or authorize replacing any of the 105 historical records.
When a new accepted set is authorized, retain the complete scenario/provider/model/effort set, including declared conditions, repetitions and failures, under the [whole-set/Git-history policy](../../plans/specs/2026-09-06-skilltest-controlled-inputs-design.md#working-requirements-inventory).
Commit accepted evidence and recoverable provenance before a later whole-set replacement; do not accumulate dated checked-out archives or delete scratch still needed for review.
