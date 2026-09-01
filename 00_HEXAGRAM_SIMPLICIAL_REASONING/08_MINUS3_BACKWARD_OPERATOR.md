# 08 — -3 BACKWARD OPERATOR

**Project:** Vuzol-19  
**Module:** Hexagram Simplicial Reasoning  
**Status:** RECONSTRUCTION / SHADOW AUDIT SPEC  
**State:** CRYSTAL  
**Language:** English  
**Depends on:** `07_PLUS3_FORWARD_OPERATOR.md`

---

## 0. PURPOSE

The previous file defined:

```text
+3 FORWARD
```

as a local compression operator:

```text
children
+ local edges
+ boundary edges
      |
      v
candidate parent
+ interface
+ Shadow
+ certificate
+ uncertainty
```

This file defines the complementary operator:

```text
-3 BACKWARD
```

Its purpose is:

> **Given a compressed parent, reconstruct the local triad well enough to measure what was preserved, what was distorted, and what cannot be recovered without expanding Shadow or provenance.**

The operator is not a claim of perfect reversibility.

It is a **reconstructability test**.

---

# 1. BASIC FORM

Let the candidate parent be:

```math
P
=
(z,S,C,U,M,E_{\partial},P_{\mathrm{prov}})
```

The backward operator is:

```math
F_{-3}:
P
\longrightarrow
(\hat{X}_1,\hat{X}_2,\hat{X}_3,\hat{E})
```

where:

- `X1_hat` — reconstructed first child;
- `X2_hat` — reconstructed second child;
- `X3_hat` — reconstructed third child;
- `E_hat` — reconstructed local relation state.

The hats indicate reconstructed estimates.

---

# 2. CORE PRINCIPLE

`-3 Backward` asks:

```text
Can this parent explain where it came from?
```

Not merely:

```text
Can this parent produce a plausible story?
```

The reconstructed triad must be compared against stored provenance, Shadow, constraints, and original structure when available.

---

# 3. RECONSTRUCTION IS NOT RE-GENERATION

A language model can often invent a plausible explanation after the fact.

That is not sufficient.

A true backward audit must distinguish:

```text
reconstruction
```

from:

```text
post-hoc generation
```

The difference is:

```text
RECONSTRUCTION:
constrained by stored parent state,
provenance,
Shadow,
and certificates

POST-HOC GENERATION:
free-form plausible narrative
```

Only the first is useful as a verification mechanism.

---

# 4. BACKWARD INPUT CONTRACT

The backward operator may use:

```text
compressed parent state
retained interface
Shadow
certificate
uncertainty
provenance references
operator version
task schema
```

Minimal abstract input:

```python
BackwardInput(
    parent_state=...,
    interface=...,
    shadow=...,
    certificate=...,
    uncertainty=...,
    provenance=...,
    operator_version=...,
)
```

---

# 5. BACKWARD OUTPUT CONTRACT

The operator should return:

```text
reconstructed children
reconstructed edges
reconstruction error
constraint consistency
coupling consistency
ambiguity
required expansions
audit verdict
```

Conceptually:

```python
BackwardResult(
    children_hat=[...],
    edges_hat=...,
    reconstruction_error=...,
    constraint_error=...,
    coupling_error=...,
    ambiguity=...,
    expand_requests=[...],
    verdict=...,
)
```

---

# 6. EXACT INVERSE CASE

Some local operations are exactly invertible if enough information is stored.

Example:

```text
X1 = 4
X2 = 7
operator = ADD
parent = 11
```

From `11` alone, the original inputs are not recoverable.

But if provenance stores:

```text
X1_id
X2_id
operation = ADD
```

then the audit can verify:

```math
4+7=11
```

This is not inversion from the scalar parent.

It is reconstruction using retained provenance.

---

# 7. LOSSY CASE

Suppose three long text fragments are compressed into:

```text
"constraint risk is increasing"
```

The original text cannot be exactly reconstructed from the summary.

Therefore `-3 Backward` should not pretend otherwise.

