# Deferred: add a `safe-by-accident` review angle to `adversarial-review`

**Status:** **SUPERSEDED (2026-06-26)** — merged into `plans/deferred/2026-06-26-generative-unexercised-cases-baseline-rule-deferred.md`. Do NOT implement this as a standalone angle: its content (the stated/local/robust/symmetric grading, the false-positive autopsy trigger, the rationalization rows + red-flags, and the readiness-continuation RED case) becomes the **invariant face** of the generative "Generate the unexercised cases" BASELINE rule — an earlier, narrower reach at the same "a green test proves the case it ran, not robustness" insight. The notes below are retained as the source material the implementer folds in.

_(Original status: Deferred, captured 2026-06-24. Implementation happens in the **`disciplined-development-skills` repo**, not meeting-pipeline — this file is the capture point.)_

**Governing skills for the implementer:** `superpowers:writing-skills` (binding — skill edits obey its Iron Law: RED → GREEN → REFACTOR, no skill change without a watched failure first) + `lean-plan-writing`/`concise-writing` for the angle text (the skill bar is every-word-counts).

## Why

Across the 2026-06-24 ML-engine slice (PR 5) review, the external Codex gate repeatedly raised findings that looked like false positives — a thing that "could happen" but that passing tests showed does not. The reflexive response (trust the tests, dismiss it) is *behaviorally* right but stops short: each time, investigating **why a careful reviewer read it as a bug** surfaced a real **design/interface inconsistency** — the code was correct only by an unstated, non-local, or fragile assumption, often asymmetric with how a sibling path handled the same hazard.

The existing angles don't catch this: `consistency` is about naming/contract/terminology drift; `durability` is about failure/partial-state paths. Neither names the failure mode "correct by accident, not by construction" or the move "a dismissed false positive is a signal to find the tacit invariant." That's the gap this angle fills.

**Watched baseline failure (already observed — reuse as the RED case).** In PR 5, `MLEngine.spawnAndAwaitReady` starts the inbound-stream consume task *before* installing the readiness continuation. Codex flagged "`ready` can be dropped before the waiter is installed." It is in fact safe — but only because there is no `await` between those two points, so the actor never suspends in that window (a non-local, unstated, fragile invariant; a future inserted `await` breaks it silently). The reply path defends the identical hazard *explicitly* with a `pendingReply` buffer; the readiness path relies on the implicit invariant. The asymmetry + implicitness is what made a careful reviewer see a bug — and it is a genuine design smell, not noise. The orchestrator's first response was "trust the tests / false positive"; the design inconsistency only surfaced on a second prompt to investigate *why*. That two-step is exactly what the angle should collapse into one.

## Where the work happens

- **Repo:** `github-personal:midris/disciplined-development-skills` (the canonical source). In a meeting-pipeline checkout the file is the gitignored symlink `.claude/skills/adversarial-review/SKILL.md`; **edit the canonical file in the dd-skills clone**, not through the symlink.
- **Concurrent editors:** the dd-skills repo has more than one editor (see meeting-pipeline memory `skills-repo-parallel-edits`). Before any git op, check the repo's branch + clean state; work on a short-lived branch; do not clobber others' WIP.
- **Propagation:** after merging, consumers pick it up via the repo's `install-skills.sh <consumer-root>` (re-runs the symlinks). No meeting-pipeline change is required — the symlink already points at the file.

## Deliverable — the angle, and where it slots into `SKILL.md`

Add **one new angle, `safe-by-accident`**, to the existing "Review angles" section. Four edit sites, all in `adversarial-review/SKILL.md`. The text below is a near-final draft; the implementer tightens it to the skill bar **after** the RED/GREEN cycle confirms what wording actually changes behavior — do not paste it verbatim without testing (Iron Law).

**1. Angle table — add a row:**

> | **safe-by-accident** | correctness held by an UNSTATED, NON-LOCAL, or FRAGILE assumption rather than enforced by construction — including a hazard defended explicitly in one path but only implicitly in a sibling (asymmetry). A passing test proves the assumption holds *now*; not that it is stated, locally checkable, or survives a refactor. |

**2. "When to apply" — add a bullet:**

