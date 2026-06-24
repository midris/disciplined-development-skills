# Strengthen `adversarial-review` with angles extracted from the ML-engine plan-hardening

**Status:** Deferred. Captured 2026-06-23 from the ML-engine-slice plan-hardening (15 external-gate
rounds + a 2-reviewer internal pass + a manual codex pass — **53 findings**). The plan/spec hardening
is done; this is a follow-up to fold the *pattern* of those findings back into the reviewer skill so
the next plan gets caught up front instead of over 15 gate rounds.

**Where this is implemented (NOT this repo):** `skills/adversarial-review/SKILL.md` in the private
**`disciplined-development-skills`** repo (`github-personal:midris/disciplined-development-skills`).
In meeting-pipeline that file is a **gitignored symlink** — edit it in the dd repo, not here.
⚠️ That repo has concurrent editors (memory `skills-repo-parallel-edits`): check branch + clean
state before any git op there.

**Governing discipline:** `superpowers:writing-skills` (+ `superpowers:test-driven-development`).
The **Iron Law applies to edits**: NO skill change without a failing test first. Each angle change
below ships only after its RED (baseline reviewer misses the defect class) → GREEN (reviewer with
the new angle catches it) is recorded. Testing method: `writing-skills/testing-skills-with-subagents.md`
and the **micro-test wording** loop (5+ reps, a no-guidance control, read every flagged match).

**Evidence base (the 53 findings):** they persist verbatim in
`meeting-pipeline/.claude/.dd-state/.logs/reviews.jsonl` (the `gate:pre-pr` rows on branches
`feat/ml-1-filename-template-removal` and `feat/ml-meeting-event-model`). Pull them with the
extractor in this repo's session log if the fixtures below need more examples.

---

## Why these angles (the pattern in the 53 findings)

The findings cluster into four classes. One (**D — durability**) was already caught by the existing
`durability` angle; the other three slipped through round after round because the skill has no lens
for them. Counts are approximate (some findings span classes).

| Class | ~count | Representative findings (verbatim-ish) |
|---|---|---|
| **A — one contract restated in N places, fixed in 1** | ~17 | "ML spec still defines the claim as the atomic move, contradicting the plan's event-first"; "claim-loop summary (line 74) vs event-set (line 178)"; `transcribed/` dropped in recovery **and** test-posture **and** single-claim **and** recovery-seq; "**shutdown diagram** contradicts the drain ordering"; "artifact *or nothing*" (spec) vs "artifact before `_completed`" (plan) |
| **B — built-vs-planned tense conflation** | ~8 | "ARCHITECTURE says the ML engine exists **today** while marking it unbuilt"; "recording still writes `events.jsonl`, so the planned `recording.events.jsonl` cannot exist"; "PR 4b exempts active docs that still contain **current-state** `events.jsonl` claims" |
| **C — plan asserts something the real code contradicts** | ~15 | "`MLStageEvent` can't append to the single-payload log"; "`extracting→extracted` needs `phase`, `MeetingTransition` rejects without it"; "`hashFile(at:)` is a **free function**, not `RecordingHash.hashFile`"; "`EventLog.openOrCreate` is **private**"; "extend-the-enum mislabels category (hardcoded `"recording"`)"; "`/status` seam is **synchronous**" |
| **D — source-of-truth invariant stated loosely** | ~5 | already covered by the existing `durability` angle — **no change** |

The throughline: A and B are *consistency-flavoured* but in places the current `consistency` angle
never names (other altitudes, other docs, **diagrams**, **tense**). C is *executability-flavoured*
but the current `executability` angle only checks the artifact against **itself**, never against the
**real codebase** it builds on.

---

## Change 1 — Strengthen the `consistency` angle (Class A)

The `consistency` row today reads (roughly): *"divergence across the corpus — contract / signature /
import drift, terminology drift, wording drift, single-source duplication."* That posture missed
siblings ~17 times because it doesn't tell the reviewer **where siblings hide**.

