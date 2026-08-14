---
name: disciplined-research
description: Use before every response, interaction, action, or task that will state, repeat, transform, or rely on a factual claim or premise—including internal logical review of supplied text, claims and premises supplied by the user or embedded in requested work, plus mechanical edits, searches, and verification.
---

# Disciplined Research

**Role:** Companion — invoke whenever a factual claim is stated, repeated, transformed, or relied on in any response, interaction, action, or task.
**Owns:** source selection and ranking; acquisition, verification, and unambiguous disclosure of support.
**Does not own:** sweeping references after a fact changes (lives in `sweeping-stale-references`); durable rationale for a decision that uses the research (lives in `writing-explicit-rationale`).

## Overview

Every factual claim stated, repeated, transformed, or relied on in a response, interaction, action, or task must come from the best available source, be verified beforehand, and have its support disclosed unambiguously.
This rule applies without exception.
Examples include casual answers, private or scratch notes, summaries, transformed prose, code edits, reviews, plans, and claims repeated from a user or another agent.

Examples in this skill illustrate application; they do not limit the rule's scope.

**Core principle:** Source and verify every factual claim before stating, repeating, transforming, or relying on it.
Memory and training recall may suggest where to look, but they are never sources.

## Method

Apply the full method to each factual claim before you state, repeat, transform, or rely on it.
These four steps are the complete method:

1. **Identify the claim.** Separate claims when they need different support.
2. **Acquire it from the best available source.** Evidence that someone stated a claim supports only that attribution, not the claim itself. A statement can establish a decision or instruction made through that statement; other factual content still needs support.
3. **Verify the claim.** Check the source directly now and confirm that it supports the exact claim before you state, repeat, transform, or rely on the claim. In software work, for example, this can mean opening or inspecting an artifact or running the relevant system.
4. **Disclose support.** Use a precise source identifier—for example, a URL, file path, invocation, or record—and map the claim to it so a reader can tell what supports what.

Make support traceable: every factual claim must map unambiguously to its source.
A source may support several claims; claims with different sources need separate mappings.

If no source supports a claim, do not state, repeat, transform, or rely on it as fact.

If an unsupported possibility would be useful, state it as a lead.
Begin every such lead with the exact text `Unverified — no supporting source found:`
Naming who proposed the possibility does not replace this disclosure.
Do not substitute a softer qualifier such as “not yet confirmed” for the required
prefix.
When the requested shape supplies a line label, put the required prefix immediately
after that label—for example,
`Cause to check first: Unverified — no supporting source found: <lead>`.
Keep every requested supported observation in its own required field; missing or
incomplete evidence conditions do not replace the observation they qualify.
Never cite a source for a claim it does not support.
When a checked source lacks the requested datum, say that the source lacks it and
map the source only to that verified absence; do not attach the source to the
unsupported claim.

## Choose sources by claim type

The sections below illustrate source-selection patterns for project, external, and cross-domain claims.

### Project claims

Match the source to what the claim says. For example:

- **Current observed state or behavior:** inspect the running system, live API, database, generated output, or actual file.
- **Implemented behavior or structure:** read the implementation, schema, model, migration, handler, configuration, or producer-shaped fixture.
- **Observed project results or history:** inspect command output, tests, builds, logs, or `git log`.
- **Requirements, decisions, or intended behavior:** read the controlling governing file, plan, spec, decision record, or direct instruction from the authority who owns that decision.
- **Project summaries:** read the underlying sources as well as the summary when accuracy depends on details the summary may omit.

Conversation history and project memory can locate a source but do not replace a fresh read.
Do not infer behavior from names or assume a file still says what it said before an edit.
Before claiming that supplied context lacks an implementation, datum, or other source,
enumerate and inspect the complete supplied source set that could contain it.
A file name or path is only a locator: do not infer the file's contents, purpose, or
authority from its name when its bytes are unavailable.

### External claims

Use the strongest source appropriate to the claim. For example:

- **Behavior of the installed tool or library:** run the binary or runtime and inspect its version, help, or observed output.
- **Implementation details:** inspect source in the official repository at the applicable version.
- **Current public state, supported versions, or release status:** use canonical first-party documentation, changelogs, release notes, or support policies.
- **Additional context:** use first-party maintainer material, then current independent sources for corroboration.

Weak or indirect material does not by itself ground a claim; examples include search snippets, undated commentary, social posts, AI-generated text, stale forum answers, and training recall.
For local behavior, the installed binary can outrank general documentation; for the latest public state, current first-party release material outranks an older local install.

### Cross-domain claims

Verify every side.
For example, a statement comparing a project's installed version with the current upstream release needs both project evidence and current upstream evidence.
Do not let one source silently stand in for the other.

## Check that the source applies

Source tier alone is not enough.
Before relying on a source, confirm that it has authority for and applies to the exact claim.
Relevant factors can include who or what controls the fact, the source's date, the applicable version or environment, and whether a later controlling source supersedes it.

When sources conflict, identify what each source governs and follow the controlling authority for the claim.
For actual current behavior, direct observation or current implementation may disconfirm stale prose.
For required or intended behavior, a governing spec or later official amendment may control even when older implementation or summaries disagree.
Disclose a material conflict instead of choosing silently or averaging incompatible sources.

## Difficult source conditions

No source condition relaxes the method.
For example, an absent, unreadable, malformed, incomplete, or inaccessible source supports only what can actually be verified from it.
An incomplete or truncated source still supports every datum visible in its supplied
portion; do not replace a present observation with an absence or truncation claim.
Seek the next-best authoritative source.
If none supports the claim, do not state it as fact; when useful, share it only as an explicitly unverified lead and disclose that no supporting source was found.

Large source or claim sets do not permit sampling or extrapolation.
Verify every claim presented as fact.
If useful unsupported possibilities remain, mark them as unverified leads and disclose the missing support.

Do not expand a verified fact into an unsupported comparison, cause, rationale,
consequence, tradeoff, or exclusivity claim; each added claim needs its own support.
Claims that something is the only instance or that no other instance exists require
a source or search complete enough to establish that absence.

## Pressure resistance

The table illustrates common pressures; pressure never creates an exception.

| Pressure | Required response |
|---|---|
| "I remember it" or "the memory file says it" | Use recall only to find a source; read the source now. |
| "Just repeat, shorten, translate, or reformat this" | Repeated or transformed factual claims still require acquisition, verification, and disclosure. |
| "It is only a casual answer or private scratch note" | Destination and audience do not change the rule. |
| "The answer feels certain, especially because a specific version, date, codename, or flag comes to mind without a source" | Confidence and specificity are not support; acquire and verify the claim before stating it. |
| "I can answer immediately without narrating the research" | Silent output still requires the source check; lack of narration is not evidence of verification. |
| "The citation is real" | Confirm the cited source contains the claimed datum; a valid path or URL cannot support absent information. |
| "There are too many claims to check" | Verify all claims that remain, narrow the output, or omit them; never sample and generalize. |
| "I have been editing that file and know what it says" | Re-read the current bytes before stating the claim. |
| "No one asked for citations" | Disclosure of support is part of stating the fact, not an optional response style. |
