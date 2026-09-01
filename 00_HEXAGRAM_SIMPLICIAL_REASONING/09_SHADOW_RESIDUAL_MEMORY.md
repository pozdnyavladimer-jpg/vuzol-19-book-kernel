# 09 — SHADOW / RESIDUAL MEMORY

**Project:** Vuzol-19  
**Module:** Hexagram Simplicial Reasoning  
**Status:** RESIDUAL MEMORY SPEC  
**State:** CRYSTAL  
**Language:** English  
**Depends on:** `08_MINUS3_BACKWARD_OPERATOR.md`

---

## 0. PURPOSE

The previous file defined:

```text
-3 BACKWARD
```

as a reconstruction and audit operator.

That operator depends on information that the compressed parent did not fully absorb.

This file gives that information a dedicated memory layer:

```text
SHADOW
```

The central definition is:

> **Shadow is the explicit memory of information that could not be safely absorbed into the compressed parent without increasing reconstruction risk, constraint risk, or uncertainty.**

Shadow is not:

```text
garbage
noise
hidden magic
error itself
```

It is a controlled residual channel.

---

# 1. WHY SHADOW EXISTS

Compression creates a choice:

```text
retain
discard
or store for possible recovery
```

If every detail is retained in the parent:

```text
no meaningful compression
```

If every non-dominant detail is discarded:

```text
high risk of irreversible reasoning loss
```

Shadow creates a third option:

```text
compress the active state
while retaining recoverable residual structure
```

---

# 2. BASIC DECOMPOSITION

Let the original local state be:

```math
X
```

The forward operator produces:

```math
P=F_{+3}(X)
```

and a reconstruction:

```math
\hat{X}=F_{-3}(P)
```

Define the residual:

```math
S
=
X-\hat{X}
```

In the simplest vector case, `S` is the Shadow.

For structured reasoning, Shadow may be richer than a numeric residual.

---

# 3. SHADOW AS STRUCTURED MEMORY

A practical Shadow record may contain:

```text
ShadowRecord
|
+-- residual values
+-- omitted child fields
+-- omitted edges
+-- unresolved constraints
+-- approximation remainder
+-- ambiguity branches
+-- provenance references
+-- uncertainty delta
+-- deletion / retention policy
```

Therefore Shadow is better treated as a typed residual object.

---

# 4. SHADOW IS NOT UNCERTAINTY

This distinction is critical.

Uncertainty means:

```text
we do not know exactly
```

Shadow means:

```text
we know some information was not promoted
into the compressed active state
```

Example:

```text
uncertainty:
the true edge weight may be between 0.4 and 0.7
```

Shadow:

```text
the exact intermediate edge was omitted from parent
but stored for possible reconstruction
```

They may coexist.

They are not the same variable.

---

# 5. SHADOW IS NOT ORDINARY MEMORY

Ordinary memory may store:

```text
facts
events
past states
documents
```

Shadow specifically stores:

> information excluded by a compression, abstraction, pruning, or commit decision.

Therefore Shadow always has a relation to a parent or transition.

A Shadow item should answer:

```text
Shadow of what?
Why was it not retained?
When may it be needed again?
```

---

# 6. SHADOW PARENT LINK

Every Shadow record should contain:

```text
parent_id
compression_step_id
operator_version
```

This allows the system to reconnect the residual with the exact compression event that created it.

---

# 7. SHADOW CLASSES

Recommended first taxonomy:

```text
S1 — numeric residual
S2 — omitted edge
S3 — omitted child state
S4 — unresolved constraint
S5 — approximation remainder
S6 — branch ambiguity
S7 — provenance residue
S8 — uncertainty residue
S9 — boundary interface residue
```

These classes are implementation labels.

They are not claimed to be universally complete.

---

# 8. S1 — NUMERIC RESIDUAL

For numeric state:

```math
S_{\mathrm{num}}
=
X-\hat{X}
```

Example:

```math
X=(6,3,1)
```

```math
\hat{X}=(5.9,3.0,1.1)
```

Then:

```math
S_{\mathrm{num}}
=
(0.1,0,-0.1)
```

