# Adversarial Review Schema 0.2 Catalog Migration Implementation Plan

> **For agentic workers:** Use `superpowers:executing-plans` to implement this
> plan and `superpowers:verification-before-completion` before completion claims.

**Goal:** Package all fifteen active `adversarial-review` scenarios for the
schema `"0.2"` runner, prove that every package loads and prepares, and retain
one completed representative smoke result.

**Architecture:** Each canonical scenario becomes one self-contained package.
Current repository skills remain live fixture sources; canonical scenario files
and the selected Superpowers 6.2.0 dependencies are stored inside the packages.
`AR-01` is the sole representative smoke because it supplies the catalog's
complete nine-skill composition and a project fixture. The migration evaluates
only runner mechanics, never response quality.

**Tech Stack:** Markdown, RFC 8259 JSON, Python 3.11+, pytest, `uv`, and
`skilltest` schema `"0.2"`.

**Spec:** [schema `"0.2"` catalog migration design](specs/2026-08-29-catalog-migration-design.md),
[scenario porting roadmap](2026-08-24-scenario-porting-roadmap.md), and
[scenario migration index](../skill-validation/scenarios/README.md).

## Scope and constraints

- Implement on branch `feature/adversarial-review-schema-02` in worktree
  `.worktrees/adversarial-review-schema-02/`, starting from clean `main` that
  contains this plan.
- Use canonical source commit
  `13599fb7d3127334b0d07bfe468767e586ec5f9c` for scenario scope, prompts,
  rubrics, scenario-owned files, and meaning.
- Package exactly `AR-01` through `AR-08`, `AR-10`, and `AR-12` through
  `AR-17` at
  `skill-validation/scenarios/adversarial-review/<lowercase-id>/`.
  `AR-09` is retired and `AR-11` is exploratory; package neither.
- Give each `test.json` exactly the schema `"0.2"` keys `schema_version`, `id`,
  `prompt`, `fixtures`, and `execution`, with lowercase ID,
  `"prompt":"prompt.md"`, and execution
  `{"provider":"codex","model":"gpt-5.6-sol","effort":"high"}`.
- Use current repository `SKILL.md` files directly for live skill inputs. Do not
  copy or hash-pin them.
- Store only the canonical scenario-owned files and pinned external dependencies
  listed below. Do not package validation manifests, historical controls,
  ablation patches, the retired checker, or the canonical candidate's renderer.
- Apply only the prompt substitutions listed below. Preserve all other prompt
  and rubric bytes, including the trailing LF.
- Keep every scenario response-only. Do not name `{{evidence_dir}}`, request
  file changes, inspect or score a response, apply a rubric, or validate output.
- Add only the catalog-local acceptance test named below. Do not change the
  runner, providers, schema, skills, dependencies, fixtures outside this
  catalog, shared helpers, or other catalogs.
- Run the focused catalog acceptance and the complete offline runner suite, then
  stop for explicit smoke approval. Do not invoke a provider before approval.
- The approved smoke is one `AR-01` attempt with no retry. A result other than
  runner status `COMPLETED` stops the migration for owner direction.

## Catalog definition

| ID | Purpose | Scenario context |
|---|---|---|
| `AR-01` | Exercise direct adversarial review, severity, output, and composition over a complete bundle. | Nine live skills plus ratio project |
| `AR-02` | Preserve P3-only handling and prevent a quoted verdict from replacing the final verdict. | Prompt-contained completed review |
| `AR-03` | Require complete caller enumeration, rationale verification, and blocking treatment of a nonlocal invariant. | Six-file normalization project |
| `AR-04` | Map the holistic baseline and additive specialized lenses by artifact kind. | Artifact matrix |
| `AR-05` | Apply broad durability and holistic review without requiring one predetermined valid defect selection. | Real EventLog project slice |
| `AR-06` | Reach beyond a patch to absent, malformed, and out-of-scale paths. | Import-boundary project and patch |
| `AR-07` | Treat producer ordering as an unresolved blocking invariant. | Derived review-series patch |
| `AR-08` | Synthesize an evidence-backed pattern across API, queue, and file findings. | Boundary-ingestion project |
| `AR-10` | Challenge and remove unsupported duplicate state. | Receipt proposal |
| `AR-12` | Reject activity or proxy success that does not measure the governing outcome. | Onboarding proposal |
| `AR-13` | Reject a generic shared cause for two independently caused findings. | Independent-provenance project |
| `AR-14` | Apply the skill-authoring lens while retaining the holistic baseline. | Flawed skill and authoring dependencies |
| `AR-15` | Avoid inventing a blocking defect or shared cause in a supported bounded proposal. | Six-file clean proposal |
| `AR-16` | Report unchecked encoding failure as caller-visible termination requiring a typed failure path. | Focused EventLog encoding fixture |
| `AR-17` | Reject interior empty records as replay corruption. | Focused EventLog replay fixture |

