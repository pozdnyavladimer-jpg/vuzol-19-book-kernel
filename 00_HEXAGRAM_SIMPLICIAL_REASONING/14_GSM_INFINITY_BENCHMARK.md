# 14 — GSM-INFINITY BENCHMARK

**Project:** Vuzol-19  
**Module:** Hexagram Simplicial Reasoning  
**Status:** BENCHMARK / EXPERIMENT DESIGN SPEC  
**State:** CRYSTAL  
**Language:** English  
**Depends on:** `13_INFINITY_AND_LIMITS_TEST.md`

---

## 0. PURPOSE

The previous file tested the architecture on one exact limit.

This file moves to a scalable external benchmark:

```text
GSM-Infinity / GSM-∞
```

The benchmark was introduced by Zhou et al. as a synthetic long-context mathematical reasoning benchmark with controllable reasoning complexity and context length.

Its core representation is closely related to computational graphs, making it useful for testing the central Vuzol-19 hypothesis:

> **Reasoning reliability may improve when dependency structure, local coupling, residual uncertainty, and verification are represented explicitly rather than left inside one long sequential trace.**

This file does **not** modify the benchmark definition.

It defines an experimental wrapper for comparing the Vuzol-19 architecture against simpler baselines.

---

# 1. EXTERNAL BENCHMARK

Official paper:

```text
GSM-∞: How Do your LLMs Behave over
Infinitely Increasing Reasoning Complexity and Context Length?
```

Authors:

```text
Yang Zhou
Hongyi Liu
Zhuoming Chen
Yuandong Tian
Beidi Chen
```

Published in:

```text
ICML 2025
Proceedings of Machine Learning Research, Volume 267
```

Official software repository:

```text
https://github.com/Infini-AI-Lab/gsm_infinite
```

Official paper page:

```text
https://proceedings.mlr.press/v267/zhou25m.html
```

---

# 2. WHY THIS BENCHMARK IS RELEVANT

Many long-context benchmarks can be dominated by:

```text
retrieval
summarization
finding one relevant passage
```

GSM-∞ was designed to increase:

```text
reasoning complexity
and
context length
```

in a controlled synthetic setting.

The benchmark therefore provides a useful environment for studying:

```text
dependency depth
computational graph size
reasoning degradation
irrelevant-node noise
operation composition
```

These properties directly overlap with the target problem defined in:

```text
01_PROBLEM_LLM_LONG_REASONING.md
```

---

# 3. IMPORTANT EMPIRICAL RESULT FROM GSM-∞

The GSM-∞ paper reports that model reasoning performance declines systematically as reasoning complexity increases.

The reported behavior is approximately sigmoid-like rather than a sudden binary failure.

This makes it natural to measure:

```text
where performance begins to collapse
how sharply it collapses
whether a new architecture shifts that collapse point
```

That motivates the Vuzol-19 metric:

```text
N50
```

defined later in this file.

---

# 4. BENCHMARK SUBSETS

The public repository currently describes three broad subsets:

```text
SYMBOLIC
MEDIUM
HARD
```

The repository describes them approximately as:

```text
SYMBOLIC:
abstract mathematical operations

MEDIUM:
realistic problems with limited implicit entity relationships

HARD:
realistic problems with more complex implicit relationships
```

The Vuzol-19 experiments should begin with:

```text
SYMBOLIC
```

because dependency structure is easier to inspect exactly.

Only then should testing move to:

```text
MEDIUM
HARD
```

---

# 5. WHY START WITH SYMBOLIC

The first experiment should minimize semantic ambiguity.

Symbolic tasks allow us to know:

```text
the true operation graph
the required dependencies
the correct intermediate values
the final answer
```

This lets us measure:

```text
edge retention
local reconstruction
error localization
false Gate decisions
```

without relying on subjective labels.

---

# 6. CORE EXPERIMENTAL QUESTION

The benchmark question for this project is:

> **At equal or clearly reported compute, does hierarchical verified reasoning preserve accuracy for larger dependency graphs than standard prompting or simpler memory methods?**

The desired result is not:

```text
"the architecture looks structured"
```

but:

```text
accuracy collapse occurs later
or
repair becomes cheaper
or
false commits decrease
```

---

# 7. CONTROL VARIABLES

The experiment should separately control:

```text
context length
reasoning complexity
dependency depth
number of operations
number of irrelevant nodes
graph branching
cross-branch coupling
```

