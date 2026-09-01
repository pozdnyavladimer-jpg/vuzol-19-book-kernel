# 04 — TRIANGLES INSIDE TRIANGLES

**Project:** Vuzol-19  
**Module:** Hexagram Simplicial Reasoning  
**Status:** HIERARCHICAL PROVENANCE SPEC  
**State:** CRYSTAL  
**Language:** English  
**Depends on:** `03_HEXAGRAM_STATE_MODEL.md`

---

## 0. PURPOSE

The previous file defined the outer Hexagram state:

```text
FORM = (Y, B, V)
FLOW = (R, O, G)
```

with explicit node values and coupling relations.

This file addresses the next problem:

> **Where did each outer state value come from?**

A flat value such as:

```text
R = 0.73
```

does not preserve its causal or computational provenance.

The proposed solution is:

> represent each state component as a recursively decomposable local triad.

This creates **triangles inside triangles**.

---

# 1. OUTER VALUE IS NOT ENOUGH

Suppose two reasoning states both produce:

```text
Pressure = 0.73
```

A flat representation sees:

```math
R_A = R_B = 0.73
```

and therefore:

```math
|R_A - R_B| = 0
```

But the histories may be different.

Example A:

```text
Pressure = 0.73
  |
  +-- external load       = 0.60
  +-- internal conflict   = 0.10
  +-- uncertainty         = 0.03
```

Example B:

```text
Pressure = 0.73
  |
  +-- external load       = 0.05
  +-- internal conflict   = 0.18
  +-- uncertainty         = 0.50
```

The same outer score hides different internal structure.

This is the **equifinality problem**.

---

# 2. HIERARCHICAL STATE IDEA

Instead of storing only:

```math
x \in \mathbb{R}
```

store:

```text
x
|
+-- child_1
+-- child_2
+-- child_3
```

Each child may itself be decomposed:

```text
x
|
+-- child_1
|    |
|    +-- child_11
|    +-- child_12
|    +-- child_13
|
+-- child_2
|
+-- child_3
```

This gives a recursive ternary structure.

---

# 3. LOCAL TRIAD

A local node is decomposed into three components:

```text
Parent
  |
  +-- A
  +-- B
  +-- C
```

The third component does not have to mean the same thing in every task.

Possible meanings:

```text
A = source
B = target
C = coupling
```

or:

```text
A = cause 1
B = cause 2
C = uncertainty
```

or:

```text
A = state
B = constraint
C = residual
```

The architecture defines the **triadic structure**.

The task defines the semantics.

---

# 4. RECURSIVE DECOMPOSITION

Let a parent node be:

```math
X^{(0)}
```

Its first-level decomposition is:

```math
X^{(0)}
\longrightarrow
\left(
X_1^{(1)},
X_2^{(1)},
X_3^{(1)}
\right)
```

Each child may then decompose:

```math
X_i^{(1)}
\longrightarrow
\left(
X_{i1}^{(2)},
X_{i2}^{(2)},
X_{i3}^{(2)}
\right)
```

and recursively:

```math
X_{i_1\dots i_k}^{(k)}
\longrightarrow
\left(
X_{i_1\dots i_k1}^{(k+1)},
X_{i_1\dots i_k2}^{(k+1)},
X_{i_1\dots i_k3}^{(k+1)}
\right)
```

This forms a ternary reasoning tree.

---

# 5. WHY THREE

The choice of three is motivated by the architecture developed here:

```text
node A
node B
relation / coupling
```

This is stronger than using only a pair:

```text
A <-> B
```

because the relation itself becomes an explicit local state.

The triad is therefore:

```text
A
B
R(A,B)
```

rather than only:

```text
A
B
```

This is a **MODEL CHOICE**, not a mathematical proof that every reasoning system must use three branches.

---

# 6. TRIANGLE AS A LOCAL CLOSURE UNIT

A local triad can be viewed as:

```text
             C
            / \
           /   \
          /     \
         A ----- B
```

where:

- `A` — first local state;
- `B` — second local state;
- `C` — coupling, constraint, or third state.

The important idea is:

> A local reasoning unit is considered more complete when the relation between its active components is represented explicitly.

---

# 7. BARYCENTRIC REPRESENTATION

A local triad may be mapped to barycentric coordinates:

```math
p=(a,b,c)
```

with:

```math
a,b,c \ge 0
```

and, for normalized shape:

```math
a+b+c=1
```

This places the local state on a standard 2-simplex.

The point inside the triangle represents relative contribution.

Example:

```math
p=(0.60,0.30,0.10)
```

means the first component dominates the local state.

---

# 8. SHAPE IS NOT MAGNITUDE

Two triads may have the same normalized shape:

```math
(0.6,0.3,0.1)
```

but different magnitude.

Example:

```text
Triad A:
(0.60, 0.30, 0.10)
total magnitude = 1.00
```

and:

```text
Triad B:
(6.0, 3.0, 1.0)
total magnitude = 10.0
```

After normalization, both have the same barycentric shape.

Therefore store:

```text
shape
+
magnitude
```

not shape alone.

---

# 9. NODE STATE CONTRACT

A minimal recursive node should carry:

```text
Node
|
+-- raw value
+-- normalized local coordinates
+-- magnitude
+-- children
+-- couplings
+-- provenance
+-- uncertainty
+-- Shadow
+-- certificate
```

Possible abstract structure:

```python
SimplicialNode(
    value=...,
    coords=(a, b, c),
    magnitude=...,
    children=[...],
    couplings={...},
    provenance=...,
    uncertainty=...,
    shadow=...,
    certificate=...,
)
```

---

# 10. PROVENANCE

Each node should record where it came from.

Possible provenance identifiers:

```text
source token range
source equation
source graph node
previous reasoning state
tool output
observation ID
memory node
```

A node without provenance may still be useful.

But a node with provenance can be audited.

This supports the question:

```text
Why does this state have this value?
```

---

# 11. PATH IDENTITY

A hierarchical node is identified not only by its value.

It may also be identified by its path.

Example:

```text
ROOT
 |
 +-- FLOW
      |
      +-- PRESSURE
           |
           +-- EXTERNAL
```

This path can be encoded as:

```text
FLOW/PRESSURE/EXTERNAL
```

or symbolically:

```math
\pi=(i_1,i_2,\dots,i_k)
```

The complete state may therefore depend on:

```math
X = X(v,\pi)
```

where:

- `v` — local value;
- `pi` — provenance path.

This makes equal values with different histories distinguishable.

---

# 12. PATH TOPOLOGY

Two states can have equal leaf values but different tree structure.

Example:

```text
State A

ROOT
 |
 +-- A
 |    |
 |    +-- X
 |
 +-- B
```

versus:

```text
State B

ROOT
 |
 +-- A
 |
 +-- B
      |
      +-- X
```

The leaf `X` exists in both.

Its location in the hierarchy differs.

This is why the architecture should compare:

```text
value
+
path
+
local neighborhood
```

rather than value alone.

---

# 13. EQUIFINALITY EXAMPLE

Consider two systems ending in:

```text
Balance = 0.80
```

State A:

```text
Balance
 |
 +-- low pressure
 +-- low flow
 +-- stable constraints
```

State B:

```text
Balance
 |
 +-- high pressure
 +-- high flow
 +-- active compensation
```

Both outer values are:

```math
G_A = G_B = 0.80
```

But they are not operationally equivalent.

State A may be naturally stable.

State B may require active control.

A flat representation hides this difference.

---

# 14. WHY THIS MATTERS FOR AI CONTROL

Suppose an AI sees:

```text
Balance = 0.80
```

and chooses:

```text
ALLOW
```

That may be safe for State A.

It may be unsafe for State B if the balance depends on temporary compensation.

Therefore a Gate may need to inspect:

```text
outer value
+
internal decomposition
```

before committing.

---

# 15. RECURSIVE DEPTH

Let decomposition depth be:

```math
d
```

At depth 0:

```text
1 node
```

At depth 1:

```text
3 nodes
```

At depth 2:

```text
9 nodes
```

At depth `d`:

```math
3^d
```

possible leaf positions in a full ternary tree.

This grows rapidly.

Therefore recursive decomposition requires stopping rules.

---

# 16. STOPPING RULES

A node should stop decomposing when one or more conditions are met.

Possible stopping criteria:

```text
1. uncertainty below threshold
2. reconstruction error below threshold
3. node is atomic for the task
4. further decomposition does not improve prediction
5. information gain is too small
6. maximum depth reached
7. compute budget reached
```

Formally:

```math
\mathrm{STOP}(X)
=
\mathbf{1}
[
q(X) \le \tau
]
```

for some task-specific quality function `q`.

---

# 17. ADAPTIVE DEPTH

Not all branches need equal depth.

Example:

```text
ROOT
 |
 +-- A
 |    |
 |    +-- deep decomposition
 |
 +-- B
 |
 +-- C
```

This is preferable when only one branch is uncertain.

Adaptive depth reduces unnecessary computation.

---

# 18. EXPAND ON FAILURE

If a Gate later detects a problem, the system may reopen a compressed node.

```text
Parent
  |
  v
Gate fails
  |
  v
EXPAND
  |
  v
restore child triad
```

Then only the local subtree is recomputed.

This is one of the intended advantages of hierarchical provenance.

---

# 19. LOCAL VS GLOBAL MEMORY

The architecture separates:

```text
local memory
```

from:

```text
global state
```

