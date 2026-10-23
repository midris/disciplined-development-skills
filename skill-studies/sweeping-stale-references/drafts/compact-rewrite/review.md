# Compact SSR rewrites: static comparison

Status: active-author review of three untested drafts against both preserved base versions.
The [design](../../../../plans/specs/2026-10-23-ssr-compact-rewrite.md) records the owner's scope and drafting-before-testing instruction.
The original, comprehensive version, parked context/accounting draft and all historical evidence remain unchanged.
These judgments concern contract coverage and readability on inspection; none establishes model effectiveness.

## Five-version comparison

| Version | Complete words | What it contributes | Limitation relevant to this rewrite |
| --- | ---: | --- | --- |
| [Baseline](../../cases/skill-original/SKILL.md) | 1,182 | Concrete reference surfaces, a worked inventory and ten distinct rationalization rows | Repeats the procedure in overview, quick reference, scope and output sections; does not explicitly teach new-form search, contextual comparison or an already-current outcome |
| [Comprehensive](../../cases/skill-candidate-comprehensive/SKILL.md) | 923 | Clear Search/Triage/Reconcile stages; old/new search, attached-rationale preservation, honest proposal/verification limits | Eight rationalization rows merge original distinctions; already-current references have no explicit disposition; contextual inspection and local reporting still admit observed errors |
| [Draft 1: procedure](01-procedure/SKILL.md) | 842 | Familiar stages, readable outcome list, separate commit account; conditional context reading and explicit locality | Vendor triage is repeated; verification truthfulness appears both under Reconcile and in the template; some sentences retain parallel synonyms that can be tightened |
| [Draft 2: outcome-first](02-outcome-first/SKILL.md) | 811 | Useful end-state framing and compact disposition table | Reconciliation, rationale preservation and post-edit checks sit under the disposition heading, making the action sequence less visible; the table duplicates the template's label structure |
| [Draft 3: checklist](03-checklist/SKILL.md) | 758 | Clear before-edit/before-commit timing and least surrounding prose | Four dispositions share one long bullet; commitment, placement, grouping, counts and encoding requirements share another. The saved words increase scanning/reconstruction burden |

All three new drafts retain the baseline's 303-word rationalization table verbatim, rather than the comprehensive version's 184-word table.
Their surrounding guidance therefore compresses more than the whole-file differences alone suggest.
No word-count target determines selection.

## Contract comparison

The draft columns refer to the complete procedure, outcome-first and checklist versions respectively; retained obligations were checked in each, rather than inferred from a shared template.

| Responsibility | Baseline | Comprehensive | Draft 1 | Draft 2 | Draft 3 |
| --- | --- | --- | --- | --- | --- |
| Name and trigger-only description | Source | Identical source | Identical | Identical | Identical |
| Search beyond reviewer citation before editing; code/docs/tests/config/scripts/CI/build | Explicit | Explicit | Search | Find consumers | Before editing |
| Old/new search, synonyms, variants and existing new-form uses/collisions | Old and synonyms; no explicit new-form pass | Explicit old/new pass | Search | Find consumers | Before editing |
| Inspect meaning, quantities, conditions and outcomes when snippets are insufficient | Owner-intended semantic outcome, no explicit reading step | Search specificity, no explicit full-claim comparison | Conditional full claim/block | Conditional full claim/block | Conditional full claim/block |
| Matching heading versus adjacent context | No explicit boundary | Generic headings excluded unless they encode the fact | Matching heading triaged | Matching heading triaged | Matching heading triaged |
| Update, preserve unrelated/historical material, include vendor/archive triage, exclude immutable history | Explicit | Explicit | Triage/scope | Dispositions/scope | Before editing |
| Genuine reference already expresses intended state | No explicit category | No explicit category | Explicit fourth outcome | Explicit fourth outcome | Explicit fourth outcome |
| Differently worded claims and relative links after a move | Owner-clarified outcome | Semantic search supports outcome; relative-link technique implicit | Explicit | Explicit | Explicit |
| Preserve distinct attached rationale and avoid inventing another match for it | Ownership reference; no comparable detailed rule | Explicit | Reconcile | Dispositions | Before committing |
| One reconciliation commit; post-edit searches before claiming verification in it | One commit; no explicit post-search timing | One commit and repeated search; observed timing misses remain | Explicit before commit | Explicit before commit | Explicit before commit |
| Every match accounted; precise locations/counts; same path/outcome only; audited old → new | Inventory rules; no explicit encoding requirement | Explicit | Commit account | Leave evidence | Before committing/template |
| Required negative form and accepted comprehensive all-match locality | Single-file/no-sweep; original scoring accepts preserved outside matches | All matches in changed file | Explicit, all four outcomes count | Explicit, all four outcomes count | Explicit, all four outcomes count |
| Group before exceeding body preference; retain necessary audit detail | Explicit | Explicit | Explicit | Explicit | Explicit |
| Truthful observed verification, read-only status and no invented branch-readiness verdict | No comparable standalone instructions | Explicit | Commit account | Leave evidence | Closing proposal rule |
| Initial grounding/rationale ownership and rationalization protections | Ownership + original ten rows | Ownership + compressed eight rows | Ownership + exact original ten | Ownership + exact original ten | Ownership + exact original ten |

