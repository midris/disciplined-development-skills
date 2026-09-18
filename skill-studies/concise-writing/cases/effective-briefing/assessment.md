# Search-preview briefing

## Identity and purpose

Format version: `1`
Study ID: `concise-writing`
Case ID: `effective-briefing`
Definition version: `1`
Status: accepted for contribution-baseline-01; fixed criteria ready for committed input freeze.
Purpose and realistic failure opportunity: Test whether CW preserves an already-effective briefing, including useful explanation and reinforcement, rather than damaging it through unnecessary compression.
Protocol coverage and membership/exposure: [suite](../../protocol.md#suite-and-evidence), selected development case B, O1–O4; O5 only when explicit uncertainty is observable. Author and assessor share construction history; no held-out or independent-validation claim.

## Inputs and setup

Subject inputs: [task](task.md) and the complete [source document](fixture/report.md), mounted as `report.md` in a disposable workspace. Original additionally receives the exact [preserved CW skill](../skill-original/SKILL.md); control receives no target skill. Other runtime context must match. Prepared inputs: [original configuration](original.json), [control configuration](control.json) and [input manifest](manifest.json); the protocol contains the exact collection commands and offline checks. Collection is approved; committed input freeze and readiness checks remain outstanding.
Controller-only: this definition, examples and the [qualification record](../../qualification.md). Do not expose them or the protocol to subjects. Both sources are fictional, constructed in the active session for this study; neither is an observed model output or an actual project report. All factual authority is supplied in the source; subjects edit prose and do not execute the actions it describes.
Setup validity requires evidence of the intended source bytes, correct skill condition, matched surrounding context, writable output path and captured final workspace. A capture/setup fault that prevents assessment is excluded and charged under the eventual batch scope, not a CW failure. With valid setup, judge the captured final file under the criteria below; unchanged bytes alone are not an outcome defect. Resolve uncertain setup separately before assigning criterion outcomes.

## Rules and evidence

Policy: [CW-assessment-1 controller copy](../../assessment-policy.txt), derived verbatim from the [protocol policy body](../../protocol.md#current-cw-assessment-policy); exact policy, criteria and input identities must be pinned by the input manifest before collection.
Inspect the complete source and final saved `report.md` before judging. If that file remains unchanged or is only partly edited, assess its actual contents under each criterion; an unsaved edit in a completion message does not replace it. Record delivery claims and process evidence separately rather than assigning blanket functional failures. If reliable evidence establishes that the subject left `report.md` absent or empty, F1–F3 are not met because no document remains to serve the required functions. If capture is incomplete, follow the setup/uncertainty rule above rather than inferring absence or failure. Execution evidence takes precedence over self-reports. File comparison and optional `wc -w` provide mechanical facts only; no lexical matching, compression target, heading count or preferred layout determines success.
The source is the factual authority. The contextual notes below identify discriminators, not an exhaustive list of independently scored sentences. Preserve all substantive information and useful communicative functions, allowing consolidation, paraphrase and relocation. Different layouts and lengths may pass. Examples illustrate boundaries, not required answers. Unknown judgment remains insufficient evidence, never silently a pass or a failure.

### Contextual expectations

The source already supports a Thursday decision with a visible recommendation, bounded evidence, ordered prerequisites and follow-up. This case tests restraint: leaving it unchanged can pass all functional criteria. An effective alternative need not preserve its headings or exact repetition.

| Source location | Expected semantic effect and valid alternatives |
|---|---|
| Opening and closing | Keep the distinction between inviting four teams and making the preview the default easy to find. Six teams may continue; the preview stays opt-in. The closing recap helps a decision reader return to the question after evidence and conditions. It can be replaced or consolidated if that orienting function survives. |
| “What we learned” | Preserve the week, six teams, 120 searches, two timeouts both successful on retry, no evidence of lost documents, three filter questions and no reports of incorrect results. Absence of reports does not establish correctness. Do not turn absent evidence into proof. |
| Collection-size rationale | Preserve the untested over-50,000-document boundary, proposed teams each below 20,000, and why that broadens feedback without validating large collections. Do not imply every collection size below 50,000 has been tested. |
| “Before inviting anyone” | Preserve Nia’s consent and switch-back checks, Omar’s timeout check, and the exact postponement condition: greater than 5% over the preceding 24 hours. Investigate before reconsidering. Checks and Thursday approval precede Nia’s invitations. |
| Invitation/default distinction and follow-up | Preserve off-by-default and invited teams’ choice, plus review after seven days of timeout data and feedback. Success does not authorize automatic expansion. Repeated scope reminders serve decision, execution and recap contexts; faithful consolidation is allowed. |

The [effective alternative](examples/effective.md) changes wording and presentation while retaining those functions. Neither change for its own sake nor a reduction in word count is necessary to pass.

## Criteria

### F1: Preserve meaning and useful framing

Basis: [skill](../skill-original/SKILL.md), core test and When NOT to cut; owner-approved preservation requirement in the protocol. The ordinary editing task does not repeat this skill guidance.
Coverage: O1; contextual expectations above.
Dimension: functional
Applies to: `original`, `control`
Judgment unit: complete delivered document.
Required evidence: source and delivered file, with specific passages supporting preservation or loss.
Met: substantive information, uncertainty, reasons and useful framing remain faithful and usable; no unsupported assertion changes the meaning.
Not met: a substantive fact, condition, reason or necessary framing is lost, distorted or replaced by an unsupported claim. A shorter output is no compensation.
Insufficient evidence: retained source/output evidence is insufficient to resolve a consequential semantic question; identify the unresolved point.
Alternatives: consolidated, relocated or differently worded information and functionally equivalent emphasis; see shared rules.
Consequence: blocks the functional summary because the user can no longer rely on the document as a faithful edit.
Overlap: F2 assesses avoidable burden and F3 presentation; one shared defect may explain multiple criteria but counts as one failed execution.

### F2: Remove avoidable verbosity in context

Basis: skill core test, two-altitude pass and named verbosity patterns; owner rejects mechanical minimization.
Coverage: O2; contextual expectations above.
Dimension: functional
Applies to: `original`, `control`
Judgment unit: complete delivered document, including relationships across sections.
Required evidence: full source/output comparison and the function or avoidable burden of disputed text.
Met: no clear noncontributing padding or purposeless duplication remains; retained explanation, emphasis and context have a reader-facing purpose.
Not met: identifiable empty narration, unhelpful restatement, scattered duplicate explanation or noncontributing elaboration remains. Name the passage and why it adds no information or useful framing; length alone is not evidence.
Insufficient evidence: the reader purpose of a disputed passage cannot be established from the task and source; do not force a cut judgment.
Alternatives: different lengths, useful repeated warnings, and unchanged already-effective text can pass; neither maximal compression nor deletion of a particular sentence is required.
Consequence: blocks the functional summary for leaving an actual concision defect; no word-count bonus or penalty.
Overlap: harmful cutting fails F1 even when the remaining prose meets F2; removing padding alone does not establish F3.

### F3: Support clear reading and the intended decision

Basis: skill’s easy-to-read goal and treatment of structure; owner-resolved target to improve difficult organization in the protocol; task’s decision purpose. No specific order or restructuring procedure is attributed to the original.
Coverage: O3; contextual expectations above.
Dimension: functional
Applies to: `original`, `control`
Judgment unit: complete document as consumed by its intended reader.
Required evidence: delivered document’s organization and connections, assessed against the source’s stated reading difficulty or existing effectiveness.
Met: the reader can readily locate and connect the decision, evidence/limits, prerequisites and next action; a poor source’s structural difficulty is resolved, or an effective source’s usability is maintained.
Not met: the edit leaves or introduces a concrete reading obstacle, such as burying the decision among fragmented details or scattering dependent instructions so the sequence is hard to follow. Explain the actual obstacle, not a layout preference.
Insufficient evidence: the task/context does not settle whether a claimed reading obstacle affects this reader; record that limitation.
Alternatives: any effective section order, heading scheme, paragraphing or bullets; no obligation to change an already-effective source.
Consequence: blocks the functional summary because faithfully retained facts alone do not deliver the requested usable document.
Overlap: F1 owns semantic loss; do not automatically fail F3 whenever F1 fails. Fail both only where a distinct reading/use obstacle is demonstrated.

### P1: Apply the prescribed editing process

Basis: skill two-altitude pass and instructions to draft first and diff against the source.
Coverage: O4. Record O5 as a conditional observation under the limits below.
Dimension: procedural
Applies to: `original`
Judgment unit: observed editing execution.
Required evidence: available actions/files showing drafting before finalization, local and whole-document review and an actual source/edit comparison. Self-reported completion alone is insufficient.
Met: retained actions support the required drafting, comparison and both review scopes.
Not met: affirmative evidence establishes an omitted step, such as an explicit choice to skip comparison; distinguish this from an unobserved internal review.
Insufficient evidence: the trace does not establish whether one or more steps occurred; a good final document alone cannot establish process compliance.
Alternatives: no prescribed diff tool or three-file workflow. A draft in the working file followed by a source comparison can satisfy the procedure; equivalent observable comparisons are acceptable.
Consequence: visible and non-blocking for the functional summary under the owner-approved policy. Control has no target-skill process obligation.
Overlap: actual artifact harm belongs under F1–F3; procedural failure adds no second failed execution.

## Limits

This is constructed development material, exposed to its author/assessor. Semantic expectations are judgment rules, not automated verdicts or an independent evaluation. The [qualification record](../../qualification.md) checks concrete boundaries without provider calls; its examples are not observed skill behavior.
No uncertain framing/padding choice is deliberately required here. O5’s keep-and-flag instruction is therefore not a separate criterion: record it if the trace explicitly shows unresolved uncertainty and a keep/flag decision, but do not infer hidden uncertainty from assessor disagreement. This leaves that conditional behavior incompletely tested.
These two software-oriented updates do not establish performance on long documents, other audiences, plan/spec composition, discovery or broader prose genres. Per-case/condition repetition aggregates and limitations belong in the eventual batch assessment; no numerical reliability threshold is selected.