A parent stores a compact local summary.

The full reasoning tree stores how that summary was produced.

This gives two access modes:

```text
FAST:
use parent

AUDIT:
expand subtree
```

---

# 20. COMPRESSION WITHOUT ERASURE

The goal is not:

```text
child details
-> delete
-> parent
```

The goal is:

```text
child details
-> compress
-> parent
   |
   +-- retained summary
   +-- provenance pointer
   +-- Shadow
   +-- reconstruction certificate
```

This prepares the architecture for `+3 Forward` and `-3 Backward`.

---

# 21. TRIANGULAR NUMBERS — LIMITED ROLE

Triangular numbers are:

```math
T_n
=
\frac{n(n+1)}{2}
```

giving:

```text
1, 3, 6, 10, 15, 21, ...
```

Gauss's theorem states that every nonnegative integer can be represented as a sum of three triangular numbers.

This may inspire decomposition experiments.

However:

> It does not define a unique semantic or causal decomposition.

Therefore:

```text
14 = 10 + 3 + 1
```

may be used as a structural example.

It must not be treated as proof that the three parts are the true causes of `14`.

---

# 22. NON-UNIQUENESS

A decomposition method may produce multiple valid triads.

Therefore define a selection rule:

```math
D(X)
=
(X_1,X_2,X_3)
```

where `D` may optimize:

```text
reconstruction quality
constraint preservation
information gain
causal relevance
predictive value
compression efficiency
```

The decomposition rule is part of the model.

It cannot be left implicit.

---

# 23. LEARNED DECOMPOSITION

A learned decomposition model may use:

```math
(X_1,X_2,X_3)
=
D_{\theta}(X)
```

where `D_theta` is trained to preserve task-relevant information.

A training objective may combine:

```math
\mathcal{L}
=
\lambda_1 \mathcal{L}_{\mathrm{rec}}
+
\lambda_2 \mathcal{L}_{\mathrm{task}}
+
\lambda_3 \mathcal{L}_{\mathrm{constraint}}
+
\lambda_4 \mathcal{L}_{\mathrm{compression}}
```

The exact objective remains experimental.

---

# 24. INFORMATION GAIN

A child split should ideally reveal useful structure.

Let parent uncertainty be:

```math
U(X)
```

and weighted child uncertainty be:

```math
U_{\mathrm{children}}
```

Then a simple information-gain signal is:

```math
IG
=
U(X)
-
U_{\mathrm{children}}
```

If:

```math
IG \approx 0
```

the split may not be useful.

This can help stop infinite recursive decomposition.

---

# 25. COUPLING INSIDE EACH SUBTRIANGLE

Each local triad may also carry internal edge states:

```text
A <-> B
B <-> C
C <-> A
```

Thus recursion happens over:

```text
nodes
and
relations
```

not nodes alone.

A recursive node is therefore better thought of as a small local graph.

---

# 26. HIGHER-ORDER LOCAL STATE

A triangle contains more than three scalar vertices.

A local state may include:

```math
T
=
(V,E,F)
```

where:

- `V` — vertex values;
- `E` — edge relations;
- `F` — triangle-level aggregate state.

This avoids reducing the triangle to a list of three numbers.

---

# 27. TWO TYPES OF RECURSION

The architecture may use two different recursive operations.

### Type A — semantic decomposition

```text
Pressure
-> external
-> internal
-> uncertainty
```

### Type B — computational grouping

```text
operation 1
operation 2
coupling
-> parent result
```

These should not be confused.

One decomposes meaning.

The other restructures computation.

Both can use the same node interface.

---

# 28. MINIMAL EXAMPLE — MATHEMATICAL REASONING

Suppose a local reasoning state is:

```text
Limit behavior
```

Decompose:

```text
Limit behavior
 |
 +-- base behavior
 +-- exponent behavior
 +-- rate coupling
```

For:

```math
\left(1-\frac{3}{n+5}\right)^{3n}
```

this becomes:

```text
base behavior:
1 + epsilon_n

exponent behavior:
3n

coupling:
3n * epsilon_n
```

The coupling preserves the information that determines the final limit.

This is a concrete example of a triangle whose third component is a relation.

---

# 29. MINIMAL EXAMPLE — SOFTWARE REASONING

Suppose:

```text
Service instability
```

decomposes into:

```text
Service instability
 |
 +-- request pressure
 +-- retry activity
 +-- queue coupling
```

A high request rate is not sufficient to predict failure.

A high retry rate is not sufficient either.

The coupling between them may create overload.

Again:

```text
meaning can live in the relation
```

---

# 30. DISTANCE BETWEEN HIERARCHICAL STATES

A flat distance may be:

```math
d_{\mathrm{flat}}
=
\|z_A-z_B\|
```

