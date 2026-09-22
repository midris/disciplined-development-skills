# Runner input-isolation correction

Scope: the owner-approved filesystem boundary for Codex and Claude, the runner guide, SSR resumption and combined accounting.
Method: active-session adversarial review against the current framework, plan, emitted policies and installed-runtime evidence; not independent review.
No subject, evaluator, authoring or retry calls were made.

## Correction and evidence

The prior fix controlled ambient guidance and writes, but allowed general filesystem reads.
The new shared acceptance test first failed for both providers in both permission modes on a sibling controller file.
The final boundary grants declared fixture/evidence inputs, private scratch and specified runtime/authentication dependencies.
It blocks reads and writes to surrogate controller records, sibling runs, ordinary home files, Claude settings, unrelated keychain-directory files, and shared-temp files through `/tmp`, `/private/tmp`, `/var/tmp`, `/private/var/tmp` and symlink paths.
A `cd /tmp` followed by a recursive search cannot return those marker contents.
Both modes can use private scratch; writable mode can edit and commit; read-only mode rejects overwrite, delete, rename, creation and Git mutations.
Codex retains its protected-directory exclusions and network-bind denial.

Codex 0.154.0's [platform-default implementation](https://github.com/openai/codex/blob/rust-v0.154.0/codex-rs/sandboxing/src/seatbelt.rs) explicitly opens shared temporary trees for process sandboxes.
Testing confirmed ordinary root/temp denies were insufficient; explicit deny globs override those allowances.
Declared Codex roots must therefore be outside those trees, with preparation rejecting unsafe roots before a model invocation.
Inherited templates and the conflicting special TMPDIR deny were replaced with explicit path grants; subject shells receive only the restricted PATH and private TMPDIR.

Claude's whole-process Seatbelt wrapper covers native file tools and shell descendants.
Installed Git needed Xcode runtime reads and its exact license-state plist; system Python and tools use the declared installation roots.
Claude 2.1.278 real subscription preflight initially failed and then passed with an exact read grant for `~/Library/Keychains/login.keychain-db`.
A preferences-only grant did not fix authentication, and no whole `~/.claude` directory/subtree grant was added.
Authentication output remained in memory; no credentials were copied or retained.
Git may print a denied shared xcrun-cache warning but still succeeds; shared-cache writes remain blocked.

[Qualification index](../skill-studies/sweeping-stale-references/input-isolation-qualification.json) identifies the exact source hashes, four initial failing probes, seven passing probes and the verified external inventory (438 entries).
Raw evidence uses the existing same-host study store; this does not establish a new backup arrangement.
These are local enforcement and authentication checks, not another model/tool round trip or exhaustive host isolation proof.
Runtime installation roots and exact authentication files remain deliberate read exceptions; Claude's model-network access remains available.
The first authorized amended observation must still be inspected before continuing.

## Review findings addressed

- The documented Codex minimal profile did not close shared-temp reads. Tested deny globs and pre-invocation path rejection address the entire shared-temp/alias class.
- The scratch deny conflicted with the required private allowance. Removing inherited templates and using explicit grants made both permission modes pass the scratch checks without broad temp access.
- Existing probes and dummy providers relied on undeclared controller files and a home-installed Python. Test inputs now travel through argv, executable content or declared fixture/evidence paths and use installed system tooling; production permissions were not expanded for test harness files.
- The old resumption command used the now-denied namespace. The protocol amendment supplies the per-user namespace, preserves historical commands and input pins, and requires the amended runner's committed invocation authority.

The final review traced both permission modes, setup rejection, scratch and symlink behavior, authentication, capture/cleanup, historical input preservation and resumption instructions.
No further blocking finding remains identified.

## Verification

- Runner: 458 passed.
- Installed-policy acceptance: seven passed (four shared isolation, two read-only, one Codex Git/network), zero model calls.
- Real Claude subscription preflight: passed; private runtime cleanup succeeded.
- Hooks: 263 passed, three existing environment skips.
- Qualification source hashes and external inventory verified.
- SSR protocol and completed/partial batch assessment readiness checked; frozen manifests and existing result records unchanged.
- `git diff --check` passed.

The runtime finding in the earlier expansion checkpoint is resolved for future attempts by `input-isolation-1`.
Orders 1–2 remain as recorded; orders 3–10 remain unrun and must use the committed amendment as a distinct runtime stratum.

DD-VERDICT: PASS
