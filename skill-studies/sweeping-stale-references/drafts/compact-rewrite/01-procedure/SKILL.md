---
name: sweeping-stale-references
description: Use when changing a load-bearing fact that appears in multiple places — renaming a symbol (rename refactor, find references, find usages), updating a documented behavior, changing a schema, amending a spec constraint, propagating a cascading change. Also when a reviewer flags ONE stale reference, before fixing it.
---

# Sweeping Stale References

A changed fact can leave code, documentation and tooling disagreeing.
A reviewer’s citation is one sample: search the repository, reconcile its consumers together, and leave an auditable account.
Initial factual grounding belongs to `disciplined-research`; the reason for changing the fact belongs to `writing-explicit-rationale`.

## 1. Search

Before editing, search old and intended new encodings, including plausible synonyms and language/path variants.
Cover code, docs/comments, tests/fixtures, config, scripts, CI and build files, including vendor/archive matches.
New-form hits can reveal existing consumers, collisions or partial migrations.

Read enough context to determine each match’s meaning.
If a snippet omits part of a claim or code block needed for that judgment, read the complete claim/block and compare its quantities, conditions and outcomes with the settled fact.
A heading matching an old/new form still needs triage; adjacent navigation/context that neither matches nor encodes the fact is not an extra reference.

## 2. Triage

Give every mutable-tree match one outcome:

- `update` — a consumer must change;
- `already current` — the same fact already has the intended meaning; preserve it;
- `false positive: <reason>` — the search form means something else;
- `intentionally stale: <reason>` — an old fact deliberately retained, such as historical design or migration context.

Commit messages, PR descriptions and chat logs are immutable history, outside this inventory.
Vendor/archive matches still need disposition.

## 3. Reconcile

Update every affected consumer, including differently worded descriptions and relative links after a move.
Preserve attached rationale’s distinct causes, constraints and accepted costs/downsides with the replacement or its explanation; labels alone do not preserve meaning.
An unchanged attached rationale line is not another false positive merely because it lacks the old encoding.

Before committing, repeat relevant old/new searches and check the resulting claims against the settled fact.
Commit all updates together.
Record only verification actually performed and results observed.

## Commit account

Put `References swept:` after narrative and before `Verification:`.
Account for every mutable-tree match; count each reference once across repeated searches.
Group only by the same path and outcome, retaining precise locations and counts.
State audited old → new encodings for updates, using faithful language-specific forms.

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
If all mutable-tree matches are in the changed file, the required account is `References swept: n/a — change affects only this file.`
Any outside-file match, including an unchanged or unrelated one, requires the positive inventory.
Group before exceeding the normal commit-body preference; necessary audit evidence may still exceed it.

For a read-only proposal, report observed matches, intended encodings and outcomes; distinguish proposed/applied/outstanding status only from supplied file state.
A sweep alone does not establish broader branch readiness or a blocker.

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
