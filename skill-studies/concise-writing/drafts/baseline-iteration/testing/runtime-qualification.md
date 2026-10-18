# E iteration runtime and collection controls

Qualification date: 2026-10-18.
Authority and progress belong to the [protocol](../../../protocol.md).
The [machine-readable identities](runtime-identities.json) pin binaries and the retained qualification inventory.
No model inference was used in qualification; exact production availability is checked by each model's first scheduled charged attempt, without fallback.

## Qualified setup

Subjects use Codex 0.163.0 / gpt-5.6-sol low and Claude Code 2.1.301 / claude-sonnet-5 low, workspace-write, 900-second timeout.
The Codex controller assesses outcomes; Opus claude-opus-5-5 medium supplies the cross-family output review.
Actual CLI requests against a local scripted endpoint verify that exact evaluator ID and medium effort, native Read delivery, no Skill/Bash/Write/Edit tools and no exposed skills.
A scripted response proves transport and argument handling, not production model availability or automatic selection.
New runtime strata are kept separate from the previous 0.157.1/2.1.283 subject batches.

Homebrew Python 3.14.8 and Git 2.56.0 are installed, but the global python3 shortcut is absent.
The controller-only [runtime setup](runtime_setup.py) places symlinks to those existing binaries inside each invocation's already granted private scratch and prepends that directory to its prepared PATH/login profile.
Both providers use this same fixed setup in all four conditions.
It supplies no subject instruction, source document or skill and changes neither production runner code nor filesystem read grants.
No host installation, global shortcut or sandbox widening is performed.
The adapter logs actual tool paths and hashes in each bundle; the controller checks frozen identities before each invocation.
Private runtime scratch is invocation-owned and removed through the existing runtime cleanup.

Twelve checks passed under the prepared setup: four actual login-shell/Claude-CLI checks across both permission modes, four input-isolation checks, two read-only mutation checks, one Codex Git/network check and one exact Opus native-reader transport check.
These exercise controller/sibling/home/shared-temp/symlink isolation and protected-file writes as well as shell interpreter/Git resolution, heredocs and warning-free host Git defaults.
The earlier shared temporary toolchain attempt is retained: Claude passed, but Codex correctly denied traversal and selected Apple tools.
Moving the links into already permitted invocation scratch resolves that attempt without weakening its deny rule.
No production model was called by either attempt.
A final combined command passed eleven runtime checks but could not start the Opus check because its evidence directory name collided with Claude’s generic check.
The Opus check then passed in a separate fresh directory; both records remain retained, with zero model calls.

## Freeze and dispatch

Use the [ordered schedule](schedule.json): twenty Codex attempts then twenty Claude attempts, five repetitions per condition, with the declared cyclic rotations and residual imbalance.
Run sequentially: verify and register each stopped bundle and charge before dispatching the next slot.
The [E card](assessment.md) changes only applicability/setup metadata and links from the preserved E definition; criterion semantics remain unchanged.
Configs supply exactly the existing report, task, new notes and condition-specific prompt; skill-bearing conditions additionally receive their complete assigned CW body.
The no-CW control receives no CW body or descriptor; do not supply criteria, comparison labels, this adapter or prior results as subject guidance.
Require complete skill exposure before the first task edit for explicit-load arms; inspect the trace rather than trusting the completion claim.
Inspect captured guidance and actual model/effort before advancing, and stop on unexpected ambient guidance or identity, setup/capture failure, drift or uncertain charge.
A valid behavioral miss remains included and does not stop collection.

Retain raw bundles and inventories under `/Users/simon/work/personal/skill-study-private/concise-writing/e-iteration-20261018/` using the owner-accepted single-host arrangement.
Never run Git inside retained bundles; read files or use disposable copies.
Forty subjects and two Opus reviews are allocated; retries, replacement attempts, further wording rounds and full-suite collection are not automatically funded.
The controller must record every attempt, including pre-invocation failures charged zero and uncertain charges that stop dispatch.
The proposal's fixed post-E rules govern the next owner decision; no between-repetition changes or automatic authoring.
