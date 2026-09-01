# 17 — EXPERIMENTS AND ABLATIONS

**Project:** Vuzol-19  
**Module:** Hexagram Simplicial Reasoning  
**Status:** CANONICAL RESEARCH EXECUTION PLAN  
**State:** CRYSTAL  
**Language:** English  
**Depends on:** `16_AI_ARCHITECTURE_INTEGRATION.md`

---

## 0. PURPOSE

The previous file integrated the full architecture.

This file defines the canonical experimental matrix required to test whether the architecture actually helps.

The central rule is:

> **No component is considered useful because it is conceptually elegant. Every component must survive comparison against simpler alternatives under controlled compute, memory, and task difficulty.**

This file defines:

```text
systems
task families
datasets
metrics
ablation matrix
error injection
compute controls
statistical protocol
success criteria
negative results
```

---

# 1. PRIMARY RESEARCH QUESTION

The main question is:

> **Does explicit hierarchical state, dependency memory, residual tracking, backward audit, Gate verification, and verified commit improve long-reasoning reliability compared with simpler baselines?**

The research target is not:

```text
beautiful geometry
```

The target is:

```text
higher reliable reasoning depth
lower undetected error propagation
better local repair
or better memory/compute efficiency
```

---

# 2. PRIMARY HYPOTHESIS

Let:

```math
A_s(N)
```

be exact-answer accuracy for system `s` at reasoning complexity `N`.

Define:

```math
N_{50}^{(s)}
```

as the first tested complexity where:

```math
A_s(N)<0.5
```

Primary hypothesis:

```math
H_1:
N_{50}^{(\mathrm{full})}
>
N_{50}^{(\mathrm{strong\ baseline})}
```

under comparable inference budget.

---

# 3. SECOND PRIMARY HYPOTHESIS

For injected local errors, define:

```math
R_{\mathrm{escape}}
=
\frac{
\text{errors reaching root undetected}
}{
\text{errors injected}
}
```

Second primary hypothesis:

```math
H_2:
R_{\mathrm{escape}}^{(\mathrm{full})}
<
R_{\mathrm{escape}}^{(\mathrm{strong\ baseline})}
```

This tests verification rather than only raw answer accuracy.

---

# 4. THIRD PRIMARY HYPOTHESIS

For local repair:

```math
S_{\mathrm{repair}}
=
\text{number of nodes recomputed after one local failure}
```

Hypothesis:

```math
H_3:
S_{\mathrm{repair}}^{(\mathrm{hierarchical})}
<
S_{\mathrm{repair}}^{(\mathrm{full\ restart})}
```

while preserving final correctness.

---

# 5. CANONICAL SYSTEM LADDER

Use the following ordered system ladder.

```text
A — Plain LLM

B — LLM + explicit sequential reasoning

C — LLM + summary memory

D — LLM + explicit dependency graph

E — D + recursive grouping / hierarchy

F — E + explicit Coupling / Edge Memory

G — F + Shadow / residual memory

H — G + -3 Backward audit

I — H + Gate

J — I + Bindu / verified persistent memory
```

Optional later systems:

```text
K — J + learned GSL routing

L — K + Hexagram FORM/FLOW controller

M — L + 14/10/10/8 funnel

N — L + alternative learned/adaptive funnel
```

---

# 6. WHY SYSTEM A IS REQUIRED

System A measures the base model without external reasoning structure.

It answers:

```text
How far can the model go unaided?
```

This establishes the natural failure curve.

---

# 7. WHY SYSTEM B IS REQUIRED

System B tests whether simple explicit reasoning already solves most failures.

If:

```text
B ~= full system
```

then the architecture may be unnecessary.

---

# 8. WHY SYSTEM C IS REQUIRED

System C tests ordinary compression by textual summary.

This is a strong conceptual competitor to hierarchical compression.

The architecture must show that:

```text
typed edges
Shadow
audit
Gate
```

add value beyond good summaries.

---

# 9. WHY SYSTEM D IS THE STRONGEST SIMPLE BASELINE

System D stores the dependency graph explicitly.

This baseline already solves much of the:

```text
node memory
vs
edge memory
```

problem.

Therefore:

> **If the full architecture cannot beat or complement an explicit dependency graph, its extra complexity is not justified on that task.**

---

# 10. SYSTEM E — RECURSIVE HIERARCHY

Adds:

```text
local grouping
parent summaries
recursive tree/DAG scaffold
```

No Shadow.

No backward audit.

No Gate.

This isolates whether hierarchy alone helps.

---

# 11. SYSTEM F — COUPLING MEMORY

Adds:

```text
typed edges
directed coupling
critical edge retention
boundary interface
```

This isolates the value of explicit relational state.

---

# 12. SYSTEM G — SHADOW

Adds:

```text
residual storage
omitted critical detail
branch ambiguity
approximation remainder
```

This isolates whether recoverable residual memory improves reliability.

---

# 13. SYSTEM H — BACKWARD AUDIT

Adds:

```text
-3 reconstruction
cycle consistency
component-wise residual
ambiguity detection
```

This tests reconstructability as a local verifier.

---

# 14. SYSTEM I — GATE

Adds explicit promotion control:

```text
ALLOW
HOLD
EXPAND
RECOMPUTE
SHADOW
UNKNOWN
```

This tests whether verification prevents invalid state propagation.

---

# 15. SYSTEM J — BINDU

Adds:

