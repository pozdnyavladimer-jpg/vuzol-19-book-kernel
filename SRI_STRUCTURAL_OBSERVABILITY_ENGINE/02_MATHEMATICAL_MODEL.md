# 02 — MATHEMATICAL MODEL
## State space, operators, invariants, and reproducible formal definitions

**File:** `02_MATHEMATICAL_MODEL.md`  
**Role:** Mathematical contract for the SRI Structural Observability Engine  
**Status:** Formalization baseline; unresolved definitions are explicitly marked `OPEN`

---

## 1. Purpose and scope

This document defines the mathematical objects that the software is expected to manipulate.

It separates:

1. a general state-transition framework;
2. the specific finite integer examples used in the current research;
3. binary calculations over GF(2);
4. proposed extensions that are not yet formally established.

The definitions below are a starting mathematical contract. They do not prove that the model has an advantage over existing solvers, and they do not establish a physical interpretation.

## 2. Basic state-space model

Let the modeled state space be:

\[
\mathcal{S} \subseteq \mathcal{X}
\]

where \(\mathcal{X}\) is the declared ambient representation space and \(\mathcal{S}\) is the subset of admissible states.

A state is denoted:

\[
s \in \mathcal{S}
\]

The model must specify:

- the type and shape of a state;
- the valid value range for each component;
- the constraints defining admissibility;
- whether the state space is finite or continuous;
- how equality and identity are determined.

For a finite integer model, a state may be represented as a tuple:

\[
s=(x_1,x_2,\ldots,x_n), \qquad x_i \in \mathbb{Z}
\]

If bounds are imposed, they must be stated explicitly, for example:

\[
x_i \in \{0,1,\ldots,M\}
\]

Do not assume a bound or value range that is not present in the experiment specification.

## 3. Constraints and admissibility

Let the hard constraints be functions:

\[
g_j:\mathcal{X}\rightarrow\{\text{true},\text{false}\}
\]

for \(j=1,\ldots,m\).

The admissible set is:

\[
\mathcal{S}=
\{x\in\mathcal{X}:g_j(x)=\text{true}\;\text{for all }j\}
\]

A candidate that violates any hard constraint is not admissible, regardless of its score.

Soft objectives may be represented separately:

\[
f_k:\mathcal{S}\rightarrow\mathbb{R}
\]

A weighted score may be used only when the weights, units, normalization, and direction of preference are documented. A weighted score must not silently override a hard constraint.

## 4. Forward and reverse operators

The project uses the names `+3` and `−3` for paired operations. Their exact implementation is domain-dependent.

Define a forward proposal operator:

\[
F_{+3}:\mathcal{S}\rightarrow 2^{\mathcal{X}}
\]

It maps a state to a set of candidate states. The powerset \(2^{\mathcal{X}}\) allows zero, one, or multiple proposals.

Define a reverse or audit operator:

\[
F_{-3}:\mathcal{X}\times\mathcal{S}\rightarrow\mathcal{A}
\]

where \(\mathcal{A}\) is an audit-result space. It may compare a candidate with its source state, required constraints, or a defined rollback relation.

**Important:** `F_{-3}` is not assumed to be the mathematical inverse of `F_{+3}`. If an implementation claims inverse behavior, it must define the relevant domains and prove or test the property.

For a deterministic transition function \(T\), an inverse claim would require a suitable identity such as:

\[
T^{-1}(T(s))=s
\]

on a stated domain. If the forward operator is one-to-many, an ordinary single-valued inverse may not exist.

## 5. Shadow as an audit record

Shadow is represented as structured evidence, not as an undefined scalar.

Let:

\[
H(s,c)=\{h_1,h_2,\ldots,h_q\}
\]

be the set of unresolved audit items for source state \(s\) and candidate \(c\).

Each item should include:

```text
shadow_id
candidate_id
kind
description
status
severity
evidence_refs
resolution_condition
next_action
```

The mathematical aggregation of Shadow items into a score is **OPEN**. Do not invent a universal Shadow norm or combine unlike categories without a justified model.

