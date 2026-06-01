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

- **Skill/reference authoring is out of scope.** For it, use
  `superpowers:writing-skills`; do not invoke concise-writing separately. Skill
  prose is the every-word-counts extreme, and writing-skills enforces its own
  stricter token-efficiency bar there. (This matches the SKILL.md description's
  "use that there, not this." The boundary is settled — re-tweaking its wording
  is drift.)
- **Length (~900 words) is accepted** over an aggressive shrink. Only the
  description is always-on; the body loads on invocation, so the frequently-loaded
  <200-word target does not apply. A worked before/after example was kept for
  teaching value over a smaller word count.

## On edits

Re-run the relevant probe before shipping any change: verbosity delta + over-trim
for rule/content edits, routing for description/trigger edits.

## Appendix — captured run (cache-eviction build domain)

The skill was written against this baseline. Task: a "Cache Eviction" README
subsection from 6 fixed facts (LRU; capped at `MAX_CACHE_SIZE_MB`; evict-on-write
until under cap; last-access timestamp updated per read; atomic temp+rename;
synchronous on the write path), under "be thorough/clear for junior engineers."

This is a technique skill, so the baseline failures are the padding behaviors
themselves — agents wrote padded prose without verbal justification, not under-
pressure rationalizations. The patterns in SKILL.md map 1:1 to what was observed.

**RED (no skill) — representative excerpt (~310 words full):**

> ## Cache Eviction
> The cache is bounded by a least-recently-used (LRU) eviction policy. This
> section explains how that policy works and the invariants you need to preserve
> when changing cache code.
> ### Size cap
> The total size of the cache is capped at the value of the `MAX_CACHE_SIZE_MB`
> config setting. The cache is allowed to grow up to this limit; once it would
> exceed the limit, the service reclaims space by evicting entries (see below).
> ### Tracking recency
> Every cache entry records a **last-access timestamp**. […LRU re-defined here…]
> ### Eviction runs synchronously
> […] As a result, a write that triggers eviction does more work — and takes
> longer […]. Keep this in mind when reasoning about write latency, and do not
> assume eviction happens "later" in the background.

Failure modes observed (verbatim → pattern):
1. Meta-framing — *"This section explains how that policy works and the invariants you need to preserve…"*
2. Say-it-twice — Size-cap restated within the same paragraph.
3. Cross-section duplication — LRU defined in the intro **and** again under "Tracking recency."
4. Over-sectioning — 4 headed subsections for 6 facts.
5. Unrequested elaboration — *"Keep this in mind when reasoning about write latency, and do not assume eviction happens 'later'…"* (advice past the 6 facts).
6. Emphasis inflation — scattered bold.

**GREEN (skill applied) — full output (~120 words, all 6 facts, 0 patterns):**

> ## Cache Eviction
> The cache uses LRU (least-recently-used) eviction. Total cache size is capped
> at the `MAX_CACHE_SIZE_MB` config value. Each cache entry records a last-access
> timestamp, which is updated on every read — this is what "recently used" is
> measured against.
> On each cache write, the service checks total cache size against the cap. If the
> cache is over the cap, it evicts entries in least-recently-used order (oldest
> last-access timestamp first) until the cache is back under the cap. Eviction
> runs synchronously on the write path, not in a background worker, so a write
> that pushes the cache over the cap performs the eviction before it returns.
> Cache writes are atomic: the service writes to a temp file, then renames it
> into place.

A later effectiveness pass re-ran the same method on an unseen domain (webhook
retries) with agents reading the verbatim `SKILL.md`, reproducing the cut with
zero fact loss — confirming the skill addresses observed failures, not a
domain it was tuned on.
