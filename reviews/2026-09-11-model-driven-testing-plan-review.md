# Fresh testing framework: plan and specification review

Status: record of the completed internal reviews below.
Claude's subsequent external review remains open, with a consolidated response in the [current plan](../plans/2026-09-11-model-driven-skill-testing.md); the PASS verdict below does not close that later review.
Earlier task numbers and layout descriptions below refer to the revisions reviewed at the time, not the current six-stage checklist.

Reviewed the [plan](../plans/2026-09-11-model-driven-skill-testing.md) and [specification](../plans/specs/2026-09-11-model-driven-skill-testing-framework.md) for consistency, executability, evidence quality and unnecessary prerequisites.
This was an in-session self-review, followed by a review of the corrections; it was not an independent evaluation or an empirical validation of the framework.
The scope included current tooling capabilities and skill instructions relevant to the proposed workflow.
Historical scenarios, rubrics and grades were not used as design authority.

## Initial review findings and resolutions

| Finding | Consequence | Resolution in both documents |
|---|---|---|
| P1: Reserved tests lacked a complete exposure rule. | Calibration, baseline reporting or the author's existing context could reveal tests later described as independent transfer evidence. | Reserve cases before calibration/pilot; use a fresh author context with declared inputs; exclude revealing results from the author's report; reclassify exposed cases as development evidence. Fix the candidate before revealing reserved results to its author. |
| P2: Calibration lacked a concrete readiness decision. | Repeated evaluator agreement could be mistaken for correct interpretation. | Establish source-supported reference judgments and a declared readiness rule before calibration. Unresolved consequential errors require repair and recalibration or an owner-agreed scope reduction. |
| P2: Rewrite comparisons did not explicitly control for model/runtime drift. | A difference between an old baseline and a later rewrite could be attributed to the skill without support. | Capture available versions, compare the original and candidate contemporaneously, and investigate material drift. Include a contemporary no-target control for claims of current benefit over unguided behavior. |
| P2: Task ordering could make full archival a prerequisite for fresh design. | Historical migration complexity could stall the first skill's contract and tests. | Establish the minimum workspace/archive boundary early and continue preservation alongside design; block only dependent actions or removal of unverified originals. |

The follow-up review checked that these rules agree across the specification and execution tasks, including the order of starting the fresh author context before authoring.
No unresolved actionable findings remained in this document review.

## Verification and limits

- Hook suite: `python3 -m pytest -q` in `skills/disciplined-development/hooks` — 263 passed, 3 skipped.
- Checked local document links and whitespace in the reviewed files.
- Checked that this work changed no skill bodies or runner files.

These checks support the document changes and repository integrity; they do not establish evaluator reliability or skill effectiveness.
Candidate choice, collection budget, repetition policy, calibration thresholds and rewrite acceptance boundaries remain explicitly assigned to the candidate study.
No provider experiment, archive migration or skill rewrite was performed by this review.

## Additional executability and consistency review

The owner requested another review focused on an implementer without conversation history.
This was an in-session walkthrough of the written handoffs, not a separately launched fresh-context agent or an implementation trial.

| Finding | Correction |
|---|---|
| P1: Active entry points still routed to the old charter, plan and record-update workflow. | Reconciled `CLAUDE.md`, `README.md` and `ARCHITECTURE.md`; added an explicit historical boundary to `skill-validation/README.md`. The plan distinguishes the runner's mechanics from its optional legacy worksheet conventions. |
| P2: Resumption depended on conversation knowledge of artifacts, decisions and temporary material. | Added starting/resuming instructions, decision and authorization provenance, links to evidence and the next authorized action, and the known scratch location for preservation. Kept author handoffs separate from reserved-case content. |
| P2: The pilot-to-baseline handoff did not explicitly require a runnable record. | Required exact inputs, commands, setup, evidence checks and case/condition/repetition-to-attempt mapping before dispatch. Reuse that record for baseline and comparison; prepare the concrete proposal before obtaining any additional authorization. |
| P2: `writing-skills` evidence requirements were first read at the authoring task. | Read them in Task 1 so they inform suite design; re-read and reconcile changes before rewriting. |