It may instead reconstruct:

```text
high-level child roles
critical constraints
main coupling
uncertainty
```

and report:

```text
LOSSY_RECONSTRUCTION
```

This is valid if the loss is explicit.

---

# 8. REVERSIBILITY CLASSES

Define four practical classes.

```text
CLASS 0 — EXACT
original local state can be reconstructed exactly

CLASS 1 — CERTIFIED APPROXIMATE
reconstruction is approximate but within declared tolerance

CLASS 2 — PARTIAL
only task-critical structure can be reconstructed

CLASS 3 — NON-RECONSTRUCTABLE
parent lacks enough information
```

The class should be stored in the audit result.

---

# 9. RECONSTRUCTION ERROR

Let original local state be:

```math
X
```

and reconstructed state be:

```math
\hat{X}
```

Define:

```math
E_{\mathrm{rec}}
=
d(X,\hat{X})
```

The distance `d` must match the representation.

Possible components:

```text
value error
shape error
magnitude error
sign error
edge error
constraint error
provenance mismatch
```

---

# 10. MULTI-COMPONENT RECONSTRUCTION ERROR

A more informative vector is:

```math
\mathbf{E}
=
(
E_{\mathrm{value}},
E_{\mathrm{shape}},
E_{\mathrm{mag}},
E_{\mathrm{sign}},
E_{\mathrm{edge}},
E_{\mathrm{constraint}}
)
```

This allows local diagnosis.

A single scalar may hide which component failed.

---

# 11. WEIGHTED TOTAL ERROR

If one scalar is required:

```math
E_{\mathrm{total}}
=
\alpha_1E_{\mathrm{value}}
+
\alpha_2E_{\mathrm{shape}}
+
\alpha_3E_{\mathrm{mag}}
+
\alpha_4E_{\mathrm{sign}}
+
\alpha_5E_{\mathrm{edge}}
+
\alpha_6E_{\mathrm{constraint}}
```

The weights must be task-dependent.

Do not use arbitrary weights as if they were universal.

---

# 12. CHILD-WISE RESIDUAL

For reconstructed children:

```math
r_i
=
X_i-\hat{X}_i
```

Store:

```math
r
=
(r_1,r_2,r_3)
```

This identifies the branch that failed most strongly.

Example:

```text
child 1 residual = small
child 2 residual = small
child 3 residual = large
```

Then the system can issue:

```text
EXPAND CHILD 3
```

instead of recomputing everything.

---

# 13. SHADOW AUDIT

Shadow contains information omitted from the parent core.

The backward operator should use Shadow in two ways:

```text
1. reconstruction assistance
2. residual verification
```

Conceptually:

```text
Parent
 + Shadow
    |
    v
reconstructed triad
    |
    v
compare to provenance / original
```

The purpose of Shadow is not to hide errors.

It is to make lost information explicit and recoverable when needed.

---

# 14. SHADOW DEPENDENCY RATIO

If reconstruction depends too heavily on Shadow, compression may be weak.

Define:

```math
\eta_S
=
\frac{
\text{information retrieved from Shadow}
}{
\text{information required for reconstruction}
}
```

Interpretation:

```text
eta_S near 0:
parent core carries most useful information

eta_S near 1:
Shadow carries almost everything
```

A high value is not automatically wrong, but it reduces compression benefit.

---

# 15. EDGE RECONSTRUCTION

The operator must reconstruct local relation state:

```math
\hat{E}
```

not just child values.

For weighted adjacency matrices:

```math
E_{\mathrm{edge}}
=
\|K-\hat{K}\|_F
```

For typed edges, compare:

```text
edge existence
edge type
edge direction
edge weight
edge uncertainty
```

---

# 16. EDGE TYPE MISMATCH

Example:

```text
original:
A inhibits B
```

reconstructed as:

```text
A activates B
```

Node values may still look plausible.

But the edge semantics are wrong.

Therefore typed edge mismatch should be treated as a major audit failure.

---

