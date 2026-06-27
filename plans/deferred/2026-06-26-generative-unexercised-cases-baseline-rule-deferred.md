# Add a generative "Generate the unexercised cases" BASELINE RULE to `adversarial-review` (subsumes `safe-by-accident`)

**Status:** Deferred (captured 2026-06-26). **Supersedes / merges** `plans/deferred/2026-06-24-safe-by-accident-review-angle-deferred.md` — that proposal's content becomes the *invariant face* of this rule (see "Subsumption" below); do not implement it separately.

**⚠ Cross-repo:** the skill is `skills/adversarial-review/SKILL.md` in the private **`disciplined-development-skills`** repo (`github-personal:midris/disciplined-development-skills`). In a meeting-pipeline checkout that file is a **gitignored symlink** — edit the canonical file in the dd-skills clone, then re-run that repo's `install-skills.sh <consumer-root>`. **That repo has concurrent editors** (memory `skills-repo-parallel-edits`): check branch + clean tree before any git op; branch.

**Governing for the implementer:** `superpowers:writing-skills` (binding — Iron Law: no skill change without a watched RED first; RED → GREEN → REFACTOR; micro-test wording vs a no-guidance control, 5+ reps, read every flagged match by hand) + `concise-writing`/`lean-plan-writing` for the text.

## For a fresh dd-repo session (read first)

You work in the **`disciplined-development-skills`** repo with **no access to meeting-pipeline**. To execute this self-contained:

- **Inputs you are handed:** this file **and** the superseded `2026-06-24-safe-by-accident-…` plan — its notes are the verbatim source for the invariant face (the four rationalization rows, four red-flags, and the readiness RED case). Work from both; if you only have this file, its summaries below are sufficient to reconstruct the fixtures.
- **Re-read `skills/adversarial-review/SKILL.md` from disk FIRST.** It evolves; confirm the live `## Rules` section, the `## Common reviewer rationalizations` table, and the `## Red flags` list before choosing insertion points. The anchor named below ("after *Challenge every piece for necessity*") is where it stood on 2026-06-26 — verify, don't assume.
- **Fixtures are self-contained synthetic artifacts** built in the dd-repo test harness — do NOT reference meeting-pipeline code (you can't see it). The prose descriptions here reduce each finding to a small standalone reproducer.
- **Testing method:** `superpowers:writing-skills` + its `testing-skills-with-subagents.md`.
- **No `description` change.** This is an always-on baseline rule (the skill is already loaded whenever a review runs), so the frontmatter `description` (which states *when to use*, not what the skill does) stays as-is.

## Why — the gap (RED evidence, already observed)

The step-13 transcription implementation passed every **internal** review layer (per-task adversarial reviews + two cadence reviews + a Gate-5 whole-branch self-review) and was then BLOCKED by the **external Codex gate** on **three P1s** the internal layers all missed:

- **Absent** — a model not on disk triggers an in-job HuggingFace *download* instead of `ml.model_missing` (D4 violation).
- **Malformed** — a worker IPC `result` missing `transcript_ref` is committed as a *successful* audit event.
- **Out-of-scale** — the CLI's 5s HTTP timeout vs an ~8-min synchronous walk on a 2-hour meeting.

All three share one shape: a condition the happy path **silently assumes** and the artifact **never names**, so a reviewer anchored to what's written — and to what the tests exercised — walks past it. The skill's existing baseline rules are **reactive**: *enumerate* what's claimed, *verify* what's asserted, *challenge* what's present. None is **generative** — "manufacture the input/condition the artifact is silent on and break it." That is the gap.

**Key realization (the consolidation):** the deferred `safe-by-accident` angle was an earlier, narrower reach at the *same* insight — "a passing test proves the case it ran, not robustness." Its object is a tacit **invariant** (correctness held by an unstated/fragile ordering assumption); this rule's first object is the **input space**. They are two faces of one generative discipline: **a green signal fixes both the inputs fed and the execution context; generate variations of each it never exercised.** So `safe-by-accident` merges in here rather than landing as its own angle.

## Placement decision: BASELINE RULE, not an angle

An angle is a *specialized, conditional* lens. This applies to almost any artifact that consumes an input, depends on a resource/precondition, or sets a fixed bound — i.e. nearly everything — so it belongs in the **always-on baseline**, as a fourth Rule beside *Enumerate every class / Verify every rationale claim / Challenge every piece for necessity*. (Confirmed with the skill owner, 2026-06-26.)

## The change — the rule text (near-final draft; tighten AFTER RED/GREEN, per the Iron Law)

Add a fourth `### Generate the unexercised cases` rule under "## Rules" (after "Challenge every piece for necessity"):

> A passing test (or a clean read) proves the case it ran — not robustness. The artifact and its tests show you the happy path; manufacture what they held fixed and break each.
>
> **Inputs the tests didn't feed.**
> - *Absent?* a required resource/precondition not there (model not on disk, file / permission / config unset) → documented error, or silent fallback / download / hang / default?
> - *Malformed?* data crossing a trust boundary (a peer's IPC reply, an external response, a parsed field) used or **committed** without validation → a malformed reply recorded as a *valid* result?
> - *Out-of-scale?* a fixed timeout / limit / buffer tuned to the test case → survives the *largest real* input (a multi-hour recording, a 10k-item list, a slow link)?
>
> **The invariant the green run relied on** *(when correctness rests on an unstated / non-local / fragile assumption — ordering, init-order, "no `await` in this window," a sibling guarding the same hazard explicitly while this path relies on it implicitly).* Grade it: *Stated?* (written — comment/assert/type, not re-derived from the runtime model) *Local?* (checkable at the site, not by tracing three functions away) *Robust?* (a plausible inserted `await`/log/reorder can't silently break it) *Symmetric?* (the same hazard handled the same way across sibling paths). Any "no" is the finding **even though it passes now**; the fix makes it correct-*by-construction* (state it / enforce it / unify with the sibling), never "add a test."
>
> **The autopsy (trigger).** A finding you're about to dismiss as a false positive — "the tests show it can't happen" — is the signal: a careful reviewer saw a bug. Name the invariant that *actually* makes it safe and grade it before dismissing. The explanation is usually the finding.

**Also extend the two existing lists** (folded from `safe-by-accident`):
- *Common reviewer rationalizations* — add: "It's a false positive." → First explain *why* a careful reviewer saw a bug; the explanation is usually the finding. / "The tests prove it can't happen." → They prove it doesn't *now* — not that the assumption is stated, local, or robust. / "Safe because of how the runtime/actor schedules it." → Safe by accident — one edit from safe by nothing. / "The model's always there / the result's always well-formed / meetings are short." → That's the assumption. Remove it and re-read.
- *Red flags* — add: about to write "false positive" without explaining why the reviewer saw a bug; closing a finding with "tests pass" when it's about an unstated/fragile assumption or an unfed input; the safety argument requires tracing another function or the scheduler; the same hazard guarded one way here and another (or not) in a sibling.

**Form (writing-skills — Match the Form to the Failure).** Two failure shapes, two forms — write *and test* each to its shape:
- The **input + invariant faces** are a *technique the reviewer omits*, not a rule they knowingly skip → write them as a positive **recipe** (generate-and-check, mirroring "Enumerate every class"). A **prohibition** ("don't review only the happy path") backfires on a generative move — agents negotiate with "don't". Micro-test the recipe's wording against a no-guidance control.
- The **false-positive dismissal** (the autopsy trigger + the rationalization/red-flag rows) is a *known-better skip under the "trust the tests" pressure* → that's the discipline shape; the rationalization table + red flags are its counter, pressure-tested under "but the tests pass."
- **No nuance/exemption clauses** ("generate X unless…", "doesn't apply to Y"). They reopen the negotiation and degrade a winning recipe to noise; express any real exception as its own conditional on an observable predicate.

**Anti-bloat:** the baseline already carries three rules of similar density; keep this to two short checklists + the trigger (mirror `durability`'s two-checklist density). Do not restate the base posture. `wc -w` before/after.

## Subsumption — what merges from `safe-by-accident`, and what stays separate

**Merges in** (the `2026-06-24` plan's content becomes the *invariant face* + the autopsy trigger):
- the stated / local / robust / symmetric grading → the invariant checklist;
- the false-positive-autopsy → the rule's trigger;
- its four rationalization rows + four red-flags → the skill's existing tables (above);
- its **RED case** (`MLEngine.spawnAndAwaitReady` starts the consume task before installing the readiness continuation — safe only because no `await` suspends the actor in that window, while the reply path defends the identical hazard explicitly with `pendingReply`) → the **invariant-face** test fixture;
- "the fix is correct-by-construction, never 'add a test'" → the fix-guidance line.

**Stays a separate deferred item** (NOT subsumed — distinct axis):
- `traversal` (`2026-06-25`) — generative over **structure** (a datum across every *layer*), not the condition space. Cross-references this rule (both are "generate what's silent") but keeps its own producer→decoder→stub→consumer→wire method.
- `currency` + the `consistency`/`executability` strengthenings (`2026-06-23`) — doc-tense and doc↔code *correspondence*; unrelated to runtime robustness.

**Carving vs the existing angles (anti-bloat cross-check — required at GREEN):** the *Malformed?* face overlaps `durability`'s "reads that accept non-committed data," but `durability` is scoped to durable-state machinery and explicitly skips stateless code, whereas *Absent?* / *Out-of-scale?* apply to stateless code too (the model load, the CLI timeout) — outside durability entirely. The one seam — a peer's input that *becomes* durable state (validate before the commit) — stays here, so the three faces live together. The *Symmetric?* grade overlaps `consistency` (asymmetry is a consistency signal): reference it, don't restate. Confirm at GREEN that the rule reads as new guidance, not a paraphrase of `durability` / `consistency`.

## Test plan (Iron Law — required)

Two RED/GREEN pairs, one per face; micro-test wording vs a no-guidance control first (5+ reps, read every flagged match by hand).

- **Input face — RED:** a fresh reviewer on `adversarial-review` *without* the rule, over three small seeded artifacts **each with a passing happy-path test**: (a) a `load_model` that downloads on cache-miss; (b) a result-handler that commits metadata without checking required keys; (c) a client with a short fixed timeout on a synchronous long-running endpoint. Baseline expectation: passes them (the green test anchors it). Capture the misses. **GREEN:** with the rule → flags absent-not-errored, malformed-committed-as-valid, bound-breaks-at-scale. Plant a decoy that genuinely validates/bounds correctly so "flag everything" fails.
- **Invariant face — RED/GREEN:** the readiness-continuation fixture (above) **+ a passing test proving current safety**. Baseline dismisses it as a false positive / "tests prove it can't happen"; with the rule, runs the autopsy, grades the invariant, and reports the tacit/asymmetric invariant with a correct-by-construction fix. (Reuse `safe-by-accident`'s test plan verbatim — it's the invariant-face test.)
- **REFACTOR:** fold any new rationalizations the GREEN runs surface into the table; re-test under "but the tests pass" pressure.

## Done-when

- Reviewer *without* the rule misses a planted unfed-input gap AND a planted tacit-invariant gap; *with* it, catches both (RED→GREEN recorded for each face).
- The fourth baseline rule + the table/red-flag additions land — terse, non-duplicative of `durability`/`consistency`; `wc -w` reasonable.
- Committed to the dd-skills repo (branch/clean-state checked first); `install-skills.sh` re-run on a consumer to confirm the symlink resolves.
- `2026-06-24-safe-by-accident-…` left marked SUPERSEDED (this plan owns its content).

## Related follow-up — author-side mirror (SEPARATE edit, own RED/GREEN)

The reviewer-side rule has a plan-**author**-side mirror: an author who generates the unexercised cases *before* review leaves the rule less to catch. Add a one-line self-check cross-reference to **`lean-plan-writing`** (the author-side home; `writing-explicit-rationale` is the alternative if the framing fits better there): *before declaring a plan ready, name the absent / malformed / out-of-scale inputs each task assumes, and any correctness resting on a tacit invariant — pin the expected behavior or mark it an accepted edge.* This is a **separate skill edit with its own RED/GREEN** (a plan-author scenario: a plan silent on an absent precondition or an unbounded input → baseline author ships it; author-with-the-cross-reference names it). **Do NOT bundle it** with the reviewer-rule edit — different skill, different baseline failure, different test. (Originally flagged in the `2026-06-23` plan's "Cross-reference" note; recorded here so it isn't lost.)

## Out of scope

- This project's code (the three findings are already fixed in the step-13 PR).
- The `disciplined-development` parent skill / gates — the rule lives in `adversarial-review` only.
- `traversal` / `currency` / the consistency-executability strengthenings — separate deferred items, not bundled here.