Walked the full dependency chain after the corrections:

| Handoff | Written path and completion boundary |
|---|---|
| Start → foundation | Current entry points lead to this plan/spec; Task 1 can begin with read-only inspection and ends with an owner-selected skill and identified sources. |
| Foundation → contract | Tasks 1 and 3 cover behavioral-contract layer 1; Task 2's archive migration proceeds alongside fresh design. |
| Contract → tests and evaluation | Task 4 covers layers 2 and 3 with two-way coverage, evidence requirements and early reserved-case separation. |
| Proposed tests → runnable study | Tasks 5 and 6 cover layer 4 with calibration readiness, qualified mechanics, concrete run records and bounded authorization. |
| Study → baseline | Tasks 6 and 7 cover layers 5 and 6 with retained attempts, frozen criteria, supported judgments and a permitted author report. |
| Baseline → rewrite and decision | Tasks 8 and 9 cover layer 7 with an agreed objective, appropriate author context, fixed candidate, contemporary controls and owner adoption decision. |
| First skill → reusable framework | Task 9 requires a contrasting second application before standardizing conventions or adding recurring mechanical tools. |

The consistency pass checked scope, terminology, task order, completion status, approval persistence, source identity, information boundaries and spec-to-plan coverage.
Candidate-dependent choices remain assigned to named tasks with prerequisites; they do not prevent starting the foundation inventory.
The corrected walkthrough left no unresolved actionable findings.
Fresh verification: hook suite — 263 passed, 3 skipped; current document links and whitespace checked; skill bodies and runner files unchanged.

## Abandoned testing-process reference cleanup

The owner clarified that prior testing frameworks and pending workflows are abandoned, with existing runner documentation and core skill documentation retained.
The reference sweep therefore covered project navigation, framework plans/specs, CW process reviews, validation-directory entry points and known continuation handoffs.

- Added explicit abandonment notices and current spec/plan links to 49 historical project documents: 39 plans/specs, three CW reviews, six validation entry documents and `scratch.md`.
- Marked both known temporary continuation handoffs so their former approvals cannot be mistaken for instructions to resume.
- Made the abandonment explicit in current project entry points and the fresh spec/plan; added a historical-results notice at `skill-validation/accepted/README.md`.
- Preserved historical bodies, status labels and references beneath the notices rather than rewriting the evidence of what happened.
- Left runner documentation, core skills, their implementation histories and raw test evidence unchanged; matches in those excluded documents do not activate an abandoned framework.

Verification checked all 49 original project-document bodies and both handoff bodies byte-for-byte after removing only the inserted notices, and confirmed the new notice links resolve.
The final consistency pass checked the current routes and the historical/current boundary; no unresolved actionable findings remained in this cleanup scope.
The hook suite passed with 263 passed and 3 skipped, and `git diff --check` passed.
Physical archive migration remains separate work; this change makes the retained locations unambiguous now.

## Response to Claude's second external review

The repeated failure was adding another execution structure while retaining the first.
The plan has been rewritten from 3,987 to 1,636 words with one six-stage checklist, one workspace and one next action; the nine tasks and overlaid proposal were removed.
`protocol.md` now holds study-specific facts, decisions and evidence links, without a second checklist.

The spec's calibration rule now distinguishes checked properties from model judgments actually used, and its status explicitly governs preparation while reserving execution authority to recorded owner decisions.
The plan proposes a 60-call, five-calendar-day outer limit, pending owner confirmation, and requires removing or combining unhelpful framework work when that limit is reached.
Reserved material belongs outside the main repository and its history, with access restrictions verified before transfer claims; a separate branch alone does not qualify.

The runner worksheet link remains unchanged under the owner's explicit instruction to leave runner documentation intact; the plan and abandoned target document state its historical status.
This is an accepted scope limit on the P3 finding, not a claim that the link was removed.
The documentation reset is being preserved separately from the old untracked test inputs; Git history is the evidence of its commit state.
The source-preservation and link checks passed, and the hook suite passed with 263 passed and 3 skipped.
External reviewer acceptance and owner confirmation of the candidate/limits remain open; the earlier internal PASS below is not their substitute.

DD-VERDICT: PASS
