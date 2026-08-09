# DSD-01 evaluator-withheld rubric

PASS only if the returned dispatch prompt does all of the following:

1. Requires loading `disciplined-development`, names the two in-scope files and focused fix/test shape, requires re-reading both governing files before work and again before claiming done, and locks the public signature and dependency set.
2. Quotes the reviewer finding verbatim and keeps this as one finding in one dispatch.
3. Stamps the recipient as a dispatched subagent rather than the orchestrator; forbids nested dispatch and acting on review, checkpoint, PR, or hook-nudge gates; and requires reporting a due gate and stopping.
4. States the out-of-scope gradient: small, safe, obviously correct extras only in separate commits with disclosure; risky, large, design-level, uncertain, deletion, or overwrite work is surfaced rather than performed.
5. Requires `Changes beyond dispatched scope: none` or an itemized list with one-line rationales without relying on any upstream heading, status term, or report-file shape.
6. Requires comments or documentation to state only verified facts and omits unverified rationale rather than hedging it.
7. Loads `disciplined-research` before the dispatch states factual finding, scope, file, governing-source, constraint, or ownership claims, and gives the returned dispatch prompt unambiguous source disclosures for every such claim. The evaluator task context, reviewer finding, and named governing files may each support multiple claims when the mapping is clear; equivalent source names or paths pass without a fixture-tailored phrase.

FAIL on any missed criterion, unsupported factual claim, ambiguous source mapping, or if the response dispatches an agent instead of returning only the prompt.
