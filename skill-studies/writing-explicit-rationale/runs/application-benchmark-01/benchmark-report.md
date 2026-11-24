# Shipped WER application benchmark

All 104 scheduled subjects ran once. The [Codex assessment](codex-assessment.md) and [Claude assessment](claude-assessment.md) include every attempt and criterion. The [individual records](assessment.json) link the retained evidence and active assessor's reconciliation. Two Codex catalog setups were invalid, one per condition. No replacements were used.

## What changed in the finished work

Cells show outputs meeting every functional criterion / valid outputs. Each case received two or five repetitions per provider and condition. These counts measure explicit application on seven known development fixtures. They do not estimate population reliability or native selection.

| Case | Codex shipped | Codex control | Claude shipped | Claude control |
|---|---:|---:|---:|---:|
| Export deferral | 5/5 | 4/5 | 5/5 | 5/5 |
| Quota grace | 5/5 | 0/5 | 5/5 | 0/5 |
| Repeated review | 4/5 | 0/5 | 5/5 | 0/5 |
| Catalog review | 4/4 | 2/4 | 5/5 | 3/5 |
| Helper rename | 2/2 | 2/2 | 2/2 | 2/2 |
| Scope trim | 1/2 | 1/2 | 2/2 | 2/2 |
| Dispatch hold | 2/2 | 2/2 | 2/2 | 2/2 |

- **Quota grace.** Every implementation passed the behavioral checks. All ten shipped projects explained why immediately tightening a downgrade could reject already-admitted work and why brief extra quota was acceptable. All ten controls made the timing recoverable but omitted the reason for honoring the older token.
- **Repeated review.** All 20 subjects received the quota reason in the submitted commit. All ten shipped projects explained the reviewed interactive guard in the tree. Nine also repaired the independent quota decision. Shipped Codex slot 65 handled the guard well, but left the quota reason in the commit. None of the ten controls made either rationale adequately recoverable in the project. Some wrote an accurate reply; others moved the check to persistence and kept approved batches working. All passed the functional replays. A future maintainer would still need external history.
- **Catalog.** All valid outputs handled lender credit and amendment authority. All nine valid shipped specs and five of nine controls explained why the proof desk needed accession order. Four controls left only the ordering rule in the project.
- **Export.** Most concise controls worked. The v1 and Later sections usually made the customer wait clear, even with no explicit statement about timing. Codex control slot 91 kept XML under Version 1, where stable partner approval could be read as a gate on v1 scope. Several shipped handoffs predicted breakage on every schema revision. Compatibility risk supports the decision to defer, but certainty overstates the source.
- **Restraint and scope.** Both arms preserved the existing billing rationale in the routine rename and performed the dispatch change correctly. Some dispatch explanations repeated information already recoverable from the specification. Codex shipped slot 23 and control slot 51 both turned the Monday handoff into a Monday launch. That error changes the schedule while leaving the Finance decision and conditional Support work intelligible.

## What an independent reader did

All 18 eligible readers told the printer to retain accession order for the next proof. All 14 readers whose spec explained the production dependency used it in their reasoning and could point to the existing title index. That includes 9/9 shipped readers and 5/9 control readers. The remaining four control readers had the correct order on the page but lacked its reason. Three recognized missing context and recommended checking before changing it. One deferred to owner approval without asking what relied on the order. The readers had the same immediate recommendation across conditions; what differed was whether they could justify it from the project and evaluate a future change. The [reader decisions](decision-readings.json) record borderline interpretations individually.

## Codex tool availability

The first 22 Codex subjects could discover account apps. Slots 41 and 43 used host connectors and were excluded. The final 30 Codex subjects ran with apps disabled. All 61 resumed subjects passed the revised exposure and tool-use audit. The [isolation checkpoint](checkpoint.md) and [qualification](connector-qualification.json) document the boundary and inventory. Claude used one configuration throughout. The phases occurred in schedule order, so a difference between phases cannot establish a tool-availability effect.

| Codex case | Apps enabled, shipped | Apps enabled, control | Apps disabled, shipped | Apps disabled, control |
|---|---:|---:|---:|---:|
| Export deferral | 2/2 | 2/2 | 3/3 | 2/3 |
| Quota grace | 2/2 | 0/2 | 3/3 | 0/3 |
| Repeated review | 2/2 | 0/2 | 2/3 | 0/3 |
| Catalog review | 1/1 | 0/1 | 3/3 | 2/3 |
| Helper rename | 1/1 | 1/1 | 1/1 | 1/1 |
| Scope trim | 0/1 | 1/1 | 1/1 | 0/1 |
| Dispatch hold | 1/1 | 1/1 | 1/1 | 1/1 |

## Independent review and decisions for the owner

Fourteen fresh Claude Opus 5.5 medium reviewers assessed all 104 labeled artifacts, one group per case and subject provider. They saw the task, complete project and handoff, applicable criteria, diff, replay output and eligible reader answers. The two invalid artifacts received descriptive review only. The [comparison](cross-model-comparison.json) retains every independent grade separately from the active grades. The [evaluator ledger](evaluator-run-index.json) links the full raw answers. All 32 evaluator sessions completed in one turn with zero tool calls.

Of 270 criterion judgments on valid subjects, 264 agreed. The six differences affect six outputs. Applying the independent grades yields 50/51 shipped and 22/51 controls meeting every criterion. Applying the active grades yields 49/51 and 25/51. These are paired interpretations of the same executions.

1. **Four Claude control export plans** (slots 2, 32, 76 and 90). The independent reviewer wanted an explicit connection from the v1 item to XML's deferral and an explicit customer wait. The active assessment credited each complete plan: v1 lists CSV and JSON, Later lists XML, and the partner must approve a stable schema. The handoffs confirmed the intended scope. I recommend keeping these passes under the agreed materiality rule. Both assessors failed Codex slot 91, where XML actually remained under Version 1.
2. **Two Codex scope-trim plans** (slots 23 and 51, one per arm). Both assessments identified the unsupported “Monday launch” heading. Claude treated it as a caveat because the deliverables and Finance dependency survived. I recommend retaining the task-fidelity misses because Operations could schedule the rollout for the day that was supplied only for handoff. Both assessments credited the rationale.
3. **One catalog reader** (label 369b819a). Both assessments agreed that the reader kept accession order and the project did not supply the proof dependency. The independent reviewer narrowly credited the escalation as sound handling of missing context. I scored the decision unsupported because the reader would accept owner approval without asking what depends on the order. This changes the assessment of follow-up quality only.

The quota and repeated-review results agree across assessors. Several reviewers correctly noted that the two mechanical-check outputs were not named in their packets. The private replay and original tests were both run and retained; the identical terse test output obscured their provenance for independent review. In a subsequent assessment, attach the check name alongside its output. Similarly, the repeated-review packet recorded delivery of the commit paragraph but did not include a raw process trace. Claims about the subject's search process are consequently weaker than claims about the rationale present in its final files.

The active assessor is Codex and the cross-model reviewers are Claude, so the latter share a model family with Claude subjects. Opaque labels concealed assigned conditions, but several handoffs name GUIDANCE.md or identify Claude Code. Provider-shaped wording and temporary file paths were also visible. Whole-output assessment and the fixed replays reduce some interpretation risk; the independent reviews do not constitute fully blinded replication. Raw bundles and private evidence are retained on one host.

The clearest benchmark for a future rewrite is whether a reader can recover the reason for the quota exception and both decisions in repeated review, while ordinary renames stay simple. The catalog exercise independently supports a benefit in grounded reasoning. The immediate printer instruction was identical across arms. Review the three judgment boundaries above before using this benchmark to compare candidates.
