# 10 — GATE AND HOLD PROTOCOL

**Project:** Vuzol-19  
**Module:** Hexagram Simplicial Reasoning  
**Status:** LOCAL VERIFICATION / TRANSITION CONTROL SPEC  
**State:** CRYSTAL  
**Language:** English  
**Depends on:** `09_SHADOW_RESIDUAL_MEMORY.md`

---

## 0. PURPOSE

The previous files defined:

```text
state representation
simplex structure
coupling / edge memory
+3 Forward
-3 Backward
Shadow / residual memory
```

This file defines the transition-control layer that decides whether a candidate local state may move upward in the reasoning hierarchy.

That mechanism is:

```text
GATE
```

The Gate does not generate the candidate state.

It evaluates whether the candidate is sufficiently consistent, reconstructable, constraint-safe, and uncertainty-bounded to be promoted.

The complementary state is:

```text
HOLD
```

which prevents unsafe or incomplete local reasoning from contaminating higher levels.

---

# 1. CORE IDEA

The architecture separates:

```text
generation
```

from:

```text
permission to commit
```

Conceptually:

```text
candidate
   |
   v
 GATE
   |
   +--> ALLOW
   |
   +--> HOLD
   |
   +--> EXPAND
   |
   +--> RECOMPUTE
   |
   +--> SHADOW
   |
   +--> UNKNOWN
```

This prevents a fluent or numerically plausible result from being treated as valid by default.

---

# 2. GATE INPUT

A Gate evaluates a candidate parent:

```math
P
=
(z,S,C,U,M,E_{\partial},P_{\mathrm{prov}})
```

together with reconstruction and audit information.

A practical Gate input may contain:

```text
candidate state
reconstruction error
constraint status
coupling status
Shadow risk
uncertainty
provenance integrity
resource budget
operator status
```

---

# 3. MINIMAL GATE FORM

A minimal logical Gate is:

```math
G
=
G_{\mathrm{rec}}
\land
G_{\mathrm{constraint}}
\land
G_{\mathrm{coupling}}
\land
G_{\mathrm{uncertainty}}
```

This can later be extended with:

```math
G_{\mathrm{shadow}}
```

```math
G_{\mathrm{provenance}}
```

```math
G_{\mathrm{resource}}
```

```math
G_{\mathrm{version}}
```

---

# 4. FULL GATE FORM

A more complete logical form is:

```math
G_{\mathrm{full}}
=
G_{\mathrm{rec}}
\land
G_{\mathrm{constraint}}
\land
G_{\mathrm{coupling}}
\land
G_{\mathrm{uncertainty}}
\land
G_{\mathrm{shadow}}
\land
G_{\mathrm{provenance}}
\land
G_{\mathrm{resource}}
```

The exact fields must remain task-dependent.

The purpose of the formula is to make the conditions explicit.

---

# 5. HARD GATES VS SOFT GATES

Separate two categories.

## Hard Gate

A hard Gate condition must be satisfied.

Examples:

```text
hard constraint preserved
critical edge retained
branch identity known when required
sign not inverted
operator version compatible
```

A hard failure normally yields:

```text
HOLD
```

or:

```text
EXPAND
```

## Soft Gate

A soft condition may tolerate bounded error.

Examples:

```text
small approximation residual
moderate uncertainty
low-impact Shadow
small reconstruction error
```

A soft failure may increase risk rather than block automatically.

---

# 6. HARD FAILURE OVERRIDES AVERAGE SCORE

Do not allow a good average score to hide one catastrophic violation.

Example:

```text
reconstruction = excellent
uncertainty    = low
coupling       = correct
hard domain constraint = violated
```

The final verdict must still be:

```text
HOLD
```

Therefore hard conditions should be checked before soft aggregation.

---

# 7. GATE STAGES

Recommended evaluation order:

```text
1. INPUT VALIDITY
2. HARD CONSTRAINTS
3. CRITICAL EDGE CHECK
4. PROVENANCE CHECK
5. RECONSTRUCTION CHECK
6. SHADOW CHECK
7. UNCERTAINTY CHECK
8. RESOURCE CHECK
9. VERDICT
```

This order reduces wasted computation.

