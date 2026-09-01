# 18 — FAILURES AND FALSIFIABILITY

**Project:** Vuzol-19  
**Module:** Hexagram Simplicial Reasoning  
**Status:** CRITICAL REVIEW / FALSIFICATION SPEC  
**State:** CRYSTAL  
**Language:** English  
**Depends on:** `17_EXPERIMENTS_AND_ABLATIONS.md`

---

## 0. PURPOSE

The previous file defined how to test the architecture.

This file defines:

```text
what would count as failure
what would falsify each major hypothesis
which assumptions are hidden inside the design
which concepts are metaphors
which concepts are formal
which results would force simplification
where the architecture is not expected to work
```

The central rule is:

> **A theory that cannot describe what would prove it wrong is not yet a useful research theory.**

This file therefore treats failure as a first-class output.

---

# 1. PROJECT CLAIM LEVELS

The architecture contains several different claim types.

They must not be mixed.

```text
FACT
MODEL
HYPOTHESIS
TEST
METAPHOR
ENGINEERING CHOICE
```

Every future document should distinguish them when ambiguity exists.

---

# 2. FACT

A statement belongs under:

```text
FACT
```

only when it is supported by established mathematics, computer science, benchmark results, or directly measured experiment.

Examples:

```text
a 2-simplex has three barycentric coordinates constrained by one sum rule

lossy compression is not generally invertible

a dependency graph can contain information not recoverable from node values alone

balanced ternary hierarchy depth is logarithmic in the number of leaves

total work does not automatically become logarithmic
```

---

# 3. MODEL

A statement belongs under:

```text
MODEL
```

when it defines a representation or computational mechanism.

Examples:

```text
GSL 6D
FORM / FLOW grouping
recursive triads
Shadow
Gate
Bindu
MemoryAtom
```

A model may be useful even if it is not uniquely correct.

---

# 4. HYPOTHESIS

A statement belongs under:

```text
HYPOTHESIS
```

when it predicts measurable benefit.

Examples:

```text
explicit coupling improves edge-sensitive reasoning

Shadow improves reconstruction under fixed parent size

local Gate reduces undetected error propagation

recursive hierarchy increases N50 under bounded active memory

14/10/10/8 lies near a useful compression frontier
```

These claims require experiments.

---

# 5. METAPHOR

Some Vuzol-19 language is metaphorical or organizational.

Examples:

```text
Bindu
Shadow
Hexagram
Flower
Sri
resonance
crystal
```

These terms may help architecture design.

But they must map to explicit computational objects if used in a technical claim.

Example:

```text
"resonance"
```

must map to something measurable such as:

```math
E_{\mathrm{cycle}}
```

or:

```math
R_{\mathrm{local}}
=
e^{-\lambda E}
```

Otherwise it remains metaphor.

---

# 6. ENGINEERING CHOICE

Examples:

```text
ternary grouping
six GSL axes
specific Gate thresholds
JSONL event logs
SQLite memory
14/10/10/8 widths
```

These are implementation choices.

They should not be elevated into universal theory without evidence.

---

# 7. GLOBAL FALSIFIABILITY PRINCIPLE

The architecture should be simplified if a simpler baseline achieves the same or better:

```text
accuracy
error containment
repairability
memory efficiency
compute efficiency
```

with lower complexity.

The default scientific direction is:

```text
remove unnecessary machinery
```

not:

```text
preserve every original concept
```

---

# 8. CORE NULL HYPOTHESIS

A strong null hypothesis is:

```math
H_0:
\mathrm{Utility}_{\mathrm{Vuzol}}
\le
\mathrm{Utility}_{\mathrm{dependency\ graph}}
```

under matched resource conditions.

The project must attempt to reject this null.

If it cannot, the explicit graph baseline remains preferable.

---

# 9. FAILURE OF THE CORE ARCHITECTURE

The core architecture is weakened if:

```text
dependency graph alone matches full system
```

on:

```text
N50
error escape
repair span
active memory
false allow
```

while using less compute or memory.

In that case, the correct action is:

```text
simplify to graph + verifier
```

---

# 10. FAILURE OF GSL 6D

The GSL 6D hypothesis fails as a control representation if:

1. paraphrases map inconsistently;
2. negation is unstable;
3. axes collapse into sentiment-like correlation;
4. axis labels cannot be annotated reliably;
5. GSL adds no predictive value beyond embeddings;
6. scheduler/Gate performance is unchanged when GSL is removed;
7. random six-dimensional projections perform similarly;
8. learned systems consistently prefer different state factors.

Then GSL should become:

```text
diagnostic visualization
```

or be removed.

---

# 11. FAILURE OF HEXAGRAM FORM/FLOW

The Hexagram grouping is weakened if:

```text
FORM = (Y,B,V)
FLOW = (R,O,G)
```

does not outperform:

```text
flat 6D
random 3+3 partitions
learned partitions
```