# 17. BOUNDARY EDGE AUDIT

A parent may correctly summarize its internal triad while losing external dependencies.

Therefore reconstruct or verify:

```math
\partial E(T)
```

the boundary interface.

Audit questions:

```text
Which external nodes depended on this subtree?
Which constraints crossed the boundary?
Which outgoing effects were promised?
```

If these cannot be recovered, the parent is unsafe for higher-level reasoning.

---

# 18. PROVENANCE RECONSTRUCTION

The backward operator should recover:

```text
which child came from which source
which edge came from which relation
which compression step created the parent
```

This is not semantic reconstruction only.

It is audit provenance.

Example:

```text
Parent P42
|
+-- child source: equation 7
+-- child source: constraint 3
+-- coupling source: derivation step 12
```

---

# 19. PROVENANCE MISMATCH

If reconstructed content is plausible but provenance does not match:

```text
content matches
source does not
```

the audit should not mark the node as fully valid.

This prevents fabricated explanations from passing.

---

# 20. CONSTRAINT RECONSTRUCTION

For every hard constraint active in the child triad, the backward audit should answer:

```text
Was the constraint retained?
Was it applied to the correct node?
Was its validity interval preserved?
Was it satisfied?
```

Define:

```math
E_{\mathrm{constraint}}
```

as a task-specific mismatch score.

A hard constraint mismatch should usually trigger `HOLD`.

---

# 21. TEMPORAL RECONSTRUCTION

If child relations depend on order:

```text
A before B before C
```

the parent must preserve enough information to reconstruct that order.

A backward audit should detect:

```text
A -> B -> C
```

being reconstructed incorrectly as:

```text
B -> A -> C
```

even when all operations are present.

---

# 22. BRANCH IDENTITY

Consider a many-to-one map:

```math
y=x^2
```

with:

```math
y=4
```

The parent alone does not reveal whether:

```math
x=2
```

or:

```math
x=-2
```

was used.

Therefore branch identity must be stored in:

```text
provenance
sign metadata
Shadow
or explicit branch ID
```

Backward reconstruction should detect ambiguity rather than invent one branch.

---

# 23. AMBIGUITY SCORE

Define:

```math
A_{\mathrm{back}}
=
\text{number or mass of plausible reconstructions}
```

Possible interpretation:

```text
low ambiguity:
one reconstruction dominates

high ambiguity:
many reconstructions fit the parent
```

A high ambiguity score may trigger:

```text
EXPAND
```

or:

```text
UNKNOWN
```

---

# 24. SET-VALUED RECONSTRUCTION

Some inverse problems naturally produce a set:

```math
F^{-1}(P)
=
\{X^{(1)},X^{(2)},\dots\}
```

The operator should support:

```text
candidate reconstruction set
```

instead of forcing one answer.

This is mathematically more honest for non-injective compression.

---

# 25. POSTERIOR RECONSTRUCTION

A learned backward model may output:

```math
p(X|P)
```

rather than a single `X_hat`.

Then the audit can inspect:

```text
posterior concentration
branch probability
uncertainty
```

This is an advanced version.

The first prototype may remain deterministic.

---

# 26. BACKWARD MAP

General form:

```math
\hat{X}
=
R_{\phi}
(
P,
S,
C,
P_{\mathrm{prov}}
)
```

where `R_phi` may be:

```text
symbolic
rule-based
learned
hybrid
```

The backward operator should be versioned separately from the forward operator.

---

# 27. FORWARD-BACKWARD CONSISTENCY

Let:

```math
P
=
F_{+3}(X)
```

and:

```math
\hat{X}
=
F_{-3}(P)
```

Then define cycle consistency:

```math
E_{\mathrm{cycle}}
=
d(X,\hat{X})
```

This is the core local audit quantity.

---

# 28. BACKWARD-FORWARD CONSISTENCY

Also test the opposite cycle.

Given parent `P`:

```math
\hat{X}
=
F_{-3}(P)
```

then:

```math
\hat{P}
=
F_{+3}(\hat{X})
```

Compare:

```math
E_{\mathrm{parent}}
=
d(P,\hat{P})
```

This checks whether the reconstructed children reproduce the same parent state.

---

# 29. DUAL CYCLE TEST

A stronger audit uses both:

```text
child cycle:
X -> P -> X_hat
```

and:

```text
parent cycle:
P -> X_hat -> P_hat
```

Then:

```math
E_{\mathrm{dual}}
=
\lambda E_{\mathrm{cycle}}
+
(1-\lambda)E_{\mathrm{parent}}
```

This remains a **MODEL**.

---

# 30. WHY BOTH CYCLES MATTER

A backward model may reconstruct children that are close to the original but compress differently.

Or it may reconstruct very different children that happen to produce the same parent.

The two cycle tests catch different failure modes.

---

# 31. LOCAL RESONANCE

Within Vuzol-19 language, a successful forward/backward match may be described as:

```text
resonance
```

Operational definition:

```text
forward parent
and
backward reconstruction
agree within declared tolerances
```

Do not use "resonance" as a substitute for a measurable error.

It must map to explicit metrics.

---

# 32. RESONANCE SCORE

One possible normalized score:

```math
R_{\mathrm{local}}
=
\exp(
-\lambda E_{\mathrm{dual}}
)
```

Then:

```text
near 1:
high local consistency

near 0:
poor reconstruction consistency
```

This is only a convenient score.

The raw errors should still be retained.

---

# 33. HARD GATE PRECONDITION

Some failures should immediately block promotion.

Examples:

```text
wrong sign
missing critical edge
hard constraint violation
branch identity lost
invalid operator inversion
```

Even if total reconstruction error is numerically small.

This prevents average metrics from hiding categorical failures.

---

# 34. SOFT FAILURE

Other mismatches may be tolerable:

```text
small approximation error
low-impact residual
low-confidence optional edge
```

These can increase uncertainty instead of forcing rejection.

---

# 35. AUDIT VERDICTS

Recommended backward verdicts:

```text
PASS
PASS_WITH_RESIDUAL
HOLD
EXPAND
RECOMPUTE
AMBIGUOUS
NON_INVERTIBLE
UNKNOWN
```

This is richer than a binary true/false result.

---

# 36. PASS

Use:

```text
PASS
```

when:

```text
critical structure reconstructed
hard constraints satisfied
edge state consistent
error below threshold
ambiguity acceptable
```

---

# 37. PASS_WITH_RESIDUAL

Use:

```text
PASS_WITH_RESIDUAL
```

when:

```text
task-critical structure is preserved
small declared residual remains
residual is bounded
```

The residual should remain in Shadow.

---

# 38. HOLD

Use:

```text
HOLD
```

when:

```text
validation incomplete
critical mismatch detected
uncertainty too high
```

No higher-level commit should occur.

---

# 39. EXPAND

Use:

```text
EXPAND
```

when the parent needs more local detail.

Example:

```text
child 3 residual dominates
```

Action:

```text
reopen child 3 subtree
```

This is the preferred local repair mechanism.

---

# 40. RECOMPUTE

Use:

```text
RECOMPUTE
```

when the local transformation itself may be wrong.

The system should rerun the local forward synthesis.

---

# 41. AMBIGUOUS

Use:

```text
AMBIGUOUS
```

when multiple reconstructions remain plausible.

Do not force one history without evidence.

---

# 42. NON_INVERTIBLE

Use:

```text
NON_INVERTIBLE
```

when the forward mapping is known to destroy branch identity or information irreversibly.

This is not necessarily a bug.

It becomes a bug only if the architecture claimed reversible audit.

---

# 43. UNKNOWN

Use:

```text
UNKNOWN
```

when the system lacks enough evidence to classify the reconstruction.

This is preferable to false certainty.

---

# 44. LOCAL ERROR LOCALIZATION

Suppose:

```math
E_1=0.01
```

```math
E_2=0.02
```

