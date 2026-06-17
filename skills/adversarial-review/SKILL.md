---
name: adversarial-review
description: Use when code-reviewing or self-reviewing code, specs, plans, or designs — especially same-family pairings where the default reviewer posture risks compounding over-engineering, accepting unverified rationale, or missing unenumerated edge cases.
---

# Adversarial Review

## Overview

Reviewer skill that injects adversarial posture. Use directly, paste into
a review prompt, or feed to local automation.

## Role

Adapter on top of `superpowers:requesting-code-review`. Augments; does NOT replace. Base skill = what code review *is*; this skill = what *mode* to be in.

## Posture

**Default mental model: something is wrong here; find it.**

- Thorough reviewer asks "is this complete?" → expands scope, adds rigor.
- Adversarial reviewer asks "is this wrong?" → scrutinizes claims, challenges necessity.
- Adversarial ≠ antagonistic. Adversarial = presumption of flaw + duty to find + verification over trust.
- Adversarial is the requested service. Soft review and not surfacing issues quickly is failure to deliver.
- Apply across code, architecture, design choices, and rationale.

## End of posture

Adversarial posture is scoped to the review. When the review completes, return to your pre-review posture.

Don't carry the reviewer's verification duty past the review.

## Severity rubric

- **[P0]** — critical / blocks merge. Data loss, security hole, broken core path.
- **[P1]** — important / resolve before opening the PR. Incorrect behavior on documented input, regression on tested path.
- **[P2]** — minor / resolve before opening the PR. Cleanup, naming, comment drift.
- **[P3]** — nit / optional. Style preference, missing punctuation.

## Output format

One finding per line, the line starting with its severity token; put any
detail on indented lines beneath:

```
- [PN] <path>:<line>: <one-line summary>
  <optional indented reasoning>
```

A line that starts with `[P0]`–`[P3]` is read as a finding — so start no
other line with one. Clean reviews emit exactly:

```
No findings.
```

Emit it only after enumerating, verifying, and challenging.

## Rules

### Enumerate every class

When the artifact references a class — "every X," "all Y," "handles Z" — list members and trace each.

- "Handles all `git commit` forms" → bare, `-a`, `<pathspec>`. Does the design hold for each?
- "Covers all error paths" → list them. Walk each.
- Coverage claimed without enumeration is itself a finding.

### Verify every rationale claim

For every "we chose X because Y" / "Y doesn't support Z" / "Y is too slow":

- Y is presumed unverified.
- Check from primary sources (docs, code, measured behavior).
- If Y can't be verified from the artifact + linked context, flag the rationale.

Author confidence is not evidence. Citations are not verification.

### Challenge every piece for necessity

For each piece of the artifact, ask:

- Observed failure mode, or hypothetical?
- Real use case, or "just in case"?
- Defense-in-depth justified by evidence, or by convention?
- Feature, or non-feature framed as a feature?

Hypothetical / just-in-case / convention / non-feature → flag for removal.

## Review angles

The posture and rules above apply to every review. An **angle** layers one
focused lens on top — it *adds* a focus, it does **not** narrow the diff you
review (the whole-picture *holistic* review owns the seams between angles).

This catalog is the single source for what each angle is. *Which* angle runs at
*which* tier — and when to substitute one (e.g. on a doc-dominant cold-read) — is
dispatch orchestration owned by the dispatcher (the `/dd-review` command), not
here. A reviewer assigned an angle by name applies the matching definition below.

| Angle | Focus |
|-------|-------|
| **correctness** | logic, boundary / off-by-one, wrong-variable, control-flow bugs. |
| **rationale** | verify every docstring / comment / "safe" / "trusted" claim against the actual code. |
| **cross-file** | divergence from canonical modules, broken imports, caller / contract drift. |
| **security** | path traversal, injection, unvalidated input, unsafe path building. |
| **necessity** | cut what doesn't earn its place. Code: dead code, over-engineering, premature abstraction / config (`disciplined-development` Principle 7). Prose: padded / verbose docs + comments — also load the `concise-writing` skill. |
| **executability** | could a zero-context implementer execute this? Verify every factual repo claim; flag missing definitions, ambiguous contracts, misdirecting file lists. |
| **doctrine-consistency** | drift against governing docs: CLAUDE.md, locked decisions in plans/specs, companion plans, the skills' own rules, single-source duplication. |

## Few-shot examples

### Findings present

```
- [P1] spec.md:124: stdout-marker detection silently misses `git commit --quiet`
  Quiet commits land without emitting `[<branch> <sha>]`. The counter
  drifts. Either document `--quiet` as unsupported or use HEAD-before/
  after as the detection signal.

- [P2] spec.md:127: `mkdir -p` doesn't establish the documented mode-0600
  `mkdir -p` honors umask; `mv` preserves temp file mode. Either
  `umask 077` for the section or `chmod 600` before rename.
```

### Clean pass

```
No findings.
```

## Common reviewer rationalizations

| Excuse | Reality |
|--------|---------|
| "Looks reasonable to me." | "Reasonable" is not a finding. State what's broken or `No findings.` |
| "The author cited a reason." | Citations ≠ verification. Check the claim. |
| "I don't see anything obvious." | Adversarial = look harder. Enumerate, verify, challenge necessity. |
| "Trivial piece; nothing to scrutinize." | Necessity check applies most where complexity hides — "obviously harmless" pieces. |
| "Author deferred the choice; that's a valid design move." | A design that punts decisions punts the spec. Flag the unmade choice. |
| "Don't be harsh." | Adversarial is the requested service. Softening = failing to deliver. |

## Red flags

Stop and re-read if you catch yourself:
- "Looks good" without verification.
- "Found nothing" without enumeration.
- Accepting rationale without checking the claim.
- Accepting a punted decision as the design.
- Skipping a section as trivial.

## Composition

- **`superpowers:requesting-code-review`** — base skill for request/response mechanics; this skill adds the posture.
- **`superpowers:receiving-code-review`** — implementer-side discipline for handling findings.
- **`disciplined-development` Principle 7** — implementer-side counterpart (don't add what evidence doesn't demand).
