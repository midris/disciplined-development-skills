# SSR expansion: offline qualification

Status: offline preparation, not model observations or independent evaluation.
The active session constructed and inspected the cases and reference solutions under the original contract.

## Checks

Run from the repository root:

```sh
python3 -B -m unittest discover -s skill-studies/sweeping-stale-references -p test_expansion_fixtures.py
python3 -B -m unittest discover -s skill-studies/sweeping-stale-references/cases/initiating-change/fixture/tests
```

Seven controller tests and three supplied project tests pass.
The project tests were written before its source module and first failed because the module was absent; they passed after fixture implementation.
The controller suite exercises:

- The runnable initial service, including script invocation from outside its directory.
- A complete disposable reference rename with unchanged behavior, direct new-key invocation, preserved vendor/history bytes and a clean committed Git tree.
- A code-only rename that breaks the unchanged CLI consumer, demonstrating a useful incomplete-repair boundary.
- Fourteen declared reference occurrences or twelve unique matching lines across nine files; both units are acceptable when clear and internally consistent.
- A single local correction with valid supplied file links and preserved near-match material.
- The diagnostic's inclusive line ranges, 126 matches, ten paths and eleven path/outcome groups.
- Configured input existence, unique targets, absence of controller facts and original/control differences confined to guidance.

The tests qualify fixture mechanics, not the semantic scoring of arbitrary subject outputs.
Reference replacements are only one correct solution. The assessor must accept equivalent layouts/implementations and inspect the whole project and commit history.
The tests do not auto-grade prose, infer what a model read or prove absence of ambient guidance.

## Semantic boundaries inspected

| Constructed outcome | Intended interpretation |
|---|---|
| Correct initiating rename with all current consumers, causal explanation and preservation intact | Eligible for F1/F2; F3 requires the committed result |
| Runtime passes, but script or current documentation still uses the retired interface | F1 failure; tests alone are insufficient |
| Rename changes vendor settings or rewrites the historical event meaning | F2 failure |
| Complete correct task changes only in working tree | F3 failure |
| Correct local heading edit after scope inspection, with justified negative account | Functional success and procedure eligible |
| Correct local edit, missing negative account | Functional success; P3 defect |
| Broad replacement changes unrelated shipping or billing meaning | F2 failure |
| Accurate diagnostic entries with no redundant grand total | P3 can be met |
| Correct grand total conceals a missing or mixed-outcome group | P3 not met |
| Correct diagnostic inventory followed by a fabricated project-test claim | P3 not met |

These are worked boundaries, not scored executions; no subject was run or inferred to have failed.
All three manifests passed the existing working-manifest generator, including original/control parity checks for the executable cases. All five configurations were materialized with the actual runner workspace API; supplied bytes and rendered fixture paths matched. No provider was invoked.
The unchanged hook suite passed 263 tests with three existing environment skips; file-link checks and git diff --check passed.
Draft manifests intentionally have no frozen source revision; collection readiness and owner spending authority are still required before dispatch.

The version-2 reporting extension is offline-qualified separately: procedural-only results require not measured, mixed aggregates preserve separate counts, and excluded/missing attempts never inflate success.
The large-sweep diagnostic draft now selects that schema; the two executable cases retain version 1.