The new drafts are whole-version alternatives, not pure compression of an identical behavioral contract.
They explicitly teach conditional contextual inspection, introduce `already current`, clarify matching headings/locality, state relative-link handling and deduplicate repeated search hits.
These address the owner-clarified outcomes and the [diagnosis](../../rewrite-diagnosis.md); their effectiveness and reporting consequences remain untested.
Do not apply the new category or counting language retrospectively to frozen scores.

## Selection and synthesis

Use Draft 1's visible Search/Triage/Reconcile sequence, retain its separate disposition bullets and commit account, and cut its duplicate scope/verification statements.
Use Draft 3's direct timing and Draft 2's concise outcome definitions, without putting reconciliation beneath triage or compressing several decisions into one checklist bullet.
Retain the complete original rationalization table unchanged.
Make tool independence explicit in the finalist: the retained table's emphatic grep wording should not remove the base versions' allowance for any effective search tool.
Use a conditional complete-claim read rather than the parked draft's unconditional full-block read.
Keep separate examples for positive and negative commit accounts so the mandatory literal negative form is easy to find.

This yields a synthesized [finalist](finalist/SKILL.md), rather than declaring the shortest draft the winner.
The finalist's full-source review checked every row above, then inspected the complete skill for lost context, contradictory boundaries, inflated obligations and needless duplication.
The output skeleton remains a contract aid, not a new fictional worked scenario; preserve the comprehensive version's choice to omit the longer aggregate worked example.

## Finalist review

The complete finalist is **814 words**, 109 fewer than comprehensive (11.8%) and 368 fewer than baseline (31.1%).
It restores all ten original rationalization rows, adding 119 table words relative to comprehensive, while reducing the surrounding material from 739 to 511 words (30.9%).
Its 56-word increase over the shortest draft buys separate dispositions, a visible commit-account section, an explicit negative-form example, tool independence and less slash-heavy prose.
These are static readability judgments, not evidence that an agent will perform better.

The final review found and resolved three clarity issues in synthesis:

- Require comparing each match's meaning with the settled fact even when its snippet is sufficient; only expansion to the complete claim/block is conditional. Otherwise the reading rule could leave the observed read-but-misunderstood failure untouched.
- State that any effective search tool is acceptable. The unchanged rationalization table's emphatic grep language must not silently narrow the procedural tool choice.
- Keep grounding/rationale ownership beside the opening purpose, and use ordinary conjunctions instead of compressing those distinctions into slashes. Their meaning should not be reconstructed from a footer or a dense bullet.

The complete-source comparison finds no remaining omitted responsibility in the matrix under the stated draft contract.
The accepted comprehensive locality boundary is explicit: preserved, unrelated and already-current outside-file matches all require the positive inventory.
The template includes the fourth outcome structurally, rather than relying on a prose reminder alone.
Expansion to the complete claim/block remains conditional on evidence sufficiency, avoiding a mandatory full-file/full-block read for each mechanical hit.
Post-edit search occurs before commit; truthful verification and read-only proposal status remain separately stated.
The original table is unchanged, including concrete references to tests, IDE renaming, documentation, config/CI/build consumers, TODO deferral and diff-size rationalizations.

Remaining uncertainties are empirical: whether the new category is applied correctly, whether context comparison prevents semantic misses, and whether the reading/accounting work remains proportionate on ordinary changes.
Those are future fixed-scenario questions; static inspection supplies no GREEN result or adoption authority.

## Remaining evidence

No model subject or evaluator has received these drafts.
The three drafts and finalist are exposed development artifacts, written and reviewed by the same active author.
Static preference for the finalist is not a cross-model review or a claim of improved task outcomes, native selection, low reading cost or reliable accounting.
Future tests should compare fixed relevant cases under declared conditions and the accepted output-review process.
The proposed eventual version comparison is baseline/comprehensive/finalist; it has no approved cases, counts, runtime or allocation yet and makes no unguided-contribution claim.
The earlier no-SSR/comprehensive/context-only diagnostic remains an alternative proposal, not a configuration for this finalist.

## Verification

Static checks verify all four files' complete frontmatter against both base versions, byte equality of all ten original rationalization rows, word counts, balanced fences and whitespace.
The shipped skill, frozen source snapshots, parked context/accounting draft and pre-existing CW fixture edit retain their prior bytes; no study configuration points to a compact draft.
All 603 checked local link targets resolve, combined effort accounting sums correctly, and the existing Opus batch assessment-readiness check remains complete.
The hook suite passes with 263 tests and three environment skips using the existing runner-venv Python from the hooks directory; `git diff --check` passes.
The active-author static review is logged through `log_review.py`; no external reviewer or subject was invoked.

No blocking findings remain in this bounded static review; behavioral validation is unperformed.

DD-VERDICT: PASS