Do not collapse all difficulty into one variable if the benchmark generator exposes finer control.

---

# 8. CONTEXT LENGTH VS REASONING COMPLEXITY

These are distinct axes.

A task may have:

```text
long context
low reasoning complexity
```

or:

```text
shorter context
high reasoning complexity
```

The architecture specifically targets:

```text
dependency integrity
```

so reasoning complexity should be analyzed separately from token length.

---

# 9. COMPUTATIONAL GRAPH VIEW

Represent each problem as:

```math
G=(V,E)
```

where:

```text
V:
values / operations / entities / intermediate states

E:
dependencies required to compute downstream states
```

A final answer corresponds to a target node:

```math
v_{\mathrm{target}}
```

The model succeeds only if the required dependency structure is preserved sufficiently well to compute that target.

---

# 10. REQUIRED SUBGRAPH

Not every generated node necessarily contributes equally to the target.

Define:

```math
G^*
=
(V^*,E^*)
```

as the ground-truth subgraph required for the final answer.

This enables exact structural metrics.

---

# 11. DEPENDENCY DEPTH

Define target dependency depth:

```math
D(G^*)
=
\max_{\pi}
|\pi|
```

where `pi` is a required path ending at the target.

This is one useful difficulty measure.

---

# 12. REQUIRED OPERATION COUNT

Define:

```math
N_{\mathrm{op}}
```

as the number of dependent operations required for the answer.

This may be a better scaling variable than raw token count for some experiments.

---

# 13. GRAPH WIDTH

Define:

```math
W
```

as a task-specific width measure.

Possible definitions:

```text
maximum number of simultaneously active branches
maximum nodes at one topological level
frontier size during execution
```

Width may matter because active-memory overload can occur even when depth is moderate.

---

# 14. CROSS-BRANCH COUPLING

For the Vuzol-19 hierarchy, define:

```math
C_{\mathrm{cross}}
```

as the number or weighted mass of required edges crossing local compression groups.

A high value should make hierarchical decomposition harder.

This is an important falsification variable.

---

# 15. NOISE NODES

If a generated problem contains irrelevant or unnecessary nodes, define:

```math
N_{\mathrm{noise}}
```

and:

```math
r_{\mathrm{noise}}
=
\frac{
N_{\mathrm{noise}}
}{
|V|
}
```

This separates:

```text
reasoning failure
```

from:

```text
retrieval / filtering failure
```

---

# 16. PRIMARY SYSTEM LADDER

The canonical comparison ladder is:

```text
A — Plain LLM

B — LLM + sequential explicit reasoning

C — LLM + summary memory

D — LLM + explicit dependency graph

E — D + recursive local grouping

F — E + explicit Coupling / Edge Memory

G — F + Shadow

H — G + -3 Backward audit

I — H + Gate

J — I + Bindu / verified reusable commits
```

Each stage should be tested separately.

---

# 17. WHY THE LADDER MATTERS

If the complete system wins, we still need to know:

```text
which component caused the gain
```

The ladder supports attribution.

For example:

```text
D beats C:
dependency graph matters

F beats E:
explicit edge state matters

G beats F:
Shadow matters

H beats G:
backward audit matters

I beats H:
Gate matters
```

---

# 18. STRONG BASELINE: DEPENDENCY GRAPH

A plain explicit dependency graph is a strong baseline.

This is important.

If:

```text
dependency graph only
```

matches the full architecture, then:

```text
triangular recursion
Shadow
Gate
Bindu
```

may be unnecessary for this benchmark.

The project must accept that result.

---

# 19. STRONG BASELINE: MORE INFERENCE COMPUTE

The benchmark paper studies inference scaling.

Therefore the Vuzol-19 method should be compared against:

```text
same base model
+
more inference attempts / tokens / sampling
```

Otherwise an apparent architecture gain may simply come from more compute.

---

# 20. EQUAL-COMPUTE PRINCIPLE

For every main comparison, report:

```text
input tokens
generated tokens
model calls
tool calls
wall-clock time
estimated inference cost
memory used
```

A result should not be described as an efficiency gain if the architecture used much more compute without disclosure.

---

# 21. TWO FAIR COMPARISON MODES

Use both.

## Mode A — Equal Compute

Give all systems approximately the same budget.

Question:

```text
Who achieves higher accuracy?
```

## Mode B — Equal Accuracy

Find the cost required to reach the same accuracy.

Question:

```text
Who achieves the target accuracy more cheaply?
```

