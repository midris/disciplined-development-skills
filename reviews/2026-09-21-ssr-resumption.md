# SSR expansion resumption review

Scope: approved orders 3–10, frozen source inputs and SSR policy 3; no skill edit or extra model calls.
Owner clarified after round-10 PASS that time is a guideline and asked to proceed; invocation ceiling remains 56.

## Runtime finding and correction

Order 3's retained stdout shows denied `/Users/simon/.gitconfig` access and failed heredoc creation, followed by successful subject workarounds and a correct committed one-line correction.
No outside guidance is observed. Input hashes and neutral baseline match; retain it as valid with runtime friction, not as a skill failure or an uncharged attempt.
Inspection found shell HOME was stripped by `inherit=none`; zsh inferred the user home. TMPDIR was forwarded, but zsh independently defaults TMPPREFIX to `/tmp/zsh`.
The fix forwards HOME and TMPPREFIX into the already-granted private scratch. Permissions are unchanged.

The new no-model installed-policy regression failed on both login and non-login shells before the fix. Both pass after it; four existing two-provider isolation probes also pass. The documented `uv run pytest -q` command passes 458 tests.
Raw red/green qualification commands and results are retained under `/private/tmp/ssr-shell-qualification` pending durable retention at closure.
The test runs the actual generated permission policy and explicitly applies the generated shell environment; the sandbox subcommand itself does not emulate the model shell tool's environment construction.
An Apple Git selected by the system login profile can emit denied optional xcrun-cache warnings while completing all Git operations. The test requires successful commits and heredocs, not silence; it does not widen access to that shared cache.

Review: filesystem grants, auth handling, frozen task inputs and scoring are unchanged. The added shell variables address the two observed failures. No additional provider qualification call was made.
