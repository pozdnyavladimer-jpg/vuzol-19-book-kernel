# 11 — BINDU COMMIT PROTOCOL

**Project:** Vuzol-19  
**Module:** Hexagram Simplicial Reasoning  
**Status:** COMMIT / PERSISTENT-STATE SPEC  
**State:** CRYSTAL  
**Language:** English  
**Depends on:** `10_GATE_AND_HOLD_PROTOCOL.md`

---

## 0. PURPOSE

The previous file defined:

```text
GATE
```

as the mechanism that decides whether a candidate state is permitted to proceed.

This file defines the next operation:

```text
BINDU
```

Bindu is the explicit **commit point**.

The central distinction is:

```text
Gate = permission
Bindu = commit
```

A state may be verified and still remain uncommitted.

This separation is important for:

- rollback;
- competing candidates;
- delayed commit;
- human review;
- transaction safety;
- persistent memory.

---

# 1. CORE IDEA

The local reasoning chain is:

```text
candidate
   |
   v
 Gate
   |
   v
 ALLOW
   |
   v
 BINDU
   |
   v
committed state
```

Bindu should answer:

> **When does a verified candidate become part of the persistent reasoning state?**

---

# 2. COMMIT IS A STATE TRANSITION

Let:

```math
P
```

be an allowed candidate.

Bindu performs:

```math
B:
P
\longrightarrow
M
```

where:

```math
M
```

is the committed state.

The transformation must preserve:

```text
identity
provenance
Gate verdict
certificate
critical Shadow
version
timestamp / step
```

---

# 3. BINDU INPUT

Recommended Bindu input:

```text
allowed candidate
Gate result
certificate
provenance
Shadow summary
current parent state
commit policy
```

A commit request should be invalid if:

```text
Gate verdict != ALLOW
```

unless the commit policy explicitly permits a qualified state such as:

```text
ALLOW_WITH_RESIDUAL
```

---

# 4. BINDU PRECONDITION

Default hard precondition:

```text
Gate verdict = ALLOW
```

or:

```text
Gate verdict = ALLOW_WITH_RESIDUAL
```

with:

```text
residual policy explicitly satisfied
```

Do not allow:

```text
HOLD
EXPAND
RECOMPUTE
UNKNOWN
```

to commit as valid persistent state.

---

# 5. COMMIT OBJECT

A committed state should not be only:

```text
value
```

Recommended object:

```text
CommittedState
|
+-- state value
+-- state ID
+-- parent IDs
+-- Gate result
+-- certificate
+-- critical Shadow summary
+-- provenance
+-- timestamp / step
+-- operator versions
+-- commit policy
+-- status
```

---

# 6. STATE IDENTITY

Every committed state needs a stable identifier.

Example:

```text
state_id = BINDU-000042
```

or content-addressed form:

```text
hash(state + provenance + version)
```

The purpose is to make the commit referenceable and auditable.

---

# 7. IMMUTABILITY

Preferred default:

> A committed state should be immutable.

If a correction is required:

```text
do not overwrite old commit
```

Instead:

```text
commit v1
  |
  v
superseded by
  |
  v
commit v2
```

This preserves history.

---

# 8. COMMIT LINEAGE

A committed state should record:

```text
parent commit
source candidate
Gate event
repair history
```

Example:

```text
M17
 |
 +-- parent: M12
 +-- candidate: P31
 +-- Gate event: G77
 +-- repair path: [EXPAND child_2, RECOMPUTE]
```

This makes state evolution reproducible.

---

# 9. COMMIT TRANSACTION

A useful software model:

```text
BEGIN COMMIT

1. verify Gate verdict
2. verify candidate version
3. verify critical Shadow policy
4. assign state ID
5. freeze certificate
6. write provenance
7. write commit record
8. update active pointer

COMMIT
```

If any step fails:

```text
ABORT
```

---

# 10. ATOMIC COMMIT

Bindu should ideally be atomic.

Meaning:

```text
either
the complete state record is committed

or
nothing is committed
```

Avoid partial persistent writes such as:

```text
state saved
but provenance missing
```

or:

```text
value saved
but Gate result lost
```

---

# 11. ACTIVE POINTER

The system may maintain:

```text
ACTIVE_STATE
```

pointing to the current committed state.

Example:

```text
ACTIVE_STATE -> M42
```

A new successful commit changes:

```text
ACTIVE_STATE -> M43
```

without deleting `M42`.

---

# 12. COMMIT VS MEMORY

Bindu is the commit action.

