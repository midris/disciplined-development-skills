# CW cross-model evaluation procedure and execution review

The [protocol](../skill-studies/concise-writing/protocol.md) owns completion, decisions and accounting.
The [method](../skill-studies/concise-writing/evaluation/README.md), [assessment](../skill-studies/concise-writing/evaluation/assessment.md) and [ledger](../skill-studies/concise-writing/evaluation/evaluator-run-index.json) preserve supplemental judgments and provenance.
This is the controller’s self-review, not an additional independent code-review invocation or an adoption verdict.

## Scope and boundaries

The owner selected all 136 completed CW outputs before evaluator outcomes: 120 expanded and sixteen historical.
The twelve primary groups and one explicitly approved retry consume twelve evaluator and one retry slot, with no subject/authoring calls or pool transfer.
The manual owner-supplied review remains outside controller dispatch accounting.
The retrospective includes every selected condition and repetition, with 124 functional outputs and twelve procedural-only N3 outputs.
Historical contribution and comparison batches remain separate, as do their Codex 0.154.0 runtime, expanded Codex 0.157.1 and Claude Sonnet strata.
The active assessor is GPT; Claude Fable is an independent second-model judge relative to that assessor, while sharing a family with Claude subjects.
Visible labels prevent a blinded claim, and exposed development cases prevent a held-out claim.

All thirteen real captures confirm Claude CLI 2.1.301 and claude-fable-5-1, with medium effort requested in the fixed configurations and command settings.
A scripted local endpoint separately verified Fable alias resolution, the medium request and native Read delivery with zero inference.
Only Read, Glob and Grep are available under the verified read-only OS policy; no skills, Bash, edit tools, MCP or fallback model are enabled.
Every protected fixture still matches its configured source.
All raw capture inventories match, all selected outputs were delivered completely, and emitted first-pass judgments precede prior-content access.
Read/Grep access was checked; filename-only discovery is not treated as exposure to prior scores.
N3 observations are task-only, including collective reporting in the Codex native review; invocation is never inferred from artifact quality.

## Packet defect and correction

The directory-based packet builder missed E’s aliased source report and new notes in both provider packets.
The original Codex E review correctly returned insufficient evidence for all nine F1/F2 judgments; its F3 judgments, raw evidence, input inventory and charge remain intact.
Its read-order audit establishes delivery of declared inputs, not completeness of the task inputs.
The controller stopped dispatch and checked the entire packet class against every non-skill fixture declared in the original subject configurations.
Only the two E packets were deficient; all other packets pass.
The corrected packets were inventoried and committed before dispatch, without modifying the original private preparation store.
Claude E had not been dispatched; Codex E received exactly the owner-approved retry, independently reviewing the same nine subject outputs.
The new checker still rejects the retained bad packet, while every final packet passes.
This closes the preparation defect without overwriting or silently replacing observations.

## Supplemental accounting change

The linked version-1 evaluator ledger counts review calls without manufacturing subject execution results.
Rows retain the evaluator role; optional allocation_pool selects evaluator or explicitly authorized retry, defaulting to evaluator.
Tests reject booleans, invalid roles/IDs/pools, malformed pool/list shapes, duplicate IDs, unknown versions and mixed subject/evaluator formats.
The valid-retry and invalid-pool cases failed before implementation; a malformed-pool case also reproduced its wrong diagnostic before the final correction.
All eleven focused ledger cases pass afterward.
The projection does not establish semantic validity, owner consent or adequate evidence by itself.
No provider runtime or live skill changed.

## Evidence interpretation

The completed reviews preserve the active assessments and independent first-pass judgments separately.
Fable passes every complete functional output while repeatedly flagging the same omissions, repetition and unsupported claims identified by the active assessor.
The assessment distinguishes reasonable readability-threshold disagreement from missing recording actions and unsupported evidence claims; it does not accept the reviewer’s defenses or causal language automatically.
Equal pass counts do not establish equivalent consequential quality, skill contribution or population reliability.
The shorter-SKILL.md preference applies only after equivalence is supported.
Existing D1 outcomes remain unchanged and are required context for any adoption decision.
The owner’s next decision concerns coverage, consequential disagreements and a CW editing objective; no edit or adoption is claimed.

## Verification and limitations

All 136 original subject bundles and all thirteen review bundles match their inventories; the three preparation stores also match.
All sixteen existing CW/SSR batch-readiness checks pass, including cross-study accounting.
The original skills, case inputs, canonical results and assessment policy are unchanged from a8ae018.
Final runner suite: 477 passed and six unchanged surrogate Claude process-smoke failures; focused ledger tests: eleven passed; unit suite excluding process smokes: 332 passed.
Hook suite: 263 passed, three environment skips.
The full-suite failures are:

- tests/process_smoke/test_cli.py::test_claude_same_cli_bundle_and_worksheet_with_declared_skill_inputs[no-dd]
- tests/process_smoke/test_cli.py::test_claude_same_cli_bundle_and_worksheet_with_declared_skill_inputs[a]
- tests/process_smoke/test_cli.py::test_claude_same_cli_bundle_and_worksheet_with_declared_skill_inputs[b]
- tests/process_smoke/test_cli.py::test_claude_same_cli_bundle_and_worksheet_with_declared_skill_inputs[composition]
- tests/process_smoke/test_runtime.py::test_claude_dummy_provider_uses_policy_fixture_git_and_raw_trace
- tests/process_smoke/test_runtime.py::test_claude_child_policy_denies_surrogate_semantic_reads_and_home_writes

These surrogate executables fall back to Apple Python because the prepared Homebrew Python path is absent, failing authentication-status preparation before inference.
The original actual-CLI shell probes also fail on that missing prerequisite; no new CLI regression is established.
The separate native-reader qualification and shared isolation/mutation-denial probes pass.
No host Python installation, sandbox widening or new shell-dependent subject testing was performed.
The active plan retains the supported-Python prerequisite for that work.

Self-review enumerated all groups, conditions, repetitions, input aliases, allocations, read/assessment ordering, identities, retained inventories and applicable score denominators.
The packet defect and accounting edge are resolved across their classes; interpretive disagreements remain disclosed for the owner.
No blocking finding remains in this evidence package; the environment limitations above remain outside this native-reader scope.

DD-VERDICT: PASS