### Canonical prompts and rubrics

Canonical paths are
`skill-validation/fixtures/adversarial-review/{prompts,rubrics}/<id>.md` at the
source commit. Hashes cover complete bytes. Rubric hashes guide materialization
and review only; catalog acceptance does not inspect rubric contents.

| ID | Canonical prompt SHA-256 | Adapted prompt SHA-256 | Rubric SHA-256 |
|---|---|---|---|
| `AR-01` | `b900f8dcea4585af8641052e01b54dc34f1419430d1916c63525d64735ecc27d` | `a70567cd4c8196340d478d8738de3a244b28df00919cfb643053db4a9ac506f8` | `33c459e9042000e46c5f82488511d140b750ff53076d8ab11331cf24c91447ab` |
| `AR-02` | `471108bcba67e89a618f927a8fb2138624f0c1734ffef77db5792ab679c8d194` | `afe180c4bb8bc0635561fa799ef5ea66a6e807c2edcb19d8d20a5baecd9e7390` | `0f97269c27c2d801d14ed0687e73c9f519754d0a6404b388e3ef156f32e9ca09` |
| `AR-03` | `fa8499a73e1a3b58ad31c2b897bddd467b8ec29f894e1737e3f9424a5a0ad5c0` | `a32a3269f7e89640a65b041b3f9d1ec5907f7397b032593e9473e59e42518fc8` | `31b5fab1a4a9c34a8517c51ee58aa974b309a5cecad4780caab930e7c0cf4244` |
| `AR-04` | `09fd681eb02d4d158d80ad1ee0c4eeb636568ab87217be5977932e12d0af0a91` | `525112073efaf10c6af7f6eb9fedfe3ce0c6e5c56ba443c27c73244e3b13a016` | `3eb7b7a502cb47c88af3ecdd9741cc85ded600ba35d47646ea5460f0387210a2` |
| `AR-05` | `94158d5dc3d103db900b2b681cf7fb992e1cc82231e332de6da38d03af192e2d` | `0f62c02acd47bf781d762420897a9a6a14ab7a94026494dfbed71cce9de1be41` | `2dd2372981b9b88eff3567ce5e1c6b5b3b8c7999285400c79ab1711fe6bbfa94` |
| `AR-06` | `25d8a0ba5f7f752c50b018e93b3a2677df3588c7cc567b0d7d0c6a0bd2cec5bc` | `64297e2b5919d9026c259bbdde24e64e929a812e59db10d7bd5cede490afe01b` | `1fcc10f48c998b173626c37e61259ecf9bd41d2ea96b31c8b34086d14a94b924` |
| `AR-07` | `583d41453d2b6a2e52faaa779bf48de02ef3d236dca0b4899f02952bb6f686bd` | `7023f5a2cdb2aadc443477d2c934e8ef584cf1e3539b602db607465caad2833f` | `a9f2bb2083974a0e6e793e26e0a3ced34dd4f5260b6d1359bb5e33dbc418f003` |
| `AR-08` | `9e5287bf4e2d5b899d9a30c3783242a6e332374256690d78a3bc036e19dce153` | `f2b266a29190821363eb02a2535587498eea852a2cb9fa3173910bb5333be3aa` | `a974a1585bb968b072bd7d724828cd311c03f6b624a158cf70cd2972e3cb9502` |
| `AR-10` | `54d4cc9f5d8f62bb6486dd6266e0ef7fcf18d203ed2ae2b1752777bbf3378b41` | `bebc32961df677d4a15b45d5d87201e43b5ae60b4a16362495a9e5de3cff9baa` | `6c161f73eab08e12f5b05bed900eb8efa08647365b064ac93417ee1a33f1b314` |
| `AR-12` | `9957e3f09da7dfd5d807b85825645f3d6f593499809cc623737309c14a1a26b7` | `4f268b13214207496769286295cec06d7ab0925b72c9b52195b26d9c12bc2a6a` | `0b84e78ffb224c2cf3be29eb4bb0ec45cb6d02f16021ba392b93859c3a2c5f99` |
| `AR-13` | `f1fd096b8ecda0523739b5c28b2eb9b009f6fdbaa898453518288a70b0017c16` | `76e00b195de7e65f0a9039d7a8fbde578fea9e58ae28764fccbcfc2ffa2dcb38` | `0ea6ad7ec83921325946609145fe06ce733d6e7496bddcf13af3168082dbc1f2` |
| `AR-14` | `62955b478d83abfb1c46533ea3899d4ed51aab839697ae0043cbcb94ab738fca` | `02531c56c34ec74e7148730ab81388aba27cbc4d7a68d4a8577d8ac9c83c3539` | `3dd645611692344bd7f8a79e57b036a47eb4b658a69624ae413090bd3193827a` |
| `AR-15` | `e9aa0eb1d99925bc624cb2b0dcd9b1905557f5ff39279e76142b30c5ca07afc2` | `7864f44d15beef43df08bea1fab53586ea634a9c5eda2576c06453a539accc28` | `67ac9d18db0aab32349752b26e25c21e89a8c5e94f675366fefaef7a2c869cc8` |
| `AR-16` | `445d6e37b60af5e80c6b57df6f20dce92badafb1bc70cf93f326c8d3fcf901e4` | `1513a66015109f998e8ca2bd5c0f92aa1b09f9791ec9b40abd87b71dc18d9c17` | `53f9a6581424dbde7b29c0975adea621b71696707e22ce0d08c30bfb67128a23` |
| `AR-17` | `445d6e37b60af5e80c6b57df6f20dce92badafb1bc70cf93f326c8d3fcf901e4` | `1513a66015109f998e8ca2bd5c0f92aa1b09f9791ec9b40abd87b71dc18d9c17` | `2d059422fc110f99a4e1120c48a2286f44311e610787381d998ca0eeced84844` |

