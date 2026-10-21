# Claude native-catalog inspection amendment

The first Claude discovery subject (global slot 121) completed and was retained with one charge.
The original inspector then rejected its setup because it expected the complete description in the live `system/init` JSON.
Claude Code 2.1.305 reports skill names in that event; its qualified model request carries the descriptions.
The mismatch is in the controller inspection, not the subject runtime, capture or skill.
No subject is repeated or excluded.

## Evidence and correction

The retained `qualification-20261021` store is pinned by inventory SHA-256 `bff2209bbd8cae12655159a74e0a3894f038ad40110b41f08857fb4a0e518a3e` in [runtime identities](runtime-identities.json).
For each description, its captured first request contains the exact assigned description and no complete body; the later request contains the complete assigned body.
The actual slot-121 startup event lists `concise-writing` and the `Skill` tool, with the pinned model and CLI.
Ordered live events read the task and numeric file and edit the number without requesting or receiving CW.
Live request payloads are not independently captured on the paid subject call; description/body separation relies on the retained qualification with matching CLI and skill bytes.
Do not describe the live init event as an observed full descriptor.

[Inspector v2](inspect_native_v2.py) preserves the original inventory, capture, identity, protected-input, body-delivery and edit-order checks.
For Claude native availability, it verifies the retained qualification inventory and [catalog contract](claude_catalog.py), then combines that proof with the actual name/tool catalog.
Codex's directly recorded descriptor check remains unchanged.
The corrected evidence check changes neither D1 nor any functional criterion.
The [original inspector](inspect_one.py) and the first subject's original manifest remain retrievable unchanged.
The two Claude discovery manifests add this controller amendment prospectively before slot 122; their subject sources, configurations, criteria, models, permissions, order and call ceiling stay unchanged.
Slot 121 retains its original invocation and manifest pins and is assessed through a read-only replay of its retained evidence.

## Verification

The original inspector fails replay of the completed slot with `exact native descriptor absent`.
The corrected inspector passes that same replay without a model call or subject modification.
[Seven offline cases](inspection-tests/test_claude_catalog.py) accept name-only init with qualified payloads and reject missing catalog name/tool, wrong description, initially exposed body, incomplete loaded body and empty qualification.
All three retained description qualifications are replayed against their exact assigned skill bytes.
The execution result cites the qualification request artifact alongside live trace/log evidence.
The protocol owns current progress and accounting; this amendment authorizes no new calls, replacements or criteria changes.

The complete runner check produced 477 passes and six Claude setup failures, both inside and outside the outer sandbox.
The separate non-process-smoke selection passes 332 cases with 151 deselected; among those 151 process-smoke cases, 145 passed and six failed.
Those six are the four declared-skill-input variants in `tests/process_smoke/test_cli.py` plus the dummy-provider-policy and child-policy cases in `tests/process_smoke/test_runtime.py`.
Their fake executable chooses `python3` only from `/opt/homebrew/bin:/usr/bin:/bin`; this host has versioned Homebrew Python but no `/opt/homebrew/bin/python3`, so the fake uses Apple's launcher.
A controlled fake-only replay produces `xcrun_db` cache-write warnings under the child policy, contaminating the status channel before JSON authentication parsing.
No runner source changed in this amendment; this host-dependent smoke prerequisite is tracked separately in the active plan.
The real subjects use the already qualified absolute Homebrew toolchain and Claude binary; their fifteen zero-model qualification checks and the completed paid call remain valid.
Do not report the complete runner suite as green or widen subject read/write permissions to silence the fake's warnings.

The [verification record](native-inspection-amendment.json) pins the retained red/green replay logs, seven-case checks, full-suite failures and source snapshots.
