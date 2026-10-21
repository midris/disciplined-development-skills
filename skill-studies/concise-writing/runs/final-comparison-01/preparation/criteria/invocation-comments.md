# Native CW selection while editing code comments

## Identity and purpose

Format version: `1`
Study ID: `concise-writing`
Case ID: `invocation-comments`
Definition version: `4`
Status: final-comparison preparation; allocation approval and committed collection freeze remain required.
Purpose and realistic failure opportunity: Select CW for text inside source code and produce useful, faithful maintenance comments without changing executable behavior.
Scenario mechanism: Reuse the source case and supplied task, with two unchanged bodies sharing the selected description; natural availability measures selection separately from artifact quality.
Protocol coverage and membership/exposure: [protocol](../../../../protocol.md#suite-and-evidence); exposed development/regression case.

## Inputs and setup

All subject fixtures, prompts and selected skill versions are enumerated in the [configuration index](../configuration-index.json).
The [input provenance](../input-sources.json) preserves committed source bytes, including the pre-existing N2 notes fixture without modifying its unrelated working edit.
Both conditions use the [selected combinations](../../../../drafts/baseline-iteration/final-comparison/skill-identities.json).
Setup requires exact fixture/condition identity, qualified isolation, complete capture and retention.
Require available catalog and skill bytes, but do not exclude a missed, partial or late load; D1 records it.

## Rules and evidence

Apply [CW-expanded-1](../../../../protocol.md#expanded-suite-assessment-policy), the source [case definition](../../../../cases/invocation-comments/assessment.md) and the [prospective interpretation](../interpretation.md).
The criteria below retain the source factor meanings and extend applicability to the two complete combinations; explicit siblings omit native D1.
Read every complete task/source/notes/code input and the complete output before any functional judgment.
Equivalent wording, relocated meaning, effective layouts and useful reinforcement are accepted; an introduced inaccuracy fails F1 independently of F2/F3.
Unresolved consequential meaning remains insufficient evidence rather than automatically taking the stricter reading.
No-CW controls are absent: this is relative candidate performance, not a new claim of incremental CW benefit.
For comments, use the source --compare token/syntax check without executing subject-produced code; report comment-only lengths descriptively.
For N3, F1-F3 and CW effectiveness are not measured; retain exact numeric edits and the complete assistant-stream literal reply as task-only observations.
Other cases inherit their case-specific length treatment; counts never substitute for semantic assessment.
O4/O5 process remains unscored.

## Source-case rules and reader context

The following source rules supply reader purpose and case-specific length treatment; current applicability, explicit/native setup and the owner interpretation above take precedence over historical condition references.

The controller applies [CW-expanded-1](../../../../protocol.md#expanded-suite-assessment-policy) with this case card; historical policy-4 scores remain unchanged.

This is code-comment editing with supplied rationale, not a historical policy-4 editing reassessment.
Assess the complete resulting comments in code context against the source and maintenance notes, using prospective F1–F3 below.
Apply [native evidence](../../../suite-2026-09-27/preparation/README.md#native-evidence): only availability is arranged, never an explicit CW read request.
The full body must arrive before the first task comment edit; reading code/notes and the neutral baseline commit may precede loading.
Keep invocation and comment-quality outcomes separate, including missed/partial/late loads and insufficient capture.

Check that only # comments changed: compare the ordered non-comment Python tokens, including indentation and literals, and parse the complete source/output to detect syntax or executable changes.
Blank-line or comment placement differences alone do not establish changed behavior; executable token changes or added docstrings violate this task's editing boundary.
The controller-only [fixture checker](../../../../cases/invocation-comments/check_fixture.py) verifies four total sends on exhaustion, early success, non-temporary send failure and acknowledgement failure without retry, including TemporaryUploadError from record_ack.
These probes qualify the constructed source and the preservation check; they cannot establish comment quality or CW invocation.
Inspect subject outputs as data using token/syntax comparison; do not execute model-produced code to assess comments.
Run `python3 skill-studies/concise-writing/cases/invocation-comments/check_fixture.py --compare /absolute/path/to/output.py` from the repository root and retain its result with the assessment.
Exit 0 confirms executable-token preservation only; exit 1 identifies invalid syntax or changed tokens; exit 2 is an input/checker problem to resolve before scoring.
Judge comment meaning manually in the complete file; no required location, exact wording or one-comment-per-operation rule applies.
Record comment-only word counts separately from code and notes; useful new explanation may increase comment length without a failure.
Missing capture is uncertainty; a reliably missing required artifact is a task failure.
See [boundary checks](../../../suite-2026-09-27/preparation/boundary-checks.md).

## Criteria

### F1: Entire output remains correct

Basis: [skill](../../../../cases/skill-original/SKILL.md) and owner’s [assessment policy](../../../../protocol.md#assessment-policy); no new subject instruction.
Coverage: O1; source fidelity and meaningful qualifications.
Dimension: functional
Applies to: `original-body`, `revised-body`
Judgment unit: complete delivered comments in their code context, compared with the maintenance notes and original executable code.
Required evidence: Complete source, notes and output, with token/syntax comparison; the constructed source behavior is qualified separately.
Met: The complete code-and-comment artifact accurately conveys retry and acknowledgement behavior and preserves the supplied rationale; executable code remains unchanged. Facts already clear in the code need not be restated in comments.
Not met: Comments misstate the behavior or lose a consequential condition or rationale, or executable code changes; a missing required artifact is reliably established.
Insufficient evidence: available source/output evidence cannot settle this factor; identify the unresolved question rather than forcing a pass or failure.
Alternatives: faithful paraphrase, consolidation, relocation, useful repetition and any effective layout; no sentence-matching or preferred answer.
Consequence: Correctness is a primary gate; failure blocks overall success regardless of the other factors.
Overlap: a shared defect may affect multiple factors but counts as one failed execution; do not infer another factor’s failure automatically.

### F2: Comments support safe maintenance

Basis: [skill](../../../../cases/skill-original/SKILL.md) and owner’s [assessment policy](../../../../protocol.md#assessment-policy); no new subject instruction.
Coverage: O1–O3 applied to maintenance text in a source file.
Dimension: functional
Applies to: `original-body`, `revised-body`
Judgment unit: complete delivered comments in their code context, compared with the maintenance notes and original executable code.
Required evidence: Complete code/comments/notes comparison for the next maintainer.
Met: A maintainer can identify the retry limit and error boundary and understand why acknowledgement failures must not resend an accepted batch, without reconstructing the separate notes.
Not met: The comments omit or obscure the maintenance trap, such as describing acknowledgement as retryable or failing to explain the risk of sending an already accepted batch again. Identify the practical loss.
Insufficient evidence: available source/output evidence cannot settle this factor; identify the unresolved question rather than forcing a pass or failure.
Alternatives: faithful paraphrase, consolidation, relocation, useful repetition and any effective layout; no sentence-matching or preferred answer.
Consequence: Serving the stated reader purpose is required for an overall functional pass.
Overlap: a shared defect may affect multiple factors but counts as one failed execution; do not infer another factor’s failure automatically.

### F3: Comments are readable in code context

Basis: [skill](../../../../cases/skill-original/SKILL.md) and owner’s [assessment policy](../../../../protocol.md#assessment-policy); no new subject instruction.
Coverage: O3; readability and coherent organization.
Dimension: functional
Applies to: `original-body`, `revised-body`
Judgment unit: complete delivered comments in their code context, compared with the maintenance notes and original executable code.
Required evidence: Complete output file read as a maintainer, with concrete evidence of useful explanation or needless narration.
Met: The comments and code together make the relevant limit, error boundary and rationale easy to follow without needless narration of obvious statements or purposeless repetition; useful reinforcement is allowed.
Not met: Comments bury the maintenance guidance in obvious line-by-line narration, repeat it without purpose or disconnect the warning from the code it explains. Identify the reader burden rather than counting comments or words.
Insufficient evidence: available source/output evidence cannot settle this factor; identify the unresolved question rather than forcing a pass or failure.
Alternatives: faithful paraphrase, consolidation, relocation, useful repetition and any effective layout; no sentence-matching or preferred answer.
Consequence: Readability is required for an overall pass.
Overlap: a shared defect may affect multiple factors but counts as one failed execution; do not infer another factor’s failure automatically.
### D1: Timely native selection

Basis: Owner-selected task and [behavioral contract](../../../../protocol.md#behavioral-contract-and-consumers).
Coverage: Native code-comment writing/editing trigger
Dimension: procedural
Applies to: `original-body`, `revised-body`
Judgment unit: Native selection, delivered body and task-writing sequence
Required evidence: Qualified catalog/description availability, exact skill identity and complete ordered model-visible events.
Met: The complete CW body is delivered before the first task comment edit, without an explicit task-level loading request. Initial reading and the neutral baseline commit may precede the load.
Not met: With valid availability and complete capture, CW is never loaded, only partly loaded before writing, or fully loaded only after writing starts. Report missed, partial and late separately.
Insufficient evidence: Missing or conflicting capture prevents establishing the required evidence; identify the gap rather than inferring success or failure.
Alternatives: Equivalent wording, structure and tool use are accepted where they preserve the stated outcome; no hidden preferred answer.
Consequence: D1 is separate from functional outcomes; successful prose cannot substitute for loading. No invocation-rate reliability claim.
Overlap: A shared cause may affect multiple criteria but is one execution; report invocation and task outcomes separately.


## Limits

Three repetitions per condition/provider are diagnostic, not a reliability or equivalence estimate.
Native selection and output quality have separate denominators; N3 supplies no CW functional score.
The owner accepts surplus loading as a caution where output remains intact; retain D1 misses and any demonstrated output consequences without automatic rejection solely for loading.
The source case and operative interpretation define the reader purpose and functional boundary; no new answer template or literal phrase is required.
