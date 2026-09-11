# CW baseline and edit runbook

**Baseline and candidate evidence validity are owner-accepted; further interpretation remains open.**
The [accepted evidence index](../accepted/concise-writing/codex-gpt-5.6-sol-medium/README.md) retains results, frozen revisions and verification for 81 fresh plus 18 reused observations.
Both command batches are exhausted; follow the [current testing plan](../../plans/2026-09-09-dd-skill-testing.md#remaining-work), not the reusable collection instructions below, for the next action.
The [archived CW design](../../plans/completed/specs/2026-09-07-cw-validation-design.md) preserves the completed comparison contract, and the [catalog mapping](cw-catalog.md) owns exact inputs, purpose separation, counts and order.
This is an agent-followed procedure using `skilltest`, not a new program.
Reuse the [routine scoring](README.md#scoring-and-handoff), [recovery policy](README.md#failure-and-recovery) and [qualification reference](qualification/README.md); this page supplies CW-specific inputs and baseline/edit decisions.
The existing `pilot/` location avoids a migration; it does not make future observations repetitions of the completed procedure pilot.

## Routine suite preparation

The [baseline specification](../../plans/specs/2026-09-10-cw-baseline-specification.md) has been reviewed, and the owner authorized preparing the resulting coverage proposal.
The [prospective input map and fixture conditions](cw-catalog.md#prospective-input-map) own the reviewed tasks approved for commit/push; the [reviewed scoring](#prospective-scoring) is approved for commit/push.
The prior coverage approval and retrospective assessments do not establish a completed baseline under that specification.

The following preparation procedure describes the earlier approved suite and its retained observations.
The owner reviewed and approved the six `routine/` prompt/rubric pairs in the [input map](cw-catalog.md#routine-input-map) after commit `6867030`; the other 12 purposes in that earlier suite retained their linked material.
That earlier approval does not authorize a new provider batch or bind the prospective tasks to the historical preparation details below.
Use the primary repository checkout on `main` for preparation.
Do not edit the old comparison prompts, rubrics, configs or accepted packages; changed tasks require new comparison evidence under a new approved batch.

Each new `routine/prompt.md` contains the common task, not condition-specific skill-loading instructions.
Prepare condition prompts in fresh scratch using these exact prefixes, followed by a blank line and the unchanged common task:

- Ordinary effectiveness no-DD: no prefix.
- Ordinary effectiveness current-DD or candidate: the CW prefix below.
- CW-13/14 composition no-DD: the common authoring prefix below.
- CW-13/14 composition current-DD or candidate: the CW prefix, a blank line, then the common authoring prefix.

CW prefix for Codex:

```text
Read {{fixture_dir}}/.agents/skills/concise-writing/SKILL.md completely and follow it as binding guidance for this task.
```

Common authoring prefix for Codex:

```text
Read {{fixture_dir}}/.agents/skills/writing-skills/SKILL.md, {{fixture_dir}}/.agents/skills/writing-skills/testing-skills-with-subagents.md and {{fixture_dir}}/.agents/skills/test-driven-development/SKILL.md completely and follow them for this task. Their canonical skill names are superpowers:writing-skills and superpowers:test-driven-development.
```

For a separately selected Claude batch, substitute `.claude/skills/` for `.agents/skills/` in these prefixes and every declared native skill target; no task or rubric change follows from provider choice.
Loading must follow the supplied skill's applicability rules: CW-17 asks for the detailed response, not a boolean declaration of internal method use.
Keep no-DD/current-DD/candidate tasks and rubrics identical; omit DD files and the CW prefix only in no-DD.
No-DD versus current-DD compares the supplied DD bundle, not CW in isolation: all nine DD bodies are absent in no-DD.
Current-DD versus candidate isolates the CW wording change because every other supplied skill remains identical.
For each ordinary case, use the corresponding ordinary fixture group; CW-20 uses CW-01's group, and CW-17/18 loaded replacements use the ordinary group rather than description inputs.
For composition, use the corresponding CW-13/14 authoring group, keeping all common Superpowers bytes identical between conditions.
Candidate preparation replaces only the CW body with the retained unchanged candidate snapshot; no new skill edit or adoption is implied.
Retained discovery cases keep their hint-free prompts and native-selection criteria, with only a declared provider-native path transformation if needed.

The new task text is embedded in the prompts; no additional task-source files are required.
CW-18 routine permits creating only `fixture/clothing-swap-guide.md`; CW-03/13/14/17/20 routine return prose and remain read-only.
The authoring checkpoint records are synthetic scenario premises, not newly collected evidence or a claim that the subject executed a validation lifecycle.
The subject may read supplied skills, revise the quoted material in its response and state its decision; it cannot deploy, run the quoted command, change a skill or dispatch tests.
Keep rubric/runbook text out of subject prompts and fixtures.

Before proposing a batch, use the existing `load_config`/`prepare_workspace` helpers without launching a provider to inspect each final prompt, declared fixture, allowed output and shared-input equality.
Scratch-only preparation configs may reuse historical provider/model declarations to exercise the helpers; that does not select or approve a new collection schedule.
Select the real batch's provider/model/effort, skill/composition snapshots, counts/order, qualified CLI and necessary control checks explicitly, then freeze its recoverable inputs and show the expanded commands for approval.
The old 99/66-call schedules below are exhausted and do not supply defaults for new calls.
Requalify CW-07 when invocation mechanics or skill/composition wording changes project prerequisites, companion dependencies or mandatory procedures, even if the runner is unchanged.

## Prospective scoring

**Status:** Reviewed scoring approved for commit/push; the collection schedule and commands require separate approval.
Use the exact purpose's rubric in the [input map](cw-catalog.md#prospective-input-map), grounded in the [baseline specification](../../plans/specs/2026-09-10-cw-baseline-specification.md) and its declared source bodies.
Historical rubrics and judgments remain unchanged.

### Worksheet and evidence

Freeze selected rubrics, these rules, the specification and relevant source bodies as withheld evaluator inputs.
Record their recoverable revisions/paths and hashes once in the existing collection summary’s input section; each worksheet links that same input record from methodology notes.
Keep this input record fixed while adding results elsewhere in the summary.
The generator already records the local rubric hash; leave generated identity fields unchanged and keep evaluator inputs out of subject fixtures.

Fill the existing category and purpose fields, including the condition.
Write one semantic result per rubric assessment group, using its bullets as a checklist rather than separately scoring every fact.
A group passes only when all applicable checks pass; a demonstrated violation fails it.
Missing evidence is NOT_JUDGEABLE, not a pass; distinguish an absent source fact in a visible output (a judgeable omission) from an unavailable output.
If a group has both a known violation and missing evidence, retain the violation in its notes and mark the group NOT_JUDGEABLE.
Omit inapplicable conditional groups with a reason; do not average results.
Use existing [verdict precedence](../../plans/completed/specs/2026-09-02-skill-testing-methodology-design.md#scenario-verdict): infrastructure disposition, then `RUN_NOT_JUDGEABLE`, then failure, otherwise pass.

For effectiveness/composition, assess the complete source and final artifact before inspecting condition labels or loading traces where practical; treat this as a reading order, not a claim of blind evaluation.
Then inspect the full trace and actual file/Git state to verify exposure, task boundaries and any process-owned behavior before finalizing results.
Self-reported reads, edits, searches or commits are not execution evidence; a missing file prevents judging its contents.
For explicitly loaded conditions, missing/unproven required body access invalidates that intended condition; retain separately observable task outcomes.
No-DD omits DD loads; CW-22's common writing-plans load still applies.

### Effectiveness and comparison

Assess preservation (CW-I1) and economy (CW-I2) separately; CW-17 also includes its requested explanation under CW-I3.
Preserve source meaning and add no unsupported claims.
Check the whole artifact for its intended reader: original wording, placement or repetition need not survive if information and useful framing do.
Repetition is allowed when it improves clarity, readability or effectiveness for the intended reader, including emphasis, retention, orientation or point-of-use recall without adding a new fact.
No word-count reduction, heading quota or mandatory rewrite applies; an unchanged effective source can pass.
Generation still has an economy obligation, but its length is not compared with raw source notes as though they were a prior draft.

Give a brief, evidence-linked reason for each result, detailing every failure: what meaning changed and what the reader could misunderstand/do differently; what passage is removable without lost value; or what became harder to find or understand.
A preference for a tighter alternative or evaluator uncertainty about padding is not enough to fail.
Record readability in its existing section: improved, equivalent or degraded against the source for revisions; usability for the requested reader for generation.
Materially harder comprehension/use is a preservation failure; cross-reference the readability evidence rather than scoring the same defect twice.
In composition, keep each companion's assessment separate; cross-reference shared defects without counting them as independent failures or claiming full companion validation.

#### Padding-failure check

Before assigning an economy failure for padding, record in the existing worksheet's evidence/notes:

1. The passage and its context for the intended reader.
2. Any plausible reader function, including orientation, transitions, emphasis, retention or point-of-use recall even when it adds no fact, or why none applies.
3. Why that function supplies no useful value in this context, as well as why no information would be lost by cutting it.

“It is removable,” “the headings already say this,” or “it adds no new fact” is insufficient justification on its own.
Ground a claimed framing benefit in the artifact's actual reader and use, rather than inventing a hypothetical benefit.
If a useful function remains plausible and unresolved, note that uncertainty without assigning a padding failure on that basis; this does not excuse another demonstrated defect.
Evaluator uncertainty about value is not missing evidence and does not by itself make the run `RUN_NOT_JUDGEABLE`; nor does it establish that the subject expressed uncertainty under CW-21.

Calibration example: in CW-23's short restart guide, “Use these checks before and after restarting a worker” usefully orients the reader to both stages despite overlap with the title and headings.
Retaining that sentence is not an economy failure.
By contrast, “This section describes the final check” immediately beneath “Final check” is padding when it merely repeats the heading without a useful orienting or other reader function.
These are contextual judgments, not a whitelist of sentences or a blanket exemption for introductions.

#### Comparing conditions

Apply the same outcome criteria to matching no-DD and baseline conditions.
Finish individual judgments before comparing their outputs.
In the existing collection summary, explain whether the supplied skills materially helped, made little difference or hurt on those observations; say when evidence is insufficient or mixed.
CW need not outperform the control for a test to be useful.
Record no observed degradation when direct comparison shows that the CW condition preserves successful task behavior and equivalent or better readability; cite the output features supporting that conclusion.
Two PASS labels alone establish neither equivalence nor added benefit, and an unresolved comparison remains unresolved.
Retain ordinary control passes and cases that check preservation of successful behavior; do not redesign them merely to force a control failure or a CW win.
Describe the actual supplied bundle and observed loads: a bundle comparison does not isolate CW's contribution, and a small sample does not establish reliability.

### Discovery and task boundaries

Discovery scores selection/exposure (CW-I3), not prose effectiveness.
Positive cases require model-initiated access to the complete CW body before final handoff; direct or companion-mediated access and jointly complete chunks count.
With qualified availability and a complete trace, absent/partial access or a claim without access fails; pre-injected bodies or inadequate trace coverage invalidate native-discovery judgment.
For excluded-authoring cases, reading CW to check scope or using it to word the separate selection response is allowed; selecting it as guidance for the excluded edit fails.
A resolved selection excluding CW can pass without naming CW; an unresolved CW selection is NOT_JUDGEABLE.
CW-13/14 do not require a particular alternative skill or score its authoring procedure, validation prerequisites, readiness criteria or deployment decisions, even if volunteered.
Keep task-boundary and evidence-validity checks; authoring-method correctness is outside both their CW and task-fidelity scores.

Record task shape, requested read/diff mechanics and mutation/authority boundaries under fidelity unless the rubric identifies a skill-owned consequence.
Fidelity defects do not erase independently judgeable semantic results, but invalidate a condition when they prevent its intended judgment.
All 18 purposes have protocol N/A; CW-23's actual reconciliation/accounting is semantic, while its exact heading and accounting presentation are fidelity.

#### Output scope

Before freezing a new collection, make output restrictions explicit in the common task received by both conditions.
For ordinary prose revisions, use “In your final answer, return only the revised text”; for file deliverables, explicitly limit the final answer to the requested completion notice.
These constrain the final answer, so a separate progress message alone is not a fidelity violation of that restriction.
If silence throughout the conversation is a material task requirement, say “Do not send progress messages; your only prose response must be the final revised text,” and score all emitted prose against that boundary.
Do not infer conversation-wide silence from an unspecified “return only.”

Update the selected prospective prompt and its input-map/rubric links before freezing; keep historical source prompts and retained packages unchanged.
Record the clarification as changed task input, preserve all other task facts and permissions, and apply it equally to both arms.
These prospective instructions do not reinterpret earlier runs: CW-05's recorded output-only failures, and other historical fidelity judgments, retain their original evaluation contract.

### First collection and scoring check

Start with the [six-purpose subset](cw-catalog.md#initial-pilot-selection) to check scoring usability before extending collection; model, effort, counts and exact commands still need separate approval.
Before scoring that batch, select one effectiveness observation and one composition observation for a second assessment without consulting their first worksheets.
Use the same frozen rules and retained evidence, make no additional provider calls, and retain both assessments separately.
Explain disagreements as an ambiguous rule, missed evidence or unresolved judgment in the collection summary; this small self-check does not establish independent evaluator agreement.
If clarification is needed, document the proposed rule change and its effect, resolve it with the owner before broader collection, and preserve the original rules and judgments.
The [CW-21 rubric](cw-21/specification/rubric.md) records its provisional uncertainty coverage and when to reconsider the task.

## Routine suite assessment

This section records the assessment method used for the latest 18 observations and their authorized retrospective review.
It is not the scoring contract for the proposed specification-based suite; the catalog identifies pending changes, including CW-17's treatment of generated verbosity.

Read the complete case rubric and this section before scoring; freeze both as withheld evaluation inputs.
Fill the worksheet's `Test category / supporting purpose` from the catalog and the rubric, and record the exact case/condition in `Scenario purpose`.
Reuse the existing semantic, protocol, fidelity, readability and infrastructure ledgers; category is metadata, not another score.

- Judge actual returned prose or the independently inspected output file against each case's source facts and criteria, with criterion-level evidence. Apply identical semantic rules to no-DD/current-DD/candidate; a no-DD pass remains a valid result.
- Judge the complete deliverable for its intended reader and use, allowing ordinary comprehension of surrounding text. Preserve actual lookup needs, but do not require each fragment to stand alone. In composition cases, the draft warning/reference is the reader's artifact; the separate deployment decision cannot supply meaning missing from it.
- For each conservation failure, identify the consequential loss of meaning, rationale or correct action in context. A removed heading, cross-reference or example is not itself a failure when its reader function remains. Explicitly requested worked explanations, such as CW-17's examples, remain requirements.
- For padding failures, assess information and framing separately: repetition may add no fact while still providing emphasis, retention, orientation or a useful reminder. A new example, action or context is not required to justify reinforcement. Explain why the repeated wording serves no useful reader function before marking it padding; when that distinction is uncertain, retain it as an observation rather than infer a failure. Overall shortening does not excuse demonstrated padding, but a merely possible stylistic improvement is not a failure.
- Require every applicable semantic criterion for semantic PASS; any judgeable failed criterion is FAIL. Disclose incomplete or ambiguous evidence rather than assuming a pass or inventing missing behavior.
- For composition, report CW revision criteria and writing-skills authority criteria separately. Neither can substitute for the other; a composition-wide result is not solely a CW result.
- Record full requested body reads under task fidelity. Ignored loading does not establish loaded behavior and is not by itself an infrastructure failure. No-DD has no CW-loading requirement; its common authoring loads still apply.
- Assess requested deliverables and mutation boundaries under fidelity. A missing draft/file leaves its semantic behavior unassessed and cannot produce a successful whole-case claim; do not turn an absent artifact into an invented semantic verdict. Assess any independently judgeable decision separately.
- Inspect the complete trace and final inventory. Pre-existing fixture files are protected; only the named CW-18 file can be added in the new cases. No Git mutation, outside-fixture task reads, network tasks or dispatch is permitted.
- Deterministic protocol is N/A. Record readability as improved, equivalent or degraded against the source, citing organization, repetition, findability or processing effort. For CW-17, assess usability of the requested explanation against the supplied notes; this is generation, not compression of a draft.
- Add one CW-I1 semantic criterion for no material degradation of comprehension/use. Use the readability ledger for comparative evidence, not a second scored failure; if an existing conservation row already captures the same reader consequence, reference that row rather than failing twice. Equivalent readability can pass; improvement is not mandatory. Do not require a word count, exact prose, hidden method-use claim or specific heading unless it serves the case's reader-use requirement.
- Follow the [methodology's verdict rules](../../plans/completed/specs/2026-09-02-skill-testing-methodology-design.md#scenario-verdict): a fidelity failure remains visible but does not change a semantic PASS into FAIL unless it prevents judgment.
- Assess padding and preservation together for revisions. No removal target is planted in CW-20, and CW-17's explicit detailed-response case measures requested depth; their CW-I2 removal rows are N/A, not evidence of padding removal.

### Authorized retrospective assessment

On 2026-09-10 the owner authorized rescoring the latest 18 CW-03/13/14/17/18/20 observations under this clarified whole-document contract.
Their revised `routine/` rubrics and this method govern the reassessment; preserve copies of these evaluation inputs alongside the new worksheets.
Keep original collection inputs, rubric snapshots, worksheets, schedule and audit intact; link separate rescored worksheets from the existing summary.
Report criterion changes separately from evaluator corrections under the original rules.
This is retrospective interpretation after inspecting outcomes, not fresh validation under a predeclared contract or grounds for automatic adoption.
The accepted 99/66-run comparison and historical records are outside this authorization; the other 12 routine purposes retain their inputs pending any future input review.

Successful provider-free preparation or a review of these materials establishes input readiness only; skill effectiveness requires separately approved, judgeable observations.
For a first evidence pass on new tasks, one observation per selected condition can reveal scoring or task defects without committing to repetitions of every new input.
Keep these judgeable observations if later unchanged-input repetitions are approved; do not discard or replay them merely to assemble a larger comparison.
One observation cannot establish consistency, and three observations are not a precise reliability estimate; choose additional sampling for the decision it must support, never to replace an unwanted result.

## Completed-comparison procedure

The following schedule and variant-specific instructions document the completed comparison.
Reuse mechanics only after reconciling them with the prospective case's actual boundaries above; do not replay historical commands.

## Test set

Use the [catalog mapping](cw-catalog.md#source-to-variant-map): each condition links its exact prompt, evaluator-only rubric and medium config.
The worksheet scenario is the directory containing that prompt/rubric, not `efforts/medium/`.
Read the complete rubric and linked sources before scoring.
Keep source IDs and variant purposes distinct; a discovery observation cannot stand in for the source's loaded behavior or contract quiz.

The completed schedule is 33 conditions × three repetitions = 99 observations, including 66 current-DD and 33 no-DD.
The [record-by-record checks](cw-catalog.md#counts-order-and-reuse) supported reuse of 18 observations; the 81 new calls are now complete.
Any future exact command list requires new approval before launch; drift requires affected requalification and a revised count, not automatic recollection.
The candidate schedule added 66 observations under its own freeze, qualification/reuse and command approval; those observations are also complete.
No other models/efforts or catalogs are included.
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

The completed collection used `.worktrees/cw-validation-design` on `feature/cw-validation-design`, now retired; new work uses the primary checkout, reflected in the next approved command list.
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
3. Reconcile relevant qualification against the [retained CW/extension evidence](../../plans/completed/2026-09-06-skilltest-sol-low-pilot.md#task-9-qualify-and-exercise-the-cw-purposes). Reuse only demonstrably unchanged controls; a new prose task does not automatically require another paid setup probe. Reconcile the added authoring group, description-only inputs and CW-18's file-creation/retention path explicitly. Missing evidence or changed CLI/catalog/tool controls must be resolved before launch.
4. Record the selected CLI executable and fixed qualified version/digest capture directory, and resolve affected observation reuse. Do not treat an old version pin or a current version command as historical run provenance.
5. After those decisions and any required corrections, commit the reviewed inputs, rubrics, this runbook and linked scoring guidance; record the full recoverable revision in one scratch summary. Require a clean worktree, including no untracked inputs. Subsequent input or guidance changes invalidate that freeze and require affected checks and a new freeze before command approval.
6. Create a fresh scratch root with `mktemp -d /private/tmp/skilltest-cw-baseline.XXXXXX` for baseline collection or `mktemp -d /private/tmp/skilltest-cw-candidate.XXXXXX` for candidate collection, then its `runs/` and `attempts/` directories. Keep preparation evidence separate. Put the frozen revision, qualified-control reference, ordered condition/repetition rows and command list in its `summary.md`.

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
git diff --exit-code "$CW_REVISION" -- skill-validation/pilot skill-validation/runner skill-validation/charter/core-contracts.md skill-validation/scenarios/concise-writing plans/2026-09-09-dd-skill-testing.md plans/completed/specs/2026-09-07-cw-validation-design.md plans/completed/specs/2026-09-06-skilltest-controlled-inputs-design.md plans/completed/specs/2026-09-02-skill-testing-methodology-design.md
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

Fill every assessment, the declared category/supporting purpose, and the provider CLI-version cell with its tied capture reference; preserve generated mechanical fields.
Score the full response trace, including narration, not just final.txt; tool output proves reads/actions, not model-authored prose quality.
Judge prose behavior, transport, composition decisions, description/contract diagnostics, native discovery, fidelity, readability and infrastructure under their separate contracts; deterministic protocol is N/A for this set.
Retain all judgeable results, including FAILs and passing no-DD controls, then update the summary row and continue through the approved batch when required checks pass.
Nonfatal diagnostics are non-blocking only under the linked recovery policy's evidence checks; neither an ERROR label nor exit 0 alone decides validity.

## Use the baseline for an edit

For prospective work, first settle the reviewed specification, catalog coverage and scoring under the [active plan](../../plans/2026-09-09-dd-skill-testing.md#remaining-work).
The steps below retain the earlier comparison mechanics; use only scenarios and conditions agreed for the new edit, rather than automatically including the historical quizzes or fixture groups.

The full-CW baseline and existing rewritten CW comparison have owner-accepted evidence validity; further interpretation and skill decisions remain open.
Testing an existing candidate can compare its frozen bytes, but cannot establish a prior RED-before-authoring chronology.
The unchanged candidate was evaluated under the [existing-candidate comparison contract](../../plans/completed/specs/2026-09-07-cw-validation-design.md#existing-cw-candidate-preparation) and steps 3–6 below; steps 1–2 govern new authoring, not a prerequisite to evaluating that snapshot.
These steps remain a procedure for separately approved future work, not authorization to repeat completed runs.

1. Review the relevant behavior pairs for a targeted, judgeable no-DD failure before authoring. If the control passes, retain that result; select or design a separately approved diagnostic rather than declaring RED, weakening criteria or repeating until failure. A current-DD failure alone is not the required no-DD control.
2. Before new authoring, agree the edit hypothesis, required RED/GREEN repetitions, regression coverage and acceptance rule under `superpowers:writing-skills`. This baseline schedule does not waive that skill's applicable requirements. The original conditional charter schedule is not activated automatically.
3. After owner approval of candidate preparation, freeze current-DD and snapshot the existing candidate or authorized new edit into separately named inputs. For a CW-only change, replace only CW source bytes in body-based configs; for CW-09/11, replace only the CW description with the candidate's exact frontmatter value. Keep native targets, other DD inputs, common Superpowers, task prompt and rubric unchanged. Separate candidate IDs/source paths record the condition; never overwrite frozen current inputs. A new dedicated tool is a separately approved skill-plus-tool change.
4. Agree candidate coverage against the full catalog before collection. Keep discovery separate from behavior and retain relevant regressions; an existing-candidate catalog comparison and a targeted new edit need not have identical scope. Loaded contract/decision diagnostics do not prove executed prose-method application or an authoring lifecycle; do not broaden claims beyond their evidence.
5. Reuse prior no-DD/current observations only when their recoverable inputs, model/effort, actual CLI/version/digest, required qualification, scoring rules and agreed sampling remain comparable. Otherwise propose fresh affected controls; do not stitch mismatched observations into a comparison or automatically rerun the entire historical catalog.
6. Present the complete candidate/control/regression command batch for approval, with its fixed counts/order. Collect and score under the same procedure; any test-contract change needs fresh affected comparison evidence. Report targeted improvement and regressions separately, without pooling discovery into prose effectiveness or attributing a composition-wide result solely to CW.

## Handoff and retention

Keep one summary linking each bundle, CLI/command captures and completed worksheet; criterion detail belongs in worksheets, not duplicate reports.
At handoff, verify records, frozen inputs and changed links, run the repository-required hook suite once and report gaps for owner review.
Rerun offline runner tests when harness code/environment or failed verification invalidates the existing evidence, not after each observation.
Scratch remains scratch until owner acceptance; no replacement of the 105 historical records is authorized.
The accepted CW baseline is stored under `skill-validation/accepted/concise-writing/codex-gpt-5.6-sol-medium/`, with one directory per purpose-separated scenario and all its declared conditions/repetitions.
Its [index](../accepted/concise-writing/codex-gpt-5.6-sol-medium/README.md) records archive restoration checks and preserved provenance; verify the evidence commit before candidate collection or scratch cleanup.
Before packaging, record the exact destination and retained contents in the scratch summary; preserve complete bundles, full traces and permitted outputs, worksheets, tied CLI/command captures and the qualification/provenance needed to interpret them.
Verify preserved bytes and navigation independently of the original scratch paths before committing; retain the source packages until that check succeeds.
When a new accepted set is authorized, retain the complete scenario/provider/model/effort set, including declared conditions, repetitions and failures, under the [whole-set/Git-history policy](../../plans/completed/specs/2026-09-06-skilltest-controlled-inputs-design.md#working-requirements-inventory).
Commit accepted evidence and recoverable provenance before a later whole-set replacement; do not accumulate dated checked-out archives or delete scratch still needed for review.
