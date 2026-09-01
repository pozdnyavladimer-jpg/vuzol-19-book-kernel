# 07 — +3 FORWARD OPERATOR

**Project:** Vuzol-19  
**Module:** Hexagram Simplicial Reasoning  
**Status:** FORWARD COMPRESSION / LOCAL SYNTHESIS SPEC  
**State:** CRYSTAL  
**Language:** English  
**Depends on:** `06_COUPLING_EDGE_MEMORY.md`

---

## 0. PURPOSE

The previous files defined:

```text
node state
+
simplex coordinates
+
magnitude
+
sign
+
coupling / edge memory
+
provenance
+
uncertainty
+
Shadow
+
certificate
```

This file defines the first active reasoning operator:

```text
+3 FORWARD
```

Its purpose is:

> **take a local triad of reasoning states and produce a higher-level parent without silently erasing the information required for later audit.**

The operator is a **MODEL**.

It must be tested against simpler aggregation methods.

---

# 1. BASIC FORM

Let the local triad be:

```math
X
=
(X_1,X_2,X_3)
```

with local edge state:

```math
E
```

The forward operator is:

```math
F_{+3}:
(X_1,X_2,X_3,E)
\longrightarrow
P
```

where `P` is the parent node.

A parent is not only a compressed scalar.

Recommended structure:

```math
P
=
(z,S,C,U,M,E_{\partial},P_{\mathrm{prov}})
```

where:

- `z` — retained compressed state;
- `S` — Shadow / residual;
- `C` — certificate / invariants;
- `U` — uncertainty;
- `M` — magnitude / scale metadata;
- `E_partial` — retained boundary couplings;
- `P_prov` — provenance pointer.

---

# 2. CORE TRIAD

The local unit is:

```text
            X3
           /  \
          /    \
         /      \
       X1 ------ X2
```

The third component may represent:

```text
a third state
a constraint
a coupling
a residual
an uncertainty source
a task-specific relation
```

The architecture does **not** require that `X3` always have the same semantic role.

The decomposition policy must declare the role.

---

# 3. FORWARD SYNTHESIS IS NOT SIMPLE AVERAGING

A naive compressor may use:

```math
z
=
\frac{X_1+X_2+X_3}{3}
```

This is useful as a toy baseline.

But it can erase:

- sign;
- direction;
- graph structure;
- constraint status;
- provenance;
- edge asymmetry;
- rare but critical residual terms.

Therefore the real `+3 Forward` operator must be task-aware.

---

# 4. OPERATOR CONTRACT

The operator should produce five logically separate outputs:

```text
1. RETAINED STATE
2. RETAINED INTERFACE
3. SHADOW
4. CERTIFICATE
5. UNCERTAINTY
```

Conceptually:

```text
children + internal edges + boundary edges
                  |
                  v
              +3 FORWARD
                  |
      +-----------+-----------+
      |           |           |
      v           v           v
   Parent       Shadow    Certificate
      |
      v
Boundary Interface
```

---

# 5. INPUT CONTRACT

Each child should expose at least:

```text
value
shape
magnitude
sign
uncertainty
provenance
internal certificate
active boundary edges
```

A minimal abstract input:

```python
ChildState(
    value=...,
    shape=...,
    magnitude=...,
    sign=...,
    uncertainty=...,
    provenance=...,
    certificate=...,
    edges=...,
)
```

---

# 6. LOCAL GRAPH INPUT

The forward operator acts not only on three child nodes but on the induced local graph.

Define:

```math
G_T
=
(V_T,E_T)
```

where:

```math
V_T
=
\{X_1,X_2,X_3\}
```

and `E_T` contains all retained local relations.

The operator input is therefore better written as:

```math
F_{+3}(G_T,\partial E_T)
```

where `partial E_T` denotes edges from the triad to the external graph.

---

# 7. BOUNDARY INTERFACE

When a local triad is compressed, external dependencies must survive.

For subtree `T`, define its boundary edges:

```math
\partial E(T)
```

A parent must expose a compact interface:

```text
ParentInterface
|
+-- required incoming information
+-- outgoing effects
+-- active constraints
+-- unresolved couplings
+-- uncertainty
```

The parent is valid only if higher layers can use this interface without reopening the subtree immediately.

---

# 8. RETAINED STATE

The compressed state `z` may be:

```text
a scalar
a small vector
a six-axis GSL state
a simplex point
a learned latent
a symbolic object
```

The architecture does not force one representation.

The rule is:

> `z` must be smaller or more useful than the raw children while preserving task-relevant information.

