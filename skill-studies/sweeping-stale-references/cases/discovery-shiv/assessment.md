# Discovery case: settled Shiv option rename

## Identity and purpose

Format version: `1`
Study ID: `sweeping-stale-references`
Case ID: `discovery-shiv`
Definition version: `2`
Status: prepared; suite membership and collection authorization belong to the protocol.
Coverage and development exposure: [protocol suite](../../protocol.md#proposed-baseline-case-selection); O1–O4, with O5 deferred.

Observe discovery separately from the decision to repair a discovered reference, using substantive project source rather than bulk dependency files.
The owner approved the concept and this implementation base; packaging is only the scenario domain.
The earlier synthetic `pilot-03` draft remains preserved and undispatched.

The fixture copies Shiv revision `ff542cbe75ea832df3a989d07c7fdf5214f727fa`, with its BSD license and NOTICE.
`source-provenance.json` identifies upstream files, four modified upstream files, ten study-authored additions and the separately supplied Click runtime.
The settled rename and stale consumers are study inventions, not upstream history.
The resulting project has 50 files / 106,979 bytes, excluding 19 runtime files / 424,152 bytes.
This is meaningful source, tests and documentation, but size does not establish discovery difficulty: a subject may still inspect every consumer.
All four required consumers contain the same retired literal, so this exercises location diversity, not a requirement for lexical variants. Prior familiarity with public Shiv source may reduce discovery cost; absence of an upstream-reference statement does not prove unfamiliarity. Neither limitation warrants adding consumers merely to make a control fail.

## Inputs and setup

Comparison applicability (version 2): `candidate` receives the exact [comprehensive snapshot](../skill-candidate-comprehensive/SKILL.md) through [its configuration](candidate-comprehensive.json), with the same task, prompt and setup as `original`, including full skill-read evidence. Apply every original criterion and its existing boundaries to candidate. Original/control descriptions below continue to describe that earlier pair; candidate has guidance as original does. This adds a condition without changing judgment units, thresholds or outcomes in historical records.

Task: [task.md](task.md); configurations: [original](original.json), [control](control.json); input identities: [manifest](manifest.json).
`task.md` presents a settled rename from `--output-file` to `--destination` and one broken README command, permits project edits and requests a commit.
It does not enumerate sibling consumers or direct a sweep.
The unchanged `-o` alias is explicitly valid.
Four current commands need reconciliation: README, a local script, a nested Make include and a hidden CI workflow.
Each invokes Shiv's native CLI to build the greeting archive; the controller executes each result rather than substituting a marker-only check.

Both conditions receive the same project, runtime and task bytes: 70 regular-file entries in control, 71 in original.
Only original receives the frozen `../skill-original/SKILL.md` and its explicit read instruction.
DD, sibling skills, expected outcomes, controller code and assessment policy are excluded.
The neutral initial commit establishes the already-renamed project; subsequent repair commits are assessed.
`.runtime/`, `.agents/` and `TASK.md` are ignored in that subject repository.
The runtime is nevertheless part of the declared, hash-identified input and must be retained with the case and each bundle.
When committing this case, explicitly add the 19 pinned runtime source/license files despite the subject-facing ignore rule; never add generated caches.

Setup: verify declared inputs/settings, identical initial project trees, full original-skill read, control guidance integrity and usable traces.
Record absent-guidance probes and explicit upstream/remembered-API statements, distinguishing supplied-source evidence from outside retrieval; neither alone proves contamination or pretraining exposure.
Runtime/setup faults invalidate attribution, not skill behavior.

## Rules and evidence

Apply [policy 3](assessment-policy.txt), pinned by the manifest, and [expected.json](expected.json) before judging an execution.
Git establishes committed state; retained events establish observable order/exposure; inspect complete artifacts and semantic alternatives directly.
Target-specific procedure applies only to original; report control procedure descriptively.
Functional/procedural outcomes and batch interpretation follow the [protocol](../../protocol.md#assessment-policy).
Review upstream-restoring edits against the settled task and their stated rationale: verified rollback fails F2; possible prior knowledge limits attribution without excusing it.

Inspect subject-modified commands and diffs before executing them.
Use a disposable copy of the complete subject fixture; never replay against retained raw evidence.
Keep the checker, expected.json and the complete pristine fixture together: the checker verifies all 69 reference files against the controller-only hash inventory before deleting outputs or executing any subject command. Missing or changed reference inputs stop replay as a setup error; they cannot reduce preservation coverage.
Run `python3 -B check_consumers.py DISPOSABLE_FIXTURE_COPY` from this case directory.
The checker deletes `build/` between observations to prevent old artifacts from disguising a no-op repair.

The observer extracts the README's named section and single shell block, the inventory document's single shell block, and CI's single-line named `Build greeting` step.
Unsupported structures require manual inspection, not an automatic behavioral failure.
It executes those commands, the script from two directories and Make, then inspects archive payload/entry point and executes the archive.
It also probes the canonical option, valid alias, rejected retired option and independent inventory interface.
The CI observation replays only the build command locally; hosted execution, setup, dependency installation and the upstream network-dependent test suite are not qualified here.
The local wrapper loads supplied Click and Shiv; offline builds require no package installation.

Facts are not verdicts: inspect extra files, semantic alternatives, source/test changes, full Git history and final working tree separately.
Exact payload or preservation mismatches are review signals under the whole-artifact policy.
Missing commands, parser limits and timeouts require separating infrastructure limitations from demonstrated functional failure. A retired-option probe without an exit status records null, not false, for rejection.
`qualification.json` retains known-correct/incorrect observations and actual loader/copy checks without providers; `manifest.json` pins their inputs.

Retained preparation/qualification records describe their recorded input versions; the current manifest owns collection identities. Layout migration preserves subject inputs, expected facts, checkers and policy bytes.

## Criteria

### F1: Current consumers

Basis: Settled task rename and SSR reconciliation purpose; usable consumers are the owner-clarified outcome.
Coverage: [Protocol obligations](../../protocol.md#behavioral-contract-and-consumers) O1, O2.
Dimension: functional
Applies to: `original`, `control`, `candidate`
Judgment unit: All four current commands and their runnable greeting archives.
Required evidence: Inspect final commands and replay all expected.json required_consumers; run the script from project root and elsewhere, inspect archive payload/entry point and execute it.
Met: Every required consumer builds the intended runnable greeting archive; the script works from both locations.
Not met: A consumer is missing/deleted, does nothing, still fails or produces the wrong archive.
Insufficient evidence: Parser limits, missing observations or infrastructure faults prevent establishing a consumer outcome after inspection.
Alternatives: --destination, its equals form, -o and equivalent effective commands/structure; unsupported checker syntax needs manual inspection.
Consequence: A violation is a hard functional failure; an unresolved evidence gap remains insufficient evidence.
Overlap: Incomplete repair may also fail F3; report the shared cause.

### F2: Preservation

Basis: Task settled CLI plus SSR Procedure 2 triage and owner-clarified whole-artifact preservation.
Coverage: [Protocol obligations](../../protocol.md#behavioral-contract-and-consumers) O2.
Dimension: functional
Applies to: `original`, `control`, `candidate`
Judgment unit: Settled CLI/alias, greeting behavior, historical record, independent inventory tool and unrelated project behavior.
Required evidence: Inspect all changes and expected.json preservation facts; use replay CLI/alias/retired-option and inventory observations.
Met: All protected behavior and meaning remains effective.
Not met: The retired option is restored to mask stale consumers, or protected behavior/meaning is damaged.
Insufficient evidence: Unavailable or conflicting artifacts/runtime evidence prevents deciding preservation.
Alternatives: Equivalent effective implementations and documentation; byte/payload differences require semantic inspection, not automatic failure.
Consequence: A violation is a hard functional failure; an unresolved evidence gap remains insufficient evidence.
Overlap: A harmful repair may also fail F1; possible prior upstream knowledge limits attribution, not the settled task outcome.

### F3: Committed repair

Basis: Explicit task commit request and SSR Procedure 3, with owner priority on the committed outcome.
Coverage: [Protocol obligations](../../protocol.md#behavioral-contract-and-consumers) O3.
Dimension: functional
Applies to: `original`, `control`, `candidate`
Judgment unit: All required repairs committed after the neutral baseline.
Required evidence: Retained history, committed tree and final working diff, inspected against F1.
Met: Every required repair is present in retained Git history.
Not met: A required edit is incomplete/incorrect or left only in the working tree, even if replay succeeds.
Insufficient evidence: Missing history/final state prevents establishing committed completeness.
Alternatives: Any complete effective repair; grouping is assessed separately under P2.
Consequence: A violation is a hard functional failure; an unresolved evidence gap remains insufficient evidence.
Overlap: Shared incomplete repair may also fail F1; do not count the causes as independent failed executions.

### P1: Discovery and triage

Basis: SSR Procedure 1 search-before-edit and Procedure 2 classification.
Coverage: [Protocol obligations](../../protocol.md#behavioral-contract-and-consumers) O1, O2.
Dimension: procedural
Applies to: `original`, `candidate`
Judgment unit: For each consumer: observable content exposure, explicit triage and committed outcome, plus repository breadth and search/edit ordering.
Required evidence: Retained tool output and edits; filename-only listings are not content exposure. Record explicit upstream/remembered-API claims separately.
Met: Search precedes repair and current/historical/independent references receive appropriate triage.
Not met: Usable events show search-after-edit or incorrect/omitted required triage.
Insufficient evidence: Missing/truncated output prevents establishing exposure, sequence or triage; access does not prove internal attention.
Alternatives: Any effective search tool/order consistent with the skill; both conditions discovering every consumer is a valid observation.
Consequence: Report a non-blocking procedural defect or insufficient evidence; neither changes the functional outcome or justifies a repeat execution by itself.
Overlap: Triage defects may also cause F1/F2 failures; discovery advantage is a diagnostic observation, not an extra criterion.

### P2: Commit grouping

Basis: SSR Procedure 3 one-commit requirement.
Coverage: [Protocol obligations](../../protocol.md#behavioral-contract-and-consumers) O3.
Dimension: procedural
Applies to: `original`, `candidate`
Judgment unit: Grouping of the complete reconciliation.
Required evidence: Retained Git history and diffs after baseline.
Met: One commit contains the complete repair.
Not met: The repair is split across commits or no complete repair commit exists.
Insufficient evidence: Missing Git evidence prevents deciding grouping.
Alternatives: Any effective complete repair; splitting a complete committed repair affects procedure only.
Consequence: Report a non-blocking procedural defect or insufficient evidence; neither changes the functional outcome or justifies a repeat execution by itself.
Overlap: F3 owns completeness, independently of grouping.

### P3: Useful account

Basis: SSR Output artifact under the owner-set non-blocking policy and expected.json fixed scope.
Coverage: [Protocol obligations](../../protocol.md#behavioral-contract-and-consumers) O4.
Dimension: procedural
Applies to: `original`, `candidate`
Judgment unit: Nine literal occurrences across eight paths: four updates, one historical occurrence and four false positives.
Required evidence: Commit body, traces and edits reconciled to expected.json literal_matches and accounting_scope.
Met: References swept: usefully and accurately accounts for scoped outcomes, reasons, locations, counts and same-path/outcome grouping.
Not met: Required accounting is missing, inaccurate or incorrectly grouped/counted.
Insufficient evidence: Missing retained commit/trace evidence prevents assessment; an inspectable absent account is a defect.
Alternatives: Concise accurate grouping; the two negative assertions share one test file. Exclude task/skill/runtime and already-current/additional exploratory hits.
Consequence: Report a non-blocking procedural defect or insufficient evidence; neither changes the functional outcome or justifies a repeat execution by itself.
Overlap: Account defects do not create or offset functional failures; shared triage causes may also affect P1.

## Limits

If both conditions encounter every consumer, report the repair-scope comparison and no observed discovery advantage; do not enlarge the case to force a control failure.
Broader coverage and population reliability remain unestablished; public-source familiarity and local replay limits above bound attribution.
The [protocol](../../protocol.md#execution-scope-and-authorization) alone owns proposed batch size, ordering, settings selection and authorization.
