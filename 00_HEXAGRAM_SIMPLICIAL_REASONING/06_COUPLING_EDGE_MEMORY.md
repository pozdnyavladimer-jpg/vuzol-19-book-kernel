# 06 — COUPLING / EDGE MEMORY

**Project:** Vuzol-19  
**Module:** Hexagram Simplicial Reasoning  
**Status:** RELATION-PRESERVATION SPEC  
**State:** CRYSTAL  
**Language:** English  
**Depends on:** `05_BARYCENTRIC_SIMPLEX_SPACE.md`

---

## 0. PURPOSE

The previous file defined the local simplex state:

```text
shape
+ magnitude
+ sign
+ edge state
+ uncertainty
+ provenance
+ Shadow
+ certificate
```

This file focuses on one critical component:

> **The relation between nodes may contain information that is not recoverable from node values alone.**

The architecture therefore treats edges / couplings as first-class memory.

This is called **Coupling / Edge Memory**.

---

# 1. NODE MEMORY IS NOT ENOUGH

A flat state may store:

```text
A = value_A
B = value_B
C = value_C
```

But many tasks depend on:

```text
A affects B
B constrains C
C feeds back into A
```

Therefore the reasoning state is not only a set of nodes.

It is at least:

```text
nodes
+
relations
```

Formally:

```math
G=(V,E)
```

where:

- `V` — node set;
- `E` — edge set.

---

# 2. SAME NODES, DIFFERENT SYSTEM

Consider two systems with identical node values.

System A:

```text
A = 1
B = 1

A -> B
```

System B:

```text
A = 1
B = 1

A -| B
```

The node values are equal.

The relation differs.

If:

```text
->  means excitation
-|  means inhibition
```

then the two systems are not operationally equivalent.

Therefore:

```math
V_A=V_B
```

does not imply:

```math
G_A=G_B
```

---

# 3. EDGE AS A FIRST-CLASS STATE

Represent an edge as:

```math
e_{ij}
=
(i,j,r,w,d,u,p)
```

where:

- `i` — source node;
- `j` — target node;
- `r` — relation type;
- `w` — relation strength;
- `d` — direction;
- `u` — uncertainty;
- `p` — provenance.

This is a general interface.

Not every task requires every field.

---

# 4. RELATION TYPES

Possible edge semantics include:

```text
causal
constraint
temporal
algebraic
rate
logical
resource
dependency
inhibition
activation
equivalence
approximation
ownership
reference
```

The type must be explicit.

Do not collapse all relations into one generic scalar if the task depends on their meaning.

---

# 5. DIRECTED EDGE

A directed edge is:

```math
A \rightarrow B
```

with state:

```math
e_{AB}
```

In general:

```math
e_{AB}
\ne
e_{BA}
```

This matters for:

- causality;
- forward computation;
- influence;
- dependency;
- control.

---

# 6. UNDIRECTED EDGE

Some relations may be symmetric:

```math
A \leftrightarrow B
```

Then:

```math
e_{AB}
=
e_{BA}
```

Examples may include:

- distance;
- compatibility;
- similarity;
- undirected physical connection.

The model should not assume symmetry by default.

---

# 7. EDGE MATRIX

For three local nodes:

```text
A
B
C
```

define a directed coupling matrix:

```math
K
=
\begin{bmatrix}
0      & k_{AB} & k_{AC} \\
k_{BA} & 0      & k_{BC} \\
k_{CA} & k_{CB} & 0
\end{bmatrix}
```

This matrix contains local influence strengths.

If relations have different types, use multiple channels:

```math
K^{(1)},K^{(2)},\dots,K^{(m)}
```

or an edge feature tensor.

---

# 8. MULTI-RELATIONAL EDGE TENSOR

For `m` relation types:

```math
\mathcal{K}
\in
\mathbb{R}^{3\times3\times m}
```

Example channels:

```text
channel 1 — causal
channel 2 — constraint
channel 3 — temporal
channel 4 — uncertainty
```

