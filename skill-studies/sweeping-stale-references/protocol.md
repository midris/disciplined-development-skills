# Sweeping stale references: study protocol

Format version: `1`
Study ID: `sweeping-stale-references`
Status: contract and version-1 formats accepted; unrun input layouts migrated; semantic-delivery-01 collected and assessed; wider baseline incomplete; core-baseline-01 is paused for unresolved setup evidence.
The [plan](../../plans/2026-09-11-model-driven-skill-testing.md) owns progress; the [spec](../../plans/specs/2026-09-11-model-driven-skill-testing-framework.md) owns the workflow.
Seven subject executions completed mechanically: four historical development executions, semantic-delivery-01’s two baseline executions and core-baseline-01’s first attempt. The latter has unresolved setup evidence; the wider baseline and any skill rewrite remain incomplete. Eleven approved core-baseline-01 calls remain unattempted, with dispatch paused under its stop rule.

## Sources and intended use

The original is [sweeping-stale-references](../../skills/sweeping-stale-references/SKILL.md) at repository revision `53a06ff4e2fcefb3c7706565bebe07d88e2782ea`, SHA-256 `d6812c33cae026807bbb3ebe851d93b60b513dd87ea5efd98aea28f5c02f9157`.
Original-condition runs load the [frozen study snapshot](cases/skill-original/SKILL.md), not the live skill path. Preserve these bytes for contemporaneous original-versus-candidate comparisons; candidate edits must not replace this snapshot.
[sources.json](sources.json) records inspected file paths, sizes and hashes, including all nine DD skills, installed authoring guidance and runner implementation.
This inventory identifies the initial preparation sources at the recorded revision, including the runner before its permission extension; it is not the frozen manifest of inputs supplied to subjects.
The owner directed simplifying the reusable manifest: derive prompt/fixture mappings from configurations, pin shared source files once and use Git for history. Prepared unrun manifests use version 1 and pin source commits containing their identified bytes. Historical observed inputs retain their recorded identities.
The [permission qualification index](permissions-qualification.json) identifies the updated runner sources.

