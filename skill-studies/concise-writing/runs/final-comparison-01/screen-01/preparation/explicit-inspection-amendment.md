# Explicit-load teaching-body inspection amendment

Claude subject 7 completed and was retained with one charge under the original manifest.
The original inspector rejected its valid native Skill delivery because it required YAML frontmatter as well as the teaching body.
The retained trace delivers the exact complete assigned teaching body at event 14 before the first task edit at event 16; native Skill omits YAML metadata.
This is a controller representation error, not a subject failure, missing teaching or reason to repeat the run.

[Inspector v2](inspect_explicit_v2.py) accepts the complete body with or without frontmatter, including numbered Read output; fragments, metadata alone and altered bodies do not qualify.
Inventory, capture, runtime identity, edit ordering and protected-input checks remain unchanged.
The [original inspector](inspect_one.py), original slot-7 manifest, invocation, capture and charge remain intact.
Slot 7 is assessed by read-only replay; the amended Claude manifest applies prospectively to slots 8–12.
Subject files, skill bodies/descriptions, prompts, criteria, order, models, permissions and allocation remain byte-identical.
No new inference, retry or exclusion is authorized by this repair.

[Six offline cases](inspection-tests/test_body_delivery.py) first produced two failures and four passes with the full-file predicate, then six passes after correction.
The [verification record](explicit-inspection-amendment.json) pins retained original-failing and corrected-passing replay logs, source snapshots and the six-case test run.
The protocol remains the authority for progress and accounting.