```math
E_3=0.60
```

Then:

```text
global recomputation
```

is wasteful.

Prefer:

```text
EXPAND child 3
```

This is the practical value of child-wise residuals.

---

# 45. REPAIR LOOP

A local repair cycle:

```text
Parent
  |
  v
-3 Backward
  |
  v
audit
  |
  +--> PASS
  |
  +--> EXPAND child k
          |
          v
      recompute local subtree
          |
          v
      +3 Forward
          |
          v
      audit again
```

This prevents one local failure from invalidating the entire reasoning graph.

---

# 46. MAXIMUM REPAIR DEPTH

Repair loops need stopping criteria.

Possible limits:

```text
maximum retries
maximum expansion depth
maximum token budget
maximum wall-clock budget
uncertainty floor
```

Otherwise the system may recurse indefinitely.

---

# 47. REPAIR BUDGET

Define:

```math
B_{\mathrm{repair}}
```

as allowed compute for local recovery.

A scheduler may allocate more budget to:

```text
high-impact
high-uncertainty
critical-edge
safety-relevant
```

nodes.

---

# 48. BACKWARD AUDIT AS ERROR CONTAINMENT

The main architectural hypothesis is not:

```text
errors disappear
```

It is:

> **errors can be detected and contained locally before they contaminate higher-level reasoning.**

This is a stronger and more testable claim.

---

# 49. SEQUENTIAL ERROR PATH

Without local audit:

```text
error at X3
   |
   v
X4
   |
   v
X5
   |
   v
...
   |
   v
wrong root
```

With local audit:

```text
error at X3
   |
   v
local parent
   |
   v
-3 audit
   |
   v
HOLD / EXPAND
```

The key metric is how far an error travels before detection.

---

# 50. ERROR DETECTION DISTANCE

Define:

```math
D_{\mathrm{detect}}
=
\text{number of graph levels between error injection and detection}
```

Desired:

```text
small D_detect
```

This is a useful benchmark metric.

---

# 51. ERROR ESCAPE RATE

Define:

```math
R_{\mathrm{escape}}
=
\frac{
\text{local errors reaching root undetected}
}{
\text{local errors injected}
}
```

The method should reduce this rate.

---

# 52. RECONSTRUCTION COVERAGE

Not every field needs exact reconstruction.

Define:

```math
C_{\mathrm{rec}}
=
\frac{
\text{critical fields reconstructed}
}{
\text{critical fields required}
}
```

This helps distinguish:

```text
full reconstruction
```

from:

```text
task-sufficient reconstruction
```

---

# 53. CRITICAL FIELD SET

Let:

```math
F_{\mathrm{critical}}
```

contain:

```text
hard constraints
branch identity
critical couplings
sign
domain assumptions
output interface
```

Backward audit should prioritize these fields over decorative details.

---

# 54. EXACT SYMBOLIC EXAMPLE

Forward:

```text
X1 = 4
X2 = 7
X3 = ADD
```

Parent:

```text
value = 11
provenance = [4, 7, ADD]
```

Backward:

```text
read provenance
reconstruct X1 = 4
reconstruct X2 = 7
reconstruct operation = ADD
```

Audit:

```math
4+7=11
```

Verdict:

```text
PASS
```

---

# 55. MANY-TO-ONE EXAMPLE

Forward:

```math
x=2
\longrightarrow
y=x^2=4
```

or:

```math
x=-2
\longrightarrow
y=x^2=4
```

If branch identity is omitted, backward result is:

```math
x\in\{-2,2\}
```

Verdict:

```text
AMBIGUOUS
```

This is correct behavior.

---

# 56. LIMIT EXAMPLE

Forward local parent retains:

```text
dominant coupling = -9
```

Shadow retains:

```text
higher-order terms
```

Backward audit reconstructs:

```text
epsilon_n
3n
3n * epsilon_n
higher-order remainder
```

and verifies:

```math
3n\varepsilon_n\to -9
```

```math
3n\varepsilon_n^2\to0
```

