---
name: sweeping-stale-references
description: Use when changing a load-bearing fact that appears in multiple places — renaming a symbol (rename refactor, find references, find usages), updating a documented behavior, changing a schema, amending a spec constraint, propagating a cascading change. Also when a reviewer flags ONE stale reference, before fixing it.
---

# Sweeping Stale References

**Role:** Companion — invoke when changing a fact that appears in multiple places, or when a reviewer flags one stale reference.
**Owns:** Search → Triage → Reconcile, the `References swept:` commit-body artifact, the required `n/a` form, and resistance to one-fix-at-a-time review loops.
**Does not own:** initial factual grounding (`disciplined-research`) or the rationale for changing a fact (`writing-explicit-rationale`).

## Contract

Reviewers see the diff; you must inspect the repository.
Before editing, search for every encoding of the changed fact.
Reconcile every mutable reference in one commit and account for the complete search in its `References swept:` evidence.
A reviewer finding is one sample, not the search boundary; fixing only that line creates a loop in which each review finds the next stale reference.

## Search → Triage → Reconcile

### 1. Search

Search before editing, then repeat the relevant searches after editing.
Tool choice does not matter; completeness does.

- Search every applicable literal old symbol or prose form and its likely synonyms.
- For each old form, search the intended new symbol or prose form too, before and after the change, to find pre-existing uses, collisions, partial migrations, and reconciliation context.
- Cover code, documentation and comments, tests and fixtures, config, scripts, CI, and build files.
- Use semantically specific forms; a nearby heading or generic component word is not a reference candidate unless it encodes the changed fact.

### 2. Triage

Give every mutable-tree match exactly one outcome:

- `update` — a real consumer that must change;
- `false positive: <reason>` — the search form refers to something else;
- `intentionally stale: <reason>` — a real old reference deliberately preserved, usually in a historical postmortem, completed plan, or migration note.

Code symbols, docs and comments, tests and fixtures, config, scripts, CI, and build files are in scope.
Vendor and archive directories still require triage: vendor matches may be false positives, while genuine historical references may be intentionally stale.
Commit messages, PR descriptions, and chat logs are immutable history; exclude them from the mutable-reference inventory rather than rewriting or classifying them.

### 3. Reconcile

Land all `update` outcomes together.
In the commit body, account for every mutable-tree match in a `References swept:` section.
Group matches only when they share both path and outcome, and retain precise locations and counts so the entries reconcile to the search total.
Never group across paths or outcomes.

Every proposed replacement or `update` entry must state the audited old → new encoding, using the intended replacement or its faithful language-specific form rather than an adjacent concept or invented synonym.
When a matched reference carries rationale, preserve the source's distinct cause or constraint and accepted cost or downside with the replacement or its attached explanation.
Labels such as `partner constraint` or `tradeoff preserved` do not substitute for those meanings.
Do not inflate the inventory by classifying an unchanged attached rationale line as a separate false positive merely because it contains no old encoding.

## Commit-body artifact

For a positive sweep:

```text
References swept:
- path/to/file.ext:LINES — update `old` → `new` (N matches: <short role>)
- path/to/history.ext:LINE — intentionally stale: <reason> (N matches)
- path/to/unrelated.ext:LINE — false positive: <reason> (N matches)

Verification:
- <check actually performed and result observed>
```

Include only outcome groups actually observed.

If all mutable-tree matches are in the changed file, use the required negative form:

```text
References swept: n/a — change affects only this file.

Verification:
- <check actually performed and result observed>
```

The `n/a` line is mandatory; omitting it is indistinguishable from forgetting the sweep.
Put `References swept:` after the narrative body and before `Verification:`.

Group before exceeding the repository's normal commit-body preference.
A legitimate broad sweep may still exceed that preference after grouping because the audit is correctness evidence, not narrative rationale.

Record only checks and results actually observed.
The sweep establishes reference disposition, not broader branch readiness; do not infer a blocker or readiness verdict from evidence that does not establish one.
For a read-only proposal, account for every observed match and intended outcome; claim an update as applied or outstanding only when supplied file state establishes that status.

## Rationalizations

| Excuse | Reality |
|---|---|
| “The reviewer flagged only one line.” | Treat it as a sample and search for siblings before fixing it. |
| “The IDE handled the rename.” / “Tests will catch the rest.” | IDEs and tests miss docs, comments, plain-string fixtures, config, scripts, CI, build files, and non-indexed references. |
| “I checked the obvious places.” | Search every required surface and old/new encoding; selective attention is not an inventory. |
| “The other matches are obviously unrelated.” | Record each path/outcome group as `false positive: <reason>` rather than skipping it silently. |
| “It is only a test, doc, or typo.” | Those surfaces encode the fact and can remain silently stale. |
| “I will add a TODO and sweep later.” | Reconcile in the same commit so no intermediate revision is internally inconsistent. |
| “The plan probably covers it.” | Search; zero siblings requires the explicit `References swept: n/a` line. |
| “This change is too small for a sweep.” | Applicability depends on the fact being propagated, not the diff size. |
