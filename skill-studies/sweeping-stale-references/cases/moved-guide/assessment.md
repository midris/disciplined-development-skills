# Moved service guide

## Identity and purpose

Format version: `1`
Study ID: `sweeping-stale-references`
Case ID: `moved-guide`
Definition version: `2`
Status: prepared; collection scope and authorization belong to the protocol.
Purpose: reconcile references to one moved guide across different relative-path contexts and an executable consumer, while preserving history and an independent same-name guide.
Coverage/exposure: [protocol suite](../../protocol.md#proposed-baseline-case-selection), O1–O4; an exposed development case, with no held-out or O5 claim.
This is the same subject scenario as historical [pilot-02](../pilot-02/assessment.md), using its subject/configuration/checker bytes by reference. This controller definition adopts the accepted layout and current policy 3 without changing criterion meanings or relabelling pilot observations.

## Inputs and setup

Comparison applicability (version 2): `candidate` receives the exact [comprehensive snapshot](../skill-candidate-comprehensive/SKILL.md) through [its configuration](candidate-comprehensive.json), with the same task, prompt and setup as `original`, including full skill-read evidence. Apply every original criterion and its existing boundaries to candidate. Original/control descriptions below continue to describe that earlier pair; candidate has guidance as original does. This adds a condition without changing judgment units, thresholds or outcomes in historical records.

Task: [pilot-02/task.md](../pilot-02/task.md); configs: [original](../pilot-02/original.json), [control](../pilot-02/control.json); current controller identities: [manifest](manifest.json).
The guide already moved from docs/setup.md to docs/reference/setup.md. The task flags one README link, permits project edits and requires a commit; other consumers remain discoverable through ordinary project files.
Both conditions receive identical project/task/setup bytes. Original alone adds the frozen SSR snapshot and read instruction. DD, sibling skills, criteria, expected facts and checkers are excluded.
The neutral baseline captures the settled move; TASK.md and guidance are excluded from project commits. Config test IDs retain ssr-pilot-02-original/control; they do not rename this case or make later executions historical pilots.
Setup: verify supplied hashes/settings, identical initial trees, full original-skill read, control guidance integrity and usable traces. Missing-guidance probes alone are not contamination; setup faults limit attribution rather than establish skill failures.

## Rules and evidence

Apply [policy 3](assessment-policy.txt), pinned by the manifest, and the unchanged [expected facts](../pilot-02/expected.json). The historical pilot retains its own policy-2 input identity.
Correct relative-path handling is an owner-clarified functional outcome, not an explicit technique in the skill. A miss fails that outcome without proving disobedience to an explicit relative-path instruction.
Git proves committed state; ordered tool events support search claims; inspect whole artifacts and semantic preservation directly. Missing evidence leaves the affected criterion uncertain. Control procedure is descriptive, without undisclosed target obligations.
The existing [check_paths.py](../pilot-02/check_paths.py) emits path/content facts for ordinary inline Markdown links; unsupported forms require manual inspection. It cannot establish semantic preservation, search procedure or Git completeness by itself.
After inspecting changes, use a disposable copy: run `python3 -B ../pilot-02/check_paths.py FIXTURE` from this definition's directory and execute `sh scripts/export-guide.sh` from the replay project root and by absolute script path from another directory. Compare output to the service guide; never replay against retained raw evidence.
The retained [qualification](../pilot-02/qualification.json) covers complete, README-only, wrong-but-existing, destructive and rollback variants plus equivalent path spelling. Reuse those observations and checks; no new qualification model call is needed.

## Criteria

### F1: Current consumers

Basis: Owner-clarified functional relative-path outcome applied to the settled moved-guide task; SSR broad reconciliation purpose.
Coverage: [Protocol obligations](../../protocol.md#behavioral-contract-and-consumers) O1, O2.
Dimension: functional
Applies to: `original`, `control`, `candidate`
Judgment unit: Three Markdown consumers and the export script, each reaching the intended moved service guide.
Required evidence: Inspect README, docs/index.md and docs/tutorials/quickstart.md; resolve links relative to their containing file. Run check_paths.py and the inspected export script on a disposable copy from the project root and another directory; compare exported content to the service guide.
Met: All three current links resolve to docs/reference/setup.md and exporting the guide emits its intended content from both working directories.
Not met: A required consumer is missing/deleted, resolves to a wrong existing destination, fails or emits wrong content.
Insufficient evidence: Unsupported link forms or incomplete/missing runtime observations prevent deciding a consumer after inspection.
Alternatives: Equivalent normalized relative paths, labels and document structures that preserve the consumer roles; checker parser limits do not invalidate a valid alternative.
Consequence: A violation is a hard functional failure; an unresolved evidence gap remains insufficient evidence.
Overlap: Incomplete repair may also fail F3; count the shared cause once at execution level.

### F2: Preservation

Basis: Settled task move and SSR Procedure 2 triage under the owner-clarified whole-artifact policy.
Coverage: [Protocol obligations](../../protocol.md#behavioral-contract-and-consumers) O2.
Dimension: functional
Applies to: `original`, `control`, `candidate`
Judgment unit: Service guide content, historical location record and independent vendor guide/link, with the settled move intact.
Required evidence: Inspect all final files/diffs and expected.json protected paths; verify the vendor link still reaches its own guide and the old path was not restored or duplicated to hide breakage.
Met: Service instructions and historical meaning remain useful, the independent vendor guide/link works, and the settled move remains intact.
Not met: Protected meaning/function is damaged or the old path is restored/duplicated to conceal broken consumers.
Insufficient evidence: Missing or conflicting files/runtime evidence prevents establishing preservation.
Alternatives: Effective semantic equivalents; changed bytes initiate inspection, not automatic failure.
Consequence: A violation is a hard functional failure; an unresolved evidence gap remains insufficient evidence.
Overlap: A wrong consumer destination can also fail F1; record shared causes.

### F3: Committed repair

Basis: Explicit task commit request and SSR Procedure 3; owner priority on complete committed outcome.
Coverage: [Protocol obligations](../../protocol.md#behavioral-contract-and-consumers) O3.
Dimension: functional
Applies to: `original`, `control`, `candidate`
Judgment unit: All required consumer repairs committed after the neutral fixture baseline.
Required evidence: Inspect retained Git history, committed tree and final working diff against F1.
Met: All required edits appear in committed history.
Not met: A required repair is missing/incorrect or left only in the working tree.
Insufficient evidence: Missing Git history/final state prevents establishing committed completeness.
Alternatives: Any effective repair under F1; complete repairs split across commits affect P2 separately.
Consequence: A violation is a hard functional failure; an unresolved evidence gap remains insufficient evidence.
Overlap: Incomplete repair may also fail F1; commit grouping alone belongs to P2.

### P1: Search and triage

Basis: SSR Procedures 1 and 2.
Coverage: [Protocol obligations](../../protocol.md#behavioral-contract-and-consumers) O1, O2.
Dimension: procedural
Applies to: `original`, `candidate`
Judgment unit: Observable repository search, search/edit order and reasons for repair/preservation.
Required evidence: Retained ordered tool events, content exposure and explicit triage; final correctness alone does not establish the procedure.
Met: Search precedes reconciliation and current, historical and independent references receive appropriate triage.
Not met: Usable events show reconciliation before search or incorrect/omitted required triage.
Insufficient evidence: Missing/truncated traces prevent establishing breadth, sequence or triage.
Alternatives: Any effective search tool/order consistent with search-before-repair.
Consequence: Report a non-blocking procedural defect or insufficient evidence; neither changes the functional outcome or justifies a repeat execution by itself.
Overlap: A triage defect may also cause F1/F2 failures; assess that outcome separately.

### P2: Commit grouping

Basis: SSR Procedure 3 one-commit requirement.
Coverage: [Protocol obligations](../../protocol.md#behavioral-contract-and-consumers) O3.
Dimension: procedural
Applies to: `original`, `candidate`
Judgment unit: Grouping of the complete repair after the separate setup commit.
Required evidence: Retained commit history and diffs.
Met: One repair commit contains all required changes.
Not met: The repair is split across commits or no complete repair commit exists.
Insufficient evidence: Missing Git evidence prevents deciding grouping.
Alternatives: Equivalent complete repairs; multiple complete commits are a non-blocking procedural defect.
Consequence: Report a non-blocking procedural defect or insufficient evidence; neither changes the functional outcome or justifies a repeat execution by itself.
Overlap: F3 owns committed completeness, separately from grouping.

### P3: Audit usefulness

Basis: SSR Output artifact and the fixed moved-document accounting scope, with owner-set non-blocking severity.
Coverage: [Protocol obligations](../../protocol.md#behavioral-contract-and-consumers) O4.
Dimension: procedural
Applies to: `original`, `candidate`
Judgment unit: Four current moved-guide references plus the historical reference in expected.json.
Required evidence: Commit body, searches and final changes reconciled to scoped references, reasons, locations, grouping and counts.
Met: References swept: usefully and accurately explains the repair and deliberate preservation for the five scoped references, with same-path/outcome grouping.
Not met: Required accounting is absent, inaccurate or incorrectly grouped/counted.
Insufficient evidence: Missing commit/trace evidence prevents judging the account; an inspectable absence is a defect.
Alternatives: Concise useful accounts; unrelated-match triage is descriptive and already-current or additional broad basename hits are not required entries.
Consequence: Report a non-blocking procedural defect or insufficient evidence; neither changes the functional outcome or justifies a repeat execution by itself.
Overlap: Account defects cannot create or offset functional failures; shared triage causes may also affect P1.

## Limits

The same-name vendor guide makes path existence insufficient; the intended destination matters. This compact known scenario does not establish broad repository discovery or population reliability.
Historical pilot evidence stays outside the new batch aggregates. The protocol owns ordering, repetitions, scope and authorization; no historical extra-development proposal applies.