A missing measurement, a violated hard constraint, and a low-confidence estimate are different kinds of evidence and should remain distinguishable.

## 6. Gate and Bindu

Let the Gate predicate be:

\[
G(c,H,E)\in\{\text{true},\text{false}\}
\]

where:

- \(c\) is the candidate;
- \(H\) is its Shadow record;
- \(E\) is the available evidence.

The Gate is true only when every required admissibility condition for the stated task has passed.

Bindu maps the candidate and audit information to a verdict:

\[
B(c,H,E)\in
\{\text{ALLOW},\text{HOLD},\text{REPAIR},\text{REWRITE},\text{BLOCK}\}
\]

A minimal policy is:

- `BLOCK` if a hard prohibition is violated;
- `HOLD` if required evidence is missing or uncertainty prevents a decision;
- `REPAIR` if a localized, correctable defect is identified;
- `REWRITE` if the representation or proposal is invalid and must be reformulated;
- `ALLOW` only if all required checks pass for the declared scope.

If multiple conditions apply, precedence must be explicit. A suggested safe precedence is:

```text
BLOCK > HOLD > REWRITE > REPAIR > ALLOW
```

This precedence is a proposed software policy, not a theorem. It must be reviewed against the actual task.

## 7. Memory representation

A MemoryAtom stores a record:

\[
M=(id, s, c, v, E, H, t, version)
\]

where:

- `id` is a stable identifier;
- \(s\) is the source state or its reference;
- \(c\) is the candidate or its reference;
- \(v\) is the verdict;
- \(E\) is the evidence set;
- \(H\) is the unresolved Shadow set;
- \(t\) is a timestamp or monotonic sequence;
- `version` identifies the model and rule versions.

Memory is a provenance mechanism. Storing a claim does not increase its truth status.

## 8. Six-node cyclic example

This section defines a small graph example used to test the meaning of the `+3` and `−3` route notation.

Let:

\[
V=\{0,1,2,3,4,5\}
\]

with arithmetic modulo 6.

Define the step-two map:

\[
T(i)=(i+2)\bmod 6
\]

Then the orbit beginning at node 0 is:

\[
0\rightarrow2\rightarrow4\rightarrow0
\]

The orbit beginning at node 1 is:

\[
1\rightarrow3\rightarrow5\rightarrow1
\]

If the project chooses the reverse orientation for the second route, it may be written:

\[
1\rightarrow5\rightarrow3\rightarrow1
\]

These are two 3-cycles in the same six-node graph. They are graph orbits, not physical particle trajectories.

### 8.1 Properties

For every node \(i\):

\[
T^3(i)=i
\]

because:

\[
i+2+2+2=i+6\equiv i\pmod 6
\]

The map \(T\) is a permutation and its inverse is:

\[
T^{-1}(i)=(i-2)\bmod6
\]

The inverse route from node 0 is:

\[
0\rightarrow4\rightarrow2\rightarrow0
\]

Do not confuse the inverse of this specific graph map with every use of the project's general `−3` audit operator.

## 9. Integer plate model

The current research example uses three ordered integer triples:

\[
U_9=(14,10,12)
\]
\[
U_6=(11,7,13)
\]
\[
U_3=(7,11,5)
\]

and corresponding reverse triples:

\[
D_9=(12,9,10)
\]
\[
D_6=(10,5,11)
\]
\[
D_3=(5,9,4)
\]

These values are a test fixture. They are not universal constants and must not be interpreted as measured physical quantities unless a separate experiment establishes that meaning.

For any triple \(U=(a,b,c)\), define its component sum:

\[
\Sigma(U)=a+b+c
\]

For the supplied forward triples:

\[
\Sigma(U_9)=36,\qquad
\Sigma(U_6)=31,\qquad
\Sigma(U_3)=23
\]

The vertical sum vector for the supplied ordering is:

\[
V=U_9+U_6+U_3=(32,28,30)
\]

The component-wise addition is:

\[
(14+11+7,\;10+7+11,\;12+13+5)=(32,28,30)
\]

This vertical sum is distinct from the sum of all nine entries:

\[
32+28+30=90
\]

The implementation must not confuse a vector of column sums with a scalar total.

### 9.1 Other proposed plate metrics

The research code has used metrics such as:

- squared Euclidean norm;
- component-wise difference;
- cross-resonance expressions;
- cubic determinant expressions;
- perimeter-like sums.

These names are not enough to define the metrics. Each metric must be specified by an exact equation in the implementation or in an experiment document before its result is treated as reproducible.

For a triple \(x=(x_1,x_2,x_3)\), the squared Euclidean norm is:

\[
\|x\|^2=x_1^2+x_2^2+x_3^2
\]

For two triples \(x,y\), the squared Euclidean distance is:

\[
d^2(x,y)=\sum_{i=1}^{3}(x_i-y_i)^2
\]

Do not call a quantity a determinant unless the exact matrix whose determinant is calculated is shown.

## 10. GF(2) and XOR model

The binary field is:

\[
GF(2)=\{0,1\}
\]

with addition and multiplication modulo 2.

Addition in \(GF(2)\) is XOR:

\[
1+1=0,\qquad 1+0=1,\qquad 0+0=0
\]

For nonnegative integers, bitwise XOR applies this operation independently to each binary digit.

For the forward triples, define syndrome components:

\[
S_i=U_{9,i}\oplus U_{6,i}\oplus U_{3,i}
\]

Using the supplied ordering:

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

As four-bit vectors:

```text
2 = 0010
2 = 0010
0 = 0000
```

The XOR of all three syndrome components is:

\[
S_1\oplus S_2\oplus S_3=2\oplus2\oplus0=0
\]

### 10.1 Permutation-invariant parity identity

For any fixed three triples \(A,B,C\), define:

\[
S_i=A_i\oplus B_i\oplus C_i
\]

Then, by associativity and commutativity of XOR:

\[
S_1\oplus S_2\oplus S_3
=
(A_1\oplus A_2\oplus A_3)
\oplus
(B_1\oplus B_2\oplus B_3)
\oplus
(C_1\oplus C_2\oplus C_3)
\]

The XOR of the entries within each triple is invariant under permutation of that triple. Therefore, if the XOR of the three row-XOR values is zero for one set of fixed triples, the total syndrome XOR remains zero under independent permutations of those triples.

For the supplied forward triples:

\[
14\oplus10\oplus12=8
\]
\[
11\oplus7\oplus13=1
\]
\[
7\oplus11\oplus5=9
\]

and:

\[
8\oplus1\oplus9=0
\]

Thus the closed-parity identity holds for every independent permutation of these three fixed triples.

This is an algebraic invariant of the specified values and operation. It is not a physical conservation law.

### 10.2 Rank consequence

If the syndrome matrix uses the three syndrome vectors as rows and the closed relation is:

\[
S_1\oplus S_2\oplus S_3=0
\]

then one row is the XOR of the other two. Hence:

\[
\operatorname{rank}_{GF(2)}(S)\leq2
\]

This conclusion applies to that exact syndrome matrix. It does not imply that every other matrix derived from the same plate data has rank at most 2.

The project must name each matrix separately, for example:

- `syndrome_matrix`;
- `pillar_matrix`;
- `feature_matrix`.

Their ranks must not be conflated.

## 11. Rank-three criterion for three binary vectors

Let \(v_1,v_2,v_3\in GF(2)^n\).

The three vectors are linearly independent if and only if no nonempty subset has XOR equal to zero.

For exactly three vectors, this means:

1. \(v_1\ne0\), \(v_2\ne0\), \(v_3\ne0\);
2. no pair is equal, because \(v_i\oplus v_j=0\) iff \(v_i=v_j\);
3. \(v_1\oplus v_2\oplus v_3\ne0\).

If the triple XOR is zero, the three vectors are dependent even if all three are nonzero and pairwise distinct.

The implementation should test independence by Gaussian elimination over GF(2), not by floating-point rank.