on meaningful metrics.

If the geometry adds no control value:

```text
retain only as visualization
```

not as computational necessity.

---

# 12. FAILURE OF TRIANGULAR GROUPING

Ternary grouping is falsified as a privileged branching rule if:

```text
binary
quaternary
variable-width
graph-native
```

grouping performs equally or better under matched compute.

Then:

```text
3-way grouping
```

should be treated as one optional decomposition scheme.

---

# 13. FAILURE OF RECURSIVE HIERARCHY

The hierarchy is not useful if:

```text
active memory does not decrease
repair span does not decrease
N50 does not improve
cross-edge management dominates cost
root verification requires full expansion every time
```

Then a flat dependency DAG may be superior.

---

# 14. FAILURE OF EDGE MEMORY

Explicit Coupling / Edge Memory is weakened if:

1. node-only models match edge-aware models on edge-sensitive tasks;
2. edge extraction error dominates all gains;
3. edge storage grows too rapidly;
4. pruning critical edges cannot be done reliably;
5. edge type distinctions provide no measurable benefit;
6. graph representations already supplied by the task make extra coupling state redundant.

Then keep only the minimum dependency representation required.

---

# 15. FAILURE OF SHADOW

Shadow fails as a compression mechanism if:

```math
\rho_{\mathrm{total}}
\ge1
```

for most useful tasks, where:

```text
parent + Shadow + metadata
```

uses as much or more memory than the original trace.

Shadow also fails if:

```text
retrieval rarely helps
critical residuals are often missed
Shadow becomes an unstructured dump
Shadow-of-Shadow grows without bound
```

In that case, ordinary checkpoints may be better.

---

# 16. FAILURE OF -3 BACKWARD

Backward audit fails if:

1. reconstruction is mostly hallucinated;
2. provenance does not constrain reconstruction;
3. exact and ambiguous inverse cases are not distinguished;
4. injected errors are not detected better than by a simple verifier;
5. reconstruction cost exceeds full recomputation;
6. component-wise residuals do not improve localization;
7. a standard consistency checker performs equally well.

Then `-3` should be reduced to explicit verification rather than generative reconstruction.

---

# 17. FAILURE OF GATE

Gate fails if:

```text
false ALLOW remains high
false HOLD becomes impractical
latency dominates reasoning cost
thresholds do not transfer
reason codes do not match actual failure
repair routing does not help
```

A Gate that blocks everything is not robust.

A Gate that allows everything is not useful.

---

# 18. FAILURE OF BINDU

Bindu fails as a distinct commit layer if:

```text
ordinary checkpointing provides the same reliability
```

or if:

```text
rollback rarely helps
reentry frequently reuses stale states
commit metadata dominates memory
immutability gives no practical audit benefit
```

Then persistence should be simplified.

---

# 19. FAILURE OF MEMORYATOM

MemoryAtom is weakened if:

```text
stored verified states are rarely reusable
validity scope is hard to determine
retrieval creates more stale errors than savings
provenance does not change decisions
```

Then persistent verified reasoning memory may not be worth its complexity for that task class.

---

# 20. FAILURE OF 14/10/10/8

The fixed funnel should be rejected as privileged if:

```text
alternative widths outperform it consistently
```

or:

```text
learned effective dimensions do not approach 10/10/8
```

or:

```text
the second 10-stage adds no measurable value
```

or:

```text
adaptive widths dominate fixed widths
```

The rest of the architecture must remain independent of this result.

---

# 21. FAILURE OF THE SRI MAPPING

The historical / geometric origin of:

```text
14 / 10 / 10 / 8
```

does not establish computational necessity.

If experiments do not support it:

```text
do not reinterpret failure as hidden confirmation
```

The mapping must be downgraded to:

```text
inspiration only
```

---

# 22. FAILURE OF "TRIANGLES INSIDE TRIANGLES"

The recursive triangle metaphor becomes misleading if actual task decompositions are usually:

```text
4-way
5-way
dense DAGs
hypergraphs
continuous manifolds
```

and forcing triads creates artificial structure.

Then the correct generalization is:

```text
recursive local simplicial / graph units
```

not strict triangles everywhere.

---

# 23. FAILURE OF THE SIMPLEX REPRESENTATION

The simplex representation fails if:

```text
relative composition is not meaningful
signed states dominate
absolute scale matters more than ratios
normalization destroys useful information
```

Then use:

```text
raw vectors
affine coordinates
signed channels
task-specific geometry
```

instead.

---

# 24. FAILURE OF BARYCENTRIC INTERPRETABILITY

If barycentric coordinates cannot be mapped consistently to stable semantic roles, they should be treated as:

```text
numerical local coordinates
```

not explanatory semantics.

Interpretability must be demonstrated.

---

# 25. FAILURE OF LOCAL CLOSURE

The architecture assumes some reasoning subproblems can become locally closed.