This localizes distortion.

---

# 9. S2 — OMITTED EDGE

Original local graph:

```text
A -> B
B -> C
A -> C
```

Compressed parent retains:

```text
A -> C
```

Shadow may store:

```text
A -> B
B -> C
```

These edges may later be needed for audit.

---

# 10. S3 — OMITTED CHILD STATE

A parent may hide an intermediate child:

```text
A -> B -> C
```

compressed to:

```text
A -> C
```

Then Shadow may retain:

```text
B
```

or a compressed description of `B`.

This supports future expansion.

---

# 11. S4 — UNRESOLVED CONSTRAINT

Suppose a constraint is known but not yet decidable.

Example:

```text
x must remain positive
```

but the parent only knows an interval:

```math
x\in[-0.1,0.5]
```

The unresolved constraint belongs in Shadow or unresolved certificate state.

It must not disappear.

---

# 12. S5 — APPROXIMATION REMAINDER

For:

```math
\log(1+\varepsilon)
=
\varepsilon
-
\frac{\varepsilon^2}{2}
+
\frac{\varepsilon^3}{3}
-\dots
```

if the parent retains only:

```math
\varepsilon
```

then Shadow may contain:

```math
-\frac{\varepsilon^2}{2}
+
\frac{\varepsilon^3}{3}
-\dots
```

or a certified remainder bound.

This is a strong mathematical example of Shadow.

---

# 13. S6 — BRANCH AMBIGUITY

For:

```math
y=x^2
```

with:

```math
y=4
```

the parent state may not identify whether:

```math
x=2
```

or:

```math
x=-2
```

If branch identity is not retained in the parent core, Shadow should preserve:

```text
possible branches = {-2, +2}
```

or the actual provenance branch if known.

---

# 14. S7 — PROVENANCE RESIDUE

A compressed parent may retain a conclusion but not the full source path.

Shadow can preserve:

```text
source node IDs
source equations
source text spans
tool result IDs
derivation references
```

This prevents post-hoc fabricated provenance.

---

# 15. S8 — UNCERTAINTY RESIDUE

Compression may increase uncertainty.

Store the increment:

```math
\Delta U
=
U_{\mathrm{after}}
-
U_{\mathrm{before}}
```

This can be treated as a Shadow signal if it was caused by omitted information.

---

# 16. S9 — BOUNDARY INTERFACE RESIDUE

When a subtree is compressed, some weak external edges may be removed from the active interface.

If they may matter later, store them in Shadow.

Example:

```text
subtree T
|
+-- active boundary edge to X
+-- weak omitted edge to Y
```

The second edge may enter `S9`.

---

# 17. ACTIVE VS PASSIVE SHADOW

Two modes:

```text
ACTIVE SHADOW
=
monitored continuously
```

```text
PASSIVE SHADOW
=
stored only for retrieval
```

Active Shadow may trigger Gate conditions.

Passive Shadow is cheaper but less responsive.

---

# 18. CRITICAL SHADOW

Some residuals must never be discarded casually.

Examples:

```text
hard constraint residue
branch identity
sign information
critical edge
irreversible operation metadata
safety-relevant provenance
```

Mark:

```text
critical = true
```

These items should have stronger retention policy.

---

# 19. SHADOW PRIORITY

Assign priority:

```math
P_S
=
f(
\mathrm{impact},
\mathrm{uncertainty},
\mathrm{irreversibility},
\mathrm{constraint\ status},
\mathrm{reconstruction\ need}
)
```

This is a **MODEL**.

The exact function is task-dependent.

---

# 20. SHADOW SIZE

Define:

```math
M_S
=
\mathrm{size}(S)
```

A useful architecture must track how much memory Shadow consumes.

Shadow is not free.

---

# 21. SHADOW RATIO

Relative to original local state size:

```math
\rho_S
=
\frac{
\mathrm{size}(S)
}{
\mathrm{size}(X)
}
```

If:

```math
\rho_S\approx1
```

then almost everything has moved into Shadow.

The active parent may look compressed, but total memory has not improved much.

