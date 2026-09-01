# 19 — IMPLEMENTATION ROADMAP

**Project:** Vuzol-19  
**Module:** Hexagram Simplicial Reasoning  
**Status:** EXECUTION ROADMAP / BUILD ORDER  
**State:** CRYSTAL  
**Language:** English  
**Depends on:** `18_FAILURES_FALSIFIABILITY.md`

---

## 0. PURPOSE

The previous files defined:

```text
the problem
state representation
coupling
recursive triads
+3 Forward
-3 Backward
Shadow
Gate
Bindu
recursive hierarchy
benchmark strategy
falsification criteria
```

This final file converts the research architecture into an executable build sequence.

The central rule is:

> **Build the smallest deterministic mechanism first. Add learned or symbolic layers only after the lower layer has measurable value.**

The roadmap is intentionally staged so that each milestone can fail independently without invalidating the entire project.

---

# 1. DEVELOPMENT PRINCIPLE

Do not implement:

```text
the whole architecture at once
```

Instead:

```text
build
test
measure
freeze
integrate
ablate
```

The system should grow only when the previous layer has:

```text
working tests
clear metrics
known failure modes
```

---

# 2. TOP-LEVEL MILESTONES

Canonical build sequence:

```text
M0 — Repository / contracts / deterministic core

M1 — Dependency graph runtime

M2 — +3 Forward

M3 — -3 Backward

M4 — Shadow / residual memory

M5 — Gate

M6 — Bindu / MemoryAtom

M7 — Recursive reasoning tree

M8 — Benchmark harness

M9 — LLM integration

M10 — GSL 6D

M11 — Hexagram controller

M12 — 14/10/10/8 funnel

M13 — Cross-domain validation

M14 — Evidence review / architecture reduction
```

Each milestone has:

```text
GOAL
INPUTS
OUTPUTS
TESTS
EXIT CRITERIA
STOP CONDITIONS
```

---

# 3. REPOSITORY LAYOUT

Recommended structure:

```text
00_HEXAGRAM_SIMPLICIAL_REASONING/
|
+-- docs/
|
+-- vuzol_reasoning/
|   +-- __init__.py
|   +-- models.py
|   +-- graph.py
|   +-- triads.py
|   +-- plus3.py
|   +-- minus3.py
|   +-- shadow.py
|   +-- gate.py
|   +-- bindu.py
|   +-- memory.py
|   +-- scheduler.py
|   +-- gsl.py
|   +-- hexagram.py
|   +-- funnel.py
|   +-- runtime.py
|   +-- metrics.py
|
+-- tests/
|
+-- experiments/
|   +-- configs/
|   +-- runners/
|   +-- datasets/
|   +-- results/
|   +-- reports/
|
+-- benchmarks/
|
+-- examples/
|
+-- README.md
```

The current Markdown files may remain at the project root if preferred.

---

# 4. MILESTONE 0 — CONTRACTS AND DETERMINISTIC CORE

## Goal

Create the minimum typed state system.

No LLM.

No learned model.

No symbolic geometry requirement.

Implement:

```text
ReasoningNode
Edge
Triad
CandidateParent
BackwardResult
ShadowRecord
GateResult
MemoryAtom
FailureAtom
```

---

# 5. M0 — MODELS

Suggested initial dataclasses:

```python
@dataclass
class ReasoningNode:
    id: str
    value: Any
    node_type: str
    uncertainty: float
    provenance: dict
```

```python
@dataclass
class Edge:
    source: str
    target: str
    relation: str
    weight: float
    critical: bool
```

```python
@dataclass
class Triad:
    children: list[str]
    internal_edges: list[Edge]
    boundary_edges: list[Edge]
```

Keep the first contracts minimal.

---

# 6. M0 — EXIT CRITERIA

Milestone 0 is complete when:

```text
all core objects serialize
all objects have stable IDs
schemas are versioned
unit tests pass
no LLM required
```

Recommended test:

```text
pytest
```

with deterministic outputs.

---

# 7. M0 — STOP CONDITION

Stop and redesign if:

```text
object contracts change on every new test
```

This means the architecture is not yet defined cleanly enough.

Do not proceed by accumulating ad-hoc fields.

---

# 8. MILESTONE 1 — DEPENDENCY GRAPH RUNTIME

## Goal

Create the strongest simple baseline first:

```text
explicit dependency graph
```

Use:

```text
NetworkX
```

or another simple graph library.

Required operations:

```text
add_node
add_edge
remove_edge
boundary_edges
critical_edges
topological_order
invalidate_dependents
shared_subproblems
```

---

# 9. M1 — GRAPH CONTRACT

Graph:

```math
G=(V,E)
```

Node state:

```text
value
type
provenance
uncertainty
```

Edge state:

```text
source
target
relation
criticality
weight
direction
```

This becomes the baseline that all later architecture must beat.

---

# 10. M1 — FIRST TEST DATA

Use exact synthetic graphs.

Example:

```text
A = 4
B = 7
C = A + B
D = C * 2
```

Ground-truth graph:

```text
A -> C
B -> C
C -> D
```

Tests:

```text
edge recall
topological order
dependency invalidation
```

---

# 11. M1 — EXIT CRITERIA

Complete when:

```text
graph execution is correct
dependency invalidation works
shared nodes work
critical edges are identifiable
graph metrics are logged
```

At this point, there is already a complete strong baseline.

---

# 12. MILESTONE 2 — +3 FORWARD

## Goal

Implement local synthesis.

Start with exact deterministic cases.

Example:

```text
(4, 7, ADD)
-> 11
```

The output should include:

```text
parent value
child IDs
retained interface
certificate
uncertainty
```

Do not add learned compression yet.

---

# 13. M2 — SIMPLE FORWARD POLICIES

Implement several policies:

```text
exact_arithmetic
mean_summary
weighted_summary
symbolic_relation
```

The purpose is not to choose one universal forward operator.

The purpose is to establish a common interface.

---

# 14. M2 — GROUPING BASELINES

Implement:

```text
sequential grouping
random grouping
dependency-aware grouping
```

Do not assume ternary grouping is useful until benchmarked.

---

# 15. M2 — EXIT CRITERIA

Complete when:

```text
three children can create one parent
grouping metadata is exact
critical boundary edges survive
forward certificate exists
tests cover exact and lossy cases
```

---

# 16. MILESTONE 3 — -3 BACKWARD

## Goal

Implement local reconstructability audit.

Start with deterministic reconstruction only.

Do not use an LLM as backward decoder in the first version.

---

# 17. M3 — FIRST CASES

Implement:

```text
exact inverse case
partial reconstruction
many-to-one ambiguity
non-invertible case
```

Example:

```math
y=x^2
```

with:

```math
y=4
```

Expected:

```text
AMBIGUOUS
```

unless branch identity exists.

---

# 18. M3 — METRICS

Add:

```text
reconstruction error
component residuals
edge reconstruction error
ambiguity count
cycle consistency
```

Both cycles:

```text
X -> P -> X_hat
```

and:

```text
P -> X_hat -> P_hat
```

---

# 19. M3 — EXIT CRITERIA

Complete when:

```text
exact cases reconstruct exactly
ambiguous cases remain ambiguous
non-invertible cases are labeled honestly
edge mismatch is detected
cycle metrics are stable
```

---

# 20. MILESTONE 4 — SHADOW

## Goal

Introduce controlled lossy compression.

Implement typed residual memory.

Start with:

```text
numeric residual
omitted edge
omitted child
branch identity
approximation remainder
provenance pointer
```

---

# 21. M4 — SHADOW STORE

First implementation:

```text
in-memory dictionary
```

Then optionally:

```text
SQLite
```

Required operations:

```text
put
get
find_by_parent
promote
expire
tombstone
```

---

# 22. M4 — SHADOW METRICS

Track:

```text
Shadow size
Shadow ratio
total compression ratio
retrieval hit rate
miss rate
reopen rate
critical residual retention
```

Do not claim compression benefit without including Shadow cost.

---

# 23. M4 — EXIT CRITERIA

Complete when:

```text
lossy parent can be reconstructed better with Shadow
critical residuals survive
total memory is measured
Shadow corruption can be detected
```

---

# 24. MILESTONE 5 — GATE

## Goal

Separate:

```text
candidate generation
```

from:

```text
permission to promote
```

Implement hard checks first.

---

# 25. M5 — FIRST HARD CHECKS

Start with:

```text
schema valid
hard constraints pass
critical edge present
branch identity valid
no unresolved critical Shadow
```

Only after this add:

```text
soft reconstruction threshold
uncertainty threshold
resource threshold
```

---

# 26. M5 — VERDICTS

Canonical runtime verdicts:

```text
ALLOW
HOLD
EXPAND
RECOMPUTE
SHADOW
UNKNOWN
```

Every non-ALLOW result must include:

```text
reason_codes
```

---

# 27. M5 — GATE TEST SET

Construct synthetic local states labeled:

```text
valid
invalid
ambiguous
insufficient evidence
```

Measure:

```text
false allow
false hold
reason-code accuracy
repair routing accuracy
```

---

# 28. M5 — EXIT CRITERIA

Complete when:

```text
hard failures never receive ALLOW in unit tests
false hold is measurable
Gate outputs deterministic reason codes
repair action is explicit
```

---

# 29. MILESTONE 6 — BINDU / MEMORYATOM

## Goal

Create persistent verified commits.

First implementation should support:

```text
atomic commit
immutable records
parent lineage
rollback
supersede
reentry
```

---

# 30. M6 — MEMORY BACKEND

Start with:

```text
SQLite
```

because it provides:

```text
transactions
simple queries
local persistence
low complexity
```

Tables may include:

```text
memory_atoms
failure_atoms
gate_events
shadow_records
lineage
```

---

# 31. M6 — COMMIT SAFETY TESTS

Required tests:

```text
Gate HOLD cannot commit
partial write rolls back
invalidated state can be rolled back
superseded state remains in history
reentry checks version
```

---

# 32. M6 — EXIT CRITERIA

Complete when:

```text
commit is atomic
rollback works
lineage is inspectable
stale version is detected
FailureAtom can be stored separately
```

---

# 33. MILESTONE 7 — RECURSIVE REASONING TREE

## Goal

Scale local verified units.

Implement:

```text
bottom-up grouping
parent creation
ancestor invalidation
local repair
shared DAG references
```

Remember:

```text
tree = compression hierarchy
graph = dependency structure
```

---

# 34. M7 — FIRST TREE

Use 9 leaves:

```text
X1..X9
```

Build:

```text
P1 = X1,X2,X3
P2 = X4,X5,X6
P3 = X7,X8,X9
R  = P1,P2,P3
```

Inject one error into:

```text
X5
```

Expected repair:

```text
X5
-> P2
-> R
```

but not:

```text
P1
P3
```

---

# 35. M7 — METRICS

Track:

```text
active dependency depth
active node count
repair span
detection distance
error escape
reopen rate
group churn
cross-edge count
```

---

# 36. M7 — EXIT CRITERIA

Complete when:

```text
local repair does not recompute unrelated branches
cross-branch edges remain explicit
stale ancestors are detected
tree can handle shared DAG nodes
```

---

# 37. MILESTONE 8 — BENCHMARK HARNESS

## Goal

Create reproducible architecture comparison.

Implement runners for:

```text
System A
System D
System E
System G
System H
System I
```

First.

---

# 38. M8 — FIRST SYSTEMS

Recommended minimal experimental set:

```text
A — plain baseline
D — dependency graph
E — graph + hierarchy
G — hierarchy + coupling + Shadow
H — + backward audit
I — + Gate
```

Do not add GSL, Hexagram, Bindu reuse, or funnel yet.

---

# 39. M8 — FIRST DATASET

Begin with synthetic exact graphs.

Why:

```text
ground truth known
edge truth known
failure injection easy
evaluation deterministic
```

Only after instrumentation works, integrate GSM-Infinity.

---

# 40. M8 — RUN MANIFEST

Every experiment must store:

```text
run_id
seed
system config
task config
model config
budget
metrics
git commit
timestamp
```

---

# 41. M8 — EXIT CRITERIA

Complete when one command can:

```text
generate tasks
run selected systems
store logs
calculate metrics
produce result table
```

Example:

```text
python -m experiments.run --config configs/core_ablation.yaml
```

---

# 42. MILESTONE 9 — LLM INTEGRATION

## Goal

Insert an LLM only after deterministic control mechanics work.

Use the LLM for:

```text
candidate reasoning
semantic parsing
graph extraction
local explanation
```

Keep:

```text
IDs
Gate hard checks
commit
lineage
```

deterministic where possible.

---

# 43. M9 — ORACLE GRAPH FIRST

First LLM condition:

```text
LLM
+
oracle dependency graph
```

