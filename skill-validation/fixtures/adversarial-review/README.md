# adversarial-review replay artifacts

These files contain the frozen evaluator definitions and synthetic fixtures plus the active Task 22 definitions for `adversarial-review`.
All files are UTF-8. Frozen SHA-256 values are recorded here and in [the validation record](../../adversarial-review.md), which owns activation and execution evidence.

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
| `AR-15` | Repository fixture at this commit | `skill-validation/fixtures/adversarial-review/ar-15/project/approval-evidence.md` | `project/approval-evidence.md` | `4e0b97116bb4dcd2e0f406e8bd43da561b267de29ebfe5adb5d252fd42c540b2` |
| `AR-15` | Repository fixture at this commit | `skill-validation/fixtures/adversarial-review/ar-15/project/change-request.md` | `project/change-request.md` | `40ec5077bd654fdae4d82fe5321ce157d23da86228f2eb186d813fd8a83266e4` |
| `AR-15` | Repository fixture at this commit | `skill-validation/fixtures/adversarial-review/ar-15/project/decision-record.md` | `project/decision-record.md` | `b26aef2a0076d52c7578ae442a0afa5d863b20ffae5371fa7d87f6c487e630d6` |
| `AR-15` | Repository fixture at this commit | `skill-validation/fixtures/adversarial-review/ar-15/project/interface-contract.md` | `project/interface-contract.md` | `9996f1267cd295f7331866bfb03461bbe8a73b35b13405476154f9410e5857f1` |
| `AR-15` | Repository fixture at this commit | `skill-validation/fixtures/adversarial-review/ar-15/project/proposal.md` | `project/proposal.md` | `bf8b784fdf97b333d976872b134f3881b527f706b4efc7f75f66742538ea9698` |
| `AR-15` | Repository fixture at this commit | `skill-validation/fixtures/adversarial-review/ar-15/project/support-evidence.md` | `project/support-evidence.md` | `504c72f8798cf1957fe98e442aa197599ca46f9702f44f2fd04c82d1faedf626` |
| `AR-16` | Focused contract at this commit | `skill-validation/fixtures/adversarial-review/ar-16/project/contract.md` | `project/contract.md` | `c5d2479b1b24c120da384a16afb12d8628fd8fec93c9c626f91fc24049949202` |
| `AR-16` | Real-source excerpt from `meeting-pipeline` at `b0f4511b2d43a566acdcbc5f0d61db6342a4c882` | `swift/Steno/Sources/Steno/Events/EventLog.swift` | `project/EventLog.swift` | `025c48a43595883ae06929affaccddd57f9df2b45f5fa56e409ac61c99cd9e09` |
| `AR-17` | Focused contract at this commit | `skill-validation/fixtures/adversarial-review/ar-17/project/contract.md` | `project/contract.md` | `2557208d3e59c3d25e8dc914911fb73ce3b5beb7d55d43879fcc7e4ad0270a0f` |
| `AR-17` | Real-source excerpt from `meeting-pipeline` at `b0f4511b2d43a566acdcbc5f0d61db6342a4c882` | `swift/Steno/Sources/Steno/Events/EventLog.swift` | `project/EventLog.swift` | `f1eda7207c1241654507072d3906db8a03947ecd65e155b4ad7591968638d41a` |

## Task 22 active definitions (2026-08-15–16)

The following hashes identify the changed/new definitions activated by the exact-hash Task 22 run; run evidence lives in the owning validation record and does not replace preserved historical hashes.

