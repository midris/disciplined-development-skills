# Disciplined development — validation

## Active catalog audit (2026-08-05)

The parent owns three active scenarios. They are the smallest catalog that tests the
parent's orchestration rather than duplicating child procedures: `DD-01` covers the
eight modes, active loading, negative boundaries, and four ownership seams;
`DD-02` crosses Gates 1–5 in one fixed non-trivial sequence; and `DD-03` protects
Principle 7's analysis-to-implementation
threshold. Fourteen inherited scenarios complete the parent baseline.

| Historical evidence | Classification | Active disposition |
|---|---|---|
| Whole-repository review scope | Repair | `DD-02` replaces the old one-off orphaned-safeguard probe with a replayable Gates 1–5 orchestration target |
| Principle 7 parser threshold | Repair | `DD-03` preserves the demonstrated contract/reachability/invariant boundary with exact prompt and rubric bytes |
| Mixed five-cell trigger matrix | Retire | `DISC-01`–`DISC-10` now own atomic description routing and parent-plus-companion availability |
| Eight-mode direct invocation and required/conditional/inapplicable selection | Add | `DD-01` simplifies the dense taxonomy to exact active loading, one explicit negative per row, no-op handling, and four ownership seams |

Classification: **Keep 0, Repair 2, Merge 0, Retire 1, Add 1**.
Superseded and mixed-protocol results remain compact historical evidence below; they
do not count toward the active baseline.

## Active scenario catalog

The owner and sole affected skill for `DD-01`–`DD-03` is
`disciplined-development`. Exact evaluator prompts and evaluator-withheld rubrics
are linked rather than duplicated here.

Common protocol: control commit
`4296647f0dff48a9e77b979ef07e813bf1f66db2`; Codex CLI 0.146.0;
Superpowers 6.2.0; `gpt-5.6-sol` at high reasoning effort; five fresh read-only,
no-agents processes per arm; maximum concurrency three; manual orchestrator scoring;
rubrics withheld; zero infrastructure errors in accepted runs. Excluded attempt-level
events were one outer-sandbox rejection before the accepted `DD-01` restart and two
incomplete `DD-02` attempts aborted by the orchestrator; all were retried unchanged.

| ID | Type / status | Protected promise and sections | Supplied skill context | Exact prompt | Withheld rubric | Rerun trigger |
|---|---|---|---|---|---|---|
| `DD-01` | Direct invocation + composition + focused regression / target | All eight modes select the exact current methodologies and companions, preserve one explicit negative boundary per row, distinguish loading from child action, choose model tiers by task complexity, and assign four ownership seams; frontmatter, Role/ownership, gates, Principles 1–8, mode table | Complete integrated bundle | [prompt](fixtures/disciplined-development/prompts/dd-01.md) | [rubric](fixtures/disciplined-development/rubrics/dd-01.md) | Description, parent/child ownership, required-sub-skill loading, gate/principle applicability, model-tier rule, mode row, methodology, companion-selection, or requested ownership-seam changes |
| `DD-02` | Non-trivial application + direct invocation + composition / target | One fixed development sequence preserves the Iron Law, all Gates 1–5, full-suite routing, artifacts, rereads, ownership, pass conditions, and blocked transitions without restating child procedures; Overview, Iron Law, Gates 1–5, Principles 1–6 and 8, rationalizations | Complete integrated bundle | [prompt](fixtures/disciplined-development/prompts/dd-02.md) | [rubric](fixtures/disciplined-development/rubrics/dd-02.md) | Iron Law, gate order/artifact, active methodology, full-suite routing, reread, TDD, verification, commit, Gate 5 review/smoke, or owner-boundary changes |
| `DD-03` | Focused regression / preservation | Analysis always generates cases, while implementation follows only for contract requirements, reachable accepted input, observed use, or robust invariants; Principle 7 and its rationalizations | Parent-only bundle | [prompt](fixtures/disciplined-development/prompts/dd-03.md) | [rubric](fixtures/disciplined-development/rubrics/dd-03.md) | Principle 7 threshold, accepted-input contract, malformed-input invariant, speculative-scale, or related rationalization changes |

### Immutable materials

