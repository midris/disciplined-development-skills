---
name: concise-writing
description: 'Use when writing or finalizing prose a reader must get through — docs, READMEs, plans, specs, design notes, commit bodies, code comments, and chat replies — and the output risks being verbose, padded, wordy, or bulky; also when asked to be more concise, tighten, trim, or "get to the point." Skill/reference authoring is owned by superpowers:writing-skills (a stricter, every-word-counts bar) — use that there, not this.'
---

# Concise writing

**Role:** Companion — invoke when producing prose a reader has to get through.
**Owns:** the verbosity test (does cutting this lose information or necessary framing?), the named padding patterns, the two-altitude compression pass, the anti-over-trim guard.
**Does not own:** what goes into a plan vs. code (`lean-plan-writing`); whether rationale is present at all (`writing-explicit-rationale`); stale-reference sweeps (`sweeping-stale-references`).

## Overview

Cut **verbosity** — words beyond what the information needs — while keeping every bit of information and any framing that aids comprehension. Density is good; padding is not. This is not brevity-for-its-own-sake: a rich, complete document is the goal.

## The core test

For each sentence or clause:

> Does cutting it lose **information** or **necessary framing**?

- **Neither** → cut it.
- **Either** → keep it.

The "or framing" half is the guard: recaps, misread-preventing transitions, and orienting context all carry framing, so they stay. Padding carries neither.

## The compression pass — two altitudes

Run before finalizing any durable artifact (and self-apply to chat). Trim at both altitudes:

- **Local** — sentence and clause level, via the core test. Doable as you write.
- **Global** — read the edit *against the whole artifact*: does this content already appear elsewhere? Cross-section duplication surfaces only at this altitude, so any edit that adds prose requires this read.

## Verbosity patterns

| Pattern | Cut |
|---|---|
| **Meta-framing** — sentences about what the doc/section does ("This section explains…", "In this guide we'll…") | The content explains itself. Delete the narration. |
| **Say-it-twice** — a fact, then the same fact reworded in the next sentence with nothing added | Keep one statement. (Deliberate reinforcement is exempt — see When NOT to cut.) |
| **Cross-section duplication** — the same definition or fact stated in two places serving no distinct purpose | State it once, at its best home. (Global-altitude catch.) |
| **Over-sectioning** — a short doc split into many headed subsections, each with a lead-in sentence | Collapse headers; the lead-ins vanish with them. |
| **Unrequested elaboration** — advice or inference past the source material, added to seem thorough | Cut unless it is genuinely necessary framing. |
| **Emphasis/hedge inflation** — scattered bold, doubled descriptors ("each and every"), "always / so it always" | One clear statement, minimal emphasis. |

## Before / after

Meta-framing and say-it-twice removed; every fact kept (~45% shorter):

> **Before:** This section explains how eviction works. The cache uses LRU eviction. Total size is capped at `MAX_CACHE_SIZE_MB`. The cache may grow up to this limit; once it would exceed the limit, the service reclaims space by evicting least-recently-used entries until it is back under the cap.
>
> **After:** The cache uses LRU eviction, capped at `MAX_CACHE_SIZE_MB`. On write, if it is over the cap, it evicts least-recently-used entries until back under.

## When NOT to cut

Over-trimming is its own failure. Keep:

- **Closing recaps and navigation aids** in long documents — they carry framing.
- **Deliberate repetition** for emphasis or retention — restating a key point in a summary, or echoing a critical warning where it's needed. The target is *accidental* restatement that adds nothing, not intentional reinforcement.
- **Orienting context** that prevents a misread or makes a jump followable.
- **Rationale** — owned by `writing-explicit-rationale`; concision never licenses dropping the why.
- **Spec/plan completeness** — owned by `lean-plan-writing`; a requirement list is not padding.

Concision is judgment, not mechanical minimization. When unsure whether something is framing or padding, keep it and flag it.

## Rationalizations

| Excuse | Reality |
|---|---|
| "More words make it clearer for junior readers." | Padding lowers clarity — it buries the point. Density with good structure is what helps. |
| "Being thorough means covering every angle." | Thorough = every required fact, once. Restating and elaborating past the source is padding, not thoroughness. |
| "The intro and the section should each be self-contained." | Then cross-reference; don't re-state. One home per fact. |
| "A lead-in sentence per section reads more smoothly." | In a short doc the headers and lead-ins are the bulk. Collapse them. |
| "It's just one extra sentence." | One per paragraph is how a 130-word doc becomes 300. The test is per-sentence. |
| "Trimming risks dropping something important." | That's what the core test's 'or framing' half protects. Cut only what carries neither information nor framing. |

## Red flags

Stop and run the compression pass if you catch yourself:

- Opening a section by describing what the section will do.
- Rewording the previous sentence instead of advancing — and nothing new is added.
- Finalizing added prose without reading it against the whole document (the global-altitude check).

## Pairing

- `lean-plan-writing` — when editing plans/specs, both apply (it governs what goes in; this governs how many words carry it).
- `writing-explicit-rationale` — keep the rationale; tighten its wording.
- `sweeping-stale-references` — a trim that removes a referenced anchor triggers a sweep.

Invoked on-demand, not gate-shaped — apply whenever prose risks padding.
