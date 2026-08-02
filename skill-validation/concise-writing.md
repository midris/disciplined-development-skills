# concise-writing — validation

## Active catalog audit (2026-08-02)

The shared discovery suite owns ordinary all-nine description routing. Its unchanged
`DISC-03` control selected `concise-writing` in all five repetitions; see
[skill-discovery.md](skill-discovery.md#control-and-target-results). Focused
skill/reference-authoring routing regressions are owned here as `CW-09` and `CW-11`.

Historical evidence was classified before defining the active skill-owned suite:

| Historical evidence | Classification | Active disposition |
|---|---|---|
| Cache-eviction verbosity delta | Repair | Atomize its six pattern checks across `CW-01` and `CW-03`–`CW-06` with exact prompts and five repetitions |
| Unseen webhook follow-up | Merge | `CW-01` and `CW-03`–`CW-06`; it reran the same named-pattern method in an unseen domain but has no independently replayable prompt |
| Over-trim probe | Repair | `CW-02`; preserve rationale, navigation, and recap explicitly |
| Composite duplicate-red-flags cell B | Retired by Task 1; excluded from Task 2 counts | Rehome its framing criteria in `CW-02`; replace its self-reported whole-document duplicate check with the stronger behavioral fixture in `CW-03` |
| Routing: active-plan implementation with delegation | Merge | Shared `DISC-06` owns this negative route with all nine descriptions |
| Routing: padded README tightening | Merge | Shared `DISC-03` owns the positive ordinary-prose route |
| Routing: SKILL.md shortening | Retire | Its exclusion contract was superseded by the user-approved body-level ownership design; replace it with the new `CW-09` co-selection and `CW-10` ownership targets |
| Routing: plan deferral with PR-only rationale | Retire | Ambiguous composition cell did not isolate a positive or negative concise-writing promise |
| Routing: routine convention-preserving rename | Merge | Shared `DISC-08` owns this negative route with all nine descriptions |

No prior scenario met the common protocol unchanged: **Keep 0, Repair 2, Merge 4,
Retire 2**. Safe full-bundle direct invocation, non-software extraction, frontmatter
skill/reference-authoring co-selection, and explicit body-level ownership were
absent, so `CW-07`–`CW-12` are **Add 6**. The untested 2026-07-19 draft-first reminder
is not counted as a prior scenario; `CW-02` protects its observable preservation
outcome without claiming to observe private drafting behavior.

## Active scenario catalog

Common run metadata: control commit
`4296647f0dff48a9e77b979ef07e813bf1f66db2`; Codex CLI 0.146.0;
`gpt-5.6-sol`; high reasoning effort; Superpowers 6.2.0; run date 2026-08-02;
five fresh processes per scenario; maximum concurrency three; enforced read-only,
no-agents transport; manual scoring; rubric withheld.

The owner of `CW-01`–`CW-12` is `concise-writing`. The sole affected repository skill
for `CW-01`–`CW-08`, `CW-10`, and `CW-12` is `concise-writing`; `CW-09` and `CW-11`
affect `concise-writing` and `adversarial-review-loop` plus the external
`superpowers:writing-skills` dependency. The linked shared discovery cells retain
Task 1 ownership and their recorded affected-skill maps.

`CW-01`–`CW-06`, `CW-08`, `CW-10`, and `CW-12` receive only the immutable control
`skills/concise-writing/SKILL.md`. Its file SHA-256 is
`4d12a2eb475c6b2ef57e2300c8c07af3f59c1e07b2b82695a3b7669eee1d6d72`;
the single-file archive SHA-256 is
`b8bb253165cb686149b016c34b3b524eeaa2cb317998db7c985b2d65253b908e` and
its canonical content-manifest SHA-256 is
`c3ab86f0cc501d6c07c2758574e0aabea1cc2a4fbb2569a09941ab3d81780ae7`.
`CW-07` receives the immutable complete nine-skill control bundle whose archive
SHA-256 is `8f21c8267d005c349702ec94d6aff26c13a09bfbe29f2b43efcfbb37304f16e3`
and content-manifest SHA-256 is
`e2249c4b24132523f1374d506957197a303314e2bfbc6e32c9c1b233909cbbff`.
`CW-09` and `CW-11` receive the identical descriptions-only bundle. Repository sources are
`skills/adversarial-review-loop/SKILL.md` and `skills/concise-writing/SKILL.md` at
git commit `4296647f0dff48a9e77b979ef07e813bf1f66db2`, with source file SHA-256 values
`46b85eafc5db54cb521eed9c4a110e552c76d97cfae72e141f109c9dea10f0c6` and
`4d12a2eb475c6b2ef57e2300c8c07af3f59c1e07b2b82695a3b7669eee1d6d72`.
Their bundle paths are `descriptions/adversarial-review-loop.txt` and
`descriptions/concise-writing.txt`. The external source is Superpowers 6.2.0
`skills/writing-skills/SKILL.md`, with source file SHA-256
`d34db5c8aed6a4e0440132bd0613aace70a693ec7819d5637ad77481d8e10d1b` and bundle path
`descriptions/superpowers-writing-skills.txt`. The three extracted-description file
hashes in that order are
`38843f7718501f52116bfd4f95a6640cb16b560851767df540c808a1ed18cefa`,
`586a741a9cb28746078ca1b5f7aa570a4e621a5d2cdecac16e31bd6d2c82fd62`, and
`5504b0825ec458aa8c20e9a55c6a932b36849e261a97aaf98af366e19a937154`.
The canonical three-entry content-manifest SHA-256 is
`49c129fea1a0782f6daaf9908e134bf92ea684c031f52b12d520ebe3aac7b2a3`.
Each fixture file is exactly the named single line below followed by one LF:

`descriptions/adversarial-review-loop.txt`

```text
Use when an adversarial review surfaces findings — including when successive rounds keep surfacing new, surface-different findings (possible shared root), and always when a review loop enters its third cycle. Applies to both internal (self-review, mid-flight work, code review) and external (a different model, a CI reviewer bot, a required reviewer) reviews.
```

`descriptions/concise-writing.txt`

```text
Use when writing or revising reader-facing prose — docs, READMEs, plans, specs, design notes, commit bodies, or code comments — that risks being verbose, padded, repetitive, wordy, or bulky; also when asked to tighten, trim, shorten, or "get to the point". Excludes skill and reference authoring.
```

`descriptions/superpowers-writing-skills.txt`

```text
Use when creating new skills, editing existing skills, or verifying skills work before deployment
```

| ID | Type / status | Affected skills | Protected promise and section | Supplied context | Exact prompt | Evaluator-withheld rubric | Rerun trigger |
|---|---|---|---|---|---|---|---|
| `CW-01` | Simple application / preservation | `concise-writing` | Remove local padding without fact loss; Core test + Verbosity patterns | Single-skill control | [CW-01](#cw-01--simple-padding-removal) | Remove meta and duplicate statements; retain all four states and both state-specific fields; add nothing | Core test, local compression, or verbosity-pattern change |
| `CW-02` | Non-trivial application + focused regression / preservation | `concise-writing` | Preserve necessary framing while cutting local padding; Compression pass + When NOT to cut | Single-skill control | [CW-02](#cw-02--compression-with-framing) | Cut opener/duplicate; keep distinction, both rationales, navigation, and failure rule | Compression, anti-over-trim, rationale/navigation/recap, or existing-text rule change |
| `CW-03` | Focused regression / preservation | `concise-writing` | Remove actual cross-section duplication; Cross-section duplication | Single-skill control | [CW-03](#cw-03--cross-section-duplication) | Define the URL, single-use rule, and expiry once; keep every section-specific fact | Global compression or cross-section-duplication change |
| `CW-04` | Focused regression / preservation | `concise-writing` | Collapse over-sectioning without losing facts; Over-sectioning | Single-skill control | [CW-04](#cw-04--over-sectioning) | Replace four one-sentence subsections with one compact section; preserve expiration after 20 minutes of inactivity, a warning two minutes before expiration, mouse/keyboard/touch resets, and sign-in recovery | Over-sectioning rule change |
| `CW-05` | Focused regression / preservation | `concise-writing` | Remove elaboration not supported by the source facts; Unrequested elaboration | Single-skill control | [CW-05](#cw-05--unrequested-elaboration) | Preserve every supplied fact and remove both unsupported recommendations | Unrequested-elaboration rule change |
| `CW-06` | Focused regression / preservation | `concise-writing` | Remove emphasis and hedge inflation without weakening the rule; Emphasis/hedge inflation | Single-skill control | [CW-06](#cw-06--emphasis-inflation) | State each semantic rule once; allow `Every request must` once, but no bold, `single`, `each and every`, `always`, or repeated rejection | Emphasis/hedge-inflation rule change |
| `CW-07` | Direct invocation / preservation | `concise-writing` | Complete safely without project state when invoked with the complete bundle installed; full skill | Complete nine-skill control | [CW-07](#cw-07--full-bundle-direct-invocation) | Complete the notice without a blocker or unavailable-requirement ceremony and preserve every supplied fact | Direct-invocation contract or integrated-suite ownership change |
| `CW-08` | Portability/extraction / preservation | `concise-writing` | Apply the technique outside software with no sibling dependency; full skill | Single-skill control | [CW-08](#cw-08--non-software-policy-extraction) | Preserve all eligibility, exception, deadline, accommodation, appeal, finality, and navigation facts; cut padding; no software assumptions | Portability, extraction, or any protected policy-compression rule change |
| `CW-09` | Discovery + focused routing regression / target | `concise-writing`, `adversarial-review-loop`; external `superpowers:writing-skills` | Allow `concise-writing` and `superpowers:writing-skills` to be co-selected for skill prose while excluding an unrelated candidate; frontmatter description | Three descriptions only | [CW-09](#cw-09--skill-authoring-co-selection) | Exact alphabetical JSON array containing both applicable skills and excluding `adversarial-review-loop` | Description or skill-authoring routing change |
| `CW-10` | Focused ownership regression / target | `concise-writing` | Defer skill-authoring decisions and validation; ownership block | Single-skill control | [CW-10](#cw-10--skill-authoring-ownership) | Exact JSON object naming `superpowers:writing-skills` for both responsibilities and quoting source-verifiable evidence | Skill-authoring ownership change |
| `CW-11` | Discovery + focused routing regression / target | `concise-writing`, `adversarial-review-loop`; external `superpowers:writing-skills` | Allow both skills to be co-selected for reference prose shipped within a skill while excluding an unrelated candidate; frontmatter description | Three descriptions only | [CW-11](#cw-11--reference-authoring-co-selection) | Exact alphabetical JSON array containing both applicable skills and excluding `adversarial-review-loop` | Description or reference-authoring routing change |
| `CW-12` | Focused ownership regression / target | `concise-writing` | Defer reference-authoring decisions and validation; ownership block | Single-skill control | [CW-12](#cw-12--reference-authoring-ownership) | Exact JSON object naming `superpowers:writing-skills` for both responsibilities and quoting source-verifiable evidence | Reference-authoring ownership change |

Every prompt below is byte-for-byte evaluator input. The rubrics above and expanded
criteria below are never included in evaluator prompts.
For every rewriting scenario (`CW-01`–`CW-08`), PASS also requires that the response
contain only the requested artifact with no preface, postscript, or procedural
narration, and introduce no unsupported fact, advice, or assumption.

### CW-01 — simple padding removal

```text
You are a fresh, read-only skill evaluator.
Do not edit files, change git state, inspect anything outside the supplied bundle, or dispatch agents.
Read `skills/concise-writing/SKILL.md` completely and follow it as binding guidance.
Return only the requested deliverable.

Tighten this reader-facing documentation and return only the revised text:

## Export status

This section explains the export status. An export can be queued, running, complete, or failed. The status reports which of these four states the export is currently in. Completed exports include a download link. Failed exports include an error code. In other words, complete jobs have a link, while failed jobs have an error code.
```

PASS requires one concise section that removes the meta opener and both restatements,
retains `queued`, `running`, `complete`, and `failed`, retains the download-link and
error-code distinctions, and introduces no new fact or advice.

### CW-02 — compression with framing

```text
You are a fresh, read-only skill evaluator.
Do not edit files, change git state, inspect anything outside the supplied bundle, or dispatch agents.
Read `skills/concise-writing/SKILL.md` completely and follow it as binding guidance.

Tighten the excerpt without losing necessary information or framing. Return only the revised excerpt.

## Delivery retries

This section explains how delivery retries work. Each delivery is attempted at most three times. Retries are counted per delivery, not per endpoint; this distinction prevents one failing delivery from exhausting retries for later deliveries. The worker attempts a delivery up to three times. We keep retries synchronous because downstream acknowledgements must preserve delivery order. Before changing retry behavior, see "Delivery ordering" below. A delivery is marked failed only after its third unsuccessful attempt.
```

PASS removes the meta opener and one duplicated three-attempt statement; preserves
the per-delivery distinction and its consequence, the synchronous-ordering rationale,
the `Delivery ordering` navigation aid, and the final failure rule. Paraphrase is
allowed only when each protected fact and its causal relationship remain explicit.

### CW-03 — cross-section duplication

```text
You are a fresh, read-only skill evaluator.
Do not edit files, change git state, inspect anything outside the supplied bundle, or dispatch agents.
Read `skills/concise-writing/SKILL.md` completely and follow it as binding guidance.
Return only the requested deliverable.

Tighten this complete two-section guide and return only the revised guide:

## Access links

An access link is a single-use URL that expires after 30 minutes. Send the link only to the intended recipient.

## Expiration

Access links are URLs that can be used once and expire after 30 minutes. After expiration, an administrator must issue a new link.
```

PASS defines an access link as a single-use URL expiring after 30 minutes exactly
once; preserves the intended-recipient rule and administrator reissue rule; and
introduces no new fact.

### CW-04 — over-sectioning

```text
You are a fresh, read-only skill evaluator.
Do not edit files, change git state, inspect anything outside the supplied bundle, or dispatch agents.
Read `skills/concise-writing/SKILL.md` completely and follow it as binding guidance.
Return only the requested deliverable.

Tighten this short guide and return only the revised text:

## Session behavior

### Timeout

Sessions expire after 20 minutes of inactivity.

### Warning

A warning appears two minutes before expiration.

### Activity

Mouse, keyboard, or touch input resets the inactivity timer.

### Recovery

Expired sessions require signing in again.
```

PASS returns one compact `Session behavior` section without the four one-sentence
subheadings and preserves expiration after 20 minutes of inactivity, a warning
exactly two minutes before expiration, mouse, keyboard, and touch as reset inputs,
and the sign-in-again rule.

### CW-05 — unrequested elaboration

```text
You are a fresh, read-only skill evaluator.
Do not edit files, change git state, inspect anything outside the supplied bundle, or dispatch agents.
Read `skills/concise-writing/SKILL.md` completely and follow it as binding guidance.
Return only the requested deliverable.

Authoritative notes: The archive is generated nightly at 02:00 UTC. It contains completed orders from the previous UTC day. Archives are retained for 30 days.

Tighten this documentation and return only the revised text:

The archive is generated nightly at 02:00 UTC. It contains completed orders from the previous UTC day. Archives are retained for 30 days. Teams should download every archive immediately to avoid any chance of data loss. For best performance, process archives before business hours.
```

PASS preserves the generation time, included order window, and retention period;
removes both unsupported recommendations; and introduces no new claim.

### CW-06 — emphasis inflation

```text
You are a fresh, read-only skill evaluator.
Do not edit files, change git state, inspect anything outside the supplied bundle, or dispatch agents.
Read `skills/concise-writing/SKILL.md` completely and follow it as binding guidance.
Return only the requested deliverable.

Tighten this documentation and return only the revised text:

Every single request must **always** include an API key. Each and every API key must be sent in the `Authorization` header. Requests without a key are always rejected, so a request without a key will always be rejected.
```

PASS states once that every request requires an API key in the `Authorization`
header and once that requests without one are rejected. The construction `Every
request must` is allowed once to express universal scope and obligation. Bold,
`single`, `each and every`, `always`, and any repeated rejection statement fail.

### CW-07 — full-bundle direct invocation

```text
You are a fresh, read-only skill evaluator.
The complete local skill bundle is installed, but no project files, active plan, external fact source, or writable target is supplied. Do not edit files, change git state, inspect anything outside the supplied bundle, or dispatch agents.
Invoke `concise-writing` directly: read `skills/concise-writing/SKILL.md` completely and follow it as binding guidance.
If the skill cannot complete the task without an unavailable input or another procedure, return `BLOCKED: <missing requirement>` instead of a revision.

Tighten this reader-facing release notice and return only the revised notice:

This release notice explains the new download behavior. Reports are now downloaded as CSV files. CSV downloads preserve the filters currently applied to the report. The downloaded file uses UTF-8 encoding. In other words, whatever filters are active remain active in the CSV that is downloaded. Existing PDF downloads are unchanged. There is no change to PDF download behavior.
```

PASS returns only a concise notice—not `BLOCKED` or procedural narration—that states
CSV format, filter preservation, UTF-8, and unchanged PDF behavior exactly once each
and adds no fact.

### CW-08 — non-software policy extraction

```text
You are a fresh, read-only skill evaluator.
Do not edit files, change git state, inspect anything outside the supplied bundle, or dispatch agents.
Read `skills/concise-writing/SKILL.md` completely and follow it as binding guidance.
Return only the requested deliverable.

Tighten this applicant-handbook policy and return only the revised section:

## Community arts grants

This section explains the rules for community arts grants. Applicants must be 501(c)(3) organizations with annual budgets below $2 million. Organizations without 501(c)(3) status may apply through an eligible fiscal sponsor; see Appendix A for sponsor requirements. Applications are due by 5:00 p.m. ET on October 15. The deadline for applications is October 15 at 5:00 p.m. Eastern Time, and late applications are not reviewed. To request an application accommodation, contact the program at least five business days before the deadline. Denied applicants may appeal within 10 calendar days; see Appeals for the required form. After the appeal decision, the decision is final.
```

PASS removes the opener and duplicated deadline; preserves eligibility as a
`501(c)(3)` organization with an annual budget strictly below $2 million; preserves
the exception allowing an organization without that status to apply through an
eligible fiscal sponsor; preserves `Appendix A` navigation, the October 15 deadline
at 5:00 p.m. ET, the rule that late applications are not reviewed, the five-business-
day accommodation lead time, denied applicants' ten-calendar-day appeal window,
`Appeals` navigation, and finality after the appeal decision; and adds no software or
repository assumption.

### CW-09 — skill-authoring co-selection

```text
You are a fresh, read-only skill-routing evaluator.
Do not inspect anything outside the supplied bundle, use skill bodies, edit anything, or dispatch agents.
Read `descriptions/adversarial-review-loop.txt`, `descriptions/concise-writing.txt`, and `descriptions/superpowers-writing-skills.txt` completely. Each file contains one skill description.
Their scoring identifiers are respectively `adversarial-review-loop`, `concise-writing`, and `superpowers:writing-skills`.
Given those descriptions and one request, select every skill whose description directly applies now.
Do not select a skill merely because it might become useful later.
Return only a compact JSON array of selected skill names in alphabetical order, with no whitespace.

User request: Tighten the frontmatter description in an existing SKILL.md without changing its trigger behavior.
```

PASS is exactly `["concise-writing","superpowers:writing-skills"]`. Any prose,
malformed JSON, wrong order, missing required skill, or inclusion of
`adversarial-review-loop` fails.

### CW-10 — skill-authoring ownership

```text
You are a fresh, read-only skill-contract evaluator.
Do not edit files, change git state, inspect anything outside the supplied bundle, or dispatch agents.
Read `skills/concise-writing/SKILL.md` completely and follow it as binding guidance.

A user is authoring a skill and asks which skill owns the authoring decisions and validation.
Extract only ownership stated explicitly in the supplied contract; do not infer an owner from prior knowledge or from a skill name.
Return only a compact JSON object with keys `authoring_owner`, `validation_owner`, and `evidence`, in that order and no whitespace. Use the explicitly named owner's canonical skill name for each owner. Quote the complete ownership sentence from the supplied contract verbatim as `evidence`. Use `null` for all three values if that sentence is absent.
```

PASS is exactly
``{"authoring_owner":"superpowers:writing-skills","validation_owner":"superpowers:writing-skills","evidence":"During skill or reference authoring, `superpowers:writing-skills` owns authoring decisions and validation."}``
and the evidence sentence must occur byte-for-byte in the supplied contract. Any
prose, malformed JSON, wrong key order, other owner, or absent/non-verbatim evidence
fails.

### CW-11 — reference-authoring co-selection

```text
You are a fresh, read-only skill-routing evaluator.
Do not inspect anything outside the supplied bundle, use skill bodies, edit anything, or dispatch agents.
Read `descriptions/adversarial-review-loop.txt`, `descriptions/concise-writing.txt`, and `descriptions/superpowers-writing-skills.txt` completely. Each file contains one skill description.
Their scoring identifiers are respectively `adversarial-review-loop`, `concise-writing`, and `superpowers:writing-skills`.
Given those descriptions and one request, select every skill whose description directly applies now.
Do not select a skill merely because it might become useful later.
Return only a compact JSON array of selected skill names in alphabetical order, with no whitespace.

User request: Tighten a reference guide shipped inside an existing skill without changing its requirements or trigger behavior.
```

PASS is exactly `["concise-writing","superpowers:writing-skills"]`. Any prose,
malformed JSON, wrong order, missing required skill, or inclusion of
`adversarial-review-loop` fails.

### CW-12 — reference-authoring ownership

```text
You are a fresh, read-only skill-contract evaluator.
Do not edit files, change git state, inspect anything outside the supplied bundle, or dispatch agents.
Read `skills/concise-writing/SKILL.md` completely and follow it as binding guidance.

A user is authoring a reference file shipped as part of a skill and asks which skill owns the authoring decisions and validation.
Extract only ownership stated explicitly in the supplied contract; do not infer an owner from prior knowledge or from a skill name.
Return only a compact JSON object with keys `authoring_owner`, `validation_owner`, and `evidence`, in that order and no whitespace. Use the explicitly named owner's canonical skill name for each owner. Quote the complete ownership sentence from the supplied contract verbatim as `evidence`. Use `null` for all three values if that sentence is absent.
```

PASS is exactly
``{"authoring_owner":"superpowers:writing-skills","validation_owner":"superpowers:writing-skills","evidence":"During skill or reference authoring, `superpowers:writing-skills` owns authoring decisions and validation."}``
and the evidence sentence must occur byte-for-byte in the supplied contract. Any
prose, malformed JSON, wrong key order, other owner, or absent/non-verbatim evidence
fails.

## Active results

Every non-control arm cell records `R1/R2/R3/R4/R5; total`; aggregate-only results
are invalid. Exact misses identify the arm and repetition without reproducing raw
transcripts.

| ID | Control bundle | R1 | R2 | R3 | R4 | R5 | Sol-high control | Target GREEN (R1/R2/R3/R4/R5; total) | Cleaned Sol-high (R1/R2/R3/R4/R5; total) | Sol-low control (R1/R2/R3/R4/R5; total) | Cleaned Sol-low (R1/R2/R3/R4/R5; total) | Exact misses | Run date | Infrastructure errors |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---:|
| `CW-01` | single-skill `c3ab86f0…` | PASS | PASS | PASS | PASS | PASS | 5/5 PASS | n/a | Task 17 | Task 11 | Task 27 | None | 2026-08-02 | 0 |
| `CW-02` | single-skill `c3ab86f0…` | PASS | PASS | PASS | PASS | PASS | 5/5 PASS | n/a | Task 17 | Task 11 | Task 27 | None | 2026-08-02 | 0 |
| `CW-03` | single-skill `c3ab86f0…` | PASS | PASS | PASS | PASS | PASS | 5/5 PASS | n/a | Task 17 | Task 11 | Task 27 | None | 2026-08-02 | 0 |
| `CW-04` | single-skill `c3ab86f0…` | PASS | PASS | PASS | PASS | PASS | 5/5 PASS | n/a | Task 17 | Task 11 | Task 27 | None | 2026-08-02 | 0 |
| `CW-05` | single-skill `c3ab86f0…` | PASS | PASS | PASS | PASS | PASS | 5/5 PASS | n/a | Task 17 | Task 11 | Task 27 | None | 2026-08-02 | 0 |
| `CW-06` | single-skill `c3ab86f0…` | PASS | PASS | PASS | PASS | PASS | 5/5 PASS | n/a | Task 17 | Task 11 | Task 27 | None | 2026-08-02 | 0 |
| `CW-07` | full bundle `e2249c4b…` | PASS | PASS | PASS | PASS | PASS | 5/5 PASS | n/a | Task 17 | Task 11 | Task 27 | None | 2026-08-02 | 0 |
| `CW-08` | single-skill `c3ab86f0…` | PASS | PASS | PASS | PASS | PASS | 5/5 PASS; preservation | n/a | Task 17 | Task 11 | Task 27 | None | 2026-08-02 | 0 |
| `CW-09` | descriptions `49c129fe…` | FAIL | FAIL | FAIL | FAIL | FAIL | 0/5 watched RED | Pending Task 2A | Task 17 | Task 11 | Task 27 | R1–R5: omitted `concise-writing` | 2026-08-02 | 0 |
| `CW-10` | single-skill `c3ab86f0…` | FAIL | FAIL | FAIL | FAIL | FAIL | 0/5 watched RED | Pending Task 2A | Task 17 | Task 11 | Task 27 | R1–R5: both owners and evidence were `null` | 2026-08-02 | 0 |
| `CW-11` | descriptions `49c129fe…` | FAIL | FAIL | FAIL | FAIL | FAIL | 0/5 watched RED | Pending Task 2A | Task 17 | Task 11 | Task 27 | R1–R5: omitted `concise-writing` | 2026-08-02 | 0 |
| `CW-12` | single-skill `c3ab86f0…` | FAIL | FAIL | FAIL | FAIL | FAIL | 0/5 watched RED | Pending Task 2A | Task 17 | Task 11 | Task 27 | R1–R5: both owners and evidence were `null` | 2026-08-02 | 0 |

## Preserved historical evidence

Everything below preserves the pre-audit evidence trail. It is not the active
catalog, current rerun guidance, or current authoring-boundary design.

### Duplicate red-flag consolidation (2026-08-01)

**Edit.** Remove the `Red flags` section whose cases repeat the retained verbosity patterns, compression pass, and rationalization table.

**Non-trivial shared matrix.** Tighten a padded document containing meta-framing, a duplicate definition, a misread-preventing transition, a load-bearing closing recap, and on-page design rationale.
PASS cuts the first two, preserves the latter three, and runs the global duplicate check.

**Unprimed control: 5/5 PASS. Unprimed GREEN after removal: 5/5 PASS.** Every evaluator preserved the anti-over-trim and global-altitude behavior.
This cell ran as one subcase in a four-skill composite matrix; all four subcases had to pass for a repetition to count.
Exact prompt, protocol, and per-repetition outcomes: [duplicate-red-flags-scenarios.md](duplicate-red-flags-scenarios.md).

Built and maintained test-first per `superpowers:writing-skills` (skills are TDD
for process docs: no skill — and no edit — without a failing test first). This
records the trail so the rationale is recoverable from the bundle.

### Method

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

### Results

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

### Deliberate calls (recorded so reviewers don't re-litigate)

- **Historical authoring exclusion (control behavior; approved for replacement).**
  The earlier record stated: “For it, use `superpowers:writing-skills`; do not
  invoke concise-writing separately. Skill prose is the every-word-counts extreme,
  and writing-skills enforces its own stricter token-efficiency bar there. (This
  matches the SKILL.md description's ‘use that there, not this.’ The boundary is
  settled — re-tweaking its wording is drift.)” This remains immutable control
  history, not current design guidance. The 2026-08-02 audit approved co-selection
  with `superpowers:writing-skills` owning authoring decisions and validation;
  `CW-09`–`CW-12` are watched REDs pending Task 2A implementation and GREEN.
- **Length (~900 words) is accepted** over an aggressive shrink. Only the
  description is always-on; the body loads on invocation, so the frequently-loaded
  <200-word target does not apply. A worked before/after example was kept for
  teaching value over a smaller word count.

### On edits

Re-run the relevant probe before shipping any change: verbosity delta + over-trim
for rule/content edits, routing for description/trigger edits.

#### Trigger-only description routing (2026-08-01)

**Matrix.** Route five prompts from metadata only: active-plan implementation with delegation; padded README tightening; SKILL.md shortening; plan deferral with PR-only rationale; and a routine convention-preserving rename.

**Pre-edit control: 3/3 PASS.** All evaluators selected `concise-writing` for the padded README and routed SKILL.md shortening to `superpowers:writing-skills` without separately selecting `concise-writing`.
The edit removes embedded ownership/process prose while retaining the skill-authoring exclusion as a trigger boundary.

**GREEN requirements.** Preserve ordinary prose routing and the skill/reference-authoring exclusion using trigger conditions only.

**GREEN result: 3/3 PASS.** All three independent metadata-only evaluators selected `concise-writing` for ordinary prose tightening and selected `superpowers:writing-skills`, not `concise-writing`, for SKILL.md shortening.

- **2026-07-19, "When editing existing text, draft first" rule** — shipped as an
  owner's-call without a fresh probe. Low-risk addition (a process reminder, not a
  new pattern to detect); flagged here rather than silently skipping the process.

### Appendix — captured run (cache-eviction build domain)

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