This prevents one scalar from mixing incompatible meanings.

---

# 9. RATE COUPLING

A particularly important edge type is **rate coupling**.

Suppose:

```math
a_n \to a
```

and:

```math
b_n \to b
```

The final behavior may depend on how fast those limits are approached.

The crucial state may be:

```math
c_n
=
f(a_n,b_n)
```

rather than either endpoint alone.

This is exactly what happens in indeterminate forms.

---

# 10. EXAMPLE — INDETERMINATE LIMIT

Consider:

```math
L
=
\lim_{n\to\infty}
\left(
1-\frac{3}{n+5}
\right)^{3n}
```

Node states:

```text
base     -> 1
exponent -> infinity
```

These alone produce:

```math
1^{\infty}
```

which is indeterminate.

Define:

```math
\varepsilon_n
=
-\frac{3}{n+5}
```

The decisive coupling is:

```math
c_n
=
3n\varepsilon_n
```

and:

```math
c_n
=
-\frac{9n}{n+5}
\to -9
```

Therefore:

```math
L=e^{-9}
```

The final answer is controlled by the **edge relationship between rates**.

---

# 11. EDGE MEMORY LESSON FROM THE LIMIT

If the reasoning state stores only:

```text
base = 1
exponent = infinity
```

the critical information is gone.

A coupling-aware state stores:

```text
base
exponent
rate coupling
```

The local triad becomes:

```text
          rate coupling
             /     \
            /       \
         base ----- exponent
```

This is a concrete justification for making the third local component a relation.

---

# 12. CONSTRAINT COUPLING

Another edge type is:

```text
node <-> constraint
```

Example:

```text
x = -2
```

may be numerically valid.

But if the active domain constraint is:

```math
x>0
```

then the state is invalid.

The value alone is insufficient.

The edge:

```text
x --satisfies?--> constraint
```

must be retained.

---

# 13. TEMPORAL COUPLING

Some relations depend on order.

Example A:

```text
heat
-> deform
-> cool
```

Example B:

```text
cool
-> deform
-> heat
```

The same operations appear.

The sequence differs.

Therefore store temporal relation:

```math
t(A)<t(B)
```

or explicit transition edges.

A bag of nodes cannot distinguish the two.

---

# 14. LOGICAL COUPLING

Consider:

```text
A is true
B is true
```

This does not determine whether:

```text
A AND B
A OR B
A IMPLIES B
A EXCLUDES B
```

is active.

Logical relation type is part of the state.

---

# 15. APPROXIMATION EDGE

Scientific reasoning often uses:

```math
A \approx B
```

rather than exact equality.

An approximation edge should carry:

```text
error tolerance
validity region
assumptions
provenance
```

Example:

```math
\log(1+\varepsilon)
\approx
\varepsilon
```

is only safe under a small-`epsilon` condition.

The approximation relation must therefore remember its domain of validity.

---

# 16. EDGE CERTIFICATE

Each important edge may carry a certificate:

```text
EdgeCertificate
|
+-- relation type
+-- source
+-- assumptions
+-- tolerance
+-- verification status
+-- uncertainty
```

This allows later Gate logic to inspect relations, not only nodes.

---

# 17. COUPLING STRENGTH

For quantitative tasks, an edge may have strength:

```math
w_{ij}
```

Possible meanings:

- derivative sensitivity;
- correlation;
- causal effect;
- resource dependency;
- influence score;
- constraint weight.

The semantics of `w_ij` must be declared.

---

# 18. SENSITIVITY AS COUPLING

For a function:

```math
y=f(x)
```

local sensitivity is:

```math
\frac{\partial y}{\partial x}
```

This can be treated as an edge state.

For multiple variables:

```math
J_{ij}
=
\frac{\partial F_i}{\partial x_j}
```

the Jacobian acts as a local coupling map.

This gives a rigorous bridge between:

```text
edge memory
```

and:

```text
error propagation
```

---

# 19. ERROR PROPAGATION THROUGH EDGES

