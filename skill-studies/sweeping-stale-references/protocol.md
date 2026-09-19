# Sweeping stale references: study protocol

Format version: `1`
Study ID: `sweeping-stale-references`
Status: closed for the selected Sol-low study; all authorized collection and assessment complete. Owner deferred adoption while further studies proceed; no rollout or further collection is selected.
The [plan](../../plans/2026-09-11-model-driven-skill-testing.md) owns progress; the [spec](../../plans/specs/2026-09-11-model-driven-skill-testing-framework.md) owns the workflow.
The [core baseline](core-baseline-01-assessment.md) retains its two setup exclusions and runtime strata; the [comparison](comprehensive-comparison-01-assessment.md) records twelve valid executions of the original and preserved candidate. Both collection scopes are spent. Storage and accounting retains the SSR closing checkpoint and links the current combined totals.

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
Core-baseline-01 fixes two executions per case/condition and descriptive counts; no universal acceptance threshold follows from the format example.
Input-format changes do not alter the following criterion policy. Historical references to preserving or separately identifying a correction are satisfied by committed Git versions and a concise reason, not duplicate history files.

The [policy-3 copy](assessment-policies/SSR-assessment-3.txt) derives verbatim from the following subsection. Existing assessed pilot inputs retain policy 2; the current Shiv, semantic-delivery and moved-guide controller definitions use policy 3.

### Session evidence amendment: capture-2

Owner-approved on 2026-09-16: “the code change is approved, please continue”, together with addressing the review findings. Applies prospectively to core-baseline-01 orders 2–12; order 1 retains its frozen assessment and remains excluded. The amendment preserved the twelve-slot scope, orders 2–12, model/effort, task/skill bytes, criterion meanings and no-retry rule.
Codex session persistence replaces ephemeral execution in the fresh private profile. Before cleanup, the runner copies its single session to `provider-session.jsonl` in the existing bundle; result schema 0.4 identifies that artifact. Each resumed attempt cites this amendment at its frozen Git revision, which also identifies the revised runner. Earlier input-manifest pins still identify unchanged subject inputs and criterion policy; this explicit capture amendment governs the new evidence source.
Admissible exposure evidence is either complete command output in `stdout.txt` or actual tool-response content in `provider-session.jsonl`. For the session source, verify its hash against the mechanical result/inventory, match session identity to stdout's thread ID and session cwd to this invocation's fixture, and connect each response's call ID to its read command. Inspect output content, ordering and truncation; whole-text equality to the frozen skill, or faithful reconstruction from retained ordered read/poll responses, must establish full exposure. An attempted command, model summary, input-file presence or filename listing alone is insufficient. Missing/truncated output that cannot establish the required content keeps setup `insufficient evidence` and stops further dispatch for inspection.
Controller checks record `original_skill_read_evidence` with the source artifact, response line numbers and call IDs; `original_skill_read_trace_lines` in older checks remains historical stdout-only evidence. The old field is not a required field for new checks. The same admissible-source rule supports content exposure/search-order inspection for both conditions; target procedures remain inapplicable to control. Apply missing-evidence consequences only to what the evidence cannot establish.

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

### Proposed coverage expansion (2026-09-19)

The owner selected SSR for the next preparation step and requested fleshing out the necessary scenarios before editing the skill.
The [coverage proposal](coverage-expansion.md) adds an ordinary initiating change and a genuinely local correction to the existing three executable situations, plus a separate large-sweep accounting diagnostic.
[Offline qualification](expansion-qualification.md) and the new case cards describe concrete tasks, source-grounded rules, alternatives and boundaries; all are exposed reconstructed development cases.
Preparation is authorized; new case definitions are draft, no additional subject allocation is approved, and no skill authoring or adoption follows.
The completed baseline and comparison remain unchanged. The old local-change deferral describes their collected scope; the proposed new case does not retroactively fill that gap.
The proposed eight-call original/control expansion and the resolved diagnostic-only record representation are stated in the coverage proposal for owner review.
Current combined accounting remains in the CW protocol as linked below; CW scenario expansion is deferred while SSR is selected.