---

# 9. FORWARD MAP

General form:

```math
z
=
f_{\theta}
(
X_1,
X_2,
X_3,
E_T,
\partial E_T
)
```

where `f_theta` may be:

```text
symbolic
hand-designed
learned
hybrid
```

The first prototype should preferably be simple and inspectable.

---

# 10. SIMPLE SYMBOLIC VERSION

For arithmetic-style tasks:

```text
X1 = operand A
X2 = operand B
X3 = operator / relation
```

Then:

```math
z
=
X_3(X_1,X_2)
```

Example:

```text
X1 = 4
X2 = 7
X3 = addition
```

produces:

```math
z=11
```

But the parent should also preserve:

```text
operation = addition
inputs = provenance refs
constraint state
Shadow = none or residual
```

---

# 11. COUPLING-AWARE VERSION

Suppose:

```math
X_3
=
R(X_1,X_2)
```

is itself a relation.

Then the parent may depend on:

```math
z
=
f(X_1,X_2,R)
```

This is useful for problems where the relation is decisive.

Example:

```text
base behavior
exponent behavior
rate coupling
```

in an indeterminate limit.

---

# 12. MULTI-CHANNEL SYNTHESIS

If the local state has different feature channels:

```text
semantic
constraint
uncertainty
edge
magnitude
```

do not mix them blindly.

Use separate submaps:

```math
z_s=f_s(X)
```

```math
z_c=f_c(C)
```

```math
z_e=f_e(E)
```

```math
z_u=f_u(U)
```

then combine:

```math
z
=
g(z_s,z_c,z_e,z_u)
```

This makes the operator easier to audit.

---

# 13. SHAPE AGGREGATION

If three child magnitudes are nonnegative:

```math
m_1,m_2,m_3
```

define local normalized shape:

```math
p_i
=
\frac{m_i}{
m_1+m_2+m_3
}
```

when the denominator is positive.

This gives:

```math
p
\in
\Delta^2
```

Store both:

```text
shape p
+
total magnitude M
```

where:

```math
M=m_1+m_2+m_3
```

if additive scale is task-valid.

---

# 14. MAGNITUDE RULE MUST BE TASK-VALID

Do not automatically use:

```math
M=m_1+m_2+m_3
```

for every domain.

Possible magnitude rules include:

```text
sum
max
norm
energy
probability mass
task-specific conserved quantity
learned aggregate
```

The operator specification must declare the rule.

---

# 15. SIGN PRESERVATION

If child values can be signed:

```math
x_i\in\mathbb{R}
```

the forward operator must preserve direction.

Possible parent metadata:

```text
dominant sign
signed moments
positive mass
negative mass
sign pattern
```

Do not normalize absolute values and discard signs.

---

# 16. INTERNAL EDGE SYNTHESIS

Local edges may be transformed into parent-level relations.

Example:

```text
X1 -> X2
X2 -> X3
```

may allow a derived relation:

```text
Parent exposes X1 -> X3
```

only if the edge types support composition.

The operator must check relation contracts before composing edges.

---

# 17. EDGE COMPOSITION RULE

For:

```math
X_1
\xrightarrow{f}
X_2
```

and:

```math
X_2
\xrightarrow{g}
X_3
```

a compressed relation may be:

```math
X_1
\xrightarrow{g\circ f}
X_3
```

only when:

```text
f and g are composable
```

The relation-type registry should declare:

```text
composable = true / false
```

---

# 18. NON-COMPOSABLE CASE

Example:

```text
X1 similar-to X2
X2 causes X3
```

does not justify:

```text
X1 causes X3
```

The forward operator must not invent transitivity.

If compression requires such a relation, the correct action is:

```text
HOLD
or
retain both original edges
```

---

# 19. CRITICAL EDGE PRESERVATION

Before compression, define:

```math
E_{\mathrm{critical}}
\subseteq
E_T\cup\partial E_T
```

Critical edges may include:

- hard constraints;
- rate couplings;
- high-sensitivity dependencies;
- irreversible transitions;
- causal bottlenecks;
- branch identity edges.

The operator must not silently remove them.

---

# 20. SHADOW GENERATION

Compression divides information into:

```text
retained
+
Shadow
```

Define abstractly:

```math
S
=
\Psi
(
X_1,X_2,X_3,E
)
-
\widehat{\Psi}
(
z,E_{\partial}
)
```

The exact form depends on representation.

A simpler operational definition is:

```text
Shadow =
information required for audit
that is not stored in the parent core
```

