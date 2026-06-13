---
name: sweeping-stale-references
description: Use when changing a load-bearing fact that appears in multiple places — renaming a symbol (rename refactor, find references, find usages), updating a documented behavior, changing a schema, amending a spec constraint, propagating a cascading change. Also when a reviewer flags ONE stale reference, before fixing it.
---

# Sweeping Stale References

**Role:** Companion — invoke when changing a fact that appears in multiple places, OR when a reviewer flags one stale reference.
**Owns:** the Search / Triage / Reconcile procedure, the `References swept:` commit-body format, the required `n/a` negative-form line, the loop-of-fixes anti-pattern framing.
**Does not own:** the initial grounding of a load-bearing fact before it changes (lives in `disciplined-research`); the rationale for WHY a fact was changed (lives in `writing-explicit-rationale`).

## Overview

Reviewers see the diff; you see the world. When a fact changes, every
place encoding it goes stale. Sweep every stale reference and reconcile
in one commit. Single-citation point fixes leave the **loop-of-fixes
anti-pattern**: each review round catches one more.

## Quick reference

| Situation | Do |
|---|---|
| About to commit a rename / schema / spec / doc-claim change | Grep first, before editing |
| Reviewer flags ONE stale citation | Grep for siblings before fixing the cited one |
| Single-file change | Commit body line: `References swept: n/a — <reason>` |
| Multi-file change | Commit body section: `References swept:` with one line per match, each tagged `update` / `false positive: <reason>` / `intentionally stale: <reason>` |

## Procedure

Three steps. Don't skip any.

**1. Search.** Use any tool (grep, rg, ag, IDE find-references) —
thoroughness matters, not which tool. Cast wide across code, docs,
tests/fixtures, AND config/scripts/CI/build files (this last category
is easy to miss because it's not in the "obvious file types"). Search
the literal old string AND likely synonyms — a renamed `getUser` may
also appear as `"user fetcher"` in prose or `get_user` in Python
bindings.

**2. Triage.** For each match, label the outcome:

- `update` — real consumer; update it.
- `false positive: <reason>` — match shares the search term but
  refers to something else.
- `intentionally stale: <reason>` — real reference to the old fact,
  deliberately preserved. Rare. Examples: historical postmortems,
  archived completed-plan files, migration notes describing past
  state.

**3. Reconcile in one commit.** All updates land together. Document
every match in the commit body's `References swept:` section.

## What counts as a reference

| ✅ In scope | ❌ Out of scope |
|---|---|
| Code symbol references — callsites, type users, schema users, imports | Commit messages, PR descriptions, chat logs (immutable history; rewriting is worse than leaving stale) |
| Doc + comment citations — READMEs, architecture docs, plans, specs, code comments | |
| Test fixtures + assertions — hard-coded values, mock returns, fixture JSON, snapshots | |
| Config + build files — env-var names, CLI flags, schema keys, CI references | |

**Vendor / archive directories** are usually OK to skip — annotate
each as `false positive: out of scope (vendor|archive)` so the audit
trail records that you considered them.

## Output artifact

The `References swept:` section in the commit body:

```
References swept:
- path/to/file.ext:LINE — <outcome>
- ...
```

`<outcome>` uses the three labels from Procedure step 2 (`update` /
`false positive: <reason>` / `intentionally stale: <reason>`),
optionally with a short note like `update (declaration)` or
`update (3 assertions)`.

**Single-file or no-sweep case (required negative form):**

```
References swept: n/a — change affects only this file.
```

The `n/a` line is **required, not optional** — its absence reads
identically to "I forgot to sweep."

**Placement:** `References swept:` goes after the narrative body and
before `Verification:`. Sweep is part of the correctness story;
verification is proof the result works.

### Worked example

Renaming `auth.getUser` → `auth.fetchUser` for naming consistency:

```
refactor(auth): rename getUser → fetchUser for naming consistency

Every other lookup function in the auth package uses fetch*
(fetchSession, fetchToken). getUser was the outlier; rename for
consistency.

References swept:
- backend/auth/user.go:42 — update (declaration)
- backend/auth/user.go:67 — update (internal caller in validateSession)
- backend/auth/user_test.go:18,34 — update (2 test functions renamed)
- backend/auth/user_test.go:22,38 — update (2 assertions)
- backend/api/handlers/login.go:103 — update (callsite)
- backend/api/handlers/profile.go:55 — update (callsite)
- ARCHITECTURE.md:201 — update (doc citation in Auth section)
- README.md:78 — update (API example)
- plans/completed/auth-redesign.md:142 — intentionally stale: completed plan, captures the design as it was at the time
- docs/migrations/v1-to-v2.md:8 — false positive: refers to the SQL getUser stored procedure, not the helper
- scripts/ci-test-filter.sh:12 — update (CI test-name filter)

Verification:
- go test ./auth/... ./api/... → all pass
- grep -rn 'getUser' --include='*.go' --include='*.sh' → 0 hits

Co-Authored-By: ...
```

## Rationalizations

| Excuse | Reality |
|--------|---------|
| "The reviewer only flagged one citation." | The reviewer reads the diff; you read the world. Sweep before fixing only the cited line. |
| "I'll fix the obvious places and let tests catch the rest." | Tests pass against stale fixtures silently. Grep is the only way. |
| "I checked the obvious places." / "I checked the obvious file types." | "Obvious" is what your eye lands on; grep doesn't have selective attention. Cast wide across both locations and file types — config, scripts, CI, build files encode the same facts and miss silently. |
| "The IDE handled the rename." | IDE rename refactors code symbols. They don't touch docs, comments, plain-string fixtures, plan files, CI scripts, or anything non-indexed. |
| "Other matches are obviously different references." | Maybe — annotate each as `false positive: <reason>` in the commit body. Don't skip silently; the audit trail is the proof. |
| "It's only in tests." | Tests encode the old fact. Passing tests against stale fixtures is the loudest form of silent rot. |
| "It's just a doc edit / typo." | Docs are first-class consumers. The claim probably appears in 3+ other docs and a code comment. Sweep. |
| "I'll add a TODO and sweep later." | Later = never. The commit lands inconsistent; `git bisect` lands readers on a half-finished state. |
| "Probably already has it." / "The plan implicitly covers it." | Implicit isn't covered. Grep. If the sweep finds zero matches, that's a `References swept: n/a` line, not silence. |
| "Sweep is overkill for this small change." | The skill applies on the basis of *what the change touches*, not on size. A single-line schema rename can have 30 consumers. |

## Red flags

Earlier warning signs — stop if any cross your mind:

- "Just this one citation."
- "The other places aren't really the same thing."
- "I'll get to the rest in a follow-up."
- "The reviewer would have caught more if there were more."
- "I already updated everything I could think of."
- "Single-file change, no sweep needed." (without writing the `n/a` line)

## References

- [`references/sweep-check-hook-design.md`](references/sweep-check-hook-design.md) — deferred design for a pre-commit hook that enforces the `References swept:` audit trail automatically.
