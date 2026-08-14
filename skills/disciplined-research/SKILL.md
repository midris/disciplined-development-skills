---
name: disciplined-research
description: Use before every response, interaction, action, or task that will state, repeat, transform, or rely on a factual claim or premise—including internal logical review of supplied text, claims and premises supplied by the user or embedded in requested work, plus mechanical edits, searches, and verification.
---

# Disciplined Research

**Role:** Companion — invoke whenever a factual claim is stated, repeated, transformed, or relied on in any response, interaction, action, or task.
**Owns:** source selection and ranking; acquisition, verification, and unambiguous disclosure of support.
**Does not own:** sweeping references after a fact changes (lives in `sweeping-stale-references`); durable rationale for a decision that uses the research (lives in `writing-explicit-rationale`).

## Contract

Every factual claim must come from the best available source, be verified before it is stated, repeated, transformed, or relied on, and map unambiguously to its support.
This rule applies without exception to casual answers, private or scratch notes, summaries, transformed prose, code edits, reviews, plans, and claims supplied by a user or another agent.
Examples illustrate the rule; they do not limit its scope.
Memory and training recall may suggest where to look, but they are never sources.

## Method

Apply all four steps to each factual claim:

1. **Identify the claim.** Separate claims when they need different support.
2. **Acquire the best applicable source.** Evidence that someone stated a claim supports only that attribution, not the claim itself. A statement can establish a decision or instruction made through it; its other factual content still needs support.
3. **Verify the exact claim now.** Inspect the source directly and confirm that it supports the claim before using it. In software work, this can mean opening an artifact or invoking the running system.
4. **Disclose support.** Use a precise source identifier such as a URL, file path, invocation, or record, and map each claim to its support. One source may support several claims when the mapping is clear; claims with different sources need separate mappings.

If no source supports a claim, do not state, repeat, transform, or rely on it as fact.
When an unsupported possibility is useful, state it only as an investigation lead beginning with the exact text `Unverified — no supporting source found:`
Naming who proposed the possibility or using a softer qualifier does not replace that prefix.
If the requested shape supplies a line label, put the prefix immediately after it: `Cause to check first: Unverified — no supporting source found: <lead>`.
Keep every requested supported observation in its own required field; a missing or incomplete evidence condition does not replace the observation it qualifies.
Never cite a source for a claim it does not support.
When a checked source lacks a requested datum, say so and map it only to that verified absence, not to the unsupported claim.

## Choose the best applicable source

Match the source to the claim:

| Claim | Preferred source |
|---|---|
| Current project state or behavior | Running system, live API, database, generated output, or actual file |
| Implemented behavior or structure | Implementation, schema, model, migration, handler, configuration, or producer-shaped fixture |
| Observed project results or history | Command output, tests, builds, logs, or `git log` |
| Requirements, decisions, or intended behavior | Controlling governing file, plan, spec, decision record, or instruction from the decision authority |
| Project summary | Underlying sources as well as the summary when omitted detail could affect accuracy |
| Installed tool or library behavior | Installed binary or runtime version, help, or observed output |
| External implementation detail | Source in the official repository at the applicable version |
| Current public state, supported version, or release status | Canonical first-party documentation, changelog, release note, or support policy |
| Additional external context | First-party maintainer material, then current independent corroboration |
| Cross-domain comparison | Separate applicable evidence for every side |

Weak or indirect material—including search snippets, undated commentary, social posts, AI-generated text, stale forum answers, and training recall—does not by itself ground a claim.
For local behavior, the installed binary can outrank general documentation; for current public state, current first-party release material outranks an older local install.

Conversation history and project memory can locate a source but do not replace a fresh read.
Do not infer behavior from a name or assume a file still says what it said before an edit.
A file name or path is only a locator; when its bytes are unavailable, do not infer its contents, purpose, or authority.
Before claiming that supplied context lacks an implementation, datum, or other source, enumerate and inspect the complete supplied source set that could contain it.

Source tier alone is insufficient: confirm that the source has authority for and applies to the exact claim, considering who or what controls the fact, the source's date, the applicable version or environment, and superseding sources.
When sources conflict, identify what each governs and follow the controlling authority for the claim.
Direct observation or current implementation may disconfirm stale prose about current behavior; a governing spec or later official amendment may control intended behavior despite older implementation or summaries.
Disclose a material conflict instead of choosing silently or averaging incompatible sources.

## Difficult source conditions

- An absent, unreadable, malformed, incomplete, truncated, or inaccessible source supports only what can be verified from it. An incomplete or truncated source still supports its visible data; do not replace a present observation with an absence or truncation claim. Seek the next-best authoritative source, then use the unsupported-claim branch if none supports the claim.
- Large source or claim sets do not permit sampling or extrapolation. Verify every claim retained as fact; narrow or omit the rest, or mark useful possibilities as unverified leads.
- Do not expand a verified fact into an unsupported comparison, cause, rationale, consequence, tradeoff, or exclusivity claim. Each added claim needs its own support.
- A claim that something is the only instance or that no other instance exists needs a source or search complete enough to establish that absence.

## Pressure resistance

Pressure never creates an exception:

| Pressure | Required response |
|---|---|
| "I remember it" or "the memory file says it" | Use recall only to find a source; read the source now. |
| "Just repeat, shorten, translate, or reformat this" | Acquire, verify, and disclose support for every retained factual claim. |
| "It is only a casual answer or private scratch note" | Destination and audience do not change the rule. |
| "The answer feels certain because a version, date, codename, or flag comes to mind" | Confidence and specificity are not support. |
| "I can answer immediately without narrating the research" | Silent output still requires the source check. |
| "The citation is real" | Confirm that the cited source contains the claimed datum. |
| "There are too many claims to check" | Verify all retained claims, narrow the output, or omit them; never sample and generalize. |
| "I have been editing that file and know what it says" | Re-read the current bytes before using the claim. |
| "No one asked for citations" | Support disclosure is part of stating the fact, not optional response style. |