For:

```math
x_{k+1}=F_k(x_k)
```

small perturbations propagate approximately through:

```math
\delta x_{k+1}
\approx
J_k\delta x_k
```

The edge sensitivity is therefore part of the path by which error moves.

A local audit may prioritize edges with large sensitivity.

---

# 20. EDGE RISK SCORE

Define a possible edge risk:

```math
R_e
=
|w_e|\,U_e\,I_e
```

where:

- `w_e` — influence magnitude;
- `U_e` — uncertainty;
- `I_e` — importance / downstream impact.

High-risk edges may trigger:

```text
EXPAND
RECHECK
HOLD
```

This is a **MODEL**, not a universal formula.

---

# 21. EDGE PROVENANCE

Every critical relation should point to its source.

Possible provenance:

```text
equation number
constraint statement
tool result
previous node pair
dataset row
source paragraph
reasoning step
```

If a relation cannot be traced back, it should have lower confidence.

---

# 22. EDGE LIFETIME

Some relations are temporary.

Example:

```text
constraint valid only during phase 2
```

Therefore an edge may carry:

```text
start_step
end_step
activation condition
```

This prevents stale constraints from remaining active forever.

---

# 23. DYNAMIC EDGE STATE

Let:

```math
e_{ij}^{(t)}
```

denote the relation at time `t`.

Then:

```math
e_{ij}^{(t)}
\to
e_{ij}^{(t+1)}
```

may change while nodes remain stable.

This is important for transition reasoning.

---

# 24. EDGE-FIRST TRANSITION

Example:

```text
Node values stay constant.
```

But:

```text
t0:
A supports B

t1:
A blocks B
```

Then:

```math
V_t \approx V_{t+1}
```

but:

```math
E_t \ne E_{t+1}
```

A node-only memory misses the transition.

---

# 25. COUPLING DELTA

Define edge change:

```math
\Delta K_t
=
K_{t+1}-K_t
```

A large:

```math
\|\Delta K_t\|
```

may signal:

- phase transition;
- branch switch;
- rule change;
- topology change;
- control reversal.

This can become a Gate trigger.

---

# 26. EDGE TOPOLOGY

The relation graph may also change structurally.

Example:

```text
Before:
A -> B -> C
```

After:

```text
A -> C
B disconnected
```

This is not just a weight change.

It is a topology change in the dependency graph.

The architecture should distinguish:

```text
edge-weight deformation
```

from:

```text
edge creation / deletion
```

---

# 27. EDGE CREATION

A new relation may appear when previously independent variables become coupled.

Represent:

```text
NO EDGE
```

changing to:

```text
ACTIVE EDGE
```

with provenance.

The creation event itself may be important memory.

---

# 28. EDGE DELETION

Deleting an edge can be dangerous.

Before removal, store:

```text
why the edge was removed
what condition invalidated it
whether it may return
whether its information enters Shadow
```

Silent edge deletion is a major failure mode.

---

# 29. SHADOW FOR EDGES

If an edge is removed during compression, preserve a residual representation:

```text
retained graph
+
edge Shadow
```

Example:

```text
original:
A -> B
B -> C
A -> C

compressed:
A -> C

Shadow:
A -> B
B -> C
```

Later backward audit can test whether the compressed direct edge preserves the two-step relation.

---

# 30. EDGE RECONSTRUCTION

Let original edges be:

```math
E
```

and reconstructed edges:

```math
\hat{E}
```

Define edge reconstruction error.

For weighted matrices:

```math
E_{\mathrm{edge}}
=
\|K-\hat{K}\|_F
```

where `||.||_F` is the Frobenius norm.

For discrete edge sets, use precision / recall style metrics.

---

# 31. EDGE RETENTION SCORE

Given ground-truth edge set:

```math
E^*
```

and retained / reconstructed edge set:

```math
\hat{E}
```

define recall:

```math
R_{\mathrm{edge}}
=
\frac{
|E^*\cap\hat{E}|
}{
|E^*|
}
```

