# Semantic drift: notification delivery policy

## Identity and purpose

Format version: `1`
Study ID: `sweeping-stale-references`
Case ID: `semantic-delivery`
Definition version: `1`
Status: prepared; collection authorization pending.
Purpose: observe reconciliation of differently worded documentation after a settled behavior change.
Coverage and development exposure: [protocol suite](../../protocol.md#proposed-baseline-case-selection); O1–O4, with no O5/local-change claim.
This study-authored case uses earlier pilot bootstrap mechanics; [preparation](preparation.json) records the source inspection and reuse decision.

## Inputs and setup

Task: [task.md](task.md); configurations: [original](original.json), [control](control.json); input identities: [manifest](manifest.json).
The task states that the delivery worker now permits one initial attempt plus up to three retries, stopping on success, and flags one contradictory README claim.
It permits project edits and requests a commit without instructing a sweep or naming other consumers.
`fixture/` is a compact local Python project with no packages or network service to install.
Identifiers and paths remain stable; the application code and tests already implement the settled behavior.
Three current reference blocks express the stale policy as total attempts, additional tries and exhaustion after failures.
The completed migration note describes the former policy accurately; a separate helper's three-attempt behavior and documentation remain current.
The README links to the ordinary operational docs. Discovery difficulty is not an objective of this small case.

Both configs supply identical project/task bytes. Original alone adds the frozen `../skill-original/SKILL.md` and a full-read instruction; DD and sibling guidance are not supplied.
The inherited pilot-02 bootstrap records a neutral `fixture baseline` before repair. TASK.md and guidance are excluded from project commits but retained as inputs.
The case criteria, policy copy, expected outcomes, probe, constructed variants and qualification records are controller-only.
Declared-input parity is not proof of host-wide read isolation: inspect actual subject traces for outside guidance, missing-skill stops and task feasibility before accepting attribution.

Setup: verify input/settings identities, identical initial trees, full original read, control guidance integrity and usable traces.
Record absent-guidance probes without treating them alone as contamination; setup faults invalidate attribution, not skill behavior.

## Rules and evidence

Apply [policy 3](assessment-policy.txt), pinned by the manifest, and the [expected facts](expected.json) for reference/accounting scope, alternatives and runtime observations.
Git establishes committed state; tool events establish observable action order; inspect document meaning directly.
Missing evidence limits the affected criterion; self-reports and passing runtime tests cannot substitute for artifact inspection.
Control procedure is descriptive only; no undisclosed target-format obligations apply.
The [protocol](../../protocol.md#assessment-policy) owns functional/procedural consequences and batch interpretation.

After inspecting the supplied code and all changes, make a disposable replay copy and invoke the controller-owned tool:

```sh
python3 -I -B probe_behavior.py /absolute/path/to/disposable-fixture
```

The probe runs fresh modules using the case's public operations and deterministic local transports. It records actual calls and returned booleans independently of the subject's test suite.
It does not parse or score documentation, check preservation semantics, or inspect Git; those require separate evidence and judgment.
`observed` means runtime facts were captured, not that the behavior or task passed. Compare observations with expected.json, not with subject self-reports.
Missing APIs, import errors, timeouts and unexpected or incomplete output require inspection; unknown observations are not zero attempts or proof of behavioral failure.
The child uses isolated imports and a bounded timeout, not a security sandbox. Inspect before executing; use only disposable copies. Supporting a changed public API or additional imports may require an explicit inspection/replay amendment rather than rejection of an otherwise valid refactor.

`qualification-variants.json` defines nine complete reconstructions from fixture bytes and exact replacements. The controller references distinguish pristine/README-only work, a complete repair, blanket numeric replacement, attempts-versus-retries confusion, always-four wording, removed guidance, equivalent consolidation and correct-but-uncommitted work.
All these documentation variants deliberately retain the same runtime behavior. Runtime success cannot decide their differing semantic outcomes.
The complete committed variant has sparse accounting and succeeds functionally; the correct-uncommitted variant fails only committed completeness. Runtime mutations separately exercise rollback, removed tests, loss of early stopping and changing the independent helper.

The active agent or human reads the resulting documents together, compares their meaning with the settled behavior and preservation requirements, and records evidence-backed criterion judgments. The constructed variants clarify valid alternatives and common mistakes; they are not a separate evaluator qualification gate. If retained evidence cannot settle a criterion, record insufficient evidence and its reason. Local construction does not establish independent evaluator accuracy; no provider call is made by qualification.

From the repository root, run the subject checks, controller tests and local reconstruction:

```sh
python3 -B -m unittest discover -s skill-studies/sweeping-stale-references/cases/semantic-delivery/fixture/tests
python3 -B -m unittest discover -s skill-studies/sweeping-stale-references/cases/semantic-delivery -p 'test_*.py'
python3 -B skill-studies/sweeping-stale-references/cases/semantic-delivery/qualify_case.py
```

Reconstruction rejects optimized Python, which would disable its qualification assertions, and clears inherited Git overrides before operating on scratch repositories. It writes its report to a new temporary directory and prints the path; it never replaces frozen case records or invokes a provider.
The manifest identifies preserved input bytes and controller artifacts. Existing original/control settings are Sol-low, workspace-write; they are prepared configurations, not approved commands to run models.
Retained preparation/qualification records describe their recorded input versions; the current manifest owns collection identities. Layout migration preserves subject inputs, expected facts, checkers and policy bytes.

## Criteria

### F1: Complete, useful documentation

Basis: Owner-clarified changed-behavior outcome, applied to the [task](task.md).
Coverage: [Protocol obligations](../../protocol.md#behavioral-contract-and-consumers) O1, O2.
Dimension: functional
Applies to: `original`, `control`
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
Applies to: `original`, `control`
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
Applies to: `original`, `control`
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
Applies to: `original`
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
Applies to: `original`
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
Applies to: `original`
Judgment unit: Semantic reference blocks specified by expected.json accounting_scope.
Required evidence: Commit body, trace and final documents reconciled to required block IDs, locations, outcomes, grouping and counts.
Met: The account accurately explains updates/preservation for required blocks using References swept: and useful locations, same-path/outcome grouping and counts.
Not met: The account omits required entries/header/detail or gives incorrect outcomes, locations, grouping or counts.
Insufficient evidence: Missing retained commit/trace evidence prevents judging the account; an inspectable absent account is a defect.
Alternatives: Concise accurate grouping and relocated content mapped by meaning; independent helper triage is optional. Deduplicate repeated searches and exclude already-current facts, task/skill text and incidental numbers as expected.json directs.
Consequence: Report a non-blocking procedural defect or insufficient evidence; neither changes the functional outcome or justifies a repeat execution by itself.
Overlap: Account defects cannot offset or create F1–F3 failures; shared triage causes may also affect P1.

## Limits

A small synthetic project cannot establish broad repository discovery, reserved transfer, population reliability or completeness of the full SSR catalog.
Functional ties and procedural differences are reportable; no control failure or discovery advantage is required.
Collection scope and authorization belong to the [protocol](../../protocol.md#execution-scope-and-authorization).