If a hard failure appears early, later checks may be skipped.

---

# 8. STAGE 1 — INPUT VALIDITY

Check:

```text
required fields present
schema valid
operator version known
no NaN / invalid numeric state
child IDs resolvable
edge references valid
```

If basic state integrity fails:

```text
HOLD
```

or:

```text
RECOMPUTE
```

---

# 9. STAGE 2 — HARD CONSTRAINT CHECK

Let hard constraints be:

```math
\mathcal{C}_{\mathrm{hard}}
=
\{c_1,c_2,\dots,c_k\}
```

Candidate state `P` must satisfy:

```math
c_i(P)=\mathrm{true}
```

for every required hard condition.

If any hard condition fails:

```text
HOLD
```

unless the correct recovery action is explicitly:

```text
EXPAND
```

or:

```text
RECOMPUTE
```

---

# 10. CONSTRAINT ERROR

For soft numeric constraints, define:

```math
E_{\mathrm{constraint}}
```

Example:

```math
E_{\mathrm{constraint}}
=
\max(0,-x)
```

for the condition:

```math
x\ge0
```

Then a soft threshold may be:

```math
E_{\mathrm{constraint}}
\le
\tau_C
```

---

# 11. STAGE 3 — CRITICAL EDGE CHECK

Let:

```math
E_{\mathrm{critical}}
```

be the set of edges that must survive compression.

A Gate should verify:

```text
edge exists
edge type correct
direction correct
weight or tolerance acceptable
provenance preserved
```

A missing hard edge should normally block promotion.

---

# 12. COUPLING ERROR

For weighted coupling matrices:

```math
E_{\mathrm{coupling}}
=
\|K-\hat{K}\|_F
```

For typed graphs, use field-level mismatch.

A Gate may require:

```math
E_{\mathrm{coupling}}
\le
\tau_E
```

provided all categorical hard relations are also correct.

---

# 13. STAGE 4 — PROVENANCE CHECK

A candidate should be able to answer:

```text
Where did this result come from?
Which child states produced it?
Which edge relations were used?
Which operator version was applied?
```

A provenance failure does not always mean the result is false.

But it weakens auditability.

Possible verdict:

```text
HOLD
```

for high-stakes or exact tasks.

Possible verdict:

```text
ALLOW_WITH_LOW_CONFIDENCE
```

for low-risk exploratory tasks.

---

# 14. PROVENANCE INTEGRITY SCORE

A simple completeness score:

```math
P_{\mathrm{prov}}
=
\frac{
\text{required provenance fields present}
}{
\text{required provenance fields}
}
```

This is only a structural metric.

It does not prove source truth.

---

# 15. STAGE 5 — RECONSTRUCTION CHECK

From `-3 Backward`, obtain:

```math
E_{\mathrm{rec}}
=
d(X,\hat{X})
```

The Gate evaluates:

```math
E_{\mathrm{rec}}
\le
\tau_{\mathrm{rec}}
```

or uses component-wise errors:

```math
\mathbf{E}
=
(
E_{\mathrm{value}},
E_{\mathrm{shape}},
E_{\mathrm{mag}},
E_{\mathrm{edge}},
E_{\mathrm{constraint}}
)
```

A critical component may override the total error.

---

# 16. RECONSTRUCTION CLASS

Use the classes:

```text
EXACT
CERTIFIED_APPROXIMATE
PARTIAL
NON_RECONSTRUCTABLE
```

Possible default policy:

```text
EXACT                  -> may ALLOW
CERTIFIED_APPROXIMATE  -> may ALLOW
PARTIAL                -> depends on critical coverage
NON_RECONSTRUCTABLE    -> HOLD / EXPAND / UNKNOWN
```

---

# 17. CRITICAL COVERAGE

If only part of the original state is reconstructable, measure:

```math
C_{\mathrm{critical}}
=
\frac{
\text{critical fields reconstructed}
}{
\text{critical fields required}
}
```

A Gate may allow a partial reconstruction if:

```math
C_{\mathrm{critical}}=1
```

and noncritical loss is bounded.

---

# 18. STAGE 6 — SHADOW CHECK

The Gate should inspect:

```text
critical unresolved Shadow
Shadow risk
Shadow size
residual debt
branch ambiguity
unresolved constraint Shadow
```

A parent may be numerically stable but still unsafe because a critical residual remains unresolved.

---

# 19. CRITICAL SHADOW RULE

Recommended hard rule:

```text
if critical Shadow is unresolved:
    HOLD
```

unless the task explicitly allows deferred resolution.

This prevents dangerous residual information from being hidden behind a compact parent state.

---

# 20. SHADOW RISK

A candidate risk score:

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

This is a **MODEL**, not a universal formula.

A soft Gate may require:

```math
R_S
\le
\tau_S
```

---

# 21. RESIDUAL DEBT

From the Shadow layer:

```math
D_S
=
\sum_i
w_i M_{S_i}
```

A Gate may reject a state if too much unresolved residual debt accumulates across levels.

This protects against repeated compression that pushes unresolved information downward without ever resolving it.

---

# 22. STAGE 7 — UNCERTAINTY CHECK

Let parent uncertainty be:

```math
U_P
```

A Gate may require:

```math
U_P
\le
\tau_U
```

for high-confidence commit.

But uncertainty thresholds should depend on task risk.

---

# 23. RISK-DEPENDENT THRESHOLD

High-stakes tasks may require:

```text
low uncertainty threshold
strong reconstruction
complete provenance
no critical Shadow
```

Exploratory tasks may allow:

```text
higher uncertainty
partial reconstruction
deferred Shadow
```

Therefore Gate policy must include a task-risk profile.

---

# 24. STAGE 8 — RESOURCE CHECK

A theoretically valid state may still be too expensive to keep expanding indefinitely.

Track:

```text
token budget
memory budget
repair budget
latency budget
Shadow budget
```

Possible verdict when resources are insufficient:

```text
UNKNOWN
```

rather than pretending the state is verified.

---

# 25. RESOURCE FAILURE IS NOT LOGICAL FAILURE

If the system cannot verify due to resource exhaustion:

```text
verification incomplete
```

must not be reported as:

```text
state false
```

or:

```text
state true
```

Use:

```text
UNKNOWN_RESOURCE_LIMIT
```

or equivalent.

---

# 26. GATE VERDICTS

Recommended canonical verdicts:

```text
ALLOW
HOLD
EXPAND
RECOMPUTE
SHADOW
UNKNOWN
```

Optional extensions:

```text
ALLOW_WITH_RESIDUAL
AMBIGUOUS
NON_INVERTIBLE
RESOURCE_LIMIT
VERSION_MISMATCH
```

The core six verdicts should remain stable across the project.

---

# 27. ALLOW

Use:

```text
ALLOW
```

when:

```text
hard constraints pass
critical edges pass
provenance adequate
reconstruction acceptable
critical Shadow resolved
uncertainty acceptable
resource policy satisfied
```

The candidate may then be promoted.

---

# 28. HOLD

Use:

```text
HOLD
```

when:

```text
state cannot yet be trusted
but local repair may resolve it
```

A HOLD state should remain addressable.

It should not be silently discarded.

---

# 29. EXPAND

Use:

```text
EXPAND
```

when the compressed representation lacks enough detail.

Typical trigger:

```text
reconstruction failed in one child
critical Shadow unresolved
branch ambiguity
boundary edge lost
```

Action:

```text
reopen local subtree
```

---

# 30. RECOMPUTE

Use:

```text
RECOMPUTE
```

when the local transformation itself appears wrong.

Difference:

```text
EXPAND:
need more detail

RECOMPUTE:
current local result may be incorrect
```

---

# 31. SHADOW VERDICT

Use:

```text
SHADOW
```

when a result may proceed only if unresolved information remains explicitly attached as residual memory.

This is a controlled deferment.

It should not be equivalent to unconditional ALLOW.

---

# 32. UNKNOWN

Use:

```text
UNKNOWN
```

when available evidence is insufficient.

This is an important safety state.

It is better than fabricated certainty.

---

# 33. GATE AS A STATE MACHINE

