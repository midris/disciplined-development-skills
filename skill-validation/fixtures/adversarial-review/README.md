# adversarial-review replay artifacts

These files are the canonical evaluator prompts, evaluator-withheld rubrics, and synthetic fixtures for the active `adversarial-review` catalog.
All files are UTF-8 and their SHA-256 values are recorded in [the validation record](../../adversarial-review.md).

For each run, place the scenario fixture at its recorded relative path under an isolated root, materialize the recorded skill bundle, make the root read-only, and invoke a fresh `gpt-5.6-sol` evaluator at high reasoning effort with the prompt file's exact bytes.
Never supply the rubric to the evaluator.
The orchestrator scores the last-message bytes against the matching rubric.

## Bundle digest

Bundle digests in the validation record use this algorithm from the bundle root:

```bash
find . -type f -print0 \
  | LC_ALL=C sort -z \
  | xargs -0 shasum -a 256 \
  | LC_ALL=C sort -k2 \
  | shasum -a 256
```

The digest therefore commits to every relative path and byte in the isolated root.

## Canonical fixture mappings

`This commit` means the full repository commit containing this manifest and the named canonical source file.

| Scenario | Source kind and revision | Source path | Bundle path | SHA-256 |
|---|---|---|---|---|
| `AR-04` | Repository fixture at this commit | `skill-validation/fixtures/adversarial-review/ar-04/artifacts.md` | `context/artifacts.md` | `8b924afe56754ad28ae0fc04e265d8823d73826bea1732514f41e321b5402e1b` |
| `AR-06` | Repository fixture at this commit | `skill-validation/fixtures/adversarial-review/ar-06/context/head-change.patch` | `context/head-change.patch` | `ba2d42b8dd3c3b1b04a1a81f217f4a215aeae5b68d89ae80f05a3e7c1d21a8df` |
| `AR-06` | Repository fixture at this commit | `skill-validation/fixtures/adversarial-review/ar-06/project/plans/import-endpoint.md` | `project/plans/import-endpoint.md` | `2c38ef43ecfa7d63efcfdf079a4a81a14503e1002d27ac3f1bac95a255308c2f` |
| `AR-06` | Repository fixture at this commit | `skill-validation/fixtures/adversarial-review/ar-06/project/src/api.py` | `project/src/api.py` | `43246548de85a93a0c973d9893a3d23d4493e134250d04f5a0574e7a70bfb152` |
| `AR-06` | Repository fixture at this commit | `skill-validation/fixtures/adversarial-review/ar-06/project/src/importer.py` | `project/src/importer.py` | `6657310fb0eb39c2cf2927be270d6c9204ff62b7743f7e39180e6356e28e1b8e` |
| `AR-07` | Repository fixture at this commit | `skill-validation/fixtures/adversarial-review/ar-07/review-series.patch` | `subject/review-series.patch` | `948088882749126f0e351155b6cdf505b530250b88504c0bb4421dcaf21dcdcf` |

## Real-source fixtures

`AR-05` is materialized from `git@github.com:simon-idris_CORONIS/meeting-pipeline.git` at `b0f4511b2d43a566acdcbc5f0d61db6342a4c882`:

| Bundle path | SHA-256 |
|---|---|
| `subject/plans/2026-06-18-recording-slice.md` | `1d10c2845101df73f4418c7a4db147a79d53335a6f08f5bec822073e2e180c40` |
| `subject/swift/Steno/Sources/Steno/Events/EventEnvelope.swift` | `42cd5c2df5a1dadb34df0e15cafa6e36f76588661e1cb99f93f83e158488800b` |
| `subject/swift/Steno/Sources/Steno/Events/EventLog.swift` | `26b7accda8f8115ef23249243512384413fb198ab702961f65a3103f0f090aa0` |
| `subject/swift/Steno/Tests/StenoTests/EventLogTests.swift` | `65134b891cd8ee803c1367518ea7c3b832fca4a862fa411ed848146d656a4b52` |

`AR-06` is the compact synthetic import-boundary fixture in the canonical mapping table above. It keeps the whole-project, absent-resource, malformed-trust-boundary, and out-of-scale behaviors together because they arise from one shared import path.

`AR-07` uses the committed custom excerpt [review-series.patch](ar-07/review-series.patch), SHA-256 `948088882749126f0e351155b6cdf505b530250b88504c0bb4421dcaf21dcdcf`.
It was derived from `git@github-personal:midris/steno.git` range `0fae3e34d73505960313efa6ff7c6256c00f7029..59d08686570724d288c716a756984d364ef50e49`.

`AR-13` uses the committed four-file fixture under [ar-13](ar-13/).
Its provenance file establishes that the two planted defects have independent causes, so the scenario tests the multi-finding `NONE` branch rather than inviting a generic similarity.

