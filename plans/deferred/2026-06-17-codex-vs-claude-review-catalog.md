# Codex vs. Claude review — divergence catalog (seed)

**Purpose.** Catalog how Codex's pre-PR review approach + findings diverged from Claude's in-session adversarial reviews, on one controlled case (step-11 ML-worker lifecycle, `meeting-pipeline`), to extract **new review angles for the `disciplined-development` skill set**.

**Why this case is clean evidence.** Same diff, same window. Claude ran a 6-agent Gate-5 (holistic + correctness + rationale + cross-file + security + necessity), two cold-read rounds, and an interim review. Codex ran a 5-round blocking pre-PR gate. The overlap in findings was **near zero** — they failed in opposite directions. That's the signal.

---

## 1. Empirical record

| | Caught | Missed |
|---|---|---|
| **Claude** (6-agent Gate-5 + 2 cold-reads + interim) | input-validation crash (`_run_ping` bad-arg → unhandled `ValueError`, "F5"); config-doc **accuracy** (a comment misdescribed `job_silence_timeout` as idle behaviour); `send()` failure not logged; necessity/concise items; stale-comment + parity dispositions; correctly **rejected** ~3 weak findings with rationale | **every** concurrency/lifecycle interleaving bug below |
| **Codex** (5-round pre-PR gate) | ~19 lifecycle bugs: terminate/respawn races, ready-vs-death (two orderings), cross-generation buffer/handle bleed, join-before-act gaps, breaker double-count + no-reset, expected-death flag leaks, Swift↔Python validation-parity gap | input-validation crash (F5); doc-accuracy; necessity — i.e. Claude's catches |

**Headline:** Claude's *six* parallel adversarial agents, explicitly angled and instructed to "presume a flaw," found **0** of the concurrency bugs. Codex found ~19 across 5 rounds. Conversely Codex's concurrency-focused passes didn't flag the input-validation crash, the doc-accuracy drift, or the necessity items Claude caught. **Complementary, not redundant.**

**Recurrence data point.** The readiness-timeout double-count was caught by Codex *pre-plan* (fixed with a per-generation dedup guard), then **recurred** at gate round 5 because the fix was a local patch (the idle-death path bypassed the guard). Patching an instance, not the class, let the same bug back in. This is the core argument for adding *class-level* angles.

---

## 2. How the approaches diverged (the mechanism)

Claude's reviewers read **control flow** — "for this function and these inputs, is the logic right? are the claims true? is each piece necessary?" They trace a path and verify. Strong on: claim-checking, necessity, enumerating *input* cases, doc/spec drift.

Codex reasoned about **execution schedules** — it behaved like an interleaving model-checker. Its findings share a shape Claude's angles don't target:

1. **Adversarial schedule construction ("evil scheduler").** Almost every finding was *"event B arrives between line X and line Y of A's handler, while timer C is pending."* E.g. *"`terminate()` returns before the termination handler runs; `recordReadinessFailure` moves the lifecycle; THEN the killed process exits."* That's a deliberately-chosen 3-step ordering, not a path you reach by reading top-to-bottom.

2. **Re-entrancy awareness (every `await` is a yield point).** In a Swift actor, state can change at every suspension. Codex implicitly asked at each `await`: *"what mutable state can another task change while I'm suspended here, and does my post-await code still assume the pre-await state?"* The `.ready`-case-overwrites-a-death bug was exactly this.

3. **State-lifetime / cross-boundary tracing.** For each mutable flag/buffer/handle it asked *"set in generation N — when is it consumed, and can generation N+1 consume it instead?"* The four `expecting*` flag leaks and the cross-generation `LineBuffer`/`Process` bleed are all this lens.

4. **Reciprocal-completeness.** *Every* set needs a guaranteed consumer; every breaker-open a reset; every increment exactly once. Codex flagged the *missing reciprocal*: a flag set when no exit will consume it; a breaker with no reset path; one failure counted twice.

5. **End-to-end consequence past the function/diff boundary.** *"ping before the venv is bootstrapped → `Process.run` throws → breaker opens → nothing resets it → worker dead until app restart."* It chased the consequence across `Server` → `WorkerManager` → bootstrap, not just within the changed file.

**Why Claude's six agents still missed it.** The angles partitioned by *topic* (security, correctness, …), not by *method*. A "correctness" reviewer still read control flow linearly and **trusted the generation guards** ("there's a guard, so it's handled") instead of constructing the schedule under which the guard doesn't hold. Breadth across topics ≠ depth at a single join point. Six shallow passes missed what one deep interleaving pass caught.

---

## 3. Finding taxonomy → the bug classes

The ~19 findings collapse to five classes, each with the lens that catches it:

