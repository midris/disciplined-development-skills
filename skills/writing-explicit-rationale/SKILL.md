---
name: writing-explicit-rationale
description: 'Use when a plan, spec, policy, design, or code choice needs durable reasoning to understand correctness or guide a future decision; especially for descopes, deferrals, exceptions, defensible alternatives, repeated re-litigation, or rationale that exists only in chat, a commit, or a PR.'
---

# Writing explicit rationale

**Role:** Companion — owns when and where rationale belongs, how much to include, and reference-not-repeat; not plan density, commit-message composition, or stale-reference sweeping.

## What rationale means here

There are three things that you should consider writing down. The **what**, the **how**, and the **why**. Always document **what** applies and **how** it works in practice. The **why** is not required. Add **why** only when it helps a future reader, implementer, or reviewer assess correctness or make a sound decision. Do not include any history that affects neither correctness nor future decisions.

## Keep one authoritative home

If review re-litigates the same decision twice, treat that as evidence that rationale is missing, unclear, or misplaced.
Audit related sites once rather than answering only the reported instance.

1. Search the affected code and project documentation for existing rationale.
2. If it is current, cite its stable path and section or decision site.
3. If it is missing, create it at the nearest durable place where the decision is visible:
   - plan, spec, policy, design, or architecture document — beside the affected choice;
   - code — at the decision site as a comment, or in a project document when the reasoning governs multiple sites.
4. At other sites, reference the authoritative home instead of restating its explanation.

Chat, commit messages, and PR descriptions may point to the authoritative rationale; they are not rationale stores.

## Resist duplicate rationale

| Excuse | Reality |
|---|---|
| "The user asked for the explanation in the commit or PR." | Put necessary rationale in the code or project document. The commit or PR may point there; do not copy the explanation. |
| "Repeating it here is clearer than making the reader follow a reference." | Parallel explanations drift. Improve the authoritative source and give the reader a precise reference. |
| "The background might be useful someday." | Background without a correctness or decision consequence is noise and future cleanup surface. |