Memory is the stored result.

Therefore:

```text
Bindu
=
transition into persistent state

MemoryAtom
=
the persistent record produced by that transition
```

This distinction will matter later.

---

# 13. MEMORYATOM INTERFACE

A minimal conceptual `MemoryAtom`:

```text
MemoryAtom
|
+-- id
+-- state
+-- state_type
+-- parent_ids
+-- provenance
+-- Gate verdict
+-- certificate
+-- Shadow summary
+-- uncertainty
+-- created_step
+-- schema version
```

---

# 14. WHY STORE THE GATE VERDICT

A future reasoning step should know whether a state was:

```text
fully allowed
allowed with residual
human-reviewed
recovered after repair
```

Without this metadata, all committed states appear equally trustworthy.

That is undesirable.

---

# 15. COMMIT CONFIDENCE

A committed state may carry:

```math
C_M
\in
[0,1]
```

representing calibrated confidence or validation strength.

But:

```text
confidence
```

must not replace:

```text
explicit Gate checks
```

A high confidence score cannot legalize a failed hard constraint.

---

# 16. CRITICAL SHADOW AT COMMIT

Before Bindu, inspect:

```text
critical unresolved Shadow
```

Default rule:

```text
critical unresolved Shadow
-> no final commit
```

Possible exception:

```text
commit as provisional state
```

with explicit status:

```text
PROVISIONAL
```

---

# 17. COMMIT STATUS

Recommended statuses:

```text
FINAL
PROVISIONAL
SUPERSEDED
ROLLED_BACK
INVALIDATED
ARCHIVED
```

This is separate from Gate verdict.

A Gate may say:

```text
ALLOW
```

while Bindu chooses:

```text
PROVISIONAL
```

because the broader commit policy requires later review.

---

# 18. PROVISIONAL COMMIT

Use when:

```text
local state is valid
but global verification is incomplete
```

Example:

```text
local mathematical lemma verified
global proof not complete
```

The state may be stored without being treated as final.

---

# 19. FINAL COMMIT

Use when:

```text
required local and global Gate conditions pass
critical residuals resolved or accepted
commit policy satisfied
```

A final commit should be stable enough to serve as future trusted state.

---

# 20. SUPERSEDED STATE

When a newer valid state replaces an older one:

```text
M42 -> M43
```

mark:

```text
M42.status = SUPERSEDED
```

Do not erase it.

This preserves temporal lineage.

---

# 21. INVALIDATED STATE

A previously committed state may later be found invalid.

Example:

```text
new evidence reveals a hidden hard constraint failure
```

Then:

```text
status = INVALIDATED
```

and create a correction lineage.

This is preferable to silent mutation.

---

# 22. ROLLBACK

Rollback means:

```text
move active pointer back
to a previous committed state
```

Example:

```text
ACTIVE -> M43
```

after failure:

```text
ACTIVE -> M42
```

The rollback event itself should be recorded.

---

# 23. ROLLBACK IS NOT DELETION

The invalid or failed later state may remain in history.

Rollback changes:

```text
which state is active
```

not:

```text
what history existed
```

This is important for audit.

---

# 24. ROLLBACK TRIGGERS

Possible triggers:

```text
new hard constraint violation
failed global Gate
corrupted provenance
version incompatibility
failed post-commit audit
human/operator rejection
```

---

# 25. POST-COMMIT AUDIT

Bindu does not mean:

```text
never inspect again
```

A committed state may be re-audited later.

Possible actions:

```text
remain valid
mark provisional
invalidate
supersede
rollback
```

This supports evolving knowledge.

---

# 26. REENTRY

A committed state may later reenter active reasoning.

This is:

```text
reentry
```

The system should verify:

```text
schema version
operator compatibility
constraint context
Shadow references
provenance availability
```

before reuse.

---

# 27. REENTRY GATE

A state that was valid under an old context may not be valid now.

Therefore:

```text
committed
```

does not imply:

```text
universally reusable
```

A reentry Gate may check context compatibility.

---

# 28. CONTEXT-BOUND COMMIT

Some commits are valid only within a domain:

```text
temperature range
software version
legal jurisdiction
task assumptions
time interval
```

Store:

```text
validity_scope
```

inside the commit record.

---

# 29. VALIDITY SCOPE

Possible structure:

```text
ValidityScope
|
+-- domain
+-- assumptions
+-- time range
+-- environment
+-- version constraints
```

A future consumer must satisfy the scope.

---

# 30. COMMIT HASH