| Arm | Scenarios | Content-manifest SHA-256 | Parent SHA-256 |
|---|---|---|---|
| Complete control | `DD-01`, `DD-02` | `ffeeb68d8fae44b81d4c1b57a7a92f6e5ed82fd6cc58e429cfcf4c826c8c8475` | `1151a7575a5b6f72e007229c97efdb7a829695d08e8f44450d0d71b232e75dec` |
| Parent-only control | `DD-03` | `49191f92b1cf5b2f3cfa51bc7066716c15b7671c960ded6bb1b1c7dfd8a38a76` | `1151a7575a5b6f72e007229c97efdb7a829695d08e8f44450d0d71b232e75dec` |
| Complete current target evaluated | `DD-01`, `DD-02` | `63bf6c72d8f61c8043c4bc8dd05bd28ca8d69da258de2d25bacaa8beddaaa29e` | `dff55e1348ebde0ec45c8b1861e48c000a5befdbd2f23deb4e857fa1945c93a6` |
| Complete formatting-only materialization | `DD-01`, `DD-02` | `085181b62e8124fbd7db9e9ea3d6e1dac458b14562046538afc4e210560327ad` | `dff55e1348ebde0ec45c8b1861e48c000a5befdbd2f23deb4e857fa1945c93a6` |
| Final gate-ownership target evaluated | `DD-01`, `DD-02` | `7f681413cdd4a27d6f83673f481007cb5951f7f42c4d5320398001c3e28e6766` | `dff55e1348ebde0ec45c8b1861e48c000a5befdbd2f23deb4e857fa1945c93a6` |
| Task 17 candidate integrated target | `DD-01`, `DD-02` | `3fc788a23bd66ce2977a43b4a2f8d71fa6a13515a3286df1baf3089c6a4c2a53` | `dff55e1348ebde0ec45c8b1861e48c000a5befdbd2f23deb4e857fa1945c93a6` |
| Parent-only current target | `DD-03` | `c5263d41f32f970cf75e78cf7b3d9ebfd0d655c9cd162a9625676d7880b60061` | `dff55e1348ebde0ec45c8b1861e48c000a5befdbd2f23deb4e857fa1945c93a6` |