```text
CANDIDATE
    |
    v
VALIDATE
    |
    +--> ALLOW
    |
    +--> HOLD
    |
    +--> EXPAND
    |
    +--> RECOMPUTE
    |
    +--> SHADOW
    |
    +--> UNKNOWN
```

After local repair:

```text
EXPAND / RECOMPUTE
        |
        v
new candidate
        |
        v
Gate again
```

---

# 34. GATE SHOULD BE REENTRANT

A node may pass through Gate multiple times.

Example:

```text
candidate v1
-> HOLD
-> expand
-> candidate v2
-> ALLOW
```

Store Gate history.

This supports debugging and learning.

---

# 35. GATE HISTORY

A minimal record:

```text
gate_event_id
parent_id
input_version
checks
verdict
reason
timestamp / step
repair_action
```

This allows analysis of repeated failure patterns.

---

# 36. GATE REASON CODE

Every non-ALLOW verdict should have a reason code.

Examples:

```text
MISSING_CRITICAL_EDGE
RECONSTRUCTION_TOO_HIGH
HARD_CONSTRAINT_FAIL
CRITICAL_SHADOW_UNRESOLVED
UNCERTAINTY_TOO_HIGH
PROVENANCE_INCOMPLETE
RESOURCE_LIMIT
```

Do not return only:

```text
HOLD
```

without explanation.

---

# 37. MULTIPLE FAILURE REASONS

A candidate may fail multiple checks.

Return:

```text
primary reason
secondary reasons
```

Example:

```text
HOLD
primary:
MISSING_CRITICAL_EDGE

secondary:
UNCERTAINTY_TOO_HIGH
PROVENANCE_INCOMPLETE
```

This helps prioritize repair.

---

# 38. REPAIR POLICY

Map failure reasons to repair actions.

Example:

```text
MISSING_CRITICAL_EDGE
-> EXPAND

RECONSTRUCTION_TOO_HIGH
-> EXPAND / RECOMPUTE

HARD_CONSTRAINT_FAIL
-> RECOMPUTE

CRITICAL_SHADOW_UNRESOLVED
-> PROMOTE SHADOW / EXPAND

UNCERTAINTY_TOO_HIGH
-> GATHER EVIDENCE

PROVENANCE_INCOMPLETE
-> RETRIEVE SOURCE
```

---

# 39. GATE SCORE — OPTIONAL

A soft score may summarize quality:

```math
Q_G
=
w_1q_{\mathrm{rec}}
+
w_2q_{\mathrm{edge}}
+
w_3q_{\mathrm{constraint}}
+
w_4q_{\mathrm{uncertainty}}
+
w_5q_{\mathrm{shadow}}
```

But:

> hard failures must not be averaged away.

Use score only after hard checks.

---

# 40. GATE SCORE NORMALIZATION

If component quality scores lie in:

```math
[0,1]
```

then:

```math
Q_G\in[0,1]
```

may be convenient.

Possible threshold:

```math
Q_G\ge\tau_G
```

for soft acceptance.

Again, this is policy, not universal mathematics.

---

# 41. GATE AND FALSE-GREEN

A central Vuzol-19 failure concept is:

```text
FALSE-GREEN
```

Meaning:

```text
the output looks valid
but the process that produced it is broken
```

Gate is intended to detect this class.

Example:

```text
final number correct
but
hard constraint violated during derivation
```

A result should not receive full ALLOW merely because the endpoint matches.

---

# 42. PROCESS VALIDITY VS OUTPUT VALIDITY

Separate:

```text
output_correct
```

from:

```text
process_valid
```

Possible states:

```text
output correct / process valid
output correct / process invalid
output wrong / process valid but incomplete
output wrong / process invalid
```

The Gate should preserve this distinction.

---

# 43. ENDPOINT COINCIDENCE

Two wrong paths may accidentally produce the correct final number.

Therefore verification should include:

```text
route integrity
```

when route correctness matters.

This is especially important in:

```text
proof
scientific derivation
safety reasoning
code execution
```

---

# 44. GATE AND BINDU

Gate decides permission.

Bindu performs commit.

The intended chain is:

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
Bindu
  |
  v