| Active source | SHA-256 |
|---|---|
| `prompts/ar-04.md` | `09fd681eb02d4d158d80ad1ee0c4eeb636568ab87217be5977932e12d0af0a91` |
| `rubrics/ar-04.md` | `3eb7b7a502cb47c88af3ecdd9741cc85ded600ba35d47646ea5460f0387210a2` |
| `rubrics/ar-05.md` | `2dd2372981b9b88eff3567ce5e1c6b5b3b8c7999285400c79ab1711fe6bbfa94` |
| `rubrics/ar-08.md` | `a974a1585bb968b072bd7d724828cd311c03f6b624a158cf70cd2972e3cb9502` |
| `rubrics/ar-13.md` | `0ea6ad7ec83921325946609145fe06ce733d6e7496bddcf13af3168082dbc1f2` |
| `rubrics/ar-14.md` | `3dd645611692344bd7f8a79e57b036a47eb4b658a69624ae413090bd3193827a` |
| `prompts/ar-15.md` | `e9aa0eb1d99925bc624cb2b0dcd9b1905557f5ff39279e76142b30c5ca07afc2` |
| `rubrics/ar-15.md` | `67ac9d18db0aab32349752b26e25c21e89a8c5e94f675366fefaef7a2c869cc8` |
| `prompts/ar-16.md` | `445d6e37b60af5e80c6b57df6f20dce92badafb1bc70cf93f326c8d3fcf901e4` |
| `rubrics/ar-16.md` | `53f9a6581424dbde7b29c0975adea621b71696707e22ce0d08c30bfb67128a23` |
| `prompts/ar-17.md` | `445d6e37b60af5e80c6b57df6f20dce92badafb1bc70cf93f326c8d3fcf901e4` |
| `rubrics/ar-17.md` | `2d059422fc110f99a4e1120c48a2286f44311e610787381d998ca0eeced84844` |
| `skill-validation/validate_adversarial_review_output.py` | `21ea8a09e64f20155a1d4222587d6a4a5f741f779a0a679049c9b6a9592fd340` |
| `skill-validation/tests/test_validate_adversarial_review_output.py` | `498bf6dc8ede36352585eac1d0e44ecbfa61991301fd80fc5bdd8abbcc6d8bfa` |
| `skills/adversarial-review/scripts/render_review.py` | `1469c4499fbc20960427bd1d99b7c9f0315afe5f6701672c31025c23c0fa31c2` |
| `skill-validation/tests/test_render_adversarial_review_output.py` | `b07818da119f7895795a2c859f5bf66fde53a4ad6ab1332eea8f7992fdb5e541` |

AR-15–AR-17 are preservation coverage, and AR-05 has a repaired behavior definition; their fresh five-Sol-high and five-Sol-low immediate controls and fresh five-Sol-high current evidence are recorded in the owning validation record.
For every protocol adjudication, run the checker against the exact same final-response bytes that semantic scoring consumed; do not reconstruct, normalize, or generate a second response.
For two-or-more-finding responses, pass `--expect-pattern none` or `--expect-pattern shared` from the orchestrator's semantic branch adjudication; the checker fails closed when that branch is omitted.

## Real-source fixtures

`AR-05` is materialized from `git@github.com:simon-idris_CORONIS/meeting-pipeline.git` at `b0f4511b2d43a566acdcbc5f0d61db6342a4c882`:

| Bundle path | SHA-256 |
|---|---|
| `subject/plans/2026-06-18-recording-slice.md` | `1d10c2845101df73f4418c7a4db147a79d53335a6f08f5bec822073e2e180c40` |
| `subject/swift/Steno/Sources/Steno/Events/EventEnvelope.swift` | `42cd5c2df5a1dadb34df0e15cafa6e36f76588661e1cb99f93f83e158488800b` |
| `subject/swift/Steno/Sources/Steno/Events/EventLog.swift` | `26b7accda8f8115ef23249243512384413fb198ab702961f65a3103f0f090aa0` |
| `subject/swift/Steno/Tests/StenoTests/EventLogTests.swift` | `65134b891cd8ee803c1367518ea7c3b832fca4a862fa411ed848146d656a4b52` |

`AR-16` and `AR-17` factor two protected `AR-05` seams into token-efficient atomic fixtures.
Their `EventLog.swift` files preserve selected source lines from the same `meeting-pipeline` revision: `AR-16` selects the generic class declaration, append signature/body, encoding rationale, and closing brace; `AR-17` selects the generic class declaration, replay method/comment/body, and closing brace.
Only unrelated class members and method context are omitted; the selected source lines are byte-for-byte unchanged.
Their focused contracts make the required caller-visible behavior explicit without supplying the evaluator-withheld rubric.

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

## Pre-Task22 historical complete-bundle dependency manifest

This table records the pre-Task22 `AR-01` original/current arms only: the nine project skills from cleanup control commit `4296647f0dff48a9e77b979ef07e813bf1f66db2` plus Superpowers 6.2.0's base-review files.
Its historical current arm changed only `skills/adversarial-review/SKILL.md` from `9004ff153d5dc3a3690254667c4f666151dcabff7ef6f705cc751134be56499c` to `b266f35b751a23967d99030678ffe893d72137bf1ffbc7c433db811ed1bbf085`.

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

