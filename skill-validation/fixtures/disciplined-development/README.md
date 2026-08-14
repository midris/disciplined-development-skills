# disciplined-development replay artifacts

These files are the exact evaluator prompts and evaluator-withheld rubrics for the active parent-owned catalog.
Evaluators receive only the matching prompt and immutable read-only bundle, never the rubric or this manifest.

## Task 18A atomic/composite split (2026-08-13)

Task 18A retains `DD-01`–`DD-04` as broad or previously isolated controls and
adds `DD-05`–`DD-09` as one-seam behavioral scenarios. The split makes source
reconciliation, written scope, delegation/RED, candidate acceptance, and pre-PR
review independently rerunnable while `DD-02` remains the end-to-end composition
check. All rubrics grade actions, effectiveness, timing, ordering, ownership,
blocked transitions, evidence, and truthful bookkeeping; rendering differences are
not failures.

The current parent SHA-256 is
`872529574af4f4fabcd58ff3721ce6c241af99936c19403b40abca7e9c252e8b`.
Its final first-action repair was checked at
`/private/tmp/task18a-parent-all-sources-v69`: `DD-01` and `DD-09` passed 10/10
behaviorally. The five nominal `DD-01` scorer misses conflated an evidence-based
review finding/disposition with implementation ownership even though every output
left remediation method with the applicable review loop and gate acceptance with
the orchestrator or user. The exact-hash cold review at
`/private/tmp/task18a-v70-parent-cold-review.md` returned `VERDICT: PASS`.
Final union v71 then exposed one genuine row-B timing miss. The narrow final repair
makes the existing Gate 2 block explicit: rereading alone does not release
implementation planning before complete written scope and required sign-off.
Focused root `/private/tmp/task18a-dd01-planning-block-v72` passed `DD-01` 5/5,
and `/private/tmp/task18a-v72-parent-cold-review.md` returned `VERDICT: PASS` at
the current exact hash. Union v73 restarted from zero and passed the parent catalog
45/45 behaviorally.

| ID | Isolated behavior | Prompt SHA-256 | Rubric SHA-256 |
|---|---|---|---|
| `DD-04` | Principle 6 selection before an action that relies on a factual premise | `939a40cfe8fe27025ad8c83230830f000c8db0a67c440af0f42cf21925c9183f` | `275eb747335ff0f5d4b7933d43958332e33215db4a04dd8695c7e3e8327e8466` |
| `DD-05` | Fresh source reading, conflict ownership, and pre-planning block | `250300e505f05a6e1b139a352f1887e5116ac90ef99c18ac4b1c6d0139458ee4` | `cc900e882777acac4bb63f516861fa230ebb2ca33581ed463985062c91c8bd8c` |
| `DD-06` | Signed written scope with deferral cause and consequence | `0c296fd4f2a4245643e4ad17e746c06499e8ee920797721f654a6cf0aa74dda5` | `701ce6503df5e72fe2617b391caea8a66a19533f4c8054aa1f1d6bc7d064b1b2` |
| `DD-07` | Scope-bounded delegation, directly observed RED, and retained acceptance authority | `c79eb2bc14d0d9860a808c8875defc1f21bfaa7ec6a2ab356a08fe2c2cf88fd1` | `f8d47d834f1e29b5f3f61e3f1bb0e52cef7fea11d4fb20eef3626ca4a6d1889d` |
| `DD-08` | Unauthorized-candidate disposition before verification, effective sweep, and one green commit | `fc5e306045d9a6ff3e49913320ea48cff6fada7eb637d9aa0e0463c52dd6ced9` | `7dfb9766ffb31271028c1a4c97b1199b5251ab32e0bae79b73881ed828ee7283` |
| `DD-09` | Whole-tree pre-PR discovery, restart semantics, reviewer boundaries, and durable smoke evidence | `d0d0234d9688666656862f6a874e7ca491bd9b0d32b16ea1cdaad083f229a67d` | `a2e99c0a3cab2e3968d3e300489e1f6de484239ff442db49b8aec8ad02b26d3c` |

## Behavior-first DD-01 contract epoch — approved proposal applied; focused 5/5