```text
verified commits
MemoryAtom
rollback
reentry
reuse
```

This primarily targets:

```text
persistent multi-step reasoning
repeated subproblem reuse
stale-state control
```

It may not improve one-shot benchmark accuracy.

That distinction must be reported.

---

# 16. OPTIONAL SYSTEM K — GSL ROUTING

Adds learned or rule-based:

```text
R O Y G B V
```

state projection.

The key question is:

```text
Does GSL improve routing, Gate calibration, or repair?
```

If not, it remains a diagnostic visualization.

---

# 17. OPTIONAL SYSTEM L — HEXAGRAM CONTROLLER

Adds:

```text
FORM = (Y,B,V)
FLOW = (R,O,G)
```

with explicit cross-coupling.

Compare against:

```text
flat 6D
random 3+3 grouping
learned grouping
```

---

# 18. OPTIONAL SYSTEM M — 14/10/10/8

Adds the fixed funnel:

```text
14 -> 10 -> 10 -> 8
```

Only after the core architecture is validated.

It must compete against alternative widths.

---

# 19. TASK FAMILY 1 — SYNTHETIC ARITHMETIC GRAPHS

Purpose:

```text
exact graph
exact operations
exact answer
controllable depth
controllable width
```

Variables:

```text
operation count
dependency depth
branching
shared subproblems
noise nodes
cross-edge density
```

This should be the first implementation target.

---

# 20. TASK FAMILY 2 — GSM-INFINITY

Use:

```text
SYMBOLIC
then
MEDIUM
then
HARD
```

Measure:

```text
accuracy collapse
dependency sensitivity
context sensitivity
```

The benchmark adapter must remain separate from the architecture.

---

# 21. TASK FAMILY 3 — LIMITS / ASYMPTOTICS

Use controlled families such as:

```math
\left(
1+\frac{a}{n}
\right)^{bn}
```

and harder variants.

Targets:

```text
rate coupling
remainder control
Shadow
False-Green
```

---

# 22. TASK FAMILY 4 — CONSTRAINT REASONING

Construct problems where:

```text
arithmetic path is locally plausible
but one hard constraint invalidates the result
```

Examples:

```text
domain restrictions
resource constraints
type constraints
ordering constraints
```

This is a direct Gate benchmark.

---

# 23. TASK FAMILY 5 — CODE TRACES

Use:

```text
control-flow graphs
data dependencies
validation order
branching
shared state
```

Targets:

```text
edge retention
temporal order
local repair
shared subproblems
```

Strong baselines:

```text
AST
control-flow graph
static analysis
symbolic execution
```

---

# 24. TASK FAMILY 6 — PLANNING

Synthetic plans with:

```text
resources
timing
constraints
dependencies
fallback branches
```

Targets:

```text
stale state
branching
global vs local constraints
```

---

# 25. TASK FAMILY 7 — CLAIM / EVIDENCE GRAPH

Long-form reasoning over text where:

```text
claims
evidence
counterevidence
conditions
sources
```

form an explicit graph.

This tests whether the architecture transfers beyond symbolic domains.

---

# 26. TASK DIFFICULTY VARIABLES

Every dataset should expose as many of the following as possible:

```text
N_op          — required operation count
D_dep         — dependency depth
W_graph       — graph width
N_nodes       — total nodes
N_edges       — total edges
R_noise       — irrelevant-node ratio
C_cross       — cross-group coupling
N_shared      — shared subproblems
N_constraints — active constraints
```

---

# 27. DEPTH SWEEP

Fix:

```text
graph width
noise
operation type
```

Increase:

```math
D_{\mathrm{dep}}
```

Measure:

```text
accuracy
N80
N50
error escape
active memory
```

This isolates long-chain dependence.

---

# 28. WIDTH SWEEP

Fix depth.

Increase:

```text
number of simultaneously active branches
```

This tests active-memory overload.

---

# 29. NOISE SWEEP

Keep required graph unchanged.

Increase irrelevant information.

Measure:

```text
node precision
edge precision
active memory
accuracy
```

This tests filtering.

---

# 30. CROSS-EDGE SWEEP

Increase dependencies crossing hierarchy boundaries.

Hypothesis:

```text
tree-like compression becomes less useful
as cross-boundary critical coupling rises
```

This is a key structural limit.

---

# 31. SHARED-SUBPROBLEM SWEEP

Increase reuse of one verified node across branches.

This should favor:

```text
DAG references
Bindu reuse
incremental recomputation
```

---

# 32. CONSTRAINT-DENSITY SWEEP

Increase:

```text
number of active hard/soft constraints
```

Measure:

```text
false allow
false hold
Gate cost
```

---

# 33. PRIMARY METRIC — EXACT ACCURACY

```math
A_{\mathrm{exact}}
=
\frac{
\text{exactly correct final answers}
}{
\text{all tasks}
}
```

Use exact comparison for synthetic tasks whenever possible.

---

# 34. PROCESS VALIDITY

Define:

```math
A_{\mathrm{process}}
=
\frac{
\text{valid required reasoning routes}
}{
\text{all evaluated outputs}
}
```

This is required for False-Green analysis.

---

# 35. FALSE-GREEN RATE

```math
R_{\mathrm{FG}}
=
\frac{
\text{correct endpoints with invalid required process}
}{
\text{correct endpoints}
}
```

This is a core Vuzol-19 metric.

---

# 36. N80 / N50

For accuracy curve:

```math
A(N)
```