This measures how many required relations survived.

---

# 32. EDGE PRECISION

Also define:

```math
P_{\mathrm{edge}}
=
\frac{
|E^*\cap\hat{E}|
}{
|\hat{E}|
}
```

High recall with low precision means the system keeps many spurious relations.

Both matter.

---

# 33. EDGE F1

Combine precision and recall:

```math
F1_{\mathrm{edge}}
=
2
\frac{
P_{\mathrm{edge}}R_{\mathrm{edge}}
}{
P_{\mathrm{edge}}+R_{\mathrm{edge}}
}
```

when the denominator is nonzero.

This provides one compact edge-memory metric.

---

# 34. CRITICAL EDGE SET

Not all edges are equally important.

Define:

```math
E_{\mathrm{critical}}
\subseteq
E
```

Critical edges may include:

- hard constraints;
- rate couplings;
- causal dependencies;
- irreversible transitions;
- safety boundaries.

Compression should prioritize preserving these.

---

# 35. EDGE PRIORITY

A simple priority model:

```math
P_e
=
f(
\mathrm{impact},
\mathrm{uncertainty},
\mathrm{constraint\ status},
\mathrm{irreversibility}
)
```

High-priority edges should resist compression.

This is a routing mechanism for memory allocation.

---

# 36. EDGE BOTTLENECK

A long reasoning task may fail because one relation has extremely high downstream importance.

Example:

```text
many nodes
many relations
one forgotten hard constraint
```

The architecture should detect such bottleneck edges.

Possible signal:

```math
B_e
=
\text{downstream dependency count}
```

or graph centrality.

---

# 37. GRAPH CENTRALITY — OPTIONAL

Possible graph metrics:

```text
degree
betweenness
PageRank-like influence
path count
separator importance
```

These may help decide which relations should be preserved.

They are optional.

Task semantics should dominate generic graph metrics.

---

# 38. COUPLING AND TREEWIDTH

Some graphs compress easily into local triads.

Others have many cross-connections.

A graph with heavy cross-coupling may resist clean ternary decomposition.

This is important.

The architecture should not assume every dependency graph can be reduced efficiently.

Relevant structural difficulty may be related to:

```text
graph separators
treewidth
cross-level edges
```

This sets a real limitation on hierarchical compression.

---

# 39. CROSS-TRIAD EDGE

Suppose two local triangles exist:

```text
Triangle A
Triangle B
```

A relation may connect a node in A to a node in B.

If compression treats triangles independently, that edge may disappear.

Therefore each parent must track:

```text
internal edges
+
external boundary edges
```

before compression.

---

# 40. BOUNDARY EDGE SET

For a subtree `T`, define:

```math
\partial E(T)
```

as edges connecting nodes inside `T` to nodes outside `T`.

A compressed parent must preserve enough information about:

```math
\partial E(T)
```

to remain compatible with the rest of the reasoning graph.

This is crucial.

---

# 41. LOCAL COMPRESSION CONTRACT

Before compressing a triad into a parent:

```text
children
+
internal edges
+
boundary edges
```

must be summarized.

The parent should carry:

```text
internal summary
boundary interface
Shadow
certificate
```

This is similar to a software module exposing an interface while hiding internals.

---

# 42. PARENT INTERFACE

A parent node may expose:

```text
ParentInterface
|
+-- output state
+-- required inputs
+-- active constraints
+-- boundary couplings
+-- uncertainty
+-- reconstruction handle
```

This allows higher layers to reason without reopening the full subtree.

---

# 43. EDGE CONSISTENCY CHECK

Suppose the parent claims:

```text
A causes C
```

while the children encode:

```text
A inhibits B
B causes C
```

The compressed edge may not preserve the true relation.

Therefore later `+3 Forward` must compute edge-level consistency.

This file defines the need.

The operator will be formalized later.

---

# 44. COMPOSITION OF EDGES

Some edge relations can compose.

Example:

```math
A \xrightarrow{f} B
```