committed state
```

Do not merge Gate and Bindu into one operation.

This separation allows:

```text
verified but not yet committed
```

states.

---

# 45. GATE BEFORE HIGHER COMPRESSION

A candidate parent should not automatically become a child of the next-level `+3 Forward`.

Preferred:

```text
local triad
  |
  v
+3 Forward
  |
  v
candidate parent
  |
  v
Gate
  |
  v
ALLOW
  |
  v
eligible for higher-level grouping
```

This contains local error.

---

# 46. GATE AFTER HIGHER COMPRESSION

Higher-level parents must also pass their own Gate.

Thus:

```text
Gate
```

exists at every level.

The hierarchy becomes:

```text
local synthesis
-> local Gate
-> parent

parent triad
-> higher synthesis
-> higher Gate
-> higher parent
```

---

# 47. LOCAL GATE VS GLOBAL GATE

Local Gate:

```text
checks one compressed region
```

Global Gate:

```text
checks compatibility across major branches
before final commit
```

The same protocol may be reused with different thresholds and scope.

---

# 48. GATE HIERARCHY

Possible levels:

```text
G0 — leaf validity
G1 — local triad
G2 — subtree parent
G3 — cross-branch consistency
G4 — final Bindu pre-commit
```

This is a possible implementation pattern.

The exact number of Gate levels is not fixed.

---

# 49. THRESHOLD CALIBRATION

Gate thresholds should be calibrated empirically.

Do not select:

```text
tau = 0.1
```

only because it looks reasonable.

Use:

```text
validation data
ROC curves
precision/recall
task risk
cost of false allow
cost of false hold
```

---

# 50. FALSE ALLOW

A false allow occurs when:

```text
Gate says ALLOW
but state is invalid
```

This is the most dangerous Gate error in high-risk reasoning.

Define:

```math
R_{\mathrm{FA}}
=
\frac{
\text{invalid states allowed}
}{
\text{invalid states}
}
```

---

# 51. FALSE HOLD

A false hold occurs when:

```text
Gate blocks a valid state
```

Define:

```math
R_{\mathrm{FH}}
=
\frac{
\text{valid states held}
}{
\text{valid states}
}
```

A system can become useless if false hold rate is too high.

---

# 52. GATE TRADEOFF

The Gate balances:

```text
safety
vs
throughput
```

Too permissive:

```text
errors escape
```

Too strict:

```text
reasoning stalls
```

This tradeoff must be measured.

---

# 53. RISK-SENSITIVE LOSS

A Gate learner may optimize:

```math
\mathcal{L}_{G}
=
\lambda_{\mathrm{FA}}
\mathcal{L}_{\mathrm{false\ allow}}
+
\lambda_{\mathrm{FH}}
\mathcal{L}_{\mathrm{false\ hold}}
+
\lambda_{\mathrm{cost}}
\mathcal{L}_{\mathrm{compute}}
```

High-risk tasks may choose:

```math
\lambda_{\mathrm{FA}}
\gg
\lambda_{\mathrm{FH}}
```

---

# 54. GATE LATENCY

Define:

```math
T_G
=
\text{time required for Gate evaluation}
```

If Gate cost approaches or exceeds reasoning cost, the architecture may become impractical.

This must be benchmarked.

---

# 55. GATE COMPUTE OVERHEAD

Define:

```math
C_G
=
\frac{
\mathrm{compute}_{\mathrm{with\ Gate}}
}{
\mathrm{compute}_{\mathrm{without\ Gate}}
}
```

Accuracy gains should always be reported together with `C_G`.

---

# 56. GATE MEMORY OVERHEAD

Gate history, certificates, and Shadow metadata consume memory.

Define:

```math
M_G
=
\mathrm{memory\ overhead\ of\ verification}
```

A good system should avoid storing redundant audit data.

---

# 57. SELECTIVE GATING

Not every node may need full Gate checks.

Possible modes:

```text
FULL
RISK_BASED
RANDOM_SAMPLE
BOUNDARY_ONLY
FINAL_ONLY
```

Risk-based gating is likely the most scalable.

---

# 58. RISK-BASED GATING

Define local risk:

```math
R_P
=
f(
U_P,
R_S,
E_{\mathrm{critical}},
depth,
downstream_impact
)
```

High-risk nodes receive more expensive checks.

Low-risk nodes may use lightweight checks.

---

# 59. LIGHT GATE

Possible light Gate:

```text
schema valid
hard constraints pass
critical edge present
uncertainty below threshold
```

No full reconstruction.

Useful for low-risk intermediate states.

---

# 60. FULL GATE

Possible full Gate:

```text
schema
hard constraints
critical edges
provenance
-3 reconstruction
Shadow audit
uncertainty
resource check
cycle consistency
```

Use before important commits.

---

# 61. ADAPTIVE GATE DEPTH

A Gate may escalate:

```text
LIGHT
  |
  v
