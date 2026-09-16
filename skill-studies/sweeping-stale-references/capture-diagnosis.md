# Codex command-output capture: diagnosis and repair

Status: diagnosis complete; owner approved the code change and review corrections on 2026-09-16. Session retention is implemented and verified offline; capture-2 governs resumed collection.
Affected collection: [core-baseline-01](protocol.md#core-baseline-core-baseline-01), paused after order 1. This investigation used zero model calls.

## Finding and evidence

Codex CLI 0.154.0 can omit early command output from its JSON command event while supplying that output in the model-facing tool response. A partial JSON event cannot establish that the model missed the text.
The tested executable matches the study hash, `4f85982624b3898c8991cb80c0981b2aa71070e3537046c9a95950318a95afcc`.

The provider-free reproduction uses a localhost server returning fixed tool calls, a fresh profile without credentials, and the frozen skill text as a known payload. Each command prints that payload and then a delayed marker; alternating commands also delay before the payload. No model generates any response.

| CLI mode | Immediate commands missing payload in JSON | Delayed commands with complete JSON | Complete model-facing outputs | Session outputs exactly matching model-facing outputs |
|---|---:|---:|---:|---:|
| Existing ephemeral mode | 4/4 | 4/4 | 8/8 | No session file |
| Session persistence enabled | 4/4 | 4/4 | 8/8 | 8/8 |

These are deterministic diagnostic commands, not study executions or estimates of the bug's population frequency. All commands exited successfully. The retained session file was 218,452 bytes in this diagnostic; real study evidence size remains to be measured.

The matching public source tag resolves to Git `6b9826e3aa83b1a5947db50f4332cb9c65f1b340`. The [process manager](https://github.com/openai/codex/blob/6b9826e3aa83b1a5947db50f4332cb9c65f1b340/codex-rs/core/src/unified_exec/process_manager.rs#L497) starts the process before subscribing to its output stream. [The subscriber](https://github.com/openai/codex/blob/6b9826e3aa83b1a5947db50f4332cb9c65f1b340/codex-rs/core/src/unified_exec/async_watcher.rs#L58) maintains a separate transcript; [output selection](https://github.com/openai/codex/blob/6b9826e3aa83b1a5947db50f4332cb9c65f1b340/codex-rs/core/src/unified_exec/async_watcher.rs#L457) falls back to the collected tool response only when that transcript is empty. If early bytes arrive before subscription and later bytes arrive after it, the nonempty partial transcript wins. The reproduction demonstrates this failure mode in the installed binary.
The study runner captures and publishes the CLI stdout bytes without filtering these events. Adding another stdout copy would retain the same omission.

[Official CLI documentation](https://learn.chatgpt.com/docs/non-interactive-mode#basic-usage) identifies `--ephemeral` as disabling persisted session rollouts. Removing that flag in the offline diagnostic retains the model-facing tool responses even though the JSON command events still lose their early output.

Retained diagnostic bundle: `/Users/simon/work/personal/skill-study-private/sweeping-stale-references/development/capture-diagnostic-20260916/`.
Inventory: `/Users/simon/work/personal/skill-study-private/sweeping-stale-references/development/capture-diagnostic-20260916.inventory.json`, SHA-256 `84f2885b406e59089c75e7dbb83877b8f5d8a357b5907c00ecb6af95b436c630`.
It contains the reproducer, both raw diagnostic streams and local request bodies, the persisted session, machine-readable checks and pinned source excerpts. Profiles/authentication files and the cloned source repository are excluded. These diagnostic observations do not enter the study attempt index or consume its call pools.

## Approved capture change

1. Run Codex with session persistence in the existing fresh private profile. Keep each invocation isolated and never resume a subject session.
2. Before private-profile cleanup, retain that invocation's session JSONL as `provider-session.jsonl` at the bundle root, alongside the existing stdout/stderr. Copy session evidence only; preserve it for unsuccessful attempts when available. Treat missing, ambiguous or uncopyable expected session evidence as an explicit capture error, retaining recovery information rather than claiming successful preservation.
3. Expose the additional file's identity in a versioned runner result record. Include it in the existing complete bundle inventory and cite its tool-response entries when JSON command output is incomplete. A session file does not automatically prove adequate evidence: inspect actual content and truncation under the existing criteria.
4. Verify capture before cleanup, error paths and unchanged isolation with offline tests. Record the revised runner/capture identity and exact invocation in the protocol before resuming the eleven approved executions. Keep the skill, task, criteria, model/effort, order, sample size and no-retry rule fixed.

The owner approved this change to frozen collection mechanics. The prospective [capture-2 amendment](protocol.md#session-evidence-amendment-capture-2) explicitly admits session tool responses and fixes identity, read-command, content and truncation checks before resumption. It adds evidence retention to the existing runner, not the later document generator/validator or a new assessment stage. No CLI upgrade or subject prompt workaround is required.

## Repair verification

The revised production adapter passed a credential-free localhost check: both scripted tool responses exactly matched the text supplied to the model, the session artifact survived, and the private profile was removed. This used zero model calls. Its eight-file, 291,355-byte evidence set is retained at `/Users/simon/work/personal/skill-study-private/sweeping-stale-references/development/session-capture-qualification-20260916/`; the sibling `.inventory.json` has SHA-256 `34273e261bcd88bea6464bfbf4374ba80691fa4c00b57e5725c2c4382968e833`. It includes the production-adapter probe and controller session-inspection scripts. The offline runner suite passes 306 tests, including successful/nonzero execution retention and missing, ambiguous, symlink and copy-failure cases.

## Effect on the stopped attempt

The bug explains how the observed omission can occur despite a complete model-facing read. It does not recover that particular invocation's tool response: it used ephemeral mode and its private profile was cleaned up.
Keep its canonical result unchanged: observable functional repair met, setup evidence unresolved, excluded from valid-setup aggregates. Its charged call remains spent; no replacement is authorized. The eleven unattempted executions can resume after the approved capture change is verified and its authority frozen. Record the capture-mode difference explicitly when assessing the batch.
