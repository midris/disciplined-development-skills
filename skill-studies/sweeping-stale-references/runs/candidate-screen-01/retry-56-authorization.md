# Slot 56 retry authorization

On 2026-10-26 the owner stated: “I've re-authenticated Claude. Please continue the tests, and I approve one retry for failed slot 56.”
This authorizes exactly one additional invocation of global slot 56 (Claude invocation-verification, candidate, repetition 2), followed by the remaining 59 original subjects and ten previously approved output reviews under the existing stop rules.
The failed parent remains retained, invalid and charged to the subject pool; attempt 2 links to it and charges the retry pool if invocation starts.
No further retry, skill edit, top-up or adoption is authorized.
The combined ceiling remains 888 subjects / 68 evaluators / 4 authoring / 4 retries; the SSR subset now has one retry allocated within that existing combined ceiling.

Subject configuration, manifests, criteria, runtime identities and original invocation authority remain exactly `eb1761bb7014034a174877d548898417ac4d2030`.
Production Claude authentication was verified after the owner's re-authentication; all frozen executable hashes match.
Retry and later attempts still require unchanged input/runtime checks and complete retention, inspection and active-session scoring before the next invocation.

The runner's retention command and batch membership checker only represent initial attempts.
Use its unchanged full capture/inventory/publication checks against a private initial-attempt projection, then register the verified new retry with attempt number 2, the original parent ID, this committed authorization and allocation pool `retry` in the full Claude index.
For later initial attempts, retain against the initial-only projection and append only the newly verified row to the full index.
Check that the full index has not changed during this operation, and validate its typed retry links and evidence identities after registration.
The projection is a retention adapter, not evidence exclusion: the full index is authoritative and preserves both attempts.
Batch aggregate checks that reject retries remain explicitly unsupported; a manual full-index audit must check scope, charges and inclusion.
Use distinct retry claim/outcome/inspection/result identities so no original evidence is overwritten.
