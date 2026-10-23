---
name: sweeping-stale-references
description: Use when changing a load-bearing fact that appears in multiple places — renaming a symbol (rename refactor, find references, find usages), updating a documented behavior, changing a schema, amending a spec constraint, propagating a cascading change. Also when a reviewer flags ONE stale reference, before fixing it.
---

# Sweeping Stale References

Treat a changed fact or one reviewer citation as a repository-wide consistency question.
The result is complete reconciliation, preserved unrelated/history meanings and an inspectable account.
Grounding the fact belongs to `disciplined-research`; explaining why it changes belongs to `writing-explicit-rationale`.

## Before editing

- Search old and intended new encodings, synonyms and language/path variants across code, docs/comments, tests/fixtures, config, scripts, CI and build files. New-form hits expose existing uses, collisions and partial migrations.
- Include vendor/archive matches; exclude immutable commit messages, PR descriptions and chat logs.
- Inspect enough surrounding context to establish meaning. If a snippet is insufficient, read the complete claim/block and compare quantities, conditions and outcomes with the settled fact. Matching headings require triage; adjacent context that neither matches nor encodes the fact is not another reference.
- Assign every mutable-tree match: `update`; `already current` (same fact, intended state; preserve); `false positive: <reason>` (different meaning); or `intentionally stale: <reason>` (deliberately retained old meaning, such as historical design or migration context).

## Before committing

- Reconcile every affected consumer, including equivalent prose and relative links after moves.
- Preserve attached rationale’s distinct causes/constraints and accepted costs/downsides with the replacement or explanation. Labels alone are insufficient; unchanged rationale without the old encoding is not a separate false positive.
- Repeat relevant old/new searches and inspect the resulting claims against the settled fact.
- Commit all updates together, with `References swept:` after narrative and before `Verification:`. Account for every mutable-tree match, counting each reference once across repeated searches. Group only by the same path/outcome, with precise locations, counts and audited old → new encodings or faithful language-specific forms for updates.

```text
References swept:
- path:LINES — update `old` → `new` (N matches)
- path:LINES — already current: <intended state> (N matches)
- path:LINES — false positive: <reason> (N matches)
- path:LINES — intentionally stale: <reason> (N matches)

Verification:
- <check actually performed and observed result>
```

Include only observed outcome groups.
Use the mandatory `References swept: n/a — change affects only this file.` only when all mutable-tree matches are in the changed file.
An outside-file match requires a positive inventory even if unrelated or unchanged.
Group before exceeding the normal commit-body preference; necessary audit detail may still exceed it.

For read-only proposals, report matches and intended encodings/outcomes, claiming applied/outstanding status only from supplied file state.
Report only verification actually observed; a sweep establishes neither broader readiness nor a blocker.

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
