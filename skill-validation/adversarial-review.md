# adversarial-review — validation

## Active catalog audit (2026-08-04)

The shared all-nine discovery suite remains owned by [skill-discovery.md](skill-discovery.md#active-catalog-definitions).
`DISC-01` protects routing into `adversarial-review`; this record owns the application suite.

### Historical disposition

The historical record contained useful evidence but no uniformly replayable suite.
The audit repaired seven families, merged two overlaps, retired one obsolete comparison, and added seven missing atomic scenarios.

| Historical family | Classification | Active disposition |
|---|---|---|
| Declared verdict and quoted-token loophole | Repair | `AR-02` |
| Unverified rationale plus caller-order invariant | Repair | `AR-03` |
| Standalone angle selection | Repair | `AR-04` |
| Durability failure paths | Repair | `AR-05` |
| Whole-project generated cases | Repair | `AR-06` |
| Fix-by-construction severity | Repair | `AR-07` |
| Holistic baseline and retained-angle focus | Repair | `AR-04`–`AR-06` |
| Duplicate red-flags composite | Merge | Atomic behavior in `AR-03`; history retained in [duplicate-red-flags-scenarios.md](duplicate-red-flags-scenarios.md) |
| Whole-repo/angle-selection overlap | Merge | Selection in `AR-04`; application in `AR-06` |
| Historical subjective discrimination arms | Retire | Preserved below; exact opaque-arm evidence is incomplete |
| Simple complete-bundle review | Add | `AR-01` |
| Shared finding-pattern synthesis | Add | `AR-08` |
| No-shared-pattern branch | Add | `AR-09` |
| Necessity challenge | Add | `AR-10` |
| Effectiveness challenge | Add | `AR-12` |
| Multi-finding no-shared-pattern branch | Add | `AR-13` |
| Replayable angle discrimination | Add | `AR-14` |

Counts: **Keep 0, Repair 7, Merge 2, Retire 1, Add 7**.

`AR-11` was an exploratory two-turn scope-guard probe, not an active addition.
Its current arm passed 5/5, but deleting the whole `End of posture` section also passed 5/5.
A later original-control run was confounded by the globally mandatory brainstorming skill and produced one reasonable clarification instead of a label.
The probe is therefore non-discriminating and retired rather than weakened after observation; its exact files remain in [exploratory-ar-11](fixtures/adversarial-review/exploratory-ar-11/README.md).

### Necessity and simplification review

Each section was challenged for necessity and for a simpler equivalent.
The result keeps distinct behavioral contracts and consolidates duplicate guidance.

| Skill section | Necessity and smallest effective form | Evidence |
|---|---|---|
| Frontmatter | Needed for routing; no duplicate owned routing test | `DISC-01` |
| Overview | Needed to identify the skill as a reviewer adapter and its invocation modes; two sentences are already the smallest scannable introduction | `AR-01` |
| Role | Needed to assign mechanics versus posture/output ownership; one precedence sentence resolves the only template conflict | `AR-01`, `AR-04` |
| Posture | Needed to distinguish adversarial review from ordinary completeness review; the compact contrast and counters induce the default mental model | `AR-01`, `AR-03`, `AR-05`–`AR-07` |
| End of posture | Retained as a compact scope guard on owner judgment; the exploratory ablation showed no causal lift, so no active scenario claims one | Retired `AR-11` |
| Severity rubric | Needed; P3 pass and blocking durability/invariant cases cover the meaningful branches | `AR-02`, `AR-03`, `AR-05`, `AR-07`, `AR-09` |
| Output format | Needed as a parser contract; finding shape, final verdict, enumeration, shared pattern, and `NONE` remain distinct | `AR-01`–`AR-03`, `AR-08`, `AR-09` |
| Enumerate every class | Needed and deliberately comprehensive; “every relevant set” was rejected because it permits silent exclusion | `AR-03` |
| Verify every rationale claim | Needed; one false 18% claim checked against 1.8% evidence is sufficient | `AR-03` |
| Necessity and effectiveness | Needed as one unified baseline section: remove unsupported pieces and reject activity/proxy success that does not advance the intended outcome | `AR-10`, `AR-12` |
| Generate unexercised cases | Needed; one whole-project scenario covers absent, malformed, out-of-scale, and beyond-patch reach | `AR-06` |
| Invariant grading / fix by construction | Needed; one isolated ordering boundary protects P2+, construction, and the documentation/test loophole | `AR-07` |
| Review angles | Needed only where the holistic baseline lacks a lens; selection, durability application, and one full-versus-holistic skill-authoring discrimination are sufficient | `AR-04`, `AR-05`, `AR-14` |
| Few-shot examples | Needed only to demonstrate exact output shape; no separate example scenario | `AR-02`, `AR-09` |
| Reviewer rationalizations | Needed as compact counters; application cases exercise the distinct failure modes without one scenario per row | `AR-03`, `AR-05`–`AR-07`, `AR-10`, `AR-12` |
| Composition | Needed to declare the base-review dependency and sibling boundaries | `AR-01` |
| Whole skill | Discovery plus thirteen atomic owned scenarios is the smallest suite that protects every retained observable contract and the demonstrated value of a specialized angle | `DISC-01`, `AR-01`–`AR-10`, `AR-12`–`AR-14` |

The enumeration miss had a concrete cause: the old prose required enumeration during review, but the output contract required only findings and a final verdict.
Evaluators could group callers behind phrases such as “other callers” and still believe they had completed the internal enumeration.
The approved repair makes member-by-member named accounting observable and removes the later duplicate warning.

The approved behavior slice also adds one evidence-backed `DD-PATTERN` line before the verdict and folds effectiveness into the necessity section.
The effectiveness wording is retained for clarity and owner intent, not claimed as measured lift: both the current and ablated `AR-12` arms passed 5/5.
The response-template precedence sentence is likewise an owner-approved clarification with preserved 5/5 behavior, not a claimed RED/GREEN lift.

## Active scenario catalog

Common metadata: Codex CLI 0.146.0; `gpt-5.6-sol`; high reasoning effort; Superpowers 6.2.0; five fresh processes per arm; maximum concurrency three; enforced read-only transport; no nested agents; evaluator-withheld rubric; orchestrator scoring; run dates 2026-08-03–04.
Every `AR-*` scenario is owned by and affects `adversarial-review`; shared `DISC-01` lists its cross-skill ownership separately.
The base-review dependency is Superpowers 6.2.0 `requesting-code-review`, skill SHA-256 `d71cc01ba56d2325cf8af5f7c11837819b63ecd57de0bfdb812f7f3ff7751df8`, template SHA-256 `b2f2ec7596925fe52dac158fdfbca19b3a7d779d619c481e6706a6c0001662d3`.
`AR-01` receives the complete nine-skill bundle recorded in [the fixture manifest](fixtures/adversarial-review/README.md#complete-bundle-dependency-manifest); other scenarios receive only `adversarial-review`, the base-review dependency, and their declared fixture.

| ID | Type / status | Protected promise and section | Supplied context | Exact prompt and withheld rubric | Rerun trigger |
|---|---|---|---|---|---|
| `AR-01` | Simple application + direct invocation / preservation | Complete-bundle review finds the documented defect and follows severity/output contracts; Overview, Role, Posture, Severity, Output, Composition | Nine skills + committed ratio fixture | [Prompt](fixtures/adversarial-review/prompts/ar-01.md), [rubric](fixtures/adversarial-review/rubrics/ar-01.md) | Direct invocation, dependency, severity, finding shape, or verdict |
| `AR-02` | Focused regression / preservation | P3-only review passes and quoted verdict content cannot replace the final verdict; Severity, Output, Examples | Prompt-contained completed review | [Prompt](fixtures/adversarial-review/prompts/ar-02.md), [rubric](fixtures/adversarial-review/rubrics/ar-02.md) | P3 threshold, quoted tokens, verdict position, or output shape |
| `AR-03` | Non-trivial application + focused regression / target | Every caller is named; false rationale is verified; asymmetric nonlocal invariant blocks; Output, Enumeration, Rationale, Invariants | Committed six-file normalization fixture | [Prompt](fixtures/adversarial-review/prompts/ar-03.md), [rubric](fixtures/adversarial-review/rubrics/ar-03.md) | Enumeration, caller accounting, rationale verification, invariant severity, or fixture |
| `AR-04` | Simple application + focused regression / preservation | Holistic baseline always runs and specialized angles select by artifact kind; Review angles | Committed artifact matrix | [Prompt](fixtures/adversarial-review/prompts/ar-04.md), [rubric](fixtures/adversarial-review/rubrics/ar-04.md) | Baseline/angle taxonomy, artifact classification, or JSON contract |
| `AR-05` | Non-trivial application + focused regression / preservation | Durability catches corruption and crash-on-input with construction remedy plus a holistic defect; Durability, Rationale | Real EventLog slice at `b0f4511b2d43a566acdcbc5f0d61db6342a4c882` | [Prompt](fixtures/adversarial-review/prompts/ar-05.md), [rubric](fixtures/adversarial-review/rubrics/ar-05.md) | Durability checklist, crash rationale, holistic baseline, or source slice |
| `AR-06` | Non-trivial application / preservation | Review reaches beyond the patch and generates located absent, malformed, and out-of-scale findings; Whole-repo scope, Unexercised cases | Committed import-boundary fixture | [Prompt](fixtures/adversarial-review/prompts/ar-06.md), [rubric](fixtures/adversarial-review/rubrics/ar-06.md) | Whole-repo scope, generated-case classes, or fixture |
| `AR-07` | Non-trivial application + focused regression / preservation | Plain-array producer ordering remains P2+ and unresolved by documentation/tests; Invariants, Severity | Committed excerpt derived from Steno range `0fae3e34d73505960313efa6ff7c6256c00f7029..59d08686570724d288c716a756984d364ef50e49` | [Prompt](fixtures/adversarial-review/prompts/ar-07.md), [rubric](fixtures/adversarial-review/rubrics/ar-07.md) | Invariant severity, construction rule, loophole, or excerpt |
| `AR-08` | Focused regression / target | Findings across API, queue, and file adapters receive one evidence-backed shared pattern without a new finding/severity; Output | Committed boundary-ingestion fixture | [Prompt](fixtures/adversarial-review/prompts/ar-08.md), [rubric](fixtures/adversarial-review/rubrics/ar-08.md) | Pattern syntax, named adapter accounting, evidence threshold, or synthesis boundary |
| `AR-09` | Focused regression / target | A single finding emits `DD-PATTERN: NONE`; Output | Committed health-status fixture | [Prompt](fixtures/adversarial-review/prompts/ar-09.md), [rubric](fixtures/adversarial-review/rubrics/ar-09.md) | `NONE`, evidence threshold, pattern placement, or fixture |
| `AR-10` | Non-trivial application / preservation | Unsupported duplicate state is challenged and removed; Necessity | Committed receipt proposal | [Prompt](fixtures/adversarial-review/prompts/ar-10.md), [rubric](fixtures/adversarial-review/rubrics/ar-10.md) | Necessity wording, removal rule, or fixture |
| `AR-12` | Non-trivial application / preservation | Activity/proxy success is rejected when it does not measure the governing outcome; Effectiveness | Committed onboarding proposal | [Prompt](fixtures/adversarial-review/prompts/ar-12.md), [rubric](fixtures/adversarial-review/rubrics/ar-12.md) | Effectiveness wording, outcome/proxy rule, or fixture |
| `AR-13` | Focused regression / target | Two unrelated blocking findings emit `DD-PATTERN: NONE` without generic over-synthesis; Output | Committed independent-provenance fixture | [Prompt](fixtures/adversarial-review/prompts/ar-13.md), [rubric](fixtures/adversarial-review/rubrics/ar-13.md) | Multi-finding `NONE`, evidence threshold, provenance, or fixture |
| `AR-14` | Non-trivial application + focused regression / preservation | The skill-authoring lens catches workflow-summary and untested-discipline traps that a holistic-only ablation misses; Review angles | Committed flawed skill, writing-skills 6.2.0 dependencies, and exact ablation patch | [Prompt](fixtures/adversarial-review/prompts/ar-14.md), [rubric](fixtures/adversarial-review/rubrics/ar-14.md) | Skill-authoring angle, supplied authoring guidance, ablation, or fixture |

### Results

Original control commit: `4296647f0dff48a9e77b979ef07e813bf1f66db2`; original skill SHA-256: `9004ff153d5dc3a3690254667c4f666151dcabff7ef6f705cc751134be56499c`.
Current approved draft SHA-256: `b266f35b751a23967d99030678ffe893d72137bf1ffbc7c433db811ed1bbf085`.

| ID | Original/RED result | Control date | Classification and exact misses | Current result | Current outcomes | Current date | Infrastructure errors |
|---|---:|---|---|---:|---|---|---:|
| `AR-01` | 5/5 (`P P P P P`) | 2026-08-03 | Preservation; none | **5/5** | P P P P P | 2026-08-04 | 0 |
| `AR-02` | 5/5 (`P P P P P`) | 2026-08-03 | Preservation; none | **5/5** | P P P P P | 2026-08-04 | 0 |
| `AR-03` | **2/5** (`F P P F F`) | 2026-08-03 | Watched RED. r1 omitted `bulk_normalize` and did not state that both sorting callers sort; r4/r5 omitted `validate_batch` and `bulk_normalize` and did not trace those sorting callers | **5/5 GREEN** | P P P P P | 2026-08-04 | 0 |
| `AR-04` | 5/5 (`P P P P P`) | 2026-08-03 | Preservation; none | **5/5** | P P P P P | 2026-08-04 | 0 |
| `AR-05` | 5/5 (`P P P P P`) | 2026-08-03 | Preservation; none | **5/5** | P P P P P | 2026-08-04 | 0 |
| `AR-06` | 5/5 (`P P P P P`) | 2026-08-04 | Preservation; every output traced unchanged importer behavior and found the absent-file, malformed-record, and 5 GiB memory paths | **5/5** | P P P P P | 2026-08-04 | 1 |
| `AR-07` | 5/5 (`P P P P P`) | 2026-08-03 | Preservation; none | **5/5** | P P P P P | 2026-08-04 | 0 |
| `AR-08` | **0/5** (`F F F F F`) | 2026-08-04 | Watched RED under the repaired all-three-adapter rubric; every output named API, queue, and file defects but omitted the pattern line and synthesis | **5/5 GREEN** | P P P P P | 2026-08-04 | 0 |
| `AR-09` | **0/5** (`F F F F F`) | 2026-08-04 | Watched RED; every output omitted `DD-PATTERN: NONE` immediately before the verdict | **5/5 GREEN** | P P P P P | 2026-08-04 | 0 |
| `AR-10` | 5/5 (`P P P P P`) | 2026-08-04 | Preservation; every output challenged the unsupported duplicate store | **5/5** | P P P P P | 2026-08-04 | 0 |
| `AR-12` | 5/5 (`P P P P P`) | 2026-08-04 | Preservation; every output rejected the wizard-completion proxy | **5/5** | P P P P P | 2026-08-04 | 0 |
| `AR-13` | **0/5** (`F F F F F`) | 2026-08-04 | Watched RED; every output found both unrelated defects but lacked the required `DD-PATTERN: NONE` line | **5/5 GREEN** | P P P P P | 2026-08-04 | 0 |
| `AR-14` | 5/5 (`P P P P P`) | 2026-08-04 | Preservation; with identical authoring dependencies available to every arm, the complete skill catches both authoring traps. Holistic-only ablation: **0/5** (`F F F F F`), every output missed both specialized traps | **5/5** | P P P P P | 2026-08-04 | 0 |

Current aggregate: **65/65 PASS**.
Preservation controls: **45/45 PASS**.
All four watched RED targets reach 5/5 GREEN; the `AR-14` holistic-only discrimination arm remains 0/5.
Raw evaluator transcripts remain uncommitted scratch artifacts.

Before freeze, cold review invalidated an earlier `AR-06` prompt because it named the three generated-case classes that the withheld rubric scored. Removing that priming exposed a second design problem: the broad real-source fixture contained many stronger unrelated defects, so outputs did not consistently surface all three classes. The active scenario replaces it with one atomic import-boundary fixture and fixes its patch metadata. A scoped re-review then exposed an over-specific rubric demand for a literal unchanged-file path even when a finding demonstrably traced the unchanged helper; the final criterion protects out-of-patch behavior instead. Every repair restarted both arms from zero, and no superseded run is counted above.
The final current arm had one infrastructure error: a complete response appeared in the execution log but the required last-message artifact was absent. An identical retry supplied the fifth evaluable response.

### Replay hashes

The exact bundle-digest algorithm, complete `AR-01` dependency manifest, and source/fixture manifests are in [fixtures/adversarial-review/README.md](fixtures/adversarial-review/README.md).

| ID | Original/RED bundle | Current bundle | Fixture digest or source manifest |
|---|---|---|---|
| `AR-01` | `b9d0fdb62e4fbbf58df32afd8dadeb92aeb3f17495afd8d6ad9ad76644b64b2d` | `9d2da380bb7754c1a756ce3f97eb26429623aee1919bf36093c18f23c7ef6797` | `e649e8171b59461a6acc1153e402f0ba03864137894052aafe61e94b157034df` |
| `AR-02` | `9f9ed9bf1f6207adc88881ad237fb4d0ff5058e9890f32f335491d15d8cb9f68` | `06c8fac830cd0f76336b3e4743b81145db87c8c51bd491094be0398a5b38821d` | Prompt-contained |
| `AR-03` | `4d0a16a4aa09c20c02d9682d99a595b85e47b4700e848cc3b272263ce78d317f` | `d9e8caf31fd44525521bd8b14cdbd48c68cb9f4f6052ed6231c25213661ee263` | `9f0b321743659dc5d1757065040fdfe4361bbca164454e29153155a9b24f8304` |
| `AR-04` | `413722aff2eadfdfaea2545923966846f64f44a3bf86eba514755f3e022c274c` | `cccc7975f243936c8a387d1ef65aee064350c9d3adb4aaa50a5fe223936be6db` | `4c4ce69c48cbf0c6e70fb326e66badeb7ee70b678f87dfe42e0969c9f643035b` |
| `AR-05` | `668e4ca719e5b311920336c8f036202a0d96e7362805adc72be030500cf1a96e` | `a71de6373f61b74ca6fd8c8d02d30dd770654b1c38c27474af5f67d4e811dd13` | Real-source manifest |
| `AR-06` | `c93ae68b82f07e34e7ceeb06ae0e2aefb3c149ec807a8e0dde8a7c9808af673c` | `5e75ae2860b99482ab700033dc5d8fe0241faeb53fa3449251d75762f2b2ce71` | `4d1b589859c509c8f7d5d0fad4ed35039d1490bd22e9b27f97048109fa932544` |
| `AR-07` | `9858504b49ea5fe81941ed391452f80e7d7983cc1c1c8f9e1fe2b42381edcef5` | `65c7db22c5b467372fe25af46751d220f521953917b2b2217a9d663d7650c2ed` | `15d0a79a8055485afe38dd09f68f9bdeabb6919efe22af36dbe4b9a02c1aa6f8` |
| `AR-08` | `f1ba98d7da412f1833e81a0074b2bcbeaa82534b4f95a94f295f10902f1a0d85` | `eab0ad23dda579d65a5f1c44805766846bf1243300868eb8b1d26b92ff21537c` | `648af0899b9dac0c0d57b1122027a2a46c3a33ab31f3214c6ab523596d8d12a3` |
| `AR-09` | `bbdb3bc8df9f75db48edcd3b55314231df870db3c9bb962656c897795a228eac` | `b83c130c1c14dfddbcc1a659491fe7d3d7d01703fb393c162bc72e1ed0bd995f` | `0b591ed214d2428181f70c51b928aed83490f8ca66eb64002db8409c78fd266e` |
| `AR-10` | `494e22a999f09cdfde87295f0eac2ba2f403ee549070377f40c3cdf9debb87fa` | `7dc90667fe5703937a3984925942fb77ecc2e96b57645628a6dae4d0abd03742` | `7403d026fa3b647dea3b6b18c2ae0d9e9edc0318cd10e222818803825e9bbc9a` |
| `AR-12` | `724f9e4f1e34c939e8e2e45f35c33770f3bac02dd0498a9b7af68ecddb4f0cc2` | `2cc97263dce09b63455c4d7881742dfc7b80408c8cf448ef6ce176500bc36743` | `8ebc3934102abf000fc21686c1c0ec5441f340abfbfa6f735facfb89b4738227` |
| `AR-13` | `60af81e4a7afae4b1809fb72a51b58c85735530d72fef9cb40b5906f9ffbba00` | `d95aa85a065c0b7fc70a5543fcb30fb135e9e65d24aac726995f9194a6f5ebc0` | `e1f1af3532c608d14c2e1656f0cc82dad2b24b97003bc273fc63b1ac6ae38e49` |
| `AR-14` | `688cd9b4d504089e1cf5a0b3b5d13c9598e563a73430adb63e65fe1f099c45a5` | `81a3ea02cb9253a1c80bbce4a5fc844bed37be07a94152964065352a14114f44` | `aa8d2b77c69d81104c4a342ae1553c02dc1a6b65d82f3200843632b1a89cc2c5` |

`AR-14`'s holistic-only ablation bundle digest is `4724c2b778e9b7ebbcad07080e743f77aa742412588e3794c8706ae9a0dad93f`.

| ID | Prompt SHA-256 | Rubric SHA-256 |
|---|---|---|
| `AR-01` | `b900f8dcea4585af8641052e01b54dc34f1419430d1916c63525d64735ecc27d` | `33c459e9042000e46c5f82488511d140b750ff53076d8ab11331cf24c91447ab` |
| `AR-02` | `471108bcba67e89a618f927a8fb2138624f0c1734ffef77db5792ab679c8d194` | `0f97269c27c2d801d14ed0687e73c9f519754d0a6404b388e3ef156f32e9ca09` |
| `AR-03` | `fa8499a73e1a3b58ad31c2b897bddd467b8ec29f894e1737e3f9424a5a0ad5c0` | `31b5fab1a4a9c34a8517c51ee58aa974b309a5cecad4780caab930e7c0cf4244` |
| `AR-04` | `d2dcfc886c023b2cbabd6364facb001e853b3ff655c29066b0a11bb797a1d4a0` | `a7e708bdaf6cc52e54d8368aacc1b7e1260f4f7ac8c45cc009334508d1a32b4b` |
| `AR-05` | `94158d5dc3d103db900b2b681cf7fb992e1cc82231e332de6da38d03af192e2d` | `fc29aeb715a8f9ece4b2573d153eed05adacc93d7a8eae296f2b1d0f263e84c4` |
| `AR-06` | `25d8a0ba5f7f752c50b018e93b3a2677df3588c7cc567b0d7d0c6a0bd2cec5bc` | `1fcc10f48c998b173626c37e61259ecf9bd41d2ea96b31c8b34086d14a94b924` |
| `AR-07` | `583d41453d2b6a2e52faaa779bf48de02ef3d236dca0b4899f02952bb6f686bd` | `a9f2bb2083974a0e6e793e26e0a3ced34dd4f5260b6d1359bb5e33dbc418f003` |
| `AR-08` | `9e5287bf4e2d5b899d9a30c3783242a6e332374256690d78a3bc036e19dce153` | `76a48aefaa2141c8ec81639201d386e9c22431a970896b97b861ce23aed54d2e` |
| `AR-09` | `9e5287bf4e2d5b899d9a30c3783242a6e332374256690d78a3bc036e19dce153` | `a7793ba00cfa9a414b10cc29f323ab9e73b4a37c8eeeb4818a6190ccfaed4725` |
| `AR-10` | `54d4cc9f5d8f62bb6486dd6266e0ef7fcf18d203ed2ae2b1752777bbf3378b41` | `6c161f73eab08e12f5b05bed900eb8efa08647365b064ac93417ee1a33f1b314` |
| `AR-12` | `9957e3f09da7dfd5d807b85825645f3d6f593499809cc623737309c14a1a26b7` | `0b84e78ffb224c2cf3be29eb4bb0ec45cb6d02f16021ba392b93859c3a2c5f99` |
| `AR-13` | `f1fd096b8ecda0523739b5c28b2eb9b009f6fdbaa898453518288a70b0017c16` | `3c69edfa734227c8710f1fdd0445808cbd288369fd29540a0404a92266cd809b` |
| `AR-14` | `62955b478d83abfb1c46533ea3899d4ed51aab839697ae0043cbcb94ab738fca` | `533e151b2e0d9f09880e9acbdd62d2ec9bf750c85d8e6d9324e75621827f76c6` |

## Historical evidence — not active scenarios

## Duplicate red-flag consolidation (2026-08-01)

**Edit.** Remove the `Red flags` section whose cases repeat the retained rules and rationalization table.

**Non-trivial shared matrix.** Review a cited-but-unverified performance rationale and a passing-tested design that relies on a nonlocal caller-ordering invariant while a sibling guards the same hazard locally.
PASS requires independent rationale verification, a P0–P2 invariant finding despite tests, and `DD-VERDICT: BLOCK`.

**Unprimed control: 5/5 PASS. Unprimed GREEN after removal: 5/5 PASS.** Every evaluator preserved citation verification and the stated/local/robust/symmetric invariant test.
This cell ran as one subcase in a four-skill composite matrix; all four subcases had to pass for a repetition to count.
Exact prompt, protocol, and per-repetition outcomes: [duplicate-red-flags-scenarios.md](duplicate-red-flags-scenarios.md).

Records how the `adversarial-review` angle set was derived and how to re-validate
it. The skill is standalone/portable: a consumer with only the skill can run a
review, name an angle, or list the angles — it requires no external command.

**Dispatch protocol.** Read-only and bounded per CLAUDE.md's evaluation-subagent
rule (Claude Code: `Explore`). One scenario per agent, text-only.

## The angle-necessity bar

An **angle earns its place only if it catches a class of issue the baseline
holistic review reliably misses.** The baseline is the always-on posture +
Rules (find what's wrong · enumerate every class · verify rationale · challenge
necessity · generate the unexercised cases). The test for an angle is **discrimination vs holistic**: plant a
*subtle* instance of the angle's class, then keep the angle only if a focused
reviewer catches it AND a holistic reviewer misses it. Goal: close the lenses
that make different models (codex vs claude) catch different things, so the
reviewer is model-consistent.

## Audit (2026-06-16/17)

Ran discrimination tests (holistic RED vs angle GREEN) on subtle planted targets
for seven candidate angles.

**Holistic caught the target in 6/6 of correctness, rationale, cross-file/
consistency, security, executability, necessity — and 4/4 conformance** (incl. a
noisy multi-issue diff, two independent holistic runs). Lesson: **per-angle
discrimination on a small artifact is the wrong instrument** — a strong model
following the posture catches everything when there's nothing to dilute its
attention. It discriminates only for (a) **scope** changes to a definition, and
(b) **specialized lenses the posture lacks**.

**Decisions:**

| Angle | Verdict | Why |
|---|---|---|
| correctness | **dropped** | the posture *is* "find what's wrong" — holistic caught it |
| rationale | **dropped** | already base posture Rule "Verify every rationale claim" |
| necessity | **dropped (as angle)** | already base posture Rule "Challenge necessity"; its Principle-7 + concise-writing pointers folded into that Rule |
| conformance | **dropped** | "verify against governing rules" is posture; holistic caught 4/4 |
| security | **deferred** | claude finds low-hanging secrets via posture; real leverage is a dedicated security skillset applied explicitly, not a one-line angle |
| **consistency** | **kept** | cross-corpus drift (contract/terminology/wording/single-source) is *not* in the posture; manually prompting it reliably yields findings |
| **executability** | **kept** | the zero-context-implementer lens; surfaced by the maintainer's codex-review gap observations (not reproduced inline here) |
| **skill-authoring** | **kept** | the **only** angle that beat holistic in discrimination — see below |

`security` was broadened (+ leaked secrets/keys) and tested cleanly (old def
returned "No findings" on a hardcoded key; broadened def flagged it P0) — so the
broadening *is* load-bearing — but the angle was still dropped per the bar above:
holistic already catches secrets, and a future dedicated security skill is the
higher-leverage home.

The pre-branch command also had `cross-file` and `doctrine-consistency`; both
folded into `consistency` (their drift / single-source concerns), and the
governing-rule half of `doctrine-consistency` became `conformance`, then dropped.

## skill-authoring discrimination (the one that passed)

Planted a skill whose `description` summarized the workflow and whose rule
("Always run the tests") had no rationalization-loophole counters.

- **Holistic (RED):** flagged executability/consistency issues but **missed** the
  CSO trap (description-summarizes-workflow → agents skip the body) and framed the
  open rule as a P3 "discipline smell," not as exploitable loopholes.
- **skill-authoring (GREEN):** caught both — the CSO trap and the open
  rationalization loopholes — applying the `superpowers:writing-skills` lens.

Holistic missed what the angle caught → it earns its place.

## Standalone angle selection

- **RED — pre-edit skill, doc-dominant artifact:** with selection delegated to the
  command, a skill-only agent **guessed** and excluded the right doc angle.
- **GREEN — post-edit skill:** the **When to apply** list lets a skill-only agent
  select correctly and answer "what angles are available?" — the portability goal.

## Per-angle focus (kept angles catch their target)

Each angle's definition transmits the right focus (a reviewer applying it catches
its class):

| Angle | Target | Result |
|---|---|---|
| consistency | terminology drift across the corpus; keyword-only arg passed positionally (cross-file) | ✓ flagged |
| executability | doc step with undefined deps / no command | ✓ flagged |
| skill-authoring | CSO description trap + open rationalization loopholes | ✓ flagged (holistic missed) |
| durability | INV-2 read-side (torn tail, interior blank line) + crash-on-bad-input rationale | ✓ lifted (baseline missed); generalizes to Python/Go |

## durability angle (added 2026-06-19)

Failure-path lens for code that mutates or reads durable / source-of-truth state.
**INV-1** durable mutations are atomic (or fully roll back + typed error + retry-safe);
**INV-2** reads reject anything not fully committed (torn tail, interior corruption,
gaps, unknown/forward version) and distinguish empty from corrupt.

**Why kept (per the necessity bar).** Single-model small-artifact discrimination
under-credits this class, so the angle ships on **lens-not-in-posture + the
cross-model gap**: in the meeting-pipeline PR-2 "event-log substrate" session,
codex's blocking pre-PR gate caught **8 failure-path defects across rounds 1–5**
(round 6 clean) while Claude's three holistic per-task reviews AND an Opus
whole-branch "ready to merge" missed every one — a whole unexamined axis. The
RED/GREEN below is **corroborating**, not a vetoable gate.

**Fixtures** (read-only `Explore`, subjects on sonnet; cold-read on opus; ≥5 reps
on the primary; every flagged match read by hand). Primary: the `b0f4511`
`EventLog.swift` (inlined in the durability deferred plan — ~160-line append-only
log, failure-path defects latent among correct happy-path code). Generalization:
a Python append-only JSONL log, a Go atomic-overwrite snapshot store (different
shape), a clean Go store (over-fire control), an in-memory rate limiter (skip
control). All are paper/transcript reviews.

**Results.**
- **RED (no angle) vs GREEN (angle), b0f4511, 5 reps each.** Baseline reliably
  caught the visible logic bugs (I/O error handling, line-count seq miscount: 5/5)
  but **missed the INV-2 read-side** (interior blank line 0/5, torn final record
  0/5) and accepted the planted "crash is intentional" rationale on the encode
  crash (1/5). GREEN: blank line → 5/5, torn tail → 3–4/5, crash-on-bad-input →
  5/5, reviewers explicitly citing the read/replay checklist and the crash
  rationale-counter. No regression on the two the baseline already caught.
- **Generalization.** Python log: angle adds the same INV-2 read-side over a
  (stronger) baseline, in different idioms. Go snapshot (atomic-overwrite, not
  append-only): catches all planted defects 3/3 incl. panic-on-bad-input via the
  rationale-counter — the lens is not tied to the EventLog/Swift shape.
- **Over-fire / skip controls.** Clean Go: no false P0s (only genuine subtle
  issues). In-memory limiter: reviewers correctly did NOT apply the angle (the
  When-to-apply gate held).

**Probe-wording iterations (each re-tested).** crash-on-bad-input probe sharpened
to counter "it's a programmer error" (NaN 0/5 → 5/5); de-Swiftified
(`try!`/`Codable` → panic/abort/unchecked-unwrap; "a value that satisfies the
static type") to generalize off Swift, re-confirmed across all fixtures; two-harm
wording added (torn record AND caller-can't-recover) to close a "crash-is-pre-write"
dodge — closes it when the probe is applied. Residual 4/5 on the Swift primary is
a globally-lenient reviewer that skips the probe, not a wording gap; not chased,
to avoid tuning to one rep. Finally the crash parenthetical was trimmed ~22%
(rebuttal + static-type counter + both harms kept) and re-measured at parity
(Swift 4/5, Python 3/3, Go 3/3) — confirming the remaining words are the
load-bearing core.

**Cold-read on the final skill (opus; consistency + skill-authoring).** 4 findings,
all P2/P3 (checklist-under-bullet asymmetry, parenthetical length, run-on,
table-row breadth); all dismissed with rationale — the asymmetry and the
parenthetical are load-bearing (the rationale-counter is a rebuttal + two distinct
harms, each measured to drive a catch, not redundancy), the rest advisory/locked.

## Declared verdict line (2026-06-22)

**Change (Output format).** Every review ends with a final line — the last non-blank
line — containing only `DD-VERDICT: PASS` or `DD-VERDICT: BLOCK` (PASS = zero P0/P1/P2;
P3-only still PASS); few-shot examples updated to match. Rationale: the pre-PR gate
reads the reviewer's declared verdict instead of prose-scanning `[P0]`–`[P3]` counts
(design Decision 7); internal reviews declare the same verdict so a logging tool can
parse it.

**Scenario (reproducible).** Subject reads the live skill, reviews an artifact, emits
its review output. Check the last non-blank line.
- **PASS:** findings → ends `DD-VERDICT: BLOCK`; clean → `No findings.` then
  `DD-VERDICT: PASS`. **Loophole:** when the artifact itself quotes verdict tokens, the
  operative verdict must still be the last non-blank line (quotes stay inline).

**Results.**
- **RED (pre-edit, excerpt ×3):** 0/3 emitted any verdict line — contract absent.
- **GREEN (live skill, sonnet):** findings → BLOCK and clean → PASS, parity across the
  initial draft and the trimmed/root-fixed versions (findings 7/7, clean 3/3); loophole
  (artifact quoting `DD-VERDICT:`) 4/4 — incl. 2/2 with no earlier-line guard.
- **REFACTOR (trim).** Verbose first draft trimmed to the parser-complete contract. An
  opus writing-skills cold-read (3 cycles) flagged an added earlier-line guard that
  *self-contradicted the few-shot examples* and was *unbacked* — the loophole probe
  passes without it (the last-non-blank-line anchor is the protection). Guard removed
  (root fix, not a third wording tweak); cold-read then clean (PASS).

## Whole-repo scope + angle selection (2026-06-22)

The Review-angles closing line changed from "Depth sets breadth — a quick pass… full
review…" to "Every review is deep and whole-repo, anchored to the active plan and
governing docs — no light or diff-scoped tier. Only the angles vary…" Companion to the parent skill's Gate 5 change —
[disciplined-development.md](disciplined-development.md) carries the scope RED/GREEN.

**Regression — standalone angle selection.** Per "On edits," re-ran selection on a
doc-dominant artifact (three runbook docs, no code): GREEN 2/2 selected baseline +
consistency + executability and skipped skill-authoring + durability with correct
"when to apply" reasoning. The reworded line did not regress selection.

## Generate the unexercised cases — baseline rule (added 2026-06-27)

Fourth always-on Rule under `## Rules` (after *Challenge every piece for necessity*):
enumerate every input / resource / boundary / bound the code touches and generate the
case the happy path skips (*absent* / *malformed* / *out-of-scale*); grade the relied-on
invariant (*stated / local / robust / symmetric*); run the false-positive autopsy (the skill's
*Before dismissing a false positive* trigger). Folds in the superseded `safe-by-accident` content (invariant grade + autopsy + 4 rationalization
rows + 4 red flags). Owner-confirmed as a **baseline rule, not an angle** (applies to nearly
any code). Plan: `plans/completed/2026-06-26-generative-unexercised-cases-baseline-rule-deferred.md`.

**Why (escaped-P1 grounding).** meeting-pipeline step-13 PR #25 passed every internal
review layer (per-task + 2 cadence + a Gate-5 whole-branch self-review) and was BLOCKED
by the external Codex gate on three P1s all internal layers missed: **A** model cache-miss
silently HF-downloads instead of erroring (D4); **B** a worker `result` missing
`transcript_ref`/`transcript_sha256` committed as a successful `transcription_completed`;
**C** a 5 s CLI timeout on a synchronous ~8-min transcribe route.

**Methodology — faithful, not synthetic.** Synthetic snippets were *contaminated*: stated
contracts in comments turned the gaps into trivial `consistency` catches (baseline 6/6).
The valid test is the real condition — a whole-repo, plan-anchored review of PR #25's
**pre-fix tree** (`66e7179`), where the bugs are genuinely silent (omission / library-default
/ unvalidated-trust), against the active plan + spec. Read-only `Explore`, opus; baseline
(no-rule copy) vs +rule, per-item catch rate.

**Results.**
- **C (out-of-scale):** the out-of-scale *face* fires reliably — 6/6 on the shipped (trim)
  wording, every rep surfacing an out-of-scale issue. The specific CLI-timeout bug landed 4/6
  (67%) on the shipped wording (pooled ~10/14 ≈ 70% across all forms) vs baseline 1/5 (20%);
  catches cite the lens. A measured lift on a real escaped P1.
- **A (absent/HF):** 0 across baseline AND +rule (~0/19) — a **knowledge gap** (needs knowing
  `huggingface_hub` auto-downloads); no review-method rule manufactures the fact.
- **B (malformed/payload):** 0 on the specific bug across all forms — an **outlier-hard**
  buried `?? ""` default behind an IPC-contract rationalization (Codex caught it; 19 Opus
  whole-repo reviews did not). The enumeration form began reaching B's exact trust boundary
  (1 rep flagged `completeStage` "commits without verifying… trusts the worker's result" as a P3).
- Both arms find a similar set of *other* real bugs (reprocess stale-errors, idle_shutdown
  dead-knob, decode/stall) — the rule doesn't change those.

**Form iterations (each re-tested).**
- *Question-checklist* (absent?/malformed?/out-of-scale?): C 3/5, B 0/5 — drift from the
  plan's specified form.
- *Enumeration directive* (the plan's form — "list every input/boundary; for each, generate
  the case the happy path skips," mirroring *Enumerate every class*): C 3/3, surfaced a new
  malformed-boundary finding; B still 0/3.
- *Anti-bloat trim* (rule section 262 words; load-bearing out-of-scale phrasing + enumeration
  directive preserved): C 4/6, face 6/6 — trim confirmed non-degrading.

**Verdict / limitation.** Ships on the **measured out-of-scale lift** — the face fires every
rep (6/6) and the specific bug is caught ~67% on the shipped wording vs 20% baseline — the
plan-specified, owner-confirmed form. **Not** a substitute for reviewer knowledge
(A), and does not reliably crack the deepest buried-validation case (B), though it reaches
B's site. Same limitation as `durability`: small-artifact discrimination under-credits
coverage value; the lift shows at scale / across the Codex-vs-Claude gap, not as a clean
single-reviewer discrimination.

## On edits

- Adding/refining an angle: run the **discrimination test** (subtle target,
  holistic RED vs angle GREEN). Keep only if holistic misses it. Back the decision
  with cross-model (codex) gap data where available.
- Changing the **When to apply** list or a definition: re-run the standalone
  selection RED/GREEN and the affected per-angle scenario.
- Changing the Output-format **verdict contract**: re-run the declared-verdict
  scenario (findings → BLOCK, clean → PASS, stray-line loophole).
- Changing a baseline **Rule** (e.g. *Generate the unexercised cases*): re-run the
  faithful escaped-P1 test — a real pre-fix PR tree, not synthetic snippets — baseline
  vs +rule per-item catch rate; measure each wording iteration against it.
- Limitation: small-artifact discrimination can't validate *coverage* value (it
  appears only at scale / across models). consistency and executability are kept on
  the lens-not-in-posture + codex-gap grounds, not on demonstrated single-reviewer
  discrimination; skill-authoring is the one with a clean discrimination result.

## Severity floor for fix-by-construction invariants + doc-comment loophole (RED 2026-07-04)

**Origin (escaped-P2 grounding).** meeting-pipeline menubar PR-2: a positional "soonest =
`upcoming[0]`" invariant in `MenuViewModel.make` (correct only under a caller sort three files away)
was graded **P3/advisory** by an Opus whole-branch Gate-5 review and closed with a **doc comment**;
the external Codex gate then BLOCKED the PR grading it **P2** and demanding the by-construction fix
(internal sort). Separately a negative-`limit` `Array.prefix` crash was graded a task-review "Minor"
and orchestrator-accepted on KISS grounds before the adversarial pass escalated it.

**Methodology — faithful (real pre-fix diffs, not synthetic).** Subjects: the session's real
review-package diffs — S1 `0fae3e3..b6fd695` (unclamped `prefix(limit)`), S2 `0fae3e3..59d0868`
(naked `index==0` countdown, no doc/sort); over-fire control S3 = final `MenuViewModel.swift` (footgun
fixed; target = the cosmetic "1 people" pluralization). Read-only `Explore`, **current (unedited)
skill**, plan-anchored. Measured: the severity assigned to the target + the fix recommended. (Synthetic
snippets rejected per this doc's 2026-06-27 contamination lesson.)

**RED results.**
- **Crash (S1):** blocking on BOTH models — sonnet 5/5 **P1**, opus 3/3 **P2/P1**; both DETECTED it
  8/8. **Not an adversarial-review gap** — the real "Minor + accepted" lived in the SDD task-review
  scale + orchestrator KISS-acceptance (a different path), which the adversarial pass then escalated.
- **Fragile invariant (S2):** **model-inconsistent.** Sonnet 5/5 **P1** + fix-by-construction (one rep
  explicitly rejecting "documenting the caller precondition alone"). Opus **3/5 P3-advisory + 2/5 P2,
  5/5 offering "document the precondition" as an acceptable fix** — reproducing the real Gate-5
  under-grade. Opus treats "correct in the wired path / single producer / display-only" as grounds for
  advisory + doc.
- **Over-fire control (S3):** pluralization P3/P3/P2 (sonnet) — baseline doesn't inflate the cosmetic.

**Decision.** The gap is Opus leniency on the fix-by-construction-invariant class — the cross-model
inconsistency these rules exist to close. Ships as two edits (model-consistency, bring Opus to
sonnet): (1) add the fix-by-construction-invariant class to the **[P2]** bucket in the severity rubric
(single-sourced there, not a separate override), so it can't be graded P3/advisory; (2) close the
**doc-comment loophole** on the invariant-grade
line (a doc satisfies only *Stated?*; enforce/unify, not document). Plus a `disciplined-development`
Principle 7 bullet + rationalization row for the orchestrator-acceptance path. **Dropped by RED:** a
separate crash-severity rule (both models already block) and an out-of-domain detection bullet (crash
detected 8/8) — evidence demanded neither.

**GREEN — both edit sets validated (opus).**
- *adversarial-review.* S2 re-reviewed with the edited skill: **5/5 [P2] BLOCK** by-construction (RED was
  3/5 P3-advisory PASS + 5/5 offered doc); reps quote "a doc comment only flips *Stated?*". S3 over-fire
  control: **3/3 PASS**, the pluralization nit stays P3 — the [P2] addition doesn't inflate unrelated
  findings.
- *disciplined-development.* Controlled orchestrator-adjudication test (identical scenario — a task-reviewer
  "[Minor] prefix(limit) traps on negative, only caller passes 3" — with unedited vs edited Principle 7):
  RED **3/3 ACCEPT** (deferring the crash via "wait for the edge case" / "accepted edge case"), GREEN
  **3/3 FIX** by construction. Clean discrimination; RED reproduces the real-session acceptance.

Fixtures preserved in the session scratchpad (`red-reviewer-instructions.md`, `red-results.md`,
`dd-adjudication-{red,green}.md`); review subjects are the two review-package diffs, reproducible from the
commits named above.