uncertain
  |
  v
MEDIUM
  |
  v
still uncertain
  |
  v
FULL
```

This avoids paying maximum audit cost everywhere.

---

# 62. GATE CASCADE

Example:

```text
G1:
hard constraints

G2:
critical edge audit

G3:
reconstruction

G4:
Shadow sweep
```

A state stops at first failure.

This is computationally efficient.

---

# 63. GATE AND LONG CHAINS

The architectural hypothesis is:

```text
local Gate
prevents invalid local states
from entering higher-level compression
```

Thus error propagation path may shorten.

Without Gate:

```text
error
-> parent
-> higher parent
-> root
```

With Gate:

```text
error
-> local candidate
-> HOLD
```

---

# 64. ERROR ESCAPE RATE

From the previous file:

```math
R_{\mathrm{escape}}
=
\frac{
\text{local errors reaching root undetected}
}{
\text{local errors injected}
}
```

A successful Gate should reduce this.

---

# 65. DETECTION DISTANCE

Define:

```math
D_{\mathrm{detect}}
=
\text{levels between error injection and detection}
```

A local Gate should reduce `D_detect`.

---

# 66. HOLD DURATION

A HOLD state may remain unresolved.

Define:

```math
T_{\mathrm{hold}}
=
\text{steps or time spent in HOLD}
```

Long HOLD duration may indicate:

```text
bad repair policy
insufficient evidence
overly strict thresholds
```

---

# 67. HOLD QUEUE

A system may maintain:

```text
HOLD queue
```

with priority based on:

```text
risk
downstream blockage
age
repair cost
importance
```

This prevents unresolved nodes from being forgotten.

---

# 68. HOLD AGING

A HOLD node that remains unresolved should increase priority.

Example:

```math
P_{\mathrm{hold}}(t)
=
P_0+\lambda t
```

unless it is intentionally deferred.

This is a scheduling heuristic.

---

# 69. HOLD IS NOT FAILURE

A HOLD state means:

```text
not enough evidence to safely promote
```

It does not necessarily mean:

```text
the candidate is wrong
```

This distinction should be preserved in logs and training labels.

---

# 70. HOLD TO UNKNOWN

If repeated repair fails and resource budget is exhausted:

```text
HOLD
-> UNKNOWN
```

This is preferable to forcing ALLOW.

---

# 71. HOLD TO SHADOW

Some noncritical unresolved detail may move to Shadow:

```text
HOLD
-> classify residual
-> SHADOW
-> conditional progress
```

Only if policy allows deferred resolution.

Critical unresolved constraints should not take this path.

---

# 72. HOLD TO EXPAND

If the issue is missing detail:

```text
HOLD
-> EXPAND
```

This is the preferred path for reconstruction failures.

---

# 73. HOLD TO RECOMPUTE

If the local result itself is suspicious:

```text
HOLD
-> RECOMPUTE
```

This is the preferred path for operator or arithmetic failure.

---

# 74. GATE POLICY OBJECT

Conceptual structure:

```python
GatePolicy(
    rec_threshold=...,
    coupling_threshold=...,
    uncertainty_threshold=...,
    shadow_threshold=...,
    hard_constraints=[...],
    required_edges=[...],
    risk_profile=...,
    resource_budget=...,
)
```

This makes Gate behavior explicit and configurable.

---

# 75. GATE RESULT OBJECT

Conceptual result:

```python
GateResult(
    verdict=...,
    hard_failures=[...],
    soft_failures=[...],
    scores={...},
    reason_codes=[...],
    repair_action=...,
    audit_level=...,
)
```

This should be logged.

---

# 76. GATE PSEUDOCODE

```python
def evaluate_gate(candidate, audit, policy):
    failures = []
    soft = []

    if not schema_valid(candidate):
        failures.append("INVALID_SCHEMA")

    if not hard_constraints_pass(candidate, policy):
        failures.append("HARD_CONSTRAINT_FAIL")

    if not critical_edges_pass(candidate, policy):
        failures.append("MISSING_CRITICAL_EDGE")

    if not provenance_ok(candidate, policy):
        soft.append("PROVENANCE_INCOMPLETE")

    if audit.reconstruction_error > policy.rec_threshold:
        soft.append("RECONSTRUCTION_TOO_HIGH")

    if audit.coupling_error > policy.coupling_threshold:
        soft.append("COUPLING_TOO_HIGH")

    if critical_shadow_unresolved(candidate):
        failures.append("CRITICAL_SHADOW_UNRESOLVED")

    if candidate.uncertainty > policy.uncertainty_threshold:
        soft.append("UNCERTAINTY_TOO_HIGH")

    if failures:
        return GateResult(
            verdict="HOLD",
            hard_failures=failures,
            soft_failures=soft,
            repair_action=choose_repair(failures, soft),
        )

    if soft:
        return GateResult(
            verdict="EXPAND",
            hard_failures=[],
            soft_failures=soft,
            repair_action=choose_repair([], soft),
        )

    return GateResult(
        verdict="ALLOW",
        hard_failures=[],
        soft_failures=[],
        repair_action=None,
    )