and:

```math
B \xrightarrow{g} C
```

may produce:

```math
A \xrightarrow{g\circ f} C
```

This is safe only when the relation type supports composition.

Do not assume arbitrary edges compose.

---

# 45. NON-COMPOSABLE EDGE

Example:

```text
A similar-to B
B causes C
```

does not automatically imply:

```text
A causes C
```

Therefore every relation type should define whether composition is legal.

This avoids false transitive inference.

---

# 46. EDGE TYPE CONTRACT

Each relation type should declare:

```text
directed?
symmetric?
transitive?
composable?
invertible?
lossy?
constraint-bearing?
time-dependent?
```

This can later become a typed edge system.

---

# 47. REVERSE EDGE

For an edge:

```math
A \xrightarrow{f} B
```

the reverse relation may or may not exist.

If an inverse exists:

```math
B \xrightarrow{f^{-1}} A
```

it may still be unstable or ambiguous.

Therefore `-3 Backward` must not assume every edge is invertible.

---

# 48. MANY-TO-ONE EDGE

A function may compress multiple states into one output.

Example:

```math
y=x^2
```

Both:

```math
x=2
```

and:

```math
x=-2
```

produce:

```math
y=4
```

The reverse edge is ambiguous.

This is a concrete equifinality case.

Shadow or provenance is required to recover the original branch.

---

# 49. EDGE UNCERTAINTY

Each relation may carry:

```math
U_e\in[0,1]
```

Two identical node values with different edge confidence should not be treated identically.

Example:

```text
A -> B
confidence = 0.95
```

versus:

```text
A -> B
confidence = 0.20
```

Gate logic should be able to distinguish them.

---

# 50. EDGE MEMORY COST

Explicit relations increase memory.

For `n` nodes, dense pairwise storage may scale as:

```math
O(n^2)
```

This is unacceptable for large systems.

Therefore the architecture should prefer sparse edge storage.

---

# 51. SPARSE EDGE MEMORY

Store only:

```text
active
critical
high-information
or high-confidence
```

relations.

A sparse graph may require roughly:

```math
O(|E|)
```

memory.

The goal is to preserve structure without constructing a fully connected graph.

---

# 52. EDGE PRUNING

Edges may be pruned if they are:

```text
low influence
redundant
low confidence
reconstructable
irrelevant to current task
```

But pruning must create a Shadow record when the relation may matter later.

---

# 53. EDGE COMPRESSION RATIO

Let original local edge state size be:

```math
S_E
```

and compressed edge interface size:

```math
\hat{S}_E
```

Define:

```math
\rho_E
=
\frac{
\hat{S}_E
}{
S_E
}
```

This should be evaluated together with edge reconstruction error.

---

# 54. RATE-DISTORTION FOR EDGES

The same tradeoff applies:

```text
less edge memory
<-> more relation distortion
```

A good compression policy preserves the relations most important to future reasoning.

---

# 55. EDGE PREDICTIVE VALUE

A relation is useful if it helps predict:

```text
next state
constraint violation
branch outcome
error propagation
required action
```

Therefore edge retention should be driven partly by downstream predictive value.

---

# 56. MINIMAL SOFTWARE EXAMPLE

Nodes:

```text
request_rate
retry_rate
queue_length
```

Same node values:

```text
request_rate = high
retry_rate   = high
queue_length = medium
```

Case A:

```text
retries are rate-limited
```

Case B:

```text
retries amplify request load
```

The node values are identical.

The coupling structure differs.

Only Case B may trigger runaway overload.

---

# 57. MINIMAL LOGIC EXAMPLE

Nodes:

```text
A = true
B = true
```

Case A:

```text
rule = A AND B
```

Case B:

```text
rule = A XOR B
```

Same node truth values.

Different relation rule.

Outputs differ.

This is an exact demonstration that nodes alone are insufficient.

---

# 58. MINIMAL PHYSICS-STYLE EXAMPLE

Suppose:

```text
position
velocity
```

