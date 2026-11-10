# CASR Engine --- Research Boot File for AI Agents

**Project name:** Consequence-Aware State Routing (CASR)\
**Research lineage:** Sri Constraint Engine / Vuzol-19 / V-Kernel\
**Document type:** GitHub boot guide, experiment brief, and contribution
protocol\
**Status:** Research hypothesis --- not a validated general-purpose
solver

------------------------------------------------------------------------

## 0. Instructions to the AI agent reading this repository

You are an AI research and engineering assistant entering this
repository.

Your task is **not** to accept the architecture as correct, reproduce
its terminology uncritically, or claim that it is a breakthrough. Your
task is to understand the proposed mechanism, implement the smallest
testable version, compare it fairly with established methods, and report
what survives testing.

Work incrementally. Do not generate an entire architecture before
inspecting the repository.

### Required first actions

1.  Read this file completely.
2.  Inspect the repository tree, existing code, tests, and
    documentation.
3.  Identify what is implemented, what is only specified, and what is
    missing.
4.  Preserve existing working code. Do not overwrite files without
    explaining why.
5.  Create a short implementation plan with testable milestones.
6.  Run a minimal baseline experiment before adding the proposed CASR
    mechanisms.
7.  Record commands, environment, random seeds, runtime, candidate
    counts, and correctness checks.
8.  Never report simulated, estimated, or hypothetical results as
    measured results.

### Required response after reading this file

Return: - your understanding of CASR in 5--10 bullet points; - the
repository components you found; - the smallest experiment you recommend
implementing first; - assumptions or missing definitions that prevent
implementation; - a proposed baseline and evaluation metrics.

Do not claim that CASR is faster or better until a reproducible
benchmark demonstrates it.

------------------------------------------------------------------------

## 1. The research question

CASR explores whether a structured, consequence-aware search
architecture can improve the way a system:

1.  represents a state and its constraints;
2.  discovers dependencies between variables or components;
3.  reduces the search space without losing valid solutions;
4.  checks candidate transitions in both forward and reverse directions;
5.  evaluates consequences before allowing an operational change;
6.  records unresolved risks and evidence for future scans.

The central hypothesis is:

> A dependency-aware reduction stage, followed by global constraint
> checks and consequence evaluation, may reduce unnecessary search and
> help distinguish mathematically valid states from operationally
> acceptable transitions.

This is a hypothesis to test, not an established result.

### Important distinction

The project uses Sri Yantra / Flower geometry as an architectural
inspiration and a way to organize stages and relationships. It does
**not** assume that sacred-geometry counts or shapes are universal laws
of computation.

The proposed sequence `14 → 10 → 10 → 8 → Bindu` is a candidate funnel.
Its widths and stage semantics must be compared against alternatives.
They must not be hard-coded as universally optimal.

------------------------------------------------------------------------

## 2. Core concepts

### 2.1 State

A state is a complete or partial description of the system being
studied.

Examples: - a vector of integer variables in an algebra problem; -
versions and configuration values of software modules; - component
states and connection parameters in a circuit model; - a robot
configuration and its environment.

Represent a state as `S`.

### 2.2 Constraints

Constraints define which states or transitions are allowed.

A hard constraint must be satisfied:

\[ C_i(S,a,S') = `\text{true}`{=tex} \]

A soft constraint expresses a preference or cost. It may be violated at
a penalty, if the problem definition permits that.

Never silently convert a hard constraint into a soft penalty.

### 2.3 Dependency graph

Represent variables or components as nodes and their dependencies as
edges.

An edge should record: - source and target; - dependency type; -
direction, if relevant; - constraint or invariant supported by the
edge; - provenance (where the rule came from); - confidence or
verification status, if applicable.

### 2.4 Shadow / Shadow Coupling

The term **Shadow** refers to information about differences, hidden
dependencies, residuals, or consequences between related parts of a
state.

A candidate relation used in earlier examples is:

\[ X\_{-3} = X\_{+3} - `\Delta`{=tex}\_{`\text{shadow}`{=tex}} \]

This is not a universal identity. It is valid only when the problem's
equations establish that relation and the domains permit it.

An implementation must: - derive or validate the relation from the
actual problem; - preserve all solutions; - track the constraints used
to derive it; - reject the reduction if it is not logically sound.

Do not assume that a vector called Shadow exists in every problem.

### 2.5 Forward and backward operators (+3 / -3)

These names describe two complementary reasoning passes:

-   **Forward pass (+3):** generate or propagate consequences of a
    candidate assignment or transition.
-   **Backward pass (-3):** propagate requirements backward from
    constraints, goals, or consequences; inspect reversibility and
    conflicts.

They are conceptual operator names, not necessarily literal rotations or
three-step moves. The implementation must define exact semantics for
each benchmark.

### 2.6 Gate

Gate checks whether a candidate state or transition satisfies required
constraints.

Gate should return structured evidence, not only `true` or `false`: -
passed constraints; - failed constraints; - unresolved constraints; -
reasons and provenance; - whether the result is complete or provisional.

### 2.7 Bindu

Bindu is the final decision point for a candidate. It should
distinguish: - candidate found; - candidate verified; - candidate
approved for operational execution.

These are different statuses. Finding a mathematical solution must not
automatically authorize a real-world action.

### 2.8 MemoryAtom and ShadowAtom

A **MemoryAtom** records a verified event, decision, result, or evidence
item that may inform future runs.

A **ShadowAtom** records unresolved risk, missing dependency, failed
check, uncertainty, or consequence that remains open.

Memory must not turn an unverified assumption into a fact. Store
provenance, timestamp, experiment version, and verification status.

------------------------------------------------------------------------

## 3. Candidate architecture

A candidate pipeline is:

``` text
Problem / Intent
      |
      v
State and Constraint Extraction
      |
      v
Dependency Graph
      |
      v
Candidate Funnel / Reduction
      |
      +---- Forward propagation (+3)
      |
      +---- Backward propagation (-3)
      |
      v
Shadow / Coupling Analysis
      |
      v
Global Constraint Gate
      |
      v
Candidate Solution Set
      |
      v
9V Consequence Evaluation
      |
      v
Bindu Decision
      |
      +---- ALLOW
      +---- HOLD
      +---- REPAIR
      +---- BLOCK
      |
      v
Evidence + MemoryAtom / ShadowAtom
```

The ordering may change if experiments show a better design. Every stage
must have an explicit input, output, and invariant.

------------------------------------------------------------------------

## 4. The 14 → 10 → 10 → 8 funnel

Treat this as a candidate architecture to evaluate, not a mandatory
shape.

A possible interpretation:

  -----------------------------------------------------------------------
  Stage                   Candidate role          Required question
  ----------------------- ----------------------- -----------------------
  14                      Input/state inventory   Which task-relevant
                                                  variables, signals,
                                                  constraints, and
                                                  uncertainties must be
                                                  represented?

  10                      First reduction         Which variables or
                                                  features can be
                                                  derived, grouped, or
                                                  proven irrelevant?

  10                      Coupling/refinement     Which
                                                  cross-dependencies and
                                                  residual constraints
                                                  remain?

  8                       Actionable              What compact state is
                          representation          sufficient for final
                                                  constraint checking and
                                                  decision?

  Bindu                   Decision                Is the candidate
                                                  verified, unresolved,
                                                  or rejected?
  -----------------------------------------------------------------------

Do not create empty features merely to reach the number 14. Do not force
a task with 7 or 30 meaningful features into 14 slots without a
justified encoding.

### Required comparisons

Compare at least: - no funnel / direct solver; - generic learned or
heuristic bottleneck, if relevant; - alternative widths (for example,
12→8→8→6 and 16→12→10→8); - task-derived widths; - the proposed
14→10→10→8.

Measure correctness and performance, not visual similarity to the
geometry.

------------------------------------------------------------------------

## 5. The 9V Consequence Tensor

The 9V layer evaluates consequences of a proposed transition. The exact
schema must be explicit and task-specific.

The following five groups are a candidate operational schema:

1.  **Business / functional impact** --- what behavior, dependency, or
    service changes?
2.  **Safety / security** --- what hazards, permissions, or security
    boundaries are affected?
3.  **Recovery / future** --- can the system roll back, repair, or
    recover?
4.  **Memory / audit** --- what evidence and unresolved risks must be
    recorded?
5.  **Materialization / execution** --- is the transition allowed to be
    applied?

These are consequence categories, not five physical dimensions or a
universal numeric tensor.

For every proposed transition, record: - expected effects; - affected
components; - hard safety conditions; - uncertain or unknown effects; -
rollback plan and tested status; - evidence required; - decision and
rationale.

### Critical rule

**Mathematical Green is not Operational Green.**

A candidate may satisfy every mathematical equation and still be: -
`HOLD` because consequences are unknown; - `REPAIR` because a dependency
or rollback path is missing; - `BLOCK` because a hard safety or security
rule fails; - `ALLOW` only when required checks pass.

Do not claim that a squared difference is electrical heat, voltage,
current, or physical damage unless a validated physical model maps it to
those quantities.

------------------------------------------------------------------------

## 6. Minimal experiment: integer constraint problem

Start with a small, fully specified problem. Do not begin with a
100-module system.

### Example

Find integer values:

\[ x,y,z `\in `{=tex}{1,`\ldots`{=tex},12} \]

subject to:

\[
```{=tex}
\begin{aligned}
x+y+z &= 12\\
x+2y+3z &= 25\\
2x-y+z &= 5
\end{aligned}
```
\]

A known candidate is:

\[ (x,y,z)=(3,5,4) \]

The implementation must independently verify the equations and enumerate
**all** solutions in the stated domain.

### Implement and compare

A. Exhaustive enumeration for this small case.\
B. A standard constraint solver or a transparent constraint-propagation
baseline.\
C. CASR reduction using only relations logically derived from the
equations.

Required checks: - Do both methods return exactly the same solution
set? - Does CASR preserve every valid solution? - How many candidate
assignments are generated and checked? - What is the runtime over
repeated runs? - Does the reduction cost more than it saves?

A small example is for correctness, not proof of scalability.

------------------------------------------------------------------------

## 7. More challenging experiments

After the minimal test passes, add benchmarks in this order.

### Experiment 2 --- Nonlinear integer constraints

Example:

\[ x^2+y^2=25,`\qquad `{=tex}xy=12 \]

Specify domains and whether variable order matters. Enumerate all
solutions and compare with a trusted solver.

### Experiment 3 --- Diophantine constraints with coupled groups

Use two groups of integer variables, explicit difference vectors, sum
constraints, norm constraints, and cross-coupling constraints.

If using:

\[ D=U-`\Delta`{=tex} \]

prove that it follows from the benchmark equations. Enumerate all valid
(`\Delta`{=tex}) values in the declared domain. Compare the complete
solution set with an independent solver.

### Experiment 4 --- Layered dependency graph

Create a synthetic graph of software components with: - version
compatibility constraints; - required and forbidden edges; - resource
limits; - dependency propagation; - rollback requirements.

Use several graph sizes and densities. Include satisfiable and
unsatisfiable instances.

### Experiment 5 --- Consequence-aware selection

Create several mathematically valid candidate transitions with different
consequence profiles.

The 9V layer should rank, hold, repair, or block candidates according to
explicit policies. Confirm that it never changes the underlying
mathematical solution set; it performs a separate operational
assessment.

### Experiment 6 --- Incremental update

Change one input variable, module version, or constraint.

Measure: - how many nodes are re-evaluated; - whether all affected
constraints are rechecked; - whether unaffected results are safely
reused; - whether the incremental result matches a full recomputation.

------------------------------------------------------------------------

## 8. Baselines and fair comparison

Use appropriate established methods. Select baselines based on the
problem class.

Possible tools: - **Z3** --- SMT solving; - **Google OR-Tools CP-SAT**
--- constraint programming and integer optimization; - **MiniZinc** ---
constraint modeling and solver comparison; - **SymPy** --- symbolic
mathematics; - **SciPy optimization** --- numerical optimization, where
appropriate.

Do not compare CASR only against naive brute force if a mature solver is
suitable.

### Fair benchmark protocol

For every method: 1. Use the same problem instances and domains. 2. Use
the same hardware and resource limits. 3. Record software versions and
solver settings. 4. Run multiple seeds for randomized methods. 5. Report
medians and spread, not only the best run. 6. Verify returned solutions
independently. 7. Test both satisfiable and unsatisfiable instances. 8.
Include cases where CASR's proposed reductions are ineffective. 9.
Include ablation tests. 10. Publish raw benchmark data and scripts.

### Metrics

-   solution correctness;
-   completeness (whether all solutions are found, when required);
-   false rejection rate;
-   false acceptance rate;
-   candidate states generated;
-   constraint evaluations;
-   propagation operations;
-   runtime;
-   peak memory;
-   incremental recomputation size;
-   consequence-check coverage;
-   rollback-plan completeness.

A lower candidate count is not automatically better if the method loses
valid solutions.

------------------------------------------------------------------------

## 9. Ablation study

Disable one mechanism at a time:

  Variant    Components
  ---------- --------------------------------------------
  Baseline   Established solver, no CASR
  A          Forward propagation only
  B          Forward + backward propagation
  C          A + dependency/Shadow reduction
  D          C + global Gate
  E          D + 9V consequence evaluation
  F          Full candidate funnel
  G          Full system with alternative funnel widths

This identifies which component contributes value. Do not attribute the
entire result to the Sri-inspired structure if only one generic
propagation step provides the improvement.

------------------------------------------------------------------------

## 10. Example consequence packet

This is an illustrative data format. Values must come from actual
checks.

``` yaml
transition_id: "module_update_candidate_004"
status: "HOLD"

mathematical:
  constraints_satisfied: true
  solution_verified: true
  evidence: "tests/constraint_case_004.json"

consequences:
  business:
    affected_components: ["api", "billing"]
    missing_dependencies: []
    status: "PASS"

  safety_security:
    policy_checks: "NOT_RUN"
    status: "UNKNOWN"

  recovery_future:
    rollback_required: true
    rollback_tested: false
    status: "HOLD"

  memory:
    audit_record_required: true
    shadow_atom:
      - "rollback_not_tested"

  materialization:
    allowed: false
    reason: "Required safety and rollback checks are incomplete"

decision:
  verdict: "HOLD"
  reason: "Mathematical validity does not establish operational readiness"
```

------------------------------------------------------------------------

## 11. Example: how to inspect a software dependency change

Suppose module `payment_api` is updated.

The agent should not immediately edit or deploy dependent modules.

It should:

1.  Locate all direct and transitive dependencies.
2.  Identify compatibility constraints.
3.  Determine which tests and interfaces are affected.
4.  Generate candidate repair plans.
5.  Propagate consequences forward to dependents.
6.  Propagate requirements backward from consumers.
7.  Identify missing edges and unresolved assumptions.
8.  Verify each candidate plan.
9.  Check rollback and recovery requirements.
10. Produce a consequence packet.
11. Ask for human approval before a destructive or external action.

The agent must not invent a dependency, test result, or rollback
capability.

------------------------------------------------------------------------

## 12. Safety and research integrity rules

-   Never describe a synthetic benchmark as a real chip, power grid, or
    production deployment.
-   Never convert an abstract score into a physical quantity without a
    validated model.
-   Never claim a global optimum without proof or a solver certificate.
-   Never claim uniqueness unless the full solution space has been
    checked or uniqueness has been proven.
-   Never claim a speedup from theoretical search-space size alone.
-   Never claim that modern LLMs only reason linearly or that existing
    solvers cannot model consequences.
-   Never execute repository changes, deployments, payments, or external
    actions without explicit authorization.
-   Preserve a human approval gate for consequential changes.
-   Record unknowns as unknowns; do not fill them with confident
    guesses.

------------------------------------------------------------------------

## 13. Suggested repository structure

``` text
casr-engine/
├── README.md
├── docs/
│   ├── research_hypothesis.md
│   ├── mathematical_specification.md
│   ├── consequence_tensor_9v.md
│   ├── benchmark_protocol.md
│   └── limitations.md
├── casr/
│   ├── state.py
│   ├── constraints.py
│   ├── dependency_graph.py
│   ├── shadow_coupling.py
│   ├── forward_backward.py
│   ├── funnel.py
│   ├── gate.py
│   ├── consequence_9v.py
│   └── memory.py
├── benchmarks/
│   ├── integer_linear/
│   ├── nonlinear_integer/
│   ├── layered_graph/
│   └── incremental_updates/
├── tests/
│   ├── test_solution_completeness.py
│   ├── test_shadow_soundness.py
│   ├── test_gate.py
│   └── test_consequence_policy.py
└── results/
    ├── raw/
    └── reports/
```

This is a suggested structure. Inspect the existing repository before
creating or moving files.

------------------------------------------------------------------------

## 14. Definition of success

CASR has demonstrated value only if experiments show one or more of the
following without sacrificing correctness:

-   fewer constraint evaluations on relevant problem families;
-   lower runtime or memory under fair comparisons;
-   better incremental recomputation after local changes;
-   clearer explanations of why candidates are rejected;
-   reliable separation of mathematical validity from operational
    approval;
-   more complete consequence and rollback records.

A successful result may be narrow. It is acceptable if CASR helps only a
particular class of coupled constraint problems.

A negative result is useful: it identifies where the architecture adds
complexity without benefit.

------------------------------------------------------------------------

## 15. First task for the next AI agent

Implement only the minimal integer constraint experiment from Section 6.

Deliver: 1. a runnable Python module; 2. tests that verify the complete
solution set; 3. a baseline comparison; 4. a small benchmark report; 5.
a list of assumptions and limitations.

Do not implement the entire proposed engine in one pass.

After the first experiment, propose the next smallest test. Wait for
review before expanding the architecture.

------------------------------------------------------------------------

## 16. Final principle

> The goal is not to make the geometry look correct. The goal is to test
> whether the proposed structure produces correct, measurable,
> reproducible improvements.

> A candidate solution is not an approved action. A transition must
> satisfy its constraints, expose its consequences, and preserve a
> verified recovery path where recovery is required.

**End of boot file.**