```

This is an interface sketch, not a final policy.

---

# 77. MINIMAL DATA CONTRACT

```python
from dataclasses import dataclass
from typing import Dict, List, Optional

@dataclass
class GateResult:
    verdict: str
    hard_failures: List[str]
    soft_failures: List[str]
    scores: Dict[str, float]
    reason_codes: List[str]
    repair_action: Optional[str]
    audit_level: str
```

---

# 78. GATE TEST — HARD CONSTRAINT

**TEST**

Give a candidate with:

```text
excellent reconstruction
low uncertainty
```

but:

```text
hard constraint violated
```

Expected:

```text
HOLD
```

This verifies hard-failure precedence.

---

# 79. GATE TEST — CRITICAL EDGE LOSS

**TEST**

Remove one critical dependency edge.

Expected:

```text
HOLD
or
EXPAND
```

not:

```text
ALLOW
```

---

# 80. GATE TEST — SMALL RESIDUAL

**TEST**

Inject a small bounded approximation residual.

Expected:

```text
ALLOW
or
ALLOW_WITH_RESIDUAL
```

depending on task policy.

This tests that Gate is not unnecessarily strict.

---

# 81. GATE TEST — HIGH UNCERTAINTY

**TEST**

All hard checks pass, but uncertainty is high.

Expected:

```text
EXPAND
HOLD
or
UNKNOWN
```

depending on policy.

---

# 82. GATE TEST — RESOURCE LIMIT

**TEST**

Verification cannot finish within budget.

Expected:

```text
UNKNOWN / RESOURCE_LIMIT
```

not fabricated ALLOW.

---

# 83. GATE TEST — FALSE-GREEN

**TEST**

Construct a problem where final answer is correct by coincidence but one required derivation edge is wrong.

Expected:

```text
process invalid
```

even though endpoint matches.

This is a direct False-Green test.

---

# 84. GATE TEST — REPAIR LOOP

**TEST**

Inject local error.

Expected sequence:

```text
candidate
-> HOLD
-> EXPAND
-> repair
-> new candidate
-> ALLOW
```

Measure:

```text
repair success
repair cost
levels affected
```

---

# 85. GATE TEST — OVERSTRICT POLICY

**TEST**

Give many valid low-risk nodes.

Measure false hold rate.

If too high, Gate is blocking useful reasoning.

---

# 86. GATE TEST — OVERPERMISSIVE POLICY

**TEST**

Inject invalid states.

Measure false allow rate.

This is the primary safety metric.

---

# 87. ABLATION — NO GATE

Compare:

```text
recursive compression only
```

against:

```text
recursive compression + Gate
```

Measure:

```text
root accuracy
error escape rate
detection distance
compute
memory
```

This determines whether Gate adds real value.

---

# 88. ABLATION — OUTPUT-ONLY GATE

Compare:

```text
output correctness only
```

against:

```text
process + edge + constraint + reconstruction Gate
```

Use False-Green tasks.

---

# 89. ABLATION — NO SHADOW CHECK

Compare:

```text
Gate with Shadow audit
```

versus:

```text
Gate ignoring Shadow
```

Use residual-sensitive problems.

---

# 90. ABLATION — NO PROVENANCE CHECK

Compare:

```text
Gate with provenance
```

versus:

```text
Gate without provenance
```

Use tasks where post-hoc explanations can look plausible.

---

# 91. ABLATION — FULL VS RISK-BASED GATING

Compare:

```text
full audit every node
```

with:

```text
risk-based audit
```

Measure:

```text
accuracy
compute
latency
false allow
false hold
```

---

# 92. PRIMARY SUCCESS CRITERIA

A useful Gate protocol should:

1. reduce false ALLOW on invalid states;
2. reduce error escape to the root;
3. detect missing critical edges;
4. prevent unresolved critical Shadow from silently passing;
5. preserve hard constraints;
6. keep false HOLD within acceptable limits;
7. localize repair;
8. report UNKNOWN when verification is incomplete;
9. improve reliability under comparable compute.

---

# 93. FAILURE CONDITIONS

The Gate protocol should be revised or rejected if:

1. it adds high compute cost without reducing errors;
2. false HOLD rate makes reasoning impractical;
3. false ALLOW remains high;
4. thresholds are brittle across domains;
5. hard and soft failures are not distinguishable;
6. repair loops frequently fail;
7. provenance checks add no measurable value;
8. Shadow checks do not improve residual-sensitive tasks;
9. simpler verifier logic performs equally well;
10. Gate scores become opaque and uncalibrated.

---

# 94. RESEARCH STATUS

```text
FACT:
Verification and generation are distinct operations.