This fails when:

```text
every local region depends strongly on distant states
```

or:

```text
constraints remain global at every level
```

or:

```text
cross-boundary edge cost stays high under every partition
```

Such tasks may not benefit from hierarchical local compression.

---

# 26. TREEWIDTH AS A BOUNDARY CONDITION

A useful falsification hypothesis:

> The architecture should work better on dependency graphs with low or moderate effective treewidth than on densely entangled graphs.

If performance does not depend at all on decomposability, then treewidth/cut-based motivation may be wrong.

If performance collapses as predicted with dense coupling, that is not a failure of falsifiability; it identifies scope.

---

# 27. FAILURE OF ACTIVE-MEMORY ADVANTAGE

One central claim is reduced active dependency burden.

This fails if:

```math
M_{\mathrm{active}}^{\mathrm{Vuzol}}
\ge
M_{\mathrm{active}}^{\mathrm{baseline}}
```

at equal accuracy across most task scales.

Then the hierarchy is not solving the intended memory-control problem.

---

# 28. FAILURE OF N50 ADVANTAGE

The long-reasoning claim weakens if:

```math
N_{50}^{\mathrm{Vuzol}}
\le
N_{50}^{\mathrm{baseline}}
```

across seeds and models under matched compute.

Then any remaining benefit must be described separately:

```text
repair
audit
memory
```

not as reasoning-depth extension.

---

# 29. FAILURE OF REPAIR ADVANTAGE

Local repair is not useful if:

```math
S_{\mathrm{repair}}^{\mathrm{Vuzol}}
\approx
S_{\mathrm{restart}}
```

or:

```text
repair success is low
```

or:

```text
repaired ancestors are frequently inconsistent
```

Then incremental recovery is not providing value.

---

# 30. FAILURE OF ERROR CONTAINMENT

If injected local errors frequently reach the root before detection:

```math
R_{\mathrm{escape}}
```

remains high.

Then local Gate/audit is not containing failure as intended.

---

# 31. FAILURE OF FALSE-GREEN DETECTION

A core project concept is:

```text
FALSE-GREEN
```

This claim is unsupported if process-aware verification does not distinguish:

```text
correct endpoint / invalid route
```

from:

```text
correct endpoint / valid route
```

better than simple answer checking.

---

# 32. FAILURE OF PROVENANCE

Provenance is unnecessary if:

```text
removing provenance has no effect
```

on:

```text
equifinality
post-hoc explanation
reconstruction
reentry
False-Green detection
```

Then provenance may be reduced to debugging metadata.

---

# 33. FAILURE OF UNCERTAINTY CONTROL

Uncertainty is not useful if:

```text
confidence is uncalibrated
high uncertainty does not predict failure
Gate thresholds do not benefit from it
```

Then uncertainty should not drive decisions until recalibrated.

---

# 34. FAILURE OF "RESONANCE"

If "resonance" cannot be linked to:

```text
cycle consistency
state similarity
constraint satisfaction
coupling stability
```

through an explicit metric, it must remain metaphorical.

Do not treat the word as evidence.

---

# 35. FAILURE OF "CRYSTAL"

`STATE: CRYSTAL` is a documentation marker.

It must not be interpreted as:

```text
scientific validation
mathematical proof
experimental confirmation
```

It means only:

```text
the current document/spec is internally stabilized enough
to be treated as a canonical working version
```

---

# 36. FAILURE OF UNIVERSAL CROSS-DOMAIN CLAIMS

A pattern that works in:

```text
mathematics
```

does not automatically transfer to:

```text
biology
physics
psychology
materials
economics
```

Cross-domain analogy is useful for generating hypotheses.

It is not evidence of a shared physical mechanism.

Each domain requires its own validation.

---

# 37. ANALOGY FAILURE

An analogy should be discarded if it predicts nothing measurable.

Example:

```text
"this resembles a membrane"
```

is not useful unless it implies a testable behavior such as:

```text
selective boundary
threshold transition
controlled exchange
```

Use analogy only when it produces operational variables.

---

# 38. CATEGORY ERROR — TOPOLOGY

Do not call every structural change:

```text
topology
```

Strict topology concerns properties invariant under continuous deformation.

Graph connectivity, hierarchy, tensor fields, and geometry are related but distinct concepts.

Use precise terms.

---

# 39. CATEGORY ERROR — DIMENSION

Do not infer mathematical dimension from:

```text
number of nodes
number of triangles
number of roles
number of layers
```

For example:

```text
14 states
```

does not automatically mean:

```text
14-dimensional topological space
```

unless explicitly defined that way.

---

# 40. CATEGORY ERROR — TENSOR

Do not use:

```text
tensor
```

to mean:

```text
any multidimensional table
```

unless the mathematical transformation properties matter.

A matrix or multidimensional array may be sufficient terminology.

---