---

# 21. SHADOW SHOULD BE SMALL

The operator fails as a compressor if:

```text
Parent + Shadow
```

contains essentially the entire original subtree.

Define compression ratio:

```math
\rho
=
\frac{
\mathrm{size}(P)
}{
\mathrm{size}(X_1,X_2,X_3,E_T,\partial E_T)
}
```

A useful target is:

```math
\rho<1
```

under acceptable reconstruction quality.

---

# 22. SHADOW PRIORITY

Not all discarded details require equal storage.

Possible Shadow priority:

```text
high:
critical edge
constraint residual
branch identity
rare asymptotic term

medium:
uncertain local detail

low:
reconstructable redundant detail
```

This is a memory-allocation policy.

---

# 23. CERTIFICATE GENERATION

A parent should carry evidence about what was checked.

Possible certificate fields:

```text
input_valid
constraints_preserved
critical_edges_preserved
magnitude_rule_valid
sign_preserved
uncertainty_bounded
compression_ratio_valid
local_operation_verified
```

Abstractly:

```math
C
=
(c_1,c_2,\dots,c_k)
```

---

# 24. CERTIFICATE IS NOT PROOF OF TRUTH

A certificate only proves that the declared checks passed.

It does not prove:

```text
the premises were correct
the task model was correct
the decomposition was optimal
the final answer is globally correct
```

This distinction is important.

---

# 25. UNCERTAINTY PROPAGATION

Let child uncertainties be:

```math
U_1,U_2,U_3
```

The parent uncertainty should be:

```math
U_P
=
g_U(
U_1,U_2,U_3,E
)
```

Possible simple baselines:

```text
max child uncertainty
mean uncertainty
weighted mean
learned uncertainty
```

The safest initial baseline is often:

```math
U_P
=
\max(U_1,U_2,U_3,U_E)
```

because it does not hide a high-risk child.

---

# 26. UNCERTAINTY SHOULD NOT ONLY DECREASE

Compression should not automatically make a state look more certain.

If the parent drops information, uncertainty may increase.

A possible rule:

```math
U_P
=
g_U(...)
+
\lambda E_{\mathrm{comp}}
```

where `E_comp` estimates compression distortion.

This is a **MODEL**.

---

# 27. PROVENANCE POINTER

The parent should retain provenance references.

Example:

```text
Parent provenance
|
+-- child_1_id
+-- child_2_id
+-- child_3_id
+-- edge_ids
+-- compression_step_id
```

The full child data may live elsewhere.

The parent only needs enough information to reopen it during audit.

---

# 28. FORWARD OPERATOR AS A TRANSACTION

A useful software analogy:

```text
BEGIN LOCAL TRANSACTION
    read children
    read edges
    compute parent
    compute Shadow
    compute certificate
    compute uncertainty
    validate interface
COMMIT or HOLD
```

The parent should not be promoted before the local transaction is complete.

---

# 29. PRE-GATE

Before full Gate logic is introduced, `+3 Forward` may use a minimal local pre-check.

Example:

```text
valid inputs?
critical edge lost?
invalid sign transform?
constraint obviously violated?
```

If yes:

```text
HOLD
```

Otherwise:

```text
candidate parent
```

The full Gate protocol comes later.

---

# 30. FORWARD STATE MACHINE

Possible states:

```text
OPEN
  |
  v
READ
  |
  v
SYNTHESIZE
  |
  v
SHADOW
  |
  v
CERTIFY
  |
  v
CANDIDATE
```

Failure may transition to:

```text
HOLD
EXPAND
RECOMPUTE
```

---

# 31. LOCAL CLOSURE

A triad is locally "closed" when:

```text
required nodes are present
required relations are present
critical constraints are known
the compression interface is defined
the residual is accounted for
```

This is not topological closure in the strict mathematical sense.

It is an engineering notion of a complete local reasoning unit.

---

# 32. INVARIANT PRESERVATION

If the task defines an invariant:

```math
I(X_1,X_2,X_3)=c
```

the parent should carry:

```text
invariant value
or
certificate that it was preserved
```

Example:

```math
I(P)=c
```

or:

```math
|I(P)-c|
\le
\tau_I
```

---

# 33. HARD VS SOFT CONSTRAINTS

Separate:

```text
hard constraint:
must not be violated
```

from:

```text
soft constraint:
may be violated with cost
```

A hard violation should trigger:

```text
HOLD
```

A soft violation may increase:

```text
uncertainty
penalty
Shadow
```

---