define:

```text
N80:
first difficulty where accuracy < 80%

N50:
first difficulty where accuracy < 50%
```

Use interpolation only if clearly documented.

---

# 37. AREA UNDER REASONING CURVE

For discrete difficulty levels:

```math
AURC
=
\sum_{k}
A(N_k)\Delta N_k
```

Normalize if comparisons use different ranges.

---

# 38. EDGE PRECISION

```math
P_{\mathrm{edge}}
=
\frac{
|E^*\cap\hat{E}|
}{
|\hat{E}|
}
```

Measures spurious relation creation.

---

# 39. EDGE RECALL

```math
R_{\mathrm{edge}}
=
\frac{
|E^*\cap\hat{E}|
}{
|E^*|
}
```

Measures lost required relations.

---

# 40. EDGE F1

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

when denominator is nonzero.

---

# 41. CRITICAL EDGE RECALL

Define:

```math
E^*_{\mathrm{critical}}
```

as required edges whose removal can change the correct output.

Then:

```math
R_{\mathrm{critical}}
=
\frac{
|E^*_{\mathrm{critical}}
\cap
\hat{E}|
}{
|E^*_{\mathrm{critical}}|
}
```

This may matter more than total edge recall.

---

# 42. PATH RETENTION

Measure whether ordered required dependency paths survive:

```math
R_{\mathrm{path}}
=
\frac{
\text{required paths retained}
}{
\text{required paths}
}
```

Useful for temporal and noncommutative tasks.

---

# 43. RECONSTRUCTION ERROR

At each compressed node:

```math
E_{\mathrm{rec}}
=
d(X,\hat{X})
```

Report by depth:

```text
leaf parent
middle parent
root parent
```

---

# 44. RECONSTRUCTION DRIFT

```math
D_{\mathrm{rec}}
=
E_{\mathrm{rec}}^{(\mathrm{root})}
-
E_{\mathrm{rec}}^{(\mathrm{lowest\ level})}
```

Large positive drift indicates cumulative compression loss.

---

# 45. SHADOW RATIO

```math
\rho_S
=
\frac{
\mathrm{Shadow\ size}
}{
\mathrm{original\ represented\ size}
}
```

Also report:

```math
\rho_{\mathrm{total}}
=
\frac{
\mathrm{parent + Shadow + metadata}
}{
\mathrm{original}
}
```

---

# 46. ACTIVE MEMORY

Measure:

```math
M_{\mathrm{active}}
```

separately from total persistent storage.

The architecture may still be useful if:

```text
total memory similar
but active memory much lower
```

---

# 47. TOTAL MEMORY

Include:

```text
active nodes
Shadow
edge memory
provenance
Gate history
MemoryAtoms
```

Do not hide audit overhead.

---

# 48. ERROR DETECTION DISTANCE

For injected errors:

```math
D_{\mathrm{detect}}
=
\text{levels between injection and first detection}
```

Lower is better.

---

# 49. ERROR ESCAPE RATE

```math
R_{\mathrm{escape}}
=
\frac{
\text{errors reaching root undetected}
}{
\text{errors injected}
}
```

This is one of the strongest Gate metrics.

---

# 50. REPAIR SPAN

```math
S_{\mathrm{repair}}
=
\text{nodes recomputed after error}
```

Compare to:

```text
full restart
```

---

# 51. REPAIR SUCCESS

```math
R_{\mathrm{repair}}
=
\frac{
\text{corrupted tasks restored to correct answer}
}{
\text{corrupted tasks where repair attempted}
}
```

---

# 52. REOPEN RATE

```math
R_{\mathrm{open}}
=
\frac{
\text{subtree expansions}
}{
\text{subtree uses}
}
```

High reopen rate indicates poor compression policy.

---

# 53. GROUP CHURN RATE

```math
R_{\mathrm{churn}}
=
\frac{
\text{regrouping events}
}{
\text{reasoning steps}
}
```

High values indicate unstable hierarchy.

---

# 54. FALSE ALLOW

```math
R_{\mathrm{FA}}
=
\frac{
\text{invalid states allowed}
}{
\text{invalid states}
}
```

Primary safety metric for Gate.

---

# 55. FALSE HOLD

```math
R_{\mathrm{FH}}
=
\frac{
\text{valid states blocked}
}{
\text{valid states}
}
```

Primary usability metric for Gate.

---

# 56. UNKNOWN RATE

```math
R_{\mathrm{unknown}}
=
\frac{
\text{tasks ending UNKNOWN}
}{
\text{all tasks}
}
```

Report alongside accuracy.

UNKNOWN may be preferable to false confidence.

---

# 57. CALIBRATION

If systems output confidence, measure:

```text
Brier score
Expected Calibration Error
reliability curve
```

Especially useful for Gate thresholds.

---

# 58. COMPUTE METRICS

Report:

```text
input tokens
generated tokens
LLM calls
tool calls
GPU-seconds if available
wall-clock latency
estimated monetary cost if applicable
```

---

# 59. EQUAL-COMPUTE COMPARISON

Fix a budget:

```text
same model
similar total generated tokens
similar number of calls
```

Then compare accuracy and reliability.

This is the main fairness mode.

---

# 60. EQUAL-ACCURACY COMPARISON

Find the compute required to reach:

```text
80%
90%
or another target accuracy
```

Then compare efficiency.

---

# 61. EQUAL-MEMORY COMPARISON

Fix:

```text
active memory budget
```

and compare performance.

This directly tests whether hierarchical compression extends reasoning under bounded active memory.

---

# 62. PARAMETER MATCHING

For learned funnel comparisons, control:

```text
parameter count
hidden size
training steps
optimizer
dataset
```

or report differences explicitly.

---

# 63. MODEL MATCHING

All architecture comparisons should use the same base model version unless the experiment explicitly studies model scale.

---

# 64. PROMPT MATCHING

Prompts should be:

```text
identical where possible
versioned
hashed
stored
```

Architecture-specific instructions should be isolated and documented.

---

# 65. RANDOM SEEDS

Use multiple seeds for:

```text
dataset generation
model sampling
grouping
training initialization
```

when applicable.

---

# 66. HELD-OUT TESTING

Do not tune on the entire complexity range.

Example:

```text
train/tune:
N = 5..20

validation:
N = 21..30

test:
N = 31..100
```

This tests scaling beyond the calibration region.

---

# 67. HELD-OUT GRAPH SHAPES

Tune on:

```text
chains
```

test on:

```text
branching DAGs
shared dependencies
high cross-edge graphs
```

This tests structural generalization.

---

# 68. HELD-OUT OPERATION COMBINATIONS

For synthetic arithmetic, hold out combinations such as:

```text
nested subtraction after multiplication
reverse operations
shared intermediate values
```

This reduces template memorization.

---

# 69. ERROR INJECTION MATRIX

Inject errors by type:

```text
VALUE
EDGE
OPERATOR
ORDER
CONSTRAINT
PROVENANCE
SHADOW
BRANCH
SIGN
VERSION
```

and by depth:

```text
LEAF
MID
ROOT-NEAR
```

---

# 70. VALUE ERROR

Change:

```text
17 -> 19
```

Measure:

```text
detection
repair
root impact
```

---

# 71. EDGE ERROR

Change:

```text
A -> B
```

to:

```text
A -> C
```

while keeping node values unchanged if possible.

This tests structural memory.

---

# 72. OPERATOR ERROR

Replace:

```text
+
```

with:

```text
-
```

or another valid operator.

---

# 73. ORDER ERROR

Swap noncommutative or dependency-sensitive operations.

This tests temporal edges.

---

# 74. CONSTRAINT ERROR

Remove, alter, or misapply a hard constraint.

This is a direct Gate test.

---

# 75. PROVENANCE ERROR

Attach a correct intermediate value to the wrong source.

This tests whether audit checks route identity rather than number coincidence.

---

# 76. SHADOW ERROR

Delete or corrupt one critical residual.

Measure whether:

```text
-3
Gate
or
final audit
```

detects the loss.

---

# 77. BRANCH ERROR

In a many-to-one mapping, erase branch identity.

Expected:

```text
AMBIGUOUS
```

rather than arbitrary reconstruction.

---

# 78. SIGN ERROR

Flip one signed critical value.

Use asymptotic and algebraic tasks.

---

# 79. VERSION ERROR

Attempt reentry with incompatible operator or schema version.

Expected:

```text
VERSION_MISMATCH
HOLD
or
migration
```

---

# 80. ERROR MAGNITUDE SWEEP

For numeric perturbations:

```math
\delta
\in
\{
10^{-6},
10^{-4},
10^{-2},
1,
10
\}
```

or task-appropriate scales.

This tests sensitivity.

---

# 81. CRITICALITY SWEEP

Inject:

```text
critical errors
noncritical errors
```

A good system should avoid overreacting to irrelevant perturbations.

---

# 82. ABLATION — NO COUPLING

Remove edge memory.

Compare:

```text
F
vs
E
```

Primary target:

```text
edge-sensitive accuracy
critical edge recall
```

---

# 83. ABLATION — NO SHADOW

Compare:

```text
G
vs
F
```

Primary target:

```text
reconstruction
residual-sensitive tasks
repair success
```

---

# 84. ABLATION — NO BACKWARD

Compare:

```text
H
vs
G
```

Primary target:

```text
error detection distance
escape rate
false allow
```

---

# 85. ABLATION — NO GATE

Compare:

```text
I
vs
H
```

Primary target:

```text
False-Green
false allow
root corruption
```

---

# 86. ABLATION — NO BINDU

Compare:

```text
J
vs
I
```

Primary target:

```text
reuse
rollback
stale state
persistent audit
```

Do not expect large one-shot answer gains necessarily.

---

# 87. ABLATION — NO PROVENANCE

Remove source lineage while retaining values.

Use equifinality and post-hoc reconstruction tasks.

---

# 88. ABLATION — NO CRITICAL-EDGE PRIORITY

Store edges uniformly.

Compare with risk-weighted edge retention.

---

# 89. ABLATION — FULL TRACE VS SHADOW

Compare:

```text
store full local history
```

against:

```text
compressed parent + Shadow
```

Measure:

```text
memory
reconstruction
latency
```

---

# 90. ABLATION — RANDOM GROUPING

Compare:

```text
dependency-aware grouping
```

against:

```text
random 3-way grouping
```

This is essential.

If random grouping performs equally, the geometric grouping story is weak.

---

# 91. ABLATION — BINARY / TERNARY / VARIABLE

Compare:

```text
2-way
3-way
4-way
variable branching
```

under comparable compute.

---

# 92. ABLATION — FLAT 6D VS HEXAGRAM

Compare:

```text
flat GSL 6D
```

against:

```text
FORM/FLOW grouping
```

and:

```text
random 3+3 split
```

If no difference exists, Hexagram is diagnostic only.

---

# 93. ABLATION — GSL OFF

Compare scheduler and Gate with and without GSL input.

Measure:

```text
routing quality
Gate calibration
repair priority
```

---

# 94. ABLATION — 14/10/10/8

Compare against:

```text
14->8
14->10->8
14->12->10->8
14->10->10->8
14->14->14->14
learned width
adaptive width
```

Use matched compute.

---

# 95. STAGE-SPECIFIC FUNNEL ABLATION

Remove one transformation role:

```text
Role -> Form
Form -> Transition
Transition -> Current
```

Measure where performance changes.

---

# 96. ABLATION — FIXED VS LEARNED GROUPING

Compare:

```text
hand-defined grouping
graph-cut grouping
learned grouping
```

This tests whether triad structure must be learned.

---

# 97. ABLATION — DETERMINISTIC VS LEARNED BACKWARD

Compare:

```text
symbolic reconstruction
learned decoder
hybrid
```

Measure hallucinated provenance separately.

---

# 98. ABLATION — LIGHT VS FULL GATE

Compare:

```text
hard checks only
```

against:

```text
hard + reconstruction + Shadow + provenance
```

Measure compute/reliability tradeoff.

---

# 99. ABLATION — EVERY NODE VS RISK-BASED GATE

Compare:

```text
full audit every node
```

with:

```text
risk-based selective audit
```

Expected result:

```text
similar reliability
lower compute
```

if risk-based scheduling works.

---

# 100. ABLATION — LOCAL VS ROOT-ONLY GATE

Compare:

```text
verify only final root
```

against:

```text
verify every local parent
```

Primary metrics:

```text
detection distance
error escape
compute
```

---

# 101. ABLATION — SHADOW PRIORITY

Compare:

```text
critical Shadow selection
random Shadow selection
largest-magnitude residual
learned priority
```

under equal Shadow budget.

---

# 102. ABLATION — SHADOW BUDGET

Sweep:

```text
0%
10%
25%
50%
100%
```

relative residual budget.

Measure the reliability/memory curve.

---

# 103. ABLATION — ADAPTIVE DEPTH

Compare:

```text
fixed tree depth
```

against:

```text
uncertainty-driven depth
```

and:

```text
Gate-driven depth
```

---

# 104. ABLATION — REBALANCING

Compare:

```text
static hierarchy
```

against:

```text
dynamic rebalancing
```

on changing or online tasks.

---

# 105. ABLATION — REUSE

Compare:

```text
no reuse
```

against:

```text
verified subtree reuse
```

Measure:

```text
compute saved
stale-state failures
reentry Gate accuracy
```

---

# 106. EXPERIMENT PHASE 0 — UNIT TESTS

Before LLM experiments:

```text
test data structures
test graph updates
test +3 exact cases
test -3 exact cases
test Shadow integrity
test Gate hard failures
test Bindu atomicity
```

All deterministic unit tests should pass.

---

# 107. PHASE 1 — SYMBOLIC ORACLE GRAPH

No graph extraction.

Use exact graph.

Goal:

```text
test hierarchy / audit / Gate
without semantic parsing noise
```

---

# 108. PHASE 2 — LLM + ORACLE GRAPH

LLM performs local reasoning.

Graph remains exact.

This isolates model reasoning from graph extraction.

---

# 109. PHASE 3 — INFERRED GRAPH

LLM or parser builds graph.

Measure:

```text
graph extraction accuracy
```

separately.

---

# 110. PHASE 4 — LOSSY COMPRESSION

Enable:

```text
hierarchy
Shadow
backward audit
```

Measure:

```text
memory savings
reconstruction
repair
```

---

# 111. PHASE 5 — GATE

Calibrate on held-out valid/invalid local states.

Target:

```text
low false allow
acceptable false hold
```

---

# 112. PHASE 6 — REUSE / BINDU

Add persistent MemoryAtoms.

Use repeated-task suites.

---

# 113. PHASE 7 — GSL / HEXAGRAM

Only after core reliability is measurable.

Test whether interpretable state improves:

```text
routing
repair
Gate thresholding
```

---

# 114. PHASE 8 — FUNNEL

Only after the architecture works without it.

This isolates the 14/10/10/8 hypothesis.

---

# 115. PHASE 9 — CROSS-DOMAIN

Move from:

```text
synthetic arithmetic
```

to:

```text
code
planning
text evidence graphs
```

General claims should wait until this phase.

---

# 116. STATISTICAL SAMPLE SIZE

Use enough examples per difficulty point to estimate accuracy with useful confidence intervals.

Do not rely on:

```text
10 examples
```

for small performance differences.

The exact sample size should be selected from:

```text
expected effect size
variance
desired confidence
compute budget
```

---

# 117. CONFIDENCE INTERVALS

For accuracy-like proportions, report:

```text
95% confidence interval
```

using an appropriate binomial method.

Avoid reporting only the mean.

---

# 118. MULTIPLE COMPARISONS

The ablation matrix may contain many comparisons.

For formal significance claims, account for multiple testing or preregister primary contrasts.

Do not selectively report only favorable comparisons.

---

# 119. EFFECT SIZE

Report:

```text
absolute accuracy difference
relative error reduction
N50 shift
compute ratio
memory ratio
```

not only p-values.

---