# 41. CATEGORY ERROR — QUANTUM

Do not use quantum terminology to justify AI architecture unless the mechanism genuinely depends on quantum theory.

Similarity of words such as:

```text
state
field
superposition
transition
```

does not establish physical equivalence.

---

# 42. CATEGORY ERROR — ENTROPY

Entropy has precise meanings in:

```text
thermodynamics
information theory
dynamical systems
```

If using entropy for simplex activation, define the exact formula.

Do not mix it automatically with physical thermodynamic entropy.

---

# 43. CATEGORY ERROR — ENERGY

If a reasoning metric is called:

```text
energy
```

define the function explicitly.

Do not imply physical energy unless units and physical interpretation exist.

---

# 44. CATEGORY ERROR — RESONANCE

Physical resonance requires specific dynamical conditions.

A software "resonance score" is an analogy unless derived from an actual oscillatory system.

Keep names separate from claims.

---

# 45. CATEGORY ERROR — CONSCIOUSNESS

The architecture may model:

```text
state
boundary
transition
memory
self-monitoring
```

but this does not establish consciousness.

Any claims about consciousness require independent philosophical, cognitive, or neuroscientific evidence.

---

# 46. CATEGORY ERROR — MEMORY

A stored state is computer memory.

That does not imply:

```text
biological memory
physical memory of space
cosmic memory
```

without separate evidence.

Cross-domain metaphors should remain labeled.

---

# 47. HIDDEN ASSUMPTION — CORRECT GRAPH

Many architecture benefits assume a reasonably correct dependency graph.

If graph extraction is poor:

```text
every later layer inherits the mistake
```

Therefore graph extraction is a possible single point of failure.

---

# 48. HIDDEN ASSUMPTION — LOCALITY

The architecture assumes useful local groups exist.

This should be measured through:

```text
cut cost
internal coupling
boundary coupling
treewidth
reopen rate
```

Locality must not be assumed.

---

# 49. HIDDEN ASSUMPTION — CRITICALITY CAN BE ESTIMATED

Shadow and edge pruning depend on knowing what is important.

If criticality prediction is unreliable:

```text
the system may discard exactly the rare feature that matters later
```

This is a major risk.

---

# 50. HIDDEN ASSUMPTION — FUTURE RELEVANCE CAN BE PREDICTED

Compression requires guessing which details will matter later.

This is fundamentally difficult.

Shadow partly mitigates the problem.

But if future relevance is highly unpredictable, compression benefit may remain limited.

---

# 51. HIDDEN ASSUMPTION — RECONSTRUCTION IS USEFUL

Some tasks only need:

```text
forward correctness
```

and do not benefit from reconstructing the path.

In those domains, `-3` may add unnecessary cost.

---

# 52. HIDDEN ASSUMPTION — VERIFICATION IS CHEAPER THAN RECOMPUTATION

Gate / backward audit are useful only if:

```text
verification cost
<
cost of failure or full recomputation
```

If verification is equally expensive as solving the task again, architecture benefits may disappear.

---

# 53. HIDDEN ASSUMPTION — COMMIT HISTORY HAS VALUE

Bindu assumes persistent lineage matters.

For short one-shot tasks it may not.

Bindu may be useful mainly for:

```text
agents
long-running projects
reused proofs
software workflows
persistent research memory
```

---

# 54. HIDDEN ASSUMPTION — STRUCTURE CAN BE EXTERNALIZED

Some model capabilities may depend on dense latent interactions that do not map cleanly into explicit symbolic graphs.

The architecture should not assume every useful internal process can be externalized losslessly.

---

# 55. FAILURE MODE — REPRESENTATION BOTTLENECK

A small interpretable state may remove information that the LLM hidden state already represents correctly.

Then adding the control layer can make reasoning worse.

This is a central possible negative result.

---

# 56. FAILURE MODE — CONTROL OVERRIDES CAPABILITY

An over-constrained Gate may block a model from using flexible heuristics that are actually correct.

Verification should not become unnecessary rigidity.

---

# 57. FAILURE MODE — META-REASONING OVERHEAD

The model may spend more effort reasoning about:

```text
reasoning state
Gate state
Shadow state
audit state
```

than solving the actual problem.

Measure:

```text
meta-reasoning token fraction
```

where possible.

---

# 58. FAILURE MODE — SELF-REFERENTIAL LOOP

The architecture may create:

```text
audit the audit
Gate the Gate
Shadow of Shadow
```

recursively.

Set explicit stopping rules.

Do not let meta-verification recurse without bound.

---

# 59. FAILURE MODE — SHADOW DEBT

Repeated compression may defer too many unresolved details.

The active state remains clean while hidden residual debt accumulates.

This can create delayed catastrophic failure.

Track:

```math
D_S
```

and force periodic resolution.

---

# 60. FAILURE MODE — STALE CERTIFICATE

A parent certificate may remain true only under old assumptions.

