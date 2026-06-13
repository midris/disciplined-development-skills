---
name: disciplined-research
description: Use before stating any load-bearing fact in a commit, plan, spec, doc, PR body, code review comment, README, code edit, status update, or summary — project claims (schema, handlers, fixtures, file contents, git history, summaries, quotes, recaps) or external/web claims (library versions, framework features, CLI behavior, current public state). Especially when stating specifics another reader will quote downstream without re-verifying.
---

# Disciplined Research

**Role:** Companion — invoke when about to state a load-bearing claim.
**Owns:** the two-domain source-ranking taxonomy (project; external / web), the acquire-vs-verify distinction, the recency + version-applicability axis, the destination-defines-load-bearing test.
**Does not own:** the sweep procedure for facts that later change (lives in `sweeping-stale-references`); the on-page rationale for design decisions citing the research (lives in `writing-explicit-rationale`).

## Overview

Load-bearing claims become ground truth for whoever reads them next —
human or agent. They won't re-verify; they'll quote.

**Core principle:** ground every load-bearing specific in **current
source**, not memory, training data, or peer-fed framing. Recall orients
you toward sources; recall is not itself a source.

Two failure modes recur and compound:

1. **Confabulation** — stating a specific from memory or inference when
   you don't have a current source for it.
2. **Stale citation** — stating a specific that was true once, but the
   source has moved since.

## When this applies

**Project.** Everything inside this project — schema, handlers, file
contents, config, git history, fixtures, plans, specs, summaries, status
recaps, policy / spec quotes, dashboard numbers, "what we decided last
session." Ground in fresh reads of the actual file, record, transcript,
plan, or running system — not in auto-loaded `MEMORY.md` or session-recap
recall.

In code work specifically, this manifests as:

- Re-read schemas (`db.go`, models, migrations) before describing table
  shape, columns, keys, or constraints in a commit message, plan, or doc.
- Re-read handlers before describing endpoint behavior, response shape,
  status codes, or error semantics. Don't infer from function names.
- Re-read test fixtures before describing what they seed. Producer-shape
  mismatch is invisible from outside the fixture (the same posture as
  test-input fixtures matching producer shape).

