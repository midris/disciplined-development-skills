# Search-preview briefing

## Identity and purpose

Format version: `1`
Study ID: `concise-writing`
Case ID: `effective-briefing`
Definition version: `3`
Status: owner-approved whole-document reassessment of contribution-baseline-01; no new collection.
Purpose and realistic failure opportunity: Edit an already-effective briefing while retaining correctness and usefulness; prefer shorter text without requiring unnecessary cuts.
Protocol coverage and membership/exposure: [suite](../../protocol.md#suite-and-evidence), selected development case; O1–O3 assessed through F1–F3; length reported separately, O4–O5 process unscored. Author and assessor share construction history; no held-out or independent-validation claim.

## Inputs and setup

Subject inputs: [task](task.md), complete [source document](fixture/report.md), and, for original only, the [preserved CW skill](../skill-original/SKILL.md).
The [original configuration](original.json), [control configuration](control.json) and [collection manifest](manifest.json) retain the actual supplied context.
Definition 3 and policy 3 are controller-only reassessment rules, never supplied to the subjects.
Both sources are fictional study material; subjects edit prose and do not execute the actions it describes.
Setup validity requires evidence of the intended source bytes, skill condition, matched surrounding context, output path and captured final workspace.
Resolve capture/setup uncertainty separately; with valid setup assess the saved report, including an unchanged or partially edited report, under every factor.

## Rules and evidence

Policy: [CW-assessment-3 controller copy](../../assessment-policy.txt), derived verbatim from the [protocol policy body](../../protocol.md#current-cw-assessment-policy).
Inspect the complete source and complete saved output before assigning any judgment. The source is factual authority.
The reader needs to decide on Thursday whether to invite four additional teams to an opt-in search preview, using limited evidence and readiness checks, while keeping any default change or wider rollout subject to a later decision. Compare how the complete source and edit support that decision, the current preview context, conditional invitations and follow-up. Read an opening recommendation together with its conditions and approval gate. Consolidation or implicit continuity is not automatically a loss: establish what the whole document now leads the reader to understand or do.
A local difference is evidence to investigate, never an independent score. Justify each factor from the document’s overall meaning and use; identify an actual reader consequence before declaring a loss.
Historical examples and qualification judgments belong to policy 1 and are not answer keys for this reassessment.
Reliable evidence of an absent or empty delivered document fails F1–F3; reduced word count alone cannot produce a pass. Missing capture is not proof of absence.

### Length observation (unscored)

Use wc -w on the complete source and delivered Markdown files. Report both counts and the signed difference.
Shorter is preferred; unchanged is acceptable; longer is visibly flagged for consideration in context, without an automatic failure.
Additional words may improve explanation or usability. Assess those effects under F1–F3; length is neither a substitute for those judgments nor a fourth criterion.
If length cannot be measured, report it as unavailable without inventing a count or changing an otherwise supported functional result.

## Criteria

### F1: Entire output remains correct

Basis: [skill](../skill-original/SKILL.md) and owner’s [assessment policy](../../protocol.md#assessment-policy); no new subject instruction.
Coverage: O1; source fidelity and meaningful qualifications.
Dimension: functional
Applies to: `original`, `control`
Judgment unit: complete delivered document compared with the complete source.
Required evidence: Complete source and delivered document, including relationships between sections.
Met: The edit as a whole is faithful to the source’s facts, reasoning, uncertainty, conditions and scope.
Not met: The whole edit communicates a false or unsupported conclusion, distorts a consequential condition or loses information needed for a correct understanding.
Insufficient evidence: available source/output evidence cannot settle this factor; identify the unresolved question rather than forcing a pass or failure.
Alternatives: faithful paraphrase, consolidation, relocation, useful repetition and any effective layout; no sentence-matching or preferred answer.
Consequence: Correctness is a primary gate; failure blocks overall success regardless of the other factors.
Overlap: a shared defect may affect multiple factors but counts as one failed execution; do not infer another factor’s failure automatically.

### F2: Entire output is at least as effective as the original

Basis: [skill](../skill-original/SKILL.md) and owner’s [assessment policy](../../protocol.md#assessment-policy); no new subject instruction.
Coverage: O1–O3; owner’s explicit comparative-effectiveness requirement.
Dimension: functional
Applies to: `original`, `control`
Judgment unit: complete delivered document compared with the complete source.
Required evidence: Complete source/output comparison for the stated reader and purpose.
Met: The edit supports the reader’s understanding, decision and next actions at least as effectively as the source; useful explanation, emphasis and orientation still do their jobs.
Not met: The complete edit is less useful for that purpose, such as weakening a needed warning, obscuring a choice or making the reader reconstruct a necessary connection. Identify the practical loss.
Insufficient evidence: available source/output evidence cannot settle this factor; identify the unresolved question rather than forcing a pass or failure.
Alternatives: faithful paraphrase, consolidation, relocation, useful repetition and any effective layout; no sentence-matching or preferred answer.
Consequence: Comparative effectiveness is a primary gate; failure blocks overall success regardless of compression.
Overlap: a shared defect may affect multiple factors but counts as one failed execution; do not infer another factor’s failure automatically.

### F3: Entire output is readable and easy to understand

Basis: [skill](../skill-original/SKILL.md) and owner’s [assessment policy](../../protocol.md#assessment-policy); no new subject instruction.
Coverage: O3; readability and coherent organization.
Dimension: functional
Applies to: `original`, `control`
Judgment unit: complete delivered document compared with the complete source.
Required evidence: Complete delivered document read in its intended context.
Met: The reader can readily follow the reasoning and connect the decision, evidence, limits and actions.
Not met: The complete document presents a concrete comprehension obstacle, such as unclear connections or instructions whose sequence is difficult to follow.
Insufficient evidence: available source/output evidence cannot settle this factor; identify the unresolved question rather than forcing a pass or failure.
Alternatives: faithful paraphrase, consolidation, relocation, useful repetition and any effective layout; no sentence-matching or preferred answer.
Consequence: Readability is required for an overall pass.
Overlap: a shared defect may affect multiple factors but counts as one failed execution; do not infer another factor’s failure automatically.

## Limits

All three functional factors must be met. Length is reported separately. Process is unscored; no P1 criterion applies.
The owner selected this rule after seeing the existing outputs. It is a transparent reassessment, not a prospectively frozen evaluation or independent confirmation.
Two short constructed software updates cannot establish performance on long documents, other audiences, discovery or plan/spec composition.
Per-case/condition counts describe the observed repetitions, not population reliability or an adoption decision.
