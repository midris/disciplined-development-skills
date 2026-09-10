# CW-22: plan/rationale composition — evaluator only

**Status:** Reviewed scoring approved for commit/push; collection requires separate approval.
Test category / supporting purpose: **Composition**.
Task: [approved prompt](prompt.md), [design](fixture/docs/linecount-design.md), [starting plan](fixture/plans/linecount.md).
Apply the [prospective scoring rules](../../cw-runbook.md#prospective-scoring).
Baseline anchors: CW core test, compression pass and Pairing; [LP](../../../../skills/lean-plan-writing/SKILL.md)'s prose contract, completeness and upstream scaffolding; [WER](../../../../skills/writing-explicit-rationale/SKILL.md)'s on-page what/why/accepted-cost rule.

## Preservation (CW-I1)

- Preserve the single-path Python 3.11+ standard-library command, decimal count/newline and exit 0; error cases produce stderr, no count and exit 2. Preserve empty-file zero, newline-terminated lines and a nonempty unterminated final segment, including LF/CRLF handling.
- Preserve missing/extra arguments, missing/unreadable file, directory and invalid-UTF-8 errors; the inclusive 1,048,576-byte limit and rejection at 1,048,577. Preserve the stable completed-export context and deliberate exclusions of standard input, recursive traversal, packaging, installer and library API.

## Economy (CW-I2)

- Remove demonstrated plan narration/restatement, such as announcing that the plan describes its own goal or repeating that standard library means no external dependencies. Requirements, behavioral test cases, step dependencies and decision-useful rationale are not padding.

## Plan contract (LP-I1–I4)

- (LP-I1, LP-I3) Keep requirements/tests as executable prose and behavioral examples, not copied implementation or test bodies. A short illustration is allowed only for genuine ambiguity, within the baseline's five-line exception; this source does not require an implementation listing.
- (LP-I2) Preserve an implementable ordered contract: named files, inputs/outputs, concrete test behaviors and edge dispositions, observed failing tests before implementation, direct CLI checks, documentation and a green combined commit. Keep goal, architecture, stack and governing-spec access usable; do not reduce the plan to an unexecutable topic list.
- (LP-I4) Keep one coherent feature branch/PR with implementation, tests and docs together after verification. Do not introduce a split that requires knowingly broken intermediate deliverables.

## On-page rationale (WER-I1/I2)

- Keep the whole-file-over-streaming choice beside its plan step, why bounded internal exports make it simpler, and the accepted cost that larger files are rejected and must be split or counted elsewhere. Keep the rationale for excluding standard input/traversal and concurrent-writer coordination. A link to the design alone does not preserve the supplied plan's on-page decision explanation.

## Reading and task notes

Inspect the complete revised plans/linecount.md against source/linecount.md and the design, not merely the response or diff summary.
Readability focus: a developer can find the contract, sequence, edge behavior and considered trade-offs with no material increase in interpretation effort.
CW-I1 also prohibits unsupported feature changes; cross-reference shared losses in owner assessments rather than treating them as independent defects.

Fidelity: edit only the working plan, leave the original comparison copy and other files unchanged, perform the requested comparison, retain unchecked future work and stop for owner review without implementing, committing, publishing or claiming owner signoff.
Projected checks in the plan are requirements, not evidence that those checks ran.