If the remainder cannot be controlled:

```text
HOLD
```

---

# 57. APPROXIMATION EXAMPLE

Suppose forward reasoning used:

```math
\log(1+\varepsilon)
\approx
\varepsilon
```

Backward audit must recover the validity condition:

```text
epsilon is small
```

and ideally the next-order residual:

```math
-\frac{\varepsilon^2}{2}
```

If the approximation condition is missing, the parent certificate is incomplete.

---

# 58. TEXT REASONING EXAMPLE

Three paragraphs are compressed into:

```text
"the plan is structurally valid but constraint risk remains"
```

Backward reconstruction may recover:

```text
child role 1 = plan structure
child role 2 = constraint evidence
child role 3 = unresolved risk
```

It cannot reproduce the exact original paragraphs.

Verdict may be:

```text
PARTIAL / PASS_WITH_RESIDUAL
```

if the task only needs those roles.

---

# 59. CODE REASONING EXAMPLE

Local code block:

```python
x = parse(data)
validate(x)
return transform(x)
```

Parent:

```text
parse -> validate -> transform
constraint = validation must pass
```

Backward audit should detect if reconstruction becomes:

```text
parse -> transform -> validate
```

because the temporal/dependency order changed.

---

# 60. BACKWARD PSEUDOCODE

```python
def minus3_backward(parent, policy):
    recovered = reconstruct_children(
        state=parent.state,
        interface=parent.interface,
        shadow=parent.shadow,
        provenance=parent.provenance,
        policy=policy,
    )

    recovered_edges = reconstruct_edges(
        parent=parent,
        recovered_children=recovered,
    )

    errors = compare_with_reference(
        recovered_children=recovered,
        recovered_edges=recovered_edges,
        provenance=parent.provenance,
        certificate=parent.certificate,
    )

    ambiguity = estimate_ambiguity(
        parent=parent,
        recovered=recovered,
    )

    verdict = backward_verdict(
        errors=errors,
        ambiguity=ambiguity,
        uncertainty=parent.uncertainty,
    )

    return BackwardResult(
        children_hat=recovered,
        edges_hat=recovered_edges,
        errors=errors,
        ambiguity=ambiguity,
        verdict=verdict,
    )
```

---

# 61. MINIMAL DATA CONTRACT

```python
from dataclasses import dataclass
from typing import Any, Dict, List

@dataclass
class BackwardResult:
    children_hat: List[Any]
    edges_hat: Any
    errors: Dict[str, float]
    ambiguity: float
    verdict: str
    expand_requests: List[str]
```

This is an interface sketch.

---

# 62. FORWARD/BACKWARD VERSION MATCH

Store:

```text
forward_operator_version
backward_operator_version
```

A backward audit should know which forward compressor created the parent.

Otherwise version drift may look like reasoning failure.

---

# 63. DETERMINISTIC BASELINE

The first implementation should prefer deterministic reconstruction where possible.

Reason:

```text
same parent
-> same audit result
```

makes debugging easier.

Learned stochastic reconstruction can be introduced later.

---

# 64. LEARNED BACKWARD MODEL

A learned decoder may use:

```math
\hat{X}
=
R_{\phi}(P)
```

Training objective may include:

```math
\mathcal{L}_{\mathrm{back}}
=
\lambda_1\mathcal{L}_{\mathrm{rec}}
+
\lambda_2\mathcal{L}_{\mathrm{edge}}
+
\lambda_3\mathcal{L}_{\mathrm{constraint}}
+
\lambda_4\mathcal{L}_{\mathrm{task}}
```

The exact objective is experimental.

---

# 65. DANGER — LEARNED DECODER HALLUCINATION

A learned backward model may invent plausible child states not actually present in the original reasoning.

Therefore reconstruction must be checked against:

```text
provenance
stored IDs
Shadow
certificates
exact values where available
```

Do not trust decoder fluency alone.

---

# 66. HASH / ID AUDIT

For exact symbolic states, child content may be hashed or assigned stable IDs.