Both are informative.

---

# 22. PRIMARY ACCURACY METRIC

Use exact answer accuracy:

```math
A(N)
=
\frac{
\text{correct final answers at difficulty }N
}{
\text{all tasks at difficulty }N
}
```

Where `N` may be:

```text
required operations
dependency depth
graph size
```

---

# 23. N50

Define:

```math
N_{50}
=
\inf
\left\{
N:
A(N)<0.5
\right\}
```

Operationally:

```text
the difficulty scale where accuracy falls below 50%
```

The main Vuzol-19 hypothesis is:

```math
N_{50}^{\mathrm{Vuzol}}
>
N_{50}^{\mathrm{baseline}}
```

under comparable compute.

---

# 24. N80

Also define:

```math
N_{80}
```

where accuracy falls below 80%.

This is useful because high-quality systems may become practically unreliable long before reaching 50%.

---

# 25. FAILURE-CURVE FIT

The GSM-∞ paper reports approximately sigmoid-shaped degradation.

A simple fitted curve may be:

```math
A(N)
=
\frac{1}{
1+\exp(k(N-N_c))
}
```

where:

- `N_c` — approximate collapse center;
- `k` — decline steepness.

This is only a model fit.

Do not assume every system follows exactly the same curve.

---

# 26. SHIFT METRIC

If curves are fitted, define:

```math
\Delta N_c
=
N_c^{\mathrm{method}}
-
N_c^{\mathrm{baseline}}
```

Positive shift:

```text
performance collapse occurs later
```

This is more informative than one isolated accuracy number.

---

# 27. AREA UNDER REASONING CURVE

Define over a tested range:

```math
AURC
=
\int_{N_{\min}}^{N_{\max}}
A(N)\,dN
```

or discrete approximation.

This summarizes performance across many difficulty levels.

---

# 28. PROCESS VALIDITY

Exact final answers are not enough for testing Gate.

Define:

```math
A_{\mathrm{process}}
=
\frac{
\text{solutions with valid required dependency route}
}{
\text{all evaluated solutions}
}
```

This requires instrumented synthetic tasks where the correct dependency structure is known.

---

# 29. FALSE-GREEN RATE

Define:

```math
R_{\mathrm{FG}}
=
\frac{
\text{correct endpoints produced by invalid required process}
}{
\text{correct endpoints}
}
```

This directly tests:

```text
correct answer
but broken reasoning route
```

---

# 30. EDGE RETENTION

Given required edge set:

```math
E^*
```

and retained or reconstructed edge set:

```math
\hat{E}
```

define:

```math
R_{\mathrm{edge}}
=
\frac{
|E^*\cap\hat{E}|
}{
|E^*|
}
```

Also measure precision and F1 when the model may invent extra edges.

---

# 31. CRITICAL EDGE RETENTION

Not all edges are equally important.

Define:

```math
E^*_{\mathrm{critical}}
```

as edges whose removal changes the correct solution path.

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

This may correlate more strongly with answer accuracy.

---

# 32. PATH RETENTION

For each required dependency path `pi`, ask whether its ordered structure survives.

Define:

```math
R_{\mathrm{path}}
=
\frac{
\text{required paths preserved}
}{
\text{required paths}
}
```

This tests temporal / computational ordering.

---

# 33. RECONSTRUCTION ERROR

For hierarchical systems, measure:

```math
E_{\mathrm{rec}}
=
d(X,\hat{X})
```

at each compressed node.

Aggregate by depth:

```math
E_{\mathrm{rec}}^{(d)}
```

This can reveal whether error accumulates toward the root.

---

# 34. RECONSTRUCTION DRIFT

Define:

```math
D_{\mathrm{rec}}
=
E_{\mathrm{rec}}^{(\mathrm{root})}
-
E_{\mathrm{rec}}^{(\mathrm{leaf-level})}
```

Positive drift indicates reconstruction degradation through repeated compression.

---

# 35. SHADOW COST

Measure:

```math
M_S
```

and:

```math
\rho_S
=
\frac{
\mathrm{Shadow\ size}
}{
\mathrm{original\ represented\ state\ size}
}
```

A system should not claim compactness while moving the full trace into Shadow.

---

# 36. TOTAL MEMORY COST

Report:

```text
active state
+
Shadow
+
provenance
+
edge memory
+
Gate history
+
commit memory
```

This is the true memory cost.

---

# 37. ACTIVE MEMORY

Separately measure:

```math
M_{\mathrm{active}}
```

because externalized Shadow may reduce active-context burden even if total stored memory remains substantial.

This distinction is important.

---

# 38. REOPEN RATE

From earlier files:

```math
R_{\mathrm{open}}
=
\frac{
\text{subtree expansions}
}{
\text{subtree uses}
}
```

High reopen rate suggests compression is too aggressive or grouping is poor.

---

# 39. REPAIR SPAN

For an injected error:

```math
S_{\mathrm{repair}}
=
\text{number of nodes recomputed}
```

Compare against:

```text
full task restart
```

This measures local repair efficiency.

---

# 40. ERROR DETECTION DISTANCE

Define:

```math
D_{\mathrm{detect}}
=
\text{graph levels between injected error and detection}
```

The Gate hypothesis predicts smaller values.

---

# 41. ERROR ESCAPE RATE

Define:

```math
R_{\mathrm{escape}}
=
\frac{
\text{injected errors reaching root undetected}
}{
\text{injected errors}
}
```

This is one of the strongest verification metrics.

---

# 42. FALSE ALLOW RATE

For Gate:

```math
R_{\mathrm{FA}}
=
\frac{
\text{invalid local states receiving ALLOW}
}{
\text{invalid local states}
}
```

This should fall as Gate quality improves.

---

# 43. FALSE HOLD RATE

Define:

```math
R_{\mathrm{FH}}
=
\frac{
\text{valid local states blocked}
}{
\text{valid local states}
}
```

A Gate that never allows anything is not useful.

---

# 44. UNKNOWN RATE

Measure:

```math
R_{\mathrm{unknown}}
```

especially under strict resource limits.

A system that responsibly returns UNKNOWN may have lower raw completion rate but better calibrated reliability.

Report both.

---

# 45. CALIBRATION

If the system outputs confidence:

```math
p_{\mathrm{correct}}
```

measure calibration.

Possible metrics:

```text
Brier score
Expected Calibration Error
reliability curves
```

This is especially useful for Gate threshold selection.

---

# 46. EXPERIMENT 1 — COMPLEXITY SWEEP

Hold context style approximately fixed.

Increase:

```text
required operation count
or
dependency depth
```

Measure:

```text
A(N)
N80
N50
AURC
```

for every system in the ladder.

---

# 47. EXPERIMENT 2 — CONTEXT SWEEP

Hold reasoning complexity fixed.

Increase context length.

This tests whether the architecture improves:

```text
reasoning structure
```

or merely:

```text
long-context retrieval
```

---

# 48. EXPERIMENT 3 — NOISE SWEEP

Increase:

```math
r_{\mathrm{noise}}
```

while keeping required graph fixed.

Measure:

```text
answer accuracy
edge precision
active memory
```

This tests filtering robustness.

---

# 49. EXPERIMENT 4 — DEPTH VS WIDTH

Create tasks with similar total operation count but different structure.

Example:

```text
deep/narrow graph
vs
shallow/wide graph
```

This reveals which structural feature causes failure.

---

# 50. EXPERIMENT 5 — CROSS-EDGE DENSITY

For recursive grouping, gradually increase:

```math
C_{\mathrm{cross}}
```

Expected hypothesis:

```text
benefit of tree-like compression decreases
as cross-group critical coupling increases
```

This is an important falsification test.

---

# 51. EXPERIMENT 6 — RANDOM GROUPING

Compare:

```text
dependency-aware grouping
```

against:

```text
random ternary grouping
```

If performance is similar, grouping semantics may not matter.

That would weaken the architecture.

---

# 52. EXPERIMENT 7 — BINARY VS TERNARY VS VARIABLE

Compare:

```text
2 -> 1
3 -> 1
4 -> 1
variable branching
```

under matched compute.

The project should not assume ternary grouping is best.

---

# 53. EXPERIMENT 8 — EDGE ABLATION

Remove explicit edge memory while keeping node summaries.

Expected:

```text
edge-sensitive task accuracy decreases
```

If not, edge storage may be unnecessary.

---

# 54. EXPERIMENT 9 — SHADOW ABLATION

Compare:

```text
with Shadow
without Shadow
```

under equal parent-state size.

Measure:

```text
reconstruction
root accuracy
repair success
memory
```

---

# 55. EXPERIMENT 10 — BACKWARD AUDIT ABLATION

Compare:

```text
+3 Forward only
```

against:

```text
+3 Forward + -3 Backward
```

