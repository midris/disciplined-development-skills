# Abandoned CW rebuild: preservation record

This package preserves material from the abandoned testing process. Its prompts, instructions and approvals are historical only.
Current work follows the [new spec](../../../plans/specs/2026-09-11-model-driven-skill-testing-framework.md) and [new plan](../../../plans/2026-09-11-model-driven-skill-testing.md).

`manifest.json` records original locations, sizes/hashes and archived locations.
The 54-file temporary working packet was copied to `scratch-snapshot/` and verified byte-for-byte; the originals remain in place.
That local snapshot is deliberately excluded from Git because it contains working notes and scratch records. A Git checkout contains the manifest, not that payload; preserve the local snapshot when migrating machines.
The eight abandoned CW-17/CW-18 v2 inputs are preserved byte-for-byte under `untracked-inputs/` and included in Git; their original paths are recorded in the manifest.
