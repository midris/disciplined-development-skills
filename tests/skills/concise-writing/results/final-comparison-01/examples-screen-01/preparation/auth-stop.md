# Claude authentication stop

The first Claude subject, original-examples repetition 1, stopped at the first server request with `401 OAuth access token has expired`.
Run: `20261023T010814494Z-cw-examples-claude-long-handoff-original-examples-fbc3683d-9f8e-464e-9e06-74202c743f96-w7a2hzdu`.
The complete bundle and matching inventory are retained in the [attempt index](../claude-final-examples-screen-01-run-index.json), with a structured invalid-setup result.
The server reports zero API inference time/usage; the source report remains byte-identical and no final artifact exists.
One subject session is charged because invocation started; this is not a behavioral skill failure and is excluded from functional rates.
The local auth-status command had reported loggedIn=true, while the thirteen zero-model qualification probes deliberately use a scripted endpoint and surrogate credentials; neither established current server acceptance of the real subscription token.

All six Codex subjects are retained, fully read and directly assessed before this stop.
Five planned subject sessions and both reviewer sessions remain unused; no Opus call has started.
The failed receipt remains uncleared and the existing collector rejects a duplicate slot, so no later subject or replacement can dispatch automatically.
To produce the six planned Claude outputs, restore sign-in through `claude auth login` and accept one unchanged replacement from the unused retry pool.
A replacement would preserve the failure and subject charge, add one retry charge (2/4 to3/4), retain the exact frozen config/skill/source/task/criteria, and require a committed resumption record before dispatch.
The request grants no new subject/evaluator capacity, automatic additional retry, fallback model or live adoption.
The [protocol](../../../../protocol.md) owns the current recovery decision and authority.
