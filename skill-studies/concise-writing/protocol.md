# Concise writing: study protocol

Format version: `1`
Study ID: `concise-writing`
Status: all 120 expanded CW calls are retained and assessed, with three repetitions per selected scenario/condition/provider. Coverage acceptance, editing-base selection and adoption remain owner decisions.
Current action: CW remains the first end-to-end study, followed by SSR.
The owner accepted the scenario designs C, N1–N4 and revised E during the walkthrough, retained A/B, and removed tailored skill-editing/compression tests.
The owner-requested [preparation review and remediation](../../reviews/2026-09-27-cw-suite-preparation-review.md) are complete.
On 2026-09-27, the owner replied “approved, please continue” to the 104-call proposal: 72 ordinary calls followed by 32 native calls, raising the combined subject ceiling from 136 to 240.
This authorizes both stages, runtime qualification, committed input/schedule freeze and collection after readiness, with zero automatic retries; it does not authorize a skill edit or adoption.
The [preparation package](preparation/README.md) and [allocation forecast](testing-audit.md#proposed-sequence-and-allocation-forecast) define the approved scope.
Current decision: review the complete cross-provider baselines and accept or revise the stated coverage limits before selecting an editing base. Supplemental spending is 16/16; no further subject calls are authorized.
The owner clarified that three repetitions are the minimum and authorized the sixteen missing calls: “yeah, go ahead and make those. 2 is definitely not enough. I am pretty sure 3 is what we decided as a our minimum”.
This raises combined subject capacity from 240 to 256 and the expanded CW scope from 104 to 120 calls.
Three repetitions now apply to every selected CW scenario/condition/provider; this is a diagnostic minimum, not a reliability threshold or a replacement for the later fresh-wording authoring requirements.
The sixteen-attempt native indexes and assessments remain immutable batch records; the two eight-call supplements identify repetition 3 and support the combined summary below.
The supplement used the same qualified CLI binaries, models, low effort, inputs, skills and CW-expanded-1 rules, with identity checks before dispatch.
The third repetition reversed the second rotation's condition order; an odd number cannot fully balance two-condition order.
No automatic retries, replacements, new skill edits or adoption are authorized.
The initial sixteen manifests pin input revision `96b6e383da39ea807a6ad49d4513cfc1d6f4cd33`; eight supplemental manifests pin `b167a70bd26a03543407d9bae208d78b13432f2b`.
Both runtimes passed qualification and all six expanded batches passed readiness before dispatch.
Every attempt records the committed manifest, invocation authority and runner revision.
Establish and assess both providers' baselines before selecting CW edits; the existing rewrite remains an unchanged comparison condition.
Plan: [active plan](../../plans/2026-09-11-model-driven-skill-testing.md#current-next-action)
General spec: [testing framework](../../plans/specs/2026-09-11-model-driven-skill-testing-framework.md)

## Sources and intended use

Original: [checked-in skill](../../skills/concise-writing/SKILL.md), preserved as [study original](cases/skill-original/SKILL.md), from Git `99b3302f047a9b000ff804292d8746dd8bf43e42`, SHA-256 `4d12a2eb475c6b2ef57e2300c8c07af3f59c1e07b2b82695a3b7669eee1d6d72`. Complete supplied text: 860 words by `wc -w`.
Read the complete skill and its [composition map](../../ARCHITECTURE.md#composition-boundaries); relevant rationale and plan-writing companions were inspected for scope. The original snapshot matches its source bytes; it is not a new skill version.

Owner’s intended use: turn existing agent output that is verbose or voluminous into concise, clear, effective material that is easier for the owner to consume. The expanded batches cover ordinary editing, document additions, new updates, code comments and native selection. This contrasts with SSR’s repository repairs and tests semantic assessment through the same session workflow.
Historical batches covered standalone prose editing only. Expanded results add the selected document and invocation cases; they do not validate skill/reference authoring, plan/spec composition, new decision-rationale generation, anchor changes or full orchestration.
Tailored skill-editing tests were removed during suite review; those edits remain supervised and paired with writing-skills. Existing rationale in supplied prose must still survive.
Old CW frameworks, fixtures, rubrics and results remain superseded and were not used to define this contract. Historical reuse, if later selected, requires revalidation under the current spec.

## Behavioral contract and consumers

Owner scope clarification: CW is intended for text generally, including code comments; references to “prose” do not restrict it to standalone documents.
Writing or editing comments is in scope; N3’s numeric-only task leaves all wording unchanged and therefore does not exercise comment editing.

Owner clarification: concision must maintain document effectiveness. Repetition is acceptable when it reinforces important points; meaningful additional prose is acceptable when it contributes explanation, emphasis or comprehension. The target is avoidable burden, not the shortest wording or minimum repetition. This agrees with the skill’s protection of useful framing and deliberate reinforcement. Readability is an intended outcome, not just a preservation check. If the input is difficult to read or poorly organized, the edit should make it easier to follow. Existing formatting, layout, section order and paragraph boundaries are not preservation requirements; improve them where they contribute to the difficulty. This owner-resolved target makes the skill’s usability goal explicit, not evidence that its original wording teaches a particular restructuring procedure. Assess an F3 miss against that agreed target; any later added teaching technique must be described as new instruction, without claiming it was already in the original. Preserve information and the useful effects of framing and emphasis, not their exact original presentation.

| ID | Source / obligation | Intended outcome and observable evidence |
|---|---|---|
| O1 | Core test; When NOT to cut: preserve information and necessary framing. | Final document preserves facts, qualifications, causal relationships, rationale and the useful effects of orientation, emphasis and reinforcement. Compare meaning and communicative function across the complete source and final artifact; wording, layout and placement may change. Useful repetition may remain or be expressed differently. |
| O2 | Verbosity patterns; local/global compression: remove padding at sentence and document level. | Remove wording or duplication only where its lack of useful contribution is supported by the document’s purpose and context. Evaluate the complete document’s concision without requiring every phrase to be the shortest possible. Meaningful prose and useful repetition may remain; the amount cut does not establish success. |
| O3 | Skill-supported goal: a rich, easy-to-read, complete document, with good structure. Owner-resolved target: improve difficult organization; the original does not prescribe a reordering procedure or decision-first layout. | The edit makes poorly organized or hard-to-follow input easier to consume while preserving already effective material. Readers can follow the reasoning and sequence, find important points and use the document without reconstructing missing connections. Reordering, grouping, headings, paragraphs, lists or explanatory transitions are available means, not required formats. Judge the result for the stated reader and purpose. |
| O4 | Compression pass; editing instructions: review locally and globally, draft first, then diff against the original. | Observed drafting and comparison against the original support the prescribed process. No separate intermediate file, three-artifact workflow or particular diff tool is required by the skill. A polished final artifact or claim of review alone does not prove the actions occurred; evidence requirements must be fixed before collection. |
| O5 | When unsure: keep potentially necessary framing and flag the uncertainty. | Where the editor remains unsure whether material is useful framing or padding, it keeps the material and flags that uncertainty. Context may resolve ambiguity; a difficult case alone does not prove the editor was unsure or require a warning. Do not infer a hidden mental state from silence. |

Consumers: the owner needs agent output that is easier to consume without loss of meaning or usefulness; the editor/reviewer uses the source-to-draft comparison to check losses. No exact output schema or downstream program consumer was identified in the inspected CW, DD, adversarial-review, rationale and plan-writing skills, architecture/README, example guidance, command directory and hook references. DD and review guidance invoke CW but do not prescribe a parser for its edited prose. This inspection does not establish that no external consumer exists. Any real case-specific interface or link dependency must be stated explicitly; do not invent layout-preservation rules for ordinary prose.
Owner decisions: select CW, govern concision by document effectiveness as clarified above, and judge the work on its own merits. Process-only defects do not overturn a successful artifact outcome. Historical case boundaries and completed collection scopes are approved and frozen by their linked manifests.
Scenario acceptance and current dispatch authority are recorded only at the top of this protocol; the expanded batches below identify the new collection inputs.

## Assessment policy

Owner clarification, 2026-09-18: correctness, comparative effectiveness and readability determine pass/fail. Shorter is preferred, unchanged is acceptable, and longer is flagged without automatically failing.
Owner-approved review resolution: F3 explicitly includes unnecessary consumption burden; F2 retains comparison with the source for the stated reader’s purpose. Length remains a separate preference/flag and process remains unscored.
The completed reassessment applied this revised contract to the same eight retained outputs without new model calls, subject-input changes or a skill edit.
Original collection manifests retain the actual frozen collection context; the [recommendation](cases/agent-recommendation/assessment-manifest.json) and [briefing](cases/effective-briefing/assessment-manifest.json) reassessment manifests preserve those exact subject-input identities and identify the new rules.
Git preserves prior policy and result versions. The [qualification examples](qualification.md) have been re-judged under policy 4; they are controller-only boundary checks, not observed executions.

Policy identity: **CW-assessment-4**. The [controller policy copy](assessment-policy.txt) derives verbatim from the following subsection body, excluding its heading.
The protocol owns the policy; verify body/copy equality when freezing assessment inputs.

### Current CW assessment policy

Assess the complete delivered document against the complete source for its intended reader and purpose. Score exactly three functional factors: F1, the entire output remains correct; F2, it serves the intended reader’s purpose at least as effectively as the original; F3, it is readable and easy to understand. All three are required for an overall pass. Report length separately: shorter is preferred, the same length is acceptable, and longer receives a visible flag rather than an automatic failure.
Correctness and comparative effectiveness are the primary gates. If either fails, concision has been achieved at the expense of a usable, faithful document and the execution fails regardless of readability or length reduction. Do not average scores or reward greater compression to offset any failed factor.
Evaluate meaning, evidence, qualifications, reasoning and the reader’s ability to decide and act across the whole document. A changed, absent or repeated sentence is a reason to inspect context, not an independent deduction. Explain any loss of correctness or effectiveness in terms of what the complete edit communicates or enables compared with the complete source. Accept equivalent wording, relocated information, consolidated framing and useful repetition. Do not impose a preferred layout, sentence checklist or separate absence-of-padding score.
Judge readability from the complete document’s organization, connections and consumption burden for its intended reader. Merely being possible to follow is insufficient: residual padding, purposeless restatement or digression fails F3 when it makes the whole document unnecessarily difficult or laborious to consume. Explain the reader consequence in context rather than counting repeated statements, sections or words. Repetition that improves orientation, emphasis or action remains useful, not padding; the rule does not require the shortest possible phrasing. Measure length with the same wc -w command on the complete source and delivered Markdown files, including headings and list markers. Record source/output counts, the signed change and whether the output is shorter, unchanged or longer. Flag every longer output for consideration alongside its correctness, effectiveness and readability; useful added explanation may be justified. Length alone cannot establish a pass or failure, and no minimum reduction, compression bonus or automatic shorter-output tie-breaker applies. Unknown length is reported as unavailable rather than inferred; it does not by itself invalidate assessable F1–F3 outcomes.
Editing process is unscored. Traces may establish setup or explain observations, but process compliance cannot add or remove an outcome pass. Missing process evidence does not establish a skipped step. Score the saved document, not an unsaved edit or completion claim. Resolve missing capture as setup uncertainty; do not infer an empty document from missing evidence.
Record each factor as met, not met or insufficient evidence. Any failed factor gives an overall failure; otherwise any unknown gives insufficient evidence; otherwise all three met gives a pass. Aggregate counts by case, condition and factor across all valid setups, with exclusions separate. These small development samples are descriptive; no population reliability threshold, independent evaluation or causal contribution claim follows from the counts.
For comparisons, report evidence-backed differences in effectiveness and readability separately from the categorical pass/fail outcomes and length observation. Two passing documents can differ in quality; a tie in pass counts establishes only equal threshold outcomes, not equal quality. Do not invent a failure, award a shorter-output win automatically, or infer a reliable skill advantage from these small development samples. Use the same frozen policy for future authorized rewrite comparisons; any amendment must be explicit and applied consistently to compared outputs.

## Suite and evidence

Selected coverage maps to the skill’s named patterns below. These are contextual evidence targets, not eleven independent tests or fixed instructions to delete/retain particular sentences. The unit of judgment remains the complete document under O1–O3; improving layout and readability must also be assessed. The linked case cards ground expected effects and valid alternatives in their source, audience and task; A/B are owner-accepted and frozen by their historical manifests; expanded collection inputs use the provider-specific manifests below.

| Skill pattern / category | Selected coverage and discriminating evidence |
|---|---|
| Meta-framing | A: remove narration that contributes nothing, while preserving a genuinely orienting introduction. |
| Say-it-twice | A: consolidate adjacent restatement with no added purpose; contrast with useful reinforcement in the same document. |
| Cross-section duplication | A: reconcile a repeated explanation across separated sections, with no distinct reader need for two copies. A sentence-only cleanup must leave an identifiable whole-document defect. |
| Over-sectioning | A: improve fragmented headings/lead-ins and reading order; permit multiple effective layouts. |
| Unrequested elaboration | A: distinguish unrequested advice/speculation from supplied facts and useful explanation; do not introduce unsupported elaboration or remove decision-relevant information. |
| Emphasis/hedge inflation | A: reduce empty emphasis and inflated qualifiers without weakening real uncertainty or important warnings. |
| Closing recaps / navigation | B covers a short decision recap; collected C covers separate operational entry points and useful warnings. Seven Claude C outputs retain a detached duplicate mechanism section and fail F3; useful repeated safeguards are accepted. |
| Deliberate repetition | A and B: preserve reinforcement where a key point is useful in two reading contexts; do not demand identical wording or placement. |
| Orienting context | A and B: preserve the connections a reader needs to follow the argument or sequence. |
| Rationale | A and B: preserve supplied reasons and trade-offs; no requirement to invent a new decision rationale. |
| Spec/plan completeness | Untested; defer full plan/spec composition. Collected C/E exercise supplied requirements, not the full composition workflow. Revisit before claiming the lean-plan-writing interaction or changing that pairing. |
| Draft and local/global comparison (O4) | Unscored; retained traces record observed draft/comparison actions separately from F1–F3; absent trace evidence is unknown, not noncompliance. No particular diff tool or extra file is mandatory. |
| Uncertainty handling (O5) | No qualifying observed uncertainty established. C includes an underexplained repeated warning, but difficulty or silence cannot establish an O5 opportunity. Keep-and-flag effectiveness remains unmeasured. |
| Pressure and restraint | B exercises restraint; collected C adds a handoff deadline and prior line-level cleanup. Codex skill outputs preserve rationale lost by two controls; most Claude outputs preserve facts but retain unnecessary repetition. No percentage-cut requirement applies. |
| Native invocation and new prose | Three-repetition N1/N2/N4: timely positive loads are 9/9 per version on Codex, 6/9 original and 5/9 rewrite on Claude. N3 has two Codex rewrite over-triggers in three attempts; every other negative avoids loading. Task outcomes are separate; see the combined native table below. |
| Claude and current runtime | Collected 60 calls per provider on qualified Codex 0.157.1/Sol-low and Claude 2.1.283/Sonnet-low. Historical runtimes remain separate; all 120 setups are valid and retained. |
| Adding to an existing document | Collected E tests complete integration against source plus new notes. Contact recording is lost in one original output per provider and all three Claude rewrite outputs; every control retains it. A/B/C revise without supplied additions; N2 creates a new document. |
| Code-comment writing/editing | Collected N4: all twelve comment artifacts meet F1–F3 and executable-token/syntax checks. Codex loads 3/3 per version; Claude original loads 1/3 and rewrite 0/3. N3 tests the separate comments-untouched selection boundary. |
| Response-only/detailed-response boundary | Untested. Defer a separate response-only stratum; the rewrite changes this trigger boundary, so resolve intended applicability and test it before adopting that description. |
| Anchor changes and full orchestration | Untested. Defer SSR anchor repair and DD orchestration because they add separate skills and attribution questions; revisit before changing those relationships. |

A/B and the six expanded cases use constructed development fixtures, not retained real-world agent outputs. Their current criterion cards apply three whole-document factors and record length separately. The [worked examples](qualification.md) demonstrate current pass/fail boundaries; they are neither independent validation nor model observations.

| Case ID / definition | Membership | Covered obligations | Exposure | Limits |
|---|---|---|---|---|
| A: [agent-recommendation](cases/agent-recommendation/assessment.md) | completed; retain | O1–O3 assessed; O4/O5 unscored | development | Reader needs the recommendation, reasons, caveats and next action. Include both purposeless restatement and useful reinforcement, plus separated duplication and a real structural difficulty. Cover other cut patterns only where they fit naturally. |
| B: [effective-briefing](cases/effective-briefing/assessment.md) | completed; retain | O1–O3 assessed; O4/O5 unscored | development | Useful context, explanation and repetition must not be damaged by unnecessary compression. An edit must retain the source’s effectiveness; unchanged length is acceptable and increased length is flagged. |

The additions below have completed observations linked in Results; [inputs, criteria and configurations](preparation/README.md) and provider-specific manifests identify the collection freeze.
The [audit](testing-audit.md#proposed-sequence-and-allocation-forecast) gives their sequence, evidence requirements and allocation forecast.

| Expanded case | Distinct failure opportunity | Required evidence / boundary |
| --- | --- | --- |
| C: [long operational handoff](cases/long-handoff/assessment.md) | A prior local cleanup still leaves scattered duplication; a deadline encourages deleting a warning repeated where different readers enter the procedure. | Whole-document F1–F3, lookups/action branches, conditional uncertainty observation, and process traces. Keep operational requirements and rationale; no mandatory reduction. |
| N1: [natural tightening](cases/invocation-tighten/assessment.md) | Reuse A without naming CW or directing a skill read; the model may edit successfully while skipping discovery. | Catalog/description delivery and full-body load timing, with A's outcome assessed separately. |
| N2: [produce a durable update](cases/invocation-write/assessment.md) | Turn factual notes into a reader-facing update without saying tighten/concise; the model may miss the writing trigger. | Frozen source-supported content and reader purpose, native load before prose production; no hidden style instruction in the task. |
| N3: [adjacent non-prose edit](cases/invocation-nonprose/assessment.md) | Change a numeric setting beside explanatory comments; file proximity may prompt unnecessary CW loading or prose changes. | Invocation boundary and authorized edit only; exclude negative task scores from functional CW counts. |
| N4: [write useful code comments](cases/invocation-comments/assessment.md) | The task names no CW or concision cue; the agent may miss comment applicability, narrate obvious code or lose a consequential retry boundary. | Native body-load timing, comments assessed in code context against maintenance notes, and unchanged executable tokens/behavior. |
| E: [integrate a document addition](cases/document-addition/assessment.md) | New notes partly overlap an existing briefing; blind append or over-deduplication can scatter requirements or lose a distinct condition. | Complete source/notes/output comparison with prospective F1–F3; preserve useful reinforcement, allow justified growth and alternative layouts. |

The case cards describe each reader’s decision and purpose, without independently scoring source passages.
Retained evidence includes complete source and output files and available execution traces.
Ordinary editing cards score F1–F3 and report length separately; O4–O5 remain unscored process context.
Native cards separate invocation from task quality; N2 has prospective generation criteria, N4 has comment-editing criteria and N3 measures no functional CW outcome.
E assesses the expanded document against its source and authorized additions; it does not use downstream agent tests.
The [qualification record](qualification.md) evaluates six existing edits and two unchanged source controls under policy 4, including harmful over-trimming and a readable-but-laborious edit.
The historical reassessment used the same saved evidence; the aggregate checker uses result-pinned assessment rules.
Historical configurations and collection manifests below preserve the actual supplied inputs; those completed batches made no composition, discovery or held-out claim.

## Expanded-suite assessment policy

Policy identity: **CW-expanded-1**, selected for the expanded collection; its [controller copy](preparation/assessment-policy.txt) also includes unchanged CW-assessment-4.
It makes the case-specific rules explicit without changing CW-assessment-4, its controller copy, historical cards or retained scores.
Freeze this section and the exact case-card revisions together before any new assessment.

| Cases | Functional judgment and length treatment | Invocation |
| --- | --- | --- |
| A/B/C and native N1 | Apply CW-assessment-4 F1–F3 unchanged to the complete source/output for its purpose. Record complete-document word counts and the existing length preference/flag. | N1 also has D1; explicit-load A/B/C use full delivery as setup, not native-selection evidence. |
| E: document additions | Use E's prospective F1–F3 against the source plus authorized new notes. Report source, added-note and output counts separately; required additions can justify growth, with no shortening preference. | Explicit load is setup. |
| N2: new report | Use N2's prospective F1–F3 against all supplied facts and the manager's stated purpose. Notes/report lengths are descriptive because they serve different roles. | D1 measures timely native loading. |
| N4: code comments | Use N4's prospective F1–F3 on comments together with unchanged executable code, against the maintenance notes. Code may convey obvious facts; comments must retain needed rationale. Report comment-only length descriptively. | D1 measures timely native loading. |
| N3: numeric-only edit | Functional CW outcome is not measured. Record numeric-edit and literal-reply errors as task observations, outside functional counts. Length is not applicable. | D1 measures avoiding CW loading; catalog/description exposure alone is not a body load. |

Each applicable factor is met, not met or insufficient evidence under its frozen case card.
For F1–F3 cases, any failed factor gives functional failure; otherwise any unresolved factor gives insufficient evidence; all three met gives functional pass.
Invocation has its own result and denominator; neither successful text nor a successful load substitutes for the other.
A qualified native miss remains an observation, not a setup exclusion, and its artifact is assessed under the same case criteria.
Unavailable skills, contamination or missing capture remain setup/evidence questions, with all started attempts retained and no selective replacement.
O4/O5 remain unscored process observations, and missing trace evidence is not proof of a skipped step or hidden uncertainty.

Report outcomes by case, provider, available condition and repetition; preserve explicit-load/native, editing/addition/generation/comment and negative-task distinctions.
Do not pool historical runtime observations into new counts or infer a CW contribution from native cases without a no-CW condition.
Compare complete artifacts for quality differences as well as factor results; no word-count win, averaged score or small-sample reliability threshold overrides the fixed judgments.

## Execution scope and authorization

Owner selected CW, accepted the case design and task refinements, and approved the exact eight-execution scope plus single-host storage risk on 2026-09-17 (2026-09-18 UTC), replying “approved, however, I think we should probably continue on a fresh session” to the explicit approval request for both. Collection uses gpt-5.6-sol at low effort, with no automatic retries. The continuation completed input freeze and readiness before collection; the eight-call authorization is now spent. No skill edit or adoption is authorized. All eight baseline calls are spent; the separately authorized comparison below is also complete.

### Contribution baseline: contribution-baseline-01

Status: complete collection; all eight attempts assessed with valid setup, no retries or replacements.
Question: does the original CW guidance help produce effective concise edits compared with the same editing request without CW?
Scope: exactly eight sequential attempts, two cases × original/control × two repetitions, in the table order below. Reverse condition order in the second repetition and start the two cases with different conditions. This balances first/second position; it is not randomization or enough replication to establish a population reliability rate. Two repetitions permit a limited consistency check within the remaining capacity. A tie would establish no contribution advantage in these cases but could still inform whether the framework handles prose evidence; the study does not require a failing control or make a rewrite/adoption decision. One execution per cell would forgo this consistency check.
Acceptance/inclusion: descriptive-only. Include all valid-setup executions regardless of outcome; count met, not met and insufficient evidence separately per case/condition/criterion and functional result. Report invalid or unresolved setups and unattempted slots separately. No automatic retry or replacement. A successful control is useful evidence; do not manufacture a failure or pool cases to conceal differences.
Budget: approved maximum eight subject invocations, zero evaluator/authoring/retry invocations. Any started invocation costs one subject call even if it fails; an established pre-invocation failure costs zero calls but remains an attempted slot, without automatic replacement. Uncertain charges stop dispatch until resolved. The eight invocations brought combined subject spending to 38/40, leaving two. A later matching eight-call version comparison would require six more than the existing ceiling; no later comparison, Claude pass or effort benchmark is funded by this proposal.
Stop: preserve and verify each stopped bundle before the next dispatch. Stop for failed preservation, uncertain charge, suspected context contamination, an infrastructure/setup defect or a changed runtime/input identity requiring inspection. A valid behavioral failure alone does not stop the remaining rows. Stop after the eight scheduled attempts or at an outer ceiling, whichever comes first.

Settings: provider `codex`, model `gpt-5.6-sol`, effort `low`, permissions `workspace-write`, existing 900-second timeout. Both conditions get only `report.md`, `TASK.md` and the common [prompt wrapper](prompt-control.md); original additionally gets the preserved CW skill at `.agents/skills/concise-writing/SKILL.md` and the [read/apply instruction](prompt-original.md). No DD, companion skill, case criteria or examples are supplied. The ordinary tightening request is identical within each pair. It names the reader’s decision but omits preservation and restructuring advice, leaving the skill to supply that guidance. This tests contribution after explicit loading; it does not test native skill discovery. The skill’s availability is the condition difference, not a promise that control will fail.
The common baseline commit preserves the source for an actual comparison after editing; it is neutral setup, not a requirement to commit the edited result or evidence of CW process compliance. No separate draft/final files or specific diff tool are required. The task does not constrain layout and asks the subject to edit prose only, not perform the fictional operational actions.

Recorded working directory: `/Users/simon/work/personal/disciplined-development-skills`. Each completed table row used this exact command; the table does not authorize reruns:

```sh
TMPDIR=/private/tmp/cw-contribution-baseline-01 skill-validation/runner/.venv/bin/skilltest run CONFIG
```

Replace `CONFIG` only with the row’s value. The namespace has been created and checked as a real directory. Each command requires host permission for Codex app-server initialization; the subject still uses the runner’s unchanged workspace permission profile, disabled tool network, private profile and restricted shell environment. Provider/API access remains necessary to execute the model.

| Order | Case | Condition | Repetition | CONFIG |
|---:|---|---|---:|---|
| 1 | agent-recommendation | original | 1 | `skill-studies/concise-writing/cases/agent-recommendation/original.json` |
| 2 | agent-recommendation | control | 1 | `skill-studies/concise-writing/cases/agent-recommendation/control.json` |
| 3 | effective-briefing | control | 1 | `skill-studies/concise-writing/cases/effective-briefing/control.json` |
| 4 | effective-briefing | original | 1 | `skill-studies/concise-writing/cases/effective-briefing/original.json` |
| 5 | agent-recommendation | control | 2 | `skill-studies/concise-writing/cases/agent-recommendation/control.json` |
| 6 | agent-recommendation | original | 2 | `skill-studies/concise-writing/cases/agent-recommendation/original.json` |
| 7 | effective-briefing | original | 2 | `skill-studies/concise-writing/cases/effective-briefing/original.json` |
| 8 | effective-briefing | control | 2 | `skill-studies/concise-writing/cases/effective-briefing/control.json` |

Inputs: [recommendation manifest](cases/agent-recommendation/manifest.json) and [briefing manifest](cases/effective-briefing/manifest.json) freeze all 34 identities at full input commit `c19e408549bbafe76005f5cfc0b08f24d7c2bfc4`. Git retrieval and every hash passed; collection readiness passed for contribution-baseline-01. Policy/body equality and all four offline configuration/workspace checks passed again. The frozen manifests were committed before dispatch. Actual attempt records pin the invocation-authority protocol and full runner revision. The frozen protocol records approval and pre-freeze state; this live protocol owns current accounting. The original manifest revisions preserve policy-1 collection inputs. Current policy-4 case cards and re-judged qualification examples do not relabel what subjects received.
Runtime checked during preparation: full runner revision `e3c3a5c47a4ae3939ae9e7f7fdce667b3fe16166`; its runner tree is unchanged from SSR’s qualified `d899a817108330c4dcba4007f3383294a87d2f9a`. Codex CLI 0.154.0 resolves to `/opt/homebrew/Caskroom/codex/0.154.0/bin/codex`, SHA-256 `4f85982624b3898c8991cb80c0981b2aa71070e3537046c9a95950318a95afcc`; host Python is 3.14.7. Recheck these identities before collection and record the full approved runner revision; requested model names do not expose an immutable model revision.
Offline checks: all four configurations loaded and copied the exact declared files; paired common bytes/settings matched; prompt differences were limited to the CW instruction. Disposable Git baselines preserved each original document and exposed a subsequent edit in `git diff`. Generated provider arguments retain private-profile configuration flags, disabled tool network and the restricted PATH. No provider invocation was made. These checks reuse the [SSR execution qualification](../sweeping-stale-references/protocol.md#comparison-comprehensive-comparison-01) for the unchanged runtime; they do not prove new CW model behavior or exhaustive host read isolation.
Setup/evidence checks during collection: verify supplied hashes and the intended condition; in original, retained tool-response content must establish complete CW text exposure before editing. Match any `provider-session.jsonl` used as evidence to the stdout thread ID and fixture cwd, and verify its inventory hash; a filename or claimed read alone is insufficient. Inspect retained guidance for contamination and final `report.md` for artifact quality. Unexpected/missing exposure or unusable capture is a setup issue requiring inspection, not a failed CW criterion. Drafting/comparison and local/global review remain unscored observations under policy 4. Keep the complete raw trace, even when it does not establish those steps.
Evidence/index: [attempt index](contribution-baseline-01-run-index.json) records all eight actual attempts, their authority/manifest pins, charges, verified complete bundles and canonical execution results. All eight have valid setup. The [batch assessment](contribution-baseline-01-assessment.md) reconciles all results; no provider calls remain authorized by this batch.

### Comparison: comprehensive-comparison-01

Status: complete; eight valid attempts, no retries or replacements. The owner directed proceeding with the existing comprehensive rewrite and explicitly prohibited changing coverage based on that rewrite.
The two cases, source documents, tasks, prompts, qualification examples and CW-assessment-4 remain the baseline. Candidate inspection must not feed new scenarios or scoring requirements into this comparison.

Candidate: [exact comprehensive snapshot](cases/skill-candidate-comprehensive/SKILL.md), from `docs/comprehensive-skill-cleanup` at Git `13599fb7d3127334b0d07bfe468767e586ec5f9c`, path `skills/concise-writing/SKILL.md`, SHA-256 `f763b43e88c56d6fdc2a96457bc2415cba60b75a1e7cb59cd1b0ebaa3fb199ba`.
Its complete supplied text is 665 words versus the original's 860 (195 fewer, 22.7%). This measures instruction size, not output quality.
Use this whole existing version unchanged; no new authoring or deployment is selected. Reading `writing-skills` informs verification, but its failing-control authoring loop does not justify manufacturing a failure or changing this fixed suite. This comparison exercises testing an existing edit; it does not exercise fresh evidence-led authoring.

Question: on the same two ordinary prose-editing tasks, does this candidate preserve correctness, effectiveness and readability, and what useful differences appear relative to fresh original-skill executions?
Apply F1–F3 unchanged to both versions, with length separate and evidence-backed comparative observations as policy 4 requires. Threshold ties do not prove equal quality; shorter skill or output text does not automatically win.
This is a whole-version development comparison with the same active-session assessor, not blinded or independent validation. Candidate scope changes outside these cases remain untested; they neither expand coverage nor alter judgments here.

Scope: eight sequential attempts, two cases × original/candidate-comprehensive × two repetitions. Original configurations are reused exactly. Candidate configurations differ only in test ID and the supplied skill source; the mounted path, prompt, source/task bytes and execution settings match.
Use `codex`, `gpt-5.6-sol`, low effort, workspace-write and the existing 900-second timeout. Fresh original runs control for current execution conditions; the previous original/control baseline remains separate and unchanged. No new no-skill control is needed for this version-comparison question.
Include all valid-setup executions regardless of outcome; report setup exclusions and unattempted slots separately. No automatic retry or replacement. Stop for uncertain charges, input/runtime drift, contamination, setup defects or preservation failures; a valid behavioral failure alone does not stop the schedule.

| Order | Case | Condition | Repetition | CONFIG |
|---:|---|---|---:|---|
| 1 | agent-recommendation | original | 1 | `skill-studies/concise-writing/cases/agent-recommendation/original.json` |
| 2 | agent-recommendation | candidate-comprehensive | 1 | `skill-studies/concise-writing/cases/agent-recommendation/candidate-comprehensive.json` |
| 3 | effective-briefing | candidate-comprehensive | 1 | `skill-studies/concise-writing/cases/effective-briefing/candidate-comprehensive.json` |
| 4 | effective-briefing | original | 1 | `skill-studies/concise-writing/cases/effective-briefing/original.json` |
| 5 | agent-recommendation | candidate-comprehensive | 2 | `skill-studies/concise-writing/cases/agent-recommendation/candidate-comprehensive.json` |
| 6 | agent-recommendation | original | 2 | `skill-studies/concise-writing/cases/agent-recommendation/original.json` |
| 7 | effective-briefing | original | 2 | `skill-studies/concise-writing/cases/effective-briefing/original.json` |
| 8 | effective-briefing | candidate-comprehensive | 2 | `skill-studies/concise-writing/cases/effective-briefing/candidate-comprehensive.json` |

Command per row, from the repository root after approval and input freeze: `TMPDIR=/private/tmp/cw-comprehensive-comparison-01 skill-validation/runner/.venv/bin/skilltest run CONFIG`, substituting that row's CONFIG. Create the scratch parent before the first invocation.
Retain each complete stopped bundle in the existing canonical CW evidence directory with its unique run name and verified sibling inventory before starting the next row. Use the existing single-host arrangement and exposure/setup checks for both skill-bearing conditions. Record actual CLI/runtime identity on every attempt; investigate drift before attributing differences.

Approved budget: eight subject invocations, zero evaluator/authoring/retry invocations. Combined subject spending rose from 38 to 46, with the accepted subject ceiling raised from 40 to 46 (total call ceiling 60 to 66); other call ceilings and the 1,200-minute active-work ceiling remain unchanged. On 2026-09-18, in reply to the explicit eight-run and ceiling-increase question, the owner confirmed: “I approved all the necessary runs to complete this step”. This authorizes all eight rows and the necessary increase; no further confirmation is required.
The freeze extended criterion condition-applicability metadata to `candidate-comprehensive` without changing rule text. Existing collection/reassessment manifests and results remain untouched. Collection readiness and paired input parity passed before the first call.
Inputs: [recommendation comparison manifest](cases/agent-recommendation/comparison-manifest.json) and [briefing comparison manifest](cases/effective-briefing/comparison-manifest.json) pin the approved inputs at full Git revision `8eac215c81415f47b07ee3f8e4a8fd984bdca63c`. Collection readiness passed before dispatch.
Offline preparation verified exact candidate provenance and paired prompt/source/task/settings parity; baseline source, task, prompt, policy and example bytes are unchanged. Codex CLI 0.154.0 and its executable hash match baseline; runner execution code is unchanged. The invocation-authority commit is the full runner revision. Criterion definition 5 changes applicability/status metadata only; F1–F3 text remains policy 4.
Evidence/index: [comparison attempt index](comprehensive-comparison-01-run-index.json) records all eight charged attempts, verified bundles and pinned results. The [comparison assessment](comprehensive-comparison-01-assessment.md) reports 2/2 passes per case/version, qualitative tradeoffs and length separately. The candidate produced longer outputs than the original in all four pairs, but every output is shorter than its source, so no longer-output flags apply.
The comparison preserves tested quality without demonstrating an overall output-quality gain. The candidate passes the tested scope but combines behavior changes with cleanup: the [assessment](comprehensive-comparison-01-assessment.md#candidate-contract-changes) records O5 reporting removal, a narrower repetition exception, stricter explicitness and wider applicability. No revised target contract is accepted; retain the live original under the owner's deferred adoption decision. That completed comparison authorized no further scenario, model pass, authoring or adoption; see the opening for current preparation.


### Expanded collection: codex-expanded-01

Results: [completed ordinary Codex assessment](codex-expanded-01-assessment.md), based on the [current attempt index](codex-expanded-01-run-index.json).
Scope: 36 sequential attempts; codex, four ordinary tasks × three conditions × three repetitions.
Authority: included in the owner-approved 104-call allocation recorded at the top of this protocol.
Include all valid-setup executions regardless of outcome; report invalid/unresolved setup and unattempted slots separately.
No automatic retry or replacement.
Use CW-expanded-1 and the linked case cards; selection and task quality remain separate, with N3 functional CW outcomes unmeasured.
Stop for uncertain charges, contamination, input/runtime drift, unusable setup or preservation failure; a valid behavioral miss remains an observation.
Runtime and evidence controls: [expanded qualification](preparation/runtime-qualification.md).
Inputs: [codex-agent-recommendation-manifest](preparation/manifests/codex-agent-recommendation-manifest.json), [codex-effective-briefing-manifest](preparation/manifests/codex-effective-briefing-manifest.json), [codex-long-handoff-manifest](preparation/manifests/codex-long-handoff-manifest.json), [codex-document-addition-manifest](preparation/manifests/codex-document-addition-manifest.json).

| Order | Case | Condition | Repetition | CONFIG |
| ---: | --- | --- | ---: | --- |
| 1 | agent-recommendation | control | 1 | `skill-studies/concise-writing/preparation/configs/codex-agent-recommendation-control.json` |
| 2 | agent-recommendation | original | 1 | `skill-studies/concise-writing/preparation/configs/codex-agent-recommendation-original.json` |
| 3 | agent-recommendation | candidate-comprehensive | 1 | `skill-studies/concise-writing/preparation/configs/codex-agent-recommendation-candidate.json` |
| 4 | effective-briefing | original | 1 | `skill-studies/concise-writing/preparation/configs/codex-effective-briefing-original.json` |
| 5 | effective-briefing | candidate-comprehensive | 1 | `skill-studies/concise-writing/preparation/configs/codex-effective-briefing-candidate.json` |
| 6 | effective-briefing | control | 1 | `skill-studies/concise-writing/preparation/configs/codex-effective-briefing-control.json` |
| 7 | long-handoff | candidate-comprehensive | 1 | `skill-studies/concise-writing/preparation/configs/codex-long-handoff-candidate.json` |
| 8 | long-handoff | control | 1 | `skill-studies/concise-writing/preparation/configs/codex-long-handoff-control.json` |
| 9 | long-handoff | original | 1 | `skill-studies/concise-writing/preparation/configs/codex-long-handoff-original.json` |
| 10 | document-addition | control | 1 | `skill-studies/concise-writing/preparation/configs/codex-document-addition-control.json` |
| 11 | document-addition | original | 1 | `skill-studies/concise-writing/preparation/configs/codex-document-addition-original.json` |
| 12 | document-addition | candidate-comprehensive | 1 | `skill-studies/concise-writing/preparation/configs/codex-document-addition-candidate.json` |
| 13 | agent-recommendation | original | 2 | `skill-studies/concise-writing/preparation/configs/codex-agent-recommendation-original.json` |
| 14 | agent-recommendation | candidate-comprehensive | 2 | `skill-studies/concise-writing/preparation/configs/codex-agent-recommendation-candidate.json` |
| 15 | agent-recommendation | control | 2 | `skill-studies/concise-writing/preparation/configs/codex-agent-recommendation-control.json` |
| 16 | effective-briefing | candidate-comprehensive | 2 | `skill-studies/concise-writing/preparation/configs/codex-effective-briefing-candidate.json` |
| 17 | effective-briefing | control | 2 | `skill-studies/concise-writing/preparation/configs/codex-effective-briefing-control.json` |
| 18 | effective-briefing | original | 2 | `skill-studies/concise-writing/preparation/configs/codex-effective-briefing-original.json` |
| 19 | long-handoff | control | 2 | `skill-studies/concise-writing/preparation/configs/codex-long-handoff-control.json` |
| 20 | long-handoff | original | 2 | `skill-studies/concise-writing/preparation/configs/codex-long-handoff-original.json` |
| 21 | long-handoff | candidate-comprehensive | 2 | `skill-studies/concise-writing/preparation/configs/codex-long-handoff-candidate.json` |
| 22 | document-addition | original | 2 | `skill-studies/concise-writing/preparation/configs/codex-document-addition-original.json` |
| 23 | document-addition | candidate-comprehensive | 2 | `skill-studies/concise-writing/preparation/configs/codex-document-addition-candidate.json` |
| 24 | document-addition | control | 2 | `skill-studies/concise-writing/preparation/configs/codex-document-addition-control.json` |
| 25 | agent-recommendation | candidate-comprehensive | 3 | `skill-studies/concise-writing/preparation/configs/codex-agent-recommendation-candidate.json` |
| 26 | agent-recommendation | control | 3 | `skill-studies/concise-writing/preparation/configs/codex-agent-recommendation-control.json` |
| 27 | agent-recommendation | original | 3 | `skill-studies/concise-writing/preparation/configs/codex-agent-recommendation-original.json` |
| 28 | effective-briefing | control | 3 | `skill-studies/concise-writing/preparation/configs/codex-effective-briefing-control.json` |
| 29 | effective-briefing | original | 3 | `skill-studies/concise-writing/preparation/configs/codex-effective-briefing-original.json` |
| 30 | effective-briefing | candidate-comprehensive | 3 | `skill-studies/concise-writing/preparation/configs/codex-effective-briefing-candidate.json` |
| 31 | long-handoff | original | 3 | `skill-studies/concise-writing/preparation/configs/codex-long-handoff-original.json` |
| 32 | long-handoff | candidate-comprehensive | 3 | `skill-studies/concise-writing/preparation/configs/codex-long-handoff-candidate.json` |
| 33 | long-handoff | control | 3 | `skill-studies/concise-writing/preparation/configs/codex-long-handoff-control.json` |
| 34 | document-addition | candidate-comprehensive | 3 | `skill-studies/concise-writing/preparation/configs/codex-document-addition-candidate.json` |
| 35 | document-addition | control | 3 | `skill-studies/concise-writing/preparation/configs/codex-document-addition-control.json` |
| 36 | document-addition | original | 3 | `skill-studies/concise-writing/preparation/configs/codex-document-addition-original.json` |

### Expanded collection: claude-expanded-01

Results: [completed ordinary Claude assessment](claude-expanded-01-assessment.md), based on the [current attempt index](claude-expanded-01-run-index.json).
Scope: 36 sequential attempts; claude, four ordinary tasks × three conditions × three repetitions.
Authority: included in the owner-approved 104-call allocation recorded at the top of this protocol.
Include all valid-setup executions regardless of outcome; report invalid/unresolved setup and unattempted slots separately.
No automatic retry or replacement.
Use CW-expanded-1 and the linked case cards; selection and task quality remain separate, with N3 functional CW outcomes unmeasured.
Stop for uncertain charges, contamination, input/runtime drift, unusable setup or preservation failure; a valid behavioral miss remains an observation.
Runtime and evidence controls: [expanded qualification](preparation/runtime-qualification.md).
Inputs: [claude-agent-recommendation-manifest](preparation/manifests/claude-agent-recommendation-manifest.json), [claude-effective-briefing-manifest](preparation/manifests/claude-effective-briefing-manifest.json), [claude-long-handoff-manifest](preparation/manifests/claude-long-handoff-manifest.json), [claude-document-addition-manifest](preparation/manifests/claude-document-addition-manifest.json).

| Order | Case | Condition | Repetition | CONFIG |
| ---: | --- | --- | ---: | --- |
| 1 | agent-recommendation | control | 1 | `skill-studies/concise-writing/preparation/configs/claude-agent-recommendation-control.json` |
| 2 | agent-recommendation | original | 1 | `skill-studies/concise-writing/preparation/configs/claude-agent-recommendation-original.json` |
| 3 | agent-recommendation | candidate-comprehensive | 1 | `skill-studies/concise-writing/preparation/configs/claude-agent-recommendation-candidate.json` |
| 4 | effective-briefing | original | 1 | `skill-studies/concise-writing/preparation/configs/claude-effective-briefing-original.json` |
| 5 | effective-briefing | candidate-comprehensive | 1 | `skill-studies/concise-writing/preparation/configs/claude-effective-briefing-candidate.json` |
| 6 | effective-briefing | control | 1 | `skill-studies/concise-writing/preparation/configs/claude-effective-briefing-control.json` |
| 7 | long-handoff | candidate-comprehensive | 1 | `skill-studies/concise-writing/preparation/configs/claude-long-handoff-candidate.json` |
| 8 | long-handoff | control | 1 | `skill-studies/concise-writing/preparation/configs/claude-long-handoff-control.json` |
| 9 | long-handoff | original | 1 | `skill-studies/concise-writing/preparation/configs/claude-long-handoff-original.json` |
| 10 | document-addition | control | 1 | `skill-studies/concise-writing/preparation/configs/claude-document-addition-control.json` |
| 11 | document-addition | original | 1 | `skill-studies/concise-writing/preparation/configs/claude-document-addition-original.json` |
| 12 | document-addition | candidate-comprehensive | 1 | `skill-studies/concise-writing/preparation/configs/claude-document-addition-candidate.json` |
| 13 | agent-recommendation | original | 2 | `skill-studies/concise-writing/preparation/configs/claude-agent-recommendation-original.json` |
| 14 | agent-recommendation | candidate-comprehensive | 2 | `skill-studies/concise-writing/preparation/configs/claude-agent-recommendation-candidate.json` |
| 15 | agent-recommendation | control | 2 | `skill-studies/concise-writing/preparation/configs/claude-agent-recommendation-control.json` |
| 16 | effective-briefing | candidate-comprehensive | 2 | `skill-studies/concise-writing/preparation/configs/claude-effective-briefing-candidate.json` |
| 17 | effective-briefing | control | 2 | `skill-studies/concise-writing/preparation/configs/claude-effective-briefing-control.json` |
| 18 | effective-briefing | original | 2 | `skill-studies/concise-writing/preparation/configs/claude-effective-briefing-original.json` |
| 19 | long-handoff | control | 2 | `skill-studies/concise-writing/preparation/configs/claude-long-handoff-control.json` |
| 20 | long-handoff | original | 2 | `skill-studies/concise-writing/preparation/configs/claude-long-handoff-original.json` |
| 21 | long-handoff | candidate-comprehensive | 2 | `skill-studies/concise-writing/preparation/configs/claude-long-handoff-candidate.json` |
| 22 | document-addition | original | 2 | `skill-studies/concise-writing/preparation/configs/claude-document-addition-original.json` |
| 23 | document-addition | candidate-comprehensive | 2 | `skill-studies/concise-writing/preparation/configs/claude-document-addition-candidate.json` |
| 24 | document-addition | control | 2 | `skill-studies/concise-writing/preparation/configs/claude-document-addition-control.json` |
| 25 | agent-recommendation | candidate-comprehensive | 3 | `skill-studies/concise-writing/preparation/configs/claude-agent-recommendation-candidate.json` |
| 26 | agent-recommendation | control | 3 | `skill-studies/concise-writing/preparation/configs/claude-agent-recommendation-control.json` |
| 27 | agent-recommendation | original | 3 | `skill-studies/concise-writing/preparation/configs/claude-agent-recommendation-original.json` |
| 28 | effective-briefing | control | 3 | `skill-studies/concise-writing/preparation/configs/claude-effective-briefing-control.json` |
| 29 | effective-briefing | original | 3 | `skill-studies/concise-writing/preparation/configs/claude-effective-briefing-original.json` |
| 30 | effective-briefing | candidate-comprehensive | 3 | `skill-studies/concise-writing/preparation/configs/claude-effective-briefing-candidate.json` |
| 31 | long-handoff | original | 3 | `skill-studies/concise-writing/preparation/configs/claude-long-handoff-original.json` |
| 32 | long-handoff | candidate-comprehensive | 3 | `skill-studies/concise-writing/preparation/configs/claude-long-handoff-candidate.json` |
| 33 | long-handoff | control | 3 | `skill-studies/concise-writing/preparation/configs/claude-long-handoff-control.json` |
| 34 | document-addition | candidate-comprehensive | 3 | `skill-studies/concise-writing/preparation/configs/claude-document-addition-candidate.json` |
| 35 | document-addition | control | 3 | `skill-studies/concise-writing/preparation/configs/claude-document-addition-control.json` |
| 36 | document-addition | original | 3 | `skill-studies/concise-writing/preparation/configs/claude-document-addition-original.json` |

### Expanded collection: codex-invocation-01

Results: [completed native Codex assessment](codex-invocation-01-assessment.md), based on the [current attempt index](codex-invocation-01-run-index.json).

Scope: 16 sequential attempts; codex, four native tasks × two conditions × two repetitions.
Authority: included in the owner-approved 104-call allocation recorded at the top of this protocol.
Include all valid-setup executions regardless of outcome; report invalid/unresolved setup and unattempted slots separately.
No automatic retry or replacement.
Use CW-expanded-1 and the linked case cards; selection and task quality remain separate, with N3 functional CW outcomes unmeasured.
Stop for uncertain charges, contamination, input/runtime drift, unusable setup or preservation failure; a valid behavioral miss remains an observation.
Runtime and evidence controls: [expanded qualification](preparation/runtime-qualification.md).
Inputs: [codex-invocation-tighten-manifest](preparation/manifests/codex-invocation-tighten-manifest.json), [codex-invocation-write-manifest](preparation/manifests/codex-invocation-write-manifest.json), [codex-invocation-nonprose-manifest](preparation/manifests/codex-invocation-nonprose-manifest.json), [codex-invocation-comments-manifest](preparation/manifests/codex-invocation-comments-manifest.json).

| Order | Case | Condition | Repetition | CONFIG |
| ---: | --- | --- | ---: | --- |
| 1 | invocation-tighten | original | 1 | `skill-studies/concise-writing/preparation/configs/codex-invocation-tighten-original.json` |
| 2 | invocation-tighten | candidate-comprehensive | 1 | `skill-studies/concise-writing/preparation/configs/codex-invocation-tighten-candidate.json` |
| 3 | invocation-write | candidate-comprehensive | 1 | `skill-studies/concise-writing/preparation/configs/codex-invocation-write-candidate.json` |
| 4 | invocation-write | original | 1 | `skill-studies/concise-writing/preparation/configs/codex-invocation-write-original.json` |
| 5 | invocation-nonprose | original | 1 | `skill-studies/concise-writing/preparation/configs/codex-invocation-nonprose-original.json` |
| 6 | invocation-nonprose | candidate-comprehensive | 1 | `skill-studies/concise-writing/preparation/configs/codex-invocation-nonprose-candidate.json` |
| 7 | invocation-comments | candidate-comprehensive | 1 | `skill-studies/concise-writing/preparation/configs/codex-invocation-comments-candidate.json` |
| 8 | invocation-comments | original | 1 | `skill-studies/concise-writing/preparation/configs/codex-invocation-comments-original.json` |
| 9 | invocation-tighten | candidate-comprehensive | 2 | `skill-studies/concise-writing/preparation/configs/codex-invocation-tighten-candidate.json` |
| 10 | invocation-tighten | original | 2 | `skill-studies/concise-writing/preparation/configs/codex-invocation-tighten-original.json` |
| 11 | invocation-write | original | 2 | `skill-studies/concise-writing/preparation/configs/codex-invocation-write-original.json` |
| 12 | invocation-write | candidate-comprehensive | 2 | `skill-studies/concise-writing/preparation/configs/codex-invocation-write-candidate.json` |
| 13 | invocation-nonprose | candidate-comprehensive | 2 | `skill-studies/concise-writing/preparation/configs/codex-invocation-nonprose-candidate.json` |
| 14 | invocation-nonprose | original | 2 | `skill-studies/concise-writing/preparation/configs/codex-invocation-nonprose-original.json` |
| 15 | invocation-comments | original | 2 | `skill-studies/concise-writing/preparation/configs/codex-invocation-comments-original.json` |
| 16 | invocation-comments | candidate-comprehensive | 2 | `skill-studies/concise-writing/preparation/configs/codex-invocation-comments-candidate.json` |

### Expanded collection: claude-invocation-01

Results: [completed native Claude assessment](claude-invocation-01-assessment.md), based on the [current attempt index](claude-invocation-01-run-index.json).

Scope: 16 sequential attempts; claude, four native tasks × two conditions × two repetitions.
Authority: included in the owner-approved 104-call allocation recorded at the top of this protocol.
Include all valid-setup executions regardless of outcome; report invalid/unresolved setup and unattempted slots separately.
No automatic retry or replacement.
Use CW-expanded-1 and the linked case cards; selection and task quality remain separate, with N3 functional CW outcomes unmeasured.
Stop for uncertain charges, contamination, input/runtime drift, unusable setup or preservation failure; a valid behavioral miss remains an observation.
Runtime and evidence controls: [expanded qualification](preparation/runtime-qualification.md).
Inputs: [claude-invocation-tighten-manifest](preparation/manifests/claude-invocation-tighten-manifest.json), [claude-invocation-write-manifest](preparation/manifests/claude-invocation-write-manifest.json), [claude-invocation-nonprose-manifest](preparation/manifests/claude-invocation-nonprose-manifest.json), [claude-invocation-comments-manifest](preparation/manifests/claude-invocation-comments-manifest.json).

| Order | Case | Condition | Repetition | CONFIG |
| ---: | --- | --- | ---: | --- |
| 1 | invocation-tighten | original | 1 | `skill-studies/concise-writing/preparation/configs/claude-invocation-tighten-original.json` |
| 2 | invocation-tighten | candidate-comprehensive | 1 | `skill-studies/concise-writing/preparation/configs/claude-invocation-tighten-candidate.json` |
| 3 | invocation-write | candidate-comprehensive | 1 | `skill-studies/concise-writing/preparation/configs/claude-invocation-write-candidate.json` |
| 4 | invocation-write | original | 1 | `skill-studies/concise-writing/preparation/configs/claude-invocation-write-original.json` |
| 5 | invocation-nonprose | original | 1 | `skill-studies/concise-writing/preparation/configs/claude-invocation-nonprose-original.json` |
| 6 | invocation-nonprose | candidate-comprehensive | 1 | `skill-studies/concise-writing/preparation/configs/claude-invocation-nonprose-candidate.json` |
| 7 | invocation-comments | candidate-comprehensive | 1 | `skill-studies/concise-writing/preparation/configs/claude-invocation-comments-candidate.json` |
| 8 | invocation-comments | original | 1 | `skill-studies/concise-writing/preparation/configs/claude-invocation-comments-original.json` |
| 9 | invocation-tighten | candidate-comprehensive | 2 | `skill-studies/concise-writing/preparation/configs/claude-invocation-tighten-candidate.json` |
| 10 | invocation-tighten | original | 2 | `skill-studies/concise-writing/preparation/configs/claude-invocation-tighten-original.json` |
| 11 | invocation-write | original | 2 | `skill-studies/concise-writing/preparation/configs/claude-invocation-write-original.json` |
| 12 | invocation-write | candidate-comprehensive | 2 | `skill-studies/concise-writing/preparation/configs/claude-invocation-write-candidate.json` |
| 13 | invocation-nonprose | candidate-comprehensive | 2 | `skill-studies/concise-writing/preparation/configs/claude-invocation-nonprose-candidate.json` |
| 14 | invocation-nonprose | original | 2 | `skill-studies/concise-writing/preparation/configs/claude-invocation-nonprose-original.json` |
| 15 | invocation-comments | original | 2 | `skill-studies/concise-writing/preparation/configs/claude-invocation-comments-original.json` |
| 16 | invocation-comments | candidate-comprehensive | 2 | `skill-studies/concise-writing/preparation/configs/claude-invocation-comments-candidate.json` |

### Native third repetition: codex-invocation-02

Completed evidence: [codex-invocation-02 assessment](codex-invocation-02-assessment.md) and [attempt index](codex-invocation-02-run-index.json).

Scope: eight sequential attempts; codex, four unchanged native cases × two skill versions × one added repetition.
Authority: owner-approved sixteen-call supplement and minimum-three clarification at the protocol opening.
Use CW-expanded-1 and the unchanged native cards, separating D1 from F1–F3; N3 functional outcomes remain unmeasured.
Include all valid-setup executions regardless of outcome; report invalid/unresolved setup and unattempted slots separately.
No automatic retry or replacement.
Recheck runtime identities and the declared login-shell gates; retain and verify each stopped bundle before the next dispatch.
Stop on uncertain charges, preservation failures, contamination, setup defects or input/runtime drift.
[Runtime qualification](preparation/runtime-qualification.md) supplies the unchanged execution boundary; supplemental checks and assessment are recorded in the [review](../../reviews/2026-09-27-cw-native-third-review.md).
Inputs: [codex-invocation-tighten-third-manifest](preparation/manifests/codex-invocation-tighten-third-manifest.json), [codex-invocation-write-third-manifest](preparation/manifests/codex-invocation-write-third-manifest.json), [codex-invocation-nonprose-third-manifest](preparation/manifests/codex-invocation-nonprose-third-manifest.json), [codex-invocation-comments-third-manifest](preparation/manifests/codex-invocation-comments-third-manifest.json).

| Order | Case | Condition | Repetition | CONFIG |
| ---: | --- | --- | ---: | --- |
| 1 | invocation-tighten | original | 3 | `skill-studies/concise-writing/preparation/configs/codex-invocation-tighten-original.json` |
| 2 | invocation-tighten | candidate-comprehensive | 3 | `skill-studies/concise-writing/preparation/configs/codex-invocation-tighten-candidate.json` |
| 3 | invocation-write | candidate-comprehensive | 3 | `skill-studies/concise-writing/preparation/configs/codex-invocation-write-candidate.json` |
| 4 | invocation-write | original | 3 | `skill-studies/concise-writing/preparation/configs/codex-invocation-write-original.json` |
| 5 | invocation-nonprose | original | 3 | `skill-studies/concise-writing/preparation/configs/codex-invocation-nonprose-original.json` |
| 6 | invocation-nonprose | candidate-comprehensive | 3 | `skill-studies/concise-writing/preparation/configs/codex-invocation-nonprose-candidate.json` |
| 7 | invocation-comments | candidate-comprehensive | 3 | `skill-studies/concise-writing/preparation/configs/codex-invocation-comments-candidate.json` |
| 8 | invocation-comments | original | 3 | `skill-studies/concise-writing/preparation/configs/codex-invocation-comments-original.json` |

### Native third repetition: claude-invocation-02

Completed evidence: [claude-invocation-02 assessment](claude-invocation-02-assessment.md) and [attempt index](claude-invocation-02-run-index.json).

Scope: eight sequential attempts; claude, four unchanged native cases × two skill versions × one added repetition.
Authority: owner-approved sixteen-call supplement and minimum-three clarification at the protocol opening.
Use CW-expanded-1 and the unchanged native cards, separating D1 from F1–F3; N3 functional outcomes remain unmeasured.
Include all valid-setup executions regardless of outcome; report invalid/unresolved setup and unattempted slots separately.
No automatic retry or replacement.
Recheck runtime identities and the declared login-shell gates; retain and verify each stopped bundle before the next dispatch.
Stop on uncertain charges, preservation failures, contamination, setup defects or input/runtime drift.
[Runtime qualification](preparation/runtime-qualification.md) supplies the unchanged execution boundary; supplemental checks and assessment are recorded in the [review](../../reviews/2026-09-27-cw-native-third-review.md).
Inputs: [claude-invocation-tighten-third-manifest](preparation/manifests/claude-invocation-tighten-third-manifest.json), [claude-invocation-write-third-manifest](preparation/manifests/claude-invocation-write-third-manifest.json), [claude-invocation-nonprose-third-manifest](preparation/manifests/claude-invocation-nonprose-third-manifest.json), [claude-invocation-comments-third-manifest](preparation/manifests/claude-invocation-comments-third-manifest.json).

| Order | Case | Condition | Repetition | CONFIG |
| ---: | --- | --- | ---: | --- |
| 1 | invocation-tighten | original | 3 | `skill-studies/concise-writing/preparation/configs/claude-invocation-tighten-original.json` |
| 2 | invocation-tighten | candidate-comprehensive | 3 | `skill-studies/concise-writing/preparation/configs/claude-invocation-tighten-candidate.json` |
| 3 | invocation-write | candidate-comprehensive | 3 | `skill-studies/concise-writing/preparation/configs/claude-invocation-write-candidate.json` |
| 4 | invocation-write | original | 3 | `skill-studies/concise-writing/preparation/configs/claude-invocation-write-original.json` |
| 5 | invocation-nonprose | original | 3 | `skill-studies/concise-writing/preparation/configs/claude-invocation-nonprose-original.json` |
| 6 | invocation-nonprose | candidate-comprehensive | 3 | `skill-studies/concise-writing/preparation/configs/claude-invocation-nonprose-candidate.json` |
| 7 | invocation-comments | candidate-comprehensive | 3 | `skill-studies/concise-writing/preparation/configs/claude-invocation-comments-candidate.json` |
| 8 | invocation-comments | original | 3 | `skill-studies/concise-writing/preparation/configs/claude-invocation-comments-original.json` |

## Storage and accounting

Expanded collection accounting: [claude-invocation-02 attempt index](claude-invocation-02-run-index.json).

Expanded collection accounting: [codex-invocation-02 attempt index](codex-invocation-02-run-index.json).

Expanded collection accounting: [claude-invocation-01 attempt index](claude-invocation-01-run-index.json).

Expanded collection accounting: [codex-invocation-01 attempt index](codex-invocation-01-run-index.json).

Expanded collection accounting: [claude-expanded-01 attempt index](claude-expanded-01-run-index.json).

Expanded collection accounting: [codex-expanded-01 attempt index](codex-expanded-01-run-index.json).

Canonical checkout: `/Users/simon/work/personal/disciplined-development-skills`.
Approved durable raw evidence directory: `/Users/simon/work/personal/skill-study-private/concise-writing/development/`, created and verified with a disposable local copy/hash-inventory probe. All sixteen CW bundles (eight baseline, eight comparison) are stored there with verified version-1 inventories. After the runner stops writing, copy its complete emitted bundle from `/private/tmp/cw-contribution-baseline-01/skilltest-runs/` under the same unique directory name, without overwriting an existing destination. Preserve all files, including hidden/Git files and the provider session; compare the complete source/destination inventory (paths, types, modes, sizes and hashes or symlink targets), write one sibling `.inventory.json` using the existing version-1 inventory shape, and verify it before recording preservation or dispatching again. Unexpected entries or copy/cleanup errors require inspection. Keep failed attempts too; scratch cleanup is not evidence preservation.
Owner-accepted recovery decision for CW: single-host retention, as used for SSR, with one verified canonical raw bundle per attempt. The current `tmutil destinationinfo` check reports no destinations configured; `tmutil isexcluded` reports the parent private store is Included. No other working backup arrangement has been established. Machine loss or disk failure could therefore destroy CW raw evidence; Git holds case inputs and assessments but cannot recover those external bundles. Creating the directory and passing a local copy check do not establish host-loss recovery. The owner explicitly accepted this CW risk together with the eight-execution scope above.

Combined accounting sources: closed SSR [pilot 01](../sweeping-stale-references/pilot-run-index.json), [pilot 02](../sweeping-stale-references/pilot-02-run-index.json), [semantic delivery](../sweeping-stale-references/semantic-delivery-01-run-index.json), [core baseline](../sweeping-stale-references/core-baseline-01-run-index.json), [comparison](../sweeping-stale-references/comprehensive-comparison-01-run-index.json), the SSR [completed expansion](../sweeping-stale-references/coverage-baseline-01-run-index.json), the SSR [completed comparison](../sweeping-stale-references/comprehensive-comparison-02-run-index.json), the SSR [Claude smoke](../sweeping-stale-references/claude-smoke-01-run-index.json), the SSR [Claude comparison](../sweeping-stale-references/claude-comparison-01-run-index.json), the SSR [Opus invocation comparison](../sweeping-stale-references/claude-opus-invocation-01-run-index.json), and both CW indexes above. Historical pilot links contribute accounting only; they are not reclassified or reassessed.
Dispatched calls are **256 subject, 0 evaluator, 0 authoring, 0 retry**; remaining outer capacity is **0 / 12 / 4 / 4** against the [active plan](../../plans/2026-09-11-model-driven-skill-testing.md#limits-and-information-boundaries). Both eight-call CW batches are spent. The owner authorized ten SSR expansion calls under ceiling 56; all ten are spent, including the excluded control, with no replacement or pool transfer. Comparison runner durations total 508.067 seconds; baseline durations remain 494.936 seconds, including setup and capture.
Owner clarification after round-10 review: “the budget is just a guideline”. The 1,200-minute figure below remains the planning baseline, not a collection stop; invocation ceilings and the authorized SSR scope is unchanged. Retain elapsed effort and forecast variance to expose process cost.

Current combined accounting: **2,080 active minutes booked; 880 minutes above the historical 1,200-minute planning guideline**.
These are rounded effort estimates, not stopwatch measurements or a separately timed category breakdown.
Between-turn owner wait is excluded; runner durations are included once.
The initial 104 calls and sixteen native third repetitions are spent; combined subject accounting is 256/256.
The supplemental work used 40 estimated active minutes against its 40-minute forecast; model waits are included once.

| Work | Estimated active minutes |
| --- | ---: |
| Prior close | 810 |
| Comparison close and publication | 35 |
| Process discussion and spec clarification | 8 |
| Mechanical tooling and process updates | 35 |
| Tooling review and regressions | 30 |
| Round-4 contract delta | 8 |
| Cross-study stocktake | 12 |
| Historical coverage review | 8 |
| SSR scenario preparation | 20 |
| Reporting extension | 25 |
| Round-5 corrections | 8 |
| Follow-up self-review | 8 |
| Suite coverage clarification | 8 |
| Protocol/template cleanup | 12 |
| Protocol cleanup follow-up | 5 |
| Round-7 corrections | 6 |
| SSR expansion initial checkpoint | 45 |
| Two-provider isolation correction | 40 |
| Round-9 corrections | 20 |
| Expansion resumption and close | 50 |
| Invocation/pressure preparation | 20 |
| Scenario review and scoring corrections | 8 |
| Runtime/accounting review and evidence recovery | 25 |
| Discovery qualification and allocation preparation | 15 |
| Status and checklist reconciliation | 5 |
| Secondary-status sweep | 2 |
| Codex 34-call comparison | 80 |
| Minimal Claude preflight and diagnosis | 15 |
| Startup reproduction | 8 |
| Runner fixes and two Claude smokes | 25 |
| Sonnet 34-call comparison | 90 |
| Opus ten-call comparison | 20 |
| Testing/authoring stocktake | 8 |
| Round-15 corrections | 8 |
| Claude runner follow-ups | 20 |
| Runner review and malformed-event fix | 5 |
| Git defaults review, regression fixes and verification | 15 |
| Rewrite trace diagnosis and focused proposal | 20 |
| Diagnosis review and accounting-boundary clarification | 3 |
| SSR candidate drafting, concision and contract review | 8 |
| Whole-skill duplication check and CW scope preparation | 5 |
| CW coverage/process audit, evidence verification and study sequencing | 20 |
| Review resolution: experiment design, source qualification and verification | 15 |
| F allocation forecast and follow-up review correction | 5 |
| Pressure-observation interpretation clarification | 2 |
| CW draft fixtures, criteria, configurations and offline review | 55 |
| Owner-requested cross-provider repetition update and consistency checks | 3 |
| Owner scope clarification and comment-coverage check | 2 |
| Replace skill-specific tests with ordinary document integration and verify scope | 15 |
| Positive code-comment case, configurations and offline verification | 15 |
| Full preparation review, scoring/status remediation and re-verification | 25 |
| External suite review: comparison CLI, fixture cues and scope cleanup | 15 |
| Expanded allocation, runtime qualification and collection freeze | 25 |
| CW expanded collection: first Codex rotation and assessment checkpoint | 30 |
| CW expanded collection: second Codex rotation and assessment checkpoint | 20 |
| CW expanded collection: final Codex rotation, verification and batch assessment | 30 |
| CW expanded collection: first Claude rotation and checkpoint | 20 |
| CW expanded collection: second Claude rotation, index recovery and checkpoint | 25 |
| CW expanded collection: final Claude rotation, verification and batch assessment | 35 |
| CW native collection: first Codex rotation and checkpoint | 15 |
| CW native collection: second Codex rotation, verification and assessment | 20 |
| CW native collection: first Claude rotation and checkpoint | 15 |
| CW native collection: second Claude rotation, verification and assessment | 20 |
| CW final cross-provider review, accounting reconciliation and publication | 15 |
| Native third-repetition preparation, qualification and freeze | 10 |
| Native Codex third-repetition collection and assessment | 15 |
| Native Claude third-repetition collection and assessment | 10 |
| Native third-repetition final verification, review and publication | 5 |
| **Total** | **2,080** |

SSR expansion is complete. The prior 55-minute remaining forecast closed at 50 estimated minutes, including the additional shell correction; all ten subject calls are spent.
The combined batch/recovery effort is 135 estimated minutes (45 initial checkpoint, 40 isolation correction, 50 resumption), 45 above the original 90-minute allowance. Separate round-9 review effort remains in the combined ledger above.
The eight resumed runner durations total 771.611 seconds and are included in that effort, not added again.
Time is a guideline; the numeric balance is a planning comparison, not authority for additional invocations.

The completed comprehensive-comparison-02 used 80 estimated active minutes against its 180-minute planning allowance (100 below forecast).
Its runner durations total 2,350.294 seconds (39.17 minutes), already included in that estimate; the other work categories were not separately timed.
The Codex comparison closed at 90/90 combined subject calls and the two Claude smokes at 92/92. The subsequent 34-call Claude comparison is complete, bringing prior spending to 126. All ten subsequent Opus invocation calls are complete, bringing historical spending to 136; the current CW authorization is recorded at the top of this protocol.
The Claude comparison used 90 estimated active minutes against its 120-minute guideline, 30 below forecast; its 2,165.515 seconds of runner duration (36.09 minutes) are included, not added again.

The Opus comparison used 20 estimated active minutes against its 40-minute guideline, 20 below forecast; its 174.840 seconds of runner duration (2.91 minutes) are included once.

Initial fixture preparation used 55 estimated active minutes against its 60-minute midpoint forecast; subsequent owner-directed scope refinements are itemized above.
The [preparation package](preparation/README.md) records inputs and validation; current acceptance and pending decisions are at the top of this protocol.
The [allocation rationale](testing-audit.md#proposed-sequence-and-allocation-forecast) explains the 120-call scope; both approved schedules are complete.
Any fresh rewrite still needs an estimate after baseline diagnosis.

The initial approved-scope forecast was 400 active minutes: 300 ordinary and 100 native.
Ordinary Codex collection and assessment used 80 estimated minutes, including 2,417.307 seconds of runner duration once.
Ordinary Claude collection, registration recovery and assessment used 80 estimated minutes, including 1,405.021 seconds of runner duration once.
Native Codex and Claude collection/assessment each used 35 estimated minutes, including 748.348 and 394.246 seconds of runner duration respectively.
Collection/assessment totaled 230 estimated minutes, 170 below the initial 400-minute forecast; runtime qualification/freeze and final review/publication are separately booked as 25 and 15 minutes.
All 4,964.922 seconds of runner duration are included once, not added to those estimates.
The authorized collection and assessment are complete; remaining effort for this scope is zero.

| Work | Estimate | Basis |
| --- | ---: | --- |
| Remaining authorized collection and assessment | 0 | All 120 attempts and final review are complete. |
| **Total** | **0** | New work requires its own estimate and authority. |

The supplemental runner durations are 336.559 seconds for Codex and 171.913 seconds for Claude, included once in the 15- and 10-minute collection/assessment estimates.
Preparation and final review/publication account for the other 15 supplemental minutes.
A later diagnosis or rewrite needs its own bounded estimate and any new model-call authorization.

## Results and decision

The full 120-call scope is complete, with no unattempted slots, retries, setup exclusions or unresolved judgments.
Ordinary and native cases now each have three repetitions per selected condition/provider.
The native summary combines each original two-repetition batch with its separately frozen third repetition on the same qualified runtime and unchanged inputs; it does not rewrite historical batch scores.
These later observations were not interleaved with the initial repetitions, and the models expose no immutable backend revision.
The existing rewrite is not uniformly stronger: it passes all ordinary Codex attempts, but loses required contact recording in every Claude E attempt and misses more Claude positive native loads in these samples.
Both versions show Claude weaknesses in whole-document cleanup and unsupported new-report claims.
The next owner decision is whether these baselines and explicit coverage limits are sufficient, then which observed failure to target and which version to use as the editing base.
A focused investigation should separate invocation misses from output fidelity and whole-document cleanup; this is a diagnosis recommendation, not an approved rewrite or new-call allocation.
Response-only applicability, full orchestration, plan/spec generation and conditional O5 remain outside demonstrated effectiveness.
SSR stays parked until CW's cycle is settled.

### Combined native results: three repetitions

D1 means timely loading for N1/N2/N4 and appropriate non-loading for N3.
N3 task correctness is descriptive and supplies no functional CW outcome.

| Provider / case | Original D1 | Rewrite D1 | Original functional | Rewrite functional |
| --- | --- | --- | --- | --- |
| Codex N1: tightening | 3/3 | 3/3 | 3/3 | 3/3 |
| Codex N2: new update | 3/3 | 3/3 | 3/3 | 3/3 |
| Codex N3: numeric only | 3/3 | 1/3 | Not measured | Not measured |
| Codex N4: code comments | 3/3 | 3/3 | 3/3 | 3/3 |
| Claude N1: tightening | 3/3 | 3/3 | 3/3 | 3/3 |
| Claude N2: new update | 2/3 | 2/3 | 1/3 | 2/3 |
| Claude N3: numeric only | 3/3 | 3/3 | Not measured | Not measured |
| Claude N4: code comments | 1/3 | 0/3 | 3/3 | 3/3 |

Codex loads and passes all positive tasks: 9/9 per version.
Its rewrite loads prematurely in two of three numeric-only tasks; the original avoids loading in all three.
All six Codex numeric edits are correct, independently of selection.
Evidence: [first two repetitions](codex-invocation-01-assessment.md) and [third repetition](codex-invocation-02-assessment.md).

Claude timely positive loads total 6/9 original and 5/9 rewrite; functional outcomes total 7/9 and 8/9 respectively.
Both versions avoid CW on all three numeric attempts.
The new-report failures add unsupported claims: two after loading in the initial batch, and one without loading in the third original run.
All six comment artifacts pass despite five missed loads.
Extra status messages violate the numeric task's Done-only response in the earlier rewrite repetition 2 and both repetition-3 runs; final.txt alone would hide those unscored task-compliance observations.
Evidence: [first two repetitions](claude-invocation-01-assessment.md) and [third repetition](claude-invocation-02-assessment.md).

These small samples reveal repeated failure modes, not population reliability or a causal description/body effect; the descriptions differ between versions.

### Ordinary comparisons and historical evidence

Expanded ordinary Claude: [assessment and evidence](claude-expanded-01-assessment.md) records 36 valid attempts.
For A/B/C/E respectively, control passes 3/3, 2/3, 0/3 and 3/3; original passes 3/3, 3/3, 1/3 and 2/3; comprehensive passes 3/3, 3/3, 1/3 and 0/3.
The concrete failures are one evidence overstatement, seven readability misses from detached repeated mechanics, and four lost contact-recording actions.
All 24 explicit-load attempts delivered the full body before editing; this is not native-invocation evidence.
One controller index error delayed retention only and was recovered without repeating a call; the assessment links its review record.

Expanded ordinary Codex: [assessment and evidence](codex-expanded-01-assessment.md) records 36 valid attempts under CW-expanded-1.
For A/B/C/E respectively, control passes 3/3, 2/3, 1/3 and 3/3; original passes 3/3, 3/3, 3/3 and 2/3; comprehensive passes 3/3 on all four.
Every output meets F3; the four failed executions lose a responsibility, diagnostic rationale or contact-recording action.
These small exposed-case counts do not establish a reliable ranking; native outcomes are reported separately above.
The collection review corrected two B outcomes using the existing whole-document policy-4 precedent; no rules or calls changed.

Historical baseline:

The [batch assessment](contribution-baseline-01-assessment.md) records eight valid setups and all three required factors met in every output under CW-assessment-4.
Original and control each pass 2/2 on Recommendation and 2/2 on Briefing, with no unknowns, retries, replacements or exclusions.
Whole-document review withdraws the earlier briefing failures: the conditional recommendation, approval gate and continuing-preview context do not demonstrate a loss of correctness or effectiveness.
All outputs are readable and shorter; none has a longer-output flag. Length is reported separately and does not determine pass/fail. Process is unscored; Git preserves earlier judgments and original collection identities.
Pass counts are tied; the assessment reports qualitative differences in reading sequence and safeguard lookup separately. These small, constructed cases do not establish an overall CW advantage. The corrected findings do not support the earlier continuing-permissions rewrite suggestion.
Baseline collection is closed and adoption remains deferred. The live skill is unchanged; the separate existing candidate completed the comparison above.

Comparison review: [fixed-suite comparison self-review](../../reviews/2026-09-18-cw-comparison-review.md).

Baseline review: the [policy-4 resolution and self-review](../../reviews/2026-09-18-cw-policy4-review.md) records the external findings, additional validator defect and verification. No blocking findings remain.
