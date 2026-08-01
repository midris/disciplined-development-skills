# disciplined-development — validation

First validation record for the parent skill. It does **not** cover the whole skill
(the gates/principles predate this file); it records the test run for each material
change, starting with the whole-repo review-scope change (2026-06-22). Add a section
per future change.

**Dispatch protocol.** Read-only and bounded per CLAUDE.md's evaluation-subagent rule
(Claude Code: `Explore`). One scenario per agent, text-only, model `sonnet`; cold-read
on `opus`. RED points subjects at a git snapshot of the pre-edit skill; GREEN points at
the live skill.

## Whole-repo review scope (2026-06-22)

**Change.** Gate 5 steps 1–2 and the mode-emphasis "Code review (giving)" row dropped
diff-scoped review (`git diff <chunk-base>..HEAD`, "chunk diff", "read the diff") for
**deep, whole-repo, plan-anchored** review; Gate 1 lost its "review the diff" framing.
The companion assertion is in `adversarial-review` (Review-angles closing line) — see
[adversarial-review.md](adversarial-review.md). Rationale: a diff-scoped review can't
see a defect of omission — a plan-mandated safeguard orphaned (zero callers) by an
earlier refactor never appears in the current chunk's diff.

**Scenario (reproducible).** Subject is at end-of-chunk; the chunk added a `--dry-run`
flag; a plan-mandated `confirm_destructive()` was orphaned three commits ago, NOT in
this chunk's diff. Asked: what scope does the self-review use, and would it surface the
orphan?
- **PASS (GREEN):** names whole-repo / plan-anchored scope; surfaces the orphan.
- **FAIL (RED):** scopes to the chunk diff; states the orphan would not surface.

**Results.**
- **RED (pre-edit snapshot, sonnet ×2; + opus ×2 excerpt):** 4/4 scoped to
  `git diff <chunk-base>..HEAD` and said the orphan would NOT surface — the
  defect-of-omission blind spot, verbatim.
- **GREEN (live skill, sonnet ×3):** 3/3 named whole-repo, plan-anchored scope and
  surfaced the orphaned `confirm_destructive()` as a P1, several citing the
  common-rationalizations table ("future gate will catch it" rejected). Clean flip; no
  refactor.

## On edits

Re-run the scope scenario (RED snapshot vs GREEN live) on any change to Gate 5's review
steps or the mode-emphasis review rows. Keep in sync with the companion assertion in
`adversarial-review` (Review-angles).

## Analysis versus implementation threshold (2026-08-01)

**Scenario.** A parser documents required `name` and optional `tags`.
Review generates absent `tags`, malformed string `tags`, and 100,000-entry `tags`; none occurred in production.
The user cites Principle 7's old "wait for the edge case to actually occur" wording to defer all three.

**Pre-edit control: 1/1 PASS.** The evaluator already derived the intended behavior from the surrounding corpus: support absent optional input, reject representable malformed input by construction, and record the ungrounded scale case as an accepted edge.
This means the edit is a clarity refactor, not a reproduced behavior fix.

**GREEN requirement.** Preserve that exact classification while making the threshold explicit: analysis must generate cases, but implementation follows only for contract requirements, reachable accepted input, observed use, or robust invariants.

**GREEN result: 3/3 PASS.** The initial evaluator and two additional independent cold repetitions preserved the pre-edit classification and cited the new threshold directly.
All three distinguished mandatory analysis from implementation, supported absent optional input by contract, rejected representable malformed input by construction, and recorded the ungrounded scale case as an accepted edge.
