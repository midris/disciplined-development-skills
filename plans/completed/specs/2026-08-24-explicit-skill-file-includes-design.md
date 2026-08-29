# Explicit Skill File Includes Design

**Status:** Implemented under schema `"0.1"` and superseded on 2026-08-28 by
the reusable prompt runner's schema `"0.2"` contract.

## Goal

Make every provider-visible skill file explicit in `skilltest` configuration so a scenario receives exactly its declared skill context.

## Configuration contract

Configuration schema version becomes the string `"0.1"`. Every primary skill and dependency declaration contains exactly `id`, `source`, and `include`:

```json
{
  "id": "disciplined-development",
  "source": "../../../../skills/disciplined-development",
  "include": ["SKILL.md"]
}
```

`include` is a non-empty list of unique relative file paths. It must explicitly contain root-level `SKILL.md`. Nested files such as `scripts/tool.py` are allowed.

Each included path must resolve inside `source` to a regular file. Reject directories, symlinks, absolute paths, empty paths, `.` or `..` components, duplicate paths, missing files, and any declaration without `SKILL.md`.

## Copy behavior

The runner copies only the declared files into retained inputs and the provider workspace, preserving each relative path. It never copies the source directory wholesale.

An omitted or invalid `include` is a configuration error before run allocation. There is no fallback to whole-directory copying.

## Migration

Update both existing WER configurations to schema version `"0.1"` and `include: ["SKILL.md"]`. Update the runner README, design contract, loader, workspace preparation, and focused tests in the same change.

The `T2` port will declare `include: ["SKILL.md"]` for all nine supplied skills. Its implementation remains separate and resumes only after this runner change is complete.

## Non-goals

- Glob or gitignore-style matching.
- Exclusion lists.
- Directory includes.
- Implicit inclusion of `SKILL.md`.
- Backward compatibility with schema version `1` or declarations without `include`.
- Any provider, result, fixture, skill, or scenario behavior change beyond configuration migration.
