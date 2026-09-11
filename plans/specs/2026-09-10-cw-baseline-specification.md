# Concise writing: baseline behavioral specification

**Status:** Reviewed against the complete existing skill; the owner authorized proceeding to catalog evaluation under this specification.
This specifies what the current skill promises; it does not establish that the skill works, approve a rewrite or authorize test collection.
The [active testing plan](../2026-09-09-dd-skill-testing.md) owns next steps; the [existing catalog](../../skill-validation/pilot/cw-catalog.md#baseline-specification-alignment) owns test mapping and reconciliation.

## Sources and authority

The [charter](../../skill-validation/charter/core-contracts.md#concise-writing) supplies the core purpose: remove prose that adds no value while preserving reader understanding and use.
The full [baseline skill](../../skills/concise-writing/SKILL.md) supplies the specific scope, rules, exceptions, method and responsibility boundaries.
Read them together; neither the short charter nor the skill's individual slogans substitute for the complete skill.

Baseline source: `skills/concise-writing/SKILL.md` at repository revision `76b520cc581afed49135b95c874c6a6c02403d26`.
SHA-256: `4d12a2eb475c6b2ef57e2300c8c07af3f59c1e07b2b82695a3b7669eee1d6d72`.
These are also the CW bytes supplied to the latest current-DD observations; later changes to the linked file do not silently change this specification's source.
The existing candidate supplies no requirements to this specification.

The owner clarified that effectiveness is judged across the complete artifact and that repetition may provide emphasis or retention without adding facts.
Those clarifications agree with the baseline's overview, whole-artifact pass and anti-over-trimming rules.
An earlier target requiring CW not to trigger on detailed responses is absent from this baseline; its exclusion of skill/reference authoring must also remain explicit.
Different desired behavior belongs in a separately approved specification change, not a baseline failure invented by a rubric.

## Intended outcome

Produce a rich, complete, easy-to-read artifact with unnecessary prose removed.
Preserve the intended information, relationships, conditions, rationale and framing that help its reader understand and act correctly.
Judge information in the context of the whole document and its intended use, rather than requiring every sentence to repeat its context.
Reduction in word count is neither a requirement nor sufficient evidence of success.
An already-effective passage can remain unchanged; a useful explanation can remain detailed.

Read the core test's “necessary framing” alongside the overview's “any framing that aids comprehension”: framing need not be indispensable to be useful.
Orientation, transitions and reinforcement can improve reading even when the facts or headings overlap with them.
Removability, lack of a new fact, introductory placement or resemblance to a named verbosity pattern does not by itself establish padding.
Assess the passage's reader function in the whole artifact; the [shared padding-failure check](../../skill-validation/pilot/cw-runbook.md#padding-failure-check) makes that distinction explicit for evaluators.

## Behavioral requirements from the baseline

| Baseline source | Required behavior | Observable assessment |
|---|---|---|
| Description; Role; Overview | Apply to reader-facing prose at risk of verbosity, including docs, plans, specs, design notes, commit bodies and comments, and explicit tightening requests. The description excludes skill and reference authoring. | Discovery evaluates selection/body access in a task that fits the declared scope; an explicit load tests loaded behavior rather than spontaneous discovery. Do not infer a detailed-response exclusion. |
| Core test; When NOT to cut | Remove wording that carries neither information nor useful framing; preserve either when present. | Compare source and deliverable for information and reader function. Identify what is lost or what adds no value; a possible alternative edit alone is not a failure. |
| Compression pass | Before finalizing durable prose, check local wording and the complete artifact for verbosity; adding prose requires the whole-artifact pass. | Inspect local passages and distant sections together. Removing local padding while leaving demonstrated whole-document waste does not satisfy this requirement; output alone does not prove the internal pass occurred. |
| Meta-framing | Remove narration that merely announces what a self-explanatory document or section does. | Fail content-free announcements; retain orientation that helps readers understand the document's scope or progression, even when headings convey the same facts. |
| Say-it-twice; Cross-section duplication | Remove accidental restatement that serves no purpose. | Repetition is a candidate for inspection, not automatic failure. Explain why it lacks information and useful framing before classifying it as padding. |
| Over-sectioning | Avoid unnecessary subdivisions and lead-ins that add bulk without helping the reader. | Assess navigation and reading effort; there is no maximum heading count or mandated layout. |
| Unrequested elaboration | Avoid unsupported advice or inference added merely to seem thorough. | Distinguish grounded explanation and necessary framing from invented policy, promises, actions or details. |
| Emphasis/hedge inflation | Remove empty intensifiers, duplicated descriptors and scattered emphasis. | Evaluate their function in context; no forbidden-word list or blanket prohibition on emphasis follows. |
| When NOT to cut | Preserve useful recaps, navigation, deliberate reinforcement, orienting transitions, rationale and completeness. | Repetition is allowed when it improves clarity, readability or effectiveness for the intended reader, even without a new fact, example or action. Preserve these functions where needed; do not mechanically demand their original placement or wording. |
| Existing-text editing instruction | Draft and compare the revision with its source so meaning is not lost. | The retained source/output comparison can establish conservation. A final answer alone cannot prove an unobserved internal comparison; do not manufacture a process failure or demand an unsolicited intermediate draft. |
| Uncertainty instruction | Keep and flag wording when unsure whether it supplies framing or padding. | If uncertainty is expressed, check its disposition. Do not infer subject uncertainty from evaluator disagreement, or treat uncertain evaluator classification as proof of padding. |
| Owns / Does not own; Pairing | Own prose concision while preserving plan completeness, rationale and reference integrity governed by the named companions. | In composition cases, attribute each responsibility to its owner. Pairing does not demand loading every companion for every prose task or transfer its responsibilities to CW. |

The detailed-response case tests whether useful requested explanation survives, because completeness and comprehension apply to detailed prose too.
The skill does not promise never to use CW for such a response.
Likewise, testing a warning revision after an explicit CW-loading instruction does not prove that baseline CW should discover itself for otherwise-excluded authoring.

## Test design after specification and catalog review

The [intended-use and authoring guidance](../../skill-validation/README.md#intended-use-and-dependencies) places development projects first, with representative broader use and Superpowers available.
For CW, cover ordinary prose use without requiring the DD orchestrator, plus its contribution to DD-guided project tasks with the relevant companions.
Superpowers writing-skills governs how CW itself is edited and validated; it does not override CW's existing exclusion of skill/reference authoring in subject tasks.

First review this specification against the complete baseline skill, then reevaluate the full CW catalog and address coverage gaps or unnecessary overlap.
Only after those steps are settled should scoring criteria be finalized; the following retains the existing category and evidence boundaries rather than approving new rubric details.

Use the existing categories and worksheet ledgers.
For each assessment group, identify its baseline section, applicable charter invariants, scenario-specific reader needs and observable success/failure boundary.
Use source facts as checks within that result, not a separate score per fact; grouping does not relax any requirement.
Keep this mapping in the existing catalog or rubric; no additional tracking system is needed.

- **Discoverability:** does the agent find and load the skill where its actual scope calls for it, with the declared provider's qualified access mechanism?
- **Effectiveness:** when loaded, does the output fulfill the baseline promises on the concrete task? Assess conservation, removal of demonstrated waste and readability together, allowing useful repetition.
- **Composition:** does CW perform its contribution while respecting the actual responsibilities of relevant companions? Read those dependencies before specifying their criteria; skill-name recall is insufficient evidence.

For CW, record readability gains, equivalence or degradation with concrete evidence rather than awarding a pass simply because nothing is blatantly wrong.
Materially worse comprehension or use is a semantic loss; record the same consequence only once, with comparative evidence in the readability ledger.
Task-only narration and shape issues remain fidelity unless they prevent judgment; no deterministic protocol applies without a real consumer requirement.

Passing a task with CW loaded establishes observed task success, not that CW caused it.
Use meaningful no-DD controls to assess added benefit; retain ordinary control passes and disclose the supplied surrounding skills.
Treat observations as evidence about the selected model, task and context, not a universal reliability estimate.

## Establishing the baseline and judging rewrites

Review this extraction first, evaluate the full CW catalog and address its gaps, then reconcile prompts and scoring before deciding what collection is needed.
The existing tests and retained observations can inform that work; they are not automatically a completed baseline under this specification.
Preserve the original 99/66-run comparison and the latest observations with their successive judgments; record mismatches rather than rewriting history.

Once specification, scenario inputs and scoring are agreed, freeze them together with the baseline skill bytes and record matching observations.
Judge a later rewrite against the same agreed promises and comparison conditions.
If a new behavior is desired, explicitly revise the specification and affected tests before measuring that change; do not redefine success to fit the candidate's output.

The [catalog audit](../../skill-validation/pilot/cw-catalog.md#routine-suite-coverage) now identifies the proposed repairs, retirements and additions.
The [resulting task inputs](../../skill-validation/pilot/cw-catalog.md#prospective-input-map) have completed review and remediation, with owner authorization to commit/push; [reviewed scoring](../../skill-validation/pilot/cw-runbook.md#prospective-scoring) is also approved for commit/push.
The [active testing plan](../2026-09-09-dd-skill-testing.md#current-scoring-preparation) records collection results, owner decisions and the next batch; this specification does not track execution status.
Other skills and new provider calls are not activated by this specification.