If a dependency changes:

```text
certificate must become stale
```

Do not reuse it automatically.

---

# 61. FAILURE MODE — STALE EDGE

A cross-branch relation may change while node summaries remain similar.

If edge state is not versioned, the system may reason from outdated coupling.

---

# 62. FAILURE MODE — WRONG LOCALITY

A grouping policy may repeatedly place strongly coupled nodes in different subtrees.

Signals:

```text
high boundary cut
high reopen rate
high regroup churn
```

This should trigger regrouping or abandonment of hierarchical compression.

---

# 63. FAILURE MODE — GROUPING INSTABILITY

If tiny input changes produce completely different grouping:

```text
the hierarchy may be brittle
```

Measure grouping stability under perturbations.

---

# 64. FAILURE MODE — CATASTROPHIC PRUNING

One low-magnitude edge may be causally critical.

Magnitude-based pruning alone is unsafe.

Criticality must consider downstream structure.

---

# 65. FAILURE MODE — MISLEADING CONFIDENCE

A well-structured certificate may create an illusion of certainty.

Certificates only verify declared checks.

They do not validate:

```text
missing assumptions
unknown unknowns
bad source data
incorrect world model
```

---

# 66. FAILURE MODE — BENCHMARK GAMING

A system may learn benchmark-specific decomposition tricks.

Therefore:

```text
held-out generators
held-out graph shapes
cross-domain tests
```

are required.

---

# 67. FAILURE MODE — ORACLE DEPENDENCE

If the architecture works only when supplied with the true graph:

```text
graph extraction remains unsolved
```

This is a partial result, not an end-to-end success.

---

# 68. FAILURE MODE — MODEL-SPECIFIC TUNING

If gains appear only on one model and disappear on others, report:

```text
model-specific compatibility
```

not universal architectural benefit.

---

# 69. FAILURE MODE — SEED INSTABILITY

If gains depend on one random seed:

```text
evidence is weak
```

Require replication.

---

# 70. FAILURE MODE — COST HIDING

Do not compare:

```text
one-shot baseline
```

against:

```text
multi-call audited architecture
```

without reporting additional cost.

Matched compute is essential.

---

# 71. FAILURE MODE — MEMORY HIDING

Do not report only:

```text
active parent size
```

while ignoring:

```text
Shadow
provenance
Gate history
MemoryAtoms
```

Report total memory too.

---

# 72. FAILURE MODE — TOOL ADVANTAGE

If one system receives:

```text
Python
calculator
symbolic solver
```

and another does not, the comparison is invalid unless tool availability is the experimental variable.

---

# 73. FAILURE MODE — PROMPT ADVANTAGE

A more detailed prompt can itself improve performance.

Architecture comparisons should isolate:

```text
prompting benefit
```

from:

```text
runtime structure benefit
```

---

# 74. FAILURE MODE — TRAINING DATA LEAKAGE

If benchmark examples or generator rules are leaked into tuning, results may overstate generalization.

Use held-out generation.

---

# 75. FAILURE MODE — EVALUATOR BIAS

If the same model generates and judges the reasoning:

```text
evaluation may be biased
```

Prefer deterministic metrics where possible.

---

# 76. FAILURE MODE — NON-INDEPENDENT METRICS

Several metrics may measure the same underlying behavior.

Do not treat ten correlated metrics as ten independent confirmations.

Report metric relationships.

---

# 77. FAILURE MODE — POST-HOC THRESHOLDING

Choosing Gate thresholds after seeing test labels inflates results.

Thresholds must be selected on validation data.

---

# 78. FAILURE MODE — POST-HOC WIDTH SELECTION

If 14/10/10/8 is selected after trying many width combinations, its apparent success may be multiple-comparison noise.

Preregister candidate sequences.

---

# 79. FAILURE MODE — RETROFITTED INTERPRETATION

Do not interpret any learned pattern as confirmation of the original symbolism after the fact.

Example:

```text
learned effective width = 9
```

should not be re-described as:

```text
"close enough to 10"
```

unless tolerance was specified beforehand.

---

# 80. FALSIFICATION — COUPLING HYPOTHESIS

Hypothesis:

```text
explicit coupling helps when endpoint nodes are insufficient
```

Falsification test:

```text
same-node / different-edge tasks
```

If node-only systems perform equally:

```text
coupling memory hypothesis weakens
```

---

# 81. FALSIFICATION — SHADOW HYPOTHESIS

Hypothesis:

```text
Shadow improves recoverability under compression
```

Falsification:

```text
same parent size
same compute
Shadow vs no Shadow
```

If reconstruction and task accuracy do not improve:

```text
Shadow is unnecessary
```

---

# 82. FALSIFICATION — BACKWARD HYPOTHESIS

Hypothesis:

```text
-3 detects local loss
```

Inject known corruption.

If detection is no better than baseline:

```text
backward audit fails
```

