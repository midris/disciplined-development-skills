# CW cross-model output evaluation

The [protocol](../protocol.md) owns current state, charges and decisions.
The [framework](../../../plans/specs/2026-09-11-model-driven-skill-testing-framework.md#cross-model-output-review) now requires cross-model review at baseline/comparison decision boundaries.
This record preserves supplemental judgments; original subject observations, scores and assessment pins remain unchanged.

## Authority and scope

On 2026-10-17 the owner requested adding cross-model output evaluation to the procedure and evaluating completed tests through a controller-started Claude session.
The owner identified the manual evaluator as Fable at medium effort and confirmed that equivalent effectiveness should favor the shorter SKILL.md, rather than shorter generated documents.
The owner selected CW only, including its 120 expanded and 16 historical outputs; SSR evaluation is deferred until its rewrite.
The [schedule](schedule.json) fixes twelve evaluator sessions covering all 136 outputs, with historical runtime strata kept separate.
Start with the nine-output Codex long-handoff review to compare the controller-started evaluation with the owner's manual one.
Use at most two concurrent evaluator sessions after this first transport/coverage check; the active controller retains and verifies every result and stops dispatch on a fault.
The [remaining-input manifest](retrospective-inputs.json) pins the other eleven packets before their dispatch.
Use the existing twelve-invocation evaluator ceiling, with zero automatic retry or subject-call transfer.
The manual Claude review was supplied by the owner, outside controller-dispatched accounting; model/effort are owner-reported, not trace-verified.
Do not count that review as an additional subject repetition or a controller evaluator invocation.

## Evaluation method

Use the same substantive prompt supplied for the manual review: full source/task, frozen F1–F3 criteria, every condition/repetition, evidence-backed pass and failure reasons, qualitative comparisons and length as a separate observation.
The isolated copy changes filesystem locations and supplies controller-computed wc counts because shell tools are unavailable.
Require judgments before reading prior scores, then compare with the existing batch assessment.
Audit ordered reads and intermediate output; report early exposure or missing first-pass evidence as a limitation.
Condition labels are visible; this is not blind or held-out evaluation.
Do not supply the manual Claude review or the active session's response to the evaluator.
Sources, outputs, rules, label map and prior-assessment copy are explicitly inventoried and hashed.
The original evidence bundles are read by the controller only; the evaluator receives regular-file copies, never their .git directories or writable aliases.
The model returns its assessment through stdout/final output; controller-owned capture is the only durable output writer.

## Execution boundary

Reuse the existing ClaudeRuntime read-only OS policy and process lifecycle; narrow the CLI tools to Read, Glob and Grep and disable slash commands.
No Bash, Skill, Write, Edit, MCP, fallback model, inherited project guidance or automatic retry is available.
This is a declared evaluator-specific CLI composition, not a change to the subject runner or historical runtime.
The CLI is 2.1.301; the local scripted endpoint resolves alias fable to claude-fable-5-1 and captures output_config.effort=medium.
Production runs must request claude-fable-5-1 and medium explicitly and verify init/assistant model identity before accepting a review.
No immutable backend revision is claimed.
Every attempted invocation consumes one evaluator slot even if incomplete; stop for identity, capture, preservation or boundary faults.

## Qualification and limitations

Five existing zero-model checks produced three passes and two failures on the new CLI.
The shared isolation checks in both modes and the read-only mutation-denial check pass.
Both actual-CLI shell/Skill probes fail: Bash selects /usr/bin/python3 3.9.6 instead of prepared Homebrew Python and emits xcrun cache-denial messages.
The host no longer has /opt/homebrew/bin/python3, so even explicit Homebrew-first lookup selects Apple Python.
This establishes a missing runtime prerequisite, not a new CLI shell regression; restore and qualify Python 3.11+ before shell-dependent subject work.
No shell-dependent subject pass is authorized by this evaluation.
Evidence: /private/tmp/cw-evaluation-preflight-20261017/.

A separate actual-CLI scripted native-Read test passes under the same read-only OS policy, with no inference.
It verifies full declared-file delivery, no Bash/Write/Edit tools, no skills, the medium setting and Fable resolution; network is confined to its local scripted endpoint.
The test is a controller scratch derivative of acceptance/test_claude_cli.py; its exact source is retained with qualification evidence.
Evidence: /private/tmp/cw-evaluation-reader-preflight-20261017/.
Durable copies and inventories are recorded in the evaluator input manifest before dispatch.

The isolated tool surface differs from the owner's ordinary interactive Claude session, so a result is a reproduction under declared conditions, not an exact session replica.
This evaluation adds a different model's judgment, not a reader study or a statistical reliability estimate.

The twelve evaluator sessions are one diagnostic judgment per declared group, not three evaluator repetitions or an estimate of judge reliability.
The owner’s three-repetition minimum applies to the subject observations; this review includes all those repetitions without recollecting them.
