# Resolve a catalog proof review

## Identity and purpose

Format version: `1`
Study ID: `writing-explicit-rationale`
Case ID: `catalog-review`
Definition version: `2`
Status: prepared for offline qualification
Purpose and mechanism: Future editors need two production decisions made during the same proof review. Repeated questions concern one rule. The other rule is already in the spec under review, although its wording needs no change. R2 tests whether its rationale survives; inferring a deliberate audit requires separate trace evidence.

## Inputs and setup

Supply the [task](task.md) and editable [fixture](fixture/) to both conditions. Keep the worked patch, decision question and scoring rules with the controller.

## Rules and evidence

Apply the [whole-output policy](../../protocol.md#assessment-policy). First read the projected project, then compare the entire project and delivered reply with the original request. Before sealing either reader packet, classify each added project file by its contents as durable project material or correspondence to the editor. Keep the full inventory, excluded paths and reasons with the controller. Include durable project references regardless of filename. Use the catalog projection in reader_payload.py for both reader types.

## Criteria

### T1: Resolve the editorial request

Basis: Task requirement.
Coverage: [Coverage map](../../protocol.md#coverage-before-the-shipped-benchmark).
Dimension: functional
Applies to: `original`, `control`
Judgment unit: Resolve the editorial request in this execution.
Required evidence: Compare the spec and delivered reply with the task.
Met: Both editorial rules remain in force and the editor receives an accurate answer about refreshing names.
Not met: The change drops a rule or gives the editor a materially wrong or missing answer.
Insufficient evidence: Missing inputs or outputs prevent judgment.
Alternatives: Credit any discoverable wording or arrangement preserving the decision.
Consequence: Record the specific loss for the editor.
Overlap: Explain shared causes once.

### R1: Recover credit authority

Basis: WER artifact contract.
Coverage: [Coverage map](../../protocol.md#coverage-before-the-shipped-benchmark).
Dimension: functional
Applies to: `original`, `control`
Judgment unit: Recover credit authority in this execution.
Required evidence: Read the lender rule and discoverable references.
Met: A future editor can tell whose approval controls publication and when an apparently stale credit can change.
Not met: The editor could publish a rebrand without lender amendment or has to consult correspondence to resolve the authority.
Insufficient evidence: Missing inputs or outputs prevent judgment.
Alternatives: Credit any discoverable wording or arrangement preserving the decision.
Consequence: Record the specific loss for the editor.
Overlap: Explain shared causes once.

### R2: Recover the production reason

Basis: WER artifact contract.
Coverage: [Coverage map](../../protocol.md#coverage-before-the-shipped-benchmark).
Dimension: functional
Applies to: `original`, `control`
Judgment unit: Recover the production reason in this execution.
Required evidence: Read the room-order rule and discoverable references.
Met: A future editor can recover why proof corrections depend on accession order. Title lookup in the index is optional.
Not met: The only explanation is in correspondence or the editor could alphabetize without knowing that would disrupt the room-sheet match.
Insufficient evidence: Missing inputs or outputs prevent judgment.
Alternatives: Credit any discoverable wording or arrangement preserving the decision.
Consequence: Record the specific loss for the editor.
Overlap: Explain shared causes once.

## Constructed scoring checks

The worked patch plus an accurate reply meets all three criteria.
A two-column table giving signed credit and amendment authority in one row, and proof-sheet ordering and title lookup in another, also passes.
The order-reason-only variant also passes R2: knowing how proofs are matched is enough to decide whether alphabetizing would disrupt production.
The credit-only variant passes T1 and R1 with an accurate reply but leaves R2 missing even when the reply explains ordering.
The wrong-authority variant gives the publisher control of an amendment. It fails R1 even if the reply correctly names the lender; record the contradiction under T1 if it changes the delivered instruction.

## Downstream maintenance decision

Give a fresh reader only the [printer request](maintenance-question.txt) and one projected final project, without the original task, subject reply, skill, arm, rubric or prior reader answer.
Use the same request across the shipped and control conditions and seal the complete recommendation before revealing the source facts.
Record the proposed action, the project evidence for its reasoning, and the likely consequence for checking proofs.
Read the response as a whole.

- **Informed decision.** Keeping accession order because it lets the desk match corrections to room sheets passes. Approving title order with explicit acceptance of the harder proof check or a concrete way to preserve that match also passes, as does making approval conditional on verifying a workable matching method.
- **Unsupported decision.** Simply enforcing the printed rule, vaguely asking someone to confirm, or approving a reorder without considering the proof workflow leaves the material trade-off unresolved. A lucky guess about room sheets in a project that never mentions their role is unsupported even when the action is sensible.
- **Sound handling of missing context.** If the project gives only the order, a reader may reasonably hold the change and ask what depends on accession order and explain how the answer changes the recommendation. The contact can be anyone positioned to find out. A clearly labeled hypothesis is legitimate; claiming it as a project fact is unsupported. Record that as prudent reader judgment and a project that required follow-up. Do not attribute the missing explanation to reader error.
- **Unassessable.** Missing or invalid reader evidence leaves the decision unmeasured. Preserve the attempt.

Report the reader's action and whether the artifact supported an informed decision separately from the subject's T1/R1/R2 scores.
Where the project supplied the reason and the reader ignored it, record both observations.
One reader's response is evidence of what that reader did in this scenario.

## Limits

One development case with supplied reasons. Reader decisions are separate observations.