Measure:

```text
error detection
false allow
repair span
compute overhead
```

---

# 56. EXPERIMENT 11 — GATE ABLATION

Compare:

```text
root-only verification
```

against:

```text
local Gate at every level
```

Expected:

```text
lower detection distance
lower escape rate
```

with local Gate.

---

# 57. EXPERIMENT 12 — BINDU / REUSE

Create repeated tasks sharing verified subgraphs.

Compare:

```text
recompute every time
```

against:

```text
reuse committed verified subproblem
```

Measure:

```text
compute savings
accuracy
stale-state errors
reentry Gate performance
```

---

# 58. INJECTED VALUE ERROR

Select a true internal node:

```math
v_k
```

and change its value.

Example:

```text
17 -> 19
```

Then measure whether:

```text
-3 or Gate catches it
```

before root commit.

---

# 59. INJECTED EDGE ERROR

Change one dependency:

```text
A -> B
```

to:

```text
A -> C
```

while leaving node values unchanged where possible.

This isolates structural reasoning from arithmetic reasoning.

---

# 60. INJECTED OPERATOR ERROR

Replace:

```text
+
```

with:

```text
-
```

or another valid operation.

Measure local detection.

---

# 61. INJECTED ORDER ERROR

Swap two operations that are not commutative.

This tests temporal / dependency edge retention.

---

# 62. INJECTED CONSTRAINT ERROR

Add or remove a rule that changes the valid path.

This is useful for testing Gate beyond arithmetic answer checking.

---

# 63. INJECTED SHADOW ERROR

During compression, remove a residual fact required later.

Measure whether:

```text
reconstruction
or downstream Gate
```

detects that the parent is insufficient.

---

# 64. ERROR-INJECTION LOCATION

Vary injection depth:

```text
near leaves
middle level
near root
```

Measure:

```text
detection distance
repair span
root corruption
```

---

# 65. ERROR-INJECTION MAGNITUDE

For numeric errors, vary:

```math
|\delta|
```

This tests whether the audit only catches large failures.

A useful verifier should catch small but structurally critical errors when they matter downstream.

---

# 66. CRITICAL VS NONCRITICAL ERROR

Inject:

```text
critical error:
changes final answer
```

and:

```text
noncritical error:
does not affect target
```

A good system should prioritize the first.

Overreacting to irrelevant changes increases false HOLD.

---

# 67. GROUPING QUALITY METRIC

For each local group `T`, measure:

```math
Q_T
=
\frac{
W_{\mathrm{internal}}
}{
W_{\mathrm{internal}}+W_{\mathrm{boundary}}
}
```

where weighted edges reflect dependency importance.

High `Q_T` means more required coupling remains local.

---

# 68. TREE DECOMPOSABILITY SCORE

Define global average:

```math
Q_{\mathrm{tree}}
=
\frac{1}{m}
\sum_{j=1}^{m}
Q_{T_j}
```

This may predict whether recursive compression is a good fit for a problem.

---

# 69. STRUCTURAL FAILURE PREDICTION

Test whether:

```math
Q_{\mathrm{tree}}
```

or cross-edge density predicts the performance gap:

```math
A_{\mathrm{Vuzol}}
-
A_{\mathrm{graph}}
```

If yes, the architecture gains a useful boundary condition:

```text
when hierarchy helps
and
when it does not
```

---

# 70. COMPUTE-NORMALIZED ACCURACY

Define one optional efficiency measure:

```math
E_A
=
\frac{
\text{correct tasks}
}{
\text{inference cost}
}
```

The cost denominator must be clearly defined.

Possible units:

```text
generated tokens
GPU-seconds
API cost
model calls
```

Do not mix them without explanation.

---

# 71. REPAIR-NORMALIZED ACCURACY

For corrupted-task experiments:

```math
E_R
=
\frac{
\text{successfully repaired tasks}
}{
\text{repair compute}
}
```

This directly evaluates local repair value.

---

# 72. STATISTICAL REPORTING

For every major condition report:

```text
sample count
mean accuracy
confidence interval
random seed
model version
prompt version
architecture version
```

Synthetic generation makes large sample sizes feasible.

---

# 73. MULTIPLE RANDOM SEEDS

Do not rely on one generated dataset.

Use multiple seeds for:

```text
problem generation
grouping
model sampling
```

when applicable.

This reduces accidental benchmark fitting.

---

# 74. HELD-OUT DIFFICULTY

Tune thresholds on one complexity range.