This isolates:

```text
reasoning
```

from:

```text
graph extraction
```

---

# 44. M9 — INFERRED GRAPH SECOND

Then require the LLM to infer:

```text
nodes
edges
operators
constraints
```

Measure:

```text
graph extraction precision/recall
```

separately.

---

# 45. M9 — EXIT CRITERIA

Complete when:

```text
oracle/inferred graph gap is measurable
local LLM proposals enter typed runtime
Gate can reject invalid proposals
LLM cannot bypass commit rules
```

---

# 46. MILESTONE 10 — GSL 6D

## Goal

Test GSL as a predictive control state.

Do not use keyword heuristics as final evidence.

Implementation sequence:

```text
v0 — keyword prototype
v1 — embedding + linear probe
v2 — hidden-state learned projector
```

---

# 47. M10 — LABELS

Need operational targets for:

```text
R pressure
O flow
Y structure
G balance
B law
V future
```

Possible labels may come from:

```text
synthetic task properties
human annotation
derived runtime metrics
```

Each axis must have measurable meaning.

---

# 48. M10 — ABLATIONS

Compare:

```text
GSL 6D
random 6D projection
PCA 6D
learned unconstrained 6D
full embedding
```

Targets:

```text
Gate calibration
failure prediction
scheduler routing
```

---

# 49. M10 — EXIT CRITERIA

GSL remains in runtime only if it improves at least one control task reproducibly.

Otherwise:

```text
diagnostic only
```

---

# 50. MILESTONE 11 — HEXAGRAM CONTROLLER

## Goal

Test:

```text
FORM = (Y,B,V)
FLOW = (R,O,G)
```

as a useful grouping.

Baselines:

```text
flat 6D
random 3+3
learned 3+3
```

---

# 51. M11 — TEST TARGETS

Measure:

```text
Gate calibration
repair routing
state transition prediction
scheduler decisions
```

If no improvement:

```text
Hexagram remains visualization
```

---

# 52. MILESTONE 12 — 14/10/10/8 FUNNEL

## Goal

Test the fixed funnel only after the core system is already working.

Implement as an optional module:

```yaml
funnel:
  enabled: true
  widths: [14, 10, 10, 8]
```

---

# 53. M12 — BASELINES

Required alternatives:

```text
14 -> 8
14 -> 10 -> 8
14 -> 12 -> 10 -> 8
14 -> 10 -> 10 -> 8
14 -> 14 -> 14 -> 14
learned width
adaptive width
```

---

# 54. M12 — EXIT CRITERIA

The fixed funnel becomes `SUPPORTED` only if it lies near the Pareto frontier for:

```text
accuracy
active memory
reconstruction
compute
```

across more than one task family.

Otherwise:

```text
EXPERIMENTAL
```

or:

```text
REJECTED
```

---

# 55. MILESTONE 13 — CROSS-DOMAIN VALIDATION

## Goal

Test whether the surviving architecture transfers.

Recommended order:

```text
1. synthetic arithmetic graphs
2. GSM-Infinity
3. limits/asymptotics
4. code traces
5. constraint planning
6. claim/evidence graphs
```

---

# 56. M13 — DOMAIN-SPECIFIC BASELINES

For code:

```text
AST
CFG
SSA
static analysis
symbolic execution
```

For math:

```text
symbolic solver
formal verifier
dependency graph
```

For text:

```text
RAG
claim graph
summary memory
```

The architecture must compete against domain-native tools.

---

# 57. M13 — EXIT CRITERIA

A general claim requires:

```text
benefit on at least two meaningfully different domains
```

with:

```text
matched resources
strong baselines
held-out data
```

---

# 58. MILESTONE 14 — ARCHITECTURE REDUCTION

## Goal

After experiments, remove unsupported components.

Create evidence table:

| Component | Status | Evidence | Cost | Decision |
|---|---|---|---|---|
| Dependency Graph | | | | |
| Coupling | | | | |
| Triads | | | | |
| Shadow | | | | |
| -3 | | | | |
| Gate | | | | |
| Bindu | | | | |
| GSL | | | | |
| Hexagram | | | | |
| Funnel | | | | |

Possible statuses:

```text
CORE
SUPPORTED
OPTIONAL
EXPERIMENTAL
DEPRECATED
REJECTED
```

---

# 59. FINAL ARCHITECTURE RULE

