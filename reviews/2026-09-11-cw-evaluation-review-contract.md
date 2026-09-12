# CW evaluation: artifact roles and owner review

> **Abandoned testing process — historical reference only (2026-09-11).**
> Testing-framework instructions, approvals and pending work below are no longer current. Follow the [new framework spec](../plans/specs/2026-09-11-model-driven-skill-testing-framework.md) and [new testing plan](../plans/2026-09-11-model-driven-skill-testing.md).
> The original text is preserved as history; this notice does not retire existing runner tooling or core skills.


Status: unapproved proposal; the owner stopped implementation to discuss the diagnosis and then requested the [greenfield framework design](../plans/specs/2026-09-11-model-driven-skill-testing-framework.md).
This proposal is preserved for reference and is not active guidance for that design.

Applies to the current CW-02/CW-19 scoring rebuild and its review conversations.
This document makes evaluator responsibilities concrete; it does not change the skill, behavioral specification, subject tasks, scoring ledgers or evidence permissions.
The [active plan](../plans/2026-09-09-dd-skill-testing.md#fresh-scoring-rebuild-approved-handoff) owns scope and approval checkpoints.

## Diagnosis and correction

The observed failure was in the evaluator's application and presentation of the review workflow.
The [CW-19 task](../skill-validation/pilot/cw-19/specification/prompt.md) supplies a complete runbook and requests preservation of its operational requirements.
The [reviewed specification](../plans/specs/2026-09-10-cw-baseline-specification.md#intended-outcome) already explicitly permits rewriting, restructuring and useful repetition, with the complete document as the unit of judgment.
Both fresh rubric drafts already carry that rule.
Nevertheless, after the owner accepted constructed A, the evaluator presented B's two added sentences and asked whether they were useful or padding.
That question delegated a settled evaluation responsibility to the owner and made the owner repeat the governing standard.
The walkthrough also failed to make the distinction between constructed calibration and measured test results clear enough at first presentation.

The written standard was available; the failure was not caused by missing permission to repeat or restructure prose.
The review checkpoint was treated as a request for owner classification of individual edits rather than review of the evaluator's supported judgments.
This is the supported workflow diagnosis, not a claim about inaccessible model internals or the correctness of withheld historical rubrics.
Repair the review procedure here instead of adding another formulation of the same behavioral rule to the subject prompt or specification.
Documentation supplies an enforceable review practice, but does not itself prove that future model behavior will follow it.

## Which artifact owns what

| Artifact | Role | What it does not establish |
|---|---|---|
| Complete baseline CW skill | Defines the existing skill's behavior, scope, exceptions and method. Read it as a whole. | An isolated slogan cannot override its preservation and framing exceptions. |
| Reviewed behavioral specification | Extracts the skill's promises and the owner's clarified interpretation into the agreed evaluation contract. Correct it if it diverges from the complete skill. | It is not evidence that the skill achieves those promises. |
| Scenario and subject prompt | Supply the reader, task, source content, constraints and selected conditions for one test. The actual executed prompt bytes bound any later assessment. | They do not establish a preferred rewrite or authorize extra requirements absent from the source. |
| Rubric | Maps the agreed promises and scenario obligations to supported judgments in the existing ledgers. | It cannot invent skill behavior, require sentence counterparts or turn resemblance to a padding pattern into failure. |
| Constructed calibration example | Illustrates a proposed acceptable or unacceptable outcome to challenge the scoring interpretation before application. | It is not a retained run, a measured baseline, a candidate skill rewrite or evidence of effectiveness. |
| Retained subject output and run evidence | Record what the selected model actually produced under identified inputs and conditions. | A loaded-skill pass alone does not show causation or improvement over the control. |
| Assessment | Applies the reviewed, frozen rubric to retained evidence, with reasons and correct ledger assignment. | It must not silently alter criteria to fit an output. |
| Owner review and active plan | Settle disputed interpretations and authorize the specified transitions. | Review does not transfer the evaluator's reading, comparison or initial judgment to the owner. |

CW-19 A–H were constructed in the working session using the complete skill, reviewed specification, source runbook and owner feedback.
Call A an **accepted calibration example of acceptable output**; reserve **measured baseline** for actual observations under identified conditions.
Using the specification to construct an illustration is appropriate for calibration, but cannot independently validate that specification.
An accepted example is one acceptable solution, not a golden answer whose words or structure future outputs must match.

## Evaluator work before owner review

1. Identify the artifact being discussed: criterion, constructed example, retained observation or proposed contract change; state its provenance and review status when introducing it.
2. Read the complete source and complete revision, identify the intended reader and use, and account for every consequential source obligation in the existing rubric group.
3. Use local differences to investigate; then check the revision's full context, structure and relocated meaning before concluding that any difference is a loss or waste.
4. Make the judgment and support it: explain what the intended reader can understand or do at least as well, or what becomes less effective. For padding, explain why the passage supplies no information or useful reader function in this document. Repetition, removability, length and different structure are not sufficient reasons.
5. Keep semantics, readability, fidelity, protocol and evidence gaps distinct under the existing methodology. Record uncertain materiality as uncertain; do not convert it into an automatic pass or failure.
6. Present the reasoned judgment for owner review. Ask a question only for an unresolved consequential interpretation, a genuine source conflict, a requested preference outside the settled contract, or an explicit approval transition.

These steps do not add another scoring ledger or require a separate record for each source fact.
Use the current rubric's evidence and review sections.
Rewriting can redistribute meaning throughout a document; the evaluator must not require local explicitness when the complete revision conveys the relationship clearly.
Useful or warranted repetition is allowed when the whole revision remains at least as effective as the original; already-settled guidance is applied without asking the owner to reaffirm it.

## What a question for the owner must contain

For a substantive ambiguity, provide the complete comparison or accessible complete artifacts, the particular criterion at issue, the evaluator's proposed judgment and reader consequence, and the exact unresolved decision.
Short excerpts can locate the issue, but cannot replace the whole-document comparison as the basis for judgment.
If the existing contract already resolves the question, state and apply the judgment instead of asking it again.
In a requested one-at-a-time walkthrough, present one reasoned decision at a time and allow the owner to challenge it; a walkthrough does not require a vote on every sentence or variant.

For a freeze or rollout approval, name the complete version and scope being approved and summarize any unresolved limitations.
Keep those explicit gates: agreement with A, acknowledgement of an explanation, silence or elapsed time does not approve the entire rubric or authorize retained-output scoring.
The evaluator remains responsible for the assessment; the owner reviews the interpretation and authorizes the transition.

## Checks against the observed failure

These are review-practice checks, not subject tests or empirical effectiveness evidence.

| Situation | Required response |
|---|---|
| B adds two reminders to accepted A | Compare the complete runbooks and make a supported judgment about their reader function. Do not ask whether repetition is allowed or request isolated approval of the additions. The current evaluator judgment is that B is acceptable as a whole. |
| C changes mismatch readiness and the matching stop condition to allow exactly 0.1% | Explain that the complete document permits an operational state the source blocks. Apply the established preservation rule; do not reopen whether changed operational requirements matter. This remains a constructed calibration judgment. |
| G preserves predicates but requires more interpretation | Assess the complete document, distinguish correctness from processing effort, and state the evaluator's materiality judgment. If materiality remains unresolved, bring that precise boundary and supporting comparison to the owner. Do not ask a general preference about concise wording. |
| A is accepted as an example | Record acceptance of A only. Do not call it a successful measured run, freeze all criteria or infer approval of the other examples. |
| A new sentence-level concern appears | Locate its meaning in the whole revision before escalating it. An absent counterpart is not proof of lost reader understanding. |
| Old scoring might explain a disagreement | Keep the exposure checkpoint. The observed review failure does not authorize opening withheld rubrics, grades or outputs. |

## Verification and limits

For this correction, check that the active handoff, both fresh rubric drafts and the current continuation entry route to this procedure.
Verify that the baseline skill, reviewed specification, scenario prompt bytes, constructed runbooks and historical plan sections remain unchanged.
The corrected procedure can be checked against the B exchange above without a new subject or provider run.
Its effectiveness must be demonstrated by subsequent review behavior; passing file checks cannot establish that the evaluator will not repeat the mistake.
