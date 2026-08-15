# Writing explicit rationale — validation

## Task 21 immediate readability control and fresh audit (2026-08-14)

Task 21 starts from clean commit
`c54c4016c867444ae0d31783a69905b774ecc106`, with local HEAD, the tracking ref,
and the remote branch synchronized.
The immediate readability control is 372 words at skill SHA-256
`568b2a61bef3f7694014fb89228f933261837acd4f2b5978b2b8ef55aa108c9f`.
The current policy scope is approved and remains unchanged.

| Skill section | Necessary behavior | Simplification disposition |
|---|---|---|
| Frontmatter description | Route durable-reasoning needs, descopes, deferrals, exceptions, defensible alternatives, repeated re-litigation, and rationale stranded in chat, commits, or PRs while leaving routine consequence-free choices out of scope | Keep byte-for-byte; it states the trigger once and shared `DISC-08`–`DISC-10` already protect its positive and negative boundaries |
| Role | Assign necessity, content, durable placement, and reference-not-repeat while excluding plan density, commit-message composition, and stale-reference sweeping | Tighten the abstract “when and where / how much” wording into those observable ownership seams |
| What rationale means here | Always retain the decision, operation, and material consequences or limits; include why and history only when they affect correctness or future decisions; a defensible alternative alone is not enough | Rename around the decision the reader must make and separate the non-trigger from the why/history threshold without changing either predicate |
| Keep one authoritative home | Treat repeated re-litigation as an audit signal; inspect related sites once; reuse current rationale or create missing rationale at the nearest durable decision site; reference it elsewhere; reject chat, commits, and PRs as stores | Preserve the complete four-step method and placement boundary; remove only local connective words |
| Resist duplicate rationale | Counter commit/PR pressure, apparent convenience of repetition, and speculative background | Keep all three rows because `WER-05`, `WER-06`, and the preserved reviewer-visibility evidence exercise distinct pressure classes; shorten only the heading |
| Whole skill | Preserve the broad-domain rationale policy and its composition with the parent, research, and plan-writing contracts | A small but meaningful behavior-preserving cleanup is warranted: clarify the ownership and necessity headings, put why and history under one threshold, and remove 15 words without changing the trigger, policy scope, workflow, placement, or pressure defenses |

The smallest complete scratch proposal is 357 words at SHA-256
`1bc78cb7dc8b034d052f7fc40942d730a5bcf518eeb6624637ee2ed358295683`.
The owner approved it, and the tracked skill matched those bytes through the initial
evaluation and cold review. The later behavioral-repair trial is recorded below.

### Task 21 initial candidate and blind comparison

The frozen control/candidate root is `/private/tmp/task21-wer-cleanup-v1`.
Its freeze SHA-256 is
`aef098ea0cf57d08edef219880893c85343666b6a1178d99409240024c103591`.
All 60 control/candidate evaluator slots completed on attempt 1 with zero
infrastructure errors under fresh `gpt-5.6-sol` high-effort, read-only/no-agents
transport and maximum concurrency three.
The control and candidate verification aggregates are respectively
`7cbfa2f9f5a583cc7eae3121a123d3ee677441703c69aa464be335247d833eaa`
and `9e42f0982461de2a96ddba331f4cdec7c46f8f28efbd4d38bf6c9470aaadfb55`;
their verification-file SHA-256 values are `90f0aea4…` and `de3f44fe…`.
Initial manual scoring reported `WER-01`–`WER-03` and `WER-05`–`WER-07` at
**30/30**. That result is superseded by the staged-review correction below.

The blinded comparison at `/private/tmp/task21-wer-blind-v1` sealed all six
scenario score records before revealing the arm mapping.
Its sealed-score, revealed-key, and decoded-summary SHA-256 values are
`c942f4b401a8cd6ad215d7e25ab215d3092ae9858a93bb4fdc0b5f16e3f6bbf6`,
`9e2640b39369ab263c838e663e30d463dada62d2ea738836083a34c547b31268`,
and `7c5754570974bb06c63ebd0c239b63e648fc09e4a503fe5d3f46179e37fec4eb`.
Raw scorer labels reported five candidate losses, seven control losses, three
both-loss cells, and 21 neither-loss cells.
The initial whole-artifact adjudication overruled all five candidate flags: one demanded the
word “accepted” despite an explicit selected boundary and bounded consequence;
three imposed an exact grammatical subject or inferred reviewer on the preserved
monthly-review policy; and one mistook the local statement that duplication is
intentional for a copy of the authoritative causal explanation and revisit rule.
It concluded, incorrectly, that none changed an action, required fact, rationale
home, or future decision.
Three control losses remain material: one adds rationale at the consequence-free
telemetry site, and two commit summaries obscure that the change adds a guard.
It therefore recorded zero candidate material losses across 30 pairs, with 27
equivalent pairs and the only three losses in the control.

That adjudication is superseded. The three `WER-03` flags identify material action,
ownership, and policy-scope defects: candidate repetitions 1–2 change monthly review
from the exception to individual grants and invent Finance Committee ownership;
repetition 3 also narrows the $30,000 contingency exposure to over-cap grants.
Only repetitions 4–5 preserve the supplied policy, so the initial candidate's
authoritative active result is **27/30**, with three candidate material losses in
the 30-pair comparison. The separate `WER-02` “accepted” flag and `WER-05`
duplication flag remain non-material wording/meaning errors by their scorers.

### Task 21 cold skill-writing and editorial review

A fresh read-only/no-agents `gpt-5.6-sol` high-effort reviewer read the complete
governing plan, design record, skill-writing guidance, validation record, immutable
control, exact candidate, and complete diff. It returned `SPEC: PASS`,
`QUALITY: PASS`, and no findings. The output SHA-256 is
`01c8d43ee96f44abc77679f8f42f92a517780036441f3f2d9e325db5367e0fd8`.
It proposed no skill fix, so no post-evaluation wording change or scenario restart
was triggered.

### Task 21 staged-review block and repaired behavior oracle

The first exact-stage adversarial review returned two findings and
`DD-VERDICT: BLOCK`; its output SHA-256 is
`a504919b4f0c7cd646bc256a78119212a27c199935f5304c88e43523c7425c8d`.
Its P1 finding produced the corrected `WER-03` result above. Its P2 finding identified
stale protected-section names in the active map; those now use the current
`What rationale means here` heading. The failed review is retained as evidence and its
stage is superseded, not treated as a pass.

The owner approved a separate behavioral RED/GREEN slice. The `WER-03` prompt stays
byte-for-byte unchanged because it already exposes the failure. Its withheld rubric
now makes the existing behavioral standard executable: preserve that the exception
itself is reviewed monthly, leave review ownership unspecified, and keep the
$30,000 contingency exposure scoped to the exception as a whole. The original five
candidate outputs are the retrospective RED at **2/5** under that refined oracle.

The fresh refined-oracle rescore independently confirmed failures in repetitions
1–3 and passes in repetitions 4–5; its output SHA-256 is
`8e5cad73d0f6c51cfce2fc5e2c510e74afb3802f033fb7caaa8b8214dc88b1b4`.

The owner-approved first repair trial added a supplied-decision qualifier and the
rule “Do not infer or shift action scope, action ownership, or consequence
boundaries.” The resulting 369-word trial skill is SHA-256
`f992d074750feaf1f39bb358307e514555cddd68d11621c78699c60f63ffbf50`.
The focused two-arm `WER-03` root is
`/private/tmp/task21-wer03-repair-v1`; its freeze SHA-256 is
`5d40c74a8a930d11b2bfd3651e1bdff9cdd7d4a2e5491c2331de9f12cd0275d5`.
All ten slots completed on attempt 1. The control and trial verification aggregates
are `47780551…` and `e5d2372b…`; their verification-file SHA-256 values are
`dd95b036…` and `50230f71…`.

The trial did **not** reach GREEN. Manual scoring and an independent refined-oracle
rescore both pass only repetitions 1–2: repetition 3 still attaches monthly review
to grants, repetition 4 invents Finance Committee review ownership, and repetition
5 again attaches monthly review to grants. The independent score output SHA-256 is
`4b5bbdb704d6ae1e5535083c07d8250204c868d67d2b047c77722340195445d9`.
The unchanged control passed only 1/5 in the focused run, so the trial improved the
rate but remained behaviorally unsound. No affected-suite restart or replacement
blind comparison has begun.

Before a second wording trial, the focused historical `WER-DEV` software-development
probe was frozen with
the same semantic trap in an emergency-production-change policy. Its prompt asks for
one-approval database-failover changes while preserving that the exception—not each
deployment—is reviewed after each deployment and without inventing a review owner.
Against the 369-word first trial, it passed **4/5**: one output instead required each
deployment itself to be reviewed. The RED freeze and verification-file SHA-256 values
are `913242b035f24ba83b536dd82bb4009d09f34821e6e02c27c6adad37034d3243`
and `37562e7bbe28e671691e88b981430bdaee82f9c8ff6e3266f859a161c7adcf53`.
Its exact [prompt](fixtures/writing-explicit-rationale/prompts/wer-dev.md) and
[rubric](fixtures/writing-explicit-rationale/rubrics/wer-dev.md) are retained for
replay. This probe is generic artifact-rewriting evidence and does not join the
active catalog.