> - **safe-by-accident** — code whose correctness rests on ordering, concurrency/scheduling, timing, or initialization order; and ALWAYS when a finding is about to be dismissed as a false positive ("tests show it can't happen"). Run the autopsy.

**3. A short checklist sub-section (mirror how `durability` carries its two checklists):**

> **safe-by-accident — the false-positive autopsy.** A finding you are about to call a false positive is a signal: a careful reviewer saw a bug. Before dismissing it, name the invariant that actually makes the code safe and grade it — if any answer is "no", THAT is the finding (severity by blast radius if it breaks), even though current behavior is correct:
> - *Stated?* the load-bearing assumption is written (comment / assert / type) — not re-derived from the runtime model.
> - *Local?* verifiable at the site — not by non-local reasoning ("no `await` exists in this window, three functions away").
> - *Robust?* a plausible edit (an inserted await / log / reorder) cannot silently break it without a test catching the regression.
> - *Symmetric?* the same hazard is handled the same way across sibling paths — not explicitly here and implicitly there.
>
> The fix makes it correct-by-construction (state it / enforce it / unify it with the sibling's mechanism), not "add a test". A passing test closes a behavioral finding; it never closes a safe-by-accident finding.

**4. Extend the two existing lists** (`Common reviewer rationalizations` table + `Red flags`):

> Rationalization rows:
> - "It's a false positive." → First explain *why* a careful reviewer saw a bug. The explanation is usually the finding.
> - "The tests prove it can't happen." → Tests prove it doesn't *now* — not that the invariant is stated, local, or robust.
> - "It's safe because of how the runtime/actor schedules it." → Safe by accident — one edit from safe by nothing.
> - "The other path guards this; this one is fine without it." → Asymmetry is the smell. Name it.
>
> Red flags:
> - About to write "false positive" without explaining why the reviewer saw a bug.
> - Closing a finding with "tests pass" when the finding is about an unstated/fragile assumption.
> - The safety argument requires tracing another function or the runtime scheduler.
> - The same hazard is guarded one way here and another way (or not at all) in a sibling.

Keep it an *angle* (one lens added to the always-on baseline), consistent with the section's framing; do not restructure the other angles.

## Test plan (Iron Law — required, not optional)

This is a discipline/judgment edit, so test with pressure scenarios per `writing-skills`, and micro-test the wording against a no-guidance control first.

- **RED (baseline, no angle):** give a fresh reviewer subagent a self-contained version of the PR-5 readiness case (or an equivalent "safe only by an implicit no-suspension / init-order invariant, with a sibling that guards the same hazard explicitly") **plus a passing test that proves current safety**, and ask for a review. Expected baseline failure: it dismisses the concern as a false positive / "tests prove it can't happen" and stops — no autopsy, the asymmetry/fragility unnamed. Capture the verbatim rationalizations.
- **Micro-test the wording:** 5+ fresh-context reps per variant, always including the no-guidance control; read every flagged match by hand (template echoes masquerade as hits); converging output = binding wording.
- **GREEN (with the angle):** same scenario; the reviewer now runs the autopsy, grades the invariant (stated/local/robust/symmetric), and reports the tacit/asymmetric invariant as the finding with a correct-by-construction fix — without being told "trust the tests" is wrong.
- **REFACTOR:** fold any new rationalizations the GREEN runs surface into the rationalization table; re-test until it holds under "but the tests pass" pressure.

## Verification / deployment

- The angle reads correctly in context and doesn't bloat the always-on baseline (it's a lens, not a new mandatory pass). Word budget consistent with the other angles.
- Commit to the dd-skills repo on a short-lived branch (clean-state check first); PR/merge per that repo's convention; re-run `install-skills.sh` for a consumer to confirm the symlinked `adversarial-review/SKILL.md` resolves and loads.
- Cross-check: confirm the new angle doesn't duplicate `consistency`/`durability` — it references them (asymmetry is also a consistency signal) but owns the distinct "correct-by-construction vs by-accident" lens + the false-positive-autopsy trigger.

## Notes

- Name chosen: **`safe-by-accident`** (rejected: `tacit-invariant`, `correct-by-construction`, `invariant-locality`).
- This angle is the disciplined counterweight to "trust the tests": `disciplined-research` verifies a claim against reality; `safe-by-accident` verifies that *current* reality is *enforced*, not incidental.
