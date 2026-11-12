# 07 — Gemini Code, Principles & Worked Examples Boot

## Purpose

This file is the reading and execution guide for the accompanying
`07_sri_cube_gf2_reference_audit.py`.

It gives a new AI agent a disciplined way to continue the Sri-Cube / Flower
Gate / CASR work without confusing:

1. historical code and claims attributed to Gemini;
2. independent calculations and audits made in ChatGPT;
3. reconstructed reference code;
4. mathematical facts;
5. hypotheses about physical implementation.

## Provenance: what was recovered from the discussion

### Code associated with Gemini

The historical script name discussed was:

`00_FLOWER_GATE_CORE/sri_18d_9v_gf2_boot.py`

Its described modules included:

- `PlateSpec` and `PlateSolution`;
- integer sphere-vector generation;
- single-plate search using norm, perimeter, cross-resonance and determinant
  constraints;
- GF(2) matrix-rank calculation;
- XOR syndrome checks;
- a binary hardware audit;
- a Gray-code cycle test;
- 9V checks using forward shear, rollback shear, peak drop and CMOS bit-flip
  thresholds.

The full original source is not reproduced here. The companion `.py` file is
an independently written reference implementation of the recovered
calculations, not a verbatim copy of Gemini's program.

### Historical input values

```python
U9 = (14, 10, 12)
D9 = (12, 9, 10)

U6 = (11, 7, 13)
D6 = (10, 5, 11)

U3 = (7, 11, 5)
D3 = (5, 9, 4)
```

Reported derived values in the earlier discussion:

| Plate | delta = U-D | perimeter | ||U||² | ||D||² | cross value | determinant difference |
|---|---:|---:|---:|---:|---:|---:|
| 9 | (2,1,2) | 67 | 440 | 325 | 370 | 600 |
| 6 | (1,2,2) | 57 | 339 | 246 | 262 | 451 |
| 3 | (2,2,1) | 41 | 195 | 122 | 132 | 205 |

These values are preserved as historical reported values. The exact original
definitions of every derived metric must be checked against the original
script before treating the table as a verified independent reproduction.

## Principles to preserve

### 1. U, D and Shadow are separate roles

- `U` is the forward/candidate direction (+3).
- `D` is the reverse/audit direction (-3).
- `Shadow` records residuals, differences, missing constraints or unresolved
  consequences.

Do not silently merge these into one vector. Keep the raw inputs and derived
values separately auditable.

### 2. GF(2) means arithmetic modulo two

For bit vectors, addition is XOR:

```python
0 ^ 0 == 0
0 ^ 1 == 1
1 ^ 0 == 1
1 ^ 1 == 0
```

The rank is computed over the field GF(2), not over ordinary real numbers.
An integer such as `6` is interpreted as the four-bit row `0110`.

### 3. Syndrome construction

For the three aligned columns:

```python
S_m = U9[m] ^ U6[m] ^ U3[m]
```

The three syndrome values are then rows of a GF(2) matrix. Their rank measures
linear independence of these three bit rows.

A critical invariant follows:

```python
S0 ^ S1 ^ S2 == xor_all(U9 + U6 + U3)
```

If the XOR of all nine plate entries is zero, then the XOR of the three
syndromes is zero for every permutation of values within each plate.
Consequently, the three syndrome rows are linearly dependent and their rank
cannot be 3.

For the base U inputs:

- XOR(U9) = 8
- XOR(U6) = 1
- XOR(U3) = 9
- 8 XOR 1 XOR 9 = 0

Therefore closed parity is invariant under the alignments considered here.
This is a mathematical property of these inputs, not evidence of a physical
conservation law.

### 4. Keep two rank calculations distinct

There are two different quantities:

- `syndrome_rank`: rank of the three cross-plate XOR syndrome rows;
- `pillar_rank`: a separate historical metric whose exact matrix layout
  must be recovered from the original source before it can be reproduced.

Do not call both simply “rank”. The historical notes reported B as
`pillar_ranks = (3,3,3)` and `syndrome_rank = 2`, but the first tuple remains
unverified here because its matrix construction is missing.

### 5. Gray code is a digital transition check

The cycle

`00 → 10 → 11 → 01 → 00`

changes exactly one bit per step. This verifies a property of a two-bit
digital encoding. It does not by itself establish a photonic, atomic or
biological mechanism.

### 6. 9V is a proposed consequence/audit layer

The earlier code description used thresholds such as:

- `forward_shear <= 20`
- `rollback_shear <= 22`
- `peak_drop <= 4`
- `cmos_bit_flips > 6`