Evaluate on larger unseen complexity.

Example:

```text
tune:
N = 5..20

test:
N = 25..100
```

This checks whether the architecture truly scales rather than overfitting a fixed difficulty.

---

# 75. HELD-OUT GRAPH SHAPES

Train or tune on:

```text
mostly chains
```

then test on:

```text
branching DAGs
```

and vice versa.

This probes structural generalization.

---

# 76. HELD-OUT OPERATORS

Where generator design permits, hold out combinations of operations.

The architecture should preserve structural reasoning rather than memorize templates.

---

# 77. MODEL GENERALITY

Test multiple base models.

The research claim should ideally be:

```text
architecture improves reasoning control
across more than one LLM
```

not:

```text
one prompt happens to work on one model
```

---

# 78. SMALL-MODEL TEST

A particularly informative test is whether structure helps a smaller model extend its reliable reasoning range.

If a small model with explicit architecture approaches a larger baseline, that would indicate real control value.

This is a hypothesis, not an expected result.

---

# 79. LARGE-MODEL TEST

Also test a strong model.

If gains disappear entirely at higher capability, the architecture may be mainly a compensation mechanism for weaker models.

That is still scientifically useful.

---

# 80. TOOL-FREE FIRST

The initial benchmark should be:

```text
tool-free
```

where possible.

Do not mix external calculators or code execution into the first comparison unless all systems receive the same tools.

This isolates reasoning architecture.

---

# 81. TOOL-AUGMENTED SECOND

Later add:

```text
calculator
Python
symbolic algebra
graph executor
```

Then ask whether Gate/Shadow still add value when arithmetic errors are mostly removed.

This can isolate structural errors from computation errors.

---

# 82. GRAPH EXECUTOR BASELINE

A very strong baseline is:

```text
LLM extracts graph
deterministic program executes graph
```

If this solves the benchmark cheaply and reliably, the Vuzol-19 architecture must demonstrate additional value in:

```text
graph extraction
uncertainty handling
repair
partial observability
semantic tasks
```

This baseline should not be avoided.

---

# 83. REASONING TRACE STORAGE BASELINE

Another baseline:

```text
store full reasoning trace
```

This may achieve strong reconstruction at high memory cost.

Compare:

```text
full trace
vs
parent + Shadow
```

on:

```text
memory
accuracy
reconstruction
retrieval cost
```

---

# 84. SUMMARY-MEMORY BASELINE

Use ordinary textual summaries between reasoning blocks.

This is important because the proposed hierarchy may simply be a structured summary system.

Measure whether:

```text
explicit edges + Shadow + Gate
```

add measurable value beyond good summaries.

---

# 85. PREREGISTRATION

Before large evaluation, freeze:

```text
primary metrics
main baselines
difficulty ranges
Gate thresholds
grouping policy
stopping criteria
success condition
```

This reduces post-hoc interpretation.

---

# 86. PRIMARY HYPOTHESIS

Preregister:

```math
H_1:
N_{50}^{\mathrm{full}}
>
N_{50}^{\mathrm{dependency\ graph}}
```

under a defined compute budget.

This is deliberately difficult.

A weaker but still meaningful hypothesis is:

```math
H_2:
R_{\mathrm{escape}}^{\mathrm{full}}
<
R_{\mathrm{escape}}^{\mathrm{graph}}
```

under injected-error conditions.

---

# 87. SECONDARY HYPOTHESIS

```math
H_3:
S_{\mathrm{repair}}^{\mathrm{full}}
<
S_{\mathrm{repair}}^{\mathrm{restart}}
```

while preserving final accuracy.

This tests local repair independently of raw reasoning accuracy.

---

# 88. SHADOW HYPOTHESIS

```math
H_4:
E_{\mathrm{rec}}^{\mathrm{with\ Shadow}}
<
E_{\mathrm{rec}}^{\mathrm{without\ Shadow}}
```

under matched parent size.

---

# 89. EDGE HYPOTHESIS

```math
H_5:
A_{\mathrm{edge-sensitive}}^{\mathrm{with\ coupling}}
>
A_{\mathrm{edge-sensitive}}^{\mathrm{node-only}}
```

---

# 90. NULL RESULTS

The project should explicitly accept outcomes such as:

```text
dependency graph is sufficient
ternary hierarchy adds no value
Shadow cost is too high
Gate is too expensive
reconstruction is unnecessary
```

These are useful findings.