**External / web.** Library versions, framework features, third-party
API behavior, CLI tool behavior, current LTS lines, recent events,
public stats.
Ground in the source-ranking hierarchy below — **binary for
local-behavior claims** (does this installed version actually do X?);
**canonical first-party docs / changelogs for current-public-state
claims** (what's the latest LTS / current stable / recent release?).
Never training-data recall, however confident-feeling.

**Cross-domain claims.** When a claim spans both — e.g., "our project's
Vite version" (`package.json` AND upstream stable) — verify both, don't
pick one silently.

The threshold test: **would a careful reviewer notice if I got this
wrong?** If yes, the claim is load-bearing. Verify before stating it.

## Two facets

Each maps to one failure mode: **acquire from source** for
confabulation, **verify before citing** for stale citation.

### Acquire from source

When you don't have a specific: **find it; don't infer it.** Two
parallel hierarchies (internal, external) share a similar shape —
running thing > implementation > docs > recall — with derivatives and
triangulation as middle tiers externally.

**Internal sources** (strongest to weakest):

- **Running system** — DB query, live API call, schema dump, file read.
- **Source code** — implementation.
- **This session's artifacts** — test output, build log, `git log`,
  command output.
- **Project docs** — CLAUDE.md, ARCHITECTURE.md, plans, specs. Re-verify
  for high-stakes; docs lag.
- **Conversation history this session** — re-read, don't recall.
- **Memory** (MEMORY.md, training recall) — never a source; use to
  orient.

**External sources** (strongest to weakest):

- **Binary / runtime** — actual invocation. `tool --help`,
  `tool --version`, observed output. Beats docs for **local-behavior
  claims** ("does this installed version actually have feature X?") —
  docs describe intent or past versions; the binary describes what
  THIS version runs. **Not authoritative for current-public-state
  claims** ("what's the current LTS / latest stable / current major
  version?") — local install may be old; canonical first-party
  docs/changelogs win for those.
- **Source on the official repo** — GitHub, project mirror.
- **Canonical first-party docs** — official site, README, changelog,
  release notes.
- **First-party derivatives** — maintainer blogs, conference talks
  (vetted first-party content with editorial control).
- **Triangulation** — third-party docs, current well-upvoted Stack
  Overflow. Corroborate; don't ground.
- **Avoid as source** — Reddit, ad-hoc social media posts, stale SO,
  AI-generated content, undated blog posts.

When tiers conflict, the higher tier wins.

**Recency + version-applicability is a second axis, orthogonal to tier.**
A 2-year-old maintainer blog post is first-party authoritative but may
describe a deprecated API. Two checks before relying on any web source:

- **Date check.** Undated → suspect. Older than the thing's most recent
  major version → triangulate.
- **Version check.** Does the claim still apply to the version we're
  using? Cross-reference the changelog for intervening versions.

Stale or version-mismatched sources demote to the triangulation tier;
re-ground in the binary or current changelog.

### Verify before citing

When you *do* have a specific in working memory: **check the source once
more before making it load-bearing.** "Load-bearing" means any of:

- Cited in a commit, plan, doc, spec, design note, PR body, or code
  review comment.
- Quoted to a user as fact.
- Used to drive a code edit ("X has field Y, so the migration needs Z").
- Referenced in a summary another agent will act on.
- Pasted into a README, status update, or public-facing artifact.

Destination defines load-bearing, **not prompt vocabulary or length.**
"Quick one-liner for the README" is load-bearing; "long internal scratch
pad I'll delete" is not.

Cite the source — URL, file path, invocation — so readers can
re-verify.

## Common rationalizations

| Excuse | Reality |
|---|---|
| "Based on the memory file…" / "From what I remember…" / (auto-loaded memory or training recall treated as source) | Recall is a snapshot from some prior moment. Auto-loaded `MEMORY.md` may be hours stale; training data may be a year stale. Use recall to orient toward sources, not as a source. |
| "The asker said it" / "The asker stated this as fact, so its truth isn't my problem." | A peer-fed claim becomes yours the moment you paste it into a load-bearing artifact. Inheriting the prompt's confidence is inheriting its risk — even when the peer sounds confident, even when the claim turns out to be right. |
| "Quick task / one-liner / snippet / casual writing / 'snippet for review' / 'one-line command' — not a production claim." | Length and vocabulary aren't claim weight. Destination is. A one-liner in a migration warning is more load-bearing than a 200-word internal scratch note. Trigger on destination (commit, plan, doc, PR, README, code review, public-facing artifact), not on prompt phrasing. |
| (silent — agent jumps straight to answer with no meta-commentary) | Silent verification-skip is worse than verbal: no internal flag fires. Producing a load-bearing answer with no source check? Stop and ground it. |
| "I have a confident-feeling answer — that's a sign it's reliable." | For continuously-drifting facts, confident-feeling recall is anti-correlated with accuracy. The more specific the recall (codenames, dates, numbers), the more it suggests pattern-matching a snapshot. Fetch fresh. |
| "I know what's in [file/env/config] I've been editing — no need to re-read." | The actively-touched surface is the one most likely to surprise. Cat / printenv / select-from before drawing conclusions about state. |

## Red flags

Earlier than the table. Stop if any of these crosses your mind:

- "I'm pretty sure…" / "If memory serves…" / "I think it's…" —
  uncertainty signal **before** verification has fired. Verify now.
- "Quick one-liner / snippet / short answer" — task framing pushing
  past the destination gate. Length isn't the gate; destination is.
- A specific version, date, codename, or flag name in your head, no
  source citation in your head — confident specificity without confident
  sourcing is the cleanest training-cutoff-drift signal.
- "The asker said X" — peer-claim acceptance. Verify the premise before
  relaying.
- Binary, runtime, or repo source is available and you're about to
  answer from recall — invocation beats recall.
- No source named in your response — if a future reader can't
  re-verify, the claim isn't grounded.
- "I know what's in [file I've been editing]" — state assumption on a
  surface you've been touching. Re-read first.
