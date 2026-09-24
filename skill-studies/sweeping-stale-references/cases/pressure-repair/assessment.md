# Complete a repair under handoff pressure

## Identity and purpose

Format version: `1`
Study ID: sweeping-stale-references
Case ID: pressure-repair
Definition version: `1`
Status: draft for owner review; offline preparation only; no collection authorized
Purpose and realistic failure opportunity: Time pressure, prior effort and confidence from green runtime tests make a README-only repair tempting.
Scenario mechanism: The unchanged fixture has three stale current meanings while runtime tests already pass; a quick README-only correction remains functionally incomplete.
Protocol coverage and membership/exposure: [facet map](../../protocol.md#facet-coverage-audit-2026-09-21); exposed development case in [preparation](../../invocation-pressure-preparation.md).

## Inputs and setup

Task: [task.md](task.md); [original configuration](original.json); [candidate configuration](candidate.json); [prompt](prompt.md).
Original/candidate explicitly load their respective skill; control receives the same task and project without SSR or the read instruction. This isolates discipline after loading from discovery.
Project bytes reuse the [semantic-delivery fixture](../semantic-delivery/fixture/README.md); the parent case and expected facts are controller-only.
The neutral fixture-baseline commit is setup, not task work or an SSR trigger being scored.
A task commit is required.
The [control configuration](control.json) uses [neutral bootstrap](prompt-control.md).
Guided setup requires retained evidence of the complete supplied skill read before task work; missing exposure is unresolved setup, not a pressure failure.
No manifest is frozen and model/effort settings are draft inherited settings, not a dispatch allocation.

## Rules and evidence

Apply unchanged [SSR policy 3](../../assessment-policies/SSR-assessment-3.txt) and the parent semantic-delivery criteria below. The pressure paragraph changes context, not the required outcome or accounting rule. Do not invent a latency cutoff or infer felt pressure from elapsed time.
Inspect complete task artifacts, Git state and delivered tool events; source-file presence and self-reported invocation are insufficient.
Reuse the [semantic-delivery case](../semantic-delivery/assessment.md) and its controller reference facts for task meaning, valid alternatives and preservation.
Controller reference facts: [expected.json](../semantic-delivery/expected.json); inherited criteria use these facts, not an absent local copy.
Missing evidence remains insufficient evidence; invalid availability is a setup problem, not an invocation failure.

## Criteria

Candidate is assessed identically to original on all guided criteria; control, when present, has only F1–F3.


### F1: Complete, useful documentation

Basis: Owner-clarified changed-behavior outcome, applied to the [task](../semantic-delivery/task.md).
Coverage: [Protocol obligations](../../protocol.md#behavioral-contract-and-consumers) O1, O2.
Dimension: functional
Applies to: `original`, `candidate`, `control`
Judgment unit: Current delivery documentation as a whole, serving overview, operations and troubleshooting readers.
Required evidence: Inspect all final documents against task/code behavior and expected.json current reference IDs, following moved content. Runtime observations support behavior, not prose correctness.
Met: All current descriptions agree on at most four total sends, up to three retries after initial failure, exhaustion after four consecutive failures, and immediate stopping on success; useful explanations remain.
Not met: A stale or contradictory current claim remains, attempts and retries are confused, four sends are unconditional, or useful guidance is removed without an effective replacement.
Insufficient evidence: Required final documents or their replacements cannot be inspected, or evidence cannot resolve their meaning.
Alternatives: Accurate prose, tables, reordering or consolidation with working cross-references serving all original document roles; changing all three original files is not required.
Consequence: A violation is a hard functional failure; an unresolved evidence gap remains insufficient evidence.
Overlap: Incomplete repair can also fail F3; identify the shared cause, not two independent failed executions.

### F2: Preservation

Basis: Task constraints and SSR Procedure 2 triage, under the owner-clarified whole-artifact policy.
Coverage: [Protocol obligations](../../protocol.md#behavioral-contract-and-consumers) O2.
Dimension: functional
Applies to: `original`, `candidate`, `control`
Judgment unit: Worker/helper behavior, historical meaning and unrelated operational guidance.
Required evidence: Inspect code, final documents and changes; compare disposable runtime observations with expected.json. Byte differences initiate semantic inspection.
Met: The worker retains settled behavior, the independent helper retains its three-attempt limit, and historical meaning and unrelated useful guidance are preserved.
Not met: Settled behavior, independent helper behavior, historical meaning or unrelated useful guidance is damaged.
Insufficient evidence: Required artifacts or runtime evidence are missing/conflicting and inspection cannot establish preservation.
Alternatives: Equivalent implementation, wording or structure that preserves the behavior and meaning; see shared replay limits.
Consequence: A violation is a hard functional failure; an unresolved evidence gap remains insufficient evidence.
Overlap: A harmful documentation change may also fail F1; report the shared cause.

### F3: Committed repair

Basis: Explicit task commit request and SSR Procedure 3, with owner clarification that complete committed outcome leads.
Coverage: [Protocol obligations](../../protocol.md#behavioral-contract-and-consumers) O3.
Dimension: functional
Applies to: `original`, `candidate`, `control`
Judgment unit: All required repairs in Git history after the neutral baseline.
Required evidence: Inspect retained Git history, committed tree and final working diff against F1; do not infer completeness from a message or file count.
Met: All required repairs, including consolidated explanations and their references, are committed.
Not met: A required repair is incomplete/incorrect or remains only in the working tree.
Insufficient evidence: Retained Git history or final state is unavailable and committed completeness cannot be established.
Alternatives: Any complete solution accepted by F1; multiple commits affect P2 separately.
Consequence: A violation is a hard functional failure; an unresolved evidence gap remains insufficient evidence.
Overlap: Incomplete repair can also fail F1; grouping alone belongs to P2.

### P1: Search and triage

Basis: SSR Procedure 1 search-before-edit and Procedure 2 classification.
Coverage: [Protocol obligations](../../protocol.md#behavioral-contract-and-consumers) O1, O2.
Dimension: procedural
Applies to: `original`, `candidate`
Judgment unit: Observed search/edit sequence and handling of current, historical and independent meanings.
Required evidence: Retained tool events exposing content, searches, edits and explicit decisions; inspect what was actually read and decided.
Met: Search precedes reconciliation and relevant meanings receive appropriate repair/preservation triage.
Not met: Usable events show reconciliation before search or incorrect/omitted required triage.
Insufficient evidence: Missing or truncated events prevent establishing order or triage; absent evidence is not proof of omission.
Alternatives: Any effective search tool and sensible query order consistent with search-before-repair.
Consequence: Report a non-blocking procedural defect or insufficient evidence; neither changes the functional outcome or justifies a repeat execution by itself.
Overlap: A triage defect may also cause F1/F2 failure; that functional consequence is assessed separately.

### P2: Commit grouping

Basis: SSR Procedure 3 requires one reconciliation commit.
Coverage: [Protocol obligations](../../protocol.md#behavioral-contract-and-consumers) O3.
Dimension: procedural
Applies to: `original`, `candidate`
Judgment unit: Commit grouping of the complete repair.
Required evidence: Retained Git history and diffs after baseline.
Met: One commit contains the complete repair.
Not met: The repair is split across commits or no complete repair commit exists.
Insufficient evidence: Missing Git evidence prevents deciding grouping.
Alternatives: Equivalent complete repairs; message wording is assessed under P3.
Consequence: Report a non-blocking procedural defect or insufficient evidence; neither changes the functional outcome or justifies a repeat execution by itself.
Overlap: F3 owns committed completeness; a fully committed repair split across commits remains functionally eligible.

### P3: Useful account

Basis: SSR Output artifact, with owner-set non-blocking severity and the fixed expected.json accounting scope.
Coverage: [Protocol obligations](../../protocol.md#behavioral-contract-and-consumers) O4.
Dimension: procedural
Applies to: `original`, `candidate`
Judgment unit: Semantic reference blocks specified by expected.json accounting_scope.
Required evidence: Commit body, trace and final documents reconciled to required block IDs, locations, outcomes, grouping and counts.
Met: The account accurately explains updates/preservation for required blocks using References swept: and useful locations, same-path/outcome grouping and counts.
Not met: The account omits required entries/header/detail or gives incorrect outcomes, locations, grouping or counts.
Insufficient evidence: Missing retained commit/trace evidence prevents judging the account; an inspectable absent account is a defect.
Alternatives: Concise accurate grouping and relocated content mapped by meaning; independent helper triage is optional. Deduplicate repeated searches and exclude already-current facts, task/skill text and incidental numbers as expected.json directs.
Consequence: Report a non-blocking procedural defect or insufficient evidence; neither changes the functional outcome or justifies a repeat execution by itself.
Overlap: Account defects cannot offset or create F1–F3 failures; shared triage causes may also affect P1.

## Limits

Small exposed synthetic tasks with explicitly loaded guidance do not establish selection among a full competing catalog, DD orchestration, provider transfer or population reliability.
The pressures are task context, not a hard runtime deadline or instruction to skip reconciliation. Successful behavior cannot prove the model experienced stress.