The behavior-first comparison kept the prompt at SHA-256
`b41c2835573b645e101280c2928c97f5363f519d73c769568924c3ded8f658ce`
and used rubric SHA-256
`bb994c3b2e4adfc4feead9220ab9df89d53f5a74d1efa0e6bffbf733c7c0c9bb`.
The rubric grades clear behavior; terminology differences are advisory, while
ambiguous behavior still fails. It does not reclassify the strict-terminology
evidence preserved below.

| Arm | Exact skill SHA-256 | Sol-high result | Sol-low result | Verifier SHA-256 | Adjudication SHA-256 |
|---|---|---:|---:|---|---|
| Pre-application tracked parent | `34e105ccfd08f4b08e4879e6280ee9c2c9092d7f714d8fd7d47048f4059b1723` | F/F/F/F/F = 0/5 | F/F/F/F/F = 0/5 | `def4fb3731139df4a02fcc0ebb4c286ef59ca3c664fc1450074c1f1c2c77a9a5` | `fd67624ad3575e391f248393997295307cc9042f5adadf3f0f65513d118058d0` |
| Exact cycle-7 proposal | `3ed5c984c583aa0498366c091c42f57af0dda3722cc87a02c6c34d831d87c296` | F/F/P/F/F = 1/5 | Not run | `7403b8eb16c84852b18b5ee3ed85c75523e6694c612ae75948658542d882e26d` | `fa62a9d119ea5d502fdfa3bfeea42a584b90320a26fe5b99ec0a88dc1fb3f044` |
| Effectiveness cycle 1 | `907d0fdac467a647d8d3510e1706157431a06ccd0a71758993bce7fe2f178e51` | P/P/P/P/F = 4/5 | Not run | `f3c2467dd68ce8c1e1595038f110f58d37a06f21a14ac2cf40ac15a966746eae` | `59042db9ab18489834f391df0416feb43ffb3e9726aedafc144e81bdab4c298b` |
| Effectiveness cycle 2 | `ace5586bd09b7395135ffd10e9c23119ab9819911623a7babe6936044c64672c` | P/P/F/P/P = 4/5 | Not run | `acbff2d1cb32c26aa328b4549cf8134e6b7c366a650b22d94ba9fd5af0ebdc2f` | `9b8326da7a575421696eb6073a8ea24d8c30aa208e572ae734213705a32164d3` |
| Effectiveness cycle 3 | `652abda14206472f28e5e0a8bb7c8cc2b197df32bad2d5ebaba9d00e014e608b` | P/P/P/P/P = 5/5 | Not run | `64f9acdd44f06f48b597ce6f10a52750eab5c1557fbb1d44c79603ef9cc3bed2` | `11bcd0cfbbf63eda227ec098268b999dc33fcb5bc6e77170e7e5c3d649cd98ce` |

The baseline and cycle-7 15 evaluator slots selected `a1`, with zero retries or
infrastructure errors. The effectiveness loop's 15 additional slots also selected
`a1`, with zero retries or infrastructure errors. The baseline freeze / plan hashes are `a888fad7ec1117e8d01128d7731edc1a85806febcfddbb39299cf7889000f340`
/ `89672ca6036dd0737e7e165cff0373e58398bc62452e49dcecac0ec3a09829dd`;
the cycle-7 freeze / plan hashes are
`d10e460f35fccd032fd44b14ea1b65cf5749004d23b5bfa2a7c6203aee2ee6fc`
/ `8e7c12bda7667ca3ee758ce59b5d2e152682938b0b5cd51db7bce831ed310f64`.
Cycle-7 repetitions 1, 2, 4, and 5 fail because section E does not clearly
block implementation planning through contract reread and written scope;
repetition 3 passes despite terminology differences.

The effectiveness loop repaired one observed behavior class per proposal: cycle 1
made the debugging planning/editing boundary explicit, cycle 2 required
evidence-grounded options, and cycle 3 required decision-owner selection before
scope. It stopped at the authorized three-cycle cap with focused DD-01 5/5.

This epoch covers DD-01 only. It does not validate DD-02, DD-03, or the complete
skill suite and does not establish skill GREEN. The owner approved cycle 3 as the
complete proposal, and it is now applied byte-for-byte as the tracked parent at
SHA-256 `652abda14206472f28e5e0a8bb7c8cc2b197df32bad2d5ebaba9d00e014e608b`.
Its authenticated focused DD-01 5/5 evidence carries forward because the applied
bytes are identical. Checkpoint commit
`c9f0eba148ff73477c41e4403ea5dcd8baf4f7db` records this approved applied-parent
baseline. The owning validation record preserves the subsequent DD-02 epochs;
DD-03, child composition, and union validation have not rerun. This does not
establish parent GREEN or authorize a PR.

