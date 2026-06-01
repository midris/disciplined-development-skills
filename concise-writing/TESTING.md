# concise-writing — validation

Built and maintained test-first per `superpowers:writing-skills` (skills are TDD
for process docs: no skill — and no edit — without a failing test first). This
records the trail so the rationale is recoverable from the bundle.

## Method

- **Verbosity delta** — a blind subagent writes a short doc section from a fixed
  fact list, once without the skill (RED) and once applying it (GREEN), under a
  "be thorough/clear for junior engineers" pressure that elicits padding. Use a
  domain the skill's own examples don't cover, or the test is contaminated.
- **Over-trim probe** — a subagent edits a padded multi-section draft that also
  contains a load-bearing recap + an orienting sentence. Confirms the guard cuts
  padding without stripping framing.
- **Routing probe** (for description/trigger edits) — give a subagent only the
  description + a skill-editing task; check it routes correctly rather than
  mishandling the boundary.

## Results

- **RED (no skill):** ~230–310 words for ~130 words of facts — meta-framing
  openers, restated facts, cross-section duplication, unrequested elaboration.
  Cross-section duplication appeared organically, confirming the global-altitude
  check is needed.
- **GREEN (skill, fresh unseen domain):** ~80–140 words, all facts preserved,
  named patterns absent. Output also clustered tightly across runs where
  baselines varied with each writer's natural padding.
- **Over-trim:** padding cut; recap + orienting framing kept verbatim. No
  loophole.
- **Routing (description reword):** old "handled in the moment" wording left
  verbosity-handling vague; the shipped wording routes decisively to
  `superpowers:writing-skills` as the stricter owner.

The win is largest against padded baselines and shows as consistency against
already-lean ones — not a fixed percentage.

## Deliberate calls (recorded so reviewers don't re-litigate)

- **Skill/reference authoring is out of scope**, owned by
  `superpowers:writing-skills`. Skill prose is the every-word-counts extreme; a
  stricter, separate discipline handles it. The description routes there rather
  than excluding concision.
- **Length (~900 words) is accepted** over an aggressive shrink. Only the
  description is always-on; the body loads on invocation, so the frequently-loaded
  <200-word target does not apply. A worked before/after example was kept for
  teaching value over a smaller word count.

## On edits

Re-run the relevant probe before shipping any change: verbosity delta + over-trim
for rule/content edits, routing for description/trigger edits.
