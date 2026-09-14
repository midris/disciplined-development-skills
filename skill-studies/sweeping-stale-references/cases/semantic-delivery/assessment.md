# Semantic drift: notification delivery policy

Status: locally prepared and mechanically qualified; exact baseline collection configuration and dispatch remain pending.
This is a newly authored case. The six earlier SSR prompts do not supply its changed-behavior mechanism; see `preparation.json` for the inspected identities and reuse decision.

## Task and source facts

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

## Criteria

Apply the exact `SSR-assessment-3` copy identified in preparation/manifest records. Use met, not met or insufficient evidence per criterion, with no combined score.

| Criterion | Evidence and consequence |
|---|---|
| Setup | Verify input/settings identities, identical initial trees, full original read, control guidance integrity and usable traces. Record absent-guidance probes without treating them alone as contamination. Setup faults invalidate attribution, not skill behavior. |
| F1: Complete, useful documentation | Every current delivery description agrees with the settled behavior: at most four sends, up to three after an initial failure, exhaustion only after four failures, immediate stop on success. Judge the documents together. Contradictions, remaining obsolete claims or deleting useful explanations without an effective replacement fail. |
| F2: Preservation | Keep the worker's settled behavior, the independent helper's three-attempt limit, historical meaning and unrelated operational guidance. Verify code and runtime evidence. Byte differences initiate semantic review; they are not failures by themselves. |
| F3: Committed repair | Every required repair appears in retained Git history after the baseline, including a valid consolidated explanation and its references. Correct work left uncommitted fails. Inspect history and the final working diff; do not infer completeness from the message or changed-file count. |
| P1: Search and triage | Retained events show search before repair and the handling of relevant current/historical/independent meanings. Account for what the model actually read and decided; absent evidence means uncertainty. Purely procedural deviations are non-blocking. |
| P2: Commit grouping | One complete repair commit meets the grouping requirement. Complete repairs split across commits are non-blocking procedure deviations, distinct from F3. |
| P3: Useful account | Use the predeclared reference-block scope in expected.json. Assess accurate update/preservation explanations, locations, grouping and counts. Missing detail remains secondary and cannot turn functional success into failure or justify another run. |

An incomplete/incorrect repair can affect both F1 and F3; report the shared cause rather than count it as two independent failures.
Target-specific procedure applies to original; describe control behavior without imposing undisclosed format instructions.
Functional ties and procedural differences are both reportable; no control failure or discovery advantage is required.

Accept accurate prose, tables, reordered sections or consolidation with clear working cross-references that still serve each document's reader.
Do not require changing all three original files if a different complete solution satisfies the three document roles.
A reference answer is one valid repair, not the required wording.
Changing a number without understanding whether it counts attempts or retries is not sufficient; neither is passing the runtime checks while leaving prose stale.

## Runtime observations and semantic qualification

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

## Reproduction and limits

From the repository root, run the subject checks, controller tests and local reconstruction:

```sh
python3 -B -m unittest discover -s skill-studies/sweeping-stale-references/cases/semantic-delivery/fixture/tests
python3 -B -m unittest discover -s skill-studies/sweeping-stale-references/cases/semantic-delivery -p 'test_*.py'
python3 -B skill-studies/sweeping-stale-references/cases/semantic-delivery/qualify_case.py
```

Reconstruction rejects optimized Python, which would disable its qualification assertions, and clears inherited Git overrides before operating on scratch repositories. It writes its report to a new temporary directory and prints the path; it never replaces frozen case records or invokes a provider.
The manifest identifies preserved input bytes and controller artifacts. Existing original/control settings are Sol-low, workspace-write; they are prepared configurations, not approved commands to run models.
A small synthetic project cannot establish broad repository discovery, reserved transfer, population reliability or completeness of the full SSR catalog.