Then backward audit can verify:

```text
reconstructed child ID
matches original child ID
```

This is stronger than semantic similarity.

---

# 67. PARTIAL MATERIALIZATION

A parent does not always need to expand all children.

It may reconstruct only:

```text
critical child
critical edge
constraint branch
```

This supports efficient targeted audit.

---

# 68. SELECTIVE BACKWARD AUDIT

Possible policies:

```text
audit all parents
audit only high-risk parents
audit random sample
audit on Gate uncertainty
audit before final Bindu
```

This creates a compute/reliability tradeoff.

---

# 69. RISK-BASED AUDIT

Define local audit priority:

```math
P_{\mathrm{audit}}
=
f(
U,
E_{\mathrm{critical}},
impact,
depth,
history
)
```

High-risk nodes receive more backward verification.

This is a scheduler policy.

---

# 70. AUDIT FREQUENCY

Too much backward checking may double or triple compute.

Too little checking may miss errors.

Therefore benchmark:

```text
audit every node
audit every level
audit only boundary nodes
audit only high-risk nodes
audit only final path
```

---

# 71. COMPUTE OVERHEAD

Define:

```math
C_{\mathrm{overhead}}
=
\frac{
\mathrm{compute}_{+3/-3}
}{
\mathrm{compute}_{\mathrm{baseline}}
}
```

Any accuracy gain must be compared under equal or clearly reported compute budgets.

---

# 72. MEMORY OVERHEAD

Define:

```math
M_{\mathrm{overhead}}
=
\frac{
\mathrm{memory}_{\mathrm{hierarchical}}
}{
\mathrm{memory}_{\mathrm{baseline}}
}
```

A robust result reports both:

```text
accuracy
and
resource cost
```

---

# 73. ERROR LOCALIZATION BENEFIT

Define:

```math
L_{\mathrm{benefit}}
=
\frac{
\mathrm{cost\ of\ global\ recomputation}
}{
\mathrm{cost\ of\ local\ repair}
}
```

If local repair is much cheaper, backward audit may justify its overhead.

---

# 74. ABLATION — NO PROVENANCE

Compare backward audit:

```text
with provenance
```

versus:

```text
without provenance
```

If no difference occurs, provenance may not be necessary for that task.

If hallucinated reconstructions rise sharply, provenance is critical.

---

# 75. ABLATION — NO SHADOW

Compare:

```text
parent + Shadow
```

versus:

```text
parent only
```

Measure:

- reconstruction error;
- ambiguity;
- error detection;
- memory cost.

---

# 76. ABLATION — NODE-ONLY BACKWARD

Compare reconstruction of:

```text
nodes only
```

against:

```text
nodes + edges
```

Use rate-coupling and constraint tasks.

This directly tests whether edge reconstruction matters.

---

# 77. ABLATION — SINGLE SCALAR ERROR

Compare:

```text
one total reconstruction score
```

against:

```text
component-wise error vector
```

Measure local repair quality.

The hypothesis is that component-wise residuals improve localization.

---

# 78. EXPERIMENT A — INJECTED CHILD ERROR

Inject a small error into child 2 before forward compression.

Run:

```text
+3 Forward
-3 Backward
```

Measure:

```text
was child 2 identified?
how many levels did error travel?
was final answer protected?
```

---

# 79. EXPERIMENT B — EDGE FLIP

Change:

```text
A activates B
```

to:

```text
A inhibits B
```

while keeping node values unchanged.

Backward audit should detect edge mismatch.

---

# 80. EXPERIMENT C — BRANCH LOSS

Use a many-to-one operator.

Remove branch identity.

Expected verdict:

```text
AMBIGUOUS
```

not a fabricated unique reconstruction.

---

# 81. EXPERIMENT D — CONSTRAINT LOSS

Remove one hard constraint from parent interface.

Backward audit should detect the missing constraint if provenance/reference exists.

Expected:

```text
HOLD
```

---

# 82. EXPERIMENT E — ORDER SWAP