`AR-14` uses [project/SKILL.md](ar-14/project/SKILL.md) and the complete original/current review arms.
Its holistic-only arm starts from control commit `4296647f0dff48a9e77b979ef07e813bf1f66db2` and applies [holistic-ablation.patch](ar-14/holistic-ablation.patch), producing skill SHA-256 `84f34c09dd1fd568b3cffc7da5ecb81955fcfbc0c25f3fa2d5f97ac709174896`.
The patch removes only the `skill-authoring` angle row and its application trigger.

All three `AR-14` arms materialize the same Superpowers 6.2.0 authoring dependencies at the listed bundle paths. The evaluator loads an optional dependency only when the binding review guidance directs it there:

| Bundle path | SHA-256 |
|---|---|
| `skills/superpowers/test-driven-development/SKILL.md` | `bf1b8216e523851a411e91d429a7c1c2a173e79d88957bc78e348218d50edd54` |
| `skills/superpowers/using-superpowers/references/codex-tools.md` | `d3f113a8ebbd748e8ba847b09b57b7685442775ca4ee194d693ce3663f8fac68` |
| `skills/superpowers/writing-skills/SKILL.md` | `d34db5c8aed6a4e0440132bd0613aace70a693ec7819d5637ad77481d8e10d1b` |
| `skills/superpowers/writing-skills/anthropic-best-practices.md` | `217629b356c09c9bd11017c9788e8fc654ca1b32c92d4a51cd490e16dd65e59a` |
| `skills/superpowers/writing-skills/examples/CLAUDE_MD_TESTING.md` | `0b379a3415e185d3c434b3ad283d8aa132f3022c2a4f210f168865b5986bcef0` |
| `skills/superpowers/writing-skills/graphviz-conventions.dot` | `e2890a593c91370e384b42f2f67b1a6232c9e69dddea7891a0c1c46d7b20b694` |
| `skills/superpowers/writing-skills/persuasion-principles.md` | `a51bc9bf75189ea73a27b3fb504a2fdfdb966fb1f7f1cdf03203230a216ccc03` |
| `skills/superpowers/writing-skills/render-graphs.js` | `ccda971a87bb185f8febf81c56b556a20d026fa980c17b35fa3e8824fbb37852` |
| `skills/superpowers/writing-skills/testing-skills-with-subagents.md` | `c711346852c911b24a84aa161e0cff06a4cd7f4e2fa9e9c0a266cead5afcbade` |

## Complete-bundle dependency manifest

`AR-01` uses the nine project skills from cleanup control commit `4296647f0dff48a9e77b979ef07e813bf1f66db2` plus Superpowers 6.2.0's base-review files.
The current arm changes only `skills/adversarial-review/SKILL.md` from `9004ff153d5dc3a3690254667c4f666151dcabff7ef6f705cc751134be56499c` to `b266f35b751a23967d99030678ffe893d72137bf1ffbc7c433db811ed1bbf085`.

| Bundle path | SHA-256 |
|---|---|
| `skills/adversarial-review-loop/SKILL.md` | `46b85eafc5db54cb521eed9c4a110e552c76d97cfae72e141f109c9dea10f0c6` |
| `skills/concise-writing/SKILL.md` | `4d12a2eb475c6b2ef57e2300c8c07af3f59c1e07b2b82695a3b7669eee1d6d72` |
| `skills/disciplined-development/SKILL.md` | `1151a7575a5b6f72e007229c97efdb7a829695d08e8f44450d0d71b232e75dec` |
| `skills/disciplined-research/SKILL.md` | `a5c4079e5aa21651ecd39b09e3fb2d9a58f4a1f3b99354b3b6927b2d44c6fb50` |
| `skills/dispatching-development-subagents/SKILL.md` | `b89b4db8af53bd136237cb2306f956c039757a0e321b1f704bd16d1a00580500` |
| `skills/lean-plan-writing/SKILL.md` | `6a3115a4d33ad2f99238f915a6a1b7869efd8c80a6cce422d3afae60c9857fac` |
| `skills/sweeping-stale-references/SKILL.md` | `d6812c33cae026807bbb3ebe851d93b60b513dd87ea5efd98aea28f5c02f9157` |
| `skills/writing-explicit-rationale/SKILL.md` | `97eb06c649c194e8819b4dff68b808eda4ec7c948a6ead518da247daf31d6cfe` |
| `skills/superpowers/requesting-code-review/SKILL.md` | `d71cc01ba56d2325cf8af5f7c11837819b63ecd57de0bfdb812f7f3ff7751df8` |
| `skills/superpowers/requesting-code-review/code-reviewer.md` | `b2f2ec7596925fe52dac158fdfbca19b3a7d779d619c481e6706a6c0001662d3` |

## Exploratory AR-11

The `exploratory-ar-11` files preserve a retired two-turn scope-guard probe.
It is not an active regression scenario because the global mandatory brainstorming skill confounded its no-tool criterion, one original-control repetition asked a reasonable clarifying question, and deleting the entire scope-guard section still passed 5/5.
