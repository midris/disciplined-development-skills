# Controller reference facts

Synthetic adaptation of historical SSR-05. Unlike that fixture, this repository does not supply a completed negative search.

The malformed heading `Member ship` occurs once, in docs/glossary.md. Replace it with `Membership`. No supplied link targets that heading anchor; README links to the file. All other supplied membership, billing and shipping statements are current and should retain their meaning. The shipping phrase is an unrelated near-match, not a typo to normalize. The JSON values stay unchanged.

Searching sufficiently to establish locality supports P1. The required commit evidence for the original is `References swept: n/a — <reason>` explaining a justified local correction. Do not require zero hits for broad searches such as “member”: unrelated/current matches can exist without requiring edits. A search showing no exact sibling does not by itself prove the agent considered relevant variants; inspect the overall search and reasoning.

Functional evidence is the correct heading, preserved meaning/links and committed correction. Exact byte equality is a useful minimal-solution check, not the only acceptable implementation. Reformatting without semantic harm is not automatically a functional failure. A claimed broad sweep with no observable trace is not proof of procedure; missing trace produces insufficient evidence, while a captured absence of search is a P1 defect.

Boundary examples: correction with sparse account passes functionally but fails P3; correct account with heading unchanged fails F1; changing shipping meaning fails F2; an uncommitted correction fails F3. A justified local outcome is not permission to skip checking scope.
