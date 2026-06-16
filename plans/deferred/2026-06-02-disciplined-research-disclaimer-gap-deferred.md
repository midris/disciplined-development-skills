# `disciplined-research` skill — disclaimer-as-substitute gap

Surfaced 2026-06-02 during the Meetily / audio-capture pivot discussion. Deferred so the skill edit doesn't drag the in-flight design work.

## Context

When recommending process tap over ScreenCaptureKit, I stated several load-bearing facts from recall (macOS version floors, permission-string differences, recording-indicator behaviour) and added the caveat *"if we lock them into the spec I'll verify against Apple's docs first."* The user caught this: a claim driving a recommendation in the current message is already load-bearing — "I'll verify before locking" is backwards. Verification under that posture moves *after* the recommendation has shaped the user's next decision.

Subsequent verification found two of those claims wrong on specifics and two unverifiable, which would not have been caught by the current skill text. The skill's existing red flag *"A specific version, date, codename, or flag name in your head, no source citation in your head"* should have stopped me — that's an execution failure, not a skill gap. But the *disclaimer-as-substitute* pattern (naming the uncertainty honestly while still using the claim) is not explicitly covered, and that's the gap to close.

## Proposed edits to `/Users/simon/work/coronis/code/meeting-pipeline/.claude/skills/disciplined-research/SKILL.md`

### 1. Add a rationalization row

Append to the "Common rationalizations" table (after the "I know what's in [file]" row):

| Excuse | Reality |
|---|---|
| "I'll verify before it lands in [spec / commit / PR / later artifact]." | A disclaimer naming uncertainty is not a substitute for verifying. The moment a claim drives a recommendation, comparison, or design decision the reader will act on in the **current** message, the verification window has already closed. "I'll verify before X" means "I already know this should be verified" — verify now. |

### 2. Add a red flag

Append to the "Red flags" bullets:

- About to add a hedge like *"worth verifying before we lock"* / *"pending confirmation"* / *"should double-check"* and state the specific claim anyway. Naming the gap doesn't close it. Either verify before stating, or omit the specifics and describe only what is grounded.

### 3. Extend the load-bearing destination list

Under "Verify before citing", add to the bullet list (after "Pasted into a README, status update, or public-facing artifact."):

- Drives a recommendation, comparison, choice, or design decision in the **current** response, before any later verification step.

### 4. Sharpen the load-bearing framing

Below the destination list and the "Destination defines load-bearing…" paragraph, add a new paragraph:

> Load-bearing is determined by *use*, not by the downstream artifact you have in mind. Once a claim is in the response driving the reader's next action, it's load-bearing — even if you also plan to use it later. There is no "still safe to state ungrounded because the *real* destination is downstream."

## Why deferred

- The in-flight work (audio-capture pivot, Decision 1 amendment, chunk-2 replan) shouldn't be interrupted for a skill edit.
- The edit is small but has its own discipline overhead: invoke `superpowers:writing-skills`, run the existing skill's own self-test patterns, sweep for stale references from other skills/hooks/docs that reference the rationalization table or red-flag list by position.
- Existing red flags would have caught the immediate failure if followed; the proposed edits harden against a related-but-distinct pattern, not the one currently blocking work.

## When picked up

1. Invoke `superpowers:writing-skills` (skill-edit mode).
2. Apply the four edits above. Preserve the existing register (concise, table+bullets, no emoji).
3. Re-read the edited skill end-to-end to confirm the four additions cohere with the existing structure (rationalizations + red flags + destination list are mutually consistent; no contradictions or duplications introduced).
4. Sweep for stale references — search `.claude/skills/`, `CLAUDE.md`, any hooks under `.claude/skills/disciplined-development/hooks/`, and other plans/specs for positional references to the rationalization table or red-flag list. Update any that would break.
5. Test against a real recall situation in the next session where this comes up — confirm the new red flag and rationalization row actually fire before the disclaimer phrasing reaches the response.