---

# 22. TOTAL COMPRESSION RATIO

The real compression ratio must include Shadow:

```math
\rho_{\mathrm{total}}
=
\frac{
\mathrm{size}(P)+\mathrm{size}(S)
}{
\mathrm{size}(X)
}
```

This is the correct metric.

Do not report only parent size.

---

# 23. SHADOW EFFICIENCY

A candidate metric:

```math
\eta_{\mathrm{shadow}}
=
\frac{
\text{reconstruction benefit from Shadow}
}{
\text{Shadow memory cost}
}
```

High `eta_shadow` means Shadow stores useful recovery information efficiently.

This metric is conceptual and requires a task-specific benefit scale.

---

# 24. SHADOW LIFETIME

A Shadow item should not necessarily live forever.

Possible policies:

```text
until parent committed
until global Bindu
until subtree is no longer reachable
until confidence rises
until a time-to-live expires
until reconstruction certificate becomes stable
```

Retention policy must be explicit.

---

# 25. SHADOW TTL

Optional field:

```text
ttl
```

or:

```text
expire_after_step
```

Useful for low-priority residuals.

Critical Shadow may ignore TTL.

---

# 26. SHADOW DECAY

For approximate or probabilistic tasks, Shadow importance may decay:

```math
P_S(t)
=
P_S(0)e^{-\lambda t}
```

This is only a possible memory policy.

Do not use decay for hard constraints or irreversible branch identity unless explicitly justified.

---

# 27. SHADOW PROMOTION

Sometimes residual information becomes important later.

Then Shadow may be promoted back into active state.

```text
Shadow
  |
  v
relevance rises
  |
  v
PROMOTE
  |
  v
active parent / expanded subtree
```

This is the reverse of pruning.

---

# 28. SHADOW RETRIEVAL

Retrieval triggers may include:

```text
Gate failure
high uncertainty
branch ambiguity
constraint conflict
unexpected downstream result
backward audit request
final Bindu audit
```

The system should not scan all Shadow continuously.

Use indexed retrieval.

---

# 29. SHADOW INDEX

Recommended indices:

```text
parent_id
child_id
edge_id
constraint_id
provenance source
reasoning depth
risk class
timestamp / step
```

This supports targeted expansion.

---

# 30. SHADOW LOCALITY

A Shadow record should remain attached to the smallest relevant subtree when possible.

Prefer:

```text
local residual
```

over:

```text
one global unstructured residual pool
```

Locality improves error localization.

---

# 31. SHADOW CHAIN

Compression may happen recursively.

Then Shadow may itself have ancestry:

```text
Shadow level 0
  |
  v
compressed parent
  |
  v
Shadow level 1
```

The architecture must avoid uncontrolled Shadow nesting.

---

# 32. SHADOW-OF-SHADOW WARNING

If Shadow is repeatedly compressed into new Shadow without clear accounting, the system can create hidden information debt.

Therefore track:

```text
shadow_depth
```

and set a maximum or audit threshold.

---

# 33. RESIDUAL DEBT

Define residual debt:

```math
D_S
=
\sum_i
w_i\,M_{S_i}
```

where higher-risk Shadow items receive larger weights.

High residual debt may trigger:

```text
EXPAND
AUDIT
REBALANCE
```

This is a **MODEL**.

---

# 34. SHADOW BUDGET

Define a memory budget:

```math
B_S
```

The system should satisfy:

```math
M_S
\le
B_S
```

unless critical residuals force an exception.

When budget is exceeded:

```text
compress Shadow
delete low-priority Shadow
promote important Shadow
recompute subtree
```

---

# 35. SHADOW COMPRESSION

Shadow can itself be compressed.

But the same rule applies:

```text
Shadow compression
must not silently erase
critical residual information
```

Therefore Shadow compression may create:

```text
Shadow summary
+
Shadow certificate
+
critical exact fields
```

---

# 36. SHADOW LOSS FUNCTION

A learned Shadow compressor may optimize:

```math
\mathcal{L}_S
=
\lambda_1
\mathcal{L}_{\mathrm{rec}}
+
\lambda_2
\mathcal{L}_{\mathrm{critical}}
+
\lambda_3
\mathcal{L}_{\mathrm{memory}}
+
\lambda_4
\mathcal{L}_{\mathrm{task}}
```

where:

- `L_rec` — reconstruction loss;
- `L_critical` — loss on critical residual fields;
- `L_memory` — storage cost;
- `L_task` — downstream task loss.

---

# 37. SHADOW AND RATE-DISTORTION

Shadow creates a three-way tradeoff:

```text
parent size
Shadow size
reconstruction distortion
```

The design target is not:

```text
minimum parent size
```

but:

```text
minimum total cost
subject to acceptable reasoning reliability
```

---

# 38. SHADOW AND INFORMATION BOTTLENECK

Conceptually:

```text
Parent
=
task-relevant compressed state
```

```text
Shadow
=
discarded-but-recoverable residual
```

This resembles an explicit split around an information bottleneck.

The analogy is useful.

It does not make the architecture equivalent to any specific information bottleneck method.

---

# 39. SHADOW AND EXTERNAL MEMORY

Large residuals do not have to remain inside the active model context.

They may be stored in:

```text
external memory
database
graph store
file
vector store
symbolic cache
```

The active parent retains only a pointer.

This can reduce active context cost.

---

# 40. POINTER-BASED SHADOW

Instead of:

```text
Shadow = full omitted content
```

use:

```text
ShadowPointer(
    location=...,
    checksum=...,
    summary=...,
    critical_fields=...,
)
```

This is useful for large text or code subtrees.

---

# 41. SHADOW CHECKSUM

For exact stored artifacts, use:

```text
hash / checksum
```

to verify that retrieved residual data matches the original.

This prevents accidental corruption.

---

# 42. SHADOW VERSIONING

Store:

```text
shadow_schema_version
forward_operator_version
backward_operator_version
```

A Shadow record may become unreadable or ambiguous if the operator schema changes.

Versioning is required for reproducible audit.

---

# 43. SHADOW MUTABILITY

Default rule:

> Shadow should be append-only or versioned.

Do not silently overwrite old residuals.

If an updated residual is created:

```text
S_v1
-> S_v2
```

preserve the lineage.

---

# 44. SHADOW LINEAGE

A minimal lineage record:

```text
shadow_id
parent_shadow_id
source_parent_id
created_at_step
operator_version
reason_for_update
```

This supports debugging.

---

# 45. SHADOW CLEANUP

Deletion should require one of:

```text
irrelevance proven
reconstruction no longer needed
parent deleted
state superseded
budget policy
explicit human/operator decision
```

Critical Shadow should not be removed by generic cleanup.

---

# 46. SHADOW TOMBSTONE

When deleting important Shadow, keep a small tombstone:

```text
shadow existed
why deleted
when deleted
what parent it belonged to
```

This preserves minimal audit history.

---

# 47. SHADOW RETRIEVAL COST

Define:

```math
C_{\mathrm{retrieve}}
```

The system should measure:

```text
how expensive it is
to reopen residual information
```

If retrieval is too expensive, local repair loses its advantage.

---

# 48. REOPEN RATE

From the previous file:

```math
R_{\mathrm{open}}
=
\frac{
\text{number of expansions}
}{
\text{number of parent uses}
}
```

Shadow design should minimize unnecessary reopen operations while preserving safety.

---

# 49. SHADOW HIT RATE

Define:

```math
H_S
=
\frac{
\text{retrievals that materially help repair}
}{
\text{Shadow retrievals}
}
```

Low hit rate means Shadow is being retrieved too often or stores low-value information.

---

# 50. SHADOW MISS RATE

Define:

```math
M_S^{\mathrm{miss}}
=
\frac{
\text{failures caused by residual information not stored}
}{
\text{relevant failures}
}
```

This measures under-retention.

---

# 51. SHADOW FALSE-POSITIVE RATE

Over-retention also has a cost.

Define:

```math
F_S
=
\frac{
\text{stored Shadow never used and low value}
}{
\text{stored Shadow}
}
```

