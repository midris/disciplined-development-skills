---
name: sweeping-stale-references
description: Use when changing a load-bearing fact that appears in multiple places — renaming a symbol (rename refactor, find references, find usages), updating a documented behavior, changing a schema, amending a spec constraint, propagating a cascading change. Also when a reviewer flags ONE stale reference, before fixing it.
---

# Sweeping Stale References

When a fact changes, find its consumers beyond the reported defect.
A reviewer’s citation is one sample, not the repair boundary.
Initial factual grounding belongs to `disciplined-research`; the reason for changing the fact belongs to `writing-explicit-rationale`.

## 1. Search before editing

Search old and intended new forms, synonyms and language/path variants across code, docs and comments, tests and fixtures, config, scripts, CI and build files.
Use semantically specific terms and any effective search tool; new forms expose existing uses, collisions and partial migrations.

Inspect enough context to compare each match’s meaning with the settled fact.
If a snippet cannot establish disposition, read the complete claim or code block, including quantities, conditions and outcomes.
Triage matching headings; adjacent context that neither matches nor encodes the fact is not another reference.

## 2. Triage every match

- `update` — a consumer must change;
- `already current` — the same fact already expresses the intended state; preserve it;
- `false positive: <reason>` — the search form refers to something else;
- `intentionally stale: <reason>` — an old fact deliberately preserved, such as historical design or migration context.

Include vendor/archive matches.
Exclude immutable commit messages, PR descriptions and chat logs.

## 3. Reconcile and verify

Update every affected consumer, including equivalent prose and relative links after moves.
Preserve attached rationale’s distinct causes or constraints and accepted costs or downsides with the replacement or its explanation; labels alone are insufficient.
Unchanged attached rationale lacking the old encoding is not a separate false positive.

Before committing all updates together, repeat relevant old/new searches and inspect the resulting claims against the settled fact.

## Commit account

Put `References swept:` after narrative and before `Verification:`.
Account for every mutable-tree match, counting each reference once across repeated searches.
Group only by the same path and outcome, with precise locations and counts.
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
If all mutable-tree matches are in the changed file, use the mandatory negative form:

```text
References swept: n/a — change affects only this file.
```

Any outside-file match, including a preserved or unrelated one, requires a positive inventory.
Group before exceeding the normal commit-body preference; necessary audit detail may still exceed it.

Claim only verification actually observed; reference disposition alone establishes neither broader branch readiness nor a blocker.
For read-only proposals, report matches and intended encodings and outcomes, claiming applied or outstanding status only from supplied file state.

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