# 120. BOOTSTRAP

For metrics such as:

```text
AURC
N50
repair span
```

bootstrap confidence intervals may be useful.

Use consistent resampling procedure.

---

# 121. SEED REPORTING

For stochastic systems, report:

```text
mean
standard deviation
all seeds or seed range
```

A result that exists under one seed only is weak evidence.

---

# 122. MODEL VERSIONING

Store:

```text
base model ID
date/version
sampling parameters
temperature
top_p
max tokens
system prompt hash
```

Model updates can change benchmark results.

---

# 123. ARCHITECTURE VERSIONING

Store:

```text
Vuzol runtime version
Gate policy version
Shadow schema
grouping policy
funnel config
```

Every result should be reproducible.

---

# 124. DATASET VERSIONING

Store:

```text
generator commit
dataset hash
benchmark split
seed
difficulty parameters
```

---

# 125. TRAIN / VALIDATION / TEST SPLIT

Use:

```text
TRAIN:
learned modules

VALIDATION:
threshold selection
policy tuning

TEST:
final locked evaluation
```

Do not tune Gate on test outcomes.

---

# 126. PREREGISTERED PRIMARY COMPARISONS

Recommended first locked comparisons:

```text
D vs I
D vs J
E vs H
F vs G
G vs H
H vs I
```

Primary metrics:

```text
N50
error escape
false allow
repair span
active memory
```

---

# 127. PREREGISTERED FAILURE BOUNDARY

Also preregister:

```text
high cross-edge density
```

as a condition expected to reduce hierarchy benefit.

Predicting where the method fails is part of the theory.

---

# 128. NULL RESULT POLICY

Accept:

```text
no significant difference
```

as a valid result.

Do not reinterpret every null as:

```text
implementation not mature enough
```

unless there is independent evidence of implementation failure.

---

# 129. NEGATIVE RESULT POLICY

If a simpler baseline wins:

```text
document it
simplify the architecture
retain only useful components
```

This is a success of the research process.

---

# 130. COMPONENT SURVIVAL RULE

A component stays in the canonical architecture only if it provides at least one reproducible benefit:

```text
accuracy
reliability
repairability
memory
compute
interpretability with operational value
```

Otherwise mark it:

```text
OPTIONAL
EXPERIMENTAL
or
REMOVE
```

---

# 131. PARETO FRONTIER

Compare systems on:

```text
accuracy
compute
active memory
total memory
false allow
repair span
```

A system is interesting if it lies near the Pareto frontier.

There may be no single best system.

---

# 132. RESEARCH UTILITY SCORE — OPTIONAL

If one composite score is needed:

```math
U
=
w_A A
-
w_C C
-
w_M M
-
w_{FA}R_{FA}
-
w_R S_{\mathrm{repair}}
```

But the weights are normative.

Therefore report raw metrics first.

Use composite utility only as a secondary summary.

---

# 133. MAIN RESULT TABLE

Recommended table:

| System | Exact Acc. | Process Validity | N80 | N50 | Critical Edge Recall | False Allow | Error Escape | Repair Span | Active Memory | Total Memory | Compute |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| A | | | | | | | | | | | |
| B | | | | | | | | | | | |
| C | | | | | | | | | | | |
| D | | | | | | | | | | | |
| E | | | | | | | | | | | |
| F | | | | | | | | | | | |
| G | | | | | | | | | | | |
| H | | | | | | | | | | | |
| I | | | | | | | | | | | |
| J | | | | | | | | | | | |

---

# 134. MAIN ABLATION TABLE

| Ablation | Remove / Change | Primary Metric | Interpretation |
|---|---|---|---|
| Coupling | remove edge memory | edge recall / accuracy | tests relation memory |
| Shadow | remove residual store | reconstruction / repair | tests residual value |
| -3 | remove backward audit | escape / detection | tests reconstructability |
| Gate | remove local verification | false allow | tests transition control |
| Bindu | remove persistent commit | reuse / rollback | tests persistent state |
| GSL | remove 6D state | routing / calibration | tests diagnostic control value |
| Hexagram | flatten 6D | routing / accuracy | tests FORM/FLOW grouping |
| Triads | use flat graph | memory / repair | tests hierarchy |
| Funnel | remove 14/10/10/8 | accuracy / memory | tests funnel |
| Ternary | use binary/variable | N50 / compute | tests branching factor |

---

# 135. REQUIRED PLOTS

Generate at least:

```text
1. accuracy vs dependency depth
2. accuracy vs required operation count
3. N50 by system
4. error escape vs depth
5. false allow vs depth
6. critical edge recall vs depth
7. active memory vs depth
8. total memory vs depth
9. repair span vs injection depth
10. accuracy vs compute
11. Shadow ratio vs reconstruction error
12. cross-edge density vs hierarchy benefit
```

---

# 136. HIERARCHY BENEFIT CURVE

Define:

```math
B_{\mathrm{hier}}
=
A_{\mathrm{hierarchy}}
-
A_{\mathrm{graph}}
```

Plot against:

```math
C_{\mathrm{cross}}
```

Hypothesis:

```text
benefit decreases as cross-edge density rises
```

This would identify the structural regime where hierarchy helps.

---

# 137. SHADOW TRADEOFF CURVE

Plot:

```text
Shadow budget
vs
reconstruction accuracy
vs
total memory
```

Look for a knee point.

---

# 138. GATE TRADEOFF CURVE

Plot:

```text
false allow
vs
false hold
```

across thresholds.

This is analogous to a verification operating curve.

---

# 139. ACTIVE MEMORY CURVE

Plot:

```math
M_{\mathrm{active}}(N)
```

for:

```text
full trace
summary
graph
hierarchical system
```

This directly tests bounded active memory.

---

# 140. REPAIR CURVE

Plot:

```text
injection depth
vs
repair span
```

for:

```text
full restart
dependency graph incremental
Vuzol local repair
```

---

# 141. ORACLE VS INFERRED GRAPH

Run both:

```text
oracle graph
inferred graph
```

Define gap:

```math
G_{\mathrm{oracle}}
=
A_{\mathrm{oracle}}
-
A_{\mathrm{inferred}}
```

Large gap means graph extraction is the bottleneck.

---

# 142. GRAPH EXTRACTION METRICS

Measure:

```text
node precision
node recall
edge precision
edge recall
edge type accuracy
operator type accuracy
topological order accuracy
```

This prevents architecture failures from being misattributed.

---

# 143. HUMAN-EVALUATED TASKS

For text reasoning where exact graph truth is unavailable, use human evaluation only after strong synthetic validation.

Evaluation rubric should distinguish:

```text
final correctness
source faithfulness
constraint preservation
unsupported inference
uncertainty handling
```

---

# 144. LLM-AS-JUDGE WARNING

Do not use one LLM judge as the only evaluator of another LLM's reasoning.

For exact synthetic tasks, prefer deterministic evaluation.

For semantic tasks, use:

```text
multiple judges
human spot checks
agreement metrics
```

---

# 145. LEAKAGE CONTROL

Do not include:

```text
test answers
oracle graph
critical-edge labels
```

in system prompts unless the condition explicitly studies oracle information.

---

# 146. BENCHMARK CONTAMINATION

For public benchmarks, acknowledge that modern models may have training exposure.

Synthetic regenerated tasks reduce this risk.

Therefore emphasize:

```text
controlled generated variants
```

for causal architecture comparisons.

---

# 147. STOPPING RULE

A reasoning run ends when:

```text
root Bindu commit
```

or:

```text
resource budget exhausted
```

or:

```text
UNKNOWN declared
```

or:

```text
maximum repair attempts reached
```

Stopping policy must be identical across comparable systems where possible.

---

# 148. MAXIMUM REPAIR ATTEMPTS

Set:

```text
max_repair
```

before evaluation.

Do not allow the full system unlimited retries against a one-shot baseline.

---

# 149. RETRY BUDGET

If baseline systems receive self-consistency or retries, report:

```text
number of samples
aggregation rule
total tokens
```

and give comparable budget to architecture systems.

---

# 150. FAILURE TAXONOMY

Classify failures as:

```text
F1 — wrong node value
F2 — missing edge
F3 — wrong edge type
F4 — wrong order
F5 — constraint drift
F6 — provenance failure
F7 — Shadow loss
F8 — premature commit
F9 — stale reuse
F10 — grouping failure
F11 — graph extraction failure
F12 — resource exhaustion
```

This helps diagnose gains.

---

# 151. FAILURE CONFUSION MATRIX

For each system, count which true injected failures were classified as which detected failure class.

This tests not only detection but diagnosis.

---

# 152. REPAIR ACTION ACCURACY

Given a detected failure, evaluate whether the chosen action was correct:

```text
EXPAND
RECOMPUTE
PROMOTE SHADOW
RETRIEVE SOURCE
ROLLBACK
UNKNOWN
```

Define:

```math
A_{\mathrm{repair\ action}}
```

---

# 153. GATE REASON-CODE ACCURACY

Measure whether Gate reason codes match ground-truth failure type on synthetic tasks.

This tests interpretability as operational diagnosis.

---

# 154. MEMORY REUSE METRICS

For Bindu:

```text
reuse hit rate
valid reuse rate
stale reuse rate
reentry false allow
reentry false hold
compute saved
```

---

# 155. REUSE HIT RATE

```math
H_{\mathrm{reuse}}
=
\frac{
\text{tasks where a stored MemoryAtom was applicable}
}{
\text{tasks where reuse was attempted}
}
```

---

# 156. VALID REUSE RATE

```math
R_{\mathrm{valid\ reuse}}
=
\frac{
\text{reused states still valid in current context}
}{
\text{reused states}
}
```

---

# 157. STALE REUSE RATE

```math
R_{\mathrm{stale}}
=
\frac{
\text{invalid stale reused states}
}{
\text{reused states}
}
```

This should be near zero for a successful reentry Gate.

---

# 158. ROLLBACK SUCCESS

```math
R_{\mathrm{rollback}}
=
\frac{
\text{failed sessions recovered by rollback}
}{
\text{rollback attempts}
}
```

---

# 159. MINIMUM PASS CONDITION FOR CORE ARCHITECTURE

Before adding GSL / Hexagram / funnel, require the core system:

```text
D + hierarchy + Coupling + Shadow + -3 + Gate
```

to show at least one of:

```text
higher N50
lower error escape
smaller repair span
lower active memory at equal accuracy
```

relative to explicit dependency graph baseline.

---

# 160. MINIMUM PASS CONDITION FOR GSL

GSL remains in the control path only if it improves:

```text
Gate calibration
scheduler routing
failure prediction
repair priority
```

on held-out data.

---

# 161. MINIMUM PASS CONDITION FOR HEXAGRAM