For exact records, compute:

```text
commit_hash
```

over critical fields.

This supports corruption detection.

The exact hash algorithm is an implementation detail.

---

# 31. CONTENT-ADDRESSABLE MEMORY

One option:

```text
state_id = hash(content)
```

Advantages:

```text
deduplication
integrity check
stable references
```

Limitations:

```text
metadata changes alter hash
privacy considerations
large content handling
```

This is optional.

---

# 32. COMMIT COLLISION

Two different histories may produce the same outer state.

Therefore do not identify commits only by:

```text
state value
```

Include:

```text
provenance
context
version
branch identity
```

in identity semantics.

---

# 33. EQUIFINAL COMMIT

Example:

```text
State A:
Balance = 0.8
history = natural stability

State B:
Balance = 0.8
history = active compensation
```

These should not collapse into the same MemoryAtom if their provenance matters.

---

# 34. COMMIT GRANULARITY

Possible commit units:

```text
single local parent
subtree
proof step
agent action
document state
global reasoning root
```

The architecture should support different granularity.

Too fine:

```text
high commit overhead
```

Too coarse:

```text
poor rollback resolution
```

---

# 35. COMMIT FREQUENCY

Possible policies:

```text
every Gate ALLOW
every hierarchy level
only stable checkpoints
only final root
risk-based
```

This is an empirical design choice.

---

# 36. CHECKPOINT COMMIT

A useful middle ground:

```text
commit only meaningful stable checkpoints
```

while keeping transient candidates outside persistent memory.

This can reduce memory growth.

---

# 37. COMMIT COST

Define:

```math
C_{\mathrm{commit}}
```

as compute + storage cost of creating a persistent state.

The architecture should measure:

```text
commit frequency
memory growth
lookup cost
rollback benefit
```

---

# 38. COMMIT UTILITY

Candidate objective:

```math
U_{\mathrm{commit}}
=
V_{\mathrm{recovery}}
+
V_{\mathrm{reuse}}
+
V_{\mathrm{audit}}
-
C_{\mathrm{storage}}
-
C_{\mathrm{write}}
```

This is a **MODEL**.

The right commit frequency should maximize practical value.

---

# 39. COMMIT DEDUPLICATION

If two candidate states are effectively identical under the required identity policy:

```text
do not create redundant commits
```

Instead reference the existing state.

But deduplication must not erase meaningful provenance differences.

---

# 40. MERGE COMMIT

Two branches may converge:

```text
M1
 \
  -> M3
 /
M2
```

A merge commit should record both parents:

```text
parent_ids = [M1, M2]
```

This is useful for multi-branch reasoning.

---

# 41. BRANCH COMMIT

Reasoning may split:

```text
M1
 |\
 | \
M2a M2b
```

Do not force an early single branch if both remain viable.

Bindu may commit both as:

```text
PROVISIONAL BRANCHES
```

until Gate resolves them.

---

# 42. BRANCH RESOLUTION

When one branch is selected:

```text
selected branch -> active
other branch -> archived / Shadow / alternative
```

The rejected branch may remain useful for future reentry.

---

# 43. COMMIT AND AMBIGUITY

A state with unresolved branch ambiguity should not be labeled final unless the task allows set-valued output.

Possible commit:

```text
state = {branch A, branch B}
status = PROVISIONAL
```

This is more honest than choosing arbitrarily.

---

# 44. COMMIT AND UNKNOWN

An `UNKNOWN` Gate verdict should not become a valid final state.

However, Bindu may optionally persist:

```text
UnknownRecord
```

as a memory that verification failed.

That record is not a trusted solution.

---

# 45. NEGATIVE MEMORY

It is useful to remember:

```text
what was attempted
what failed
why it failed
```

This prevents repeated useless exploration.

A failed candidate may become:

```text
FailureAtom
```

rather than a committed valid state.

---

# 46. FAILUREATOM

Conceptual record:

```text
FailureAtom
|
+-- candidate ID
+-- reason codes
+-- failed constraints
+-- failed edges
+-- attempted repairs
+-- provenance
+-- timestamp / step
```

This belongs to memory, but not trusted solution state.

---

# 47. BINDU AND FALSE-GREEN

A False-Green candidate may look correct.

But if Gate rejected the process:

```text
Bindu must not commit it as valid
```

This is one of the strongest roles of separating:

```text
candidate
Gate
Bindu
```

---

# 48. COMMIT POLICY OBJECT

Conceptual policy:

```python
CommitPolicy(
    allowed_gate_verdicts=["ALLOW"],
    allow_provisional=False,
    require_provenance=True,
    require_no_critical_shadow=True,
    require_scope=True,
    persist_failure_atoms=True,
    checkpoint_mode="risk_based",
)
```

---

# 49. COMMIT RESULT

Conceptual result:

```python
CommitResult(
    committed=True,
    state_id="...",
    status="FINAL",
    reason=None,
    previous_active_state="...",
    new_active_state="...",
)
```

On failure:

```python
CommitResult(
    committed=False,
    state_id=None,
    status=None,
    reason="GATE_NOT_ALLOWED",
)
```

---

# 50. BINDU PSEUDOCODE

```python
def bindu_commit(candidate, gate_result, policy, store):
    if gate_result.verdict not in policy.allowed_gate_verdicts:
        return CommitResult(
            committed=False,
            reason="GATE_NOT_ALLOWED",
        )

    if policy.require_no_critical_shadow:
        if critical_shadow_unresolved(candidate):
            return CommitResult(
                committed=False,
                reason="CRITICAL_SHADOW_UNRESOLVED",
            )

    if policy.require_provenance:
        if not provenance_complete(candidate):
            return CommitResult(
                committed=False,
                reason="PROVENANCE_INCOMPLETE",
            )

    record = build_memory_atom(
        candidate=candidate,
        gate_result=gate_result,
        policy=policy,
    )

    state_id = store.atomic_write(record)

    update_active_pointer(state_id)

    return CommitResult(
        committed=True,
        state_id=state_id,
        status=record.status,
    )
```

This is an interface sketch.

---

# 51. MEMORYATOM DATA CONTRACT

```python
from dataclasses import dataclass
from typing import Any, Dict, List, Optional

@dataclass(frozen=True)
class MemoryAtom:
    id: str
    state: Any
    state_type: str
    parent_ids: List[str]
    provenance: Dict[str, Any]
    gate_result: Dict[str, Any]
    certificate: Dict[str, Any]
    shadow_summary: Dict[str, Any]
    uncertainty: float
    validity_scope: Dict[str, Any]
    created_step: int
    schema_version: str
    status: str
```

Immutability is represented here by:

```python
frozen=True
```

for the conceptual Python contract.

---

# 52. ATOMIC WRITE TEST

**TEST**

Simulate failure during commit.

Example:

```text
state written
provenance write fails
```

Expected:

```text
whole transaction aborted
```

No partial MemoryAtom should appear.

---

# 53. GATE-BYPASS TEST

**TEST**

Attempt to commit:

```text
Gate verdict = HOLD
```

Expected:

```text
commit rejected
```

This is a critical safety invariant.

---

# 54. CRITICAL SHADOW TEST

**TEST**

Gate says:

```text
ALLOW
```

but policy finds unresolved critical Shadow.

Expected:

```text
commit rejected
```

unless provisional policy explicitly allows it.

---

# 55. PROVISIONAL COMMIT TEST

**TEST**

Use:

```text
local state valid
global state incomplete
```

Expected:

```text
status = PROVISIONAL
```

not `FINAL`.

---

# 56. ROLLBACK TEST

**TEST**

Create:

```text
M1 -> M2 -> M3
```

invalidate `M3`.

Expected:

```text
ACTIVE -> M2
```

with rollback event recorded.

---

# 57. SUPERSEDE TEST

**TEST**

Commit corrected state:

```text
M4
```

that replaces:

```text
M3
```

Expected:

```text
M3.status = SUPERSEDED
M4.status = FINAL
```

without deleting `M3`.

---

# 58. EQUIFINALITY TEST

**TEST**

Create two equal outer values with different provenance.

Expected:

```text
different commit identities
```

when provenance affects future behavior.

---

# 59. REENTRY TEST

**TEST**

Load an old committed state under a new context.

If validity scope does not match:

```text
reentry Gate should reject or downgrade
```

This prevents stale trusted state.

---

# 60. VERSION DRIFT TEST

**TEST**

Attempt to reopen a commit made under:

```text
schema v1
```

using incompatible:

```text
schema v3
```

Expected:

```text
migration
HOLD
or
VERSION_MISMATCH
```

not silent reinterpretation.

---

# 61. BRANCH COMMIT TEST

**TEST**

Two candidate branches both pass local Gate.

Expected:

```text
both may be stored provisionally
```

until a higher-level Gate resolves them.

This prevents premature collapse.

---

# 62. FAILUREATOM TEST