---

# 83. FALSIFICATION — GATE HYPOTHESIS

Hypothesis:

```text
Gate reduces False-Green
```

Create correct-endpoint / invalid-route cases.

If false allow does not fall:

```text
Gate fails its central purpose
```

---

# 84. FALSIFICATION — HIERARCHY HYPOTHESIS

Hypothesis:

```text
hierarchy delays reasoning collapse
```

Run difficulty sweep under matched compute.

If:

```math
N_{50}^{\mathrm{hierarchy}}
\le
N_{50}^{\mathrm{graph}}
```

then the depth-extension claim fails.

---

# 85. FALSIFICATION — REPAIR HYPOTHESIS

Hypothesis:

```text
local repair is cheaper
```

Inject local error.

If repair span/cost is not smaller than restart:

```text
repair advantage fails
```

---

# 86. FALSIFICATION — BINDU HYPOTHESIS

Hypothesis:

```text
verified memory helps reuse
```

Run repeated-task suite.

If:

```text
compute savings <= stale reuse cost
```

then persistent commit provides no net benefit.

---

# 87. FALSIFICATION — GSL HYPOTHESIS

Hypothesis:

```text
6D state helps routing/control
```

If random/flat alternatives perform the same:

```text
GSL should be downgraded
```

---

# 88. FALSIFICATION — HEXAGRAM HYPOTHESIS

Hypothesis:

```text
FORM/FLOW grouping is meaningful
```

If random partitions or learned grouping perform equally:

```text
Hexagram is not computationally privileged
```

---

# 89. FALSIFICATION — FUNNEL HYPOTHESIS

Hypothesis:

```text
14/10/10/8 is near a useful Pareto frontier
```

If matched alternatives dominate:

```text
reject privileged funnel claim
```

---

# 90. FALSIFICATION — CROSS-DOMAIN HYPOTHESIS

Hypothesis:

```text
architecture transfers across task domains
```

If gains remain confined to synthetic arithmetic:

```text
claim must stay domain-specific
```

---

# 91. EXPECTED FAILURE REGIMES

The architecture is expected to struggle when:

```text
dependency graph is densely coupled
critical information cannot be predicted before compression
task structure changes rapidly
graph extraction is unreliable
verification cost approaches solving cost
semantic relations cannot be discretized cleanly
```

Predicting these regimes strengthens the theory.

---

# 92. EXPECTED SUCCESS REGIMES

The architecture is most plausible when:

```text
dependencies are explicit or inferable
subproblems have local closure
critical edges can be identified
errors can be localized
subproblems are reusable
active memory is a real bottleneck
```

These should be targeted first.

---

# 93. SCOPE LIMIT — MATHEMATICAL PROOFS

Formal proof assistants already provide strong verification.

The architecture should not claim superiority over:

```text
Lean
Coq
Isabelle
formal theorem provers
```

without direct evidence.

A more realistic role is:

```text
LLM reasoning control before formal verification
```

or:

```text
hierarchical organization of proof search
```

---

# 94. SCOPE LIMIT — CODE

Compilers and static analyzers already have precise graph structures.

Vuzol-19 must compete against:

```text
AST
CFG
SSA
dependency graphs
symbolic execution
```

It should add value only where:

```text
LLM semantic reasoning
uncertainty
repair
cross-module synthesis
```

matter.

---

# 95. SCOPE LIMIT — RETRIEVAL

If the main challenge is finding one fact in a long context:

```text
RAG
indexing
search
attention optimization
```

may be more appropriate than recursive reasoning trees.

Do not apply the architecture to every long-context problem.

---

# 96. SCOPE LIMIT — SIMPLE TASKS

For short tasks, the overhead may exceed benefit.

A simple direct model call may be best.

The architecture should be activated by difficulty/risk, not universally.

---

# 97. SCOPE LIMIT — HIGHLY DYNAMIC ENVIRONMENTS

If world state changes faster than verification completes:

```text
certificates may become stale before commit
```

The architecture needs temporal validity or may not be appropriate.

---

# 98. SCOPE LIMIT — HIGHLY STOCHASTIC TASKS

When uncertainty is intrinsic and exact reconstruction is impossible:

```text
probabilistic state
distributional reasoning
Bayesian updates
```

may be more appropriate than strict local reconstruction.

---

# 99. SCOPE LIMIT — CREATIVE TASKS

Creative writing does not always have:

```text
correct dependency graph
hard constraints
single valid route
```

Gate may over-constrain creativity.

Use only light structure where relevant.

---

# 100. SCOPE LIMIT — HUMAN VALUES

Human ethics and values cannot be reduced safely to six axes or a fixed Gate without broader social, legal, and contextual reasoning.

The architecture is not a complete moral system.

---

# 101. RESEARCH DISCIPLINE RULE

When a result is unexpected:

```text
first ask whether the hypothesis was wrong
```

