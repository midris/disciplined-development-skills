---
name: sweeping-stale-references
description: Use when changing a load-bearing fact that appears in multiple places — renaming a symbol (rename refactor, find references, find usages), updating a documented behavior, changing a schema, amending a spec constraint, propagating a cascading change. Also when a reviewer flags ONE stale reference, before fixing it.
---

# Sweeping Stale References

Finish with every current consumer expressing the settled fact, historical and unrelated meanings preserved, and an accurate account of the sweep.
A reviewer’s one stale citation does not bound the repair.
Initial factual grounding and the reason for changing it remain with `disciplined-research` and `writing-explicit-rationale`.

## Find the consumers

Search before editing across code, docs/comments, tests/fixtures, config, scripts, CI and build files, including vendor/archive directories.
Search old and intended new encodings, synonyms and language/path variants; new forms expose existing uses, collisions and partial migrations.
Inspect each match in enough context to compare its meaning with the settled fact.
When a snippet cannot establish disposition, expand to the complete claim/block, including quantities, conditions and outcomes.
Triage matching headings too; adjacent navigation/context is not a reference unless it matches or encodes the fact.
Exclude immutable commit messages, PR descriptions and chat logs.

## Give every match a disposition

| Outcome | Meaning |
| --- | --- |
| `update` | A real consumer must change. |
| `already current` | The same fact already expresses the intended state; preserve it. |
| `false positive: <reason>` | The search form refers to something else. |
| `intentionally stale: <reason>` | The old fact is deliberately preserved, such as historical design or migration context. |

Update all affected consumers, including equivalent prose and relative links after moves.
Keep attached rationale’s distinct causes/constraints and accepted costs/downsides with the replacement or its explanation; a label is insufficient.
Unchanged attached rationale without an old encoding is not a separate false positive.
Repeat relevant old/new searches and inspect resulting claims before committing all updates together.

## Leave the evidence

In the commit body, place `References swept:` after narrative and before `Verification:`.
List each observed path/outcome group with precise locations and counts, counting references once across repeated searches.
Never group across paths or outcomes.
For updates, give the audited old → new encoding or faithful language-specific form.

```text
References swept:
- path:LINES — update `old` → `new` (N matches)
- path:LINES — already current: <intended state> (N matches)
- path:LINES — false positive: <reason> (N matches)
- path:LINES — intentionally stale: <reason> (N matches)

Verification:
- <check actually performed and observed result>
```

Include only observed groups.
Use the mandatory `References swept: n/a — change affects only this file.` only if every mutable-tree match is in that changed file.
Outside-file matches require a positive inventory even when preserved or unrelated.
Group first; a broad audit may exceed the normal commit-body preference when detail remains necessary.
Claim only checks/results actually observed; reference disposition alone establishes neither broader readiness nor a blocker.
For read-only work, report matches and proposed encodings/outcomes, claiming applied/outstanding status only when supplied file state establishes it.

## Rationalizations

| Excuse | Reality |
|--------|---------|
| "The reviewer only flagged one citation." | The reviewer reads the diff; you read the world. Sweep before fixing only the cited line. |
| "I'll fix the obvious places and let tests catch the rest." | Tests pass against stale fixtures silently. Grep is the only way. |
| "I checked the obvious places." / "I checked the obvious file types." | "Obvious" is what your eye lands on; grep doesn't have selective attention. Cast wide across both locations and file types — config, scripts, CI, build files encode the same facts and miss silently. |
| "The IDE handled the rename." | IDE rename refactors code symbols. They don't touch docs, comments, plain-string fixtures, plan files, CI scripts, or anything non-indexed. |
| "Other matches are obviously different references." | Maybe — account for each path/outcome group as `false positive: <reason>` in the commit body. Don't skip silently; the audit trail is the proof. |
| "It's only in tests." | Tests encode the old fact. Passing tests against stale fixtures is the loudest form of silent rot. |
| "It's just a doc edit / typo." | Docs are first-class consumers. The claim probably appears in 3+ other docs and a code comment. Sweep. |
| "I'll add a TODO and sweep later." | Later = never. The commit lands inconsistent; `git bisect` lands readers on a half-finished state. |
| "Probably already has it." / "The plan implicitly covers it." | Implicit isn't covered. Grep. If the sweep finds zero matches, that's a `References swept: n/a` line, not silence. |
| "Sweep is overkill for this small change." | The skill applies on the basis of *what the change touches*, not on size. A single-line schema rename can have 30 consumers. |
