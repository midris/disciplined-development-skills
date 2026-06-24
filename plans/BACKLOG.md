# dd-skills backlog

Prioritized backlog distilled from the `plans/deferred/` audit (2026-06-17),
refreshed 2026-06-22 after the review-tooling overhaul landed. **All items OPEN**
unless noted; items resolved or obsoleted by the overhaul are listed near the
bottom, and the "Done" section is context.

Item shape: **ID · title** — category · source · effort/risk · one-line (+ acceptance).
Effort S/M/L. **This doc is the seed for the planned GitHub-issues integration** — IDs map
1:1 to issues once that lands; until then this is the single source for "what's next."

## Tier 1 — quick wins (small, self-contained, low risk)

- **B1 · `disciplined-research` disclaimer-as-substitute edits** — skill-content · 2026-06-02 · S/low.
  4 SKILL edits: rationalization row ("I'll verify before it lands"), red-flag for
  hedged-but-used claims, extend load-bearing destinations to current-message
  recommendations, sharpen "load-bearing = determined by *use*." Acceptance: edits present;
  cold-read confirms no worse instruction.
- **B2 · pre-PR gate announces itself** — pre-pr-gate / observability · 2026-06-08 · S/low.
  Gate runs codex ~minutes silently on `gh pr create`. Add a Gate-5 instruction to announce
  the review before invoking it (optionally a hook start-line). Acceptance: model announces
  before the gate runs.

## Tier 2 — candidate review angles (one discrimination batch)

Run all three through the angle-necessity bar (discrimination vs holistic) in one
`adversarial-review` cycle; add only those that beat holistic.
- **B4 · contract-coverage angle** — review-angles · loop #5 · M/med. Spec guarantee vs a weaker plan/code mechanism.
- **B5 · migration / backward-compat angle** — review-angles · loop #8 · M/med. Change vs already-installed/old state (PR #23 installer P1).
- **B6 · portability / environment angle** — review-angles · loop #9 · M/med. Env/path/OS assumptions (the `/var` vs `/private/var` P2).

Separately, an already-scoped angle plan (not a candidate to vet):
- **B16 · angle-hardening from the ML-engine plan-hardening** — review-angles · 2026-06-23 · M-L/med.
  Three changes, each with a designed RED/GREEN: strengthen `consistency` for sibling contracts at
  other altitudes / other docs / **diagram labels**; add a **currency** angle (built-vs-planned tense
  — `✅`-on-unbuilt, planned name written present-tense); strengthen `executability` with a
  **codebase-grounding** pass (plan claims checked against real symbols/contracts, not just internal
  clarity). Distilled from 53 findings over 15 gate rounds. Its `currency` angle can ride the same
  discrimination batch as B4–B6. Plan: `plans/deferred/2026-06-23-adversarial-review-angles-deferred.md`
  (written from a meeting-pipeline session; framing pending a dd-repo re-anchor). Acceptance: per the
  plan — each change RED/GREEN per `writing-skills`, wording micro-tested, SKILL word-count bounded,
  angles ADD a lens to the holistic baseline.

## Tier 3 — data-driven calibration (unblocked by review-logging PR #22)

- **B7 · threshold rationale on-page** — skill-content / config · 2026-06-14 · S/low.
  Document the cadence thresholds (edit nudge/block 30/60, commit cadence 3/5, commit-floor 30,
  discipline 50) as deliberately-provisional starter values.
- **B8 · calibrate thresholds from telemetry** — hook-cadence · 2026-06-14 · M/med.
  Use `reviews.jsonl` + hook logs to replace gut-feel numbers. Follows B7.

## Tier 4 — review-loop ergonomics

- **B9 · remediation commits blocked at the gate** — remediation-boundary · loop #7 · M/med.
  A review's own fix commits hit the hard block; needs a runner-set grace token (no human flag).
- **B10 · doc-vs-code nudge weighting** — hook-cadence · loop #2 · M/med. *(PARTIAL: consumer config-mitigated, source defaults unchanged.)*
- **B11 · commit-count gates over-count docs commits** — hook-cadence · loop #6 · M/med.

## Tier 5 — heavy / design-first (brainstorm before code)

- **B14 · discipline-enforcement gaps** — discipline-enforcement · 2026-06-06 · L/high-blast-radius.
  6 sub-items: checkbox hard-constraint, review-cycle tracker, debt counter
  *(note: previously **removed** — re-introduction is a decision, not a gap-fill)*,
  cadence-block + structured waiver, stale-checkbox detector, per-surface review state.
- **B15 · human-facing trust artifact** — human-facing-trust · 2026-06-14 · L/design-unsettled.
  Synthesize `reviews.jsonl` into a human decision surface. Open: anti-gaming, destination,
  producer. Brainstorm before any code.

## Deferred — not yet scoped (parked, no design yet)

- **GitHub-issues backlog integration** — move work-tracking off `plans/` markdown into a
  ticketing system (probably GitHub Issues). Out of scope now; revisit when more people use
  dd. This doc is the interim single-source for "what's next."
- **Distributable dd artifact** — package the bundle for real distribution (beyond the
  symlink installer) once external adoption grows. Out of scope now.

## Resolved / obsoleted by the review-tooling overhaul (2026-06-22)

The overhaul removed diff-scoped review (one deep, whole-repo, plan-anchored mode) and the
`fast`/`regular`/`cold-read` tier vocabulary, closing three items by construction:
- **B3 · untracked-file scope blind spot** — was "`fast` `git diff HEAD` omits untracked/new
  files, so reviews silently pass on them." No diff-scope now; reviews are whole-repo — the
  model-driven review reads the working tree and the codex gate navigates the repo on disk,
  so untracked/new files are in scope. Closed.
- **B12 · tier-depth ceiling on load-bearing artifacts** — was "fast-clean ≠ sufficient; name
  the escalation." No tiers; every review is deep. Closed.
- **B13 · artifact-angles only engage at cold-read** — was "optionally engage applicable angles
  at `regular`." One mode applies every applicable angle per `adversarial-review`'s "when to
  apply." Closed.

## Done (context — merged separately, not from this backlog)

- **Review-tooling overhaul** (PR #30, 2026-06-22) — `dd_review_runner` engine + `/dd-review`
  removed; one deep whole-repo review mode; verdict-driven fail-closed pre-PR gate; consolidated
  `reviews.jsonl` logging; de-diff-scoped doctrine; `ARCHITECTURE.md` + doc refresh.
- `reviews.jsonl` multi-source logging (PR #22) — prerequisite for B8 + B15.
- Angle catalog → skill + 3-angle audit (PR #23).
