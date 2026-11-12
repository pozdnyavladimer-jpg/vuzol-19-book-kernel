# 04 — GF(2) OBSERVABILITY AND 9V
## Binary parity, matrix rank, syndrome analysis, and consequence-audit boundaries

**File:** `04_GF2_OBSERVABILITY_AND_9V.md`  
**Role:** Specify binary calculations and define what they can and cannot establish  
**Status:** GF(2) arithmetic is formalizable; physical observability and 9V remain separate claims requiring additional models and evidence

---

## 1. Purpose

This document defines the binary-algebra layer of the SRI Structural Observability Engine and the interface for the proposed 9V consequence audit.

It has five goals:

1. define the bitwise operations used by the implementation;
2. distinguish syndrome construction from other feature or pillar matrices;
3. define rank over GF(2);
4. preserve the closed-parity invariant in the current plate example;
5. prevent algebraic rank from being overstated as physical or experimental observability.

The GF(2) calculations are exact for their specified inputs. Their interpretation is limited to the mathematical objects actually calculated.

## 2. GF(2) arithmetic

The field is:

\[
GF(2)=\{0,1\}
\]

Addition and multiplication are modulo 2:

| Operation | Result |
|---|---:|
| \(0+0\) | 0 |
| \(0+1\) | 1 |
| \(1+0\) | 1 |
| \(1+1\) | 0 |
| \(0\cdot x\) | 0 |
| \(1\cdot x\) | \(x\) |

Addition is XOR.

For nonnegative integers, bitwise XOR applies the field addition independently to each binary bit.

Example:

```text
14 = 1110
11 = 1011
 7 = 0111
---------
XOR  = 0010 = 2
```

The software must define the bit width used for displayed vectors. Integer XOR itself may be performed without a fixed display width, but matrix construction requires a fixed number of columns.

## 3. Syndrome construction for the current plate fixture

The current forward triples are:

\[
U_9=(14,10,12)
\]
\[
U_6=(11,7,13)
\]
\[
U_3=(7,11,5)
\]

Define the component syndromes:

\[
S_i=U_{9,i}\oplus U_{6,i}\oplus U_{3,i}
\]

Then:

\[
S_1=14\oplus11\oplus7=2
\]
\[
S_2=10\oplus7\oplus11=2
\]
\[
S_3=12\oplus13\oplus5=0
\]

Therefore:

\[
S=(2,2,0)
\]

Using four-bit encoding:

```text
S1 = 0010
S2 = 0010
S3 = 0000
```

This is the syndrome vector for the stated input ordering.

## 4. Closed-parity invariant

For the supplied triples, the XOR within each triple is:

\[
P_9=14\oplus10\oplus12=8
\]
\[
P_6=11\oplus7\oplus13=1
\]
\[
P_3=7\oplus11\oplus5=9
\]

The total is:

\[
P_9\oplus P_6\oplus P_3=8\oplus1\oplus9=0
\]

By associativity and commutativity of XOR:

\[
S_1\oplus S_2\oplus S_3
=
P_9\oplus P_6\oplus P_3
=0
\]

This relation remains true under independent permutations of the entries within the three fixed triples, because the XOR of a triple is invariant under reordering.

Thus:

\[
S_1\oplus S_2\oplus S_3=0
\]

and:

\[
S_3=S_1\oplus S_2
\]

This is a verified algebraic consequence of the specified values and syndrome definition. It is not a physical conservation law.

## 5. Matrix definitions: do not conflate ranks

The word “rank” is meaningful only when the exact matrix and field are specified.

The project may calculate several matrices from the same candidate. They are different objects.

### 5.1 Syndrome matrix

For three syndrome vectors \(S_1,S_2,S_3\), encoded as bit rows, define:

\[
M_S=
\begin{bmatrix}
S_1\\
S_2\\
S_3
\end{bmatrix}
\]

For the current example, using four-bit rows:

\[
M_S=
\begin{bmatrix}
0&0&1&0\\
0&0&1&0\\
0&0&0&0
\end{bmatrix}
\]

The rows are dependent. Therefore:

\[
\operatorname{rank}_{GF(2)}(M_S)=1
\]

The rank is 1, not 2, for this exact three-row syndrome matrix: the first two rows are equal and the third is zero.

More generally, the closed-parity identity alone establishes:

\[
\operatorname{rank}_{GF(2)}(M_S)\leq2
\]

It does not guarantee that the rank is exactly 2.

### 5.2 Pillar matrix

A “pillar matrix” is a separate matrix defined by the implementation's chosen feature or pillar encoding.

Its row/column layout, bit mapping, and meaning must be documented independently.

A pillar rank of 3 does not contradict a syndrome-matrix rank of 1 or 2 if the matrices contain different data or encode different features.

Do not compare two rank values without showing both matrices and their construction rules.

### 5.3 Feature matrix

A feature matrix may contain norms, differences, parity bits, or other derived values. It must have its own schema and must not be called the syndrome matrix unless its rows and columns exactly match the syndrome definition.

## 6. Rank over GF(2)

A set of vectors is linearly independent over GF(2) if no nonempty subset XORs to zero.