## Execution scope and authorization

Follow the [ordinary active-session workflow](../../plans/specs/2026-09-11-model-driven-skill-testing-framework.md#default-work-session-workflow).
No separate evaluator or calibration campaign is required. Optional read-only evaluator capability is documented in [permission qualification](permissions-qualification.json); it is not a pending dispatch.
Original and control receive the same task, project and neutral setup; original alone receives the frozen SSR skill and its read instruction. An eventual candidate substitutes only separately identified target bytes.
Supply a realistic triggering defect and permission to fix related files, without enumerating consumers or teaching the target's sweep procedure in the control.
DD and other instructions used by the controller session are not subject inputs. Assessment policies, expected facts and checkers remain controller-only.
An explicit sweep request is a different execution-quality question and cannot establish that SSR caused scope expansion.

The prepared original/control configurations retain Codex Sol-low with workspace-write. Configurations and manifests own exact settings and source identities; do not silently pool different models or changed rules.
SSR collection used config schema 0.2 and result schema 0.4; retained bundles keep their emitted versions. The current runner contract is documented in the runner guide below. It prepares a fresh Git boundary, invokes once and captures mechanical completion plus evidence; it does not decide task success.
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
At collection, the runner retained its 900-second model timeout. Its tree was byte-for-byte unchanged from the pilot-02 tested revision `c1ca9599abba6acc6a3ef884a9ac00a24e72e83c` (historical provenance is in [Results and decision](#results-and-decision)); no runner change was required for these commands. Recheck mutable execution dependencies before any future authorized dispatch.

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
The CLI resolves to version 0.154.0 and the hash recorded above. Orders 2–5 pin capture-2; orders 6–12 pin capture-2 plus runtime-1. All twelve attempts are complete. Any later selected collection must recheck mutable identities; the provider does not expose an immutable model revision.
The runner emits unique bundles beneath `/private/tmp/ssr-core-baseline-01/skilltest-runs/`; preserve complete stopped bundles under the development primary using emitted directory names and one inventory each. [core-baseline-01-run-index.json](core-baseline-01-run-index.json) records every actual attempt and canonical result.
Inspect/replay only disposable copies using fixed case checkers and semantic rules. Execution results live at `results/<run-id>.json`; the [batch assessment](core-baseline-01-assessment.md) records all twelve attempts, exclusions and aggregates. Orders 1 and 5 remain excluded for different setup faults. No retry, replacement or additional call is authorized by this completed scope.

#### Runtime amendment: runtime-1

The [runtime diagnosis](runtime-diagnosis.md) records the new fault: the subject shell selects Python 3.9.6, which cannot parse the supplied Shiv dependency. The narrow correction is implemented and verified offline: pass the prepared restricted PATH explicitly through `shell_environment_policy.set`, keeping other environment inheritance disabled. It selects the compatible host Python 3.14.7 and passes the actual CLI's scripted local tests and consumer checks with zero model calls.
Owner approved continuation on 2026-09-16 after reviewing the concrete correction: “address any relevant findings, and the let's continue”. The committed runtime-1 authority governed only orders 6–12, preserving task/skill/criteria bytes, model/effort, order, allocation and no-retry rule. All seven completed with usable setup; the invalid Shiv attempt remains excluded and unreplaced. Orders 2–4 retain their pre-correction runtime labels; the assessment reports total descriptive counts and runtime-stratum counts without claiming fixed-runtime replication across the change. The capture-error reporting correction preserves provider exit/timeout facts and adds no model call or scoring change.



### Comparison: comprehensive-comparison-01

Status: complete. The owner approved these twelve executions on 2026-09-17 after reviewing the proposal. All twelve were collected and assessed without retries or replacements, under unchanged judgment boundaries and the approved candidate-applicability extension. The frozen invocation-authority revision identifies the full runner checkout used throughout collection. This scope has no unspent call; adoption is deferred under Results and decision.
Question: on the three existing development cases, does the comprehensive rewrite preserve complete committed reconciliation and protected behavior while making its audit account more accurate/useful than the contemporaneous original?
Scope: exactly twelve sequential executions below: three cases × two versions × two repetitions. Each case has adjacent original/candidate pairs, with version order reversed for repetition 2. This balances first/second position within a case; it is not randomization or enough replication to estimate population reliability. Six calls would give only one observation per case/version; twelve permits a limited repeatability check while leaving ten subject calls unused. No no-target condition was included because this question compares versions; the earlier contribution baseline remains separate.
Acceptance/inclusion: descriptive-only. Include all valid-setup executions regardless of outcome; retain unknown criteria and report invalid/unresolved setups and unattempted slots separately. No automatic retry or replacement. Compare per-case functional and procedural counts using the same rules and evidence requirements; do not pool the historical baseline into the new denominators or hide a functional regression in a higher aggregate count. A tie in criterion outcomes demonstrates no behavioral improvement; the assessment may separately identify a simplification benefit using the spec’s size measure. Any candidate functional regression requires explanation before an adoption recommendation; ambiguous or inconsistent differences remain inconclusive. The owner decides adoption after reviewing evidence, not from a new numerical threshold.
Stop: preserve and inventory each stopped bundle before the next dispatch; stop for unresolved invocation charge, failed preservation, suspected contamination or a setup/infrastructure defect requiring inspection. A valid behavioral failure does not cancel the remaining rows. Stop at the declared twelve attempts or the study's outer ceiling; no extra calls or replacements follow automatically.
Budget: authorized maximum **12 subject invocations**, zero evaluator/authoring/retry calls. Completion would bring study subject spending to **30/40**, leaving **10 subject**, **12 evaluator**, **4 authoring**, **4 retry** capacity. This authorization covers only the twelve table rows; no pool transfer or additional call follows.

Versions and settings: original uses the preserved [original](cases/skill-original/SKILL.md); candidate uses the exact [comprehensive snapshot](cases/skill-candidate-comprehensive/SKILL.md) identified in Results and decision. The candidate changes several instructions, so any difference concerns the whole version. Both use provider `codex`, model `gpt-5.6-sol`, effort `low`, `workspace-write`, the same case task/prompt/project and the same skill target path/full-read instruction. Original configuration IDs remain unchanged; candidate IDs identify only the new configuration. Offline loader/copy checks confirm that the skill file is the only differing supplied file per pair.

Recorded working directory: `/Users/simon/work/personal/disciplined-development-skills`. Each completed row used this command with its table configuration; it is not authorization to repeat collection:

```sh
TMPDIR=/private/tmp/ssr-comprehensive-comparison-01 skill-validation/runner/.venv/bin/skilltest run CONFIG
```

`CONFIG` is the exact table value. All rows used the 900-second model timeout and qualified capture-2/runtime-1 execution path, including the restricted PATH selecting Homebrew Python. Host permission supports app-server initialization while the subject remains under the configured workspace profile.

| Order | Case | Condition | Repetition | CONFIG |
|---:|---|---|---:|---|
| 1 | semantic-delivery | original | 1 | `skill-studies/sweeping-stale-references/cases/semantic-delivery/original.json` |
| 2 | semantic-delivery | candidate | 1 | `skill-studies/sweeping-stale-references/cases/semantic-delivery/candidate-comprehensive.json` |
| 3 | moved-guide | candidate | 1 | `skill-studies/sweeping-stale-references/cases/moved-guide/candidate-comprehensive.json` |
| 4 | moved-guide | original | 1 | `skill-studies/sweeping-stale-references/cases/pilot-02/original.json` |
| 5 | discovery-shiv | original | 1 | `skill-studies/sweeping-stale-references/cases/discovery-shiv/original.json` |
| 6 | discovery-shiv | candidate | 1 | `skill-studies/sweeping-stale-references/cases/discovery-shiv/candidate-comprehensive.json` |
| 7 | semantic-delivery | candidate | 2 | `skill-studies/sweeping-stale-references/cases/semantic-delivery/candidate-comprehensive.json` |
| 8 | semantic-delivery | original | 2 | `skill-studies/sweeping-stale-references/cases/semantic-delivery/original.json` |
| 9 | moved-guide | original | 2 | `skill-studies/sweeping-stale-references/cases/pilot-02/original.json` |
| 10 | moved-guide | candidate | 2 | `skill-studies/sweeping-stale-references/cases/moved-guide/candidate-comprehensive.json` |
| 11 | discovery-shiv | candidate | 2 | `skill-studies/sweeping-stale-references/cases/discovery-shiv/candidate-comprehensive.json` |
| 12 | discovery-shiv | original | 2 | `skill-studies/sweeping-stale-references/cases/discovery-shiv/original.json` |

Assessment rules: [semantic delivery](cases/semantic-delivery/assessment.md), [moved guide](cases/moved-guide/assessment.md), [Shiv](cases/discovery-shiv/assessment.md), policy 3 and existing checkers remain the basis. Approved applicability amendment: version-2 controller definitions add `candidate` wherever a criterion applies to `original`, with identical setup and judgment boundaries/consequences. Historical manifest pins retain version 1 and prior original/control results. The comparison manifests identify the full current case condition set; only original/candidate are scheduled. Do not change a criterion to accommodate candidate output.
Input identities: [semantic manifest](cases/semantic-delivery/comparison-manifest.json), [moved-guide manifest](cases/moved-guide/comparison-manifest.json), [Shiv manifest](cases/discovery-shiv/comparison-manifest.json).

Coverage and attribution: the cases exercise complete repair, preservation, search/triage and reporting. Semantic delivery can expose irrelevant inventory entries; moved-guide can expose redundant path totals. They do not separately establish the rewrite's new old/new-search collision handling, preservation of a distinct rationale/tradeoff, read-only proposal honesty, or local-change negative form. Observe new instructions when relevant but do not add criteria or scenarios mid-batch. Native discovery, composition and transfer remain outside the claim. These are exposed development cases; the rewrite's prior authoring exposure is not independently established, and no unexposed-author or held-out claim is made.
The [original triage rule](cases/skill-original/SKILL.md#procedure) and [candidate triage rule](cases/skill-candidate-comprehensive/SKILL.md#2-triage) retain materially the same false-positive/intentionally-stale boundary. This candidate does not address the disputed Shiv negative-assertion classification, so these twelve calls do not test a resolution of that ambiguity. A classification tie would be consistent with unchanged guidance, not evidence that the boundary is correct or settled. Keep the frozen rule for both versions and qualify its interpretation separately. A category-label difference alone cannot establish that the candidate fixes a demonstrated skill defect. Likewise, report semantic block/line-count disagreements separately from unambiguous arithmetic errors; P3 remains non-blocking and never changes a functional outcome.

Runtime: all twelve rows used full runner revision `d899a817108330c4dcba4007f3383294a87d2f9a` with capture-2/runtime-1. Codex CLI 0.154.0 at `/opt/homebrew/Caskroom/codex/0.154.0/bin/codex`, SHA-256 `4f85982624b3898c8991cb80c0981b2aa71070e3537046c9a95950318a95afcc`, and Homebrew Python 3.14.7 were checked before and after collection. No runtime amendment was needed. Requested model names expose no immutable model revision.
The approved planning allowance was **180 active minutes**: 30 for freeze/runtime/input verification, 30 for model waits, 60 for preservation and per-execution assessment, and 60 for aggregation/review/contingency. Actual comparison effort and forecast variance belong to Storage and accounting; the assessment records measured runner duration and evidence size. Billed dollar cost is not established. Only closure remains forecast.

Evidence: [attempt index](comprehensive-comparison-01-run-index.json) and [batch assessment](comprehensive-comparison-01-assessment.md). The index pins every manifest, invocation authority and canonical result; the assessment pins the accepted index revision. Reviewed inputs and applicability were committed and collection readiness passed before dispatch. Each complete raw bundle was retained and verified against its inventory before the next invocation, using the existing development primary and accepted single-host recovery risk. The assessment owns counts, patterns, costs and the recommendation; no separate comparison record is needed.

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

**SSR closing accounting (2026-09-17): 688 active minutes booked; 512 minutes (8 hours 32 minutes) remain under the 1,200-minute ceiling.**
This includes preparation, review and model/tool waits, excludes owner-wait, and retains prior conservative allowances. The closing booking adds four active minutes for findings, plan reconciliation, verification and publication, excluding owner-wait. The comparison session took 41 minutes, 139 minutes below its 180-minute allowance. Measured model wait was 16.1 minutes against 30 forecast; the other preparation/preservation/assessment/review categories were not separately timed. The historical internal category split was not separately timed.
This closed-study checkpoint uses its then-approved ceilings: 40 subject, 12 evaluator, 4 authoring and 4 retry invocations. Preserve it as historical accounting; the [CW protocol](../concise-writing/protocol.md#storage-and-accounting) owns subsequent combined spending and the later ceiling increase. This avoids comparing SSR’s closing balance with a later study’s allocation.
Dispatched calls are **30 subject, 0 evaluator, 0 authoring, 0 retry**; remaining outer capacity is **10 / 12 / 4 / 4**. Core-baseline-01 has no unspent calls; neither excluded attempt has replacement authorization. Remaining capacity is a ceiling, not a selected next batch.


Remaining selected SSR work:

| Work | Estimate | Basis |
|---|---:|---|
| **Total** | **0** | Selected study closed; no further work selected. |

Closure is complete within its 30-minute allowance; no new collection or rollout follows. Future studies and model/effort experiments need their own scope and forecast; unused capacity is not automatically transferred.


## Results and decision

| Evidence | Interpretation |
|---|---|
| [Comprehensive comparison](comprehensive-comparison-01-assessment.md) | Complete twelve-execution comparison: tested functional outcomes preserved by both versions; reporting differences are mixed. Including the measured size reduction, the advisory recommendation favors the candidate. Owner deferred adoption. |
| [Core-baseline-01 assessment](core-baseline-01-assessment.md) | Selected three-case baseline complete: twelve attempts, ten included and two setup exclusions; descriptive outcomes and runtime differences remain explicit. |
| [Semantic-delivery-01 assessment](semantic-delivery-01-assessment.md) | First measured batch: original completes committed reconciliation; control leaves two current claims stale. One observation per condition; no consistency claim. |
| [Pilot 01 report](pilot-results.md), [attempt index](pilot-run-index.json), [checks](pilot-checks.json) | Historical original/control development pair; assessment correction and limits belong in the report. |
| [Pilot 02 report](pilot-02-results.md), [attempt index](pilot-02-run-index.json), [checks](pilot-02-checks.json) | Historical moved-guide pair; retained evidence supports the recorded outcomes, not a stable reliability estimate. |
| [Policy-3 worked example](assessments/pilot-02-original-policy-3-example.json), [identity/schema index](assessments/index.json) | Unchanged illustrative assessment of retained evidence, not a new execution or replacement of the canonical policy-2 result. |

Owner disposition: close the selected SSR study and defer adoption until later studies and experiments have informed finalization. Preserve both tested versions and their evidence; choosing a version is not a prerequisite for the second study. The assessment’s recommendation favors the smaller candidate, but it authorizes no rollout.
Both assessments separate unresolved Shiv category attribution from clear counting errors. Fixed-rule P3 totals do not establish that every mismatch is a skill defect; no criterion amendment or reassessment is authorized.
Batch assessments own aggregate counts, patterns, limitations and any version comparison; this section records the owner's resulting decisions by reference.
The owner suggested the existing SSR rewrite on `docs/comprehensive-skill-cleanup` as a possible comparison candidate. Inspected source: `skills/sweeping-stale-references/SKILL.md` at Git `13599fb7d3127334b0d07bfe468767e586ec5f9c`, SHA-256 `15992341f7ab2fb1e4d8a775092199d7d4e6a9de1167895dbe5a805aeafbd38c`; the clean local worktree contains those bytes. It removes the aggregate-inventory worked example and adds semantic-search, old/new-search and rationale/reporting guidance. Treat this as a whole-version candidate, not an isolated accounting intervention. The owner approved this candidate and the twelve-execution comparison on 2026-09-17; adoption is deferred. Reuse of these bytes does not resume the superseded comprehensive-rewrite workflow or import its tests/results as authority. Use the current fixed cases and a contemporaneous original condition for a relative-performance claim; assess candidate-only obligations and exposure limitations before claiming broader coverage.
The owner approved the [tooling proposal](../../plans/specs/2026-09-16-study-document-tooling.md) in the current session on 2026-09-16, including the provisional 120-minute implementation / 60-minute verification allowance. Implementation and qualification are complete; the active plan records verification. No skill edit or model collection was included.
Before authoring, re-read the selected writing-skills guidance and reconcile it with the evidence-supported objective. A passing control is useful evidence; resolve any pure-cleanup/RED conflict without manufacturing failure or resuming the abandoned wording campaign.
Compare the exact candidate with contemporaneous original executions under declared conditions; add a contemporaneous no-target condition only for a current contribution claim.
Any later adoption decision must retain the comparison’s limitations; an aggregate improvement cannot conceal a consequential regression.


### Findings and process lessons

The first study exercised the complete session workflow on one skill and two versions. Its [core baseline](core-baseline-01-assessment.md) retains ten valid observations and two charged setup exclusions; its [comparison](comprehensive-comparison-01-assessment.md) has twelve valid executions. Both versions meet every tested functional criterion in both repetitions per case. Reporting differences are mixed, and the candidate is 21.9% shorter by the agreed word-count measure. Detailed counts and attribution belong in those assessments.

All thirty subject calls used Sol-low. Small exposed cases, shared assessor context, unresolved accounting-unit/category interpretation and untested behavior limit the findings. They establish neither population reliability, held-out transfer, another model/effort’s performance nor generality to a second skill. No new rewrite was authored: the owner-selected existing candidate was tested exactly. The broader skill-testing journey remains open.

- Keep fixed cases and criteria, explicit valid alternatives, per-execution evidence and one aggregate assessment. They expose failures and uncertainty without a separate comparison record or mandatory evaluator campaign.
- Treat setup evidence as a prerequisite for inclusion. Missing full skill-read capture and the wrong Python runtime caused two exclusions; the capture/runtime repairs enabled the later twelve-execution comparison without replacements. Reuse the qualified path and check changed dependencies rather than repeating all qualification for every edit.
- Keep outcome success separate from procedural conformance and from attribution. The Shiv label dispute and semantic counting-unit mismatches show that a frozen criterion can produce a reproducible outcome without establishing a skill defect. Resolve such ambiguity before a future experiment relies on it; do not silently rescore this one.
- Use the accepted generator/validator for structure and identity checks, with semantic judgment in the active session. Keep one canonical repository record and one verified raw bundle per attempt; Git supplies record history, not recovery of external bundles. The accepted single-host evidence-loss risk remains.
- Keep documents subordinate to the testing spec. The format work drifted into separate design problems, duplicated history and unnecessary evaluator/comparison layers; subsequent simplification restored the session workflow. Reuse these formats for the second skill and change them only for an observed representational gap.
- Include simplification when interpreting a version comparison. The initial retain recommendation overlooked a measured size benefit already allowed by the spec. Word count is sufficient; smaller text does not excuse functional regression or prove token/cost savings.
- Separate evidence completion from deployment. Closing with adoption deferred preserves the findings and permits the next study without forcing a winner or another collection cycle.

The next learning question is whether the workflow works for a contrasting skill. Candidate selection and subsequent Claude/effort experiment planning belong in the active plan; none is an authorized SSR continuation.