- **A. Old generation's async tail corrupts the new one** (stale exit fires new gen's callback; buffer/handle reused across generations). Lens: *state-lifetime / cross-boundary*.
- **B. `ready` vs `exit` race** (dead worker marked running, in both the buffered and waiter-installed orderings). Lens: *re-entrancy + adversarial schedule*.
- **C. Acting before an in-flight op concludes** (dispatch fails instead of joining a respawn; swap abandons instead of draining). Lens: *re-entrancy ("did I wait for the concurrent thing?")*.
- **D. Breaker counting / reset** (one timeout counted twice; breaker never resets). Lens: *reciprocal-completeness*.
- **E. Expected-death flag leaks** (a flag set with no consuming exit leaks into the next generation). Lens: *state-lifetime + reciprocal-completeness*.

Plus the cross-cutting **end-to-end** lens (D's env-not-ready consequence) and **cross-language parity** (Swift↔Python validators drifted).

---

## 4. Proposed new dd review angles (the deliverable)

Add these as **method-angled** reviewers (alongside the existing topic-angled ones). Each is a *procedure*, not a posture — the current `adversarial-review` skill supplies posture ("presume a flaw") but no interleaving procedure, which is the gap.

### Angle 1 — Interleaving / "evil scheduler"
**Targets:** async, actors, callbacks, timers, locks.
**Procedure:** (a) enumerate the async events (each callback, timer fire, external continuation-resume, `await` completion); (b) list every **suspension point** (`await`) in each method; (c) for each pair of events that can race, write the *worst* ordering and check the invariant survives it. Output the schedule, not just the verdict.
**Catches:** B, C, and most of A.

### Angle 2 — State-lifetime & cross-boundary leak
**Targets:** any long-lived object managing a *sequence* of sub-lifetimes (generations, sessions, connections, requests).
**Procedure:** for each mutable field, build a tiny table: *set where / read where / cleared where / scoped to which identity*. Flag any field whose **set is not guaranteed to be followed by its consume**, or that is **shared across an identity boundary without being keyed to it**.
**Catches:** A, E.

### Angle 3 — Reciprocal-completeness
**Targets:** any open/close, acquire/release, set/consume, increment/reset pair.
**Procedure:** list the reciprocal pairs; for each, prove **both directions exist and fire exactly once on every path** (including error/early-return paths). Specifically hunt: a flag with no guaranteed consumer; a terminal state with no exit; a counter that can double-count.
**Catches:** D, E.

### Angle 4 — End-to-end consequence (past the diff)
**Targets:** a changed component whose failure mode is only visible downstream.
**Procedure:** for each new failure/early-return, trace the consequence across module boundaries to a **user-observable** outcome and name it. "Throws here" is not a finding; "throws here → … → stuck until restart" is.
**Catches:** D (env-not-ready), and class of "locally fine, globally broken."

### Angle 5 — Cross-mirror parity
**Targets:** logic duplicated across languages/components (validators, config mirrors, wire contracts).
**Procedure:** diff the **rules** element-by-element (bounds, finiteness, allow-lists), not just the field shapes. A field present on both sides is not parity; the *validation* must match.
**Catches:** the Swift↔Python validation drift.

**Process change, independent of angles:** Codex's gate was **iterative + blocking** (re-review the new state until clean). Claude's Gate-5 was one-shot. The block-until-clean cadence is what forced convergence — and what surfaced the *recurrence*. The dd `pre-pr` tier already does this; the in-session tiers should too for concurrency-heavy diffs.

---

## 5. Honest complementarity (don't over-correct)

Claude's reviews were **not** worthless — they caught a real input-validation crash, real doc-accuracy drift, and necessity issues Codex never raised, and they correctly *rejected* weak findings with rationale (a discipline Codex's blocking gate doesn't model — it has no "won't-fix with reason"). The goal is **additive**: bolt the five method-angles above onto the existing topic-angles so the suite gains interleaving depth **without** losing breadth, claim-checking, and necessity-pruning.

A cheap heuristic for *when* to spend the expensive interleaving angles: **does the diff contain async/actor/callback/timer/lock state that outlives a single call?** If yes (this chunk: very yes), run Angles 1–3 deeply on every join point. If no, the topic-angles suffice.

---

## 6. Open questions for building the catalog out

- Can Angles 1–3 be made into a **checklist a sub-agent reliably executes**, or do they need a different *kind* of reviewer (more reasoning budget per join-point, fewer parallel passes)? This session suggests **depth-per-join-point > breadth-across-topics** for concurrency — which argues for a single deep reviewer, not six parallel ones.
- Should the dd skill **detect** concurrency-bearing diffs (async/actor/lock keywords) and auto-escalate to the interleaving angles?
- How to capture "reciprocal-completeness" as a mechanical pass (it's close to a linter: every `X = true` flag wants a guaranteed `X = false` consumer on all paths).
- Track recurrence: when a fix is a local patch vs. a class fix. The double-count recurrence is the cautionary tale — a "did this fix the instance or the class?" prompt belongs in `receiving-code-review`.

---

*Seed written 2026-06-17 from the step-11 `meeting-pipeline` session. Findings detail lives in `plans/2026-06-15-step-5-11-ml-worker-runtime.md` (the codex-gate remediation + root-cause-refactor blocks).*