Hexagram remains a computational component only if:

```text
FORM/FLOW grouping
```

beats:

```text
flat 6D
or
random 3+3 grouping
```

on at least one meaningful control metric.

Otherwise keep it as visualization only.

---

# 162. MINIMUM PASS CONDITION FOR FUNNEL

The fixed funnel remains canonical only if:

```text
14/10/10/8
```

is competitive with matched alternative widths on the Pareto frontier.

Otherwise mark:

```text
EXPERIMENTAL
```

or replace with adaptive width.

---

# 163. SCIENTIFIC CLAIM LEVELS

Use claim levels.

```text
LEVEL 0:
prototype runs

LEVEL 1:
component improves synthetic task metric

LEVEL 2:
component survives ablations

LEVEL 3:
result replicates across models / seeds

LEVEL 4:
result transfers across domains

LEVEL 5:
practical advantage under real workload
```

Do not jump from Level 0 to universal claims.

---

# 164. CLAIM TEMPLATE

A defensible paper-style statement:

> Under matched inference budget on controlled long-dependency tasks, the full verified hierarchy reduced undetected local error propagation relative to an explicit dependency-graph baseline, while using X% less active memory / improving N50 by Y.

Only fill `X` and `Y` after measured experiments.

---

# 165. NEGATIVE CLAIM TEMPLATE

Also prepare:

> The explicit dependency graph baseline matched or exceeded the full architecture, indicating that the additional hierarchical / Shadow / Gate machinery did not provide sufficient benefit under the tested conditions.

This is a valid scientific outcome.

---

# 166. REPRODUCIBLE EXPERIMENT DIRECTORY

Recommended structure:

```text
experiments/
|
+-- configs/
|   +-- system_A.yaml
|   +-- system_D.yaml
|   +-- system_I.yaml
|
+-- datasets/
|
+-- runners/
|
+-- logs/
|
+-- metrics/
|
+-- results/
|
+-- plots/
|
+-- reports/
```

---

# 167. RUN MANIFEST

Every run should create:

```text
run_id
timestamp
git commit
model ID
dataset hash
system config
seed
budget
metrics
artifact paths
```

---

# 168. RESULT LOCKING

Once the test set is evaluated:

```text
do not silently modify thresholds
```

If changes are made, create a new experiment version.

This preserves scientific integrity.

---

# 169. IMPLEMENTATION PRIORITY

First executable ablation set should be:

```text
A — plain baseline
D — dependency graph
E — graph + recursive grouping
G — + Coupling + Shadow
H — + backward audit
I — + Gate
```

Skip Bindu, GSL, Hexagram, funnel in the first pass.

This keeps the first experiment interpretable.

---

# 170. FIRST SUCCESS TARGET

A strong first target is not necessarily higher raw accuracy.

It may be:

```text
same final accuracy
but
lower error escape
and
smaller repair span
```

That would already validate the verification architecture.

---

# 171. SECOND SUCCESS TARGET

Then test whether the architecture shifts:

```text
N50
```

under bounded active memory.

This addresses the long-reasoning goal directly.

---

# 172. THIRD SUCCESS TARGET

Then test:

```text
verified subtree reuse
```

with Bindu/MemoryAtom.

This addresses persistent reasoning memory.

---

# 173. COMPLETE EXPERIMENT FLOW

```text
UNIT TESTS
   |
   v
ORACLE GRAPH
   |
   v
BASELINE CURVES
   |
   v
HIERARCHY
   |
   v
COUPLING
   |
   v
SHADOW
   |
   v
-3 AUDIT
   |
   v
GATE
   |
   v
ERROR INJECTION
   |
   v
RESOURCE-MATCHED TEST
   |
   v
BINDU REUSE
   |
   v
GSL / HEXAGRAM
   |
   v
14/10/10/8
   |
   v
CROSS-DOMAIN TEST
```

---

# 174. RESEARCH STATUS

```text
FACT:
Ablation studies are required to attribute gains
inside a multi-component architecture.

FACT:
Accuracy alone cannot measure verification,
repair, or memory efficiency.

MODEL:
Use a canonical system ladder A-J
and controlled task-difficulty sweeps.

HYPOTHESIS:
Coupling + Shadow + backward audit + Gate
will reduce undetected reasoning-error propagation.

TEST:
Matched-compute experiments,
error injection,
hierarchy/coupling/Shadow/Gate ablations,
and strong dependency-graph baselines.
```

---

# 175. WHAT COMES NEXT

This file defines how the architecture should be tested.

The next file must define what can go wrong at the level of the theory itself.

That includes:

```text
failure modes
hidden assumptions
alternative explanations
falsification conditions
scope limits
claims that must not be made
```

---

# 176. NEXT FILE

Next:

```text
18_FAILURES_FALSIFIABILITY.md
```

Its purpose is to make the project scientifically safer by explicitly defining:

```text
what would falsify each major hypothesis
what results would force simplification
where the architecture is not expected to work
which concepts are metaphors vs formal objects
```

---

## FILE VERDICT

```text
STATE: CRYSTAL

DEFINED:
Canonical Experiments and Ablations Plan

PRIMARY COMPARISON:
full verified hierarchy
vs
explicit dependency graph

PRIMARY METRICS:
N50
error escape
false allow
repair span
active memory
critical edge recall

CORE RULE:
every component must survive ablation

NEXT:
18_FAILURES_FALSIFIABILITY.md
```