A hierarchical distance should also consider structure.

Abstractly:

```math
d_{\mathrm{tree}}
=
\alpha d_{\mathrm{value}}
+
\beta d_{\mathrm{path}}
+
\gamma d_{\mathrm{coupling}}
+
\delta d_{\mathrm{residual}}
```

The exact metric is an open design choice.

Candidates may include:

- tree edit distance;
- optimal transport;
- Wasserstein-style distances;
- graph matching;
- learned metric functions.

---

# 31. WASSERSTEIN IDEA — STATUS

If node masses are interpreted as distributions over tree locations, an optimal-transport distance may compare how much "mass" must move between causal structures.

This is mathematically plausible.

But:

> Wasserstein distance is not automatically the correct metric for all causal trees.

It should be tested against simpler metrics.

---

# 32. MEMORY COST

A recursive tree can become much larger than a flat state.

Therefore measure:

```math
C_{\mathrm{mem}}
=
\mathrm{size}(\mathcal{T})
```

and compare against:

```text
flat 6D
summary memory
full reasoning trace
dependency graph
```

The method is useful only if the added structure buys measurable reliability.

---

# 33. COMPRESSION RATIO

For a subtree `T` compressed into parent state `P`:

```math
\rho
=
\frac{
\mathrm{size}(P+\mathrm{Shadow}+\mathrm{certificate})
}{
\mathrm{size}(T)
}
```

Desired:

```math
\rho < 1
```

while preserving acceptable reconstruction and task performance.

If:

```math
\rho \ge 1
```

then the architecture may be preserving too much detail to count as compression.

---

# 34. FAILURE CONDITIONS

The recursive triangle model should be revised or rejected if:

1. equal outer states do not benefit from provenance;
2. decomposition is unstable under paraphrase;
3. tree memory grows faster than its reasoning benefit;
4. learned decomposition produces arbitrary branches;
5. edge relations do not improve task performance;
6. stopping rules are unreliable;
7. recursive expansion causes uncontrolled compute growth;
8. simpler graph representations perform equally well;
9. Shadow must store nearly the entire subtree;
10. hierarchical distance adds no useful discrimination.

---

# 35. EXPERIMENT A — EQUIFINALITY

Create pairs with equal outer labels but different hidden causes.

Example:

```text
A:
high balance caused by low pressure

B:
high balance caused by active compensation
```

Ask the model to choose a control action.

Compare:

```text
flat outer score
vs
hierarchical provenance
```

Success means provenance improves action selection.

---

# 36. EXPERIMENT B — PATH SWAP

Create two trees with the same leaf values but swap branch positions.

If the task says branch identity matters, the model should detect the difference.

This tests whether the architecture preserves path identity rather than only a multiset of values.

---

# 37. EXPERIMENT C — DEPTH ABLATION

Compare maximum depths:

```text
d = 0
d = 1
d = 2
d = 3
adaptive
```

Measure:

- accuracy;
- memory;
- latency;
- reconstruction quality.

This identifies whether deeper recursion actually helps.

---

# 38. EXPERIMENT D — THIRD COMPONENT ABLATION

Compare triads where the third component is:

```text
A — uncertainty
B — coupling
C — residual
D — learned latent
```

The goal is to determine what the third vertex should represent for each task class.

---

# 39. RESEARCH STATUS

```text
FACT:
A 2-simplex can represent three normalized components.

MODEL:
Represent a state component as a recursively decomposable triad.

MODEL:
Preserve path identity and local edge relations.

HYPOTHESIS:
Hierarchical provenance improves decisions
when equal outer states have different histories.

TEST:
Equifinality, path-swap, depth, memory-cost,
and third-component ablation experiments.
```

---

# 40. TRANSITION TO THE NEXT FILE

This file introduced recursive triads conceptually.

The next file must formalize the mathematical coordinate system used inside each triangle.

That requires a precise treatment of:

```text
barycentric coordinates
magnitude
mass
normalization
distance
reconstruction
```

---

# 41. NEXT FILE

Next:

```text
05_BARYCENTRIC_SIMPLEX_SPACE.md
```

Its purpose is to define the local simplex mathematically and prevent a critical mistake:

> `a + b + c = 1` must not be confused with "no information was lost."

The next file will separate:

```text
shape
magnitude
mass
residual
```

as distinct quantities.

---

## FILE VERDICT

```text
STATE: CRYSTAL

DEFINED:
Triangles Inside Triangles

CORE:
outer value
-> local triad
-> recursive sub-triads
-> provenance path
-> edge memory
-> adaptive depth

KEY CLAIM:
equal outer values may represent different internal histories

NOT CLAIMED:
three branches are universally optimal
triangular numbers define true causes

NEXT:
05_BARYCENTRIC_SIMPLEX_SPACE.md
```
