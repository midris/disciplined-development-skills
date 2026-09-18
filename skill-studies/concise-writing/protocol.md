# Concise writing: study protocol

Format version: `1`
Study ID: `concise-writing`
Status: preparation draft; CW selection, intended outcomes and separation of artifact quality from process compliance are owner-accepted. Case definitions, detailed scoring boundaries and collection scope remain unfrozen.
Plan: [active testing plan](../../plans/2026-09-11-model-driven-skill-testing.md#current-next-action)
General spec: [testing framework](../../plans/specs/2026-09-11-model-driven-skill-testing-framework.md)

## Sources and intended use

Original: [checked-in skill](../../skills/concise-writing/SKILL.md), preserved as [study original](cases/skill-original/SKILL.md), from Git `99b3302f047a9b000ff804292d8746dd8bf43e42`, SHA-256 `4d12a2eb475c6b2ef57e2300c8c07af3f59c1e07b2b82695a3b7669eee1d6d72`. Complete supplied text: 860 words by `wc -w`.
Read the complete skill and its [composition map](../../ARCHITECTURE.md#composition-boundaries); relevant rationale and plan-writing companions were inspected for scope. The original snapshot matches its source bytes; it is not a new skill version.

Owner’s intended use: turn existing agent output that is verbose or voluminous into concise, clear, effective material that is easier for the owner to consume. Proposed initial scope is ordinary prose editing. This contrasts with SSR’s repository repairs and tests semantic assessment through the same session workflow.
Use standalone prose editing first. Exclude skill/reference authoring as the skill does; defer plan/spec composition, generation of new decision rationale, externally referenced anchor changes, discovery and orchestration. These cases add dependencies without being needed to test the core editing behavior. Existing rationale in supplied prose must still survive.
Old CW frameworks, fixtures, rubrics and results remain superseded and were not used to define this contract. Historical reuse, if later selected, requires revalidation under the current spec.

## Behavioral contract and consumers

Owner clarification: concision must maintain document effectiveness. Repetition is acceptable when it reinforces important points; meaningful additional prose is acceptable when it contributes explanation, emphasis or comprehension. The target is avoidable burden, not the shortest wording or minimum repetition. This agrees with the skill’s protection of useful framing and deliberate reinforcement. Readability is an intended outcome, not just a preservation check. If the input is difficult to read or poorly organized, the edit should make it easier to follow. Existing formatting, layout, section order and paragraph boundaries are not preservation requirements; improve them where they contribute to the difficulty. Preserve information and the useful effects of framing and emphasis, not their exact original presentation.

| ID | Source / obligation | Intended outcome and observable evidence |
|---|---|---|
| O1 | Core test; When NOT to cut: preserve information and necessary framing. | Final document preserves facts, qualifications, causal relationships, rationale and the useful effects of orientation, emphasis and reinforcement. Compare meaning and communicative function across the complete source and final artifact; wording, layout and placement may change. Useful repetition may remain or be expressed differently. |
| O2 | Verbosity patterns; local/global compression: remove padding at sentence and document level. | Remove wording or duplication only where its lack of useful contribution is supported by the document’s purpose and context. Evaluate the complete document’s concision without requiring every phrase to be the shortest possible. Meaningful prose and useful repetition may remain; the amount cut does not establish success. |
| O3 | Overview: a rich, easy-to-read, complete document; owner clarification makes improvement of difficult prose explicit. | The edit makes poorly organized or hard-to-follow input easier to consume while preserving already effective material. Readers can follow the reasoning and sequence, find important points and use the document without reconstructing missing connections. Reordering, grouping, headings, paragraphs, lists or explanatory transitions are available means, not required formats. Judge the result for the stated reader and purpose. |
| O4 | Compression pass; editing instructions: review locally and globally, draft first, then diff against the original. | Observed drafting and comparison against the original support the prescribed process. No separate intermediate file, three-artifact workflow or particular diff tool is required by the skill. A polished final artifact or claim of review alone does not prove the actions occurred; evidence requirements must be fixed before collection. |
| O5 | When unsure: keep potentially necessary framing and flag the uncertainty. | Where the editor remains unsure whether material is useful framing or padding, it keeps the material and flags that uncertainty. Context may resolve ambiguity; a difficult case alone does not prove the editor was unsure or require a warning. Do not infer a hidden mental state from silence. |

Consumers: the owner needs agent output that is easier to consume without loss of meaning or usefulness; the editor/reviewer uses the source-to-draft comparison to check losses. No exact output schema or downstream program consumer was identified in the inspected CW, DD, adversarial-review, rationale and plan-writing skills, architecture/README, example guidance, command directory and hook references. DD and review guidance invoke CW but do not prescribe a parser for its edited prose. This inspection does not establish that no external consumer exists. Any real case-specific interface or link dependency must be stated explicitly; do not invent layout-preservation rules for ordinary prose.
Owner decisions: select CW, govern concision by document effectiveness as clarified above, and judge the work on its own merits. Process-only defects do not overturn a successful artifact outcome. Detailed case boundaries and the collection proposal remain to be prepared.

## Assessment policy

Policy direction: owner-accepted; case-specific criteria and the policy snapshot are not yet frozen.
Proposed functional criteria cover O1–O3, with source-supported case boundaries. Judge whether the complete document is concise and maintains its effectiveness, not whether it achieves maximum compression. Loss or distortion of meaning, useful emphasis or framing fails the applicable functional criterion even if every isolated fact survives. Local differences prompt investigation; they are not independent deductions for extra words or repeated points. Different effective phrasings, structures and lengths may meet the same criteria. Assess ease of consumption from the complete document and its intended use, not counts of headings, bullets, paragraphs or repeated phrases. Preserving facts while leaving the identified reading or layout difficulty unresolved does not satisfy O3; cutting text cannot compensate for that failure.
Owner-approved policy: judge the delivered document on its merits. Record O4–O5 process observations separately; a process-only defect is visible and non-blocking when the artifact outcome succeeds. If an omission also harms the document, judge that actual outcome defect under O1–O3, without counting two failed executions. Missing process evidence remains insufficient evidence, not proof of a skipped step. Consistently good documents are acceptable even when the prescribed process is not consistently followed.
Allow different faithful edits and justified preservation. Use insufficient evidence separately from observed failure. The active session applies fixed criterion cards and labels its shared context; no separate evaluator qualification is proposed.
Use the spec’s per-case/condition aggregation, counting met, not met and insufficient evidence among valid setups and reporting excluded attempts separately. Assess consistency by case across the declared repetitions, keeping individual defects visible. Initial results are proposed as descriptive-only; the owner’s emphasis on consistency does not establish a sample size, numerical acceptance threshold or population reliability claim. No word-count target is selected.
Edited-document word counts, if reported, are descriptive only: no reduction target, repetition quota, brevity bonus or shorter-output tie-breaker. A longer effective edit can pass while a shorter damaging edit fails. This is distinct from comparing the size of skill instructions while checking preserved behavior.

## Suite and evidence

Conceptual facets only; no fixtures selected or constructed yet. One case may cover several facets.

| Case ID / definition | Membership | Covered obligations | Exposure | Limits |
|---|---|---|---|---|
| Unselected: verbose agent output with local and cross-section padding | proposed facet | O1–O4 | development | Identify avoidable burden in context; do not treat repeated wording or ideas as defects by themselves. |
| Unselected: hard-to-follow organization and layout | proposed facet | O1–O4 | development | Source-supported reading difficulty must improve; allow different effective structures and preserve helpful explanation. May share a case with verbose agent output. |
| Unselected: qualifications, rationale and useful repetition | proposed facet | O1–O5 where uncertainty exists | development | Include meaningful explanatory prose and reinforcement of important points; judge their contribution to the whole document, not mere survival of facts. |
| Unselected: already-concise text | proposed facet | O1–O4 | development | No required cut percentage; unnecessary edits may be harmful. |

Evidence will retain the complete supplied text, delivered edit and available drafting/comparison trace; the harness may capture intermediate states without requiring the subject to produce separate draft and final files. Deterministic tools may supply file/diff/word-count facts; semantic preservation and usefulness require case rules and evidence-backed judgment. No checker or reference answer is yet qualified.
Coverage excludes the compositions and discovery behavior listed above. No held-out claim is selected. Agree the facets before choosing source documents or inspecting historical scenarios.

## Execution scope and authorization

Owner selected CW on 2026-09-17: “let’s go with CW”. This authorizes study preparation, not subject calls, skill edits or adoption.
No batch, configurations, manifests, commands, run order or repetitions are selected. Propose original/no-target conditions for a contribution baseline after the contract and cases are agreed; a version comparison is a later separately scoped question.
Sol-low remains the suggested initial setting for continuity with process development; no CW model/effort is frozen. Desired Claude and effort-level follow-ups belong in the active plan and have no dispatch scope yet.
Reuse the accepted version-1 formats and existing runner/document tools. Verify changed runtime/input assumptions and evidence requirements before proposing collection; no wholesale requalification or new tooling is selected.

## Storage and accounting

Canonical checkout: `/Users/simon/work/personal/disciplined-development-skills`.
No raw bundles or attempt indexes exist. A durable absolute evidence location and recovery decision must be recorded before collection; SSR’s accepted single-host risk is not silently extended to CW.
Calls spent: zero. No CW call/time ceiling is accepted and no unused SSR allocation transfers automatically.
Current preparation booking: 10 active minutes for source inspection, original preservation, contract drafting, ambiguity review, owner clarification, verification and publication, excluding owner-wait. Before case construction, propose the preparation/collection forecast within a separate CW scope. No whole-study fit or repetition budget is claimed.

## Results and decision

No observations or batch assessments. CW’s intended outcomes and process-only policy are settled. Next: make the conceptual facets concrete in a small case proposal, with audience, purpose, acceptable alternatives and observable failure boundaries. Skill adoption remains deferred under the owner’s broader direction.
