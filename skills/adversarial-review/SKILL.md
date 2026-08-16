---
name: adversarial-review
description: Use when code-reviewing or self-reviewing code, specs, plans, or designs — especially same-family pairings where the default reviewer posture risks compounding over-engineering, accepting unverified rationale, or missing unenumerated edge cases.
---

# Adversarial Review

## Role

Reviewer adapter for direct invocation, insertion into a review prompt, or local automation.
Use `superpowers:requesting-code-review` for review mechanics and this skill for posture and output; when their response templates conflict, this skill's Output format takes precedence.

## Posture

**Default mental model: something is wrong here; find it.**

- Thorough reviewer asks "is this complete?" → expands scope, adds rigor.
- Adversarial reviewer asks "is this wrong?" → scrutinizes claims and challenges necessity.
- Adversarial ≠ antagonistic. Adversarial = presumption of flaw + duty to find + verification over trust.
- Adversarial is the requested service. Soft review and not surfacing issues quickly is failure to deliver.
- Apply across code, architecture, design choices, and rationale.

The posture and its verification duty end with the review; then return to your pre-review posture.

## Severity rubric

- **[P0]** — critical / blocks merge. Data loss, security hole, broken core path.
- **[P1]** — important / resolve before opening the PR. Incorrect behavior on documented input, regression on tested path.
- **[P2]** — minor / resolve before opening the PR. Cleanup, naming, comment drift; code that's correct only by a fragile, unstated invariant ("fix by construction").
- **[P3]** — nit / optional. Style preference, missing punctuation.

## Output format

Emit one finding per line, starting the line with its severity token; put detail on indented lines beneath:

```
- [PN] <path>:<line>: <one-line summary>
  <optional indented reasoning>
```

A line starting with `[P0]`–`[P3]` is read as a finding, so start no other line with one.
When a finding concerns a referenced class, account for every member by name in the finding or its indented detail; collective shorthand such as "other callers" does not demonstrate enumeration.
Emit findings (or `No findings.`) only after enumerating, verifying, and challenging, then emit the pattern and verdict lines.

**Pattern line:** Immediately before the verdict, emit exactly one `DD-PATTERN: ...` line.
Summarize a shared cause or recurring pattern supported by at least two findings; otherwise use `DD-PATTERN: NONE`.
Generic similarity — such as both findings violating contracts or mishandling exceptional inputs — is not a shared cause or recurring pattern.
This line is synthesis, not a finding, and never changes severity or verdict.

**Verdict line:** The last non-blank line, with nothing after it, contains only `DD-VERDICT: PASS` or `DD-VERDICT: BLOCK`.
PASS means zero `[P0]`/`[P1]`/`[P2]` findings (`[P3]`-only passes); BLOCK means one or more.

## Deterministic rendering

After completing the semantic review, when command execution is available, run the bundled `scripts/render_review.py` resolved relative to this `SKILL.md`, with the completed review JSON on stdin, and return its stdout verbatim.
Use the resolved script's `--help` for the JSON input schema and command options.
If command execution is unavailable, follow the existing manual output contract above.

## Holistic baseline

Every review uses this holistic baseline: deep and whole-repo, anchored to the active plan and governing docs; there is no light or diff-scoped tier.
Whenever you state or distinguish this always-on baseline, call it the **holistic baseline**.
Always apply the posture and all four rules below before adding specialized angles.

### Enumerate every class

When the artifact or a finding references a class — "every X," "all Y," "handles Z," or a shared primitive with multiple callers — list every member or caller and trace each.

- "Handles all `git commit` forms" → bare, `-a`, `<pathspec>`. Does the design hold for each?
- "Covers all error paths" → list them. Walk each.
- Coverage claimed without enumeration is itself a finding.

### Verify every rationale claim

For every "we chose X because Y" / "Y doesn't support Z" / "Y is too slow":

- Y is presumed unverified.
- Check from primary sources (docs, code, measured behavior).
- If Y can't be verified from the artifact + linked context, flag the rationale.

Author confidence is not evidence.
Citations are not verification.

### Challenge every piece for necessity and effectiveness

For each piece of the artifact, ask:

- Observed failure mode, or hypothetical?
- Real use case, or "just in case"?
- Defense-in-depth justified by evidence, or by convention?
- Feature, or non-feature framed as a feature?
- Advances the intended outcome, or only adds activity or measures a proxy?

Hypothetical / just-in-case / convention / non-feature / ineffective → flag for removal.
This is `disciplined-development` Principle 7 applied to review.
In prose the same test catches padding — load `concise-writing` when reviewing docs.

### Generate the unexercised cases

Code rests on assumptions it never states; a passing test or clean read confirms they held this run, not that they hold.
Generate what it doesn't handle and surface what it leans on.

**Inputs and conditions.** List every input read, resource depended on, boundary crossed, and bound set; for each, generate the case the happy path skips:

- *Absent* — resource/precondition missing (model, file, permission, config): typed error, or silent download / fallback / hang?
- *Malformed* — value across a trust boundary (peer reply, API response, parsed field) used or committed unvalidated: a bad value stored as valid?
- *Out-of-scale* — timeout/limit/buffer sized to the common case: holds for the largest real input?

**The invariant it relied on.** When correctness rests on an unstated or fragile assumption (ordering, init order, timing window, a sibling guarding the same hazard this path leaves implicit), grade it:

- *Stated?* written (comment/assert/type), not re-derived.
- *Local?* checkable here, not three functions away.
- *Robust?* an inserted `await`/log/reorder can't silently break it.
- *Symmetric?* the same hazard handled the same way in siblings.

Any "no" is a finding, even if the code works today.
Fix it by construction: enforce or unify until every axis is "yes".
A doc comment only flips *Stated?*; a test flips none.
Neither lowers the severity.

**Before dismissing a false positive:** if your reason is "it can't happen" (tests pass, the scheduler prevents it, the caller never does), name the assumption that makes it safe and grade it first — explaining the safety usually surfaces the finding.

**Before promoting a hypothetical:** do not demand additional samples inside a bounded range when a supplied invariant makes behavior uniform across it; first identify a mechanism that can change within the range.
A producer guarantee does not make an unconstrained consumer input local or robust.

## Specialized angles

The holistic baseline above finds bugs, verifies rationale, challenges necessity and effectiveness, and generates unexercised cases on every review.
An angle adds one specialized lens and never narrows that baseline.
Reserve angles for lenses the baseline lacks.

| Angle | Apply when | Looks for |
|---|---|---|
| **consistency** | Every artifact | Divergence across the corpus: contract, signature, or import drift; terminology or wording drift; single-source duplication. |
| **executability** | The artifact contains instructions a reader must execute, such as plans, specs, runbooks, command docs, or setup docs | Whether a zero-context implementer can execute it: missing definitions, ambiguous contracts, or misdirecting file lists. |
| **skill-authoring** | The artifact is a `SKILL.md` | Apply `superpowers:writing-skills`: catch a `description` that summarizes the workflow, discipline rules with open rationalization loopholes, and claims not backed by a watched failure. |
| **durability** | The artifact creates, persists, or reads durable or source-of-truth state, including file writes, append-only logs, transactions, journals, spools, or stores another component treats as authoritative; skip pure in-memory or stateless code | Failure and partial-state paths: non-atomic mutations and reads that accept non-committed data. |

For **durability**, run both checklists:

- *Mutation:* partial write then error → rolled back? flush/commit fails after the write → acknowledged anyway? process killed mid-op → torn record? a write-path crash on bad input (panic/abort, unchecked unwrap, `try!`/assert; NaN/±Inf, oversized) → typed error, or process crash? ('it's a programmer error / our own typed data' is no pass — a statically-valid value can be unserializable at runtime; the crash tears the record, and even a pre-write crash denies the caller a recoverable error) failure surfaced as the documented error type, or a leaked lower-layer one? retry after a failure → duplicate / gap / reorder?
- *Read/replay:* torn/partial final record (missing terminator) rejected? interior corruption (blank line, gap, out-of-order) rejected, not skipped? unknown/forward version loud, not mis-parsed? empty distinguished from corrupt?

Before emitting findings, complete the holistic baseline over the artifact as a whole and report any concrete defects alongside angle-specific findings; no angle satisfies or replaces that baseline.

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

DD-PATTERN: NONE
DD-VERDICT: BLOCK
```

### Clean pass

```
No findings.

DD-PATTERN: NONE
DD-VERDICT: PASS
```

## Common reviewer rationalizations

| Excuse | Reality |
|--------|---------|
| "Looks reasonable to me." | "Reasonable" is not a finding. State what's broken or `No findings.` |
| "The author cited a reason." | Citations ≠ verification. Check the claim. |
| "I don't see anything obvious." | Adversarial = look harder. Enumerate, verify, challenge, generate the unexercised cases. |
| "Trivial piece; nothing to scrutinize." | Necessity check applies most where complexity hides — "obviously harmless" pieces. |
| "Author deferred the choice; that's a valid design move." | A design that punts decisions punts the spec. Flag the unmade choice. |
| "Don't be harsh." | Adversarial is the requested service. Softening = failing to deliver. |
| "It's a false positive." | Name the assumption that makes it safe — that's usually the finding. |
| "The tests prove it can't happen." | They prove it doesn't *now* — not that the assumption is stated, local, or robust. |
| "Safe by how the runtime schedules it." | Safe by accident — one edit from broken. |
| "The model's always there / the result's well-formed / inputs are small." | That's the assumption. Remove it and re-read. |

## Composition

- **`superpowers:requesting-code-review`** — base skill for request/response mechanics; this skill adds the posture.
- **`superpowers:receiving-code-review`** — implementer-side discipline for handling findings.
- **`disciplined-development` Principle 7** — implementer-side counterpart (don't add what evidence doesn't demand).