The final system should be:

```text
the smallest surviving architecture
```

not:

```text
the largest architecture originally imagined
```

Research success may mean deleting half the components.

---

# 60. VERSION 0.1 TARGET

A realistic first software release:

```text
v0.1
```

contains only:

```text
typed graph
Triad
+3 Forward
-3 Backward
Shadow
Gate
basic metrics
synthetic benchmark
```

No LLM required.

---

# 61. VERSION 0.2 TARGET

Add:

```text
recursive hierarchy
local repair
Bindu
MemoryAtom
SQLite persistence
```

---

# 62. VERSION 0.3 TARGET

Add:

```text
LLM adapter
oracle graph mode
inferred graph mode
benchmark runner
```

---

# 63. VERSION 0.4 TARGET

Add:

```text
GSM-Infinity adapter
error injection
N50 curves
equal-compute comparisons
```

---

# 64. VERSION 0.5 TARGET

Add:

```text
GSL 6D
Hexagram optional controller
```

only if they pass standalone predictive tests.

---

# 65. VERSION 0.6 TARGET

Add:

```text
14/10/10/8
alternative width search
adaptive funnel
```

as experimental modules.

---

# 66. VERSION 1.0 TARGET

A `1.0` claim should require:

```text
reproducible benchmark advantage
strong baseline comparison
documented failure boundary
cross-domain evidence
stable APIs
tests
versioned experiment configs
```

Do not call the architecture mature before this evidence exists.

---

# 67. FIRST IMPLEMENTATION SPRINT

Recommended first sprint:

```text
Day/Session 1:
models.py
graph.py

Day/Session 2:
plus3.py

Day/Session 3:
minus3.py

Day/Session 4:
shadow.py

Day/Session 5:
gate.py

Day/Session 6:
metrics.py

Day/Session 7:
synthetic experiment runner
```

The exact calendar is flexible.

The order is more important than the timing.

---

# 68. FIRST EXECUTABLE DEMO

Target demo:

```text
Input:
explicit 27-node dependency graph

Step:
group into local triads

Step:
compress each triad

Step:
inject one edge error

Step:
run -3 audit

Step:
Gate detects local failure

Step:
expand only failed subtree

Step:
repair

Step:
recompute affected ancestors

Output:
correct root
+
repair log
+
metrics
```

This is more valuable than a visually complex demo.

---

# 69. FIRST DEMO SUCCESS METRICS

The demo should print:

```text
root_correct
error_detected
error_detection_depth
repair_span
nodes_recomputed
edge_recall
Shadow_size
false_allow
runtime
```

This makes the architecture inspectable immediately.

---

# 70. FIRST EXPERIMENT CONFIG

Example:

```yaml
task:
  generator: synthetic_arithmetic_graph
  nodes: 27
  branching: 3
  error_injection: edge

system:
  graph: true
  triads: true
  coupling: true
  shadow: true
  backward: true
  gate: true
  bindu: false
  gsl: false
  hexagram: false
  funnel: false

budget:
  max_repairs: 3
  max_shadow_ratio: 0.5
```

---

# 71. FIRST COMPARISON

Run:

```text
System D:
dependency graph only
```

versus:

```text
System I-core:
graph + triads + coupling + Shadow + -3 + Gate
```

Measure:

```text
repair span
error escape
active memory
compute
```

This is the first meaningful architecture test.

---

# 72. DO NOT START WITH FULL GSL + SRI

The fastest way to make the project impossible to falsify is to start with:

```text
GSL
Hexagram
Sri
14/10/10/8
LLM
memory
tree
Gate
Bindu
```

all at once.

That creates too many interacting variables.

Build the mechanistic core first.

---

# 73. IMPLEMENTATION LANGUAGE

Recommended first language:

```text
Python
```

Reasons:

```text
fast prototyping
NetworkX
NumPy
PyTorch
scikit-learn
GUDHI / Ripser later if needed
easy benchmark integration
```

Performance optimization can come later.

---

# 74. FIRST DEPENDENCIES

Minimal package set:

```text
python >= 3.11
numpy
networkx
pydantic or dataclasses
pytest
pyyaml
pandas
matplotlib
```

Later:

```text
scikit-learn
torch
transformers
gudhi
ripser
```

Only add when needed.

---

# 75. TESTING STRATEGY

Maintain:

```text
unit tests
property tests
integration tests
benchmark tests
regression tests
```

Important invariants should have direct tests.

---

# 76. PROPERTY TEST — GATE

Property:

```text
a hard constraint failure never yields ALLOW
```

Test over many generated states.

---

# 77. PROPERTY TEST — COMMIT

Property:

```text
non-allowed candidate cannot become MemoryAtom
```

This should be impossible at API level.

---

# 78. PROPERTY TEST — SHADOW

Property:

```text
critical Shadow cannot expire under ordinary TTL policy
```

---

# 79. PROPERTY TEST — LINEAGE

Property:

```text
every committed parent can trace to source child IDs
```

unless explicitly external.

---

# 80. PROPERTY TEST — REPAIR

Property:

```text
repair of one isolated branch does not invalidate unrelated branches
```

when graph dependencies confirm independence.

---

# 81. PROPERTY TEST — AMBIGUITY

Property:

```text
many-to-one inverse without branch metadata does not produce unique PASS
```

---

# 82. CI REQUIREMENT

Before merging changes:

```text
unit tests pass
integration tests pass
schema compatibility checked
benchmark smoke test passes
```

Later add:

```text
performance regression thresholds
```

---

# 83. EXPERIMENT CONFIGURATION

All experimental choices should live in config files.

Avoid hidden defaults.

Version:

```text
grouping policy
Gate thresholds
Shadow budget
repair budget
funnel widths
model parameters
```

---

# 84. LOGGING

Use append-only logs.

Prefer:

```text
JSONL
```

for experiment events.

Every event should include:

```text
run_id
task_id
node_id
event_type
step
timestamp
schema_version
```

---

# 85. RESULT ARTIFACTS

Each experiment run should generate:

```text
config.yaml
manifest.json
events.jsonl
metrics.json
summary.md
plots/
```

This creates a reproducible evidence bundle.

---

# 86. FAILURE-FIRST DASHBOARD

The first dashboard should show:

```text
where errors entered
where they were detected
which Gate stopped them
which branch reopened
which parent became stale
what was recomputed
```

Do not begin with decorative geometric visualization.

---

# 87. VISUALIZATION AFTER METRICS

Later visualization may show:

```text
Hexagram state
triad hierarchy
Shadow load
Gate colors
dependency graph
```

But visualization follows measurement.

---

# 88. COLOR VERDICTS

If colors are used:

```text
green  = ALLOW
yellow = HOLD / SHADOW
orange = EXPAND / RECOMPUTE
red    = hard failure
gray   = UNKNOWN
```

Color must never replace text verdict.

---

# 89. SECURITY / AUTHORITY BOUNDARY

The runtime may verify reasoning.

It must not automatically grant:

```text
shell execution
network actions
Git actions
external writes
real-world control
```

Those require separate authority controls.

---

# 90. HUMAN REVIEW BOUNDARY

For high-impact use:

```text
AI reasoning
-> Gate
-> Human review
-> external action
```

Bindu for internal memory is different from authority to act.

---

# 91. DOCUMENTATION RULE

Every implementation module should have:

```text
purpose
input contract
output contract
invariants
failure modes
metrics
tests
```

This mirrors the Markdown architecture.

---

# 92. STATUS TAGS

Every module should declare:

```text
EXPERIMENTAL
SUPPORTED
CORE
DEPRECATED
```

based on evidence.

Avoid calling everything `CORE` before testing.

---

# 93. FIRST PAPER / REPORT TARGET

Do not begin with:

```text
universal theory of intelligence
```

A strong first paper/report could be:

> **Hierarchical Residual-Audited Reasoning for Long Dependency Graphs**

Focus on:

```text
graph
hierarchy
Shadow
backward audit
Gate
```

Keep symbolic inspiration secondary.

---

# 94. FIRST PAPER EXPERIMENTS

Minimum:

```text
synthetic graph benchmark
GSM-Infinity subset
dependency-graph baseline
hierarchy ablation
Shadow ablation
backward audit ablation
Gate ablation
equal-compute comparison
```

---

# 95. FIRST PAPER PRIMARY RESULT

Ideal narrow result:

```text
lower error escape
smaller repair span
or
higher N50
```

under matched resources.

Any one reproducible result can justify the next stage.

---

# 96. FIRST PAPER NEGATIVE RESULT

If no gain:

```text
publish / document the failure boundary
```

Example:

```text
hierarchy adds no benefit once an accurate dependency graph is available
```

That is still useful knowledge.

---

# 97. RESEARCH LOOP

Canonical loop:

```text
HYPOTHESIS
   |
   v
IMPLEMENT
   |
   v
UNIT TEST
   |
   v
BENCHMARK
   |
   v
ABLATE
   |
   v
FALSIFY
   |
   +--> FAIL -> simplify / remove
   |
   +--> PASS -> replicate
                  |
                  v
             cross-domain test
```

---

# 98. ARCHITECTURE EVOLUTION RULE

A new idea enters canonical architecture only after:

```text
1. explicit problem
2. measurable mechanism
3. baseline
4. test
5. ablation
6. result
```

Without these:

```text
keep as research note
```

---

# 99. IMPLEMENTATION PRIORITY MATRIX

| Component | Build Priority | Research Risk | Dependency |
|---|---:|---:|---|
| Typed graph | 1 | Low | None |
| Metrics | 1 | Low | None |
| +3 Forward | 2 | Medium | Graph |
| -3 Backward | 3 | Medium | +3 |
| Shadow | 4 | Medium | +3/-3 |
| Gate | 5 | Medium | Audit |
| Recursive hierarchy | 6 | Medium | Graph/Gate |
| Bindu | 7 | Medium | Gate |
| Benchmark harness | 8 | Low | Metrics |
| LLM adapter | 9 | High | Core runtime |
| GSL | 10 | High | LLM/labels |
| Hexagram | 11 | High | GSL |
| 14/10/10/8 | 12 | High | Stable core |

---

# 100. LOW-RISK FIRST

The project should prioritize the components that are easiest to verify independently:

```text
graph
metrics
deterministic operators
Gate invariants
```

before:

```text
semantic axes
symbolic geometry
learned funnels
```

---

# 101. HIGH-RISK LAST

The most speculative parts should be implemented last:

```text
GSL semantics
Hexagram control advantage
14/10/10/8 privileged widths
cross-domain universality
```

This protects the project from building its foundations on untested assumptions.

---

# 102. FIRST 100 TESTS TARGET

Before serious benchmark runs, aim for roughly:

```text
100 deterministic unit/property tests
```

across:

```text
graph
edges
triads
Shadow
Gate
commit
repair
versioning
```

The exact number is not sacred.

The point is broad invariant coverage.

---

# 103. RESEARCH BACKLOG

After v0.1:

```text
learned grouping
risk-based scheduler
calibrated uncertainty
adaptive Shadow budget
hypergraph support
probabilistic backward reconstruction
formal certificates
formal proof integration
code graph adapter
persistent agent memory
```

These are later projects.

---

# 104. HYPERGRAPH EXTENSION

If ordinary edges are insufficient, represent higher-order relations:

```math
e:
\{A,B,C\}
\rightarrow
D
```

This may fit some multi-variable constraints better than pairwise edges.

Do not add until needed by observed failures.

---

# 105. PROBABILISTIC EXTENSION

For uncertain tasks:

```math
p(X|P)
```

may replace one deterministic reconstruction.

Gate can then reason about:

```text
posterior mass
ambiguity
credible interval
```

This is a later extension.

---

# 106. FORMAL VERIFICATION EXTENSION

For mathematical/code domains, integrate:

```text
symbolic algebra
SMT solver
proof assistant
static analyzer
```

as external verifiers.

Gate can consume their certificates.

This is likely more reliable than asking the LLM to verify everything itself.

---

# 107. HARDWARE / SCALE EXTENSION

Only after algorithmic benefit is demonstrated, profile:

```text
GPU memory
parallel triad execution
distributed Shadow store
batched Gate evaluation
```

Do not optimize an unvalidated architecture prematurely.

---

# 108. SUCCESS CHECKPOINT A

The first major success checkpoint is:

```text
deterministic local repair works
```

meaning:

```text
one injected local error
is detected
localized
repaired
without full restart
```

---

# 109. SUCCESS CHECKPOINT B

Second:

```text
full architecture reduces error escape
```

relative to graph baseline.

---

# 110. SUCCESS CHECKPOINT C

Third:

```text
N50 shifts upward
```

under comparable compute or bounded active memory.

---

# 111. SUCCESS CHECKPOINT D