The skill combines a search-and-reconciliation technique with discipline against stopping after one cited defect.
Its intended user is a development agent changing a fact shared across project files or responding to a reviewer who found one stale reference.
The skill has its own trigger and procedure; it does not require DD or a named Superpowers base to perform a sweep.
DD invokes it at Gate 4, but that incoming invocation is not a dependency of the skill.
The [purpose and relationship map](../../ARCHITECTURE.md#composition-boundaries) records this distinction across all nine skills.
The first study measures independent application to a change and reconciliation commit; native discovery and DD orchestration are outside its claim.
[Disciplined research](../../skills/disciplined-research/SKILL.md) owns grounding the changed fact; [writing explicit rationale](../../skills/writing-explicit-rationale/SKILL.md) owns why it changed.
These ownership boundaries do not require loading either sibling into the subject context.
The task must supply a settled change and sufficient project context, rather than score this skill for inventing the desired change or resolving an unspecified business rule.


## Behavioral contract and consumers

Owner clarification, 2026-09-12: the intended outcome includes preventing documentation drift when project structure or code facts change.
When a file moves, find references to its old path and reconcile affected links, commands and other current consumers to the new location, resolving relative paths from each consumer.
When a code fact changes, find and update documentation describing that fact even when it uses different words rather than the changed identifier; search terms locate candidates, and the meaning of each reference determines the change.
The current text explicitly covers changed documented behavior, literal strings and synonyms, and doc/comment citations.
Applying that procedure to moved paths and semantically equivalent descriptions of code facts is a supported interpretation, reinforced by the owner's intended use; relative-path resolution is not an explicit instruction in the current skill.
Record those criteria as owner-clarified outcomes, not a quotation or proof that the original explicitly taught every technique needed to achieve them.
Assess those outcomes across both conditions, separately from compliance with the original's explicit procedure; a miss does not by itself establish disobedience to an explicit instruction.
Historical references and unrelated matches still receive the stated triage, rather than blanket replacement.
The broad purpose, independent evaluation direction, outcome/procedure distinction and outer limits are settled.

Judge the completed reconciliation, search evidence and commit record together.
Explicit procedural obligations remain observable requirements; an attractive final file state does not prove that the prescribed search or accounting occurred.

| ID | Obligation and source | Intended effect | Observable evidence |
|---|---|---|---|
| O1 | **Explicit procedure:** search before reconciliation edits; search literal references and plausible synonyms across code, docs, tests and config/build/CI, including vendor/archive triage. Source: Quick reference, Procedure 1, What counts as a reference. **Owner-clarified outcome:** reconcile moved paths and documentation of changed code facts; relevant path variants and relative-path resolution are applications of that intent, not explicit instructions in the skill. | Find siblings of the triggering defect, including broken path references and documentation of changed code facts. | Retained search commands/results and edit ordering, checked against supplied project state. Record a path-handling miss under the clarified outcome; do not infer an explicit-instruction violation from that miss alone. |
| O2 | Classify matches as update, false positive with reason, or intentionally stale with reason. Skill: Procedure 2. | Reconcile real consumers while preserving unrelated matches and historical meaning. | Final changes, unchanged material and reasons linked to each matching location. |
| O3 | Reconcile all required updates in one commit. Skill: Procedure 3. | Avoid committing an inconsistent intermediate project state. | Git history/diff relative to the prepared original; all required changes in one reconciliation commit. |
| O4 | Account for matches in `References swept:`, grouped only by the same path and outcome, with precise locations and counts. Group before exceeding the normal commit-body preference; a broad sweep may exceed it after grouping. Skill: Output artifact. | Make coverage and deliberate preservation independently inspectable without treating necessary audit detail as verbosity. | Commit body reconciled to retained searches and final changes; after narrative and before a Verification section when present. No invented hard length cap. |
| O5 | Give the required `References swept: n/a — <reason>` in the single-file/no-sweep case. Skill: Quick reference and Output artifact. | Distinguish a justified negative finding from forgotten accounting. | Recorded search/scope basis and the negative-form commit line. |

Accept any effective search tool, sensible query order, equivalent edits and concise grouping that preserve these obligations.
Do not require a particular document structure, word count or wording from a constructed reference answer beyond the explicitly prescribed labels/header and negative form.
Useful repetition and document restructuring remain acceptable when the resulting document is at least as effective; local text differences are evidence to inspect, not automatic failures.

Owner accepted, 2026-09-12: interpret “single-file/no-sweep” as a justified outcome after checking scope, not permission to skip searching because only one file was initially named.
Owner clarification, 2026-09-12: score functional effectiveness and procedural/mechanical effectiveness separately. Outcome failures are hard failures; the consequence of procedural inconsistency depends on the skill.
The owner initially permitted either procedural severity choice; the pilot walkthrough clarified the priority: the actual committed reconciliation matters, while a fully detailed commit message is nice to have.


## Assessment policy

The owner accepted the criterion boundaries, evidence-backed outcomes, separate setup/functional/procedural treatment and explicit assessor context.
In the retained policy text below, “fixed-format score record” means the [execution result](../formats/execution-result.template.json) for one execution; the [batch assessment](../formats/assessment.template.md) aggregates the declared repetitions under the [spec's assessment rules](../../plans/specs/2026-09-11-model-driven-skill-testing-framework.md#6-assess-observations-and-establish-the-baseline).
No batch acceptance threshold or full baseline repetition count is selected yet. Use descriptive counts until the concrete scope/rule is agreed; no default 4/5 threshold follows from the format example.
Input-format changes do not alter the following criterion policy. Historical references to preserving or separately identifying a correction are satisfied by committed Git versions and a concise reason, not duplicate history files.

The [policy-3 copy](assessment-policies/SSR-assessment-3.txt) derives verbatim from the following subsection. Existing assessed pilot inputs retain policy 2; the current Shiv, semantic-delivery and moved-guide controller definitions use policy 3.

### Current SSR assessment policy

Policy identity: **SSR-assessment-3**, 2026-09-14 workflow correction. The owner’s functional/procedural scoring decisions from SSR-assessment-2 remain unchanged; this version removes the unintended separate-evaluator/calibration prerequisite and makes active-session assessment the default. Observed-run case inputs, historical worked examples and prior assessments retain their policy-2 copies and identities; their preparation-time calibration requirements are superseded as workflow. Current controller inputs for unrun cases use policy 3. New assessments must identify policy 3 alongside the applicable versioned case criteria; do not overwrite historical scores or silently relabel old inputs.
Selected policy: assess each agreed criterion as met, not met or insufficient evidence, retaining the supporting evidence and consequence. Keep the two dimensions visible instead of combining them into a single score.
Incomplete or incorrect reconciliation, including damage to material that should be preserved, is a hard functional failure.
When the task requires committing the repair, verify that every required edit is committed; a correct but uncommitted working tree does not meet that task outcome. Separately assess whether the edits were grouped into one commit.
Lead the result with whether all affected references were correctly reconciled, protected material preserved, and required edits committed. Derive these judgments from the project, checks and Git history, not the completeness or confidence of the commit message.
Purely procedural deviations are non-blocking defects for this study: report search-order, classification/accounting, commit-grouping and format failures explicitly without treating them alone as a failed functional outcome.
Detailed accounting is secondary: an omission may be recorded against the original skill's explicit instructions, but cannot turn functional success into failure, block progression by itself, or require another run merely to obtain a fuller message. This SSR policy does not weaken output contracts for other skills with downstream consumers.
This severity policy does not make the original's explicit requirements optional or establish full compliance when they are missed.
Known output consumers: people and reviewing agents inspecting the reconciliation commit use `References swept:` as an audit account; the skill's Output artifact section explains the locations, outcomes and count reconciliation they need. DD Gate 4 and this project's commit guidance require that account.
Inspection of shipped skills, hooks, commands, examples and top-level tests found no named program consuming this format, and a targeted search of hook Python sources found no `References swept` parser. This bounds the inspection, not a claim about every consumer installation.
Missing or inconsistent accounting impairs auditability; no identified program requires exact syntax to perform the reconciliation itself. That supports the selected non-blocking accounting policy while retaining the original's explicit format checks.
Complete reconciliation with correct preservation but missing `References swept:` therefore meets the functional criteria and fails the accounting criterion; a well-formatted account cannot offset unresolved current references or incorrectly changed historical references.
Where a procedural deviation also causes a functional failure, record that consequence and apply the functional hard-failure rule.
A procedural regression remains relevant to the later adoption decision even when non-blocking; agree on the rewrite's acceptance boundaries before authoring rather than treating this policy as automatic adoption approval.
Apply the useful-outcome criteria to both conditions; target-specific compliance describes the original condition and must not penalize the unguided control for undisclosed instructions.
Count and location conventions must be fixed with the eventual checkers, including repeated searches of the same location, so duplicate search hits cannot inflate claimed coverage. State which query results require accounting, including already-current references found during exploration, before assigning a defect for omitted entries. Pilot 01 surfaced competing readings of that scope; its [assessment correction](pilot-results.md#assessment-correction-2-2026-09-12) does not establish a skill defect or authorize a rewrite objective.
Missing action traces yield insufficient evidence for order/completeness claims, not an invented behavioral failure or pass.
Historical commits, PR descriptions and chat logs are not rewrite targets; vendor/archive files still require triage under the skill's stated distinctions.

For every subsequent assessment, the active agent or human reads this policy and the applicable case criteria, inspects the retained evidence and writes the fixed-format score record. Record policy/criteria identities, assessor context, run/configuration/skill identities, evidence citations, per-criterion judgments and consequences. Copy or identify the exact policy bytes used; keep these scoring instructions out of subject inputs. Active-session assessment is a normal scored result, not an unrecorded substitute for a separately dispatched evaluator.
Before another case is dispatched, map its criteria to functional or procedural outcomes and their consequences under this policy. Apply these settled distinctions directly: complete committed reconciliation with sparse accounting succeeds functionally; incomplete reconciliation fails despite a perfect account; correct-but-uncommitted work fails the required committed outcome. Worked examples can resolve a genuine ambiguity but do not require separate model calls or an evaluator qualification gate.
If a judgment contradicts those boundaries, correct and version the assessment; do not blame or rerun the subject to repair the scoring. The runner captures evidence and configuration identity; it does not enforce these semantic judgments automatically.
The completed pilot's frozen assessment, manifest and raw bundles retain their original identities. This clarification does not change its functional verdicts; any later reassessment must be separately identified with its applied policy, rather than overwriting the original record.

## Suite and evidence

### Proposed baseline case selection

The owner accepted CLI rename, moved-path reconciliation and changed-behavior documentation as the three core situations. Core-baseline-01 selects all three with two new executions per condition under the scope below.

| Case | Membership / exposure | Coverage and limits | Rules and evidence |
|---|---|---|---|
| discovery-shiv | Selected for core-baseline-01; exposed development case | O1–O4: CLI consumers in README, script, Make and CI; triage, preservation and committed repair. Literal location diversity, not demonstrated hard discovery. | [Case](cases/discovery-shiv/assessment.md), [manifest](cases/discovery-shiv/manifest.json), [qualification](cases/discovery-shiv/qualification.json), [source provenance](cases/discovery-shiv/source-provenance.json). |
| moved-guide | Selected for core-baseline-01; historical pilot-02 pair stays separate | O1–O4: moved guide, relative links and executable export consumer; preservation and committed repair. New measured executions are distinct from the pilot. | [Current case](cases/moved-guide/assessment.md), [manifest](cases/moved-guide/manifest.json), [historical qualification](cases/pilot-02/qualification.json). |
| semantic-delivery | Measured semantic-delivery-01; selected for core-baseline-01 | O1–O4: meaning-based descriptions of attempts/retries/stopping, preservation and committed repair. Passing runtime checks alone cannot establish correct prose. | [Case](cases/semantic-delivery/assessment.md), [manifest](cases/semantic-delivery/manifest.json), [qualification](cases/semantic-delivery/qualification.json). |
| pilot-01 | Historical development evidence | Process pilot; accounting-scope ambiguity remains uncertainty, not a confirmed skill defect. | [Report](pilot-results.md), [case](cases/pilot-01/assessment.md). |
| pilot-03 | Rejected, undispatched | Replaced by Shiv preparation; not active suite work. | [Retained case](cases/pilot-03/assessment.md). |
| Genuinely local change | Deferred; no selected case | O5 unmeasured: no claim about justified negative sweeps or the required negative-form account. | Contract above. |

The cases exercise broadening beyond the trigger, complete reconciliation, preservation and useful accounting; facets may share a case.
Both pilot controls encountered all current consumers before making a narrow repair, so those observations support repair-scope comparison, not a discovery advantage.
Shiv's public-source familiarity may affect either condition; project size and lack of explicit upstream references do not establish unfamiliarity or hard discovery.
Inspect any upstream-restoring edit against the settled task before attributing its cause; familiarity does not excuse an incorrect outcome.
Equivalent repairs and document restructuring remain valid under the case rules. Checkers report observable facts; the active agent inspects meaning, preserved behavior, trace and Git evidence.
Use existing constructed correct/incorrect variants to check mechanical observations and clarify real ambiguities. They are not measured model performance or a separate evaluator exam.
Native skill discovery, composition, specialized search difficulty, reserved transfer and population reliability remain outside the selected claim. No additional case or control failure is required merely to advance collection.

## Execution scope and authorization

Follow the [ordinary active-session workflow](../../plans/specs/2026-09-11-model-driven-skill-testing-framework.md#default-work-session-workflow).
No separate evaluator or calibration campaign is required. Optional read-only evaluator capability is documented in [permission qualification](permissions-qualification.json); it is not a pending dispatch.
Original and control receive the same task, project and neutral setup; original alone receives the frozen SSR skill and its read instruction. An eventual candidate substitutes only separately identified target bytes.
Supply a realistic triggering defect and permission to fix related files, without enumerating consumers or teaching the target's sweep procedure in the control.
DD and other instructions used by the controller session are not subject inputs. Assessment policies, expected facts and checkers remain controller-only.
An explicit sweep request is a different execution-quality question and cannot establish that SSR caused scope expansion.

The prepared original/control configurations retain Codex Sol-low with workspace-write. Configurations and manifests own exact settings and source identities; do not silently pool different models or changed rules.
The existing runner uses config schema 0.2 and result schema 0.3. It prepares a fresh Git boundary, invokes once and captures mechanical completion plus evidence; it does not decide task success.
[Runner mechanics](../../skill-validation/runner/README.md) and [retained pilot reports](#results-and-decision) establish the available execution path. Recheck changed CLI/runtime/context assumptions before relying on them; directory separation alone does not prove read isolation.
Control contribution claims require evidence that omitted guidance was not loaded. Record limits on observed isolation rather than claiming exhaustive host-wide exclusion.

Pre-baseline development is closed at two pairs. Do not reopen it for a new facet; a named readiness defect requires a separately authorized diagnostic exception.
### First collection: semantic-delivery-01

Status: completed; both authorized calls spent, with no repeat of this batch authorized. The owner authorized this batch on 2026-09-16 in this session: “ok, let's do it. what model/effort will we be using for the runs?” The response confirmed the unchanged `gpt-5.6-sol` / low settings for both commands. This batch is the first baseline observation, not another process pilot or completion of the wider baseline.
Question: does the frozen original achieve complete committed semantic reconciliation here, and how does the same task behave without SSR guidance?
Scope: `semantic-delivery` only; `original` then `control`, one execution each, sequentially. This fixed order is convenient, not counterbalanced; one observation per condition cannot establish consistency or population reliability.
Inputs: [version-1 manifest](cases/semantic-delivery/manifest.json), [case rules](cases/semantic-delivery/assessment.md) and their pinned authorities. Configurations below own Sol-low/workspace-write settings; original alone supplies the frozen skill.
Acceptance: descriptive-only. Include every valid-setup execution, including functional failures and unknown criteria; show invalid/unassessed attempts and uncompleted conditions separately. No threshold, selective replacement or automatic retry.
Stop after both attempts, or earlier for preservation failure, unresolved invocation charge, suspected contamination or an execution/setup error requiring inspection. A valid behavioral failure does not cancel the control. Further attempts require separate authorization.
Authorized spending: at most **2 subject invocations**, zero evaluator/authoring/retry calls. Both invocations are spent; they authorize no larger campaign.

Commands used separately from `/Users/simon/work/personal/disciplined-development-skills`, after approval and input/CLI identity verification; recorded for reproducibility, with no re-execution authorized:

```sh
TMPDIR=/private/tmp/ssr-semantic-delivery-01 skill-validation/runner/.venv/bin/skilltest run skill-studies/sweeping-stale-references/cases/semantic-delivery/original.json
```

The first bundle was preserved and verified before the second command:

```sh
TMPDIR=/private/tmp/ssr-semantic-delivery-01 skill-validation/runner/.venv/bin/skilltest run skill-studies/sweeping-stale-references/cases/semantic-delivery/control.json
```

The namespaced temporary directory has been created. The commands require host permission for app-server initialization under the [runner's existing execution procedure](../../skill-validation/runner/README.md#run); subject permissions remain the configured workspace profile.
Local identity check: `/opt/homebrew/bin/codex` resolves to `/opt/homebrew/Caskroom/codex/0.154.0/bin/codex`, version `codex-cli 0.154.0`, SHA-256 `4f85982624b3898c8991cb80c0981b2aa71070e3537046c9a95950318a95afcc`, matching the prepared CLI. The requested model name does not expose an immutable model revision.
The runner retains its 900-second model timeout. The runner tree is byte-for-byte unchanged from the [pilot-02 tested revision](pilot-02-run-index.json), `c1ca9599abba6acc6a3ef884a9ac00a24e72e83c`; no runner change is required for these commands. Recheck mutable execution dependencies before dispatch.

The runner emits each unique bundle path beneath `/private/tmp/ssr-semantic-delivery-01/skilltest-runs/`. After writes stop, preserve the complete directory at the development primary below using that emitted directory name, inventory and verify it, then record the actual attempt in [semantic-delivery-01-run-index.json](semantic-delivery-01-run-index.json).
The index records the two actual attempts, their authorization, retained evidence and canonical execution results.
The index resolves both execution results; [semantic-delivery-01-assessment.md](semantic-delivery-01-assessment.md) records coverage, counts, uncertainty and the observed condition comparison after disposable replay and evidence inspection.
The index pins the committed authorization, frozen manifest and execution results; these completed commands do not authorize repeating the batch.


### Core baseline: core-baseline-01

Status: owner-approved on 2026-09-16 in this session: “ok, the next step is approved, please continue”, following the proposal of three prepared cases × original/control × two additional executions each (12 calls). This approval covers this batch only.
Question: across semantic delivery, a moved guide and the Shiv rename, do the original and no-target conditions repeat complete committed reconciliation, and which failures recur?
Scope: exactly the twelve executions below, sequentially. All use the existing Codex `gpt-5.6-sol` / low / workspace-write configurations. Original receives only the frozen SSR skill plus its loading instruction beyond the control inputs.
Original/control order reverses in repetition 2 for every case; case order stays fixed. This balances condition order locally, not every temporal or model effect.
Acceptance/inclusion: descriptive-only, with no threshold. Include all valid-setup executions regardless of outcome; retain unknowns in counts and reconcile invalid/uncompleted attempts separately. Earlier semantic-delivery-01 and historical pilots remain separately identified and outside this batch's denominator.
Stopping/retries: preserve and verify each stopped attempt before the next dispatch. Stop for unresolved charge, preservation failure, suspected contamination or an infrastructure/setup error requiring inspection. Behavioral failure alone does not stop the remaining planned executions. No automatic retry, replacement, extra provider call or skill edit is authorized.
Budget: at most 12 additional subject invocations; zero evaluator/authoring/retry calls. Full collection would leave 22 subject calls under the existing ceiling for later selected work. No larger campaign or pool transfer follows.

Working directory: `/Users/simon/work/personal/disciplined-development-skills`. For each row, invoke `TMPDIR=/private/tmp/ssr-core-baseline-01 skill-validation/runner/.venv/bin/skilltest run CONFIG`, substituting only the exact CONFIG path shown below. The namespace is created before invocation. These commands use the same host initialization permission and unchanged workspace profile as semantic-delivery-01.

| Order | Case | Condition | Repetition | CONFIG |
|---:|---|---|---:|---|
| 1 | semantic-delivery | original | 1 | `skill-studies/sweeping-stale-references/cases/semantic-delivery/original.json` |
| 2 | semantic-delivery | control | 1 | `skill-studies/sweeping-stale-references/cases/semantic-delivery/control.json` |
| 3 | moved-guide | original | 1 | `skill-studies/sweeping-stale-references/cases/pilot-02/original.json` |
| 4 | moved-guide | control | 1 | `skill-studies/sweeping-stale-references/cases/pilot-02/control.json` |
| 5 | discovery-shiv | original | 1 | `skill-studies/sweeping-stale-references/cases/discovery-shiv/original.json` |
| 6 | discovery-shiv | control | 1 | `skill-studies/sweeping-stale-references/cases/discovery-shiv/control.json` |
| 7 | semantic-delivery | control | 2 | `skill-studies/sweeping-stale-references/cases/semantic-delivery/control.json` |
| 8 | semantic-delivery | original | 2 | `skill-studies/sweeping-stale-references/cases/semantic-delivery/original.json` |
| 9 | moved-guide | control | 2 | `skill-studies/sweeping-stale-references/cases/pilot-02/control.json` |
| 10 | moved-guide | original | 2 | `skill-studies/sweeping-stale-references/cases/pilot-02/original.json` |
| 11 | discovery-shiv | control | 2 | `skill-studies/sweeping-stale-references/cases/discovery-shiv/control.json` |
| 12 | discovery-shiv | original | 2 | `skill-studies/sweeping-stale-references/cases/discovery-shiv/original.json` |

Input identities: [semantic delivery](cases/semantic-delivery/manifest.json), [moved guide](cases/moved-guide/manifest.json), [Shiv](cases/discovery-shiv/manifest.json). Reuse semantic delivery's existing frozen inputs; its earlier protocol pin is input/rule provenance, not this batch's authorization. Every new attempt cites the current batch authorization separately. The new moved-guide controller definition references the historical pilot's unchanged subject/configuration/checker files; its historical policy-2 package remains intact.
The CLI still resolves to version 0.154.0 and the hash recorded above; the runner remains unchanged from the qualified pilot-02 tree. Recheck mutable identities before dispatch; the provider does not expose an immutable model revision.
The runner emits unique bundles beneath `/private/tmp/ssr-core-baseline-01/skilltest-runs/`; preserve complete stopped bundles under the development primary using their emitted directory names and one inventory each. [core-baseline-01-run-index.json](core-baseline-01-run-index.json) records every actual attempt and its canonical result; an empty index before collection does not imply executions.
Inspect/replay only disposable copies, using each case's fixed checker and semantic rules. Write execution results at `results/<run-id>.json` and the aggregate at `core-baseline-01-assessment.md`; the protocol owns subsequent decisions. The [partial assessment](core-baseline-01-assessment.md) records order 1: complete functional repair, but missing full skill-read output leaves setup attribution unresolved. Collection is paused before order 2 under the existing stop rule. Diagnose capture with retained evidence/offline checks before resuming; no retry or replacement is authorized. Do not silently change frozen input/capture settings or weaken setup requirements.


## Storage and accounting

Canonical project checkout: `/Users/simon/work/personal/disciplined-development-skills`.
Reserved primary: `/Users/simon/work/personal/skill-study-private/sweeping-stale-references/`.
Reserved backup: `/Users/simon/work/personal/skill-study-backups/sweeping-stale-references/`.
External raw development primary: `/Users/simon/work/personal/skill-study-private/sweeping-stale-references/development/`; backup: `/Users/simon/work/personal/skill-study-backups/sweeping-stale-references/development/`.
These locations are resolved from the canonical checkout. The development primary and backup now contain the permission-probe bundles and all four complete pilot bundles indexed above; reserved-case access isolation remains unqualified.
For any future explicitly selected held-out claim, an unexposed author receives only permitted copied evidence. The ordinary active-session workflow uses known cases and must not claim held-out validation.
For future runs, retain one complete bundle in the existing development primary, verify it against one inventory and index it before further dispatch; include unsuccessful attempts.
The owner accepted removing the mandatory second study-managed copy; that decision did not establish an operating backup arrangement.
Backup check, 2026-09-15: `tmutil destinationinfo` reports no destinations configured, while `tmutil isexcluded /Users/simon/work/personal/skill-study-private/` reports Included.
The owner-supplied Claude review also found no common backup agents running or iCloud coverage for this location; this session independently verified the Time Machine results, not every possible backup mechanism.
Treat raw evidence retention as single-host unless another arrangement is identified. Existing same-host copies do not establish host-loss recovery, and Git cannot recover external raw bundles.
Owner decision, 2026-09-15: after the backup check and explicit host-loss explanation, the owner accepted single-host retention for this study, including possible loss of external raw bundles if the machine is lost or fails.
No backup configuration is required by this accepted scope; verify local bundle preservation before further dispatch. This storage decision does not authorize model runs.
Keep historical primary/backup copies unchanged. The small run index references runner metadata and one canonical assessment rather than duplicating settings/status/timing; Git supplies repository-record history.

Keep one canonical repository record per accepted run and commit it before correction; Git retains earlier versions.
Historical citations use commit/path/hash, including the worked example's run-index reference; no duplicate snapshots or extensive amendment ledger are required.

**Current accounting (2026-09-16): 471 active minutes booked; 729 minutes (12 hours 9 minutes) remain under the 1,200-minute ceiling.**
This includes preparation, review and model/tool waits, excludes owner-wait, and retains prior conservative allowances; the current booking includes the intervening active review turns and this preparation/attempt/diagnosis session, with verification and closing allowance through 18:58 UTC.
Preparation and collection/assessment effort are included in the combined active total; the internal category split was not separately timed.
Update this paragraph in place from the latest booked total plus new active intervals counted once; Git retains prior checkpoints, and their source logs are optional reconciliation evidence.
Dispatched calls are **7 subject, 0 evaluator, 0 authoring, 0 retry**; remaining outer capacity is **33 / 12 / 4 / 4**. Eleven core-baseline-01 subject calls remain authorized but paused; no replacement is authorized for its setup-unresolved attempt.


Remaining-work forecast, in active minutes, including model/tool waits, review and storage once:

| Work | Estimate | Basis |
|---|---:|---|
| Document generator/validator | 120 | Existing preliminary implementation/qualification allowance; refine scope after baseline assessment. |
| Evidence-capture diagnosis | 25 | Bounded offline investigation allowance; scope any changed collection mechanics before resumption. |
| Remaining core collection/preservation | 195 | Eleven 15-minute timeout ceilings plus local preservation overhead, conditional on resolving the capture pause. |
| Core batch assessment/review | 90 | Apply existing checks/rules to twelve observations and aggregate by case/condition. |
| Any justified rewrite and contemporaneous comparison | 180 | Conditional planning allowance, not a rewrite approval or selected later call count. |
| Closure and review | 30 | Decision, limitations and study closeout. |
| **Total** | **640** | Forecast, not additional authorization. |

Compare this total with the current remaining time above; it fits that ceiling with contingency, subject to revision when later scope is known. This is an estimate, not a guarantee of whole-study completion.
Preserve later comparison capacity when selecting additional repetitions; no automatic pool transfers, retries or ceiling extensions are allowed.


## Results and decision

| Evidence | Interpretation |
|---|---|
| [Core-baseline-01 partial assessment](core-baseline-01-assessment.md) | One attempt retained; setup evidence unresolved, no included aggregate observations. Eleven executions unattempted; dispatch paused. |
| [Semantic-delivery-01 assessment](semantic-delivery-01-assessment.md) | First measured batch: original completes committed reconciliation; control leaves two current claims stale. One observation per condition; no consistency claim. |
| [Pilot 01 report](pilot-results.md), [attempt index](pilot-run-index.json), [checks](pilot-checks.json) | Historical original/control development pair; assessment correction and limits belong in the report. |
| [Pilot 02 report](pilot-02-results.md), [attempt index](pilot-02-run-index.json), [checks](pilot-02-checks.json) | Historical moved-guide pair; retained evidence supports the recorded outcomes, not a stable reliability estimate. |
| [Policy-3 worked example](assessments/pilot-02-original-policy-3-example.json), [identity/schema index](assessments/index.json) | Unchanged illustrative assessment of retained evidence, not a new execution or replacement of the canonical policy-2 result. |

The first batch is assessed; no broader baseline conclusion, rewrite objective or adoption decision exists yet.
Batch assessments own aggregate counts, patterns, limitations and any version comparison; this section records the owner's resulting decisions by reference.
After baseline assessment, agree the generator/validator's bounded CLI and effort before implementation. It is not a collection prerequisite.
Before authoring, re-read the selected writing-skills guidance and reconcile it with the evidence-supported objective. A passing control is useful evidence; resolve any pure-cleanup/RED conflict without manufacturing failure or resuming the abandoned wording campaign.
Compare the exact candidate with contemporaneous original executions under declared conditions; add a contemporaneous no-target condition only for a current contribution claim.
Retain, adopt, revise or close inconclusive according to supported evidence and the owner's decision; an aggregate improvement cannot conceal a consequential regression.