# 34. PARENT VALUE VS PARENT INTERFACE

The parent may internally store:

```text
compressed core
```

while externally exposing:

```text
interface
```

These are different.

Example:

```text
internal:
latent vector z

external:
required input A
output B
constraint C
uncertainty U
```

This separation helps modular reasoning.

---

# 35. COMPRESSION OF A SUBTREE

Suppose:

```text
A -> B -> C
```

with internal relation history.

Compress into:

```text
P
```

The parent may expose:

```text
input:
A

output:
C

internal:
B hidden

Shadow:
B + residual details
```

This is useful only if future reasoning does not usually need `B`.

If `B` is frequently reopened, the compression policy may be poor.

---

# 36. REOPEN RATE

Define:

```math
R_{\mathrm{open}}
=
\frac{
\text{number of parent expansions}
}{
\text{number of parent uses}
}
```

High reopen rate means compression may be too aggressive.

This is an important empirical metric.

---

# 37. LOCAL INFORMATION GAIN

A parent should ideally reduce active complexity.

Let:

```math
C_{\mathrm{before}}
```

be active-state complexity before compression.

Let:

```math
C_{\mathrm{after}}
```

be active-state complexity after compression.

Define:

```math
G_{\mathrm{local}}
=
C_{\mathrm{before}}
-
C_{\mathrm{after}}
```

This is a generic gain metric.

The exact complexity measure may be:

```text
tokens
nodes
edges
memory bytes
active variables
description length
```

---

# 38. COMPRESSION UTILITY

A simple utility score:

```math
U_{\mathrm{comp}}
=
\alpha G_{\mathrm{local}}
-
\beta E_{\mathrm{rec}}
-
\gamma U_P
-
\delta R_{\mathrm{open}}
```

This is only a candidate objective.

It captures the desired tradeoff:

```text
compress enough
but not so much that audit or future use becomes expensive
```

---

# 39. SYMBOLIC EXAMPLE — ADDITION

Children:

```text
X1 = 4
X2 = 7
X3 = ADD
```

Forward:

```math
z=11
```

Parent:

```text
value        = 11
operation    = ADD
provenance   = [X1, X2, X3]
Shadow       = empty
uncertainty  = 0
certificate  = exact arithmetic verified
```

This is a near-lossless local closure.

---

# 40. SYMBOLIC EXAMPLE — LOSSY SUMMARY

Children:

```text
three paragraphs of reasoning
```

Parent:

```text
"constraint risk is increasing"
```

This is strongly lossy.

Therefore parent must retain:

```text
source refs
critical constraints
uncertainty
Shadow summary
```

and should expect a larger reconstruction error.

This case is fundamentally different from exact arithmetic compression.

---

# 41. LIMIT EXAMPLE

For:

```math
\left(1-\frac{3}{n+5}\right)^{3n}
```

local triad:

```text
X1 = epsilon_n
X2 = 3n
X3 = coupling = 3n * epsilon_n
```

Forward parent may retain:

```text
dominant asymptotic invariant = -9
```

and Shadow:

```text
higher-order Taylor terms
```

This produces:

```text
Parent:
main asymptotic state = -9
Shadow:
epsilon^2, epsilon^3, ...
```

Later audit verifies that the Shadow terms vanish.

---

# 42. RATE-COUPLING CERTIFICATE

For the limit example, certificate may include:

```text
epsilon_n -> 0
3n * epsilon_n -> -9
3n * epsilon_n^2 -> 0
higher-order remainder controlled
```

Only after those checks should the parent be promoted as:

```text
log-limit = -9
```

---

# 43. PARENT AS AN ATOM OF HIGHER REASONING

After successful local synthesis:

```text
(X1,X2,X3)
```

becomes:

```text
P1
```

At the next level:

```text
(P1,P2,P3)
```

can be compressed again.

Thus:

```text
leaves
-> local parents
-> higher parents
-> root
```

This is how the method attempts to reduce active dependency depth.

---

# 44. BALANCED TERNARY COMPRESSION

For `N` leaf states, idealized grouping gives:

```text
N
-> N/3
-> N/9
-> ...
-> 1
```

with approximate depth:

```math
D
\approx
\left\lceil
\log_3 N
\right\rceil
```

This refers to hierarchy depth.

It does not mean total work becomes logarithmic.

---

# 45. PARALLELISM

Independent triads at the same level may be processed in parallel.

Example:

```text
Level 0:
T1 T2 T3 T4 T5 T6

Level 1:
P1 P2
```

