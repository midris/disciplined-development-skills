# Extension qualification disposition

Provider-free gates: PASS after review of retained diagnostics, with the qualifications below.
Input freeze: `f39d72102b72d3bea9fdcd5a3f9c92c50c14f67c`; provider: Codex / gpt-5.6-sol / low.
No real credentials or model calls were used; private login-status checks used only a dummy file-cache key under verified network denial.

## Evidence and exact commands

Working directory for all commands: `/Users/simon/work/personal/disciplined-development-skills/.worktrees/skilltest-input-isolation-spike`.
`/opt/homebrew/bin/python3 /private/tmp/skilltest-sol-low-pilot.Lunoau/extension.xWS8Q2/check-local-controls.py` exited 0; its per-command argv/cwd/status, version/digest/help and loopback positive/denied outputs are retained in this directory.
The CLI remains `codex-cli 0.153.4`; version and executable-digest bytes match the original fixed preflight captures.
The deny-network policy matches the original policy; host loopback bind succeeded and the same operation under the policy was denied.

The final catalog command was:

```sh
/usr/bin/sandbox-exec -f /private/tmp/skilltest-sol-low-pilot.Lunoau/extension.xWS8Q2/no-network.sb /usr/bin/env PATH=/opt/homebrew/bin:/usr/bin:/bin:/usr/sbin:/sbin /Users/simon/work/personal/disciplined-development-skills/.worktrees/skilltest-input-isolation-spike/skill-validation/runner/.venv/bin/python /private/tmp/skilltest-sol-low-pilot.Lunoau/extension.xWS8Q2/audit-native-catalog-v3.py > /private/tmp/skilltest-sol-low-pilot.Lunoau/extension.xWS8Q2/preflight/catalog-audit-v3-stdout.txt 2> /private/tmp/skilltest-sol-low-pilot.Lunoau/extension.xWS8Q2/preflight/catalog-audit-v3-stderr.txt
```

It exited 1 at the strict historical-date comparison, not a catalog/read/cleanup failure; do not relabel that command as exit 0.
[catalog-v3/catalog-audit.json](catalog-v3/catalog-audit.json) and [catalog comparison](catalog-v3/catalog-comparison.json) establish seven no-DD entries, sixteen current-DD entries, exactly nine DD additions, matching common content and matching 60-file bootstrap maps.
The new common entry is requesting-code-review; the other six entries match the retained original catalog.
Every supplied skill path resolves through the CLI's root aliases to the expected native fixture path.
Both sides' shell probes read all 10/19 supplied AR task/dependency files using the previously observed `/bin/zsh -lc` wrapper and `/bin/cat`; inputs remained unchanged and evidence directories empty.
Both private runtimes were removed with successful cleanup records and independently checked absent paths.

The historical comparison's only further difference is `<current_date>2026-09-06</current_date>` versus `<current_date>2026-09-07</current_date>` in one environment-content element.
A read-only structural comparison verified that replacing exactly that single element accounts for the entire remaining difference; the original and extension-normalized records are retained unchanged.
Both extension arms see September 7. The new tasks use fixed supplied facts, not relative-to-today requirements; this date change does not alter the exercised discovery/read mechanism.
Record dates as common incidental context, not hidden normalization or evidence that historical and new observations are identical inputs.

## Retained audit defects

The first scratch audit expected absolute catalog paths, while the CLI emits aliased paths; the first correction had an overescaped path regex.
Both scripts, command stdout/stderr, catalogs and cleanup records remain retained under the original preflight location and `catalog-v2/`.
Their invocation form was the final command above with `audit-native-catalog.py` / `audit-native-catalog-v2.py` and the matching `catalog-audit-stdout/stderr.txt` / `catalog-audit-v2-stdout/stderr.txt` captures; both exited 1.
Before the final diagnostic, the corrected parser was tested offline against retained aliases, an intentionally wrong root, and absolute paths.
These are orchestrator audit errors, not skill failures or provider INFRA_RETRY attempts; all four disposable runtimes across the diagnostics were cleaned up.

## Reuse decision

| Control | Disposition |
|---|---|
| Competing user skill | Reuse original surrogate positive/negative evidence and prior reconciliation: same private profiles, no copied user skills, same native roots. Fresh catalogs show only intended additions. |
| Global instructions | Reuse: runtime source is byte-unchanged, and private profiles copy only file-cache authentication, not global instruction files. |
| Config instructions | Reuse: same fixed flags/environment, unchanged executable digest and adapter; no copied host configuration. Debug remains narrower than exec. |
| Parent ancestry | Reuse: runtime establishes the same fresh Git boundary in the fixture root. New task directories contain no instruction/discovery files. |
| Native catalog/common inputs | Rechecked for the changed shared review dependency: paired content and all bootstrap hashes match; the date change versus old qualification is explicitly dispositioned above. |
| Real loading/read/write mechanism | Reuse the retained q-no-dd and q-current-dd real qualification: same runner production source, CLI/digest, cwd, permissions and native local-file mechanism. The extension adds ordinary Markdown/Python/JSON input files, not a new tool or execution path. |

`git diff --exit-code 0a22a44701032d5d3c367ea9c84f13bfc5202e62 HEAD -- skill-validation/runner/src` returned 0 with no differences.
The original actual-run read/cleanup evidence is in the parent package's `attempts/q-no-dd/result.md` and `attempts/q-current-dd/result.md`; their old pending-run statements are historical, not current authority.
No additional paid qualification call is required for this extension under this scope.
Every observation still checks tied CLI provenance, copied inputs, requested full skill reads, observable violations and cleanup. Failure to follow an explicit loading directive is retained/scored as fidelity, not silently discarded.
Automatic shell-startup reads and hidden provider inputs remain the previously accepted observability limits; debug does not prove exec-only flags or universal filesystem isolation.
This is setup qualification, not a discoverability or effectiveness result. Project status and next approval remain in the active plan.