Swap two temporal child operations.

Audit should detect:

```text
sequence mismatch
```

even when all node values are present.

---

# 83. EXPERIMENT F — SHADOW TRUNCATION

Artificially reduce Shadow storage.

Measure the curve:

```text
Shadow size
vs
reconstruction quality
vs
task accuracy
```

This reveals the true compression/reliability tradeoff.

---

# 84. EXPERIMENT G — AUDIT FREQUENCY

Compare:

```text
100% audit
50% audit
risk-based audit
final-only audit
```

Measure:

```text
accuracy
compute
memory
error escape rate
```

---

# 85. PRIMARY SUCCESS CRITERIA

A useful `-3 Backward` operator should:

1. detect more local errors than a forward-only system;
2. localize errors to specific children or edges;
3. reduce error escape to the root;
4. preserve hard constraints;
5. report ambiguity instead of inventing history;
6. add less repair cost than full recomputation;
7. maintain acceptable compute overhead.

---

# 86. FAILURE CONDITIONS

The `-3 Backward` operator should be revised or rejected if:

1. reconstruction is mostly hallucinated;
2. provenance does not constrain reconstruction;
3. Shadow must contain the entire original state;
4. error detection does not improve;
5. local repair is not cheaper than global recomputation;
6. ambiguity is routinely hidden;
7. edge reconstruction fails on edge-sensitive tasks;
8. audit cost overwhelms accuracy gain;
9. the operator cannot distinguish exact, approximate, and non-invertible cases;
10. a simpler verifier performs equally well.

---

# 87. RESEARCH STATUS

```text
FACT:
Lossy compression is not generally invertible.

FACT:
Many-to-one maps require extra branch information
for unique reconstruction.

MODEL:
-3 Backward reconstructs child state and local edges
from parent + Shadow + provenance + certificate.

MODEL:
Use component-wise residuals and explicit audit verdicts.

HYPOTHESIS:
Backward reconstruction can detect and localize
reasoning loss before it propagates to the global result.

TEST:
Injected errors, edge flips, branch loss,
constraint loss, order swaps,
Shadow truncation, and audit-frequency experiments.
```

---

# 88. RELATION TO +3 FORWARD

The two operators form a local cycle:

```text
(X1, X2, X3, E)
        |
        v
    +3 FORWARD
        |
        v
       P
        |
        v
    -3 BACKWARD
        |
        v
(X1_hat, X2_hat, X3_hat, E_hat)
```

The core audit quantity is:

```text
original local state
vs
reconstructed local state
```

This cycle is the heart of the method.

---

# 89. WHAT COMES NEXT

The backward operator currently depends on Shadow, but Shadow has only been described as a supporting field.

The next file isolates it as a full memory mechanism.

We need to define:

```text
what enters Shadow
how Shadow is compressed
how long Shadow survives
how it is indexed
when it is deleted
how Shadow differs from uncertainty
how Shadow differs from ordinary memory
```

---

# 90. NEXT FILE

Next:

```text
09_SHADOW_RESIDUAL_MEMORY.md
```

Its purpose is to formalize Shadow as:

> **the explicit memory of information that could not be safely absorbed into the compressed parent.**

It will define:

```text
residual classes
Shadow budget
Shadow lifetime
Shadow retrieval
Shadow compression
Shadow decay
critical residual protection
```

---

## FILE VERDICT

```text
STATE: CRYSTAL

DEFINED:
-3 Backward Operator

INPUT:
Parent
+ interface
+ Shadow
+ certificate
+ provenance

OUTPUT:
reconstructed children
+ reconstructed edges
+ residual vector
+ ambiguity
+ audit verdict

CRITICAL RULE:
-3 Backward does not guarantee reversibility;
it measures reconstructability

CORE CYCLE:
+3 Forward
-> Parent
-> -3 Backward
-> compare
-> PASS / HOLD / EXPAND / RECOMPUTE

NEXT:
09_SHADOW_RESIDUAL_MEMORY.md
```
