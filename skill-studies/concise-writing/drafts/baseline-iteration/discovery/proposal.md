# CW revised body and description comparison proposal

The [protocol](../../../protocol.md) owns current status, accepted ceilings and dispatch authority.
This proposal supplies reviewable candidates and a staged forecast; it authorizes no model calls, live-skill changes or adoption.
The [design](../../../../../plans/specs/2026-10-17-cw-baseline-iteration.md) records the owner's request for targeted and fully rewritten descriptions alongside the revised body.

## Description candidates

| Arm | Description source | Hypothesis |
| --- | --- | --- |
| Existing | Unchanged frontmatter in [targeted-examples](../targeted-examples/SKILL.md) | Retain the current selection wording as the comparator. |
| Targeted | [description-targeted.txt](description-targeted.txt) | Use the owner-selected composing/editing/revising trigger and familiar text types, with explicit tightening synonyms; exclude tasks with no text to compose or revise, including changes limited to executable code or numeric values. |
| Rewritten | [description-rewrite.txt](description-rewrite.txt) | Lead with whether the task requires composing or revising text; make document additions and source comments direct examples. |

The owner approved the targeted wording in place of the earlier targeted draft; it does not add a fourth arm or change the proposed allocation.
Its exclusion concerns tasks requiring no text composition or revision, rather than coding generally, because coding tasks can also require comments or documentation.
The existing description already names code comments; neither candidate is merely adding a missing keyword.
Both preserve the skill/reference-authoring exclusion and contain selection cues rather than a workflow.
The numeric-only example expresses the selected negative boundary without naming a fixture, its values or its required reply.
Both are exposed-case hypotheses; improved selection on these familiar cases would be development evidence, not held-out generalization.
They compare complete alternative descriptions, so a result cannot isolate which individual phrase caused a difference.
Response-only applicability and skill/reference authoring remain outside this experiment and any adoption claim.

Every discovery arm uses exactly the same skill name and the complete revised targeted-examples body.
At freeze, materialize three skill files by replacing only the parsed description; assert byte-identical content after the frontmatter and identical names.
Do not copy or edit the body independently in each arm.
An effect of description wording remains conditional on this body and the qualified test catalog.

## Cases and observations

| Case | Purpose in this proposal | Observation |
| --- | --- | --- |
| A: recommendation | Remaining body regression; N1 reuses its content | Preserve decision, evidence and rationale while removing padding. |
| B: effective briefing | Remaining body regression | Preserve an already effective document; avoid unnecessary edits or unsupported additions. |
| C: long handoff | Focused body diagnostic | Improve whole-document organization and scattered repetition without losing useful explanations or point-of-use safeguards. |
| E: document addition | Focused body diagnostic | Integrate new notes into an existing document; apply the owner-resolved contact interpretation. |
| N1: natural tightening | Remaining discovery regression | Load the complete skill before the first task edit, separately from artifact quality. |
| N2: writing from notes | Remaining discovery and explicit-load body regression | Select CW for new writing; preserve supplied evidence and responsibilities. |
| N3: numeric-only edit | Focused discovery negative | Avoid loading CW; record numeric edit and prescribed-reply compliance separately, outside functional CW counts. |
| N4: code comments | Focused discovery positive and explicit-load body diagnostic | Select CW for comment editing; improve comments without changing executable tokens, syntax or required meaning. |

The N2 and N4 explicit-load body probes are prospective sibling strata, not relabelings of prior native observations.
Use the same task and fixtures but a separately frozen condition instruction to load the skill before work; controls have no CW available and no load request.
These probes measure body contribution, not natural invocation.
For native probes, keep existing task prompts unchanged and provide no extra hint to load CW.

## Proposed allocation

Body conditions are no CW, unchanged original and revised targeted-examples, using the existing description for both skill arms.
Discovery conditions are the three descriptions above with the revised body fixed; there is no no-CW arm because the measured question is selection from an available catalog.
Both stages use Codex and Claude separately, with fresh contexts for every subject.

| Stage | Scope | Calculation | Subjects | Opus reviews |
| --- | --- | --- | ---: | ---: |
| Focused body | C, E, N4; three conditions; five repetitions | 3 cases × 3 conditions × 2 providers × 5 | 90 | 6 |
| Focused discovery | N3, N4; three descriptions; five repetitions | 2 cases × 3 descriptions × 2 providers × 5 | 60 | 4 |
| First proposed allocation | Focused body then discovery | 75 subjects per provider | **150** | **10** |
| Remaining body regression | A, B, N2; three conditions; three repetitions | 3 × 3 × 2 × 3 | 54 | 6 |
| Remaining discovery regression | N1, N2; three descriptions; three repetitions | 2 × 3 × 2 × 3 | 36 | 4 |
| Later proposed allocation | Separate decision after the focused results | 45 subjects per provider | **90** | **10** |
| Complete forecast | Both stages, if approved unchanged | 120 subjects per provider | **240** | **20** |