remain numerically similar.

But the force coupling changes sign.

The future trajectory changes.

Thus:

```text
state values
+
dynamical coupling
```

are both required for prediction.

---

# 59. EXPERIMENT A — SAME NODES, DIFFERENT EDGES

Construct paired tasks with identical node values but different relations.

Compare:

```text
node-only model
vs
node + edge model
```

Success criterion:

```text
edge-aware model chooses the correct outcome
significantly more often
```

---

# 60. EXPERIMENT B — EDGE DELETION

Start with a valid dependency graph.

Randomly remove one critical edge.

Measure whether the architecture:

```text
detects inconsistency
requests EXPAND
or produces wrong output
```

This directly tests edge integrity.

---

# 61. EXPERIMENT C — RATE COUPLING

Use indeterminate limits and asymptotic problems where endpoint values are insufficient.

Compare:

```text
node-only summary
vs
explicit rate coupling
```

Measure exact-answer accuracy.

---

# 62. EXPERIMENT D — CONSTRAINT EDGE

Give tasks where the arithmetic is correct but one hidden domain constraint invalidates the answer.

Measure whether explicit constraint edges reduce invalid commits.

---

# 63. EXPERIMENT E — TEMPORAL ORDER

Use tasks with identical operations in different orders.

If the model stores only operation nodes, it may confuse them.

Explicit temporal edges should resolve the difference.

---

# 64. EXPERIMENT F — EDGE SHADOW

Compress a multi-step path:

```text
A -> B -> C
```

into:

```text
A -> C
```

Store the intermediate path in Shadow.

Then ask the system to reconstruct:

```text
B
```

Measure reconstruction accuracy and memory cost.

---

# 65. FAILURE CONDITIONS

Coupling / Edge Memory should be revised or simplified if:

1. explicit edges do not improve edge-sensitive tasks;
2. dense edge storage becomes too expensive;
3. learned edge types are unstable;
4. critical edges cannot be identified reliably;
5. edge Shadow stores nearly the entire original graph;
6. simple dependency graphs perform equally well;
7. relation typing adds complexity without measurable gain;
8. boundary edges are routinely lost during local compression;
9. reverse edge reconstruction remains unreliable;
10. graph decomposition cost exceeds reasoning benefit.

---

# 66. RESEARCH STATUS

```text
FACT:
Graph-structured systems require both nodes and edges.

FACT:
Different edge structures can produce different behavior
with identical node values.

MODEL:
Store critical relations as explicit Coupling / Edge Memory.

MODEL:
Preserve internal and boundary edges during local compression.

HYPOTHESIS:
Explicit edge memory improves long reasoning
when answers depend on rates, constraints,
causality, order, or other relations.

TEST:
Same-node/different-edge,
edge deletion,
rate coupling,
constraint edge,
temporal order,
and edge Shadow experiments.
```

---

# 67. TRANSITION TO THE NEXT FILE

This file defined what must be preserved before compression:

```text
nodes
+
couplings
+
boundary interface
+
uncertainty
+
provenance
```

The next file defines the actual forward operator that turns a local triad into a parent node.

That operator is:

```text
+3 FORWARD
```

---

# 68. NEXT FILE

Next:

```text
07_PLUS3_FORWARD_OPERATOR.md
```

Its purpose is to formalize:

```text
(X1, X2, X3, Couplings)
          |
          v
local synthesis
          |
          v
Parent
+ retained interface
+ Shadow
+ certificate
+ uncertainty
```

The key requirement will be:

> compression must be explicit about what is retained, what is transformed, and what is moved into Shadow.

---

## FILE VERDICT

```text
STATE: CRYSTAL

DEFINED:
Coupling / Edge Memory

CORE:
node values
+
edge relations
+
boundary edges
+
relation type
+
direction
+
uncertainty
+
provenance

CRITICAL RULE:
some answers live in relations,
not in endpoint values

NEXT:
07_PLUS3_FORWARD_OPERATOR.md
```
