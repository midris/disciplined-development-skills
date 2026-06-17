# adversarial-review — validation

Records how the `adversarial-review` angle set was derived and how to re-validate
it. The skill is standalone/portable: a consumer with only the skill can run a
review, name an angle, or list the angles, with no `/dd-review` dependency.
Dispatch/orchestration is validated in [dd-review-command.md](dd-review-command.md).

**Dispatch protocol.** Read-only and bounded per CLAUDE.md's evaluation-subagent
rule (Claude Code: `Explore`). One scenario per agent, text-only.

## The angle-necessity bar

An **angle earns its place only if it catches a class of issue the baseline
holistic review reliably misses.** The baseline is the always-on posture +
Rules (find what's wrong · enumerate every class · verify rationale · challenge
necessity). The test for an angle is **discrimination vs holistic**: plant a
*subtle* instance of the angle's class, then keep the angle only if a focused
reviewer catches it AND a holistic reviewer misses it. Goal: close the lenses
that make different models (codex vs claude) catch different things, so the
reviewer is model-consistent.

## Audit (2026-06-16/17)

Ran discrimination tests (holistic RED vs angle GREEN) on subtle planted targets
for seven candidate angles.

**Holistic caught the target in 6/6 of correctness, rationale, cross-file/
consistency, security, executability, necessity — and 4/4 conformance** (incl. a
noisy multi-issue diff, two independent holistic runs). Lesson: **per-angle
discrimination on a small artifact is the wrong instrument** — a strong model
following the posture catches everything when there's nothing to dilute its
attention. It discriminates only for (a) **scope** changes to a definition, and
(b) **specialized lenses the posture lacks**.

**Decisions:**

| Angle | Verdict | Why |
|---|---|---|
| correctness | **dropped** | the posture *is* "find what's wrong" — holistic caught it |
| rationale | **dropped** | already base posture Rule "Verify every rationale claim" |
| necessity | **dropped (as angle)** | already base posture Rule "Challenge necessity"; its Principle-7 + concise-writing pointers folded into that Rule |
| conformance | **dropped** | "verify against governing rules" is posture; holistic caught 4/4 |
| security | **deferred** | claude finds low-hanging secrets via posture; real leverage is a dedicated security skillset applied explicitly, not a one-line angle |
| **consistency** | **kept** | cross-corpus drift (contract/terminology/wording/single-source) is *not* in the posture; manually prompting it reliably yields findings |
| **executability** | **kept** | the zero-context-implementer lens; surfaced by the maintainer's codex-review gap observations (not reproduced inline here) |
| **skill-authoring** | **kept** | the **only** angle that beat holistic in discrimination — see below |

`security` was broadened (+ leaked secrets/keys) and tested cleanly (old def
returned "No findings" on a hardcoded key; broadened def flagged it P0) — so the
broadening *is* load-bearing — but the angle was still dropped per the bar above:
holistic already catches secrets, and a future dedicated security skill is the
higher-leverage home.

The pre-branch command also had `cross-file` and `doctrine-consistency`; both
folded into `consistency` (their drift / single-source concerns), and the
governing-rule half of `doctrine-consistency` became `conformance`, then dropped.

## skill-authoring discrimination (the one that passed)

Planted a skill whose `description` summarized the workflow and whose rule
("Always run the tests") had no rationalization-loophole counters.

- **Holistic (RED):** flagged executability/consistency issues but **missed** the
  CSO trap (description-summarizes-workflow → agents skip the body) and framed the
  open rule as a P3 "discipline smell," not as exploitable loopholes.
- **skill-authoring (GREEN):** caught both — the CSO trap and the open
  rationalization loopholes — applying the `superpowers:writing-skills` lens.

Holistic missed what the angle caught → it earns its place.

## Standalone angle selection

- **RED — pre-edit skill, doc-dominant artifact:** with selection delegated to the
  command, a skill-only agent **guessed** and excluded the right doc angle.
- **GREEN — post-edit skill:** the **When to apply** list lets a skill-only agent
  select correctly and answer "what angles are available?" — the portability goal.

## Per-angle focus (kept angles catch their target)

Each angle's definition transmits the right focus (a reviewer applying it catches
its class):

| Angle | Target | Result |
|---|---|---|
| consistency | terminology drift across the corpus; keyword-only arg passed positionally (cross-file) | ✓ flagged |
| executability | doc step with undefined deps / no command | ✓ flagged |
| skill-authoring | CSO description trap + open rationalization loopholes | ✓ flagged (holistic missed) |

## On edits

- Adding/refining an angle: run the **discrimination test** (subtle target,
  holistic RED vs angle GREEN). Keep only if holistic misses it. Back the decision
  with cross-model (codex) gap data where available.
- Changing the **When to apply** list or a definition: re-run the standalone
  selection RED/GREEN and the affected per-angle scenario.
- Limitation: small-artifact discrimination can't validate *coverage* value (it
  appears only at scale / across models). consistency and executability are kept on
  the lens-not-in-posture + codex-gap grounds, not on demonstrated single-reviewer
  discrimination; skill-authoring is the one with a clean discrimination result.