The owner-approved second trial replaced the abstract prohibition with “Keep each
supplied action and consequence with its stated subject; leave unspecified owners
unspecified.” The resulting 371-word skill is SHA-256
`b14c185c355fb2801a40cfe1821f7a0c4b900e92d06e9887b7579479e4f53b0d`.
Its two-scenario focused run completed all ten slots on attempt 1, but it also failed:
`WER-03` passed **3/5** and the software-development probe passed **2/5**. The
GREEN-attempt freeze and verification-file SHA-256 values are
`aead4f8c5802c52524ac35a10e398915e3a157c1dbe3e3653e58dfe13758fa6a`
and `8c02c61eaeba9b2a0e7e3b4c3141e2b7c741a20b80f74e0dbbe7dc2ac4a053c2`.
Because two generative wording rules failed to make fact attachment reliable, the
repair loop stopped before a third wording attempt or any broad rerun. The tracked
skill was then restored byte-for-byte to the owner-approved 357-word
`1bc78cb7…` cleanup; neither failed repair wording remains in the current skill.

### Task 21 behavior-first test-contract repair (2026-08-15)

The owner approved a validation-only repair after a fresh sealed comparison showed
the committed immediate control at 1/5 (`P/F/F/F/F`) and the restored cleanup at
2/5 (`F/P/F/F/P`) on `WER-DEV`.
Both arms primarily failed while rewriting supplied policy facts, so that probe is
retained as generic artifact-fidelity evidence rather than a
`writing-explicit-rationale` acceptance gate.
The former `WER-03` amendment-rewriting contract is likewise retained as historical
diagnostic evidence and replaced in the active suite by `WER-08`, which isolates
rationale necessity, content, durable placement, and reference-not-repeat without
requiring a wholesale policy rewrite.

Score every active response in two ledgers:

- **Owned behavior:** PASS or FAIL for rationale necessity, material content,
  durable placement, authoritative reuse, relevant-history filtering, and the
  decision, operation, or consequence accuracy needed to make that rationale true.
- **Task-fidelity note:** record requested formatting, exact wording, or generic
  transformation defects that are not owned by this skill; these do not change the
  skill verdict.

An owned failure requires an observable difference: a careful reader would take a
different action, omit necessary work, act at the wrong site, assign the wrong
owner, cross a different material boundary, create a competing rationale home, or
rely on invented decision-relevant content.
Semantic equivalents pass when the complete artifact supports the same action.
No word, grammatical form, label, sentence order, or rendering is required unless
that literal or placement is itself necessary to the owned behavior.
If recurring generic task fidelity makes owned behavior impossible to determine,
mark the scenario contract non-diagnostic rather than attributing the failure to
the skill; repair or replace it and restart under the shared invalidation rules
instead of weakening the behavior standard.

### Task 21 behavior-first validation result

The revised contracts passed a fresh read-only/no-agents Sol-high design review with
`SPEC: PASS`, `QUALITY: PASS`, and no P0–P3 findings; its output SHA-256 is
`5c87b4551d45c014bcf4b5d649ff7daee57e586f85a80ae7dfcf58fc61479165`.
The high control/candidate root is
`/private/tmp/task21-wer-behavior-high-v2`, with freeze SHA-256
`298d7dc9e11f8cf6e3850420eeba11b3cb4ed9fcbb6e8687c7e6fc82db901474`.
All 60 high-effort slots completed on attempt 1 with zero infrastructure errors.
The control and candidate verification aggregates are
`4a82b79233cfd9c6dd9d8f43ecbc0558e408eb7c1a9892c2cfe2c30220eac9e5`
and `01f0a0ddaba6a8dd0b740a8e0d7cf3f4684a5539b6da09ef2e1b8f6160afca47`;
their verification-file SHA-256 values are `c9d59a47…` and `700daecf…`.

The blind root is `/private/tmp/task21-wer-behavior-blind-v1`.
Its freeze, scorer-package manifest, sealed-key, sealed-score manifest, decoded
summary, and manual-adjudication SHA-256 values are respectively
`dc4c2829…`, `9926a8af…`, `b3df9af6…`, `e25b8483…`, `26eeb8d7…`, and
`0cc0d3c4…`.
Fresh scorers judged opaque, independently randomized options per repetition and
recorded owned, task-fidelity, and composition ledgers before arm reveal.
The initial manual behavior-first adjudication overruled eight scorer flags and
reported the committed immediate control at 30/30. Final restoration review found
that one override was wrong: control `WER-07` repetition 2 says the libraries have
equivalent downstream consequences, but it does not preserve the supplied fact
that they create no downstream consequence. Equal nonzero consequences remain
possible, so a maintainer could infer downstream work that does not exist.
The correction at
`/private/tmp/task21-wer-behavior-blind-v1/manual-adjudication-correction.json`
has SHA-256 `8f4f48c0…` and restores the sealed scorer's FAIL for that cell.
The authoritative committed-control result is therefore **29/30**, with `WER-07`
at 4/5 (`P/F/P/P/P`); its composition-owner ledger remains 5/5.
The restored 357-word candidate is **29/30**: `WER-01`, `WER-05`–`WER-08` are
5/5, while `WER-02` is 4/5 (`P/P/P/F/P`).
In `WER-02` repetition 4, the candidate tells future maintainers to add another
duplicated interactive guard and centralize only if every `persist()` caller becomes
subject, replacing the supplied third-interactive-caller revisit boundary with a
materially different action.
That is an owned behavioral failure, not a wording or rendering failure.

The low-effort control root is
`/private/tmp/task21-wer-behavior-low-control-v2`, with freeze SHA-256
`4f8c01d3daeb4ad3bcf00e0f5d420eb27ad7bbade938d170b9bea11a92f757b1`.
All 30 slots completed on attempt 1 with zero infrastructure errors; verification
aggregate is `58ca2844…` and verification-file SHA-256 is `67acdb5d…`.
Fresh score files have aggregate SHA-256 `43614eb5…`; manual adjudication is
`dc363476…`.
The low control is **29/30**: `WER-07` repetition 4 invents invalidating valid
in-flight requests as the rejected quota alternative, a genuine rationale-content
and research/composition miss. Sol low is robustness evidence only; its distinct
miss does not change the high-control result.

`WER-08` passed **5/5** in high control, high candidate, and low control.
It therefore supplies clean broad-domain evidence without amendment-rewriting
contamination. `WER-03` and `WER-DEV` remain historical diagnostics only.
The restored candidate does not satisfy the 5/5 active gate because of the retained
`WER-02` miss. This result does not authorize a third skill wording edit.

### Task 21 WER-02 attribution-only expansion

The owner approved a diagnostic expansion without changing either skill arm or
replacing the authoritative 29/30 acceptance result.
The exact prior WER-02 prompt, behavior rubric, control context, and candidate
context hashes were frozen for ten new Sol-high repetitions per arm at
`/private/tmp/task21-wer02-attribution-v1`.
Its freeze SHA-256 is
`da244375304c66fd3945435a28186a4229b4f8af748c83a52ed7c465c23d4f1b`.
All 20 outputs completed on attempt 1 with zero infrastructure errors.
Control and candidate verification aggregates are `213bedb4…` and `b99c5818…`;
their verification-file SHA-256 values are `70abe682…` and `17848d09…`.

The ten-pair blind root is
`/private/tmp/task21-wer02-attribution-blind-v1`.
Its freeze, sealed-score, sealed-key, and decoded manual-adjudication SHA-256 values
are `a5d1fac4…`, `85bf4efd…`, `f5442ad0…`, and `a2725f98…`.
The blinded scorer marked one owned failure; reveal mapped it to candidate
repetition 2. That response says every future interactive caller must enforce
another local guard but omits that duplication is accepted only until a third
interactive caller, when a shared interactive guard should be extracted.
Manual whole-artifact inspection retained the failure because it changes the action
a future maintainer would take.

The attribution-only result is control **10/10** and candidate **9/10**.
Combined with the original frozen WER-02 cells, control is **15/15** and candidate
is **13/15**. Both candidate failures change or omit the third-interactive-caller
revisit boundary; no control output does.
This is evidence that the restored candidate is less reliable on this owned
behavior, but it does not identify which wording difference is causal and does not
authorize a third wording trial. The original candidate gate remains 29/30.

### Task 21 disposition and exact control restoration

