# Make `adversarial-review` the standalone home of the review-angle doctrine

**Status:** active — in progress (2026-06-17; reactivated from deferred, surfaced
2026-06-12 during PR-4). Grew from "extract the catalog" into an angle-taxonomy
redesign (audit → 3 angles) plus relocating the command template to top-level.

**Governing principle (2026-06-16, supersedes the original lean):**
`adversarial-review` is a **standalone, portable** artifact — a consumer with only
the skill can ask for a review, name an angle, or list the angles, with no
dependency on `/dd-review`. So the skill owns the **whole** review doctrine: the
catalog, what each angle looks for, **and which angles apply to which artifact
(including the doc-dominant set)**. The command/hooks own CC orchestration only
(tier→trigger mapping, parallel dispatch, the codex gate) and may tighten which
set fires at which tier — but define neither the angles nor their selection.
This reverses the original lean ("substitution → command"): angle *selection* is
review judgment, so it moves into the skill. Push more into the skill, not less.

## Problem

The review **angle catalog** — the definitions of `correctness`, `rationale`,
`cross-file`, `security`, `necessity`, and (as of PR-4) `executability` /
`doctrine-consistency` — is review *judgment*, i.e. doctrine. But it lives in the
`/dd-review` **command**, not a skill, and is **duplicated across two command
copies** (`.claude/commands/dd-review.md` bundle source +
`examples/commands/dd-review.md` consumer template). The command should be pure
orchestration (resolve scope → dispatch → aggregate → iterate → checkpoint); the
angle definitions belong with the reviewer posture in `adversarial-review`.

It is the one spot where the bundle's "skills are doctrine, hooks are dumb
triggers" split is incomplete — review doctrine living in an executable command
rather than a skill.

## Desired end state

- `adversarial-review` is standalone: a **Review angles** section (catalog + a
  **When to apply** list) so a consumer with only the skill can run a review, name
  an angle, or list them. Correctness/rationale/necessity are the always-on
  baseline posture (not angles); the angle set is `consistency`, `executability`,
  `skill-authoring` (see "Angle audit" below).
- The `/dd-review` command references the skill's selection; tier rows set *depth*
  and defer *which angles* to the skill. No angle definitions or substitution rule
  in the command.
- The command template moves from `examples/commands/` to a top-level `commands/`
  (first-class + discoverable; installer + its test + CLAUDE.md/README updated).
- Single source: definitions + selection live once (the skill); the hook README
  and the `skill-validation/` records point at it.

## Angle audit — final set (2026-06-17)

Tested every candidate angle by **discrimination vs the baseline holistic review**
(the angle-necessity bar: keep an angle only if it catches what holistic misses).
Holistic caught the planted target for 6/7 candidates on small artifacts →

- **Dropped:** `correctness`, `rationale`, `necessity` (they restate base-posture
  Rules — necessity's Principle-7 + concise-writing pointers folded into the Rule);
  `conformance` (posture already covers it); `security` (deferred to a future
  dedicated security skillset — claude finds low-hanging secrets via the posture).
- **Kept:** `consistency` + `executability` (specialized lenses the posture lacks);
  **added `skill-authoring`** — the only angle that beat holistic (caught the CSO
  description trap + rationalization loopholes holistic missed).

Full record + the "discrimination is the angle-necessity bar" principle and its
limits: [skill-validation/adversarial-review.md](../skill-validation/adversarial-review.md).

## Why deferred (not folded into PR-4)

PR-4 was the locked Decision I — a minimal two-line angle addition. Extraction is
a larger change that **edits a discipline skill** (`adversarial-review`), so it
warrants its own `superpowers:writing-skills` cycle (does a reviewer dispatched by
the command still apply the right angle when the definition lives in the skill?).
Folding it into PR-4 would have bundled two changes into one PR — the
merge-boundary anti-pattern PR-3's own rule targets. So PR-4 went into the command
(status-quo home) and this extraction is logged separately.

## Open question — resolved 2026-06-16

Where does angle selection (incl. the doc-dominant set) live? **Resolved: the
skill**, per the governing principle above. Selection is review judgment and must
be derivable from the standalone skill; the command defers to it. (This is the
reversal of the earlier lean — see the header note.)

## RED finding (2026-06-16)

The baseline did NOT pass — it produced a real design constraint. A reviewer told
only "apply the correctness angle" (no definition) drifted into the **necessity**
angle's lane; one given the catalog definition stayed scoped. **The angle
definition is load-bearing — a bare name is interpreted variably.** So the
command's collapsed reference must point the subagent at the named angle's
definition in the catalog, not merely name the angle.

## Prior-round notes (2026-06-16)

- **"Subagent isn't told how to access the catalog."** Refuted and still valid:
  the command's first mandatory subagent-prompt item prescribes loading
  `adversarial-review` (Skill tool, or read the SKILL.md from disk); a GREEN test
  confirmed the subagent loads the skill and applies the looked-up definition.
- **"Flag executability/doctrine-consistency as substitutable in the skill."**
  Originally rejected as "re-injects orchestration." **Now reversed by the
  governing principle** — selection *is* skill doctrine, so the doc-dominant set
  is stated in the skill's "Select by artifact" (as explicit per-artifact lists,
  not a swap rule). The earlier rejection was too command-centric.

## Approach (prose; implementer writes against patterns)

Done in the first pass (commits on `feature/extract-angle-catalog`): catalog
moved to the skill; both command copies reference it by name; README swept.

Standalone-selection redesign — done unless noted:

1. ~~RED: pre-edit skill alone can't select for a doc artifact.~~ Confirmed —
   "I had to guess"; dropped executability.
2. ~~GREEN: lean catalog + **Select by artifact** + depth line; re-run.~~ Standalone
   selection now correct (doc set incl. executability; angles discoverable).
3. ~~Slim both command copies (delete Doc-dominant + Angle-focus blocks; cold-read
   defers to skill; fix pre-pr cross-ref).~~ done.
4. ~~README tier table + angle prose reference skill selection.~~ done (+ top-level
   README overview + the 2026-06-15 deferred watch-item swept).
5. ~~Per-angle test set → `skill-validation/adversarial-review.md`; regress
   angle-dispatch + pre-pr + loop.~~ done — 7/7 angles caught their target;
   dispatch + pre-pr regress clean; `dd-review-command.md` updated (selection now
   skill-owned). Discrimination arm limitation logged in the new record.
6. Boundary: hook suite green (297); `/dd-review cold-read`; PR.

**Final round (2026-06-17) — angle audit + relocation:**

7. ~~Audit every angle vs holistic; drop to baseline + 3 angles.~~ done — see
   "Angle audit" above; skill rewritten (necessity Rule enriched; catalog =
   consistency + executability + skill-authoring; "When to apply").
8. ~~Propagate the 3-angle model to both command copies + hook README + top-level
   README.~~ done.
9. ~~Move `examples/commands/dd-review.md` → top-level `commands/`; update
   `install-skills.sh` + `tests/test_install_skills.py` + CLAUDE.md + README.~~
   done — installer suite green (9 passed).
10. ~~Rewrite `skill-validation/adversarial-review.md` (audit + necessity bar);
    update `dd-review-command.md`; add README + CLAUDE.md skill-validation refs.~~ done.
11. Re-run validation tests on the final 3-angle model; hook suite green;
    `/dd-review cold-read`; pause for review; PR. ← in progress.