before adding a new hidden mechanism to explain it.

Avoid unfalsifiable patching.

---

# 102. PATCHING RULE

A new component may be added only if:

```text
a specific observed failure exists
the new component predicts a measurable improvement
the improvement can be ablated
```

Do not add components only to preserve symbolic symmetry.

---

# 103. COMPLEXITY PENALTY

Every new component should carry an implicit cost:

```text
implementation complexity
memory
latency
new failure modes
calibration burden
```

A small performance gain may not justify a large complexity increase.

---

# 104. MINIMUM DESCRIPTION PRINCIPLE

Prefer the simplest architecture that explains the measured gains.

If:

```text
Graph + Gate
```

performs like:

```text
Graph + Triads + Shadow + -3 + Gate + Bindu
```

use:

```text
Graph + Gate
```

for that domain.

---

# 105. SURVIVING CORE

After experiments, the final Vuzol-19 architecture may be smaller than the current design.

That is acceptable.

A successful research process may produce:

```text
fewer components
better definitions
clearer scope
stronger evidence
```

---

# 106. COMPONENT STATUS LABELS

Every major component should eventually receive one status:

```text
CORE
SUPPORTED
OPTIONAL
EXPERIMENTAL
DEPRECATED
REJECTED
```

based on evidence.

---

# 107. EVIDENCE TABLE

Recommended future table:

| Component | Current Status | Supporting Evidence | Falsification Result | Decision |
|---|---|---|---|---|
| Dependency Graph | CORE | | | |
| Coupling Memory | EXPERIMENTAL | | | |
| Triads | EXPERIMENTAL | | | |
| Shadow | EXPERIMENTAL | | | |
| -3 Audit | EXPERIMENTAL | | | |
| Gate | EXPERIMENTAL | | | |
| Bindu | EXPERIMENTAL | | | |
| GSL 6D | EXPERIMENTAL | | | |
| Hexagram | EXPERIMENTAL | | | |
| 14/10/10/8 | EXPERIMENTAL | | | |

This table should change as experiments accumulate.

---

# 108. REPLICATION REQUIREMENT

A component should not be promoted from:

```text
EXPERIMENTAL
```

to:

```text
SUPPORTED
```

based on one run.

Require:

```text
multiple seeds
held-out data
at least one strong baseline
reproducible code
```

and ideally:

```text
more than one model
```

---

# 109. CROSS-DOMAIN REQUIREMENT

A claim of generality requires at least:

```text
two meaningfully different task domains
```

A result on several arithmetic datasets still belongs to one broad domain.

---

# 110. EXTERNAL REPLICATION

Strong evidence would include:

```text
independent implementation
independent dataset
or
external researcher reproduction
```

This is a later-stage goal.

---

# 111. OPEN-WORLD WARNING

Synthetic benchmarks provide complete ground truth.

Real-world reasoning often does not.

Therefore:

```text
perfect benchmark Gate
```

does not imply:

```text
perfect real-world Gate
```

Unknown assumptions and missing evidence remain possible.

---

# 112. UNKNOWN MUST REMAIN A VALID OUTPUT

One of the architecture's strengths should be the ability to say:

```text
UNKNOWN
```

when:

```text
evidence is insufficient
resource budget exhausted
graph is incomplete
critical Shadow unresolved
```

Do not optimize UNKNOWN away merely to increase completion rate.

---

# 113. UNKNOWN CALIBRATION

Measure whether UNKNOWN correlates with genuinely difficult or underdetermined tasks.

A system that returns UNKNOWN randomly is not well calibrated.

---

# 114. HOLD MUST REMAIN TEMPORARY

`HOLD` should mean:

```text
repairable / awaiting evidence
```

not permanent uncertainty.

If HOLD nodes never resolve, the system needs:

```text
timeout
escalation
or UNKNOWN
```

---

# 115. FALSE CERTAINTY PENALTY

For high-risk tasks, false ALLOW should carry larger penalty than false HOLD.

For low-risk tasks, the balance may differ.

This is a policy choice and must be explicit.

---

# 116. OPERATOR AUTHORITY LIMIT

Gate/Bindu should not be interpreted as permission to perform real-world actions unless a separate authority system exists.

Reasoning validity and action authorization are different layers.

---

# 117. EXTERNAL ACTION SAFETY

For tool actions:

```text
AI Gate
-> authority check
-> human / policy Gate if required
-> external commit
```

The reasoning architecture cannot replace authorization, consent, or safety policy.

---

# 118. DATA QUALITY LIMIT

A perfectly structured reasoning graph can still produce wrong conclusions from bad input data.

Therefore final confidence should depend on:

```text
source quality
observation quality
data uncertainty
```

not only internal consistency.

---

# 119. SOURCE TRUTH VS ROUTE TRUTH

Separate:

```text
route valid
```

from:

```text
premises true
```