Five repetitions serve the focused wording questions; three is the owner's minimum for the remaining regression coverage.
Neither sample count establishes population reliability or equivalence.
A and N1 share task content, so do not duplicate A as another explicit-load N1 body probe.
All eight existing scenarios are represented; the new body cannot reuse old E results as validation of its changed bytes.
The previously tested targeted, fuller and comprehensive variants remain historical comparators, not additional arms in this bounded proposal.

Current accepted subject/evaluator ceilings are exhausted at 440/28.
Approving the first allocation would raise them to 590/38; approving both stages unchanged would eventually raise them to 680/48.
Authoring/retry pools stay unchanged, and unused capacity is not transferable or automatic replacement authority.
The later 90/10 is a forecast, not part of a first-stage approval.

Estimate 210–300 active minutes for the focused stage and 150–210 for the remaining stage: 360–510 combined.
This includes preparation, runtime qualification, freezing, model waits, direct assessment, grouped review and reconciliation once, informed by the prior remaining-suite collection and review effort.
These are planning estimates, not measured durations or additional time already spent; refine them before freeze if transport or packet preparation changes.

## Scoring and transition rules

Before collection, resolve or explicitly bound the consequential interpretation disagreements in the [completed reconciliation](../../../runs/baseline-iteration-suite-01/evaluation/assessment.md).
These include future-state constraints, the scope of “only staffed window”, “no evidence of loss” versus “no loss”, detached reminders, and whether accepted-batch rationale is adequately conveyed.
Use owner intent and concrete source/output comparisons, not evaluator majority vote, to fix the prospective criteria.
Do not silently alter historical scores or require literal wording; any reassessment needs a versioned mapping.

Freeze the criteria, complete bodies, descriptions, prompts, cases, schedule and transition rules before the first subject.
Rotate the three conditions cyclically and reverse provider starting order; five repetitions cannot fully balance three-condition positions, so disclose that residual order imbalance.
Three-repetition regression blocks can balance positions.
Complete a fixed stage despite valid behavioral failures; stop dispatch for invalid setup, capture/integrity failure, input drift, uncertain charge or exhausted authority.
Never edit between repetitions or replace an inconvenient result.

The owner-approved loaded-baseline RED method continues to apply; passing no-CW controls do not automatically stop this comparison or justify inventing a failure.
For body comparison, report consequential regressions and improvements by case and provider, with supporting source/output text and no-CW controls retained even when they pass.
A confirmed consequential regression in revised targeted-examples blocks advancing that body without an explicit owner decision on revision or further testing.
Absent such a regression, the body is eligible for the remaining coverage; this is not an effectiveness win or permission to adopt.
An apparent omission disputed under the frozen interpretation remains uncertainty, not an automatic failure or a reason to change wording mid-stage.

For discovery, report timely N4 loads and N3 non-loads separately for each provider, including partial or late loads.
A candidate is promising for further testing if it improves N4 timely loads on at least one provider, reduces them on neither, and adds no N3 loads on either provider relative to the existing description in this stage.
This is a descriptive advancement rule, not a statistical claim; conflicting trade-offs or equal counts return to the owner with the traces.
No advantage supports retaining the existing description unless the owner chooses more evidence; it does not authorize automatic repetitions.
Keep every valid invocation miss as evidence even if the artifact succeeds.

Final adoption still requires the selected body/description combination's complete relevant coverage and cross-model reconciliation.
The owner's shorter-SKILL.md tie-break applies only after consequential effectiveness and quality are equivalent; equal pass counts alone do not establish that.
If a body or description changes after the focused stage, propose its affected revalidation and cost before treating earlier runs as validation of the new combination.

## Qualification and cross-model review

Plan to retain the last subject settings, Codex gpt-5.6-sol low and Claude Sonnet 5 low, subject to confirming the qualified binary/model identities before freeze.
Do not silently substitute a CLI, model, effort or Python runtime; changed identities require an explicit stratum and owner allocation decision.
Run the existing login-shell Python/Git, heredoc and sandbox checks before dispatch, with zero model calls where the installed scripted transport supports them.
For each description on both providers, verify exact catalog delivery and that the body is absent until read; verify the trace can establish complete delivery before the first task edit.
Retain the catalog's complete contents and disclose its difference from a user's installed catalog; these probes do not estimate general real-world invocation rates.
Use the N4 fixture's mechanical compare command on each output and retain the complete assistant message stream for N3 reply compliance.

Codex is the active assessor, so owner-selected Opus 5.5 medium is a cross-family reviewer relative to that assessor, including when it reviews same-family Sonnet subjects.
Use one read-only review per case/provider block: fifteen outputs in each focused packet and nine in each regression packet, below the previously completed twenty-output packet size.
Freeze packet completeness, settings and tools before dispatch; provide source, task, criteria and every artifact before first-pass judgments, then expose prior scores for reconciliation.
Exclude skill bodies and candidate hypotheses from output-quality packets; record that the controller is exposed to authoring evidence and do not claim a blinded authoring experiment.
Opus reviews all output arms, including N3 task-only observations; the controller's catalog/load-timing audit owns invocation judgments.
A timeout, authentication error or incomplete review is retained and charged; no retry, automatic split or fallback reviewer is authorized by this proposal.