**TEST**

A candidate repeatedly fails hard constraints.

Expected:

```text
no valid MemoryAtom
```

but optionally:

```text
FailureAtom persisted
```

for future learning.

---

# 63. COMMIT ABLATION — NO IMMUTABILITY

Compare:

```text
immutable append-only commits
```

against:

```text
mutable overwrite
```

Measure:

```text
auditability
rollback success
debugging time
corruption recovery
```

---

# 64. COMMIT ABLATION — EVERY STEP VS CHECKPOINT

Compare:

```text
commit every allowed node
```

against:

```text
checkpoint commits
```

Measure:

```text
storage
rollback granularity
lookup cost
recovery quality
```

---

# 65. COMMIT ABLATION — NO PROVENANCE

Compare commits:

```text
with provenance
```

against:

```text
state only
```

Use equifinality tasks.

The hypothesis is that provenance prevents harmful state collapse.

---

# 66. COMMIT ABLATION — NO SHADOW SUMMARY

Compare:

```text
MemoryAtom + Shadow summary
```

against:

```text
MemoryAtom without residual metadata
```

Use tasks where later reentry depends on omitted residuals.

---

# 67. COMMIT ABLATION — NO VALIDITY SCOPE

Use states valid only under specific assumptions.

Compare reuse with and without scope metadata.

Measure stale-state errors.

---

# 68. PRIMARY SUCCESS CRITERIA

A useful Bindu protocol should:

1. prevent non-allowed candidates from becoming trusted persistent state;
2. preserve commit lineage;
3. support rollback;
4. support provisional branches;
5. preserve provenance-sensitive distinctions;
6. detect version/context incompatibility on reentry;
7. avoid partial writes;
8. support persistent audit without uncontrolled storage growth.

---

# 69. FAILURE CONDITIONS

Bindu should be revised if:

1. commit history becomes too large to manage;
2. rollback rarely helps;
3. immutability creates excessive storage without audit value;
4. provenance-sensitive commits still collapse incorrectly;
5. reentry uses stale state without detection;
6. critical Shadow is frequently committed accidentally;
7. partial writes can occur;
8. commit identity is unstable;
9. provisional and final states are confused;
10. simpler checkpointing provides the same reliability.

---

# 70. RESEARCH STATUS

```text
FACT:
Verification and persistence are distinct operations.

FACT:
Immutable append-only state histories support rollback and audit.

MODEL:
Bindu is the explicit transition from allowed candidate
to persistent committed state.

MODEL:
MemoryAtom stores state + provenance + Gate result
+ certificate + Shadow summary + validity scope.

HYPOTHESIS:
Separating Gate from Bindu reduces False-Green persistence,
improves rollback, and preserves reasoning lineage.

TEST:
Gate bypass, atomic write, rollback, reentry,
equifinality, version drift, branch commit,
and checkpoint ablation experiments.
```

---

# 71. COMPLETE LOCAL CHAIN SO FAR

The architecture now has:

```text
Signal / local state
        |
        v
simplex + coupling
        |
        v
+3 Forward
        |
        v
candidate parent
        |
        +----> Shadow
        |
        v
-3 Backward
        |
        v
audit
        |
        v
Gate
        |
        v
ALLOW
        |
        v
Bindu
        |
        v
MemoryAtom
```

This is the first complete:

```text
generate
compress
reconstruct
verify
commit
remember
```

cycle in the module.

---

# 72. WHAT COMES NEXT

The current mechanism is local.

The next challenge is scale.

We need to define how many local verified nodes can be organized recursively into a larger reasoning tree without losing:

```text
cross-branch edges
critical constraints
Shadow locality
repair locality
```

That is the purpose of the next file.

---

# 73. NEXT FILE

Next:

```text
12_RECURSIVE_REASONING_TREE.md
```

Its purpose is to formalize:

```text
leaf states
-> local triads
-> verified parents
-> higher triads
-> root
```

with:

```text
balanced and unbalanced trees
cross-level edges
adaptive depth
local repair
root verification
complexity analysis
```

---

## FILE VERDICT

```text
STATE: CRYSTAL

DEFINED:
Bindu Commit Protocol

CORE:
Gate = permission
Bindu = commit
MemoryAtom = persistent record

COMMIT SUPPORTS:
immutability
lineage
rollback
provisional states
branching
reentry
validity scope
FailureAtom memory

CRITICAL RULE:
verified does not automatically mean committed

NEXT:
12_RECURSIVE_REASONING_TREE.md
```