This is not always bad.

But a very high value indicates poor memory policy.

---

# 52. SHADOW POLICY OBJECTIVE

A practical objective is to balance:

```text
low miss rate
low memory cost
low retrieval cost
low reopen rate
high repair value
```

This is a multi-objective optimization problem.

---

# 53. CRITICAL RESIDUAL PROTECTION

Some Shadow entries should be exact.

Examples:

```text
sign
branch ID
hard constraint
irreversible transition marker
critical edge type
```

Do not lossy-compress these unless the task proves it safe.

---

# 54. APPROXIMATE RESIDUAL STORAGE

Other residuals may be stored approximately.

Examples:

```text
small numerical remainder
low-impact semantic detail
redundant local description
```

Use bounded error.

Store the bound.

---

# 55. RESIDUAL BOUND

For approximation residual:

```math
\|S\|
\le
\epsilon_S
```

A certificate should state the bound.

This is stronger than storing only:

```text
"residual is small"
```

---

# 56. TAYLOR SHADOW EXAMPLE

For:

```math
\log(1+\varepsilon)
=
\varepsilon
-
\frac{\varepsilon^2}{2}
+
R_3
```

parent retains:

```math
\varepsilon
```

Shadow stores:

```math
S
=
-\frac{\varepsilon^2}{2}
+
R_3
```

with a remainder bound.

If:

```math
n\varepsilon^2\to0
```

the Shadow is asymptotically negligible for the target limit.

This is a certified case where Shadow can remain unpromoted.

---

# 57. SHADOW PROMOTION EXAMPLE

Suppose a previously negligible term becomes multiplied by a large factor later.

Then:

```text
small Shadow
```

may become:

```text
large downstream effect
```

The system should detect relevance change and promote the term.

This is why permanent deletion is dangerous.

---

# 58. DOWNSTREAM AMPLIFICATION

Let residual be:

```math
\delta
```

and later sensitivity be:

```math
J
```

Then downstream effect is approximately:

```math
J\delta
```

A small residual with large sensitivity may become critical.

Shadow priority should consider downstream amplification.

---

# 59. SHADOW RISK SCORE

Candidate risk score:

```math
R_S
=
\|S\|
\cdot
A_S
\cdot
U_S
```

where:

- `||S||` — residual magnitude;
- `A_S` — downstream amplification estimate;
- `U_S` — uncertainty.

Again, this is a model heuristic.

---

# 60. SHADOW AND COUPLING

Residual importance often depends on edges.

A small omitted node may be irrelevant unless it has a strong coupling to a critical branch.

Therefore Shadow cannot be prioritized by node magnitude alone.

Store:

```text
residual
+
coupling context
```

---

# 61. SHADOW AND GATE

Later Gate logic may inspect:

```text
Shadow size
Shadow risk
critical residual count
unresolved constraint Shadow
branch ambiguity Shadow
```

Possible Gate rule:

```text
if critical Shadow unresolved:
    HOLD
```

This makes Shadow operational.

---

# 62. SHADOW AND BINDU

Before final commit, the system may require a final Shadow sweep.

Questions:

```text
Is any critical residual unresolved?
Is any branch ambiguity still active?
Can any omitted edge change the answer?
Is residual debt within threshold?
```

Only then should Bindu commit.

---

# 63. SHADOW AND MEMORYATOM

A future Vuzol-19 integration may write:

```text
MemoryAtom
=
committed state
+
relevant Shadow summary
+
provenance
```

This preserves not only what was accepted, but also what was intentionally left unresolved.

This is a model extension for later files.

---

# 64. SHADOW AS NEGATIVE SPACE

Conceptually:

```text
Parent
=
what was promoted
```

```text
Shadow
=
what was not promoted but still matters
```

This can be viewed as the negative space of a compression decision.

The metaphor is useful only if it maps to stored residual data.

---

# 65. SHADOW STORAGE MODES

Possible storage modes:

```text
INLINE
POINTER
COMPRESSED
EXACT
APPROXIMATE
EXTERNAL
EPHEMERAL
PERSISTENT
```