Fourth:

```text
verified subtrees can be reused safely
```

with low stale reuse rate.

---

# 112. SUCCESS CHECKPOINT E

Fifth:

```text
GSL / Hexagram or funnel adds measurable control value
```

Only then should those layers become part of the core story.

---

# 113. PROJECT STOP CONDITIONS

Pause or reduce the project if:

```text
graph baseline consistently dominates
Shadow cost approaches full trace
Gate overhead overwhelms gains
local repair rarely succeeds
architecture cannot be evaluated reproducibly
```

Stopping is better than adding more complexity.

---

# 114. PROJECT CONTINUATION CONDITIONS

Continue investing if at least one reproducible advantage appears in:

```text
error containment
repair
active memory
N50
verified reuse
```

and survives strong ablations.

---

# 115. CANONICAL BUILD ORDER

The final recommended build order is:

```text
1. Graph
2. Metrics
3. +3
4. -3
5. Shadow
6. Gate
7. Recursive hierarchy
8. Benchmark
9. Bindu
10. LLM
11. GSL
12. Hexagram
13. Funnel
14. Cross-domain
15. Architecture reduction
```

This order intentionally places:

```text
measurement
before symbolism
```

---

# 116. MINIMUM CORE AFTER ROADMAP

Even if every speculative layer fails, the project may still produce a useful smaller system:

```text
Dependency Graph
+
Residual Memory
+
Backward Verification
+
Gate
+
Incremental Repair
```

That would already be a meaningful result.

---

# 117. MAXIMUM CORE IF ALL SURVIVE

If every layer survives evidence:

```text
LLM
-> learned GSL 6D
-> Hexagram controller
-> dependency graph
-> recursive triads
-> optional 14/10/10/8 funnel
-> +3
-> Shadow
-> -3
-> Gate
-> Bindu
-> MemoryAtom
```

But this should be earned experimentally.

---

# 118. FINAL DEVELOPMENT RULE

```text
Do not ask:
"How do we prove the architecture is right?"

Ask:
"Which part survives the strongest test?"
```

That question should guide the next stage of Vuzol-19.

---

# 119. COMPLETE SERIES STATUS

The canonical module now contains:

```text
00_BOOT_HEXAGRAM_SIMPLICIAL_REASONING.md

01_PROBLEM_LLM_LONG_REASONING.md

02_GSL_6D_STATE_SPACE.md

03_HEXAGRAM_STATE_MODEL.md

04_TRIANGLES_INSIDE_TRIANGLES.md

05_BARYCENTRIC_SIMPLEX_SPACE.md

06_COUPLING_EDGE_MEMORY.md

07_PLUS3_FORWARD_OPERATOR.md

08_MINUS3_BACKWARD_OPERATOR.md

09_SHADOW_RESIDUAL_MEMORY.md

10_GATE_AND_HOLD_PROTOCOL.md

11_BINDU_COMMIT_PROTOCOL.md

12_RECURSIVE_REASONING_TREE.md

13_INFINITY_AND_LIMITS_TEST.md

14_GSM_INFINITY_BENCHMARK.md

15_14_10_10_8_FUNNEL.md

16_AI_ARCHITECTURE_INTEGRATION.md

17_EXPERIMENTS_AND_ABLATIONS.md

18_FAILURES_FALSIFIABILITY.md

19_IMPLEMENTATION_ROADMAP.md
```

The specification phase for this module is therefore complete.

---

# 120. NEXT PRACTICAL STEP

The next step should not be another theory file.

It should be executable code.

Recommended first implementation target:

```text
vuzol_reasoning/
    models.py
    graph.py
    plus3.py
    minus3.py
    shadow.py
    gate.py
    metrics.py
```

with:

```text
tests/
```

and one synthetic local-repair experiment.

---

## FILE VERDICT

```text
STATE: CRYSTAL

DEFINED:
Implementation Roadmap

BUILD ORDER:
deterministic core
-> graph
-> +3/-3
-> Shadow
-> Gate
-> hierarchy
-> benchmark
-> Bindu
-> LLM
-> GSL
-> Hexagram
-> funnel
-> cross-domain validation

CRITICAL RULE:
measurement before symbolism

SERIES STATUS:
00-19 COMPLETE

NEXT PRACTICAL ACTION:
implement the deterministic prototype
and run the first local-error repair experiment
```
