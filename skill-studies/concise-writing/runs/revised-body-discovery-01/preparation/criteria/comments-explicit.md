# Explicit-load CW comparison while editing code comments

## Identity and purpose

Format version: `1`
Study ID: `concise-writing`
Case ID: `comments-explicit`
Definition version: `3`
Status: prospective focused-round applicability; use the interpretation supplement below with unchanged F1–F3 meanings.
Purpose and realistic failure opportunity: Apply loaded CW to source comments without losing retry/acknowledgement rationale or changing executable behavior.
Scenario mechanism: Existing comments narrate obvious operations while missing the acknowledgement/retry distinction; repeated source notes tempt needless duplication, and over-trimming can erase the reason acknowledgement failure must not resend a batch.
Protocol coverage and membership/exposure: [suite map](../../../../protocol.md#suite-and-evidence); development case. Same-session author/assessor exposure; no independent or held-out claim.

## Inputs and setup

[Task](../../../../cases/invocation-comments/task.md), [source](../../../../cases/invocation-comments/fixture/uploader.py) and authoritative [maintenance notes](../../../../cases/invocation-comments/fixture/MAINTAINER-NOTES.md).
Provider/condition mappings: [schedule](../schedule.json); [preparation](../README.md).
Criteria, worked boundary examples and preparation records are controller-only; configurations enumerate every supplied file.
The protocol links provider-specific manifests and runtime qualification; this card supplies no independent dispatch authority.
Require exact source/task/condition identities, retained complete artifacts and trace.
Explicit-load skill conditions require full body delivery before editing; native cases qualify availability and then measure selection rather than excluding misses.

## Rules and evidence

The controller applies [CW-expanded-1](../../../../protocol.md#expanded-suite-assessment-policy) with this case card; historical policy-4 scores remain unchanged.

This is code-comment editing with supplied rationale, not a historical policy-4 editing reassessment.
Assess the complete resulting comments in code context against the source and maintenance notes, using prospective F1–F3 below.
For the separate native stratum, apply [native evidence](../../../suite-2026-09-27/preparation/README.md#native-evidence): only availability is arranged, never an explicit CW read request.
In skill conditions, the full body must arrive before the first task comment edit; controls have no CW body.
Native D1 is not measured in this explicit-load sibling.

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
Applies to: `control`, `original`, `candidate-targeted-examples`
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
Applies to: `control`, `original`, `candidate-targeted-examples`
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
Applies to: `control`, `original`, `candidate-targeted-examples`
Judgment unit: complete delivered comments in their code context, compared with the maintenance notes and original executable code.
Required evidence: Complete output file read as a maintainer, with concrete evidence of useful explanation or needless narration.
Met: The comments and code together make the relevant limit, error boundary and rationale easy to follow without needless narration of obvious statements or purposeless repetition; useful reinforcement is allowed.
Not met: Comments bury the maintenance guidance in obvious line-by-line narration, repeat it without purpose or disconnect the warning from the code it explains. Identify the reader burden rather than counting comments or words.
Insufficient evidence: available source/output evidence cannot settle this factor; identify the unresolved question rather than forcing a pass or failure.
Alternatives: faithful paraphrase, consolidation, relocation, useful repetition and any effective layout; no sentence-matching or preferred answer.
Consequence: Readability is required for an overall pass.
Overlap: a shared defect may affect multiple factors but counts as one failed execution; do not infer another factor’s failure automatically.
## Limits

N4 is a positive counterpart to N3: comments are in scope when edited; a nearby numeric-only change is not comment editing.
Report native comment-editing outcomes separately from N2 report generation and the ordinary explicit-load comparison.
This explicit-load sibling includes a no-CW control; it tests body contribution and does not score native D1.
This small Python file does not establish coverage of all languages, docstrings, generated code or response-only text.
O4/O5 remain unscored process observations.

## Focused-round interpretation supplement

Apply [prospective boundaries](../interpretation.md) to the complete artifact; no literal phrase or preferred layout is required.