### Prompt adaptations

Start from each canonical prompt and make only these literal changes:

- `AR-01`: add ``under `{{fixture_dir}}/skills/` `` after “every supplied
  skill file”; replace `` `project/` `` with
  `` `{{fixture_dir}}/project/` ``.
- `AR-02`, `AR-03`, `AR-05` through `AR-08`, `AR-10`, `AR-12`, and `AR-15`
  through `AR-17`: add ``under `{{fixture_dir}}/skills/` `` after “base
  code-review skills”.
- Wherever present in those prompts, replace the complete backticked paths
  `` `project/` ``, `` `subject/` ``, `` `context/head-change.patch` ``, and
  `` `subject/review-series.patch` `` with the same paths rooted at
  `{{fixture_dir}}`.
- `AR-04`: change its read sentence to
  ``Read the supplied `adversarial-review` skill under `{{fixture_dir}}/skills/`
  as binding guidance, then inspect `{{fixture_dir}}/context/artifacts.md`.``
- `AR-06`: append ``under `{{fixture_dir}}/project/` `` to “the supplied
  project plan and relevant project files”.
- `AR-08`: replace `` `plan.md` `` with
  `` `{{fixture_dir}}/project/plan.md` ``.
- `AR-13`: replace `` `skills/` `` with
  `` `{{fixture_dir}}/skills/` ``.
- `AR-14`: add ``under `{{fixture_dir}}/skills/` `` after “base code-review
  skills”; replace `` `project/SKILL.md` `` with
  `` `{{fixture_dir}}/project/SKILL.md` ``.

These are path and read-environment adaptations only. They add no task,
behavior, output, or evaluation requirement.

### Live skill mappings

Every package declares the live source
`../../../../skills/adversarial-review/SKILL.md` at target
`skills/adversarial-review/SKILL.md`.

`AR-01` additionally declares these current repository skills at matching
`skills/<id>/SKILL.md` targets:

- `adversarial-review-loop`
- `concise-writing`
- `disciplined-development`
- `disciplined-research`
- `dispatching-development-subagents`
- `lean-plan-writing`
- `sweeping-stale-references`
- `writing-explicit-rationale`

### Pinned Superpowers dependencies

