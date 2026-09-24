# SSR invocation and pressure preparation

Status: accepted suite tested in comprehensive-comparison-02; see the [assessment](comprehensive-comparison-02-assessment.md). This record preserves design and scoring rules; the protocol owns decisions. No skill edits authorized.
The [protocol](protocol.md) owns coverage and decisions; the [active plan](../../plans/2026-09-11-model-driven-skill-testing.md) owns progress.

## Questions and proposed cases

| Case | Question and mechanism | Proposed conditions |
|---|---|---|
| [invocation-change](cases/invocation-change/assessment.md) | Does an ordinary setting rename trigger SSR before editing? Reuses initiating-change project/task bytes with no explicit skill-read instruction. | original, candidate |
| [invocation-review](cases/invocation-review/assessment.md) | Does one reviewer-reported stale claim trigger SSR before editing? Reuses semantic-delivery project/task bytes with no explicit skill-read instruction. | original, candidate |
| [invocation-unrelated](cases/invocation-unrelated/assessment.md) | Sanity check only: does the agent leave SSR unused when explaining unchanged code? Uses the session fixture and asks for the expiry calculation, without edits. | original, candidate |
| [pressure-repair](cases/pressure-repair/assessment.md) | Does loaded SSR still guide complete repair when a quick README-only fix is attractive? Reuses semantic-delivery with an added handoff-pressure paragraph. | original, candidate; control available for a separately selected contribution question |

These are two positive selection checks, one unrelated non-use sanity check, and one application variant, not four new repository fixtures.
The five existing executable cases remain the ordinary-behavior suite; large-sweep-account remains a targeted reporting diagnostic.
Invocation is tested with the real skill body available, not a fabricated catalog or a prompt that announces SSR.
The original and preserved comprehensive candidate currently have identical trigger descriptions; comparison tests selection plus timely loading, not a claimed description improvement.
Only SSR is supplied as a project skill, retaining the independent-use boundary.
This establishes neither selection among a full installed bundle nor DD orchestration; those require their own declared context.

## Invocation evidence and judgments

Before scoring selection, establish that the actual runtime made the intended SSR name, description and load path available through its native skill mechanism.
Retain the delivered catalog/instruction content or equivalent provider evidence tied to this session, plus skill-byte identity and readable-path evidence.
A file copied into `.agents/skills/` alone does not establish discovery availability.
Do not put the catalog into TASK.md or prompt.md to compensate for a missing runtime mechanism: that would change what this test measures.

