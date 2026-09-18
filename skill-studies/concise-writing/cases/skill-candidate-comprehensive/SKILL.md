---
name: concise-writing
description: 'Use whenever generating or revising reader-facing prose for project files or durable project records — docs, READMEs, plans, specs, design notes, status updates, summaries, commit bodies, or code comments — or response-only prose, including when asked to be concise, tighten, trim, shorten, or "get to the point". Do not use when the user explicitly requests that the agent response itself be a detailed explanation.'
---

# Concise writing

## Contract

Apply the complete method to prose in project files and durable project records, including code comments and prose deliverables within code, structured data, or required syntax; leave surrounding code, data, and syntax unchanged.
For response-only prose, use a light pass and equivalence gate unless the user explicitly requests a detailed explanation; then do not apply `concise-writing`.

A concise revision is lossless only when, in every relevant circumstance, a careful reader can understand and use it as they could the source, without guessing or filling gaps.
Any loss of readability, meaning, impact, effectiveness, completeness, correctness, findability, or any other consequential quality is a hard failure.
During skill or reference authoring, `superpowers:writing-skills` owns authoring decisions and validation.

## Method

1. **Establish the baseline.** Read each section and the whole artifact to understand how a careful reader can use the source.
2. **Transform losslessly.** Revise from the source.
   Keep every source-explicit distinction explicit in the result; a broader category or meaning recoverable only by inference is not equivalent.
   Apply the padding patterns locally and across the whole artifact only where the lossless invariant still holds.
   Give each distinct meaning one clear, findable home; repeat only for necessary framing.
3. **Verify both directions.** Compare source and result section by section and as whole artifacts.
   In any relevant circumstance, could a careful reader understand or use the result differently, or have more difficulty finding necessary meaning?
   If yes or uncertain, restore the source until the invariant holds; then confirm every result claim is source-supported.

## Padding patterns

| Pattern | Cut |
|---|---|
| **Meta-framing** — section-purpose narration | Present content. |
| **Say-it-twice** — immediate restatement | Keep one statement. |
| **Cross-section duplication** — repetition without distinct purpose | Keep one home; cross-reference. |
| **Over-sectioning** — headings and lead-ins fragment short prose | Collapse them. |
| **Unrequested elaboration** — advice or inference beyond source | Cut unless necessary framing. |
| **Emphasis/hedge inflation** — doubled descriptors or qualifiers | State it once. |

## Examples

**Access deadline**

> **Before:** This section explains staging access.
> Engineers must submit the Access form to Platform Operations two days before deployment.
> The deadline is two days before.
>
> **After:** For staging access, engineers must submit the Access form to Platform Operations two days before deployment.

**LRU eviction**

> **Before:** This section explains how eviction works.
> The cache uses LRU eviction.
> Total size is capped at `MAX_CACHE_SIZE_MB`.
> The cache may grow up to this limit; once it would exceed the limit, the service reclaims space by evicting least-recently-used entries until it is back under the cap.
>
> **After:** The cache uses LRU eviction and is capped at `MAX_CACHE_SIZE_MB`.
> When total size would exceed the cap, the service evicts least-recently-used entries until total size is back under.

This rewrite is lossless because reaching the cap and exceeding it lead to different behavior, and the boundary remains explicit.

## Rationalizations

| Excuse | Reality |
|---|---|
| “More words are clearer or more thorough.” | Complete, clearly structured prose is thorough; padding is not. |
| “Each section needs its own explanation.” | Give each distinct meaning one clear, findable home; cross-reference it. |
| “Trimming may drop something important.” | Apply the lossless reader-use test; if the result could be understood or used differently, restore the source until the invariant holds. |

## Composition

- `lean-plan-writing` owns plan/spec content; `concise-writing` compresses its prose.
- `writing-explicit-rationale` owns rationale necessity; `concise-writing` tightens the retained rationale.
- `sweeping-stale-references` reconciles moved or removed anchors.