Read these bytes from tag `v6.2.0` in
`/Users/simon/.codex/plugins/cache/claude-plugins-official/superpowers/6.3.0`.
Store a separate copy beneath each applicable package's `fixture/` directory and
declare the path after `fixture/` as its provider target. Do not introduce shared
dependency storage.

Every package receives:

| Path beneath `fixture/` and provider target | SHA-256 |
|---|---|
| `skills/superpowers/requesting-code-review/SKILL.md` | `d71cc01ba56d2325cf8af5f7c11837819b63ecd57de0bfdb812f7f3ff7751df8` |
| `skills/superpowers/requesting-code-review/code-reviewer.md` | `b2f2ec7596925fe52dac158fdfbca19b3a7d779d619c481e6706a6c0001662d3` |

`AR-14` additionally receives:

| Path beneath `fixture/` and provider target | SHA-256 |
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

### Scenario-owned files

Except for the two exceptions noted below, copy each listed canonical source
file from
`skill-validation/fixtures/adversarial-review/<id>/<bundle-path>` at the source
commit to `fixture/<bundle-path>` and declare `<bundle-path>` as the provider
target.

| ID | Bundle path | SHA-256 |
|---|---|---|
| `AR-01` | `project/CLAUDE.md` | `7f9a434946a09909b3d837588e5dd3f49593dc151959796132487735954f9993` |
| `AR-01` | `project/plans/ratio.md` | `b42252947352d99ecc3994cf157d91746bc6c13e1dfa530d5bfe3b3750dd6424` |
| `AR-01` | `project/src/ratio.py` | `2ab9e87f7325f2203a79bdcc5f5d698607c52566e601b3a3db7556287c656ad3` |
| `AR-03` | `project/benchmarks/sort.json` | `2a3c39905224a730da2182fa14aad68215caf7a536e251f818f751d4c2e4f2ae` |
| `AR-03` | `project/plans/normalize.md` | `963cae0e7dbd0d03ad3dc944d53d79bf5166a029e2ee08ccc8b3e0c7c007ecd1` |
| `AR-03` | `project/src/bulk.py` | `1640200ee740a66856d513fc3534ab6b62301f0838a0ebc438499620db2bbab0` |
| `AR-03` | `project/src/normalize.py` | `947c4926116f228a4843a7aa213cf46c86c03553315f55735b43b5085998223d` |
| `AR-03` | `project/src/retry.py` | `424d10fc3e9c4ef274312c2bffe331f60b53ad1d6ed5d873a0d13fb07aa9ff7f` |
| `AR-03` | `project/src/validate.py` | `020d6e30bd07ed9d44fe122dc0772cdf7080434947be2cc2dc21a878e5dbbbb0` |
| `AR-06` | `context/head-change.patch` | `ba2d42b8dd3c3b1b04a1a81f217f4a215aeae5b68d89ae80f05a3e7c1d21a8df` |
| `AR-06` | `project/plans/import-endpoint.md` | `2c38ef43ecfa7d63efcfdf079a4a81a14503e1002d27ac3f1bac95a255308c2f` |
| `AR-06` | `project/src/api.py` | `43246548de85a93a0c973d9893a3d23d4493e134250d04f5a0574e7a70bfb152` |
| `AR-06` | `project/src/importer.py` | `6657310fb0eb39c2cf2927be270d6c9204ff62b7743f7e39180e6356e28e1b8e` |
| `AR-08` | `project/plan.md` | `26c7a41a11268983452b04b43120ca7c4fd43789b2a1a5be3bbedeb247e346de` |
| `AR-08` | `project/src/api.py` | `9a55bc5e939aa4b08c159afbd42222c3da4a35ae00a9fe99869dd57738da5a36` |
| `AR-08` | `project/src/errors.py` | `718d317ee842c189fe538e5b86dae070f7602c1edfc62a00474854ca64344237` |
| `AR-08` | `project/src/file.py` | `b7fa1e6b2ef16a1a53079cf7e4a6431ddd958721182225f6387696d46263e9d0` |
| `AR-08` | `project/src/queue.py` | `36fffd19621f2bcdc471ea17fba458d88de8755e017921d4bf58f49c6df9256c` |
| `AR-08` | `project/test_happy_path.py` | `c62e8137b9f5cba55feebcb22d73248c037558d5a0e971dca597bc229dcd337a` |
| `AR-10` | `project/brief.md` | `784fef67760ffc9bca3245bffed2665f751ebeba71fa604297acebe112412c54` |
| `AR-10` | `project/proposal.md` | `df3d4a609e7d879b1b0b083eb246e060b9ad4dd00d76fb3b7646885ba47dc943` |
| `AR-12` | `project/brief.md` | `0ee6c05cbe47371847150bd6c497e52c45eddee35602d1f6ef5321a085ed4db7` |
| `AR-12` | `project/proposal.md` | `2981b6228802eaa93ee1bf2f78373e2634ab8eb4a2cf07997c119bbaea5f5146` |
| `AR-13` | `project/incidents.md` | `5a9a9d85342ba751c28f63e297c66931c84065f080053d67699d90fbea0855a6` |
| `AR-13` | `project/plan.md` | `3a500c601edc5c76c0658b89f4b36d632a416226a12e0a9c5f200dc691f5dd8c` |
| `AR-13` | `project/src/audit.py` | `9188c4991ce34c96388ada0eec7a57ba966309435167ee1571819158a5c446e6` |
| `AR-13` | `project/src/ratio.py` | `2ab9e87f7325f2203a79bdcc5f5d698607c52566e601b3a3db7556287c656ad3` |
| `AR-14` | `project/SKILL.md` | `2a51181ec6e1f7f990bcd04e78f2459a88922ceaa121446c1e1b9696966c061b` |
| `AR-15` | `project/approval-evidence.md` | `4e0b97116bb4dcd2e0f406e8bd43da561b267de29ebfe5adb5d252fd42c540b2` |
| `AR-15` | `project/change-request.md` | `40ec5077bd654fdae4d82fe5321ce157d23da86228f2eb186d813fd8a83266e4` |
| `AR-15` | `project/decision-record.md` | `b26aef2a0076d52c7578ae442a0afa5d863b20ffae5371fa7d87f6c487e630d6` |
| `AR-15` | `project/interface-contract.md` | `9996f1267cd295f7331866bfb03461bbe8a73b35b13405476154f9410e5857f1` |
| `AR-15` | `project/proposal.md` | `bf8b784fdf97b333d976872b134f3881b527f706b4efc7f75f66742538ea9698` |
| `AR-15` | `project/support-evidence.md` | `504c72f8798cf1957fe98e442aa197599ca46f9702f44f2fd04c82d1faedf626` |
| `AR-16` | `project/EventLog.swift` | `025c48a43595883ae06929affaccddd57f9df2b45f5fa56e409ac61c99cd9e09` |
| `AR-16` | `project/contract.md` | `c5d2479b1b24c120da384a16afb12d8628fd8fec93c9c626f91fc24049949202` |
| `AR-17` | `project/EventLog.swift` | `f1eda7207c1241654507072d3906db8a03947ecd65e155b4ad7591968638d41a` |
| `AR-17` | `project/contract.md` | `2557208d3e59c3d25e8dc914911fb73ce3b5beb7d55d43879fcc7e4ad0270a0f` |