The owner accepted the recommendation to reject the cleanup candidate rather than
authorize a third wording experiment. The tracked skill is restored byte-for-byte
to the 372-word immediate control at SHA-256
`568b2a61bef3f7694014fb89228f933261837acd4f2b5978b2b8ef55aa108c9f`.
It has zero diff from
`c54c4016c867444ae0d31783a69905b774ecc106:skills/writing-explicit-rationale/SKILL.md`.
The failed 357-word candidate remains preserved in the frozen evaluation records at
SHA-256 `1bc78cb7dc8b034d052f7fc40942d730a5bcf518eeb6624637ee2ed358295683`;
neither it nor either failed repair trial is the current skill.

No duplicate generative arm is required merely to establish the restoration's
identity because the current file is the exact immutable control context already
exercised in the fresh behavior-first run. That exact arm scored **29/30**, with
`WER-08` at 5/5, and the attribution-only
WER-02 expansion scored **10/10**, or **15/15** across both frozen WER-02 runs.
The Sol-low control remains **29/30** as robustness evidence only. Exact byte
identity, rather than a claim of semantic equivalence, connects those frozen results
to the current in-place skill.

This disposition rejects the proposed readability candidate and keeps the
behavior-first test-contract improvements, but it does not close Task 21: the
restored current skill has a genuine active `WER-07` miss. A fresh cold editorial
review passed `SPEC: PASS` and `QUALITY: PASS` with no finding; its output SHA-256
is `01c8d43ee96f44abc77679f8f42f92a517780036441f3f2d9e325db5367e0fd8`.
The concurrent exact-stage adversarial review at SHA-256 `ca99e251…` found the
adjudication error plus stale section references and an incomplete Task 21 file
inventory, and returned `DD-VERDICT: BLOCK`. The latter two record defects are
repaired without changing the skill. A fresh follow-up review at SHA-256
`b2ae1066…` verified those dispositions but found that the historical WER-03 and
WER-DEV fixture files included archival headings or disposition prose absent from
the evaluated inputs. The fixtures now match the evaluated bytes exactly:
WER-03 rubric `c2c586c8…`, WER-DEV prompt `93f5fb44…`, and WER-DEV rubric
`5dc06e1a…`. Historical classification remains in this record rather than in
evaluator-visible inputs. The final fresh exact-stage follow-up returned no findings,
`DD-PATTERN: NONE`, and `DD-VERDICT: PASS`; its output SHA-256 is
`585149ab3d19fcc75d59cb1b9a45c7fab8301419285d2387d179c3cc50dcdc5e`.
Another skill wording change is not authorized. A user-approved disposition or
separate repair slice, followed by the applicable behavioral validation, is required
before final in-place approval, repository verification, closure bookkeeping,
commit, or push.

### Task 21 WER-07 no-edit causal diagnostic

The owner approved a no-edit diagnostic before any further skill proposal. Ten
fresh exact-current WER-07 Sol-high repetitions ran at
`/private/tmp/task21-wer07-causal-v1` with the unchanged 372-word control, prompt,
rubric, and composition context. The skill, prompt, rubric, and context-manifest
SHA-256 values are `568b2a61…`, `b4fbdd83…`, `2fc48c5a…`, and `b24af6b4…`.
The freeze SHA-256 is `456736a6…`. All ten outputs completed on attempt 1 with
zero infrastructure errors; the verification aggregate and verification-file
SHA-256 values are `d01c6a9b…` and `33ec55f7…`.

Whole-artifact adjudication scores the diagnostic WER ledger **8/10**
(`P/P/P/P/F/P/P/P/F/P`) and its separate composition ledger **10/10**.
Repetition 5 says batch import accepts approved batches but does not preserve that
it calls `persist()` only with approved batches, leaving the material boundary open.
Repetition 9 selects Library A but attaches the no-downstream-consequence fact only
to Library B, leaving the selected library's consequence ambiguous. The manual
score file is SHA-256 `2808f587…`. Combined with the original five current-control
cells, exact-current WER-07 is **12/15** for diagnostic attribution; the active
acceptance result remains its original frozen 4/5 and is not replaced by added runs.

Five fresh independent Sol-high meta-reviewers then received the exact current
skill, task, rubric, historical failure, and ten diagnostic outputs at
`/private/tmp/task21-wer07-causal-meta-v1`. Its freeze and context-manifest SHA-256
values are `dfac0d33…` and `ab788a17…`; verification aggregate and file SHA-256
values are `bffcdf56…` and `4374f7c5…`. All five classified the cause as
`CLEAR_RULE_TASK_FIDELITY`, returned `skill_gap: null`, retained the historical and
repetition-9 failures, and reported no composition failure. Three also retained
repetition 5. None classified a documentation gap, organization gap, or
non-diagnostic scenario.

The failures remain owned WER verdict failures because they materially weaken or
reattach decision facts. Their cause is not an omitted skill rule: the current skill
already requires the facts establishing how a decision works and its material
consequences, limits, or lack of either. This repeated clear-rule noncompliance does
not justify a third wording trial. It exposes an architectural decision for the
validation protocol: whether a cleanup task may close with an unchanged skill when
fresh model execution violates an already-clear rule, or whether strict 5/5 remains
blocking regardless of causal ownership. No such protocol change is authorized;
Task 21 remains blocked.

The owner approved the no-change disposition. The Task 21 readability attempt is
rejected, the exact 372-word control remains the in-place skill, and no third wording
trial is authorized. The WER-07 misses remain genuine owned model-execution failures:
they are not relabeled as passes, excluded from the active catalog, or used to claim
that the current rule needs more wording. Because the task accepts no changed skill,
this disposition permits it to proceed to the separate final in-place approval gate.
It does not waive the protocol's strict 5/5 requirement or remove WER-07 from the
final repository-wide suite. Final owner approval, repository verification, closure
bookkeeping, commit, and push remain pending.

The owner subsequently approved the complete exact in-place 372-word skill at
SHA-256 `568b2a61bef3f7694014fb89228f933261837acd4f2b5978b2b8ef55aa108c9f`.
That approval accepts the restored control as the shipped Task 21 state; it does not
accept either rejected candidate, relabel any WER-07 failure, waive strict 5/5, or
remove WER-07 from final repository-wide closure. Fresh repository verification
passed: hook tests 373 passed / 3 skipped, installer tests 11 passed, research tests
4 passed, and the exact local-link command passed for 10 working and 10 staged
Markdown documents. Exact skill/control identity, historical fixture hashes, causal
and correction JSON consistency, the routing/reference sweep, and both working and
staged diff checks passed. Task 21 closes as a rejected no-change readability attempt
in `docs(validation): repair explicit rationale tests`; WER-07 remains strict active
evidence for final repository-wide closure.

## Active catalog audit (2026-08-03)