If hardware permits, local forward synthesis can reduce wall-clock depth.

This is a potential implementation advantage.

---

# 46. NON-INDEPENDENT TRIADS

Parallel processing is unsafe when triads share critical cross-edges.

Example:

```text
T1 <----critical edge----> T2
```

The compression scheduler must detect such dependencies.

Possible responses:

```text
merge triads
delay compression
retain cross-edge interface
```

---

# 47. GROUPING POLICY

The choice of which three states to group is itself important.

Possible policies:

```text
adjacent dependency nodes
highest coupling strength
same semantic role
same time window
graph partition
learned grouping
random baseline
```

The project must compare them.

---

# 48. BAD GROUPING

A poor grouping may combine:

```text
three unrelated states
```

into one parent.

This creates artificial locality.

Therefore `+3 Forward` is only as good as its decomposition / grouping policy.

This is a major failure mode.

---

# 49. GROUPING SCORE

A candidate triad may receive score:

```math
Q_T
=
\alpha C_{\mathrm{internal}}
-
\beta C_{\mathrm{boundary}}
+
\gamma R_{\mathrm{task}}
```

where:

- `C_internal` — internal coupling strength;
- `C_boundary` — cross-boundary coupling burden;
- `R_task` — task relevance.

Higher score means a cleaner local module.

This is a candidate heuristic only.

---

# 50. PARENT IDENTITY

The parent should have a stable identifier:

```text
parent_id
```

and preserve:

```text
child IDs
edge IDs
compression version
operator version
```

This supports reproducibility and debugging.

---

# 51. DETERMINISM

A deterministic forward operator is easier to audit.

For a prototype, prefer:

```text
same input
-> same parent
```

Later, learned or stochastic compression can be introduced.

If stochasticity is used, store:

```text
random seed
model version
sampling parameters
```

in provenance.

---

# 52. VERSIONED OPERATOR

Because the compression rule may evolve, store:

```text
operator_version
```

Example:

```text
plus3_forward_v0.1
```

Otherwise an old parent may not be reproducible after code changes.

---

# 53. FORWARD FAILURE STATES

The operator should explicitly return failure modes.

Example:

```text
INVALID_INPUT
MISSING_EDGE
CONSTRAINT_VIOLATION
NON_COMPOSABLE_RELATION
SHADOW_TOO_LARGE
UNCERTAINTY_TOO_HIGH
INTERFACE_INCOMPLETE
GROUPING_BAD
```

Do not collapse all failures into one generic error.

---

# 54. CANDIDATE RESULT

The direct output of `+3 Forward` should be a:

```text
CANDIDATE_PARENT
```

not an automatically committed state.

Later:

```text
Gate
```

decides whether it may be promoted.

This prevents compression from being mistaken for validation.

---

# 55. FORWARD PSEUDOCODE

```python
def plus3_forward(children, local_edges, boundary_edges, policy):
    validate_inputs(children)

    triad = build_local_graph(
        children,
        local_edges,
        boundary_edges,
    )

    grouping_certificate = check_locality(triad)

    compressed_state = compress_state(triad, policy)
    retained_interface = compress_boundary_edges(triad, policy)

    shadow = compute_shadow(
        original=triad,
        compressed=compressed_state,
        interface=retained_interface,
    )

    uncertainty = propagate_uncertainty(
        children=children,
        edges=local_edges,
        shadow=shadow,
    )

    certificate = build_certificate(
        triad=triad,
        compressed=compressed_state,
        interface=retained_interface,
        shadow=shadow,
        uncertainty=uncertainty,
    )

    return CandidateParent(
        state=compressed_state,
        interface=retained_interface,
        shadow=shadow,
        uncertainty=uncertainty,
        certificate=certificate,
        provenance=make_provenance(triad),
    )
```

---

# 56. MINIMAL PYTHON DATA CONTRACT

```python
from dataclasses import dataclass
from typing import Any, Dict, List

@dataclass
class CandidateParent:
    state: Any
    interface: Dict[str, Any]
    shadow: Any
    uncertainty: float
    certificate: Dict[str, Any]
    provenance: Dict[str, Any]
    children: List[str]
```

This is an interface sketch, not the final implementation.

---

# 57. FORWARD TEST — EXACT CASE

**TEST**

Use arithmetic triads where exact compression is known.

Measure:

```text
correct parent
zero reconstruction error
small Shadow
valid certificate
```

This verifies the basic operator plumbing.

---

# 58. FORWARD TEST — LOSSY CASE

**TEST**

Use high-dimensional child states compressed into a small parent.

