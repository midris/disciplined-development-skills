# CW cross-model evaluation procedure and execution review

The owner requested cross-model evaluation of completed CW outputs, using a controller-started Fable-medium session after a manual review exposed a scoring disagreement.
The owner selected CW first, with SSR deferred until its rewrite, and prefers the shorter SKILL.md when effectiveness is equivalent.
The [protocol](../skill-studies/concise-writing/protocol.md) owns current progress and accounting; the [evaluation record](../skill-studies/concise-writing/evaluation/README.md) owns method and evidence.

## Preparation and first three evaluations

The full retrospective selects all 136 completed CW outputs before evaluator outcomes: 120 expanded plus sixteen historical, in twelve fixed groups.
The first handoff review is not used to select favorable later cases or alter source criteria.
The original subject records and frozen scoring policy are unchanged.
Native numeric outputs receive no functional CW score, and loading is not inferred from output quality.
Historical contribution and rewrite-comparison batches remain separate despite matching requested runtime names.
The historical-specific prompt makes that separation explicit before either historical dispatch.

Claude CLI 2.1.301 resolves fable to claude-fable-5-1; a local scripted endpoint confirms medium effort and native Read delivery with no model inference.
The reviewer exposes only Read, Glob and Grep, with no skills or shell tools, under the existing verified read-only OS policy.
All three completed real evaluations match the intended model and tool surface, retain every copied input unchanged and have matching raw-bundle inventories.
Ordered traces show all selected outputs read and a substantial first-pass assessment emitted before prior-assessment.md was read.
The first handoff review agrees with the owner's manual Fable review on all-nine-pass outcomes while preserving the active assessor's disagreement over two rationale omissions.
Neither agreement nor model voting automatically changes the canonical scores.

The original actual-CLI shell checks fail on this host because /opt/homebrew/bin/python3 is absent and lookup falls back to Apple Python 3.9.6, whose xcrun bookkeeping is denied by the policy.
The evidence does not establish a new CLI shell regression; the initial attribution was corrected in the live plan and evaluation record.
No host Python installation, production sandbox widening or subject rerun was made.
The separate file-reader qualification and shared isolation/mutation-denial probes pass.

## Supplemental accounting support

The existing accounting reader could represent evaluator pools in subject indexes, but could not count a supplemental review ledger without pretending each review was a subject execution.
A narrow version-1 charge projection now counts evaluator rows alongside the unchanged subject indexes.
Tests cover valid charges, booleans, wrong roles, missing IDs, duplicates across ledger types, unknown versions, malformed lists and mixed subject/evaluator formats.
The valid-ledger and duplicate-ID cases failed before implementation; all eight targeted cases pass afterward.
The mixed-format case uses a shadow subject-index charge that would otherwise reconcile silently; the parser rejects the mixed representation explicitly.
The ledger does not claim semantic validity or replace raw capture/retention checks.

The complete document test file now passes all 82 checks, including all eight focused ledger cases.
The main unit suite passes 332 tests, excluding 148 process-smoke checks; the full-suite failure counts remain disclosed below.
The hook suite passes 263 tests, with three environment skips.
A full runner-suite attempt reports 474 passed and six failures in unchanged surrogate Claude process smokes, reproduced with host permission.
Those surrogate executables resolve Python through the missing Homebrew path and fall back to Apple Python; the failures occur during authentication-status preparation, before inference.
These are recorded environment limitations, not passing tests or effects of the accounting change.

Preparation self-review checks authority, all selected conditions/repetitions, copied-input identities, tool restrictions, evaluation-before-prior ordering, pool separation, historical strata and unchanged source judgments.
No blocking preparation finding remains for the file-only evaluator; shell-dependent testing remains gated on the recorded Python prerequisite.

DD-VERDICT: PASS

## Packet correction and explicit retry

A post-capture configuration-derived check found missing E source inputs in both packets.
The old directory assumption is replaced by checking declared non-skill inputs against every original configuration; all remaining packets and the corrected retry pass.
Order 4 remains charged and incomplete; the owner approved exactly one corrected review from the retry pool, not a thirteenth primary slot.
The supplemental accounting projection now supports only evaluator/retry pools with the role kept evaluator.
The new retry and invalid-pool cases failed before implementation (2 failed, 8 passed), then all 10 focused ledger cases passed.
The earlier clean preparation verdict does not certify the omitted task inputs.