The storage mode should be selected by risk and size.

---

# 66. INLINE SHADOW

Use for:

```text
small critical residuals
small branch IDs
small constraint metadata
```

Stored directly inside the parent record.

---

# 67. POINTER SHADOW

Use for:

```text
large text
large code subtree
large graph fragment
external tool output
```

Parent stores a pointer and critical summary.

---

# 68. EXACT SHADOW

Use when:

```text
one bit of branch identity matters
sign must be exact
hard constraint must be exact
```

Exact storage can be tiny and highly valuable.

---

# 69. APPROXIMATE SHADOW

Use when:

```text
small numeric remainder
semantic detail
low-risk edge weights
```

Store a bounded approximation.

---

# 70. EPHEMERAL SHADOW

Use for residuals relevant only during a short local reasoning window.

Delete after safe commit.

---

# 71. PERSISTENT SHADOW

Use for:

```text
important unresolved branch
long-term audit
high-impact provenance
reusable scientific uncertainty
```

Persistent Shadow may become part of long-term memory.

---

# 72. SHADOW CONFLICT

Two Shadow records may disagree.

Example:

```text
Shadow A:
constraint active

Shadow B:
constraint expired
```

The system must not merge them silently.

Create:

```text
SHADOW_CONFLICT
```

and require reconciliation.

---

# 73. SHADOW MERGE

When merging two parent nodes, their Shadow sets may be combined:

```math
S_P
=
S_1
\cup
S_2
\cup
S_{\mathrm{new}}
```

But duplicates and contradictions must be resolved.

---

# 74. SHADOW DEDUPLICATION

Use:

```text
stable IDs
hashes
source references
semantic equivalence checks
```

to reduce redundant residual storage.

Do not deduplicate critical records only by semantic similarity.

---

# 75. SHADOW CANONICALIZATION

A structured Shadow schema helps compare residuals.

Example:

```python
ShadowRecord(
    id=...,
    parent_id=...,
    kind=...,
    payload=...,
    critical=...,
    uncertainty=...,
    provenance=...,
    created_step=...,
    ttl=...,
)
```

This should be preferred over free-form text blobs when possible.

---

# 76. MINIMAL PYTHON DATA CONTRACT

```python
from dataclasses import dataclass
from typing import Any, Optional

@dataclass
class ShadowRecord:
    id: str
    parent_id: str
    kind: str
    payload: Any
    critical: bool
    uncertainty: float
    provenance: Any
    created_step: int
    ttl: Optional[int] = None
```

This is an interface sketch.

---

# 77. SHADOW STORE

A minimal Shadow store may support:

```text
put(record)
get(id)
find_by_parent(parent_id)
find_by_kind(kind)
promote(id)
expire(id)
tombstone(id)
```

Later implementations may add graph queries.

---

# 78. SHADOW AUDIT API

Suggested conceptual function:

```python
def audit_shadow(parent_id):
    records = shadow_store.find_by_parent(parent_id)

    return {
        "critical_unresolved": ...,
        "total_size": ...,
        "risk": ...,
        "expired": ...,
        "promotion_candidates": ...,
    }
```

This makes Shadow measurable.

---

# 79. EXPERIMENT A — NO SHADOW

Compare:

```text
Parent only
```

against:

```text
Parent + Shadow
```

on tasks with injected omitted terms.

Measure:

```text
reconstruction accuracy
error localization
final-answer accuracy
memory cost
```

---

# 80. EXPERIMENT B — SHADOW SIZE SWEEP

Vary Shadow budget:

```text
0%
10%
25%
50%
100%
```

of original local-state size.

Measure:

```text
accuracy
reconstruction
memory
reopen rate
```

This reveals the useful operating region.

---

# 81. EXPERIMENT C — CRITICAL VS RANDOM SHADOW

Store:

```text
critical residuals
```

versus:

```text
random residuals
```

under equal memory budget.

If critical selection does not outperform random selection, the prioritization policy is weak.

---

# 82. EXPERIMENT D — SHADOW PROMOTION

