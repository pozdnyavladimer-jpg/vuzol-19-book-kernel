# Flower Gate — 120-project constrained planning experiment

**Status:** reproducible synthetic experiment  
**Seed:** `20261112`  
**Projects:** 120  
**Resources:** labor, budget, energy  
**Constraints:** 28 prerequisite links, 28 mutually exclusive pairs, one risk budget  
**Solver reference:** mixed-integer linear optimization with SciPy/HiGHS (not CP-SAT)

## 1. Question

Can a Flower-Gate-inspired workflow improve a feasible plan over a simple greedy heuristic, while remaining auditable and close to an exact optimization reference?

## 2. Synthetic instance

Each project has:
- a benefit value;
- a risk score;
- requirements for labor, budget and energy;
- possible prerequisite dependencies;
- possible conflict with another project.

Resource uncertainty is modeled with a conservative envelope: each project's resource requirement is increased by a generated uncertainty factor between 3% and 22%. The optimizer and heuristics all use the same conservative resource coefficients. The risk budget and resource capacities are fixed for the generated instance.

Objective:

`maximize sum(value_i - 1.8 * risk_i) * x_i`

subject to:
- all three resource limits;
- total risk limit;
- if a project is selected, its prerequisite must also be selected;
- mutually exclusive pairs cannot both be selected;
- each project is binary (selected / not selected).

This is synthetic data, not a public real-company dataset.

## 3. Compared methods

### Greedy
Ranks projects by utility divided by normalized resource burden and risk burden. It adds prerequisite bundles when feasible.

### Flower Gate prototype
Uses the same greedy plan as its starting point, then performs bounded local repair:
- propose adding a project together with its prerequisites;
- test removal of zero, one or two currently selected projects;
- reject any candidate that violates resource, risk, dependency or conflict constraints;
- accept the best feasible improvement;
- repeat until no positive improvement is found.

This maps to the Flower Gate workflow:
- State: current selected projects and resource loads;
- Pressure: capacity and risk limits;
- Shadow: inspect the current plan for inefficient combinations and hidden prerequisite/conflict effects;
- +3: generate candidate changes;
- -3: re-check constraints and consequences;
- 9V: summarize resource/risk consequences (the current prototype uses explicit numeric constraints, not a separately validated 9-dimensional consequence tensor);
- Gate: reject infeasible transitions;
- Bindu: accept the best verified candidate;
- Memory: retain inputs, seed, objective path and audit results.

### Exact reference
A mixed-integer linear model is solved with SciPy's HiGHS backend. It provides the optimum for this generated instance. It is not a CP-SAT run.

## 4. Results

| Method | Selected projects | Utility | Total value | Risk | Labor used | Budget used | Energy used |
|---|---:|---:|---:|---:|---:|---:|---:|
| Greedy | 44 | 3191.91 | 3487 | 163.94 | 88.9% | 99.8% | 75.3% |
| Flower Gate prototype | 46 | 3322.36 | 3618 | 164.25 | 99.4% | 99.8% | 92.7% |
| MILP optimum | 47 | 3426.73 | 3721 | 163.48 | 99.9% | 99.6% | 99.7% |

- Flower Gate improved the greedy objective by **4.09%**.
- Flower Gate remained **3.05% below** the exact MILP optimum.
- All three plans passed the same feasibility checks.
- Flower Gate's objective improved monotonically over its accepted sequence:
  `3191.91 → 3228.78 → 3277.45 → 3315.79 → 3322.36`.
- The MILP solver reported optimal termination with relative gap about `2.27e-6`.

## 5. What this demonstrates

The useful result is not that Flower Gate beat an exact optimizer—it did not. The useful result is that a simple, inspectable transition-and-audit loop improved a greedy plan by 4.09%, while preserving all modeled constraints and staying within 3.05% of the exact optimum.

The plan repair is explainable: each accepted change is a candidate transition, tested against the same resource, risk, prerequisite and conflict rules before acceptance.

## 6. What this does NOT demonstrate

- It does not prove that Flower Gate is a new optimization algorithm.
- It does not prove superiority over CP-SAT, OR-Tools, or commercial solvers.
- It does not establish real-world causal or predictive validity.
- The dataset is synthetic, and one seed is not enough to establish general performance.
- The current prototype's “Shadow” is a local-search opportunity detector; “9V” is represented by explicit constraints and consequence summaries, not a fully formalized independent tensor.
- The exact MILP result is the best known reference for this particular instance, not for all possible planning problems.

## 7. Next experiment required

Run at least 30–100 independent seeds and publish:
- mean and median objective improvement over greedy;
- mean and worst-case gap to MILP optimum;
- feasibility rate;
- runtime;
- number of candidate transitions proposed, rejected and accepted;
- ablations: no Shadow repair, no dependency closure, no risk penalty, no uncertainty envelope;
- comparison against CP-SAT on the same model and same data.

Only if the improvement persists across seeds and remains competitive in runtime should we claim practical advantage.

## 8. Reproduction

Run:

```bash
python flower_gate_120_project_experiment.py
```

Requires Python, NumPy and SciPy with `scipy.optimize.milp`.

The script uses a fixed seed and prints the generated instance summary, three method results, selected project IDs and feasibility audit.