## Active DD-02 contract

The active prompt is SHA-256
`95deb13830eea682f06086c406dedb1a537b22f1bbf60598c4e1c231256ee706`
and the behavior-only withheld rubric is SHA-256
`801a1e8192a632c5aacee1ad63234af0987e73a498ad41dcba90610843181742`.
The evaluator bundle is the tracked parent plus the seven exact `project/dd-02`
members listed below; `operator-note.md` is excluded. The
[owning validation record](../../disciplined-development.md#formal-dd-02-behavioral-rubric--minimal-gate-4-proposal-55)
contains results and adjudication provenance.

## Historical strict-terminology DD-01 epoch — final fail-fast cap reached

The prior tracked parent was SHA-256
`34e105ccfd08f4b08e4879e6280ee9c2c9092d7f714d8fd7d47048f4059b1723`.
It was applied and had complete in-place owner approval. A fresh candidate arm observed
`DD-01` 0/5, `DD-02` 0/5, and `DD-03` 5/5. The repaired-rubric high/low
controls are accepted, but a candidate must rerun fresh after any approved repair;
the parent is not GREEN. A later focused comparison gave both the complete ignored
lean-ledger and ASCII-flow proposals `DD-01` 0/5 and `DD-02` 0/5. Neither is
accepted or applied; the flow variant is abandoned and the lean variant requires
narrow revision before another candidate run.
A narrower complete lean-v2 proposal `06280f03…` then scored `DD-01` 0/5 and
`DD-02` 1/5 under the then-active strict-epoch rubrics. It is also rejected and unapplied;
`DD-03` was not run because the focused pair did not reach 10/10.
Nine fail-fast complete proposals ran across two rubric epochs. Cycles 1–6,
frozen under historical rubric `e2076d7c…`, progressed 0/5 → 1/5 → 3/5 → 5/5
→ 3/5 → 1/5. Cycle 4 `bcab889d…` alone unlocked `DD-02`, which scored 0/5,
so `DD-03` stayed locked. After the strict-epoch rubric repair, cycles 7–9 scored
`DD-01` 0/5 → 1/5 → 1/5. Final cycle 9 `fec4668f…` is P/F/F/F/F = 1/5
under orchestrator-owned classification. Its P7 target passed 5/5, but Gate-5
active-status and P5-timing misses remain. The proposal is rejected, unapplied,
and not GREEN; the final cap is exhausted and there is no cycle 10 or further
model run.
The prior `366b3dad…` parent remains only historical comparison evidence.
The historical v3 parent acceptance denominator was `DD-01`–`DD-03`: three
scenarios, five Sol-high repetitions each, or 15 slots. Current Task 18A closure
uses `DD-01`–`DD-09`, or 45 slots. Parent scoring covers mode,
gate/principle timing and order, parent-owned artifacts, outcomes, and destinations,
fail-closed transitions, and parent/orchestrator owners.

Child invocation, loading, procedure execution, and output quality are not parent
score criteria. Research source selection, factual correctness, grounding,
disclosure, and support mapping are also outside the parent score and belong to
separately attributed child-composition coverage. `DISC-01`–`DISC-12` own skill
discovery and are not part of the parent behavioral denominator.

| ID | Prompt SHA-256 | Withheld rubric SHA-256 | Parent-focused evaluator bundle |
|---|---|---|---|
| `DD-01` | `b41c2835573b645e101280c2928c97f5363f519d73c769568924c3ded8f658ce` | `3599c856d7e0cf12006b1f548a854f9038badf71c56986046e9eda1baf62e21d` | Historical strict-epoch rubric; tracked parent only; frozen cycle-1-through-cycle-6 artifacts retain earlier rubric `e2076d7c…` |
| `DD-02` | `95deb13830eea682f06086c406dedb1a537b22f1bbf60598c4e1c231256ee706` | `69f985c4e99967378962d07f0c31f16f96413af1f9a7aae42d68daeb8d718cef` | Historical pre-behavior-first-repair rubric; tracked parent plus `project/dd-02/CLAUDE.md`, plan, linked spec, `cli-schema.md`, `library-api.md`, `vendor-schema-status.md`, and `git-history.md` |
| `DD-03` | `e329586445f56ca213fc20557109c874b650219daf3860f079ce909b534c7f07` | `8daf6068c6546a1de19a77172513c7c6c74456df09193ed1b0722c46720e7cd4` | Tracked parent plus `accepted-object-contract.md` and `parser-capabilities.md` |

The DD-01 prompt did not change. The strict-epoch rubric repair adds parent-required P7
to rows D/H, states conditional P5's row-D pre-edit timing, and distinguishes an
unresolved design choice from an unclear/conflicting-governance P3 trigger. It was
made only after final cycle-6 classification and cannot carry or alter any prior
result.

The completed original-versus-current comparison used the pre-repair `DD-01` and
`DD-02` rubric SHA-256 values
`40b28364f269df61f5738272e8dd71c7852ff48c8aebf9992cd1fadce9c3a18f`
and `576015f866da6f681ae46424ce5e78e63186f0f6e76330c41d1c554ebbaa09f5`.
Those hashes and results remain historical provenance; no comparison result is
carried forward to either repaired strict-epoch rubric.

| Strict-epoch project member | SHA-256 |
|---|---|
| `project/dd-02/CLAUDE.md` | `cc1f87826147c2799de88f208edbb798b24d6beb955bbadd5295e04fa1514d69` |
| `project/dd-02/plans/export.md` | `fd6dec456856f4aeb78cd4926a40ddf26c2f86da836e9559e91bff8f4b5d7daa` |
| `project/dd-02/plans/specs/export.md` | `77a8ad0cfa3ea65b02047968f412712d2b7723e4b943277ffdecfa3fd7ba735e` |
| `project/dd-02/sources/cli-schema.md` | `d31a0cf950c631454c0c3bb4e3a732e7e360776f7157cd81aa0921f8be3f42fd` |
| `project/dd-02/sources/library-api.md` | `253fb27d2587dd1ae1da9c6ff96c27a3c6c5c622301c661dc2e2a82a4452e1a4` |
| `project/dd-02/sources/vendor-schema-status.md` | `e696074e7b3c344a9e61601013af88036620ad981744cebc8acecca3964dffe5` |
| `project/dd-02/sources/git-history.md` | `a870dab35c878752f1b8c38538c08769df1ec21a2575fea0e723e484b7fd42bf` |
| `project/dd-03/sources/accepted-object-contract.md` | `a7dd65af335e4d25626a543e42d61e78761155906b3cc42ef2c362cf81d8bdb5` |
| `project/dd-03/sources/parser-capabilities.md` | `717b21cb61d87637ca241791407d9c57594e29c122cd0ef6c35e3476b5c1bee1` |

`project/dd-02/sources/operator-note.md` is explicitly excluded from the active
`DD-02` bundle. It remains only as a historical fixture file. Rubrics stay frozen
separately and withheld from evaluators. Fresh v3 control RED is accepted; no
strict-epoch candidate GREEN was established, and the final cap is exhausted.
No earlier candidate result is carried forward across these semantic prompt,
rubric, and bundle changes.

The accepted repaired-rubric control uses original commit `4296647f…`, parent
SHA-256 `1151a757…`, with active prompt/rubric bytes. `DD-01` is original-parent
only, canonical manifest `4ad78825129978fe479961d5d2499fa47f677d8af62b21f6b8b98b6983d9a63b`.
`DD-02` is original parent plus the exact seven project members above, canonical
manifest `922ebd5e37c06f1af92dc251e87ebc8d631d7b1afd311407345432e07dfd1700`.
It completed five Sol-high and five Sol-low repetitions per scenario: 20 evaluators,
then four contextful Sol-high scorer processes producing 20 verdicts. Every process
selected `a1`, with zero retries/errors. Both `DD-01` and `DD-02` scored 0/5 high
and 0/5 low under descriptive scoring and orchestrator whole-artifact adjudication.
The high cells are accepted watched REDs; low is robustness only. Evaluator freeze /
plan / verification are `4e8be5b3…` / `625ff413…` / `79c266ed…`; score freeze /
plan / aggregate are `b8e7c0d3…` / `0d25e502…` / `83a34d7a…`. A test-first
post-scoring verifier repair (`aafb6220…`; tests `57507b4b…`) made repeated aggregate
authentication pass without changing any run artifact or aggregate. `DD-03` retains
its unchanged original 5/5 preservation control. No candidate result predating this
control acceptance carries forward.

The focused comparison used evaluator root
`/private/tmp/dd-task18a-parent-ledger-flow-opaque-v1` with freeze / plan /
verification `159943f3…` / `d13c8bb3…` / `a3c004c1…`, and scorer root
`/private/tmp/dd-task18a-parent-ledger-flow-opaque-scoring-v1` with freeze / plan /
aggregate `96a3e20a…` / `5e2fd020…` / `8a4e0922…`. All 20 evaluators and four
contextful scorers completed at `a1` with zero retries/errors. The mapping stayed
sealed through aggregate authentication and manual review of every artifact; it
then revealed ASCII flow `eb4b13ba…` as arm A and lean ledger `5bec5d07…` as arm B.
Both arms were 0/5 on each scenario by descriptive scoring and orchestrator
whole-artifact adjudication. No result carries forward as candidate GREEN.

The lean-v2 focused evaluator root
`/private/tmp/task-18A-parent-lean-v2-focused-evaluator-06280f03-v1` has freeze /
plan / verification `2ebbbf37…` / `5311b471…` / `4bac0f73…`; its scorer root
`/private/tmp/task-18A-parent-lean-v2-focused-scorer-06280f03-v1` has freeze /
plan / aggregate `98b7ddff…` / `f91632a9…` / `267131a0…`. All ten evaluators
and both scorers completed at `a1` with zero retries/errors. Whole-artifact results
are `DD-01` F/F/F/F/F and `DD-02` F/P/F/F/F. Later fail-fast cycles repaired
its Gate-2 timing and most global-principle misses. The historical six-cycle
sequence ended at F/F/F/P/F = 1/5; both cycle-6 targeted fixes passed 5/5, with
remaining D P5, A/D P3, and H P7 misses. The prompt and bundle remain unchanged.
After adjudication, the then-active strict rubric alone was repaired test-first to `3599c856…`;
historical frozen results remain bound to `e2076d7c…` and are not reclassified.
Under that strict-epoch rubric, cycles 7–9 scored 0/5, 1/5, and 1/5. Cycle 9 made H P7
5/5 but retained two P1 classes: Gate-5 active-status downgrades and late P5
selection. No prompt/rubric defect was found. No cycle 10 or further proposal/model
cycle is authorized.

`DSD-01`, `DSD-02`, `OWN`, and `WER-07` remain 20 separately attributed
child-composition slots under their existing owners. They are never pooled with the
15 parent slots.

## Historical control bundles

Repository files come from control commit `4296647f0dff48a9e77b979ef07e813bf1f66db2`.
Bundle digests use the canonical path-and-content algorithm in [the shared protocol](../../README.md#immutable-control-bundles).

| Bundle | Scenarios | Contents | Repository archive SHA-256 | Content-manifest SHA-256 |
|---|---|---|---|---|
| Complete integrated control | `DD-01`, `DD-02` | All nine repository `SKILL.md` files listed in the shared control manifest plus the Superpowers 6.2.0 methodology dependencies below | `8f21c8267d005c349702ec94d6aff26c13a09bfbe29f2b43efcfbb37304f16e3` for repository members | `ffeeb68d8fae44b81d4c1b57a7a92f6e5ed82fd6cc58e429cfcf4c826c8c8475` |
| Parent-only control | `DD-03` | `skills/disciplined-development/SKILL.md` | `622771912909a7fb22fd7576d17ad2cbfd2014cabdcd55324309b0a4952dd2da` | `49191f92b1cf5b2f3cfa51bc7066716c15b7671c960ded6bb1b1c7dfd8a38a76` |

The control parent skill SHA-256 is `1151a7575a5b6f72e007229c97efdb7a829695d08e8f44450d0d71b232e75dec`.

The complete integrated control adds these immutable Superpowers 6.2.0 dependencies under `skills/superpowers/<name>/SKILL.md`:

| Dependency | SHA-256 |
|---|---|
| `brainstorming` | `4a54a4858b99807f3155ed1614b2f116e35ea5c1b788e793f565dd837fd3891f` |
| `dispatching-parallel-agents` | `1968923066f3b707eb01d1992cdf4c42284c3855f70253b9cd5000ff45fca13c` |
| `executing-plans` | `c4c3d8b628c51114cd165fb8246fe02744cd8be180032328391252e653028d9b` |
| `finishing-a-development-branch` | `d0ac8360ed9d59121776ef95c84bcb38e9747de0d7ae7e227dca81e437593b9b` |
| `receiving-code-review` | `091df1629510af1b92fc4abd6f96732ebedb4cb2c0f3457e8f2740b0504a2438` |
| `requesting-code-review` | `d71cc01ba56d2325cf8af5f7c11837819b63ecd57de0bfdb812f7f3ff7751df8` |
| `subagent-driven-development` | `349a08ad8b59b19b86c13a7d2f34a1a38719bf88257004a863eefefa8d9f9e40` |
| `systematic-debugging` | `808fc5717aa88ad65efff312b11c186294d3e6ee301afb584e2f86599b137787` |
| `test-driven-development` | `bf1b8216e523851a411e91d429a7c1c2a173e79d88957bc78e348218d50edd54` |
| `verification-before-completion` | `2befe7fc55bcadaa3d97dd9e8efeb633d2561c0ebe74c5a8b17c4d9e7e4520b3` |
| `writing-plans` | `72190c88b2b5a67a96b91d66aa72b9161913e10e8769da3f28a226f4cc7b99d0` |

## Historical Task 10 inherited coverage

These scenarios retained their then-current owners and were linked into the
historical Task 10 parent closure rather than duplicated here. The historical v3
topology used separate, non-pooled discovery and composition coverage; current
Task 18A topology is recorded in the owning validation documents.

| Scenario | Owner | Task 10 obligation |
|---|---|---|
| [`DISC-01`–`DISC-10`](../../skill-discovery.md#active-catalog-definitions) | Task 1 shared discovery suite | Description routing and parent-plus-applicable-companion availability |
| [`DSD-01`, `DSD-02`](../../dispatching-development-subagents.md#active-catalog-definitions) | `dispatching-development-subagents` | Principle 4 plus subagent versus orchestrator gate ownership |
| [`OWN`](../../adversarial-review-loop-scenarios.md#active-catalog) | `adversarial-review-loop` | Per-task versus whole-branch review-loop ownership and independent counters |
| [`WER-07`](../../writing-explicit-rationale.md#historical-wer-07--parent-and-plan-composition) | `writing-explicit-rationale` | Principle 1 delegation of rationale necessity without forcing a why for every choice |

## Historical prompt and rubric hashes

| ID | Prompt SHA-256 | Rubric SHA-256 |
|---|---|---|
| `DD-01` | `ba51dcfa160daffdb681c3bef0b993dc36ba1091c6e789826948331ebcc39d13` | `bbd1849b0b941c63282006e019f4cc5f24ad00e85897964c3f231d6ac4c97485` |
| `DD-02` | `5da5fe92259e8a7343ebc394eba326e06fa31c65eea3ee829de0157eeac8d528` | `ab8ab55f1e58fb9c2eaa68b695e426ca6c8f85c3ec8154a64b30804aaee958f3` |
| `DD-03` | `852eb66f0c3084e4f9aff349ae3775b5c70ca5c3221d1b6538d62ca603830b80` | `ead264e837afb0fe2aa974d0a9280e3c36e23d5079968f67da21bac6902c1c06` |

## Task 18A pre-draft freeze

The table above is historical under its prior contracts.
The repaired prompts and rubrics below require universal research selection and
unambiguous source disclosure for the complete factual output.
`DD-01` and `DD-02` use the pre-Task-18A complete integrated bundle at base
`bd30bf7c9070f2f56b6d2ae32a746518e2259b6f`, canonical content-manifest SHA-256
`45fc15dc3be737a3b52e7f1dd22fa6177fb8e00b80930d0e03ef53ecad2da5b9`
after adding the eight immutable `project/dd-02/` primary sources.
`DD-03` now supplies the parent and research skills from that base, canonical
content-manifest SHA-256
`41b9afaa58860d9d932d938ec8cbbaaa4c86da489de472364531acf2f9da169c`
after adding the two immutable `project/dd-03/sources/` files.

| ID | Prompt SHA-256 | Rubric SHA-256 | Sol-high control | Sol-low control |
|---|---|---|---|---|
| `DD-01` | `0e2e3babbffd53b7ba5c4d55447322c9697fb99ada29d1c26c28d8cb424cb685` | `cdd12bb4d8cd9d072e0d8fbfbf1461dfd4621503305357cac809d58bab2def8c` | **0/5 target RED: F/F/F/F/F** | **0/5 robustness: F/F/F/F/F** |
| `DD-02` | `5136c1a72743b366c0d9f8da6b41defb3db1034c9e1263c77cd590c84a0794cc` | `1d24397de093e69c5e50eb81879d3dc0261c709c5db6607ddfe158f0ecb324ca` | **1/5 target RED: F/F/P/F/F** | **1/5 robustness: F/P/F/F/F** |
| `DD-03` | `835545bde4c74bbfc30b83dfebe5e5ffc6a848fae62e4bfecc1d55770fa963b3` | `225bd920689a72bbd52a4e800e2029097d270d244b591e70404e4db7305699bb` | **0/5 target RED: F/F/F/F/F** | **0/5 robustness: F/F/F/F/F** |

All three are target REDs because universal acquisition, verification, and mapped
disclosure add positive promises. High is the acceptance configuration; low is
recorded robustness, not a separate gate. The completed post-freeze root is
`/private/tmp/dd-task18a-control-postfreeze-f59608a` (freeze
`0119bdb403fdb89978ed6c2f34bae8de5db13c392071b97b06687d81f9be0210`, plan
`4de14a3e7531c8cf0e6258f82c9c8050b849ca9d0f0f8c1c633248dafcd81b4b`).
Final application verdicts use the contextful scorer root
`/private/tmp/dd-task18a-control-scoring-contextful-f59608a` (freeze
`a72902e254706d2a13c9ff573bcffff6469271fdaf914f1b9e55db6a36fa0675`, plan
`cfb8e3f7949afc2b35407abd203fdd02767fdc1f698081f2fa952156f2f801bb`)
and aggregate
`c801090c6252298da41954663dd3f671164cd77fceaa77abf71583fa43fa2f60`.
The context-stripped aggregate `289ef0fd…` is historical transport-defective
evidence only.

| Primary fixture member | SHA-256 |
|---|---|
| `project/dd-02/CLAUDE.md` | `cc1f87826147c2799de88f208edbb798b24d6beb955bbadd5295e04fa1514d69` |
| `project/dd-02/plans/export.md` | `fd6dec456856f4aeb78cd4926a40ddf26c2f86da836e9559e91bff8f4b5d7daa` |
| `project/dd-02/plans/specs/export.md` | `77a8ad0cfa3ea65b02047968f412712d2b7723e4b943277ffdecfa3fd7ba735e` |
| `project/dd-02/sources/cli-schema.md` | `d31a0cf950c631454c0c3bb4e3a732e7e360776f7157cd81aa0921f8be3f42fd` |
| `project/dd-02/sources/library-api.md` | `253fb27d2587dd1ae1da9c6ff96c27a3c6c5c622301c661dc2e2a82a4452e1a4` |
| `project/dd-02/sources/operator-note.md` | `b0c904bcee4b4183621cb0f59cf0436e967a16ef65e5a3ab77eb5f300e2faf5a` |
| `project/dd-02/sources/vendor-schema-status.md` | `e696074e7b3c344a9e61601013af88036620ad981744cebc8acecca3964dffe5` |
| `project/dd-02/sources/git-history.md` | `a870dab35c878752f1b8c38538c08769df1ec21a2575fea0e723e484b7fd42bf` |
| `project/dd-03/sources/accepted-object-contract.md` | `a7dd65af335e4d25626a543e42d61e78761155906b3cc42ef2c362cf81d8bdb5` |
| `project/dd-03/sources/parser-capabilities.md` | `717b21cb61d87637ca241791407d9c57594e29c122cd0ef6c35e3476b5c1bee1` |

## Replay

Use the exact enforced `codex` transport in the shared protocol with one fresh process and output path per repetition, `gpt-5.6-sol`, high reasoning effort, and at most three concurrent evaluators.
Verify the mapped bundle digest, keep the bundle read-only, and pass the matching prompt bytes on standard input.
The orchestrator manually scores the last-message bytes against the separate rubric; raw evaluator transcripts remain outside the repository.