## 12. Rotation and permutation search spaces

For a triple, there are:

\[
3!=6
\]

permutations.

If two triples are independently permuted while the first is fixed, the number of combinations is:

\[
6\times6=36
\]

If each of three triples is independently permuted, the number is:

\[
6^3=216
\]

If only cyclic rotations are allowed, each triple has three rotations, so three independently rotated triples yield:

\[
3^3=27
\]

The experiment must state which transformation set is being searched. “All rotations” and “all permutations” are not interchangeable.

A synchronous rotation search, where all triples use the same rotation index, has only three configurations. It is not an exhaustive search of the 9, 27, 36, or 216 configuration spaces.

## 13. Search-space size and claims

If a model has \(n\) independent coordinates and each coordinate has \(m\) possible values, the unconstrained Cartesian product has:

\[
m^n
\]

states.

For \(m=20\) and \(n=18\):

\[
20^{18}=262144000000000000000000
\]

approximately:

\[
2.62144\times10^{23}
\]

This is the size of the unconstrained Cartesian product only. A solver that uses constraints, sphere enumeration, pruning, or nested loops has not necessarily enumerated every one of those states.

Reports must distinguish:

- theoretical unconstrained state-space size;
- number of generated candidates;
- number of candidates evaluated;
- number rejected by each constraint;
- number accepted;
- whether enumeration was exhaustive within the stated constrained space.

Never claim exhaustive search over \(20^{18}\) states unless the implementation actually evaluated every state in that set.

## 14. Metrics and thresholds

A metric is a function:

\[
m:\mathcal{X}\rightarrow\mathbb{R}
\]

A threshold rule may be written:

\[
m(x)\leq\tau
\]

Every threshold must document:

- its metric;
- its units or scale;
- whether lower or higher is better;
- its chosen value;
- the rationale for the value;
- sensitivity to nearby values;
- false-accept and false-reject behavior, where measurable.

Thresholds such as forward shear, rollback shear, peak drop, or maximum bit flips are experimental policy parameters until independently justified.

A result that passes a chosen threshold means only that it passed that rule under that configuration.

## 15. Open mathematical definitions

The following must be specified before full implementation claims are made:

| Object | Required definition | Status |
|---|---|---|
| Full Flower graph | Exact nodes, edges, and allowed transitions | `OPEN` |
| General `+3` operator | Domain, codomain, and proposal rule | `OPEN` |
| General `−3` operator | Audit relation and inverse/rollback semantics | `OPEN` |
| CASR objective | Exact objective function and constraints | `OPEN` |
| Shadow aggregation | Whether and how heterogeneous items are aggregated | `OPEN` |
| 9V tensor | Nine components, domains, equations, and dependency rules | `OPEN` |
| Color verdict thresholds | Machine-readable mapping and calibration | `OPEN` |
| General Bindu precedence | Formal policy for simultaneous verdict conditions | `OPEN` pending policy review |

## 16. Minimum mathematical test suite

The implementation should include tests for:

1. the six-node map satisfies \(T^3(i)=i\) for all six nodes;
2. the inverse map satisfies \(T^{-1}(T(i))=i\);
3. supplied forward plate sums equal `(32, 28, 30)`;
4. supplied syndrome equals `(2, 2, 0)`;
5. supplied row-XOR values equal `(8, 1, 9)`;
6. total closed parity equals zero;
7. the closed parity remains zero under all 216 independent permutations of the three fixed triples;
8. the syndrome matrix rank is calculated over GF(2);
9. the rank-three criterion is tested on independent and dependent vector examples;
10. the reported search-space size is distinguished from the number of candidates actually evaluated.

## 17. Interpretation rule

The equations in this document establish properties of the defined mathematical model and supplied test values.

They do not, by themselves, establish:

- a physical structure of matter;
- a new particle model;
- a physical law;
- superior computational performance;
- laboratory observability;
- a universal decision theory.

Those claims require separate derivations, matched computational experiments, or physical measurements appropriate to the claim.
