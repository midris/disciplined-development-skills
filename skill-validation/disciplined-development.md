# disciplined-development — validation

First validation record for the parent skill. It does **not** cover the whole skill
(the gates/principles predate this file); it records the test run for each material
change, starting with the whole-repo review-scope change (2026-06-22). Add a section
per future change.

**Historical dispatch protocol (2026-06-22).** The original records below used
Claude Code `Explore`, one text-only scenario per agent, `sonnet` for scenario runs,
and `opus` for cold reads. RED pointed at a git snapshot and GREEN at the then-live
skill. This protocol is preserved as history; current and future runs follow the
immutable-bundle, Sol-high protocol in [the shared validation protocol](README.md).

## Parent-plus-companion discovery target (2026-08-01)

**Approved behavior.** When available for development work, the parent loads together with every applicable companion.
The control description named overlapping development triggers but did not state co-selection or explicitly name reviewing and development research.

**Watched REDs.** In the final shared all-nine description-only control arm, control
omitted the parent in `DISC-01` 4/5, `DISC-03` 4/5, `DISC-05` 5/5, and `DISC-06` 1/5.
The specific companion still routed 5/5 in each cell.

**GREEN.** The approved frontmatter-only change makes availability, co-selection, reviewing, and development research explicit.
Its immutable target bundle has content-manifest SHA-256 `52fd9eb8c411fcc5d42bfa4590992914c2f7a20a494f6dc7868f82c85691103b` and the changed file has SHA-256 `21a46fb9b80cf29862a5e8ee5953fc6a3b3271da044eca60ac75b7060f43562e`.
All nine shared discovery scenarios passed 5/5 on fresh Sol-high evaluators after the
final rubric repair and compact-wording restart. The first compact arm's broad
`project/external research` phrase caused one prohibited research co-selection in
`DISC-01`; restoring the action-specific research trigger produced the active 45/45
result. Exact prompts, rubrics, control results, and target summaries are in
[skill-discovery.md](skill-discovery.md).

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

## Trigger-only description routing (2026-08-01)

**Historical result, superseded for ordinary development documentation by the
parent-plus-companion target above.** The former SKILL.md-authoring negative is
retained only as historical evidence; current routing follows the target above.

**Matrix.** Route five prompts from metadata only: active-plan implementation with delegation; padded README tightening; SKILL.md shortening; plan deferral with PR-only rationale; and a routine convention-preserving rename.

**Pre-edit control: 3/3 PASS.** All evaluators triggered `disciplined-development` for implementation and plan editing, and did not rely on it for ordinary prose tightening or skill authoring alone.
The description edit is a trigger-only clarity refactor, not a routing fix.

**GREEN requirements.** Preserve the matrix while removing workflow summaries from the description and retaining session, development-work, plan, delegation, verification, commit, review, PR, and completion-boundary triggers.

**GREEN result at the time: 3/3 PASS.** All three independent metadata-only evaluators preserved the then-expected routing across all five prompts.
