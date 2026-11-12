# 05 — EXPERIMENTS AND BASELINES
## Reproducible test plan, matched controls, Monte Carlo protocol, and evaluation criteria

**File:** `05_EXPERIMENTS_AND_BASELINES.md`  
**Role:** Define how claims in this repository are tested and compared  
**Status:** Experimental protocol; results must be added only after execution

---

## 1. Purpose

This document defines the evidence protocol for evaluating the SRI Structural Observability Engine.

The experiments must answer:

1. Can the supplied arithmetic and structural claims be reproduced?
2. Do the search and audit components behave as specified?
3. Does the proposed method find valid candidates more reliably or efficiently than suitable alternatives?
4. Do the GF(2) checks expose meaningful dependencies in the encoded data?
5. Does the 9V consequence audit improve decisions once it is formally defined?
6. Are the results robust to input changes, thresholds, and random seeds?

This file is a protocol, not a report of completed experiments. Do not fill it with invented results.

## 2. Evidence labels

Use the following labels in all reports:

| Label | Meaning |
|---|---|
| `VERIFIED` | Exact arithmetic, formal derivation, or executable test reproduced. |
| `OBSERVED` | Result obtained from a run but not independently established. |
| `HYPOTHESIS` | Proposed explanation or expected benefit awaiting a test. |
| `ASSUMPTION` | Condition imposed by the experiment or model. |
| `OPEN` | Not yet tested, not fully defined, or unresolved. |

Each result must identify its scope. A result verified for one fixed fixture does not automatically generalize to other inputs.

## 3. Experiment registry

Each experiment must have a stable identifier and a record containing:

```text
experiment_id
title
hypothesis
status
date
code_version
environment
input_dataset_or_fixture
constraints
parameters
random_seed
baseline
metrics
command
raw_output_location
analysis_location
limitations
```

Recommended initial identifiers:

| ID | Experiment | Main question |
|---|---|---|
| `EXP-001` | Fixed arithmetic reproduction | Are the supplied plate and syndrome values reproduced? |
| `EXP-002` | Permutation invariant | Does closed parity hold across all 216 independent permutations? |
| `EXP-003` | GF(2) rank audit | Are syndrome and pillar matrix ranks calculated correctly and separately? |
| `EXP-004` | Rotation and permutation enumeration | Are the searched configuration counts and candidate sets correct? |
| `EXP-005` | Matched random control | Does any observed structural advantage survive a fair control? |
| `EXP-006` | Monte Carlo stability | Are results stable across seeds and sample sizes? |
| `EXP-007` | CASR versus solver baselines | Does CASR improve a relevant search metric? |
| `EXP-008` | Gate and Shadow ablation | Do audit stages improve decisions over simpler variants? |
| `EXP-009` | 9V evaluation | Does a formally defined consequence audit improve downstream outcomes? |

## 4. EXP-001 — Fixed arithmetic reproduction

### Objective

Reproduce the supplied forward plate values and derived arithmetic.

### Input fixture

```python
U9 = (14, 10, 12)
U6 = (11, 7, 13)
U3 = (7, 11, 5)

D9 = (12, 9, 10)
D6 = (10, 5, 11)
D3 = (5, 9, 4)
```

### Required calculations

Component-wise forward sum:

\[
U_9+U_6+U_3=(32,28,30)
\]

Forward syndrome:

\[
S_i=U_{9,i}\oplus U_{6,i}\oplus U_{3,i}
\]

Expected:

```text
S = (2, 2, 0)
```

Row XOR:

```text
14 XOR 10 XOR 12 = 8
11 XOR  7 XOR 13 = 1
 7 XOR 11 XOR  5 = 9
```

Expected total parity:

```text
8 XOR 1 XOR 9 = 0
```

### Acceptance criteria

- Exact integer values match.
- The implementation and an independent calculation agree.
- Tests fail if any input or expected value is changed incorrectly.

This experiment verifies arithmetic for the fixture only.

## 5. EXP-002 — Exhaustive permutation invariant

### Objective

Verify that closed parity is invariant under independent permutations of the three fixed triples.

Each triple has six permutations:

\[
3!=6
\]

The number of independent combinations is:

\[
6^3=216
\]

### Procedure

1. Generate all permutations of `U9`.
2. Generate all permutations of `U6`.
3. Generate all permutations of `U3`.
4. Evaluate the syndrome for every triple of permutations.
5. Calculate the XOR of the three syndrome components.
6. Count failures.

### Acceptance criteria

```text
configurations_checked = 216
closed_parity_failures = 0
```

This is an exhaustive finite check for these three fixed triples. It is not an exhaustive search of the full 18-dimensional state space.

## 6. EXP-003 — GF(2) rank audit

### Objective

Check that the exact binary matrix and its rank are reported correctly.

### Required matrices

The syndrome vector for the fixture is:

```text
(2, 2, 0)
```

Using four-bit rows:

```text
0010
0010
0000
```

The syndrome matrix therefore has rank 1 over GF(2).

The experiment must also define and test any separate pillar matrix. Do not infer its rank from the syndrome matrix.