FACT:
Hard constraints should not be averaged away by soft scores.

MODEL:
Gate evaluates reconstruction, constraints, coupling,
uncertainty, Shadow, provenance, and resources.

MODEL:
HOLD prevents unsafe promotion and triggers local repair.

HYPOTHESIS:
Layered local Gate checks reduce error propagation
in long hierarchical reasoning.

TEST:
False-Green, critical-edge, hard-constraint,
residual, uncertainty, resource-limit,
repair-loop, and policy-ablation experiments.
```

---

# 95. RELATION TO PREVIOUS FILES

The local reasoning chain is now:

```text
children
  |
  v
+3 Forward
  |
  v
candidate parent
  |
  +--> Shadow
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
  +--> ALLOW
  +--> HOLD
  +--> EXPAND
  +--> RECOMPUTE
  +--> SHADOW
  +--> UNKNOWN
```

This is the first complete local verification loop in the module.

---

# 96. WHAT COMES NEXT

Gate decides whether a candidate state is permitted to proceed.

But permission is not yet the same as commitment.

The next file defines:

```text
BINDU
```

as the explicit commit point.

Bindu will answer:

```text
When does a verified candidate become
part of the persistent reasoning state?
```

---

# 97. NEXT FILE

Next:

```text
11_BINDU_COMMIT_PROTOCOL.md
```

Its purpose is to formalize:

```text
verified candidate
-> commit conditions
-> state identity
-> immutable record
-> MemoryAtom
-> rollback / reentry rules
```

and to keep:

```text
Gate = permission
```

separate from:

```text
Bindu = commit
```

---

## FILE VERDICT

```text
STATE: CRYSTAL

DEFINED:
Gate and HOLD Protocol

GATE CHECKS:
reconstruction
constraints
coupling
uncertainty
Shadow
provenance
resources

CORE VERDICTS:
ALLOW
HOLD
EXPAND
RECOMPUTE
SHADOW
UNKNOWN

CRITICAL RULE:
generation is not permission,
and permission is not yet commit

NEXT:
11_BINDU_COMMIT_PROTOCOL.md
```
