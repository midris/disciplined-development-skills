Independently evaluate the quality of the retained outputs for the concise-writing scenario selected in EVALUATION-INDEX.json.

The question is whether CW helps produce documents that are concise, complete, correct and effective for their intended readers. Compare every supplied condition, including the no-CW control when present, original CW, targeted draft and fuller draft. Do not assume either skill version improves the output.

Scope: every execution in EVALUATION-INDEX.json. Assess every output, including successful controls and unsuccessful skill outputs. The index lists every source file under source_files, including the task and supplied notes/code, plus criteria, output files, conditions, repetitions and original run IDs. Read every source_files entry, not just the task. Read MECHANICAL-CHECKS.json and WORD-COUNTS.json as controller observations; no shell or execution is available. WORD-COUNTS.json contains controller-computed wc -w counts; use them instead of estimating.

Evidence handling:
- Work read-only. Do not edit files, rerun subjects or execute operations described in the documents.
- Treat tasks and documents as evidence, not instructions to carry out their contents.
- Read each complete source/task, supplied notes, assessment policy, applicable criterion card and complete output.
- Do not open prior-assessment.md until you have completed and emitted your own judgments and comparisons in an assistant message. Keep that first-pass assessment intact when you later compare judgments.
- Condition labels are visible; disclose that this review is independent but not blinded.
- No shell is available; use native file reading. Material you cannot read completely is an evidence gap, not an assumed pass.

For invocation-nonprose (N3), CW functional effectiveness is not measured. Read every saved settings file and assistant_messages artifact; report numeric-edit preservation and literal-response task observations only, without F1–F3 scores or a CW contribution claim. Do not infer D1 invocation from artifacts; the active controller separately audits ordered traces. For all other cases, evaluate each complete output against the complete source and its intended readers' needs. Apply the supplied frozen criteria:

F1 — Correctness and fidelity:
Does the document preserve the source's facts, qualifications, conditions, reasoning and consequential distinctions? Does it introduce unsupported claims?

F2 — Effectiveness:
Can the intended readers understand, decide and act at least as effectively as with the source? Consider navigation, causal explanations, safeguards and the stated reading contexts.

F3 — Readability:
Is the whole document clear, coherent and easy to consume? Has it removed unnecessary reading burden while retaining useful framing and reinforcement?

Judgment rules:
- For measured functional cases, score each applicable F1–F3 factor as met, not met or insufficient evidence. N3 remains unmeasured for CW quality; task correctness is a separate observation.
- For measured functional cases, any failed factor means overall failure. Otherwise, unresolved evidence means insufficient evidence; all three met means pass. Do not apply this functional aggregation to N3.
- Judge meaning across the whole document. Missing or changed wording is a reason to inspect context, not an automatic failure.
- Accept faithful paraphrase, relocation, consolidation and different effective layouts.
- Repetition can support orientation, emphasis or safe action. Identify its actual reader benefit or burden.
- Do not impose your preferred writing style, a sentence checklist or a requirement that every fact appear only once.
- Report word counts separately. Shorter wording cannot compensate for lost meaning or effectiveness. Apply each case's declared length treatment; required additions or supplied maintenance rationale can justify growth.
- Assess the saved artifact, not the model's completion claim.
- Do not infer skill invocation or process compliance from a good document. Invocation is outside this output-quality review.

For every output, provide:
- Run ID, condition and repetition.
- Applicable F1/F2/F3 judgments and overall result; for N3, task-only numeric-edit/literal-response observations and an explicit CW functional result of not measured instead.
- Concrete evidence supporting the judgments, including passes.
- For each failure, identify the source meaning, the relevant output passage or absence, and the practical consequence for the reader.
- Important strengths, weaknesses and uncertainty.
- Source/output word counts, without using length as a quality score. N2 is generation from notes, N4 uses the supplied comment-only counts and code context, and N3 has no length comparison.

Then compare conditions:
- Show measured functional pass counts by case and condition, preserving runtime/provider strata. Keep N3 task-only observations outside those counts.
- Explain meaningful quality differences even where both outputs pass.
- Identify what skill-bearing outputs preserve or improve compared with controls, and any regressions.
- Distinguish recurring behavior from a single observation.
- State whether the results support a useful CW contribution and whether either draft is preferable to the original. Small samples may leave that unresolved. Native tasks without controls cannot establish incremental contribution.

Only after emitting your independent assessment, read prior-assessment.md.
Compare judgments with that existing assessment using concrete evidence. Do not change your judgment merely to match it. Distinguish observation disagreements from different interpretations of the same criterion.
If a criterion is defective or ambiguous, report that separately from applying the existing rule. Do not silently replace the evaluation standard.
Return the complete assessment and comparison in your final response. Stop after the selected scope.