### Acceptance criteria

- Matrix dimensions are reported.
- Bit width is reported.
- Matrix rows are preserved in the result.
- Rank is computed by GF(2) elimination.
- A separate independent matrix has a known test rank.
- No report conflates syndrome rank with pillar rank.

## 7. EXP-004 — Rotation and permutation enumeration

### Objective

Ensure that configuration counts and search modes are correctly named.

For a three-element tuple:

- all permutations: 6;
- cyclic rotations: 3.

For two independently permuted triples with one fixed:

\[
6^2=36
\]

For three independently permuted triples:

\[
6^3=216
\]

For three independently rotated triples:

\[
3^3=27
\]

For three synchronous rotations:

\[
3
\]

### Required reporting

For each run, state:

- transformation type;
- whether transformations are independent or synchronous;
- number of possible configurations;
- number actually evaluated;
- any pruning or early stopping.

A run over three synchronous rotations must never be described as a complete search over 27 independent rotations or 216 permutations.

## 8. EXP-005 — Matched random control

### Objective

Test whether a proposed Sri-structured search has an advantage over random selection when both methods receive the same admissibility rules and search opportunities.

### Why this matters

A comparison is biased if the structured method is conditioned on a parity rule while the random baseline is not, or if one method searches multiple configurations while the other checks only one.

A baseline must not be made artificially weaker.

### Matched-control requirements

The structured and random methods must use the same:

1. admissible input domain;
2. per-plate value range;
3. duplicate policy;
4. parity preconditions;
5. constraints;
6. candidate configuration set;
7. stopping rule;
8. number of candidate evaluations;
9. success definition.

If a Sri candidate is accepted only after closed parity is satisfied, random candidates in the matched comparison must be drawn from the same parity-conditioned admissible set.

An unrestricted random sample may be reported separately as an additional reference, not as the matched control.

### Separate control arms

Use at least these arms when relevant:

| Arm | Sampling rule | Purpose |
|---|---|---|
| `A_STRUCTURED` | Candidate generation using the proposed structure | Evaluate the proposed method. |
| `B_RANDOM_MATCHED` | Random candidates from the same admissible set and same evaluation budget | Fair comparison. |
| `C_RANDOM_UNRESTRICTED` | Random candidates from the broader domain | Context only; not the primary matched control. |

### Metrics

Report:

- candidates generated;
- candidates evaluated;
- admissible candidates;
- candidates passing each gate;
- success rate with numerator and denominator;
- runtime;
- memory use, if relevant;
- objective or quality distribution;
- diversity of accepted candidates;
- seed-to-seed variability.

### Interpretation

If `A_STRUCTURED` outperforms `B_RANDOM_MATCHED`, that is evidence of an advantage under the tested setup. It is not yet proof of general superiority.

If it does not outperform the matched control, report that result without changing the success definition after seeing the data.

## 9. EXP-006 — Monte Carlo stability

### Objective

Estimate how results vary across repeated random samples and seeds.

### Procedure

1. Define the population from which samples are drawn.
2. Define whether sampling is with or without replacement.
3. Define all constraints and conditioning.
4. Run multiple independent seeds.
5. Use the same sample budget for compared methods.
6. Record raw counts for every run.
7. Aggregate only after preserving per-run results.

### Minimum report

```text
seed
attempts
accepted_population
success_count
failure_count
success_rate
mean_runtime
runtime_stddev
```

Report confidence intervals where appropriate. For proportions, use a suitable binomial interval rather than relying only on a normal approximation when counts are small.

Do not pool conditioned and unconditioned populations into one percentage.

### Reproducibility

Record:

- pseudorandom generator;
- software version;
- seed;
- sampling algorithm;
- environment;
- exact command.

A seed alone is not sufficient if the random generator or sampling procedure changes.

## 10. EXP-007 — CASR versus solver baselines

### Objective

Determine whether CASR offers a measurable benefit for a defined class of constrained search problems.

### Candidate baselines

Select relevant tools according to the problem:

- exhaustive enumeration on small instances;
- random search;
- constraint programming / CP-SAT;
- SMT solving with Z3;
- MiniZinc;
- an established domain-specific heuristic.

Do not include a baseline merely for name recognition. Explain why it is suitable.

### Benchmark design

Use a suite of problem instances with varied:

- dimension;
- constraint density;
- number of feasible states;
- objective conflict;
- noise or uncertainty, if applicable.

All methods must receive equivalent problem definitions and comparable computational budgets.

### Metrics

- feasibility rate;
- objective quality;
- time to first feasible solution;
- time to best solution;
- total runtime;
- candidate evaluations;
- memory use;
- optimality gap, when known;
- completeness status.

If the true optimum is unknown, do not claim an optimality gap without a valid bound.

## 11. EXP-008 — Gate and Shadow ablation

### Objective

Test whether the architecture's audit stages add measurable value.

Compare variants such as:

| Variant | Components |
|---|---|
| `V0_BASE` | Candidate generation and hard constraints only. |
| `V1_REVERSE` | V0 plus reverse audit. |
| `V2_SHADOW` | V1 plus structured Shadow tracking. |
| `V3_GATE` | V2 plus explicit Gate verdicts. |
| `V4_CONSEQUENCE` | V3 plus 9V, only after 9V is formally defined. |