Exceptions:

- `AR-04`: source
  `skill-validation/fixtures/adversarial-review/ar-04/artifacts.md`, package
  source `fixture/context/artifacts.md`, provider target
  `context/artifacts.md`, SHA-256
  `8b924afe56754ad28ae0fc04e265d8823d73826bea1732514f41e321b5402e1b`.
- `AR-07`: source
  `skill-validation/fixtures/adversarial-review/ar-07/review-series.patch`,
  package source `fixture/subject/review-series.patch`, provider target
  `subject/review-series.patch`, SHA-256
  `948088882749126f0e351155b6cdf505b530250b88504c0bb4421dcaf21dcdcf`.

`AR-05` comes from
`/Users/simon/work/coronis/code/meeting-pipeline` at commit
`b0f4511b2d43a566acdcbc5f0d61db6342a4c882`. Copy each source to
`fixture/subject/<source-path>` and declare `subject/<source-path>` as its
provider target:

| Source path | SHA-256 |
|---|---|
| `plans/2026-06-18-recording-slice.md` | `1d10c2845101df73f4418c7a4db147a79d53335a6f08f5bec822073e2e180c40` |
| `swift/Steno/Sources/Steno/Events/EventEnvelope.swift` | `42cd5c2df5a1dadb34df0e15cafa6e36f76588661e1cb99f93f83e158488800b` |
| `swift/Steno/Sources/Steno/Events/EventLog.swift` | `26b7accda8f8115ef23249243512384413fb198ab702961f65a3103f0f090aa0` |
| `swift/Steno/Tests/StenoTests/EventLogTests.swift` | `65134b891cd8ee803c1367518ea7c3b832fca4a862fa411ed848146d656a4b52` |