The benchmark exists to discriminate between architectures, not to confirm the preferred one.

---

# 91. MINIMUM VIABLE EXPERIMENT

Do not begin with the full system.

First implement:

```text
SYSTEM A:
plain baseline

SYSTEM D:
explicit dependency graph

SYSTEM E:
dependency graph + recursive triads

SYSTEM H:
triads + coupling + Shadow + -3

SYSTEM I:
full Gate
```

Difficulty sweep:

```text
small
medium
large
```

Measure:

```text
exact accuracy
edge retention
compute
memory
```

This is sufficient for the first signal.

---

# 92. PHASE 1 — SANITY CHECK

Use easy tasks where all systems should score near 100%.

Purpose:

```text
verify parser
verify evaluation
verify instrumentation
verify graph extraction
```

If systems fail here, scaling experiments are meaningless.

---

# 93. PHASE 2 — COLLAPSE REGION

Identify the baseline model's performance transition.

Example:

```text
accuracy near 90%
-> declining region
-> below 50%
```

Concentrate samples around this region.

This gives more statistical power for detecting `N50` shifts.

---

# 94. PHASE 3 — BEYOND COLLAPSE

Test substantially harder problems.

The goal is not necessarily high accuracy.

The goal is to see whether:

```text
errors become more detectable
UNKNOWN becomes calibrated
local repair remains possible
```

---

# 95. PHASE 4 — ADVERSARIAL STRUCTURE

Create:

```text
high cross-edge density
ambiguous grouping
shared dependencies
operator inversions
deep branch reuse
```

This tries to break the architecture.

---

# 96. PHASE 5 — REUSE

Reuse verified subgraphs across generated tasks where structurally valid.

Measure whether Bindu/MemoryAtom adds:

```text
speed
consistency
or
new stale-memory failure modes
```

---

# 97. RESULT TABLE

Recommended main table:

```text
System
Accuracy
Process Validity
N80
N50
Edge Recall
False Allow
Error Escape
Active Memory
Total Memory
Compute
Repair Span
```

Do not report only final accuracy.

---

# 98. CURVES TO PLOT

Recommended plots:

```text
accuracy vs reasoning complexity

accuracy vs context length

edge recall vs complexity

false allow vs complexity

active memory vs complexity

total memory vs complexity

repair span vs injected-error depth

accuracy vs compute
```

These curves expose tradeoffs better than one score.

---

# 99. EXPECTED FAILURE SIGNATURES

Possible baseline failure:

```text
node values retained
dependency relation lost
```

Possible recursive-compression failure:

```text
bad grouping
cross-edge loss
```

Possible Shadow failure:

```text
residual store becomes full-history copy
```

Possible Gate failure:

```text
false HOLD explosion
```

Possible Bindu failure:

```text
stale verified state reused outside valid scope
```

Instrumentation should classify these separately.

---

# 100. IMPLEMENTATION LOG FORMAT

For each problem:

```text
problem_id
generator_seed
difficulty
context_length
required_operation_count
dependency_depth
graph_width
cross_edge_count

baseline_answer
baseline_correct

Vuzol root answer
Vuzol correct

Gate events
Shadow size
reopen count
repair span
edge retention
compute cost
```

This creates a machine-readable experiment record.

---

# 101. MINIMAL JSONL RECORD

```json
{
  "problem_id": "gsm_inf_000001",
  "difficulty": 24,
  "dependency_depth": 17,
  "required_operations": 24,
  "system": "vuzol_full",
  "correct": true,
  "edge_recall": 0.96,
  "false_allow": false,
  "error_escape": false,
  "active_memory": 18,
  "shadow_size": 420,
  "repair_span": 3,
  "model_calls": 7
}
```

The final schema may differ.

---

# 102. REPRODUCIBILITY

Store:

```text
benchmark commit hash
Vuzol code commit hash
model identifier
API/model date if applicable
prompt hash
random seed
configuration file
```

This is essential because both benchmark software and models may change.

---

# 103. EXTERNAL BENCHMARK INTEGRITY

Do not modify benchmark answers or generator rules to favor the architecture.

Vuzol-specific metadata should be stored separately.

The benchmark remains the external evaluator.

---

# 104. BENCHMARK ADAPTER

Recommended architecture:

```text
GSM-∞ generator
      |
      v
problem instance
      |
      +--> baseline runner
      |
      +--> Vuzol adapter
                |
                v
         dependency state
                |
                v
         recursive reasoning
                |
                v
           evaluator
```