### Active Task 22 complete bundle

Task 22's active `AR-01` bundle is distinct from the historical manifest above.
The final model run used renderer SHA-256 `4692300de4622bbb05aca0b87a8e8ba4547ce95e67e46227e27601299ee8a110` and context-manifest SHA-256 `15c3d0f6ff76c9a97265516ad9826216b6d5a51e27291f1f6155d5549c2775d2` under the Task 22 runner's path-component ordering.
Cold-review hardening changed only invalid-input handling and executable mode, leaving valid rendering unchanged.
The active post-hardening bundle replaces only that path with renderer SHA-256 `1469c4499fbc20960427bd1d99b7c9f0315afe5f6701672c31025c23c0fa31c2` and has runner context-manifest SHA-256 `199ddc60a4046fce1bf1d92da813580364c384fc912f4f902f6aee081adc0969`.
Under the shell bundle-digest algorithm documented above, the same pre-hardening and post-hardening trees are `2bfb90939ed3f8556d35e2561dbf5688989dfdcb803aa10a3ce1b6d0108df94c` and `763a29a11a6b1601be5482cf4bd2ed2e58ee29cbd1b6109137e060f74bded79a` respectively; the values differ because that algorithm sorts full path strings rather than path components.
The exact-hash execution and activation evidence are owned by [the validation record](../../adversarial-review.md#approved-task-22-validation-method-2026-08-15-activated-2026-08-16).

| Bundle path | SHA-256 |
|---|---|
| `project/CLAUDE.md` | `7f9a434946a09909b3d837588e5dd3f49593dc151959796132487735954f9993` |
| `project/plans/ratio.md` | `b42252947352d99ecc3994cf157d91746bc6c13e1dfa530d5bfe3b3750dd6424` |
| `project/src/ratio.py` | `2ab9e87f7325f2203a79bdcc5f5d698607c52566e601b3a3db7556287c656ad3` |
| `skills/adversarial-review-loop/SKILL.md` | `56e08642a8005ac526898ed7b9cd178bcfd08a655464f2249b9ccae22aeb5387` |
| `skills/adversarial-review/SKILL.md` | `309bd02c8bc6c06bb09d166c29a06152183bb4d4197755a35653e01131c703c6` |
| `skills/adversarial-review/scripts/render_review.py` | `1469c4499fbc20960427bd1d99b7c9f0315afe5f6701672c31025c23c0fa31c2` |
| `skills/concise-writing/SKILL.md` | `f763b43e88c56d6fdc2a96457bc2415cba60b75a1e7cb59cd1b0ebaa3fb199ba` |
| `skills/disciplined-development/SKILL.md` | `872529574af4f4fabcd58ff3721ce6c241af99936c19403b40abca7e9c252e8b` |
| `skills/disciplined-research/SKILL.md` | `6fa7d81c67c3075429c1fd9f54d37d494d0e24f877de976a6c0da71da8a61984` |
| `skills/dispatching-development-subagents/SKILL.md` | `bf616daa594a90282ccfa22af210214b30393158838b5feb9220859268f9fe54` |
| `skills/lean-plan-writing/SKILL.md` | `db1ade9e0ba7395bf662d041c866ce80965f729725d3829983adcdfd21946129` |
| `skills/superpowers/requesting-code-review/SKILL.md` | `d71cc01ba56d2325cf8af5f7c11837819b63ecd57de0bfdb812f7f3ff7751df8` |
| `skills/superpowers/requesting-code-review/code-reviewer.md` | `b2f2ec7596925fe52dac158fdfbca19b3a7d779d619c481e6706a6c0001662d3` |
| `skills/sweeping-stale-references/SKILL.md` | `15992341f7ab2fb1e4d8a775092199d7d4e6a9de1167895dbe5a805aeafbd38c` |
| `skills/writing-explicit-rationale/SKILL.md` | `568b2a61bef3f7694014fb89228f933261837acd4f2b5978b2b8ef55aa108c9f` |

## Exploratory AR-11

The `exploratory-ar-11` files preserve a retired two-turn scope-guard probe.
It is not an active regression scenario because the global mandatory brainstorming skill confounded its no-tool criterion, one original-control repetition asked a reasonable clarifying question, and deleting the entire scope-guard section still passed 5/5.