**Add to the angle (exact home: the `consistency` row's "Looks for" + a one-line method note):**

> A single contract is commonly restated at **multiple altitudes** (a decision's one-line summary,
> its detailed spec, its test-posture, the build-order list) and across **multiple documents**
> (the plan ↔ each spec ↔ the architecture doc ↔ a parent/control-plane spec). **Diagram labels and
> sequence-diagram steps are siblings** — prose greps miss them. Method: when you find one statement
> of a contract, search its **old/anti-pattern wording** across every doc *and every diagram*; a
> contract corrected in one place but stale in another is the single most common defect class.

This is `sweeping-stale-references` promoted into a review lens. Keep it to ~4 sentences; do not
restate the base posture.

### RED / GREEN test (Change 1)

**Fixture `fixtures/consistency-diagram-sibling/`** — a 3-file mini-corpus with ONE contract stated
3×, corrected in 2 places, stale in the diagram:
- `spec.md`: "**Decision 5:** the claim is **event-first** — append `x.started`, then move the dir."
- `plan.md`: "Task 2 claim: append `x.started` (commit) → move." *(agrees)*
- `arch.md`: a mermaid block whose only claim edge is `A ==>|"claim = atomic move"| B`. *(stale sibling)*
- Plant 1–2 decoys (genuinely-consistent restatements) so "flag everything" doesn't trivially pass.

- **RED:** dispatch a reviewer subagent loading the **current** `adversarial-review` + `consistency`
  angle over the fixture. Baseline expectation: it flags the prose if obvious but **does not** flag
  the mermaid `claim = atomic move` edge as a sibling. Record the miss verbatim.
- **GREEN:** same fixture, reviewer loads the **updated** angle → it emits a finding naming the
  **diagram** edge as a stale sibling of the event-first contract.
- **REFACTOR:** if it now over-flags the decoys, tighten ("a *contradicting* restatement", not any
  restatement) and re-run.

---

## Change 2 — New `currency` angle (Class B)

No existing angle covers built-vs-planned tense. This caused a ~6-round detour (the gate read a
forward-looking docs PR as "code doesn't match the plan") that only cleared once the docs were
tense-tagged — confirming the *real* defect was the doc's own ambiguity, not the review scope.

**Add a new row to the angle table + a "when to apply" line:**

> **currency** — *when to apply:* any artifact that mixes **current and planned state** —
> implementation plans, a living architecture doc with built/◻ markers, a slice spec describing
> unbuilt work against an existing codebase. *Looks for:* state claims not unambiguously tagged
> current-vs-planned — a **target/planned name written in the present tense** (`recording.events.jsonl`
> as if it already exists), a **✅/"built" marker on unbuilt work**, a **future-state requirement the
> current code is faulted for not yet meeting**, or a **planned change whose tense-framed claims**
> ("*today* X; renamed to Y") **aren't scheduled to flip** when the change lands.

### RED / GREEN test (Change 2)

**Fixture `fixtures/currency-tense/arch.md`** — a living-architecture snippet using built/◻ markers
with a self-contradiction lifted from the real session:
- `"- Event logs — recording.events.jsonl ✅ — today named events.jsonl, renamed as the ML stream lands"`
  *(✅ "built" on a name that the same clause says doesn't exist yet)*
- `"Three engines today: app, recording, ML"` while another line reads `"ML engine ◻ — designed, not yet built."`
- Plant a *correctly* tense-tagged decoy (`"today events.jsonl; PR 4b renames it ◻"`) that must NOT be flagged.

- **RED:** reviewer with the **current** skill (no currency angle) over the fixture → does **not**
  flag the ✅-on-unbuilt or the "today: app, recording, ML / ML ◻" contradiction. Record the miss.
- **GREEN:** reviewer with the **updated** skill → flags both as currency defects, and leaves the
  correctly-tagged decoy alone.
- **REFACTOR:** ensure the angle's "when to apply" gates it OFF for a pure current-state doc (a
  finished-feature README) so it doesn't fire spuriously — add a negative fixture if needed.

---

## Change 3 — Strengthen `executability` with a codebase-grounding pass (Class C)

The `executability` row today checks whether a *zero-context implementer* could execute the plan —
i.e. internal clarity. It never says "check the plan's claims **against the real code**." ~15 findings
were the plan asserting something the actual codebase contradicts.

**Add to the `executability` angle (a paragraph after the existing "could a zero-context implementer
execute this?"):**

> For a plan/spec built on an **existing codebase**, executability includes a **codebase-grounding
> pass**: every code reference is verified against the actual code, not assumed. The named **symbol
> exists and is accessible** (not private); the asserted **contract holds** (required fields, a
> sync-vs-async seam, a hardcoded enum case, a single-type vs union log, a free function vs a static
> method); every file the change must touch is in the **file-list**; and the task's **tests exercise
> the real path** (the loader, not just the constructor). An assertion the real code contradicts is a
> finding **even when the plan is internally consistent**.

### RED / GREEN test (Change 3)

**Fixture `fixtures/executability-codebase/`** — a plan task + the real code it references:
- `code/Hash.swift`: `func hashFile(at url: URL) throws -> Digest` *(module-level free function)*
- `code/EventLog.swift`: `private func openOrCreate() { /* createFile only — no parent mkdir */ }`
- `plan.md` Task: "call `Hash.hashFile(at:)` … the engine creates the log via `EventLog.openOrCreate`,
  which makes the parent dir." *(two assertions the code contradicts: `Hash.` qualifier on a free
  function; `openOrCreate` is private + doesn't mkdir)*
- Plant a decoy assertion that the code **does** support.

- **RED:** reviewer with the **current** `executability` angle over `plan.md` *with the `code/` dir
  available* → it judges the task internally clear and **does not** check the symbols against the
  code; misses both contradictions. Record the miss.
- **GREEN:** reviewer with the **updated** angle → it inspects `code/` and flags (a) `Hash.hashFile`
  vs the free function and (b) `openOrCreate` private/no-mkdir; leaves the decoy alone.
- **REFACTOR:** confirm the grounding pass stays **bounded** (one focused check per named code
  reference, per the skill's existing "inspect outside the diff only for a concrete named risk"
  rule) — it must not license crawling the whole repo.

---

## Cross-reference (author-side, optional, separate test)

These three are also a plan **author's** pre-flight checklist. Once the angles land, consider a
one-line cross-reference from `lean-plan-writing` ("before review, self-check: siblings swept,
state tense-tagged, code references grounded") so plans are written clean. That is a **separate**
skill edit with its **own** RED/GREEN (a plan-author scenario), not part of this plan — note it,
don't bundle it.

## Acceptance

- [ ] Each of Changes 1–3 has a recorded **RED** (baseline reviewer misses the planted defect) and
      **GREEN** (updated angle catches it), per `writing-skills` — committed as fixtures + a short
      transcript/log in the dd repo.
- [ ] Wording micro-tested (5+ reps, no-guidance control) before the full reviewer-subagent run;
      every flagged match read by hand (template echoes masquerade as hits).
- [ ] `wc -w skills/adversarial-review/SKILL.md` stays reasonable — angles are dense rows, not prose;
      the base posture is not restated.
- [ ] The new `currency` row + the two strengthened rows compose with the always-on holistic
      baseline (they ADD a lens; they don't narrow the review).
- [ ] dd repo: branch/clean-state checked before commit; pushed; `install-skills.sh` re-run if the
      symlink set changed.