Measure:

```text
reconstruction error
task accuracy
Shadow size
reopen rate
```

This tests whether compression remains useful.

---

# 59. FORWARD TEST — MISSING CRITICAL EDGE

**TEST**

Remove a critical edge before compression.

Expected behavior:

```text
HOLD
or
certificate failure
```

Undesired behavior:

```text
confident candidate parent
```

---

# 60. FORWARD TEST — NON-COMPOSABLE RELATION

**TEST**

Use:

```text
A similar-to B
B causes C
```

and verify that the operator does not infer:

```text
A causes C
```

unless explicitly licensed.

---

# 61. FORWARD TEST — BOUNDARY EDGE

**TEST**

Create a triad with one strong outgoing dependency.

Compress the triad.

Verify that the parent interface preserves that dependency.

If it disappears, the compression is invalid.

---

# 62. FORWARD TEST — SHADOW COST

**TEST**

Track:

```math
\rho
=
\frac{
\mathrm{size(parent+shadow)}
}{
\mathrm{size(original\ local\ graph)}
}
```

If:

```math
\rho \ge 1
```

for most tasks, the compressor provides little memory benefit.

---

# 63. FORWARD TEST — UNCERTAINTY

**TEST**

Give:

```text
two high-confidence children
one low-confidence critical child
```

The parent should not become falsely high-confidence through averaging.

This checks uncertainty propagation.

---

# 64. ABLATION — NO SHADOW

Compare:

```text
+3 with Shadow
```

versus:

```text
+3 without Shadow
```

Measure:

- long-chain accuracy;
- reconstruction;
- error localization;
- memory.

This determines whether Shadow actually contributes.

---

# 65. ABLATION — NO EDGE MEMORY

Compare:

```text
+3 with edge memory
```

versus:

```text
+3 node-only
```

Use edge-sensitive tasks.

This tests whether coupling preservation is necessary.

---

# 66. ABLATION — BINARY VS TERNARY

Compare local grouping:

```text
2 -> 1
```

against:

```text
3 -> 1
```

under equal compute.

If binary grouping performs equally or better, ternary geometry is not empirically privileged.

---

# 67. ABLATION — LEARNED VS RULE-BASED

Compare:

```text
symbolic forward operator
```

against:

```text
learned compressor
```

and:

```text
hybrid
```

The project should prefer the simplest method that achieves the target reliability.

---

# 68. FAILURE CONDITIONS

The `+3 Forward` operator should be revised if:

1. it destroys critical edges;
2. it hides uncertainty;
3. it creates invalid composed relations;
4. Shadow becomes too large;
5. parent interfaces are frequently incomplete;
6. reopen rate is high;
7. grouping choice dominates performance unpredictably;
8. simpler aggregation performs equally well;
9. compression does not reduce active reasoning complexity;
10. higher-level parents become less interpretable without improving accuracy.

---

# 69. RESEARCH STATUS

```text
FACT:
Compression requires a tradeoff between retained information and loss.

FACT:
Local graph structure can be summarized through interfaces.

MODEL:
+3 Forward compresses a local triad into a candidate parent.

MODEL:
Parent carries state + interface + Shadow + certificate + uncertainty.

HYPOTHESIS:
Locally certified ternary compression can reduce active dependency depth
without losing the relations required for later reasoning.

TEST:
Exact, lossy, missing-edge, boundary-edge,
uncertainty, Shadow-cost, and grouping ablations.
```

---

# 70. TRANSITION TO THE NEXT FILE

`+3 Forward` creates a compressed candidate parent.

The next question is:

> Can the system reconstruct what the parent came from?

That is the purpose of:

```text
-3 BACKWARD
```

---

# 71. NEXT FILE

Next:

```text
08_MINUS3_BACKWARD_OPERATOR.md
```

Its purpose is to formalize:

```text
Parent
  |
  v
reconstruction
  |
  v
(X1_hat, X2_hat, X3_hat)
  |
  v
compare against original / Shadow
```

The key principle will be:

> `-3 Backward` does not guarantee reversibility; it measures reconstructability and local information loss.

---

## FILE VERDICT

```text
STATE: CRYSTAL

DEFINED:
+3 Forward Operator

INPUT:
3 local states
+ local edges
+ boundary edges

OUTPUT:
candidate parent
+ retained interface
+ Shadow
+ certificate
+ uncertainty
+ provenance

CRITICAL RULE:
compression is not validation

NEXT:
08_MINUS3_BACKWARD_OPERATOR.md
```