`AR-02` has no scenario-owned file. Do not package the source manifest,
`AR-09`, exploratory `AR-11`, `AR-14`'s historical
`holistic-ablation.patch`, any validation output, or any other file.

### Package records

Each package contains `README.md`, `prompt.md`, `rubric.md`, `test.json`, and
only its declared `fixture/` files. Before the smoke, no package contains a
result. Each README has only the required Purpose, Inputs, and Smoke sections.
After a completed smoke, only `AR-01` gains `smoke-result.json` and a result
link; no README makes a behavioral claim.

## Catalog acceptance

Create
`skill-validation/runner/acceptance/test_adversarial_review_catalog.py`. Keep
its data and any small helper local to that file. It verifies only:

- exactly the fifteen package directories and their planned package files;
- successful `load_config`, run creation, and workspace preparation for every
  `test.json`;
- prompt bytes against the adapted hashes above;
- the planned live-skill, pinned-dependency, and scenario-file source/target
  mappings;
- copied canonical and pinned file bytes against the hashes above;
- resolved prompt tokens and no stale `supplied-skills/` path;
- absence of rubric bytes from declared and prepared provider inputs; and
- an empty initial evidence directory.

Permit only `AR-01` to add optional `smoke-result.json`. Direct the runner's
temporary root to pytest's `tmp_path`.

Acceptance does not invoke a provider or validate rubric contents, README prose,
execution choices, result files, stdout, stderr, final responses, artifact
inventories, or behavioral outcomes. It does not reconstruct results, add
negative cases, or create shared machinery.

## Task 1: Package the catalog

**Files:** Create the fifteen packages under
`skill-validation/scenarios/adversarial-review/`.

- Materialize the exact prompts, rubrics, scenario-owned files, and external
  dependencies above.
- Apply only the listed prompt adaptations.
- Create the exact schema `"0.2"` configurations and minimal READMEs.
- Stop if a source or hash is unavailable, an additional adaptation is needed,
  or the runner cannot represent a package.

## Task 2: Prove provider-free preparation

**File:** Create
`skill-validation/runner/acceptance/test_adversarial_review_catalog.py`.

- Implement exactly the acceptance boundary above.
- From `skill-validation/runner`, run:

  ```bash
  uv run pytest -q acceptance/test_adversarial_review_catalog.py
  uv run pytest -q
  ```

- Commit the packages and acceptance test as
  `feat(validation): package adversarial review catalog`.
- Report both verification results and stop for explicit `AR-01` smoke
  approval. Do not invoke a provider at this gate.

## Task 3: Run and record the approved representative smoke

Proceed only after explicit owner approval.

- From `skill-validation/runner`, invoke exactly once:

  ```bash
  uv run skilltest run ../scenarios/adversarial-review/ar-01/test.json
  ```

- If the runner publishes `result.json`, copy its exact bytes to
  `skill-validation/scenarios/adversarial-review/ar-01/smoke-result.json`.
  If it publishes no result, retain no smoke result.
- Read only the runner-written status needed for disposition. Do not inspect or
  validate the response or any other result content.
- Record the mechanical outcome, including absence of a result if applicable,
  in the `AR-01` README and remove the temporary run directory. Retain no other
  run artifact.
- If status is not `COMPLETED`, do not update the migration index or retry;
  stop for owner direction.
- If status is `COMPLETED`, add the fifteen scenario links and `AR-01`
  representative line to `skill-validation/scenarios/README.md`, update totals
  to 15/15 for `adversarial-review` and 105/105 overall, and rerun only:

  ```bash
  uv run pytest -q acceptance/test_adversarial_review_catalog.py
  ```

- Commit the retained result, README, and index as
  `docs(validation): record adversarial review smoke`.

## Completion gate

Review the final diff against this plan and the migration design. Report the two
implementation commits, focused/full offline verification, smoke status, and
post-smoke focused verification. Obtain explicit approval before merging or
pushing implementation changes, archiving this plan, updating the roadmap, or
removing the branch/worktree.
