# Testing a skill

Start with the [study workflow](methodology/README.md) and [governing framework](methodology/framework.md).
Read the shipped skill and agree on the behavior a future user needs before choosing cases or drafting a revision.
The [format contracts](methodology/formats/README.md) and [runner guide](runner/README.md) cover frozen inputs, collection, retention and assessment.

## Walk through a study offline

From a clean checkout on macOS with Git, uv and Python 3.11 or later, run the following commands in one shell.
The runner tests create disposable repositories and synthetic subjects.
The walkthrough leaves the example under a new temporary directory for inspection.

```sh
cd tests/runner
uv sync --locked
export TMPDIR="$(getconf DARWIN_USER_TEMP_DIR)"
study_tmp=$(mktemp -d)
uv run --locked --offline pytest -q tests/process_smoke/test_study_walkthrough.py \
  --basetemp "$study_tmp/walkthrough"
protocol=$(find "$study_tmp/walkthrough" -type f -name protocol.md | head -1)
uv run --locked --offline skilltest docs check "$protocol" --ready-for assessment --batch example
cat "$(dirname "$protocol")/example-assessment.md"
```

The walkthrough freezes a two-attempt study in Git, runs both slots through the installed CLI with a local stand-in for Codex, and checks the resulting bundles and judgments at collection and assessment readiness.
Inspect its protocol, manifest, attempt index and results beside the assessment.
The source assigns badge pickup to the west desk. One answer directs the visitor there and one sends them east. Expect two included attempts, one met and one not met, with both results cited.
To see the readiness check reject a mismatch, change the F1 count in the working example assessment from one met and one not met to two met and zero not met, then rerun the check. It compares that table to the revision-pinned result records.
Run the full offline suite with `uv run --locked --offline pytest -q` from the same directory.

## Trace a real decision

The [Concise Writing adoption record](skills/concise-writing/README.md) identifies the selected skill bytes and links the underlying comparisons.
The discovery trial supported changing the description. The body comparisons found no consistent consequential benefit, so the owner retained the original body.
The record also preserves the failed rollback instruction and identifies which skill combination was actually used for discovery.
Use the same chain from evidence to decision when promoting subsequent skills.

## Promoting a skill

Use one PR per adopted skill. Put its protocol, runnable cases, assessment rules and adoption results under `tests/skills/<skill>/` and install the exact tested bytes under `skills/<skill>/`.
Use the existing manifest, attempt index and assessment to identify the candidate digest, case set, runner revision, provider settings, results and evidence inventories.
Include every attempt and the bounds of the comparison. Where the broader suite used a different text, identify that text.
Keep reserved inputs and raw private transcripts in the controlled evidence store. Record a durable locator, hash and retrieval instructions for authorized reviewers.
Verify the installed bytes, evidence references and offline checks in a clean checkout before merging.

The maintained runner lives under `tests/runner/`. The historical path `skill-validation/runner/` points to that same implementation for existing shell commands.
Read historical scores with the criteria and runner revision recorded at collection. The [legacy validation records](../skill-validation/README.md) retain those identities.