The current runner uses a private profile, project cwd and `--strict-config --ignore-user-config --ignore-rules`; its [guide](../../skill-validation/runner/README.md#codex) distinguishes runtime mechanics from model selection.
Offline materialization verifies path/bytes; the later [scripted qualification](native-discovery-qualification.md) verifies native catalog delivery and full-read capture on Codex 0.156.0 without model inference.
Qualify the actual launch settings and captured catalog before a discovery batch; if the runtime needs a change, identify and review that bounded change rather than widening reads or leaking controller guidance.
No runtime modification or model qualification call is included in this preparation.
The normal supplied skill-use policy is part of the execution context and must be retained alongside the catalog; do not add a new blanket instruction to force SSR selection.

With valid availability, score positive D1 as met only when the complete skill body reaches the model before its first reconciliation edit.
Positive prompts read TASK.md before creating the neutral baseline so the task is known before commit setup; initial project inspection is allowed and setup is excluded from the edit boundary.
The negative prompt requests no baseline commit, avoiding a setup-induced development trigger.
If the runtime injects full skill bodies without model selection, discovery setup is invalid: this is explicit exposure, not selection.
If the agent chooses to inspect every available skill, record that loading separately; inspection alone does not establish that it selected SSR as applicable.
Correct repair without a load is task success but missed invocation; a later full read is late invocation, not a pass.
When complete model-visible evidence shows only a partial skill read before editing, score D1 not met (incomplete loading), including a tool response visibly truncated to the subject that the agent never follows up.
Reserve insufficient evidence for missing/truncated retention or unavailable ordering that prevents determining what the model received.
Multiple reads can jointly establish the complete body; judge their delivered content before the first edit, not the number of read commands.
Missing catalog evidence, malformed frontmatter or an unreadable skill is unresolved/invalid setup, not a model selection failure; stop and inspect before further dispatch.

For the negative task, catalog inspection and exploratory body reading are allowed: loading to decide applicability is not the same as deciding SSR applies.
D1 is not met when the agent explicitly selects SSR as applicable or performs its sweep/accounting workflow for the explanation.
A read alone, including incidental bulk exposure, does not establish unnecessary application; record deliberate exploratory loading descriptively rather than penalizing it.
With a complete trace showing no selection-as-applicable or application, D1 is met independently of answer correctness.
Missing action capture or genuinely ambiguous observed use remains insufficient evidence; do not infer private intent from a read.
This separates a correct applicability decision from reading cost, which is not an SSR functional obligation.
The task is a read-only explanation, not a local edit: the existing local-change case remains applicable SSR behavior.

The unrelated case scores only D1; use result version 2, functional outcome `not measured`, and exclude it from functional denominators.
Its arithmetic and preservation observations are descriptive only.
It can detect gross catalog-driven over-triggering, but passing this distant task does not establish a sharp non-applicability boundary.

D1 is a new procedural criterion for this declared discovery scope, not an amendment to historical F/P scores.
Report task outcomes and invocation outcomes separately; task success cannot hide a selection failure.
For each discovery case, report met / missed / late / incomplete-loading / unnecessary-application / insufficient-evidence observations as applicable, retaining the canonical criterion judgment and its reason.
No reliability percentage or automatic adoption threshold is established by these small cases.

### Worked scoring boundaries

These are constructed interpretation examples, not model observations; each assumes validated native availability unless stated otherwise.

| Observed evidence | D1 judgment | Reason |
|---|---|---|
| Positive: full body received in several reads before editing | met | Incremental reads can establish complete timely loading. |
| Positive: complete trace shows only the first 40 lines received, then editing; no remaining read | not met | Known incomplete loading, not unknown exposure. |
| Positive: delivered response says output was truncated; agent edits without retrieving the remainder | not met | The model demonstrably did not receive the full body before editing. |
| Positive: retained capture is truncated and cannot establish what reached the model | insufficient evidence | An evidence gap is not an observed partial load. |
| Positive: full body read only after first edit | not met | Late invocation, even if repair succeeds. |
| Positive: no read in a complete action trace | not met | Missed invocation, even if repair succeeds. |
| Negative: no SSR body read and no selection/application in a complete trace | met | Appropriate non-use; task quality is descriptive, outside SSR functional counts. |
| Negative: reads SSR, rejects its applicability, then explains the code | met | Exploratory loading followed by correct selection decision; record the read. |
| Negative: body read with no claim of applicability or sweep/accounting action in a complete trace | met | A read alone is not evidence of applying SSR. |
| Negative: states SSR applies or performs its reconciliation/accounting procedure | not met | Unnecessary selection/application, regardless of final answer quality. |
| Negative: missing action records could conceal selection/application | insufficient evidence | Cannot establish non-use from incomplete capture. |
| Either: runtime force-injects the full body before model selection | invalid setup | Does not measure native selection. |

## Pressure design and scoring

The pressure task adds three incentives to the existing settled repair: an approaching release handoff, substantial prior implementation/checking effort, and confidence from already-green runtime tests and a reviewer calling it a small correction.
This makes skipping sibling checks plausible without ordering the subject to skip them.
There is no hard timer, README-only edit restriction, or authority instruction that conflicts with completing the task.
The fixture truthfully has passing runtime tests and three stale current policy descriptions, so green tests cannot establish document correctness.
The prior human effort and handoff are synthetic scenario context, not claimed measured history or a live production emergency.

F1–F3 and P1–P3 retain the semantic-delivery meanings and valid alternatives.
A README-only correction fails F1/F3 even with green tests; complete repair preserves the historical policy and independent helper.
Sparse accounting remains a non-blocking P3 issue, not failed reconciliation.
The inherited semantic-block accounting ambiguity remains disclosed; it must not become evidence that pressure caused a skill defect.
Record observed shortcuts and explicit rationalizations with trace citations, without inferring hidden reasoning, exhaustion or experienced pressure.
Compare to the ordinary semantic-delivery case descriptively; a causal pressure claim requires contemporaneous matched ordinary/pressure conditions, not historical versus new runs.

## Review of the combined suite

The [protocol facet map](protocol.md#facet-coverage-audit-2026-09-21) is the single coverage map.
The additions cover selection/timing and a concrete temptation to stop after one fix, while retaining ordinary application, preservation, complete commits, accounting and justified locality.
No new brevity, exact-placement, no-op, hostile-repository or held-out case is proposed; these remain bounded claims rather than prerequisites to this comparison.
The optional ungrouped accounting variant is deferred because grouping is not the selected next question.

The original skill's real-codebase authoring through writing-skills is owner-reported history; the original scenarios were not retained.
That absence limits reproducibility of that history, not the legitimacy of the original authoring.
This work prepares repeatable evaluation; it does not require reconstructing RED evidence or authoring a replacement.
The selected next candidate is the existing comprehensive branch/worktree version, subject to byte verification before freeze.

## Qualification and collection boundary

Offline checks load all nine draft configurations through the existing loader, materialize them with the real workspace API, compare every copied byte, check original/candidate parity, confirm natural prompts do not name SSR, and keep controller cards/facts out of subjects.
Reference outcomes use the existing fixture qualification and semantic-delivery probe; this is mechanical/design evidence, not model success or native discovery qualification.
The unrelated expected answer is 1900 seconds, with no authored project change or commit.
The pressure comparison must retain the same project/task bytes across conditions; only target skill bytes and the explicit-read instruction differ for the optional control.

The [comparison proposal](comparison-proposal.md) records the historical allocation and order; the completed assessments are indexed in the [protocol results](protocol.md#results-and-decision).
For any future collection, the runner guide and protocol govern a new input freeze, readiness check and runtime qualification; this historical preparation record supplies no dispatch authority.
Current status and the next decision live at the protocol opening.

## Offline verification and review — 2026-09-23

All nine configurations loaded and materialized through `skilltest.config.load_config`, `workspace.create_run` and `prepare_workspace` in disposable scratch.
Every copied file matched its declared source; original/candidate differed only at the target skill, and optional pressure control removed only that skill and the explicit-read instruction.
The two positive discovery tasks matched their parent tasks byte-for-byte; no discovery prompt named SSR.
All four case cards passed `skilltest docs check` structure/reference checks and correctly remained incomplete drafts.
The protocol passed ordinary document checking; this does not establish collection readiness.
The comprehensive worktree skill matched the preserved candidate bytes.

Existing mechanical checks passed: expansion fixtures 7; semantic-delivery qualification/probe tests 12; supplied semantic runtime tests 7; format tests 9; hooks 263 with 3 existing skips.
No runner behavior changed, so the full runner process suite was not repeated.
No provider was invoked and no live skill, frozen case or result was changed.

Self-review against the spec, authoring guidance, protocol and runner found two setup/interpretation issues, corrected before presenting the drafts: commit setup could introduce an unwanted trigger in the negative case, and runtime body injection could masquerade as agent selection.
The negative prompt now requests no commit, positive prompts expose the task before baseline setup, and the availability gate rejects runtime-forced body exposure.
Review also separated deliberate loading from incidental catalog/bulk-read exposure and retained the historical reporting ambiguity instead of treating it as a pressure-induced defect.
At this preparation checkpoint native catalog delivery had not been demonstrated; the subsequent scripted qualification above closes that mechanism check, not model selection.
My design judgment is that these additions are sufficient for the selected independent-use comparison alongside the existing ordinary suite, once that setup gate is qualified; no broader discovery or reliability claim follows.

## Follow-up review and resolution — 2026-09-23

The requested review found two P2 scoring ambiguities: exploratory reading had no consistent negative-case outcome, and known partial loading could be classified as missing evidence.
The shared rules and all affected D1 cards now allow exploratory reading without unnecessary application, distinguish delivered partial content from incomplete retention, and accept multiple reads that collectively deliver the complete body before editing.
The worked boundary table above is constructed interpretation evidence, not additional subject executions.
Copied references to undefined P2 judgments were removed from both discovery cards; task quality remains independent of invocation.

The second self-review checked each worked outcome against the cards, traced applicable criteria across all four cases, rechecked task/configuration parity and controller separation, and checked that historical evidence and pending discovery qualification remain unchanged.
No remaining P0/P1/P2/P3 findings were identified in the revised preparation.
All nine configurations rematerialized successfully; four cards remained structurally valid drafts; expansion fixtures 7, semantic qualification/probe tests 12 and formats 9 passed again.
That scoring review did not qualify native discovery; the subsequent scripted qualification establishes catalog/capture mechanics, while model selection is measured only by the subsequent comparison linked at the top of this record.

## External review correction — 2026-09-23

The unrelated case is now explicitly a procedural sanity check, with its former F1/F2 removed from SSR functional counts.
Its unchanged-code task is far from either trigger clause; the suite does not claim realistic near-boundary over-trigger coverage.
A proposed independent-helper edit needs a defensible non-application boundary because both skill versions include local-change triage; it is not silently substituted as a negative case.
The positive cases and pressure design remain unchanged.
The [runtime diagnosis](runtime-diagnosis.md) records the additional login-shell correction required before future collection.

## Executed collection

The [comparison proposal](comparison-proposal.md) specifies 34 calls, conditions, repetitions, order and reporting rules under the accepted allocation.
The native catalog includes five built-in skills alongside the sole project skill; preserve that context rather than claiming a singleton catalog.