A valid derivation from false premises remains false about the world.

Gate must not confuse logical consistency with empirical truth.

---

# 120. INTERNAL CONSISTENCY VS EXTERNAL VALIDITY

The architecture is strongest at:

```text
internal dependency integrity
```

External validity requires:

```text
measurement
observation
trusted sources
experiments
```

This is a key scope boundary.

---

# 121. FALSIFIABILITY CHECKLIST

Before accepting a new Vuzol-19 claim, ask:

```text
What is the measurable variable?

What is the baseline?

What result would count against the claim?

What is the resource budget?

What is the held-out test?

Is the term formal or metaphorical?

Could a simpler explanation account for the result?

Could this be benchmark leakage?

Could this be prompt advantage?

Could this be extra compute?

Could this be one-seed noise?
```

---

# 122. CLAIM AUDIT TEMPLATE

Use:

```text
CLAIM:
...

TYPE:
FACT / MODEL / HYPOTHESIS / METAPHOR

MEASUREMENT:
...

BASELINE:
...

FALSIFICATION:
...

RESOURCE CONTROL:
...

CURRENT EVIDENCE:
...

STATUS:
...
```

This template can be used in future files.

---

# 123. EXAMPLE — SHADOW CLAIM AUDIT

```text
CLAIM:
Shadow improves recoverability.

TYPE:
HYPOTHESIS

MEASUREMENT:
reconstruction error
repair success
root accuracy

BASELINE:
same parent representation without Shadow

FALSIFICATION:
no improvement under matched memory/compute

CURRENT EVIDENCE:
not yet established

STATUS:
EXPERIMENTAL
```

---

# 124. EXAMPLE — COUPLING CLAIM AUDIT

```text
CLAIM:
Explicit edge memory improves relation-sensitive reasoning.

TYPE:
HYPOTHESIS

MEASUREMENT:
critical edge recall
accuracy on same-node/different-edge tasks

BASELINE:
node-only model

FALSIFICATION:
no significant difference

STATUS:
EXPERIMENTAL
```

---

# 125. EXAMPLE — 14/10/10/8 CLAIM AUDIT

```text
CLAIM:
14/10/10/8 is a useful compression funnel.

TYPE:
HYPOTHESIS

MEASUREMENT:
accuracy
memory
reconstruction
compute
Pareto position

BASELINE:
alternative fixed and learned widths

FALSIFICATION:
matched alternatives dominate

STATUS:
EXPERIMENTAL
```

---

# 126. EXAMPLE — BINDU CLAIM AUDIT

```text
CLAIM:
Separating Gate from commit improves persistent reasoning safety.

TYPE:
HYPOTHESIS

MEASUREMENT:
stale reuse
rollback success
invalid commit rate

BASELINE:
ordinary checkpointing

FALSIFICATION:
no reliability improvement or worse reuse outcomes

STATUS:
EXPERIMENTAL
```

---

# 127. SCIENTIFIC STATUS OF THE CURRENT PROJECT

At this stage:

```text
the architecture is a research specification
```

not:

```text
a validated theory of intelligence
a universal theory of transitions
a proven cognitive model
a proven physical law
```

Its value now is:

```text
clear decomposition
testable operators
explicit failure criteria
benchmark plan
```

---

# 128. WHAT WOULD BE A STRONG FIRST RESULT

A strong first result would be something narrow and measurable, for example:

> On synthetic long-dependency graphs under equal model-call budget, Graph + Coupling + Shadow + -3 + Gate reduced error escape by a reproducible margin relative to an explicit graph baseline, while preserving comparable exact-answer accuracy.

That would justify further development.

---

# 129. WHAT WOULD BE A STRONG NEGATIVE RESULT

A strong negative result would be:

> The explicit dependency graph baseline matched the full architecture on N50, error escape, and repair cost while using less memory and latency.

That would justify simplification.

Both outcomes are useful.

---

# 130. NEXT FILE

Next:

```text
19_IMPLEMENTATION_ROADMAP.md
```

Its purpose is to convert the full theory into an executable development sequence.

It will define:

```text
Milestone 0 — deterministic core
Milestone 1 — graph runtime
Milestone 2 — +3/-3
Milestone 3 — Shadow
Milestone 4 — Gate
Milestone 5 — benchmark harness
Milestone 6 — LLM integration
Milestone 7 — GSL / Hexagram
Milestone 8 — funnel
Milestone 9 — cross-domain validation
```

---

## FILE VERDICT

```text
STATE: CRYSTAL

DEFINED:
Failures and Falsifiability

CORE RULE:
every major Vuzol-19 claim must have
a measurable failure condition

SEPARATED:
FACT
MODEL
HYPOTHESIS
METAPHOR
ENGINEERING CHOICE

CRITICAL LIMIT:
internal consistency is not the same as external truth

NEXT:
19_IMPLEMENTATION_ROADMAP.md
```
