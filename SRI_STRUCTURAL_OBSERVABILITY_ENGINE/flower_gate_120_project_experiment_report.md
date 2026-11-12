# Flower Gate / CASR — corrected benchmark and GF(2) audit

**Reproducibility:** fixed synthetic seed `20261112` for the 120-project benchmark; exhaustive 216-permutation audit for the stated U9/U6/U3 triples.

## 1. Corrected A/B/C syndrome assignments

For `U9=(14,10,12)`:

| Candidate | U6 | U3 | Syndrome | Syndrome rank |
|---|---|---|---|---:|
| A | (7,13,11) | (11,5,7) | (2,2,0) | 1 |
| B | (11,7,13) | (7,11,5) | (2,6,4) | 2 |
| C | (13,11,7) | (5,7,11) | (6,6,0) | 1 |

The earlier assignment of `(2,2,0)` to the base B alignment was incorrect. It belongs to candidate A.

## 2. Pillar matrix definition

For each position \(m=1,2,3\), let `bin4(x)` be the four-bit representation of x. Define:

\[
M_P^{(m)} =
\begin{bmatrix}
bin4(U_{9,m})\\
bin4(U_{6,m})\\
bin4(U_{3,m})
\end{bmatrix}
\in GF(2)^{3\times4}
\]

This gives pillar ranks:
- A: `(3,3,2)`
- B: `(3,3,3)`
- C: `(3,3,2)`

These are distinct from the rank of the syndrome matrix.

## 3. EXP-002 — 216 independent permutations

Exhaustive enumeration over all `3! × 3! × 3! = 216` permutations of the three fixed triples produced:

- configurations checked: **216**;
- closed-parity failures: **0**;
- states with syndrome `(0,0,0)` and arithmetic sum `(30,30,30)`: **6**;
- pillar ranks of each of these six states: `(2,2,2)`.

The six states:

| U9 | U6 | U3 |
|---|---|---|
| (14,10,12) | (11,13,7) | (5,7,11) |
| (14,12,10) | (11,7,13) | (5,11,7) |
| (10,14,12) | (13,11,7) | (7,5,11) |
| (10,12,14) | (13,7,11) | (7,11,5) |
| (12,14,10) | (7,11,13) | (11,5,7) |
| (12,10,14) | (7,13,11) | (11,7,5) |

This is exhaustive for the stated fixed triples and permutation operation only. “Mirror state” is a label for these six alignments, not a demonstrated physical symmetry.

## 4. EXP-007 — 120-project CASR benchmark

### Model
- 120 synthetic projects;
- three resources: labor, budget, energy;
- 28 prerequisite links;
- 28 mutually exclusive pairs;
- risk budget;
- per-project resource uncertainty uplift of 3–22%, included in conservative resource coefficients;
- objective: maximize `sum(value_i - 1.8 * risk_i)`.

The same fixed seed, instance and constraints were used for all methods.

### Results

| Method | Selected | Objective | Value | Risk |
|---|---:|---:|---:|---:|
| Greedy | 44 | 3191.91 | 3487 | 163.94 |
| Earlier Flower local repair | 46 | 3322.36 | 3618 | 164.25 |
| CASR Shadow | 46 | **3421.08** | 3712 | 161.62 |
| Exact MILP optimum (HiGHS) | 47 | 3426.73 | 3721 | 163.48 |

CASR:
- improvement over greedy: **7.18%**;
- gap to exact MILP optimum: **0.1649%**;
- measured runtime in this run: **1.965 seconds**;
- labor utilization: **99.77%**;
- budget utilization: **99.63%**;
- energy utilization: **96.85%**;
- risk utilization: **98.38%**;
- final feasibility audit: passed;
- dependencies satisfied: yes;
- conflicts avoided: yes.

Accepted objective path:

`3276.67 → 3386.85 → 3410.35 → 3415.99 → 3418.46 → 3421.08`

The exact MILP solver reported optimal termination; relative MIP gap was approximately `2.27e-6`.

### Interpretation

On this one synthetic instance, the supplied CASR heuristic improved the greedy baseline and came within 0.1649% of the exact MILP objective. It did not beat the exact optimizer. This is promising evidence for the heuristic's usefulness on this instance, not proof of general superiority or a new complexity result.

The CASR function is now integrated into `flower_gate_120_project_experiment.py`. The script performs an independent final feasibility audit after the CASR solver returns.

## 5. Required next validation

Run 30–100 independent seeds and report mean/median/worst-case:
- objective improvement over greedy;
- gap to MILP optimum;
- feasibility rate;
- runtime;
- number of proposed, rejected and accepted transitions.

Also compare against CP-SAT on the same generated instances. The current exact baseline is SciPy/HiGHS MILP, not CP-SAT.
