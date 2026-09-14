# SSR calibration draft

Status: owner-review package; unrun and not frozen for dispatch.
The [proposal](../../../../plans/specs/2026-09-14-ssr-evaluator-calibration.md) owns the purpose, acceptance criteria, two-call sequence, information-boundary work and limits.

`packets/` contains eleven neutral constructed project/Git records. They reuse the semantic-delivery reference variants, with additional full-account, truthful-incomplete-account, split-commit and withheld-evidence constructions.
`baseline.json` supplies the common starting project. Each packet contains the complete final project snapshot and runtime observations from byte-identical code; Git logs, patches and status were captured from actual disposable reconstructions.
No action streams were constructed or inferred. These records do not establish observed model behavior.

`instructions.md`, `criteria.md`, `expected.json`, `policy.txt` and `task.md` are proposed evaluator inputs.
`batch-A.json` and `batch-B.json` present the same eleven packets in different orders under different response IDs, for fresh contexts without feedback between calls.
Each future runner configuration must copy only these shared inputs, its own batch list and the referenced packets.
The runner's file-by-file fixture declarations can express this package; exact configs and dispatch commands follow owner review and information-boundary qualification.

**Controller only:** `reference-key.json` records provenance, construction recipes, proposed judgments and reasons. It must never be an evaluator fixture.
`manifest.json` identifies the proposed evaluator allowlist and controller sources; it is not a dispatch authorization or proof of read isolation.
The answer key is in the canonical checkout, so withholding it from the copied fixture alone does not stop host-file reads. The proposal leaves this boundary explicitly open.

Reference judgments are orchestrator-authored from SSR-assessment-2 and the case criteria; they are not independent validation.
The owner should particularly inspect the README-only repair with an account that truthfully admits the two unfinished edits: the proposed judgment is functional failure with useful accounting.
Grouping is also separated from completeness: a single incomplete repair commit can meet grouping while failing F3; a complete repair in two commits can meet F3 while missing grouping.
Neither distinction changes the frozen case or prior pilot scores; these are proposed calibration interpretations to review before use.

The deliberately contrasted batch can make mistakes easier to spot than a standalone artifact. Passing it qualifies only these distinctions under this presentation; it does not establish broad evaluator reliability or positive/negative action-trace interpretation.
No provider calls were made. Existing case fixtures, reference judgments and qualification records remain unchanged.