For three vectors \(v_1,v_2,v_3\), independence requires:

- all three are nonzero;
- no two are equal;
- \(v_1\oplus v_2\oplus v_3\ne0\).

The rank is the maximum number of linearly independent rows (or columns) in the matrix.

### 6.1 Gaussian elimination

Gaussian elimination over GF(2) uses:

- row swap;
- XOR one row into another.

There is no subtraction distinct from addition, because:

\[
-1=1\quad\text{in }GF(2)
\]

Pseudocode:

```python
def gf2_rank(rows):
    matrix = [list(row) for row in rows]
    if not matrix:
        return 0

    n_rows = len(matrix)
    n_cols = len(matrix[0])

    if any(len(row) != n_cols for row in matrix):
        raise ValueError("Matrix rows must have equal length")

    pivot_row = 0

    for col in range(n_cols):
        pivot = next(
            (r for r in range(pivot_row, n_rows)
             if matrix[r][col] == 1),
            None,
        )

        if pivot is None:
            continue

        matrix[pivot_row], matrix[pivot] = (
            matrix[pivot],
            matrix[pivot_row],
        )

        for r in range(n_rows):
            if r != pivot_row and matrix[r][col] == 1:
                matrix[r] = [
                    a ^ b
                    for a, b in zip(matrix[r], matrix[pivot_row])
                ]

        pivot_row += 1

        if pivot_row == n_rows:
            break

    return pivot_row
```

This is reference pseudocode. The production implementation must validate bit values, matrix shape, and empty input behavior.

## 7. Permutations and candidate configurations

For a three-element tuple there are six permutations.

For two independently permuted triples with a third fixed:

\[
6\times6=36
\]

For three independently permuted triples:

\[
6^3=216
\]

If only cyclic rotations are permitted, each tuple has three rotations. Three independently rotated tuples produce:

\[
3^3=27
\]

If all triples must use the same rotation index, there are only three synchronous configurations.

Every experiment must declare exactly which configuration set it uses.

### 7.1 Invariant test

For the three fixed plate triples in this document, the XOR of each triple is invariant under its six permutations. Since the XOR of the three row-XOR values is zero, closed parity must hold for all 216 independent permutation combinations.

This is an exhaustive finite identity check. It does not establish that a search over an unrelated or larger state space is exhaustive.

## 8. The meaning of observability

In this repository, a GF(2) rank calculation can establish linear independence or dependence of the encoded binary vectors in a specified matrix.

That is a statement about the representation.

It does not, by itself, establish that a physical system is observable.

### 8.1 Algebraic independence

A rank result can answer:

- how many independent rows or columns are present;
- whether one encoded vector is a linear combination of others;
- whether a parity dependency exists;
- whether the selected binary features contain redundant information.

### 8.2 Measurement observability

For a physical or engineered measurement system, observability requires a model connecting hidden state to measurements.

For a linear discrete-time system:

\[
x_{t+1}=Ax_t,\qquad y_t=Cx_t
\]

the classical observability matrix is:

\[
\mathcal{O}=
\begin{bmatrix}
C\\
CA\\
CA^2\\
\vdots\\
CA^{n-1}
\end{bmatrix}
\]

The system is observable if:

\[
\operatorname{rank}(\mathcal{O})=n
\]

over the field appropriate to that system, commonly the real or complex numbers for standard physical state-space models.

This classical observability test is not interchangeable with the project's GF(2) syndrome rank. A binary encoding may be useful for a digital diagnostic layer, but a physical observability claim needs a measurement model, sensor model, and appropriate rank or identifiability analysis.

### 8.3 Required evidence for a physical observability claim

At minimum, specify:

- the physical state vector;
- governing dynamics;
- measurement equations;
- sensor placement and calibration;
- noise and uncertainty model;
- sampling and aliasing conditions;
- the observability or identifiability criterion;
- experimental controls and measured results.

Until then, use phrases such as `binary feature independence` or `GF(2) syndrome rank`, not `physical observability proven`.

## 9. 9V Consequence Tensor: proposed interface

The 9V Consequence Tensor is intended as a structured audit of consequences across nine declared components.

The name does not establish the mathematical type. The object could be a vector, matrix, tensor, graph-indexed collection, or another structure. The exact form remains `OPEN`.

### 9.1 Required formal definition

Before implementation, specify:

1. the nine component names;
2. the domain of each component;
3. units or normalization, if applicable;
4. the function mapping a source/candidate pair to component values;
5. dependencies between components;
6. uncertainty representation;
7. threshold or policy for each component;
8. how missing values are handled;
9. how the result influences Gate and Bindu.

A proposed generic interface is:

```text
ConsequenceRequest
  source_state
  candidate_state
  dependency_graph
  component_schema
  model_version
  uncertainty_model
```

Possible result:

```text
ConsequenceResult
  status
  component_values
  component_uncertainties
  dependency_results
  failed_checks
  unavailable_checks
  evidence_refs
  model_version
```

`status` must distinguish at least:

- `PASS`
- `FAIL`
- `HOLD`
- `NOT_EVALUATED`

`NOT_EVALUATED` must never be treated as `PASS`.