### Evaluation

Use the same candidate stream for all variants where possible.

Measure:

- false acceptance;
- false rejection;
- unresolved issues detected;
- downstream failures;
- time and computational overhead;
- human review burden.

Define ground truth or an independent evaluation procedure before interpreting false-accept and false-reject rates.

Do not conclude that a component is useful merely because it produces more warnings.

## 12. EXP-009 — 9V evaluation

### Prerequisite

Do not run a meaningful 9V performance experiment until the nine components, equations, domains, dependencies, and uncertainty rules are formally defined.

### Proposed evaluation

Once defined:

1. construct cases with known or independently assessed downstream outcomes;
2. run the system with and without 9V;
3. preserve identical candidate inputs;
4. compare decision quality and missed consequences;
5. measure added latency and review burden;
6. test sensitivity to thresholds and uncertainty;
7. report failures and unavailable components.

### Required metrics

Possible metrics include:

- consequence detection rate;
- false alarm rate;
- missed consequence rate;
- calibration of uncertainty estimates, if probabilistic;
- decision quality against an external reference;
- additional computational cost.

Choose metrics that match the defined 9V output. Do not force metrics that do not fit its mathematical type.

## 13. Threshold sensitivity

Any threshold used by CASR, Gate, or 9V must be tested across a reasonable range.

For a threshold \(\tau\), evaluate nearby values:

\[
\tau-\Delta,\quad\tau,\quad\tau+\Delta
\]

where \(\Delta\) is stated and justified.

Report how verdicts, acceptance rates, and error rates change.

A threshold that produces a desired outcome only at one narrow value is fragile and must be identified as such.

## 14. Negative and adversarial tests

The test suite must include cases designed to break the assumptions.

Examples:

- invalid tuple length;
- values outside the declared domain;
- duplicated values when duplicates are forbidden;
- parity violation;
- a candidate with a high score but a hard-constraint failure;
- missing reverse-audit result;
- missing 9V components;
- inconsistent evidence references;
- malformed matrix;
- a random baseline with a different candidate budget;
- a candidate generator that repeats the same state;
- early stopping incorrectly labeled exhaustive.

The system should fail safely and explain the failure.

## 15. Result reporting template

Use this structure for every experiment report:

```text
# EXPERIMENT REPORT

## 1. Experiment ID and title
## 2. Hypothesis
## 3. Status: VERIFIED / OBSERVED / HYPOTHESIS / OPEN
## 4. Code version and environment
## 5. Input data and generation procedure
## 6. Constraints and assumptions
## 7. Parameters and random seeds
## 8. Method
## 9. Baseline and fairness conditions
## 10. Raw results
## 11. Metrics and calculations
## 12. Independent reproduction
## 13. Limitations
## 14. Shadow ledger
## 15. Conclusion
## 16. Next experiment
```

Include raw counts, denominators, and the exact command used.

## 16. Reproducibility commands

The eventual implementation should provide stable commands such as:

```bash
python -m pytest
python experiments/v1_reproduction.py
python experiments/v2_observability.py
python experiments/monte_carlo_control.py --seed 42
```

These are proposed command patterns. Adjust them to the actual repository and do not document a command as working until it has been run successfully.

## 17. Decision criteria for claiming an advantage

A claim that CASR or the Sri structure provides an advantage requires:

1. a clearly defined problem class;
2. a reproducible implementation;
3. a fair matched baseline;
4. a predeclared success metric;
5. multiple test instances;
6. repeated runs where randomness is involved;
7. uncertainty or variability reporting;
8. an independent reproduction where feasible;
9. an honest account of failures and limitations.

A single successful example is evidence that the example works, not proof of general superiority.

## 18. Current status register

| Item | Status | Notes |
|---|---|---|
| Fixed fixture arithmetic | `VERIFIED` by direct calculation | See `02_MATHEMATICAL_MODEL.md`. |
| Closed parity for fixed triples | `VERIFIED` by algebraic identity | Independent permutations preserve each triple's XOR. |
| 216-permutation executable test | `OPEN` until the script is run | The mathematical expectation is zero parity failures. |
| Matched Monte Carlo comparison | `OPEN` | Must use equivalent sampling conditions and budgets. |
| CASR performance advantage | `HYPOTHESIS` | Requires benchmark suite and matched baselines. |
| Gate/Shadow ablation | `OPEN` | Requires defined outcomes and evaluation criteria. |
| 9V decision benefit | `HYPOTHESIS` | 9V model must first be formally defined. |
| Physical observability claim | `NOT ESTABLISHED` | Requires physical state and measurement model. |

## 19. Final rule

Do not tune the experiment after seeing the result and then report the tuned result as if it were predicted in advance.

Preserve the original hypothesis, all failed runs, all seeds, and all deviations from the protocol.

The goal is not to make the architecture appear successful. The goal is to discover exactly where it works, where it fails, and whether it offers a measurable benefit over fair alternatives.