These are model parameters, not universal physical constants. Each threshold
must have a documented definition, unit, rationale, sensitivity analysis and
test. If a metric has no validated meaning, mark it experimental rather than
using it as a safety guarantee.

## Worked examples

### Candidate A, B and C

The discussion used these forward plate alignments:

```python
A = (
    (14, 10, 12),
    (7, 13, 11),
    (11, 5, 7),
)

B = (
    (14, 10, 12),
    (11, 7, 13),
    (7, 11, 5),
)

C = (
    (14, 10, 12),
    (13, 11, 7),
    (5, 7, 11),
)
```

Previously audited results:

| Candidate | Column sums | Syndromes | Syndrome rank |
|---|---|---|---:|
| A | (32,28,30) | (2,2,0) | 1 |
| B | (32,28,30) | (2,6,4) | 2 |
| C | (32,28,30) | (6,6,0) | 1 |

Interpretation: B has three nonzero, pairwise distinct syndrome values, but
they are linearly dependent because `2 XOR 6 XOR 4 = 0`. Its syndrome rank
is therefore 2, not 3.

### Nine cyclic alignments

The independent audit reported these nine outcomes:

| rot U6 | rot U3 | sums | syndromes | syndrome rank |
|---:|---:|---|---|---:|
| 0 | 0 | (32,28,30) | (2,6,4) | 2 |
| 0 | 1 | (36,22,32) | (14,8,6) | 2 |
| 0 | 2 | (30,24,36) | (0,10,10) | 1 |
| 1 | 0 | (28,34,28) | (14,12,2) | 2 |
| 1 | 1 | (32,28,30) | (2,2,0) | 1 |
| 1 | 2 | (26,30,34) | (12,0,12) | 1 |
| 2 | 0 | (34,32,24) | (4,10,14) | 2 |
| 2 | 1 | (38,26,26) | (8,4,12) | 2 |
| 2 | 2 | (32,28,30) | (6,6,0) | 1 |

The earlier audit also reported separate per-plate rank tuples and counts
for the 36 independent permutations. However, the precise matrix
construction used for those "pillar ranks" is not preserved in the recovered
material. The reference script therefore does NOT invent a definition for
that metric or claim to reproduce those counts. Recover the original
`gf2_matrix_rank` call sites and matrix orientation before validating
pillar-rank claims.

### 36 independent permutations

With U9 fixed and all 3! permutations of U6 crossed with all 3! permutations
of U3:

- total alignments: 36;
- arithmetic column-sum target `(32,28,30)`: 6 alignments.

Earlier notes reported additional pillar-rank counts (8 full-rank cases,
2 also meeting the sum target), but the precise pillar matrix definition
could not be recovered. Treat those as unverified historical results until
the original source or exact matrix construction is available.

This is a finite enumeration of 36 cases, not a search of the full
`20^18` state space.

## Monte Carlo warning

An earlier comparison was not a fair baseline:

- the structured sample was conditioned on closed parity and checked three
  synchronous gear configurations;
- the random baseline allowed duplicate values and checked only one fixed
  configuration.

These samples do not have the same admissible state space or search budget.
Do not conclude that the Sri construction outperforms random search from
that comparison.

A fair experiment must match:

1. value domain;
2. duplicate policy;
3. parity/admissibility constraints;
4. number of alignments checked;
5. computational budget;
6. scoring and stopping rules.

Report both:
- unrestricted random baseline;
- matched random baseline sampled from the same admissible set.

Use fixed seeds and publish all trial counts and denominators.

## Instructions to the next AI agent

1. Read this file and the companion Python script before modifying the model.
2. Run the reference script and preserve its output.
3. Find the original `sri_18d_9v_gf2_boot.py` in the repository, if present.
4. Compare every function and formula against the reference implementation.
5. Label each result as `REPRODUCED`, `NOT_REPRODUCED`, `UNTESTED` or
   `HYPOTHESIS`.
6. Do not alter historical inputs to make a result pass.
7. Do not claim exhaustive search over `20^18` unless the implementation
   truly visits that state space.
8. Do not translate the geometry into claims about protons, neutrons,
   electrons, atoms or photonic hardware without an explicit physical model
   and independently measurable predictions.
9. Preserve the human Gate: AI may propose; verified tests decide; human
   approval is required before consequential external actions.

## Core operating rule

**AI may propose transitions. Shadow must expose unresolved consequences.
Gate must verify admissibility. Bindu may commit only verified states.
Memory must preserve the evidence.**