### 9.2 Consequence function

A generic mathematical placeholder is:

\[
\mathbf{v}(s,c)=
(v_1(s,c),v_2(s,c),\ldots,v_9(s,c))
\]

This is only a nine-component vector notation. It is not yet a defined tensor model.

Each component \(v_i\) must be specified independently. Do not invent nine axes or their meanings merely to fill the schema.

### 9.3 Dependency representation

If consequences depend on one another, represent those dependencies explicitly, for example as a directed graph:

\[
D=(V_D,E_D)
\]

where vertices are consequence components and edges represent defined dependency relations.

An edge must have a documented meaning. Do not infer causal direction from correlation alone.

### 9.4 Uncertainty

If a consequence estimate is uncertain, preserve that uncertainty.

A component may return:

```text
value
uncertainty
method
assumptions
evidence_refs
```

Do not combine uncertainty values with incompatible units or statistical meanings.

## 10. Integration of GF(2) and 9V

The GF(2) engine and the 9V audit have separate responsibilities.

- **GF(2) engine:** checks binary encodings, parity relations, and rank of explicitly defined matrices.
- **9V audit:** evaluates declared downstream consequence dimensions.
- **Shadow:** preserves unresolved issues from either component.
- **Gate:** applies the task's admissibility policy.
- **Bindu:** issues the final verdict.

A successful GF(2) check does not automatically pass 9V.

A successful 9V check does not automatically prove GF(2) independence.

A candidate may pass one layer and fail another.

## 11. Required software interfaces

Suggested module functions:

```python
def encode_bits(value: int, width: int) -> tuple[int, ...]:
    ...

def xor_values(values: list[int]) -> int:
    ...

def build_syndrome_matrix(plate_values, width: int):
    ...

def gf2_rank(matrix) -> int:
    ...

def check_closed_parity(syndromes) -> bool:
    ...

def enumerate_permutations(triples):
    ...

def evaluate_9v(source_state, candidate_state, schema):
    ...
```

Every function must validate its input shape and return explicit results. Avoid hidden global thresholds.

## 12. Required tests

### GF(2) tests

1. XOR truth table.
2. Integer XOR examples: `14 ^ 11 ^ 7 == 2`.
3. Supplied syndrome equals `(2, 2, 0)`.
4. Row-XOR values equal `(8, 1, 9)`.
5. Closed parity equals zero.
6. Syndrome matrix rows are encoded with the declared width.
7. Current syndrome matrix rank equals 1.
8. A separate synthetic matrix with three independent rows has rank 3.
9. A matrix with duplicate rows has reduced rank.
10. Invalid bit values and ragged matrices are rejected.

### Permutation tests

1. A triple produces six permutations.
2. Three independent triples produce 216 combinations.
3. Closed parity remains zero for all 216 combinations of the fixed triples.
4. Synchronous rotations are not mislabeled as independent permutations.

### 9V tests

1. Undefined schema returns `NOT_EVALUATED`.
2. Missing component values cannot produce `PASS`.
3. A failed hard consequence rule returns `FAIL`.
4. Uncertainty is preserved in the result.
5. Every component result records its model version and evidence references.

## 13. Reporting requirements

Every report containing a rank result must state:

- matrix name;
- matrix dimensions;
- exact rows or columns;
- bit width and encoding;
- field (`GF(2)`);
- rank algorithm;
- rank value;
- any known algebraic dependencies.

Every 9V report must state:

- schema version;
- component definitions;
- equations or calculation methods;
- units and normalization;
- uncertainty method;
- thresholds;
- missing or unavailable components.

## 14. Current verified and open points

| Statement | Status | Scope |
|---|---|---|
| Supplied syndrome is `(2, 2, 0)` | `VERIFIED` by direct arithmetic | Exact supplied triples and ordering. |
| Triple row-XOR values are `(8, 1, 9)` | `VERIFIED` by direct arithmetic | Exact supplied triples. |
| Total closed parity is zero | `VERIFIED` by direct arithmetic | Exact supplied triples and XOR definition. |
| Closed parity persists under independent permutations | `VERIFIED` by algebraic identity | Permutations of the same fixed triples. |
| Current 3-row, 4-bit syndrome matrix has rank 1 | `VERIFIED` by direct matrix calculation | Matrix shown in Section 5.1. |
| A separate pillar matrix has rank 3 | `OPEN` until its exact matrix is specified and checked | Must not be inferred from syndrome rank. |
| GF(2) rank proves physical observability | `NOT ESTABLISHED` | Requires a physical measurement model. |
| 9V is a defined nine-component tensor | `OPEN` | Components and equations are not yet fixed. |
| 9V improves decision quality | `HYPOTHESIS` | Requires controlled evaluation against baselines. |

## 15. Interpretation boundary

The binary calculations in this document can establish exact properties of encoded data.

They cannot independently establish:

- a physical conservation law;
- a new physical degree of freedom;
- a photonic or atomic mechanism;
- a laboratory sensor's observability;
- a causal relation between consequence components;
- an advantage over other decision or search systems.

Those claims require their own mathematical models and evidence.