The complete control archive SHA-256 is
`8f21c8267d005c349702ec94d6aff26c13a09bfbe29f2b43efcfbb37304f16e3`.
The complete bundle adds the exact Superpowers dependencies enumerated in the
[fixture manifest](fixtures/disciplined-development/README.md#control-bundles).
Task 17's repaired-definition control backfill reused the exact complete-control
content manifest `ffeeb68d…`, including original `concise-writing` SHA-256
`4d12a2eb475c6b2ef57e2300c8c07af3f59c1e07b2b82695a3b7669eee1d6d72`
and original parent SHA-256 `1151a757…`; it did not mix those bytes with the
candidate bundle.

| ID | Active prompt SHA-256 | Active rubric SHA-256 | Prior evaluated prompt / rubric SHA-256 |
|---|---|---|---|
| `DD-01` | `1b826fae8bf99ddc25ee831ee1b03ecce54c4552f8a302cb2558bee0e7e5c472` | `74e10f7c401903ba325a2b17adcc18805fa590d8d8e3bd07eb6d1a8216fdd94c` | `ba51dcfa160daffdb681c3bef0b993dc36ba1091c6e789826948331ebcc39d13` / `bbd1849b0b941c63282006e019f4cc5f24ad00e85897964c3f231d6ac4c97485` |
| `DD-02` | `5da5fe92259e8a7343ebc394eba326e06fa31c65eea3ee829de0157eeac8d528` | `627444473edc00e09f3974c5435911397627697821f24b0fe80d9851ed2f83cc` | same prompt / `ab8ab55f1e58fb9c2eaa68b695e426ca6c8f85c3ec8154a64b30804aaee958f3` |
| `DD-03` | `852eb66f0c3084e4f9aff349ae3775b5c70ca5c3221d1b6538d62ca603830b80` | `ead264e837afb0fe2aa974d0a9280e3c36e23d5079968f67da21bac6902c1c06` | same active bytes |

### Inherited coverage

These scenarios retain their existing owners and enter the parent's complete
closure by reference, not duplication:

| IDs | Owner | Parent obligation |
|---|---|---|
| [`DISC-01`–`DISC-10`](skill-discovery.md#active-catalog-definitions) | Task 1 shared discovery suite | Description routing and parent-plus-applicable-companion availability |
| [`DSD-01`, `DSD-02`](dispatching-development-subagents.md#active-catalog-definitions) | `dispatching-development-subagents` | Principle 4 dispatch contract and development-subagent versus orchestrator ownership |
| [`OWN`](adversarial-review-loop-scenarios.md#active-catalog) | `adversarial-review-loop` | Per-task and whole-branch review loops keep distinct owners, rules, and counters |
| [`WER-07`](writing-explicit-rationale.md#wer-07--parent-and-plan-composition) | `writing-explicit-rationale` | Principle 1 delegates rationale necessity without forcing a why for every defensible choice |

## Section necessity and simplification

| Parent section | Is it needed, and would simpler evidence preserve intent? | Smallest evidence mapping |
|---|---|---|
| Frontmatter, Role, and ownership | Necessary for parent discovery, companion co-selection, and the parent/child boundary. Shared discovery plus the two integrated scenarios is simpler than testing each description phrase or ownership sentence separately | `DISC-01`–`DISC-10`, `DD-01`, `DD-02` |
| Overview and Iron Law | Necessary to make every boundary fail-closed. The single checkpoint sequence tests the artifact rule more effectively than a separate slogan scenario | `DD-02` |
| Gates 1–5 | Necessary because each gate owns a distinct transition and artifact. The mode matrix plus one end-to-end sequence preserves all five without one scenario per gate; dispatch and loop cells cover the ownership seam | `DD-01`, `DD-02`, `DSD-01`, `DSD-02`, `OWN` |
| Principles 1–6 and 8 | Necessary as cross-gate rules. The two integrated scenarios exercise their selection and sequence, including Principle 4's model tiers; focused linked cells are sufficient where rationale, dispatch, or review-loop ownership needs pressure | `DD-01`, `DD-02`, `WER-07`, `DSD-01`, `DSD-02`, `OWN` |
| Principle 7 | Necessary to separate mandatory analysis from evidence-backed implementation. One three-case threshold scenario is simpler and more discriminating than repeating simplicity prose across modes | `DD-03` |
| Mode table | Necessary as the compact router for eight work states. One eight-row direct invocation is the smallest complete matrix | `DD-01` |
| Common rationalizations | Necessary only where pressure could bypass a rule. Distribute that pressure across the end-to-end sequence, the threshold case, and the subagent identity case rather than create row-by-row scenarios | `DD-02`, `DD-03`, `DSD-02` |
| Whole skill | Necessary as the orchestration layer. Three owned IDs plus fourteen linked IDs are the smallest complete baseline; an additional whole-skill scenario would duplicate the same contracts | `DD-01`–`DD-03`, `DISC-01`–`DISC-10`, `DSD-01`, `DSD-02`, `OWN`, `WER-07` |

## Sol-high results

| ID / arm | Bundle | Result | Repetitions | Exact misses | Accepted / excluded infrastructure events |
|---|---|---:|---|---|---:|
| `DD-01` control | Complete control | **0/5 watched RED** | F / F / F / F / F | R1/R4/R5 missed required methodologies in C, D, and E; R3 missed them in C and D; R2 had broader routing omissions. All five selected the requested model tiers correctly | 0 / 1 pre-arm transport rejection |
| `DD-01` current | Complete current target | **5/5 PASS** | P / P / P / P / P | None | 0 |
| `DD-02` control | Complete control | **0/5 watched RED** | F / F / F / F / F | All five put smoke commands/results in the PR body rather than `plans/export.md`, the Gate 2 artifact; R1/R4 also assigned reviewers findings rather than verdicts, and R5 omitted the major-transition rereads | 0 |
| `DD-02` current | Complete current target | **5/5 PASS** | P / P / P / P / P | None after orchestrator adjudication of the scorer's R3 reordered-gate false positive | 0 / 2 orchestrator-aborted retries |
| `DD-03` control | Parent-only control | **5/5 preservation PASS** | P / P / P / P / P | None | 0 |
| `DD-03` current | Parent-only current target | **5/5 PASS** | P / P / P / P / P | None | 0 |
| `DD-01` Task 17 candidate | Task 17 candidate integrated target | **5/5 PASS** | P / P / P / P / P | None | 0 |
| `DD-02` Task 17 candidate | Task 17 candidate integrated target | **5/5 PASS** | P / P / P / P / P | None | 0 |

### Task 17 concise-writing candidate integration rerun (2026-08-08)

The owner-approved `concise-writing` always-on routing contract changed the active
selection expectations consumed by `DD-01` and `DD-02`. The active fixtures were
repaired before the fresh restart: `DD-01` requires `concise-writing` where plan,
doc, or spec prose is written and permits it for ordinary response prose without
granting authority over code or exact machine artifacts; `DD-02` records the same
boundary at checkpoint 2. Prior prompt/rubric arms remain historical and are not
mixed with these results.

The candidate arm root was `/private/tmp/dd-task17-integrated-final`. Its complete
integrated bundle had content-manifest SHA-256
`3fc788a23bd66ce2977a43b4a2f8d71fa6a13515a3286df1baf3089c6a4c2a53`
and included candidate `concise-writing` SHA-256
`f763b43e88c56d6fdc2a96457bc2415cba60b75a1e7cb59cd1b0ebaa3fb199ba`.
Both scenarios used five fresh `gpt-5.6-sol` high-effort processes, maximum
concurrency three, read-only sandboxing, and disabled agents. All ten responses
completed on attempt 1 with zero infrastructure errors and were manually scored
5/5 by the orchestrator.

These 10/10 results remain valid for the recorded candidate bytes. The later
owner-approved repair changed only `CW-19`'s rubric, not this integrated bundle,
either development scenario, or the `concise-writing` skill, so `DD-01` and
`DD-02` do not restart.

| ID | Prompt SHA-256 | Rubric SHA-256 | R1 | R2 | R3 | R4 | R5 | Result |
|---|---|---|---|---|---|---|---|---:|
| `DD-01` | `1b826fae8bf99ddc25ee831ee1b03ecce54c4552f8a302cb2558bee0e7e5c472` | `74e10f7c401903ba325a2b17adcc18805fa590d8d8e3bd07eb6d1a8216fdd94c` | P | P | P | P | P | **5/5 PASS** |
| `DD-02` | `5da5fe92259e8a7343ebc394eba326e06fa31c65eea3ee829de0157eeac8d528` | `627444473edc00e09f3974c5435911397627697821f24b0fe80d9851ed2f83cc` | P | P | P | P | P | **5/5 PASS** |

#### Task 17 repaired-definition control backfill (2026-08-08)

The fresh root `/private/tmp/dd-task17-repaired-definition-controls` froze the
active prompt and rubric hashes in the table above against original complete
control bundle manifest SHA-256
`ffeeb68d8fae44b81d4c1b57a7a92f6e5ed82fd6cc58e429cfcf4c826c8c8475`.
Each scenario ran five fresh `gpt-5.6-sol` processes at both high and low effort,
read-only, with agents disabled, maximum concurrency three, attempt 1, and zero
infrastructure errors. Independent scorer files retained every repetition-level
reason.

| ID / effort | R1 | R2 | R3 | R4 | R5 | Result | Score-file SHA-256 | Exact miss summary |
|---|---|---|---|---|---|---:|---|---|
| `DD-01` high | F | F | F | F | F | **0/5 watched RED** | `afe526c5507222a5621a8312f61351b693d65e180557fe0ed0908467de71b589` | R1 omits B's required `concise-writing`; R2/R4 omit broad methodology and companion sets; R3/R5 repeatedly omit `writing-explicit-rationale` and give D an extra methodology |
| `DD-01` low | F | F | F | F | F | **0/5 watched RED** | `b8fc0a8635d03507e545aa01719d48014bce29a2857795bd5ac3c48c0076f33a` | R1/R2 have broad omissions; R3 omits B's `concise-writing` and adds two methodologies to D; R4 omits required sets in B–E; R5 omits B's `concise-writing` |
| `DD-02` high | F | F | F | F | F | **0/5 watched RED** | `ea829f9dd99b8a698622e46ec3ed9a4366725291492704dc779e09dcaa4657fe` | Every repetition writes smoke evidence to the PR body instead of the Gate 2 artifact and fails the exact reviewer-verdict contract |
| `DD-02` low | F | F | F | F | F | **0/5 watched RED** | `a1c82400e59b59e34a14e1604dc537edbf1dcc1c67d9afb2c74b02ce1471ff3e` | R1/R3/R5 miss the Gate 2 evidence destination and reviewer `DD-VERDICT: PASS`; R2/R4 also repair before the required self-review surfaces the issue |

| ID / effort | R1 output SHA-256 | R2 output SHA-256 | R3 output SHA-256 | R4 output SHA-256 | R5 output SHA-256 |
|---|---|---|---|---|---|
| `DD-01` high | `ad597eb0cdf9d49e3a0035bee855e8eef3f89d5c9990df57792052cbc334b778` | `3bfcee0a42aa86c0c7036e6072e3497fd2be03ab3b760e18809dc3f3c4ee6609` | `b483c707c03e854de317726712d907597bead5fef1e031001d709e9e68828f02` | `406992f3e01ec0f9fdbd03dea2b52926de92197554128e6e3b7cc13ae4a0df4f` | `16ea044c8983bdd9c119b7e6e8bf7ec37c88002fc5e7389ae076cdd7973310f1` |
| `DD-01` low | `d247544b265d1156f2ef452614d442e632767eb4eec671829b1026d9d9d51318` | `ddbd1b868424f64d0113a8ed2e0d8af318ced8f99a0432efb60b6fa4d72ea5ff` | `ccfaab8e9f760d589a9957e639aa04234127ea2d97223f9bc5e22b2ebc8a2110` | `2155a66615e7f7d26ebe65a89c2e90534daf4c9ed54edad7dae0c87ac76d947d` | `e64708ff9bcec00c8f62ab91305c8fb4f6b14f406a53a781963c7bcf31553bd0` |
| `DD-02` high | `81a79e1df1094455518248eed4242d9d14cf1d89a6ee84eb4fef2de516ea349d` | `4da515207bab5fdeaebbf70791d79cf8d0039e827dfefbe640e5827b03b2d808` | `cc60961e94bcc779bdbda9de869ff001e9584b2d78fa7ecd72beed412c0f5f0c` | `033262eaaeefb68c4898987c1d6f0baefb6c538dc8d1fc5425179d3792263610` | `3b7adeac6dae28a424122c391630d906f31a680e158e6aa5b6845cb249842875` |
| `DD-02` low | `8e72f81a71e8d5cc32bf47748942916881723c759dd543b7a38fe86c5daf4918` | `7fae31122796eabfa0d2678c40d16465845bf762a98da30287b76e6165270c70` | `99a08199f91b70e8bde85d14db38fc30ac092ff846965e40f94660cc18da5934` | `d53546684e3e6d7375768efd986d70305fd8dcccff0fb203efc92114426558db` | `6d3f4c243c4ae42cc975b8963a5ca40696f8c7a54cffd238028fc718974c0aeb` |

These are the active Task 17 target REDs under the repaired definitions. Earlier
control results elsewhere in this record remain preserved under their historical
definitions. The
paired candidate arms above remain P/P/P/P/P for both IDs, so this backfill closes
the required control/candidate comparison without changing the candidate 10/10.

## Task 11 Sol-low control results (2026-08-07)

These are the frozen low-effort control outcomes. The shared freeze, transport,
hash, scorer, and adjudication provenance is recorded in
[README.md](README.md#task-11-sol-low-control-freeze-and-results).
Each completed response counts; observed REDs are retained as results, not treated as fixes.

| ID | Status | R1 | R2 | R3 | R4 | R5 | Score | Exact missed criteria / adjudication |
|---|---|---|---|---|---|---|---:|---|
| `DD-01` | target | F | F | F | F | F | **0/5** | Every routing matrix omits required exact methodology/companion sets or violates an ownership seam. |
| `DD-02` | target | F | F | F | F | F | **0/5** | Every ledger misses the exact Gate 5 pass/ownership/artifact sequence and/or delegates child mechanics at the wrong boundary. |
| `DD-03` | preservation | F | F | F | F | F | **0/5** | All choose the three smallest case actions correctly but omit the explicit distinction between mandatory analysis-time case generation and the narrower implementation threshold. |

Owned Task 11 Sol-low aggregate: **0/15**.

### Final gate-ownership rerun (2026-08-06)

The owner approved a dispatch-skill clarification that reserves every review
and gate action for the orchestrator. Because `DD-01` and `DD-02` consume the
complete integrated bundle and score that ownership seam, both scenarios
restarted on the final bundle above. Each passed five fresh `gpt-5.6-sol`
high-effort repetitions through the enforced read-only, no-agents transport;
the orchestrator manually scored every criterion, and all accepted runs
completed without infrastructure errors.

| ID | Result | Repetitions | Exact misses | Infrastructure errors |
|---|---:|---|---|---:|
| `DD-01` | **5/5 PASS** | P / P / P / P / P | None | 0 |
| `DD-02` | **5/5 PASS** | P / P / P / P / P | None | 0 |

The only repository component changed after the formatting-only materialization
was `skills/dispatching-development-subagents/SKILL.md`, now SHA-256
`93a13cd44ddd350b00477db6cb9e285d16816c20edf7c9be52931f608df4cc6a`;
all declared Superpowers 6.2.0 dependencies were unchanged. One `DD-02` response
loaded `writing-explicit-rationale` at the unresolved-decision checkpoint but
did not direct child action there. The orchestrator adjudicated it PASS under
the parent's explicit rule that required loading does not itself trigger the
child; the response used the companion at the subsequent write-down boundary.

The later staged `review_nudge.py` recovery-text change is outside the parent-owned
bundles and meets no `DD-01`–`DD-03` rerun trigger, so those results remain
current. It did meet inherited `DSD-02`'s hook-message trigger. The 2026-08-06
5/5 arm is historical because its manifest named a superseded hook hash. On
2026-08-07, the exact current bundle passed five fresh orchestrator-run
repetitions P / P / P / P / P across all four rubric criteria, with zero
infrastructure errors.

`DD-01`'s dense required/conditional/inapplicable taxonomy produced prompt/rubric
shape evidence rather than a stable routing signal. The final contract asks only for
the authoritative active load set, one exact negative per row, and four requested
ownership seams. A corrected-bundle target scored 4/5 when row D did not explicitly
request reporting due parent gates; the pre-approved prompt repair made that behavior
observable and both arms restarted from zero. A rubric-only repair
removed a duplicate Principle 8 requirement and was rescored without a behavioral
rerun because it changed no evaluator input or behavior criterion. Staged review
cycle 2 then found that Principle 4's model-tier rule was not observable. A
pre-approved prompt/rubric repair added three task-complexity choices to row D and
restarted both arms from zero; the final control scored 0/5 and current target 5/5.

`DD-02`'s earlier prompt-shape target scored 2/5. Later original and confirmation
arms scored 4/5 and 3/5: repeated omission of REFACTOR exposed an observability
mismatch between the prompt and rubric, not a skill regression. The final prompt
states the complete RED-GREEN-REFACTOR requirement explicitly. A corrected-bundle
target then scored 4/5 because checkpoint 3 did not explicitly require the subagent
to load the parent; that exact prompt repair triggered another zero restart. In the
final target, the orchestrator adjudicated R3 PASS: the current execution skill puts
the implementer commit before the task-review package, while the rubric and response
still block that commit on scope, RED, tests, CLI evidence, and sweep, and block task
completion and branch gates on the task-review verdicts. No gate was reordered.

All accepted runs had zero failed evaluator processes. The pre-arm rejection and two
incomplete final-target attempts were retried unchanged and excluded as infrastructure
events. Raw artifacts remain uncommitted scratch files.

After evaluation, the rationale companion's approved paragraph was split onto
separate source lines with no word, punctuation, predicate, or rendered-structure
change. This met no `DD-01` or `DD-02` behavioral rerun trigger before Task 11;
their 5/5 results therefore carry forward to the formatting-only manifest above.

### Complete current closure

| Coverage | IDs | Result |
|---|---:|---:|
| Parent-owned | `DD-01`–`DD-03` (3) | **15/15 PASS** |
| Shared discovery | `DISC-01`–`DISC-10` (10) | **50/50 PASS** |
| Dispatch composition | `DSD-01`, `DSD-02` (2) | **10/10 PASS** |
| Review-loop ownership | `OWN` (1) | **5/5 PASS** |
| Rationale composition | `WER-07` (1) | **5/5 PASS** |
| **Complete parent closure** | **17 IDs** | **85/85 PASS** |

The linked closure is **70/70 PASS**.

## Compact historical evidence

Before the common protocol, the parent record used Claude Code `Explore`, Sonnet for
scenario runs, and Opus for cold reads. Those results remain derivation evidence,
not active scores:

- **Whole-repository review scope (2026-06-22):** four control responses followed
  the old chunk-diff wording and missed an orphaned safeguard outside the diff;
  three edited-skill responses used whole-repository, plan-anchored scope and found
  it. `DD-02` now owns the replayable version.
- **Principle 7 threshold (2026-08-01):** one control and three edited-skill
  responses all distinguished required absent/malformed handling from an ungrounded
  scale case. `DD-03` preserves that demonstrated behavior under the common protocol.
- **Trigger routing (2026-08-01):** the old five-cell mixed matrix passed three
  responses per arm but combined unrelated routes. `DISC-01`–`DISC-10` replace it
  with atomic, owner-maintained coverage.
- **Companion discovery and rationale composition (2026-08-01–05):** their useful
  evidence moved to the shared discovery and `WER-07` catalogs, which now enter this
  record by reference.
