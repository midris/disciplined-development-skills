# dr-01 prelaunch

Input revision: e537c03909eb2b4f1986e4170a3f1b662d29a719.
Approval: ../../observation-approval-request.md; explicit owner approval of all four commands.
Working directory: /Users/simon/work/personal/disciplined-development-skills/.worktrees/skilltest-input-isolation-spike.
All checks passed; fresh CLI captures match the fixed qualification references.

```json
[
  {
    "cmd": "mkdir /private/tmp/skilltest-sol-low-pilot.Lunoau/attempts/dr-01",
    "chunk_id": "d3d15b",
    "wall_time_seconds": 0.000003041,
    "exit_code": 0,
    "original_token_count": 0,
    "output": ""
  },
  {
    "cmd": "git diff --exit-code e537c03909eb2b4f1986e4170a3f1b662d29a719 -- skill-validation/pilot skill-validation/runner",
    "chunk_id": "42d5a3",
    "wall_time_seconds": 0.00000225,
    "exit_code": 0,
    "original_token_count": 0,
    "output": ""
  },
  {
    "cmd": "git status --porcelain",
    "chunk_id": "68df0c",
    "wall_time_seconds": 0.000002333,
    "exit_code": 0,
    "original_token_count": 0,
    "output": ""
  },
  {
    "cmd": "/opt/homebrew/bin/codex --version > /private/tmp/skilltest-sol-low-pilot.Lunoau/attempts/dr-01/cli-version.txt 2> /private/tmp/skilltest-sol-low-pilot.Lunoau/attempts/dr-01/version-stderr.txt",
    "chunk_id": "4b867f",
    "wall_time_seconds": 0.000002291,
    "exit_code": 0,
    "original_token_count": 0,
    "output": ""
  },
  {
    "cmd": "/usr/bin/shasum -a 256 /opt/homebrew/bin/codex > /private/tmp/skilltest-sol-low-pilot.Lunoau/attempts/dr-01/cli-sha256.txt",
    "chunk_id": "80789a",
    "wall_time_seconds": 0.289090125,
    "exit_code": 0,
    "original_token_count": 0,
    "output": ""
  },
  {
    "cmd": "test -s /private/tmp/skilltest-sol-low-pilot.Lunoau/preflight/cli-version.txt && test -s /private/tmp/skilltest-sol-low-pilot.Lunoau/preflight/cli-sha256.txt",
    "chunk_id": "3494b3",
    "wall_time_seconds": 0.00000225,
    "exit_code": 0,
    "original_token_count": 0,
    "output": ""
  },
  {
    "cmd": "cmp /private/tmp/skilltest-sol-low-pilot.Lunoau/preflight/cli-version.txt /private/tmp/skilltest-sol-low-pilot.Lunoau/attempts/dr-01/cli-version.txt",
    "chunk_id": "c08a03",
    "wall_time_seconds": 0.000002292,
    "exit_code": 0,
    "original_token_count": 0,
    "output": ""
  },
  {
    "cmd": "cmp /private/tmp/skilltest-sol-low-pilot.Lunoau/preflight/cli-sha256.txt /private/tmp/skilltest-sol-low-pilot.Lunoau/attempts/dr-01/cli-sha256.txt",
    "chunk_id": "59d42f",
    "wall_time_seconds": 0.000002416,
    "exit_code": 0,
    "original_token_count": 0,
    "output": ""
  }
]
```