Create tasks where a residual is initially low-impact but later becomes important.

Measure whether the system promotes it before final failure.

This directly tests dynamic residual relevance.

---

# 83. EXPERIMENT E — SHADOW DECAY

Use tasks where residual relevance genuinely expires.

Compare:

```text
no decay
fixed TTL
risk-based decay
```

Measure memory savings and error rate.

---

# 84. EXPERIMENT F — SHADOW POINTERS

Compare:

```text
inline residual storage
```

against:

```text
external pointer storage
```

Measure:

```text
active context size
retrieval latency
audit success
```

---

# 85. EXPERIMENT G — SHADOW CORRUPTION

Corrupt or remove one Shadow record.

Check whether:

```text
checksum
certificate
or backward audit
```

detects the inconsistency.

This tests memory integrity.

---

# 86. EXPERIMENT H — SHADOW-OF-SHADOW

Create deep recursive compression.

Measure:

```text
shadow depth
memory growth
audit accuracy
```

This tests whether recursive residual storage becomes unstable.

---

# 87. PRIMARY SUCCESS CRITERIA

A useful Shadow system should:

1. improve reconstruction under fixed parent size;
2. reduce final error on residual-sensitive tasks;
3. preserve critical edges and branch identity;
4. allow local rather than global repair;
5. keep total memory below full-history storage for useful task classes;
6. support targeted retrieval;
7. expose unresolved information instead of hiding it.

---

# 88. FAILURE CONDITIONS

Shadow should be revised or rejected if:

1. total memory is usually equal to or larger than full history;
2. Shadow retrieval rarely helps;
3. critical residuals are often missed;
4. residual classification is unstable;
5. Shadow becomes an unstructured dump;
6. Shadow-of-Shadow grows without bound;
7. retrieval latency removes the benefit of local repair;
8. critical records are deleted by decay;
9. parent confidence remains high despite unresolved critical Shadow;
10. simpler checkpointing or graph storage performs equally well.

---

# 89. RESEARCH STATUS

```text
FACT:
Lossy compression creates residual information.

FACT:
Residual information may be necessary for reconstruction.

MODEL:
Store omitted task-relevant information in a typed Shadow layer.

MODEL:
Give Shadow explicit priority, lifetime, provenance,
risk, retrieval, and promotion rules.

HYPOTHESIS:
Explicit residual memory improves long-reasoning reliability
without requiring full active-history retention.

TEST:
Shadow budget, critical selection, promotion,
decay, corruption, pointer storage,
and recursive-Shadow experiments.
```

---

# 90. RELATION TO +3 / -3

The local cycle is now:

```text
ORIGINAL TRIAD
      |
      v
 +3 FORWARD
      |
      +----> Parent
      |
      +----> Shadow
                |
                v
          -3 BACKWARD
                |
                v
       reconstructed triad
                |
                v
             compare
```

Shadow is the explicit bridge between:

```text
compression
```

and:

```text
recoverability
```

---

# 91. WHAT COMES NEXT

We now have:

```text
state
simplex
couplings
+3 Forward
-3 Backward
Shadow
```

The next missing component is the decision mechanism that determines whether a candidate parent is allowed to move upward.

That mechanism is:

```text
GATE
```

---

# 92. NEXT FILE

Next:

```text
10_GATE_AND_HOLD_PROTOCOL.md
```

Its purpose is to formalize:

```text
reconstruction check
constraint check
coupling check
uncertainty check
Shadow check
resource check
```

and produce explicit verdicts:

```text
ALLOW
HOLD
EXPAND
RECOMPUTE
SHADOW
UNKNOWN
```

---

## FILE VERDICT

```text
STATE: CRYSTAL

DEFINED:
Shadow / Residual Memory

CORE:
compressed parent
+
explicit recoverable residual

SHADOW STORES:
omitted values
omitted edges
unresolved constraints
approximation remainder
branch ambiguity
provenance residue
boundary residue

CRITICAL RULE:
Shadow is not uncertainty
and not ordinary memory

NEXT:
10_GATE_AND_HOLD_PROTOCOL.md
```
