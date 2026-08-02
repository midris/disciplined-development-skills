# dd-skills backlog

Prioritized backlog distilled from the `plans/deferred/` audit (2026-06-17),
refreshed 2026-06-22 after the review-tooling overhaul landed; 2026-06-26 promoted the
`adversarial-review` generative rule + angle plans (B18–B20) to **Next up**; 2026-07-17
promoted the skills-portability cycle (B25) and logged the defects a codex cold read of
the doctrine already found (B23, B24, B26). **All items
OPEN** unless noted; items resolved or obsoleted by the overhaul are listed near the
bottom, and the "Done" section is context.

Item shape: **ID · title** — category · source · effort/risk · one-line (+ acceptance).
Effort S/M/L. **This doc is the seed for the planned GitHub-issues integration** — IDs map
1:1 to issues once that lands; until then this is the single source for "what's next."

## Next up (current focus) — skills-portability cycle + `adversarial-review` angle batch

Promoted ahead of the tiers below (2026-06-26): the most-developed, RED-grounded work.
Each is a skill edit, so `superpowers:writing-skills`' Iron Law binds (RED → GREEN →
REFACTOR; micro-test wording vs a no-guidance control). B18 **shipped** 2026-06-27
(PR #35); B20 **shipped** 2026-06-30 (owner's call — RED did not reproduce; see B20 below).
B19 remains — it rides the same angle-discrimination cycle as Tier 2's B4–B6 + B16's `currency`.
2026-07-17 (owner): **B25** is current focus; **B23**/**B24** are defects it already turned up.

- **B25 · skills portability review + rework cycle (codex-driven)** — skill-content / portability · 2026-07-17 · L/med.
  Verify the **skills** (not the hooks) are genuinely portable across models — the bundle's
  central claim. Method: hand each `SKILL.md` to a non-Claude reader cold and rework whatever
  doesn't survive the read. A 9-run probe of `disciplined-development/SKILL.md` alone yielded
  B23 + B24: a Claude session had been resolving those ambiguities from conversation context
  rather than from the page, which is precisely the portability defect. The other eight skills
  are unprobed. Distinct from **B6** (a review *angle* for env/path/OS assumptions in code).
  Method notes from the probe — all three cost the cycle real money if ignored:
  (1) **n=1 is noise.** Within-cell variance swamped every between-cell difference: terra/high
  burned 20,183 vs 34,634 tokens on byte-identical input, and read the repo in 1 of 2 runs.
  Every pattern visible at n=2 collapsed at n=3. Use n≥3 per cell; treat a single run as anecdote.
  (2) **Convergence measures salience, not validity.** The unanimous 9/9 finding is a judgment
  call; the two contradictions verifiable against the file scored 2/9 and 1/9. Verify each finding
  against the artifact — never rank by hit count.
  (3) **Cost does not predict quality.** The cheapest run of the nine (3,821 tokens) found the
  sharpest contradiction.
  Acceptance: a per-skill cold-read record in `skill-validation/`; defects fixed per the
  `writing-skills` Iron Law; the doctrine reads correctly to a cold non-Claude reader without
  conversation context.
- **B23 · doctrine self-contradictions (codex cold read)** — skill-content · 2026-07-17 · M/med.
  Three contradictions in `disciplined-development/SKILL.md`, each **verified against the file**,
  each surfaced by codex reading the doctrine cold (9 runs; terra/med, terra/high, sol/low, n=3):
  **(a) Principle 7** — "wait for the edge case to actually occur" + "handle observed cases;
  document the rest as accepted edge cases" vs "a crash or wrong output on a representable input
  is a defect, not an edge case. Fix by construction." Nothing says which wins. Proposed
  (terra/high#2): fix-by-construction dominates wherever the invariant is fragile. Live instance: **B26**.
  **(b) Iron Law + Gate 3 vs Principle 1** — the Iron Law admits an artifact "in writing, in chat,
  or in the running system" and Gate 3 says "Paste evidence in chat", while Principle 1 says
  "Conversation is not a contract; the file is." Same fix from 3 independent runs across both
  models: chat may discharge transient gate evidence; durable scope, decisions, deferrals and
  rationale must reconcile into the governing file before the change lands.
  **(c) "No discipline is skippable on grounds of size, effort, or impact"** vs the Mode-emphasis
  table's per-mode **Active gates** subsets — Brainstorming lists no gates, docs-editing lists
  Gates 1+4 only. "Active" implies the rest are inactive: skipping by mode rather than by size.
  Resolution shape in **B24**.
  Acceptance: each resolved on-page; RED/GREEN per `superpowers:writing-skills`; cold-read confirms
  no worse instruction; `wc -w` bounded. (a) found by sol/low#1 + terra/high#2; (b) by sol/low#2 +
  terra/med#3 + sol/low#3; (c) by terra/med#3.
- **B24 · proportionality: explicit discharge, not silent skip** — skill-content · 2026-07-17 · M/med.
  The only **9/9** finding in the probe — every run, both models, all three effort tiers: fail-closed
  everywhere reads as ceremony on tiny or no-risk work and invites the bypass it aims to prevent.
  Proposed (sol/low#3): keep the posture, drop the empty ritual — *every gate must be considered and
  explicitly discharged; a documented "not applicable" may be the artifact where the gate has no
  meaningful subject.* Subsumes B23(c): the mode table is already the proportionality dial, and the
  preamble denies it exists. Caution: 9/9 measures how the doctrine **reads**, not that it is wrong —
  this is a judgment call, unlike B23. Related: B7, B2's closure.
  Acceptance: rule on-page; RED/GREEN; the mode table and the "no discipline is skippable" line stop
  contradicting; no new hatch that permits a silent skip.
- **B18 · generative "Generate the unexercised cases" baseline rule** — skill-content · 2026-06-26 · M-L/med.
  Add a fourth always-on Rule to `adversarial-review` (beside Enumerate / Verify / Challenge):
  manufacture the input or condition the artifact is silent on, and break it. Two faces — input space
  (absent / malformed / out-of-scale) + tacit invariant (stated/local/robust/symmetric grade +
  false-positive autopsy, folded from the now-superseded `safe-by-accident` 06-24 plan). RED-grounded in
  three Codex P1s every internal review layer missed; the angle→baseline-rule reframe is owner-confirmed.
  Acceptance: per the plan — two RED/GREEN pairs (input + invariant face), wording micro-tested vs a
  no-guidance control, `wc -w` bounded, non-duplicative of `durability`/`consistency`.
  Plan: `plans/completed/2026-06-26-generative-unexercised-cases-baseline-rule-deferred.md`
  (supersedes `plans/completed/2026-06-24-safe-by-accident-review-angle-deferred.md`).
  *(DONE — merged to `main` 2026-06-27 (PR #35). Faithful
  whole-repo test on PR #25's pre-fix tree: reliable out-of-scale lift (baseline 1/5 → +rule ~70%,
  face 6/6) — ships on that. A (absent/HF) is a knowledge gap (0/19); B (malformed/payload) is
  outlier-hard (0/N specific, though the enumeration form reaches its trust boundary). Adopted the
  plan's enumeration form; anti-bloat trim confirmed non-degrading. Record: `skill-validation/adversarial-review.md`.)*
- **B19 · `traversal` (path/structure-completeness) angle** — review-angles · 2026-06-25 · M/med.
  Add an angle that follows a new datum / message / field through **every** layer it must cross
  (producer → transport → decoder → stub → consumer → status → wire → UI) and flags any layer that
  silently drops it. RED: a step-13 wire-path gap Codex caught as a P1 that in-session review missed
  one-per-round. Distinct axis from B18 (structure, not condition space). Acceptance: RED→GREEN (planted
  traversal gap missed without the angle, caught with it); terse, non-duplicative of
  `consistency`/`executability` — fold into them if testing shows overlap.
  Plan: `plans/deferred/2026-06-25-adversarial-review-traversal-angle-deferred.md`.
- **B20 · author-side mirror: generate-unexercised-cases self-check** — skill-content · 2026-06-26 · S-M/low.
  Plan-author counterpart to B18: a one-line self-check cross-ref into `lean-plan-writing` — before
  declaring a plan ready, name the absent / malformed / out-of-scale inputs each task assumes and any
  correctness resting on a tacit invariant; pin the expected behavior or mark it an accepted edge.
  Separate skill, separate baseline failure, its own RED/GREEN — do **not** bundle with B18. Source: the
  B18 plan's "author-side mirror" follow-up.
  *(SHIPPED 2026-06-30, owner's call — branch `feature/lean-plan-unexercised-cases`. Folded into
  `lean-plan-writing`'s Per-artifact `Plans` bullet: "Before calling a plan ready, name each task's unhandled
  inputs (absent/malformed/out-of-scale) and the invariants it silently relies on — then pin the behavior or
  mark it an accepted edge." **RED did not reproduce**: 10/10 authors on the current skill (edge-loud CSV
  upload + edge-quiet digest job, 5 each, sonnet) already handled the discipline's substance and dispositioned
  each face — Iron Law says no edit warranted; shipped as a reinforcement on owner judgment. **GREEN —
  measured, placement-insensitive** (digest, 5 reps/arm): dedicated collected+labeled edge-case section 5/5
  (both a titled and the shipped folded placement) vs 0/5 control; malformed-boundary reach 5/5 folded / 4/5
  titled vs 0/5 control, landing as cheap defensive hygiene; no degradation. Effect is line-wording-driven,
  not heading-driven. Record: `skill-validation/lean-plan-writing.md`.)*

## Tier 1 — quick wins (small, self-contained, low risk)

- **B22 · archival-move trigger in `sweeping-stale-references`** — skill-content · 2026-07-03 · S/low.
  Moving a plan/spec into `completed|archived|deferred` changes a load-bearing fact (its
  path) — the skill should name that as an explicit trigger: sweep referrers in the same
  commit. RED-grounded: 6 of 19 external-gate findings on steno PR #1 were accumulated
  archival path drift (31-file sweep). Acceptance: trigger row present; RED/GREEN per the
  Iron Law; steno consumers also have the mechanized guard (test_doc_references.py) as
  belt-and-braces.

- **B1 · `disciplined-research` disclaimer-as-substitute edits** — skill-content · 2026-06-02 · S/low.
  4 SKILL edits: rationalization row ("I'll verify before it lands"), red-flag for
  hedged-but-used claims, extend load-bearing destinations to current-message
  recommendations, sharpen "load-bearing = determined by *use*." Acceptance: edits present;
  cold-read confirms no worse instruction.
  *(2026-06-24 RED testing: edits 1–2 ("verify later" hedge) never reproduced across 3 scenario
  designs. Edits 3–4 (load-bearing-by-use): the deferral-framed control confabulates, but the CURRENT
  skill already grounds it correctly (3/3 fetched + cited a canonical source, consistent dates) — no
  gap to close. The reproducible unfixed failure is casual/output-pressure citation-fabrication → B17.
  B1 as scoped does not clear the writing-skills bar; recommend folding effort into B17 pending review.)*
- **B17 · `disciplined-research` citation-as-substitute / false-verification gap** — skill-content · 2026-06-24 · S-M/med.
  Found in B1 RED testing: with the skill loaded, agents satisfied "cite the source" by manufacturing
  authority — "verified against the official release page", a `Source:` URL — while the cited value was
  confabulated and inconsistent across reps; one had a fetched value in hand yet wrote a *recalled* date
  into the artifact. The skill covers ungrounded recall and stale citation, not *fabricated / over-claimed*
  citation or fetched-but-recalled-in-artifact. Candidate edits: rationalization row ("I cited a source, so
  it's grounded" — a citation you didn't actually read this turn isn't grounding) + red flag (claiming
  "verified" / "per the docs" with no invocation or path you ran this turn). Acceptance: RED reproduces the
  fabricated citation; edits flip it; cold-read no worse instruction. Evidence: B1 RED run, 2026-06-24
  (current-skill arm 3/3).
  *(CLOSED 2026-06-26 — real but wording-resistant. RED reliably reproduces the fabrication on the
  mandatory-cite floor; five approaches (explicit recipe, terse, cite-but-tag-unverified, minimal nudge,
  honest-memory-citation) all failed to move it — a hard task-level "must cite" requirement overrides
  skill guidance. Softer conditions already ground. The broader behavior change was not shipped;
  the minimal `verify the citation yourself` nudge landed in `2be8db4` after scoring 0/6 and was
  explicitly behavior-neutral. Full record in `skill-validation/disciplined-research.md`.)*
- **B2 · pre-PR gate announces itself** — pre-pr-gate / observability · 2026-06-08 · S/low.
  Gate runs codex ~minutes silently on `gh pr create`. Add a Gate-5 instruction to announce
  the review before invoking it (optionally a hook start-line). Acceptance: model announces
  before the gate runs.
  *(CLOSED 2026-06-26 — premise disconfirmed; not shipped. RED (10/10 across two arms on the
  current Gate-5 doctrine) already announces the external review before `gh pr create` — the
  announce is now default, emergent from recent dd-skill changes. The lone residual — warning
  about the multi-minute codex pause — is a knowledge gap, not a discipline gap: the model
  relays the duration only when told it (arm A 5/5), never infers it (arm B 0/5). That fact is
  Claude-Code-specific, not portable-skill material. Current behavior accepted as-is.)*

## Tier 2 — candidate review angles (one discrimination batch)

Run all three through the angle-necessity bar (discrimination vs holistic) in one
`adversarial-review` cycle; add only those that beat holistic. **B19** (Next up) and
B16's `currency` join the same cycle.
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

- **B21 · external-reviewer prompt calibration (severity + clean-pass)** — review-tooling · 2026-07-03 · S-M/med.
  `external_review.py` prompt only: P2+ requires a demonstrably-false claim contradicted by
  a cited primary source; policy/placement/style caps at P3 (P3-only = PASS); state that
  "No findings." is an expected outcome. RED-grounded: steno PR #1 — 18/18 substantive
  codex findings at exactly P2, ~4 findings/round regardless of repo state, zero
  external-gate PASS rows before 2026-07-04. Prompt content, not hook machinery (owner
  ruling) — the parked `wip/external-gate-forcing-function-built` spike is reference-only.
  Acceptance: replaying the PR #1 round-5 findings shape yields P3s -> PASS; a clean repo
  yields "No findings."; deferred plan of record:
  `plans/completed/2026-07-01-external-gate-root-attack-forcing-function.md` (closure).

- **B26 · chained relative `cd` lets the gate review a different repo** — pre-pr-gate · 2026-07-17 · S-M/med.
  `command_match.py:280`: a relative `cd` anchors to the process cwd, not to a preceding `cd`, so
  `cd /a && cd b && gh pr create` resolves to `<process_cwd>/b`. The gate can then review a
  different repo than the PR targets — a bypass vector, not merely a scoping quirk. Today an
  accepted edge with on-page rationale at the call site. Whether that acceptance survives **is**
  B23(a): the input is representable and the output is wrong, which the fix-by-construction clause
  calls a defect and the wait-for-the-edge-case clause calls an accepted edge. Raised as P1 by the
  external gate on PR #38 (terra/medium, 2026-07-17); its sibling P1 — config ignoring `--cwd` —
  was fixed there (`6f8be3e`).
  Acceptance: settle B23(a) first, then either fix by construction (resolve each `cd` against the
  running cwd) or restate the acceptance so it survives the settled rule.
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