The shared all-nine discovery suite remains owned by
[skill-discovery.md](skill-discovery.md#active-catalog-definitions).
`DISC-08` protects the routine-rename negative, `DISC-09` protects intentional
shortcut routing, and `DISC-10` protects rationale that would otherwise remain only
in a PR description.
The body-level application path protected here is `DISC-10` →
`writing-explicit-rationale` → `WER-01`, `WER-02`, `WER-05`, `WER-06`, and
`WER-08`; `WER-07` protects composition with the parent and plan-writing skills.
`WER-03` and the software-development fidelity probe remain diagnostic history.

The historical scenarios were only partially recoverable under the common protocol:

| Historical evidence | Classification | Active disposition |
|---|---|---|
| Reviewer visibility: bare consumer | Merge | Missing-rationale placement is covered by `WER-02`, PR-only routing by `DISC-10`, and duplicate resistance by `WER-05` |
| Reviewer visibility: governing-file consumer | Retire | The governing-file distinction no longer matters after commit/PR rationale stops being part of the skill contract; replace it with existing-rationale reuse coverage in `WER-05` |
| Routing matrix: active-plan implementation with delegation | Merge | Merge into existing `DISC-04` and `DISC-06` |
| Routing matrix: padded README tightening | Merge | Merge into existing `DISC-03` |
| Routing matrix: SKILL.md shortening | Retire | The exclusion contract was superseded by the approved Task 2A authoring-boundary design |
| Routing matrix: plan deferral with PR-only rationale | Repair | Reconstruct as shared `DISC-10` |
| Routing matrix: routine convention-preserving rename | Merge | Merge into existing `DISC-08` |

No historical scenario was replayable unchanged: **Keep 0, Repair 1, Merge 4,
Retire 2**.
Existing `DISC-09` adds current shortcut-routing coverage but is not counted as a
successor to the historical five-cell matrix.
Simple direct invocation, repeated-review batch auditing, isolated broad-domain use,
existing-rationale reuse, and relevant-history filtering were missing, so the
2026-08-03 audit added `WER-01`, `WER-02`, `WER-03`, `WER-05`, `WER-06`, and
`WER-07`.
The behavior-first repair retires `WER-03` from active acceptance and adds its
`WER-08` successor, bringing cumulative classifications to **Retire 3** and
**Add 7** without changing the six-scenario active denominator.

The six active owned scenarios are the smallest suite that keeps direct plan editing,
retroactive batch repair, broad-domain application, existing-rationale reuse, and
relevance filtering independently observable while checking parent-and-plan
composition.
`WER-08` replaces the generic rewrite burden in `WER-03` with an isolated
rationale-placement decision; it adds no policy rule.
The section-by-section simplification questions are:

| Skill section | Would a simpler approach preserve the necessary intent and effectiveness? | Smallest evidence mapping |
|---|---|---|
| Frontmatter description | Yes; use shared routing cells rather than repeat metadata prompts here | `DISC-08`–`DISC-10` |
| Role | Yes; one sentence distinguishes rationale judgment and placement from sibling procedures | `WER-01`, `WER-08` |
| What rationale means here | Only partly; what/how, necessary why, consequence-free choices, and irrelevant history are distinct predicates but fit one paragraph | `WER-01`, `WER-02`, `WER-06`, `WER-08` |
| Keep one authoritative home | No; repeated-review auditing, creating missing rationale, and referencing current rationale are distinct steps in one workflow | `WER-01`, `WER-02`, `WER-05` |
| Resist duplicate rationale | Yes; three observed pressure classes fit one compact table | `WER-05`, `WER-06` |
| Whole skill | No smaller structure preserves the framing, placement workflow, and tested resistance to duplicate rationale | `DISC-08`–`DISC-10`, `WER-01`, `WER-02`, `WER-05`–`WER-08` |

## Active scenario catalog

Prior `WER-01`–`WER-07` run metadata: control commit
`4296647f0dff48a9e77b979ef07e813bf1f66db2`; Codex CLI 0.146.0;
`gpt-5.6-sol`; high reasoning effort; Superpowers 6.2.0; five fresh processes per
scenario; maximum concurrency three; enforced read-only, no-agents transport;
manual scoring; rubric withheld; run date 2026-08-03; zero infrastructure errors.
This metadata does not cover the new `WER-08` contract or the behavior-first rubric
repairs. Their current provenance and results are recorded in the Task 21
behavior-first validation result above.

The owner of every active ID is `writing-explicit-rationale`.
`WER-01`, `WER-02`, `WER-05`, `WER-06`, and `WER-08` affect only that skill;
`WER-07` also affects `lean-plan-writing`, `disciplined-development`, and
`disciplined-research`.
`WER-01` receives the immutable complete nine-skill control.
`WER-02`, `WER-06`, and `WER-08` receive only the immutable control
`skills/writing-explicit-rationale/SKILL.md` and inline task context.
`WER-05` receives that single-skill control plus its declared existing-rationale fixture.
No external skill dependency or live web access is supplied.

| ID | Affected skills | Type / status | Protected promise and section | Supplied context | Exact prompt | Evaluator-withheld rubric | Rerun trigger |
|---|---|---|---|---|---|---|---|
| `WER-01` | `writing-explicit-rationale` | Simple application + direct invocation / preservation | Direct invocation safely applies a small descope to the adjacent plan item, preserves remaining scope, and records the selected scope, cause, and accepted impact; Role, What rationale means here, Keep one authoritative home | Complete nine-skill control + inline release-plan decision | [WER-01](#wer-01--simple-direct-descope) | Score the complete artifact by effect: retain CSV and JSON in v1; defer XML; state unstable partner schema as the cause; state that XML clients wait for schema approval as the accepted impact; keep rationale adjacent in the revised item. Exact item syntax, unrelated plan work, sibling procedures, or process narration are separate task-fidelity or composition notes unless they obscure or contradict an owned decision, cause, impact, or rationale home. | Trigger, direct invocation, plan placement, scope preservation, rationale shape, or bundle composition changes |
| `WER-02` | `writing-explicit-rationale` | Non-trivial application + focused regression / preservation | Twice re-litigated rationale triggers a complete decision-site audit and one batched durable repair rather than another one-off reply; consequential and consequence-free sites are distinguished; What rationale means here, Keep one authoritative home, Resist duplicate rationale | Single-skill control + inline three-site change inventory | [WER-02](#wer-02--repeated-review-batch-audit) | Score the complete artifact by effect: inventory all three sites; batch durable rationale for ingest and quota at their decision sites or one referenced project home; preserve each chosen behavior, causal boundary, and consciously retained consequence; classify telemetry as needing no rationale. Equivalent wording passes, and a bounded consequence need not use the word `accepted`. Formatting and exact column text are task-fidelity notes unless they obscure an owned action. | Retroactive signal, batch-audit, active-choice trigger, non-trigger, authoritative-home placement, or rationale shape changes |
| `WER-05` | `writing-explicit-rationale` | Focused regression / watched RED → target GREEN | When authoritative project rationale already exists, new code references it instead of creating drift-prone copies; Keep one authoritative home, Resist duplicate rationale | Single-skill control + `docs/architecture/ingest.md` existing-rationale fixture | [WER-05](#wer-05--existing-rationale-reference) | The code comment must direct a maintainer unambiguously to `docs/architecture/ingest.md#interactive-guard-placement`, and neither the comment nor commit message may recreate the causal explanation plus accepted duplication or revisit rule as a competing rationale home. A short local operational cue or statement that duplication is intentional passes when the authoritative explanation remains only in the cited document. Labels, formatting, and commit-message composition are task-fidelity notes unless they make the authoritative rationale home ambiguous or create a competing explanation. | Existing-rationale fixture, authoritative-home rule, non-duplication rule, response shape, or decision facts change |
| `WER-06` | `writing-explicit-rationale` | Focused regression / preservation | A paste-ready code comment retains history only when it constrains correctness or a future implementation decision; What rationale means here | Single-skill control + inline serializer decision | [WER-06](#wer-06--relevant-history-only) | The complete comment must tell a maintainer to preserve legacy leading zeroes and make clear that signature verification depends on exact serialized bytes, so normalization breaks that verification. Equivalent causal wording and unambiguous pronouns pass; the words `signatures` and `invalidate` are not required. Omit the migration year, Perl, and other backstory without a correctness or future-decision consequence. Comment syntax and formatting are task-fidelity notes unless meaning becomes ambiguous. | Necessity predicate, historical-context boundary, rationale content, output shape, or decision facts change |
| `WER-07` | `writing-explicit-rationale`, `lean-plan-writing`, `disciplined-development`, `disciplined-research` | Parent-and-plan composition / target RED | The parent establishes on-page placement, delegates necessity judgment without forcing rationale for every defensible alternative, and routes every factual plan claim through universal grounding; What rationale means here | Disciplined development + disciplined research + writing-plans + lean plan writing + writing explicit rationale | [prompt](fixtures/writing-explicit-rationale/prompts/wer-07.md) | [rubric](fixtures/writing-explicit-rationale/rubrics/wer-07.md); record separate rationale-owner and composition-owner verdicts, with only the former entering the WER denominator | Parent/research wording, companion delegation, necessity predicate, plan/spec pairing, supplied choices, source-disclosure mapping, or useful-versus-harmful context threshold changes |
| `WER-08` | `writing-explicit-rationale` | Broad-domain isolated application / preservation | Repeated questions expose missing rationale in a nonprofit policy; add only the causal rationale at the policy decision site instead of leaving it in chat, minutes, or a newsletter; Role, What rationale means here, Keep one authoritative home | Single-skill control + inline nonprofit policy and non-durable rationale | [prompt](fixtures/writing-explicit-rationale/prompts/wer-08.md) | [rubric](fixtures/writing-explicit-rationale/rubrics/wer-08.md) | Broad-domain scope, repeated-review signal, rationale necessity or content, authoritative-home placement, reference-not-repeat, supplied policy, or scoring boundary changes |

| Scenario | `writing-explicit-rationale` verdict owns | Separate task-fidelity or composition note |
|---|---|---|
| `WER-01` | Selected scope, necessary cause and impact, and adjacent durable placement | Exact item syntax or formatting |
| `WER-02` | Batch audit, necessity classification, rationale content, and durable homes | Exact columns, labels, or the word `accepted` |
| `WER-05` | Stable authoritative reference and absence of a competing explanation | Labels, comment syntax, or the commit summary's exact verb |
| `WER-06` | Current correctness reason and exclusion of irrelevant history | Exact nouns, pronouns, or comment rendering when meaning stays clear |
| `WER-07` | Rationale necessity, useful content, and reference-not-repeat | Parent/plan ordering and source acquisition or disclosure retain their named owners; table rendering is generic task fidelity |
| `WER-08` | Re-litigation signal, necessary causal content, policy placement, and rejection of non-durable substitute homes | Labels or formatting when the insertion action remains unambiguous |

`WER-04` is intentionally unused: its pre-freeze commit-pressure contract was merged
into `WER-02`, `DISC-10`, and `WER-05` before execution.

### 2026-08-03 bundle manifests (prior evidence)

The `WER-01` complete control uses the Task 1 nine-skill archive SHA-256
`8f21c8267d005c349702ec94d6aff26c13a09bfbe29f2b43efcfbb37304f16e3`.
The `WER-02`, `WER-03`, `WER-05`, and `WER-06` single-skill controls use file SHA-256
`97eb06c649c194e8819b4dff68b808eda4ec7c948a6ead518da247daf31d6cfe`.
Their single-skill archive SHA-256 is
`d7147756bc0cf242fa63ece39ac285216e456addef5bd2c691cb9ec62c73bd0c`;
its canonical content-manifest SHA-256 is
`b65ffacec428203c808a42a3aab00458100f0688c328e2666398f255465657dd`.

| Scenario | Source kind | Full revision or frozen content revision | Source path | Bundle-relative path | File SHA-256 |
|---|---|---|---|---|---|
| `WER-01` | Repository | `4296647f0dff48a9e77b979ef07e813bf1f66db2` | The exact nine source paths listed in [README.md](README.md#immutable-control-bundles), incorporated here as the Task 1 manifest | Same nine repository-relative paths | Per-file hashes in that manifest |
| `WER-02`, `WER-03`, `WER-06` | Repository | `4296647f0dff48a9e77b979ef07e813bf1f66db2` | `skills/writing-explicit-rationale/SKILL.md` | `skills/writing-explicit-rationale/SKILL.md` | `97eb06c649c194e8819b4dff68b808eda4ec7c948a6ead518da247daf31d6cfe` |
| `WER-05` | Repository | `4296647f0dff48a9e77b979ef07e813bf1f66db2` | `skills/writing-explicit-rationale/SKILL.md` | `skills/writing-explicit-rationale/SKILL.md` | `97eb06c649c194e8819b4dff68b808eda4ec7c948a6ead518da247daf31d6cfe` |
| `WER-05` | Inline fixture | Task 6 RED candidate frozen 2026-08-03 by the content hash in this row | `skill-validation/writing-explicit-rationale.md#wer-05-fixture` | `docs/architecture/ingest.md` | `5e25960ed19f0e046ecb263282d9244b9a5026695cc16a7ddb08663f422e4f7e` |
| `WER-07` control | Prior approved working-tree candidates + declared external dependency | Frozen 2026-08-03 by the file hashes in this row | `skills/disciplined-development/SKILL.md`; `skills/lean-plan-writing/SKILL.md`; `skills/writing-explicit-rationale/SKILL.md`; Superpowers 6.2.0 `writing-plans` | Same four paths under `skills/` | `21a46fb9b80cf29862a5e8ee5953fc6a3b3271da044eca60ac75b7060f43562e`; `4c659b76d3bfbe47a6fad906987eeb2166be577613d4a4832c96b8b341039d8c`; `ec77350bf2b51ba9ccb09375234f4727a0189417e2b1a0e1814aca30dd58a62c`; `72190c88b2b5a67a96b91d66aa72b9161913e10e8769da3f28a226f4cc7b99d0` |
| `WER-07` target | 2026-08-03 working-tree candidates + declared external dependency | Frozen 2026-08-03 by the file hashes in this row | Same four source paths as control | Same four bundle-relative paths | `82337abab625c40e811e274910bae654ce892004dc70210392adaa6fcc06d776`; `76351124307a05429d4d594394bca215df92ff7d33679f6367811beb0d8488eb`; `4035ecdf52cd6a9302d399440d4e93b1776fb043981558f62c584bf5aed39865`; `72190c88b2b5a67a96b91d66aa72b9161913e10e8769da3f28a226f4cc7b99d0` |

The `WER-07` control and 2026-08-03 target canonical content-manifest SHA-256 values are
`8f44b0c0a7118564a696d8fa10f4b267b8741ef67181010bbb3ecd56fe7eb234`
and `add84b6a7c2d04718e6957c3672e3081dad101d65eb1dfe730d57af0efd07509`.

The fixture-expanded `WER-05` canonical content-manifest SHA-256 is
`bc170bc184b7f59a991513c331ce8e72192a683909f48abc799099824b2a0c3b`.

The 2026-08-03 complete-suite target skill file SHA-256 was
`4035ecdf52cd6a9302d399440d4e93b1776fb043981558f62c584bf5aed39865`.
Its complete nine-skill, single-skill, and fixture-expanded canonical
content-manifest SHA-256 values are respectively
`6f88fedf7f60eda822f7db106abfbabf450ce97e401cb96eb8a1729bfc905e10`,
`3792834d17f9db7344c37b161c0e680993b45a1d767fbe5b09d3b88fb58dca89`,
and `51c391083ab0958ac8671cee3be11383ce71ed077d27c1764b8f7bebeba35a56`.

The owner-approved final placement clarification adds architecture documents to
the durable document examples and names a code decision-site comment explicitly.
Its skill file SHA-256 is
`a41d59faaea4be81e6cff5b2e35154f8b4b6d077afce6c0c6cd9a3d8cb82c3e6`.
Only `WER-02` and `WER-05` met their rerun triggers; both passed 5/5 on fresh
Sol-high evaluators. Their 2026-08-03 single-skill and fixture-expanded canonical
content-manifest SHA-256 values are respectively
`7a2b47984edad87463fc9dbe7405cf5646c46cf8dde142cb30acd640b9c8d3bf`
and `5faa20d515408799218af4d110b9b1a09257ed72805560201abf6fbe62903bdb`.

The 2026-08-03 complete target retains six Task 1 control files and replaces the parent,
lean-plan, and explicit-rationale skills used by the final composition test.
Its path-sorted canonical manifest is:

| Bundle-relative path | Source | File SHA-256 |
|---|---|---|
| `skills/adversarial-review-loop/SKILL.md` | `4296647f0dff48a9e77b979ef07e813bf1f66db2` | `46b85eafc5db54cb521eed9c4a110e552c76d97cfae72e141f109c9dea10f0c6` |
| `skills/adversarial-review/SKILL.md` | `4296647f0dff48a9e77b979ef07e813bf1f66db2` | `9004ff153d5dc3a3690254667c4f666151dcabff7ef6f705cc751134be56499c` |
| `skills/concise-writing/SKILL.md` | `4296647f0dff48a9e77b979ef07e813bf1f66db2` | `4d12a2eb475c6b2ef57e2300c8c07af3f59c1e07b2b82695a3b7669eee1d6d72` |
| `skills/disciplined-development/SKILL.md` | 2026-08-03 Task 16 target | `82337abab625c40e811e274910bae654ce892004dc70210392adaa6fcc06d776` |
| `skills/disciplined-research/SKILL.md` | `4296647f0dff48a9e77b979ef07e813bf1f66db2` | `a5c4079e5aa21651ecd39b09e3fb2d9a58f4a1f3b99354b3b6927b2d44c6fb50` |
| `skills/dispatching-development-subagents/SKILL.md` | `4296647f0dff48a9e77b979ef07e813bf1f66db2` | `b89b4db8af53bd136237cb2306f956c039757a0e321b1f704bd16d1a00580500` |
| `skills/lean-plan-writing/SKILL.md` | 2026-08-03 Task 16 target | `76351124307a05429d4d594394bca215df92ff7d33679f6367811beb0d8488eb` |
| `skills/sweeping-stale-references/SKILL.md` | `4296647f0dff48a9e77b979ef07e813bf1f66db2` | `d6812c33cae026807bbb3ebe851d93b60b513dd87ea5efd98aea28f5c02f9157` |
| `skills/writing-explicit-rationale/SKILL.md` | 2026-08-03 Task 16 target | `4035ecdf52cd6a9302d399440d4e93b1776fb043981558f62c584bf5aed39865` |

#### WER-05 fixture

`docs/architecture/ingest.md`

```markdown
# Ingest architecture

## Interactive guard placement

Tenant guards stay at interactive ingest handlers because batch imports reach persistence only after approval.
This accepts duplication across two interactive handlers; extract a shared interactive guard when a third caller needs it.
```

Every prompt below is byte-for-byte evaluator input.
The catalog rubrics never enter evaluator prompts.

### WER-01 — simple direct descope

```text
You are a fresh, read-only skill evaluator.
The complete nine-skill local bundle is installed. Do not edit files, change git state, inspect anything outside the supplied bundle, or dispatch agents.
Directly invoke `writing-explicit-rationale`: read `skills/writing-explicit-rationale/SKILL.md` completely and follow it as binding guidance.

The current release-plan item says: "Ship CSV, JSON, and XML export in v1."
The team decided to keep CSV and JSON in v1 but defer XML because the partner schema is still unstable. Customers who require XML will wait until the partner approves a stable schema.

Return only one revised release-plan item. Do not revise any other part of the plan or narrate your process.
```

### WER-02 — repeated-review batch audit

```text
You are a fresh, read-only skill evaluator.
Only `writing-explicit-rationale` and the supplied task context are available. Do not edit files, change git state, inspect anything outside the supplied bundle, or dispatch agents.
Read `skills/writing-explicit-rationale/SKILL.md` completely and follow it as binding guidance.

A reviewer has twice said to move the tenant rate-limit guard from `src/ingest.py:44` into shared `persist()`. The author answered only in review chat that `batch_import.py` also calls `persist()` with already-approved batches, so the guard must stay at interactive ingest; this accepts duplicated guards in `src/ingest.py` and `src/admin_ingest.py` until a third interactive caller appears.
The same change also preserves the previous quota for 60 seconds after a downgrade at `src/quota.py:73` because in-flight requests still carry the old token; this accepts up to 60 seconds of elevated quota.
At `src/telemetry.py:19`, the project chooses between two equally maintained and secure telemetry libraries with identical observable behavior and no downstream consequence.

Handle the repeated finding before another review.
Return only a decision-site inventory with `Location` and `Action` columns, followed by the exact durable artifact text to add. Do not write a reviewer reply or narrate your process.
```

### Historical WER-03 — amendment-rewriting diagnostic

The exact final evaluator-withheld rubric is retained at
[rubrics/wer-03.md](fixtures/writing-explicit-rationale/rubrics/wer-03.md).

```text
You are a fresh, read-only skill evaluator.
Only `writing-explicit-rationale` and this non-software task are available. There is no repository, code, Git, PR, hook, or sibling skill. Do not edit files, change state, inspect anything outside the supplied bundle, or dispatch agents.
Read `skills/writing-explicit-rationale/SKILL.md` completely and follow it as binding guidance.

A nonprofit's Emergency grants policy normally caps each grant at $2,000.
The finance committee approved a temporary cap of $5,000 through March 31, 2027 because winter-shelter demand has outgrown the ordinary limit.
The exception may consume up to $30,000 of contingency funds, will be reviewed monthly, and reverts to $2,000 after March 31, 2027.

Return only the exact amendment text to insert under the policy's `Emergency grants` heading.
```

### WER-05 — existing rationale reference

```text
You are a fresh, read-only skill evaluator.
Only `writing-explicit-rationale` and the supplied project document are available. Do not edit files, change git state, inspect anything outside the supplied bundle, or dispatch agents.
Read `docs/architecture/ingest.md` and `skills/writing-explicit-rationale/SKILL.md` completely and follow the skill as binding guidance.

You are adding the existing tenant guard to `src/admin_ingest.py`, the second interactive handler.
The reviewer is waiting and the user says: "Add a comment explaining why the guard stays here, and repeat the explanation in the commit message so nobody misses it."
The authoritative rationale already exists under `Interactive guard placement` in the supplied project document.

Return only two labeled, paste-ready blocks: `Code comment` and `Commit message`.
Do not narrate your process.
```

### WER-06 — relevant history only

```text
You are a fresh, read-only skill evaluator.
Only `writing-explicit-rationale` and this task context are available. Do not edit files, change state, inspect anything outside the supplied bundle, or dispatch agents.
Read `skills/writing-explicit-rationale/SKILL.md` completely and follow it as binding guidance.

The serializer at `src/archive.py:41` preserves leading zeroes in legacy numeric strings instead of normalizing them because archived records are signature-verified against their exact serialized bytes. Normalization would invalidate those signatures.
The team first encountered the issue during a 2019 migration, and the importer used for that migration was written in Perl. The migration year and implementation language do not affect current correctness or any future implementation choice.

Return only the exact code comment to place above the serialization branch.
```

### Historical WER-07 — parent and plan composition

```text
You are a fresh, read-only skill evaluator.
Only the five supplied skills are available. Do not edit files, change git state, inspect anything outside the supplied bundle, or dispatch agents.
Read `skills/disciplined-development/SKILL.md`, `skills/disciplined-research/SKILL.md`, `skills/writing-plans/SKILL.md`, `skills/lean-plan-writing/SKILL.md`, and `skills/writing-explicit-rationale/SKILL.md` completely and follow all applicable guidance.

Update a plan's decision-site table for these choices:
- Keep tenant rate-limit guards at interactive ingest handlers because `batch_import.py` calls shared `persist()` only with approved batches. This accepts two duplicated guards until a third interactive caller appears.
- Preserve the previous quota for 60 seconds after downgrade because in-flight requests carry the old token. This accepts up to 60 seconds of elevated quota.
- Use telemetry Library A rather than Library B. Both are equally maintained and secure, have identical observable behavior, and create no downstream consequence.

A senior reviewer says: "The parent doctrine requires rationale for every choice over a defensible alternative. Add a why for all three choices."

Return only a table with `Location` and `Plan text` columns. You may add a `Source disclosure` column when applicable guidance requires it. Do not narrate your process.
```

### Current parent-architecture attribution (2026-08-10)

`WER-07` remains owned here as five separately attributed child-composition slots.
It tests rationale-method composition and is never pooled into the 45-slot
`DD-01`–`DD-09` parent acceptance denominator. Child invocation, loading, rationale
output quality, and research correctness/disclosure remain attributable to their
owning contracts and are not parent PASS/FAIL criteria. The final Task 18A union
passed `WER-07` **5/5**; the evidence below remains historical under its recorded
contract. Complete current provenance is in
[the Task 18A manifest](task-18a-provenance.json).

### Task 18A WER-07 freeze

`WER-07` is reclassified as `disciplined-research` **required** because every plan
row states factual current-behavior, cause, consequence, maintenance, security, or
observable-behavior claims.
User-supplied decision context is support to acquire, verify, and disclose, not an
exemption from disclosure.
The prior prompt, four-skill bundles, rubrics, and results remain historical.

The repaired five-skill control uses base
`bd30bf7c9070f2f56b6d2ae32a746518e2259b6f` parent, research, lean-plan, and
explicit-rationale files plus Superpowers 6.2.0 `writing-plans`.
Its canonical content-manifest SHA-256 is
`9064f0d332e810f7b079c01fd71e9e4c420f65e33d964684f8ab781a78a00146`
after adding four immutable `project/wer-07/` primary sources.
Prompt SHA-256 is `b4fbdd831bc8d569a4fe61fcb9898d112b44089779c9b4329c30e1df51ece92f`;
rubric SHA-256 is `877f8a42da7696dcb97d76438c66eb2699e22c71ba5d41b51ee2a445c1ee769f`.
The pre-repair artifacts and their manual shadows remain historical. The completed
post-freeze contextful arm is 2/5 high (F/P/F/F/P) and 3/5 low (P/F/P/F/P).
Universal disclosure is a new positive promise, so this remains a target RED.
High is the candidate gate and low is robustness evidence only. The final scorer
root is `/private/tmp/dd-task18a-control-scoring-contextful-f59608a`, with freeze
SHA-256 `a72902e254706d2a13c9ff573bcffff6469271fdaf914f1b9e55db6a36fa0675`
and plan SHA-256
`cfb8e3f7949afc2b35407abd203fdd02767fdc1f698081f2fa952156f2f801bb`;
aggregate SHA-256 is
`c801090c6252298da41954663dd3f671164cd77fceaa77abf71583fa43fa2f60`.
The control root `/private/tmp/dd-task18a-control-postfreeze-f59608a` has freeze
`0119bdb403fdb89978ed6c2f34bae8de5db13c392071b97b06687d81f9be0210`
and plan `4de14a3e7531c8cf0e6258f82c9c8050b849ca9d0f0f8c1c633248dafcd81b4b`.
All selected attempts were a1 with zero retries/errors under Codex CLI 0.147.0,
read-only/no-agents transport.
The final behavior-first rubric is SHA-256
`9cf7a96a1ed25794a630a1642c7255eac9b417623cb4f6759bfb81bcdac19b4c`.
Fresh re-adjudication of the same frozen response bytes scored high 3/5 and low
5/5. The watched high control therefore remains RED; low remains robustness only.
The shared record carries the fresh scorer provenance, while `877f8a42…` remains
the historical prior-rubric epoch.
The context-stripped `289ef0fd…` aggregate is transport-defective historical
evidence only.

The prior `3e80cd1…` focused parent candidate passed `WER-07` 5/5 (`PPPPP`) at `a1`
with zero accepted retries. Full provenance is in the
[parent record](disciplined-development.md#task-18a-focused-parent-candidate-checkpoint);
the complete focused slice remains below threshold.

The revised approved `a6aa8b6…` candidate scored `WER-07` 3/5 (`FFPPP`) at
`a1` with zero accepted retries. R1 and R2 add quota-validity or enforcement
claims unsupported by the supplied quota source. These are genuine candidate
misses, not a contract defect. Exact restart provenance is in the
[restart result](disciplined-development.md#approved-focused-green-restart-result).

The approved `320cdba…` candidate passed `WER-07` 5/5 (`PPPPP`) at `a1`
with zero accepted retries or infrastructure errors. Exact provenance is in the
[next restart result](disciplined-development.md#next-approved-focused-green-restart-result);
the complete focused slice remains below threshold.

| WER-07 primary fixture member | SHA-256 |
|---|---|
| `project/wer-07/batch_import.py` | `2fbe0370868be60a4b8a96907c7404c65ae7b969bc5b63cfb0a6b521306beb20` |
| `project/wer-07/sources/ingest-architecture.md` | `abc91b3248cae99aef1b3baa1418e5ea4eb0d943c99aa3460f75fd6fbec2f46a` |
| `project/wer-07/sources/quota-tokens.md` | `0c06c4c7edc867de42105325eaccf30fb9112a7888a38eb812ec4b03945eeeef` |
| `project/wer-07/sources/telemetry-comparison.md` | `34853c94fa465fc5ba2ef01b810419f2b3200b61a03b2111bdb2a150f31ba49a` |

## Task 11 Sol-low control results (2026-08-07)

These are the frozen low-effort control outcomes. The shared freeze, transport,
hash, scorer, and adjudication provenance is recorded in
[README.md](README.md#task-11-sol-low-control-freeze-and-results).
Each completed response counts; observed REDs are retained as results, not treated as fixes.

| ID | Status | R1 | R2 | R3 | R4 | R5 | Score | Exact missed criteria / adjudication |
|---|---|---|---|---|---|---|---:|---|
| `WER-01` | preservation | P | P | P | P | P | **5/5** | Every item makes the absence of an approved stable partner schema the causal deferral boundary and states that XML customers wait; orchestrator overruled scorer literalism. |
| `WER-02` | preservation | P | P | P | P | P | **5/5** | All three sites inventoried; both triggering rationales preserve behavior/cause/consequence and telemetry is correctly consequence-free. |
| `WER-03` | preservation | P | P | P | P | P | **5/5** | Every amendment includes the temporary cap, dates, winter-shelter cause, contingency exposure, monthly review, and automatic reversion. |
| `WER-05` | target | F | F | F | F | F | **0/5** | None cites the authoritative architecture document; all also duplicate rationale into the commit message. |
| `WER-06` | preservation | P | P | P | P | F | **4/5** | R5 says normalization would invalidate `them`, failing to name signatures; R1-R4 preserve the exact-bytes/signature causal boundary without backstory. |
| `WER-07` | target | P | F | F | P | F | **2/5** | R2 invents complexity; R3 invents responsibility/precedent framing; R5 precommits a third caller to persistence rather than stating the required revisit condition. |

Owned Task 11 Sol-low aggregate: **21/30**.

**Scope disposition (2026-08-07):** `WER-03` remains valid isolated broad-domain
application evidence. Cross-model portability comes from the complete cold Sol-high
in-domain suite. The current policy scope is approved behavior; this scope repair
does not authorize a skill edit or behavioral rerun.

**Superseded active disposition (2026-08-15):** the behavior-first audit found that
the scenario's exact-amendment task makes generic artifact-rewriting fidelity the
dominant variable. Its historical outcomes remain valid for that contract, but it
no longer supplies active broad-domain skill acceptance; `WER-08` owns that role.

## Prior Sol-high results (2026-08-03; superseded)

The target bundles below preserve the 2026-08-03 evidence. The 2026-08-05 rerun
supersedes them; only the bundles in that rerun are current targets.

| ID | Original control bundle SHA-256 | Control status | Control repetitions | Exact control misses | 2026-08-03 target bundle SHA-256 | Target status | Target repetitions | Earlier-arm run date | Earlier-arm infrastructure errors | Sol-low control | Cleaned Sol-high | Cleaned Sol-low |
|---|---|---|---|---|---|---|---|---|---:|---|---|---|
| `WER-01` | `8f21c8267d005c349702ec94d6aff26c13a09bfbe29f2b43efcfbb37304f16e3` | **5/5 PASS** | P / P / P / P / P | None | `6f88fedf7f60eda822f7db106abfbabf450ce97e401cb96eb8a1729bfc905e10` | **5/5 PASS** | P / P / P / P / P | 2026-08-03 | 0 | [Task 11 detail](#task-11-sol-low-control-results-2026-08-07) | Task 26 | Task 27 |
| `WER-02` | `b65ffacec428203c808a42a3aab00458100f0688c328e2666398f255465657dd` | **5/5 PASS** | P / P / P / P / P | None | `7a2b47984edad87463fc9dbe7405cf5646c46cf8dde142cb30acd640b9c8d3bf` | **5/5 PASS** | P / P / P / P / P | 2026-08-03 | 0 | [Task 11 detail](#task-11-sol-low-control-results-2026-08-07) | Task 26 | Task 27 |
| `WER-03` | `b65ffacec428203c808a42a3aab00458100f0688c328e2666398f255465657dd` | **5/5 PASS** | P / P / P / P / P | None; isolated broad-domain preservation | `3792834d17f9db7344c37b161c0e680993b45a1d767fbe5b09d3b88fb58dca89` | **5/5 PASS** | P / P / P / P / P | 2026-08-03 | 0 | [Task 11 detail](#task-11-sol-low-control-results-2026-08-07) | Task 26 | Task 27 |
| `WER-05` | `bc170bc184b7f59a991513c331ce8e72192a683909f48abc799099824b2a0c3b` | **0/5 watched RED** | F / F / F / F / F | All five copied the existing rationale into both blocks; none cited the authoritative document from the code comment | `5faa20d515408799218af4d110b9b1a09257ed72805560201abf6fbe62903bdb` | **5/5 PASS** | P / P / P / P / P | 2026-08-03 | 0 | [Task 11 detail](#task-11-sol-low-control-results-2026-08-07) | Task 26 | Task 27 |
| `WER-06` | `b65ffacec428203c808a42a3aab00458100f0688c328e2666398f255465657dd` | **5/5 PASS** | P / P / P / P / P | None; every response retained the signature constraint and omitted irrelevant migration history | `3792834d17f9db7344c37b161c0e680993b45a1d767fbe5b09d3b88fb58dca89` | **5/5 PASS** | P / P / P / P / P | 2026-08-03 | 0 | [Task 11 detail](#task-11-sol-low-control-results-2026-08-07) | Task 26 | Task 27 |
| `WER-07` | `8f44b0c0a7118564a696d8fa10f4b267b8741ef67181010bbb3ecd56fe7eb234` | **2/5 watched RED** | P / F / F / F / P | R2 omitted unchanged telemetry behavior; R3 proposed moving enforcement into shared `persist()` after a third interactive caller; R4 had both misses | `add84b6a7c2d04718e6957c3672e3081dad101d65eb1dfe730d57af0efd07509` | **5/5 PASS** | P / P / P / P / P | 2026-08-03 | 6 excluded startup/configuration failures before the accepted runs; 0 in the 2026-08-03 target run | [Task 11 detail](#task-11-sol-low-control-results-2026-08-07) | Task 26 | Task 27 |

Every active result was manually scored against every observable criterion.
Raw evaluator outputs remain in scratch and are not committed.

`WER-05` initially scored 4/5 under a redundant rubric clause requiring a comment at
an already-visible guard site to restate that the guard applies there.
A fresh Sol-high classifier marked the clause inconsistent with the approved
reference-not-repeat contract.
After deleting only that clause, the unchanged five outputs rescored 5/5.
The unchanged Task 6 description preserved `DISC-10` routing at 5/5 after the final
body refactor; the previously completed 50/50 full discovery result remains active.

`WER-07` initially reproduced the same omission in both arms: under pressure to decide
whether each choice needs a why, two of five evaluators reduced the consequence-free
telemetry row to the choice alone and dropped its supplied unchanged behavior.
The 2026-08-03 target retained the behavior in 5/5 runs. Four also characterized the
selection as an arbitrary tie-break or as having no decision-relevant rationale.
The original exactness rubric treated those concise, fact-consistent clarifications
as invented rationale; the owner rejected that threshold because the text is accurate,
non-harmful, small, and can prevent a future reader from inferring a load-bearing
preference. A fresh Sol-high design review passed the repaired useful-versus-harmful
threshold, and a criterion-level rescore passed all five unchanged target outputs.
The repaired rubric continues to fail material invented criteria, preferences,
trade-offs, history, constraints, future consequences, or disproportionate explanation.
Six pre-run processes failed before evaluator startup while the read-only transport
was being configured; accepted evaluator processes completed without infrastructure
error.

### Pre-format holistic-rule rerun (2026-08-05; superseded)

After the owner-approved holistic rewrite of `What rationale means here`, all six
active scenarios passed fresh `gpt-5.6-sol` evaluations at high reasoning effort.
Each scenario used five fresh read-only, no-agents processes with maximum concurrency
three; the orchestrator manually scored every criterion, and no infrastructure
errors occurred.

| ID | Pre-format target bundle SHA-256 | Result | Repetitions |
|---|---|---|---|
| `WER-01` | `ae4ded66e5e77e458fdd4adcdf3385e82a6932944881e7a37e335df01c3dcb10` | **5/5 PASS** | P / P / P / P / P |
| `WER-02` | `deb77c5b3c69a7bd5131e50c66d879d7e414b73e0df06458a5bee249151665c9` | **5/5 PASS** | P / P / P / P / P |
| `WER-03` | `deb77c5b3c69a7bd5131e50c66d879d7e414b73e0df06458a5bee249151665c9` | **5/5 PASS** | P / P / P / P / P |
| `WER-05` | `e2989440b8920660f98b004f31e46c9cc2f39d25961659498206d12f2616d0fe` | **5/5 PASS** | P / P / P / P / P |
| `WER-06` | `deb77c5b3c69a7bd5131e50c66d879d7e414b73e0df06458a5bee249151665c9` | **5/5 PASS** | P / P / P / P / P |
| `WER-07` | `c4b6b2e1f1b9e29bcd94f2efd89091f36e418ce09a4d16c5f4c085d01e8561f1` | **5/5 PASS** | P / P / P / P / P |

The pre-format explicit-rationale skill file SHA-256 is
`ce0ba16731a31b5e7a08dbd7c12256d6c50b094808f3eb3c349ba4f78acdc482`.
The `WER-07` component file SHA-256 values are
`dff55e1348ebde0ec45c8b1861e48c000a5befdbd2f23deb4e857fa1945c93a6`
for disciplined development,
`76351124307a05429d4d594394bca215df92ff7d33679f6367811beb0d8488eb`
for lean plan writing, and
`72190c88b2b5a67a96b91d66aa72b9161913e10e8769da3f28a226f4cc7b99d0`
for Superpowers writing-plans.

All five `WER-07` outputs retained Library A together with the supplied equivalent
maintenance and security, identical observable behavior, and lack of downstream
consequence without inventing a material preference. All five also preserved the
ingest third-caller boundary and the quota choice's accepted 60-second elevated-quota
consequence.

### Final layout-only rerun (2026-08-05)

The cycle-3 reviewer required the three approved sentences to occupy separate
source lines. Words, punctuation, predicates, and rendered structure did not
change, but the post-approval skill-edit rule restarted all six active scenarios.
Each used five fresh read-only, no-agents `gpt-5.6-sol` high-effort processes with
maximum concurrency three and manual orchestrator scoring.

| ID | Final target bundle SHA-256 | Result | Repetitions | Accepted / excluded infrastructure events |
|---|---|---:|---|---:|
| `WER-01` | `3eec701dfa4d9641938ff334977e16fc48247a87b632e976b59e8d56460e1c46` | **5/5 PASS** | P / P / P / P / P | 0 |
| `WER-02` | `c9934a69121e404ff1fc9961942a3b6314fea163c1a8917071d2b99929f74a67` | **5/5 PASS** | P / P / P / P / P | 0 |
| `WER-03` | `c9934a69121e404ff1fc9961942a3b6314fea163c1a8917071d2b99929f74a67` | **5/5 PASS** | P / P / P / P / P | 0 |
| `WER-05` | `479f870bcb7f673852bacc27d9a04680229cbdb43531d8ee3eaa99ed162d5098` | **5/5 PASS** | P / P / P / P / P | 0 / 1 pre-start approval-service timeout |
| `WER-06` | `c9934a69121e404ff1fc9961942a3b6314fea163c1a8917071d2b99929f74a67` | **5/5 PASS** | P / P / P / P / P | 0 |
| `WER-07` | `7f04457ff1e90b9cd8dccfe45a6fc6e50244abe9d771105e31ac3917fc117c7f` | **5/5 PASS** | P / P / P / P / P | 0 |

The final explicit-rationale skill SHA-256 is
`568b2a61bef3f7694014fb89228f933261837acd4f2b5978b2b8ef55aa108c9f`.
The `WER-07` parent, lean-plan, and writing-plans component hashes remain
`dff55e1348ebde0ec45c8b1861e48c000a5befdbd2f23deb4e857fa1945c93a6`,
`76351124307a05429d4d594394bca215df92ff7d33679f6367811beb0d8488eb`,
and `72190c88b2b5a67a96b91d66aa72b9161913e10e8769da3f28a226f4cc7b99d0`.
All five final `WER-07` outputs preserved the supplied ingest and quota
consequences and the consequence-free telemetry facts without inventing a
material preference. One `WER-05` launch timed out in approval review before
evaluator startup; the identical retry completed and passed.

On 2026-08-06, cold review found that the active `WER-07` rubric named only the
telemetry behavior even though the prompt and manual scoring covered equal
maintenance, equal security, identical observable behavior, and no downstream
consequence. The rubric now enumerates all four facts. The five frozen outputs
above were rechecked against it and remain 5/5; evaluator input, bundle, and skill
prose did not change, so no new model run was required.

### Rejected cold-review proposal

A cold review proposed removing the what/how/why lead-in and adding a stale-rationale
branch. The exact scratch candidate had file SHA-256
`f8c00ce70affbb98e5348fea4b4e3227df5ef86560b7f314dea8e70561aea59d`.
It scored 4/5 on `WER-07`: one run incorrectly proposed moving the guard into shared
`persist()` after a third interactive caller. A separately reviewed stale-rationale
scenario scored 1/5 on the current control and 1/5 on the proposal; four proposed
runs still preserved obsolete history or moved current rationale into a duplicate
code home. The owner rejected the ineffective proposal and kept the current skill.

## Preserved historical evidence

### Reviewer-visibility loophole closure (2026-07-03)

**Edit:** description no longer lists commit bodies as an application surface and
gains the trigger "rationale about to land only in a commit message or PR
description"; the Role owned-scope drops commit bodies; the Scope closer names the
enforcement mechanism ("reviewers read the tree, not the log — rationale only in a
commit message is invisible to the review that will re-litigate it"); the
commit-body rationalization row sharpened to the same mechanism.

**RED evidence:** owner-watched recurring failure — models putting decision
rationale in commit messages where the whole-repo reviewer cannot see it. Loophole
analysis: the description itself sanctioned commit bodies as a rationale home
(agents act on descriptions and skip bodies — SDO), and the skill's motivation was
exclusively the future reader; the immediate consequence (gating reviewer can't see
it) was unstated. No reproducible in-harness RED: baseline arm (ambient consumer
context, original skill) passed 5/5 — steno's CLAUDE.md commit rule enforces the
same behavior ambiently, so single-shot scenarios can't isolate the skill there.

**Method + results:** commit-pressure single-shot (user explicitly instructs
"explain the choice in the commit message"), sonnet, hand-read. New wording:
**8/8 correct** — durable rationale to a code comment at the decision site + plan
note, commit body citing or additive; **zero over-fire** (every rep still satisfied
the user's instruction additively — the edit must never read as "commit bodies may
carry nothing"); low variance (one converged shape).

**Formal run (2026-07-04, skill @ `db26297`).** Commit-pressure scenario,
protocol-style (agent reads the skill file as sole doctrine; explicit "no CLAUDE.md,
no repo conventions" framing; sunk-cost + reviewer-waiting pressure; the ask pushes
rationale into the commit message). New text **5/5** artifact-first — comment at the
decision site (+ plan note in 4/5), commit body additive/citing, one rep quoting
"reviewers read the tree, not the log" back verbatim; **zero over-fire** (every rep
still explained in the body as asked). Pre-edit control **3/3 also artifact-first** —
the original body already binds when read in full, so this protocol structurally
cannot reproduce the description-layer loophole (an agent acting on the description
without reading the body). Standing evidence base for the edit therefore remains the
loophole analysis + the owner-watched incidents; these runs establish no-regression
and correct new-text behavior. True long-context in-situ pressure stays untestable in
this harness.

### Superseded edit contract

The former edit rule required both bare and governed commit-pressure arms and treated
an additive rationale-bearing commit body as a success condition.
The owner retired that contract on 2026-08-03: commits and PRs are not rationale
stores, and existing authoritative rationale is referenced rather than repeated.
`WER-02`, `DISC-10`, and `WER-05` now isolate the surviving placement, routing, and
non-duplication behaviors.

### Trigger-only description routing (2026-08-01)

**Matrix.** Route five prompts from metadata only: active-plan implementation with delegation; padded README tightening; SKILL.md shortening; plan deferral with PR-only rationale; and a routine convention-preserving rename.

**Pre-edit control: 3/3 PASS.** All evaluators selected `writing-explicit-rationale` for the plan deferral whose rationale lived only in the PR and did not select it solely for a routine convention-preserving rename.
The description edit is a trigger-only clarity and length refactor, not a routing fix.

**GREEN requirements.** Preserve the deferral, oversight-risk, defensible-alternative, re-litigation, and non-durable-rationale triggers while keeping routine self-evident choices out of scope.

**GREEN result: 3/3 PASS.** All three independent metadata-only evaluators selected the skill for PR-only deferral rationale and did not select it solely for the routine convention-preserving rename.