---

# 105. VUZOL ADAPTER ROLE

The adapter may:

```text
parse problem
construct or infer dependency graph
create local state nodes
schedule groups
store coupling
run +3 / -3
run Gate
commit verified parents
```

The adapter must not receive hidden ground-truth graph information unless the experiment explicitly studies an oracle-graph condition.

---

# 106. ORACLE GRAPH CONDITION

Use an oracle graph in one diagnostic experiment:

```text
give system the true dependency graph
```

This isolates:

```text
graph reasoning ability
```

from:

```text
graph extraction ability
```

If Vuzol works only with oracle graphs, graph extraction is the bottleneck.

---

# 107. INFERRED GRAPH CONDITION

The realistic condition is:

```text
model must infer graph from problem text
```

Compare against oracle results.

The difference quantifies:

```text
graph extraction loss
```

---

# 108. GRAPH EXTRACTION ACCURACY

Measure:

```text
node precision / recall
edge precision / recall
operator type accuracy
dependency ordering accuracy
```

Do not blame the reasoning tree for failures caused during graph construction.

---

# 109. ORACLE/INFERRED GAP

Define:

```math
G_{\mathrm{oracle}}
=
A_{\mathrm{oracle\ graph}}
-
A_{\mathrm{inferred\ graph}}
```

Large gap:

```text
state extraction is the main bottleneck
```

Small gap with low accuracy:

```text
reasoning / compression is the main bottleneck
```

---

# 110. EXPERIMENTAL DECISION TREE

Interpret outcomes:

```text
If graph baseline ~= full Vuzol:
    simplify architecture.

If full Vuzol > graph baseline:
    run ablations.

If gain disappears without Shadow:
    Shadow is important.

If gain disappears without -3:
    reconstruction audit is important.

If gain disappears without Gate:
    local verification is important.

If gain appears only with oracle graph:
    improve graph extraction.

If gain disappears at high cross-edge density:
    document decomposability boundary.
```

---

# 111. SCIENTIFIC STATUS

```text
FACT:
GSM-∞ is a synthetic benchmark
for scalable context length and reasoning complexity.

FACT:
Its design is based on computational-graph-style
grade-school mathematical reasoning.

FACT:
The published study reports systematic performance decline
as reasoning complexity increases.

MODEL:
Use GSM-∞ as an external testbed for
Coupling, Shadow, +3/-3, Gate, and Bindu.

HYPOTHESIS:
The full architecture shifts reasoning collapse
to higher complexity or improves local error containment.

TEST:
Equal-compute difficulty sweeps,
ablation ladder,
graph oracle/inferred conditions,
cross-edge sweeps,
and injected-error experiments.
```

---

# 112. REFERENCES

1. Zhou, Y., Liu, H., Chen, Z., Tian, Y., & Chen, B.  
   **GSM-∞: How Do your LLMs Behave over Infinitely Increasing Reasoning Complexity and Context Length?**  
   ICML 2025, Proceedings of Machine Learning Research 267.  
   `https://proceedings.mlr.press/v267/zhou25m.html`

2. Infini-AI-Lab.  
   **GSM-Infinite official repository.**  
   `https://github.com/Infini-AI-Lab/gsm_infinite`

---

# 113. WHAT COMES NEXT

This file defines the principal external benchmark.

The next file returns to one architecture-specific hypothesis that must remain separate from the benchmark itself:

```text
14 -> 10 -> 10 -> 8
```

It must be treated as a candidate information funnel, not as an established law.

---

# 114. NEXT FILE

Next:

```text
15_14_10_10_8_FUNNEL.md
```

Its purpose is to define:

```text
what the four stages could mean computationally
what information is reduced at each stage
what must survive
which alternative layer widths must be tested
how to falsify the proposed sequence
```

The critical rule will be:

> **14 -> 10 -> 10 -> 8 is an architectural hypothesis and must compete against alternative funnels.**

---

## FILE VERDICT

```text
STATE: CRYSTAL

DEFINED:
GSM-Infinity benchmark plan

PRIMARY TARGET:
shift the long-reasoning failure curve
or improve error containment
under comparable compute

PRIMARY METRIC:
N50

STRONG BASELINE:
explicit dependency graph

REQUIRED TESTS:
equal compute
ablations
cross-edge density
oracle vs inferred graph
error injection
memory and repair cost

NEXT:
15_14_10_10_8_FUNNEL.md
```
