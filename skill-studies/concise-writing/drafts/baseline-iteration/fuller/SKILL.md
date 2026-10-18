---
name: concise-writing
description: 'Use when writing or revising reader-facing prose — docs, READMEs, plans, specs, design notes, commit bodies, or code comments — that risks being verbose, padded, repetitive, wordy, or bulky; also when asked to tighten, trim, shorten, or "get to the point". Excludes skill and reference authoring.'
---

# Concise writing

**Role:** Companion — invoke when producing prose a reader has to get through.
**Owns:** removing verbosity locally and across the whole artifact while preserving information, useful framing and readability.
**Does not own:** plan content, rationale necessity or stale-reference reconciliation; see Pairing.

## Aim

Produce a complete, correct document that is easy for its reader to use.
Cut words that carry neither information nor useful framing.
Apply the method before finalizing the reader-facing text.
Preserve the source’s requirements, qualifications, uncertainty and reasoning; a smaller document is useful only when those still work.

## Method

### 1. Understand the reader and material

Read the complete source and any supplied additions.
Identify what the reader needs to understand, decide and do, including where they may enter the document directly.
Use the whole artifact as context: prose, tables and unchanged code can convey meaning together.
When the task authorizes only wording changes, preserve the surrounding executable code, data and required syntax.

### 2. Organize around that use

Put the decision, supporting evidence and next actions where the reader can readily connect them.
Choose headings, lists and sequence for the actual material; there is no required document template.
Group related requirements instead of scattering additions or appending a second account of the same policy.
Give repeated explanation a clear home, preserving warnings, recaps and orientation where they serve a different reading context or point of action.
Reordering and faithful paraphrase are welcome; preserving meaning does not require keeping every source sentence or heading.

### 3. Trim at both altitudes

For each sentence or clause, ask: does removing it lose information or framing that helps comprehension?
Keep clauses that carry either; cut those that carry neither.
Then read the complete result for remaining duplication, unnecessary transitions and scattered information that sentence-level edits miss.
Use these patterns to identify waste, judging their purpose in context.

| Pattern | Edit |
| --- | --- |
| **Meta-framing** — narration about what a section explains | Present the content directly. |
| **Say-it-twice** — adjacent restatement with nothing added | Keep the clearest statement. |
| **Cross-section duplication** — repeated explanation without a distinct reader use | Consolidate where the information is needed; retain useful point-of-use reinforcement. |
| **Over-sectioning** — headings and lead-ins fragment a short document | Combine related material into a followable sequence. |
| **Unrequested elaboration** — advice or inference beyond supplied material | Connect the supplied facts without adding unsupported conclusions, capabilities or assurances. |
| **Emphasis/hedge inflation** — doubled descriptors or empty qualifiers | State the meaning plainly; preserve qualifications that limit the claim. |

### 4. Verify the complete result

When editing existing text, draft first.
Compare the draft with all supplied material, including any new requirements, and inspect the diff when editing existing text.
Preserve required actions, their specified owners and governing conditions.
A completed-result formulation is valid when it still entails what the source requires; confirming a related state is not enough.
Keep the scope of evidence and uncertainty intact; successful observations do not by themselves establish broader reliability or validate untested conditions.
For source-based writing or editing, read back from the result to its sources too: each factual claim must be supported by the material and authorized additions.
Finally, read as the intended audience: can they follow the reasoning, find safeguards and take the same informed actions without reconstructing a missing connection?
Correctness and useful explanation take priority over word savings.

## What to preserve

Over-trimming is its own failure.
Keep:

- **Rationale and orienting context:** keep the explanation that makes an action, limitation or transition understandable.
- **Useful repetition:** closing recaps, navigation aids and warnings at independently used entry points can support comprehension and safe action.
- **Requirements and qualifications:** preserve obligations, decision boundaries, uncertainty and plan/spec completeness while tightening their expression.

When unsure whether something is framing or padding, keep it and flag it.
Do not invent a missing rationale to make the document feel complete.

## Examples

### Compressing an explanation

Meta-framing and say-it-twice removed; the eviction condition and size limit remain:

> **Before:** This section explains how eviction works. The cache uses LRU eviction. Total size is capped at `MAX_CACHE_SIZE_MB`. The cache may grow up to this limit; once it would exceed the limit, the service reclaims space by evicting least-recently-used entries until it is back under the cap.
>
> **After:** The cache uses LRU eviction, capped at `MAX_CACHE_SIZE_MB`. If it would exceed the cap, the service evicts least-recently-used entries until back under.

### Preserving an action and its constraints

> **Before:** This section explains staging access.
> Engineers must submit the Access form to Platform Operations two days before deployment.
> The deadline is two days before.
>
> **After:** For staging access, engineers must submit the Access form to Platform Operations two days before deployment.

This constructed illustration removes narration and repetition while retaining the actor, action, recipient and deadline; it is not an observed test result.

## Rationalizations

| Excuse | Reality |
|---|---|
| "More words make it clearer for junior readers." | Padding lowers clarity — it buries the point. Density with good structure is what helps. |
| "Being thorough means covering every angle." | Thorough = every required fact, once. Restating and elaborating past the source is padding, not thoroughness. |
| "The intro and the section should each be self-contained." | Then cross-reference; don't re-state. One home per fact. |
| "A lead-in sentence per section reads more smoothly." | In a short doc the headers and lead-ins are the bulk. Collapse them. |
| "It's just one extra sentence." | One per paragraph is how a 130-word doc becomes 300. The test is per-sentence. |
| "Trimming risks dropping something important." | That's what the core test's 'or framing' half protects. Cut only what carries neither information nor framing. |

## Pairing

- `lean-plan-writing` — when editing plans/specs, both apply (it governs what goes in; this governs how many words carry it).
- `writing-explicit-rationale` — keep the rationale; tighten its wording.
- `sweeping-stale-references` — a trim that removes a referenced anchor triggers a sweep.

Invoked on-demand, not gate-shaped — apply whenever prose risks padding.
