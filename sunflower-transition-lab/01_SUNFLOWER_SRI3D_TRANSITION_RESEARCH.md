# 01 — Sunflower / Sri3D Transition Research

Status: **RESEARCH / MODEL / HOLD**  
Project line: **Vuzol-19 / Flower-Sri / Mathematical Stress Test**  
Purpose: test whether provenance-preserving rank transitions reveal a useful recurrence or descent mechanism in the Sunflower problem.

---

## 0. Boundary

This document does **not** claim a proof of the Erdős–Rado Sunflower Conjecture.

It does **not** assume that Fibonacci numbers govern sunflower families.

It does **not** claim that a set family literally forms a physical 3D spiral.

The 3D language is used operationally:

```text
FORM        = current combinatorial state
ORIENTATION = current role/decomposition choice
MEMORY      = provenance of each reduction/lift
```

The hypothesis is narrower:

> A flat projection can create false-green by losing provenance.  
> A provenance-preserving oriented transition may expose structure that ordinary rank reduction hides.

---

## 1. Mathematical object

Let

\[
\mathcal F \subseteq \binom{[n]}{k}
\]

be a \(k\)-uniform family.

A collection

\[
F_1,\dots,F_r \in \mathcal F
\]

is an \(r\)-sunflower if all pairwise intersections are equal to the same core \(C\):

\[
F_i\cap F_j=C
\qquad
(i\neq j).
\]

Equivalently, define petals

\[
P_i=F_i\setminus C.
\]

Then:

\[
P_i\cap P_j=\varnothing
\qquad
(i\neq j).
\]

---

## 2. A measurable Shadow coordinate

For a chosen \(r\)-tuple define

\[
C=\bigcap_{i=1}^{r}F_i
\]

and

\[
P_i=F_i\setminus C.
\]

Define petal-conflict energy

\[
E(F_1,\dots,F_r)
=
\sum_{i<j}|P_i\cap P_j|.
\]

Then, for this fixed tuple,

\[
E=0
\iff
(F_1,\dots,F_r)\text{ is a sunflower}.
\]

This gives a useful diagnostic coordinate:

```text
E = 0      -> local sunflower Bindu
E > 0      -> unresolved petal conflict
```

Important:

`E` is a diagnostic for a selected tuple.  
It is not yet a global potential function for an entire family.

---

## 3. Sri3D state

Use the transition state

\[
S_t=(X_t,O_t,M_t).
\]

For this research branch:

\[
X_t=
(k_t,\mathcal F_t,C_t,E_t)
\]

where:

- \(k_t\) = current rank,
- \(\mathcal F_t\) = current family or local candidate subfamily,
- \(C_t\) = currently selected core candidate,
- \(E_t\) = local petal-conflict diagnostic.

`O_t` is the orientation / role assignment:

```text
which element is treated as core candidate?
which coordinate is removed?
which branch is active?
which reduction rule is being applied?
```

`M_t` is provenance:

```text
source family
source set
removed element
transform id
parent transition id
preserved properties
lift evidence
```

The point of the third coordinate is:

\[
\boxed{\text{same projected state}\neq\text{same transition history}}
\]

---

## 4. OrientedPetal

Ordinary rank reduction can use:

\[
F\mapsto E=F\setminus\{x\}.
\]

But this can lose the information needed to lift a lower-rank structure back to the original family.

Therefore define:

```text
OrientedPetal = (
    payload,
    source_id,
    removed_element,
    transform_id,
    orientation,
    preserved_properties,
    lift_contract
)
```

Mathematically:

\[
(F,x)
\mapsto
(E,x,\mathrm{source}),
\qquad
E=F\setminus\{x\}.
\]

The required Gate is not merely:

```text
lower-rank sunflower found
```

but:

```text
lower-rank sunflower found
AND
its members come from valid distinct sources
AND
the lifted source sets are themselves a sunflower
```

This prevents one class of false-green caused by projection.

---

## 5. Why the route can be viewed as a helix

Suppose reductions are applied successively:

\[
\mathcal F_k
\to
\mathcal F_{k-1}
\to
\mathcal F_{k-2}
\to
\cdots
\]

while every step records:

\[
(x_t,\mathrm{source}_t,O_t).
\]

Then the full route is not only a sequence of lower-rank families.

It is:

\[
\Gamma
=
\bigl(
S_0,S_1,\dots,S_T
\bigr).
\]

This is the "DNA-like" part of the model:

```text
the route remembers its previous transformations
```

The word "helix" is a visualization of recurrence + orientation + memory.

It is not a claim that the combinatorial object is physically helical.

---

## 6. Do not insert Fibonacci

A Fibonacci process has explicit second-order memory:

\[
F_{n+1}=F_n+F_{n-1}.
\]

Nothing currently proves an analogous recurrence for sunflower extremal numbers.

The correct research order is:

```text
1. encode exact transitions
2. keep provenance
3. measure state variables
4. search for recurrence
5. only then classify the recurrence
```

Possible outcomes include:

```text
first-order recurrence
second-order recurrence
piecewise recurrence
submultiplicative law
entropy inequality
potential descent
no simple recurrence
```

Therefore:

\[
\boxed{\text{Fibonacci is a candidate pattern, not an assumption}}
\]

---

## 7. The real missing Gate

Let \(M(k,r)\) be the maximum size of an \(r\)-sunflower-free \(k\)-uniform family.

The classical recurrence loses a factor depending on \(k\).

The desired type of transition would be a map

\[
\Phi:\mathcal F_k\to\mathcal G_{k-1}
\]

such that:

\[
|\mathcal G|
\ge
\frac{|\mathcal F|}{C_r}
\]

with \(C_r\) independent of \(k\), and with a lift guarantee:

\[
r\text{-sunflower in }\mathcal G
\Rightarrow
r\text{-sunflower in }\mathcal F.
\]

The current Sri3D hypothesis is therefore:

\[
\boxed{
\text{constant-loss}
+
\text{provenance-preserving}
+
\text{liftable}
+
\text{rank reduction}
}
\]

This is still **HOLD**.

The architecture only localizes the missing property.

---

## 8. Candidate Shadow descent

The next idea to test is whether there exists a global potential

\[
\Phi(\mathcal F_t,O_t,M_t)
\]

such that every valid reduction satisfies

\[
\Phi_{t+1}<\Phi_t
\]

until a terminal state is reached.

A naive candidate is based on pairwise petal overlap:

\[
E=
\sum_{i<j}|P_i\cap P_j|.
\]

But this is only local to a chosen tuple.

A useful global potential might need additional terms, for example:

\[
\Phi
=
\alpha E
+
\beta H
+
\gamma L
+
\delta R,
\]

where possible terms are:

- \(E\): petal-conflict mass,
- \(H\): concentration / entropy of element frequencies,
- \(L\): provenance loss,
- \(R\): rank or branching cost.

These terms are placeholders for experiments, not established mathematics.

---

## 9. Sri roles for this problem

The nine roles can be instantiated without claiming geometric necessity:

| Sri role | Sunflower research role |
|---|---|
| T1 Activation | choose \(n,k,r\), family, target |
| T2 Receiver | type and normalize family data |
| T3 Direction | select candidate core/reduction orientation |
| T4 Structure | build projected/oriented family |
| T5 Boundary | distinct sources, rank, valid deletion |
| T6 Balance | sunflower condition / invariants |
| T7 Memory | source, removed element, transform history |
| T8 Shadow | overlap, failed lift, false-green |
| T9 Repair | change orientation/reduction and retry |

The 3D interpretation does not replace these roles.

It makes `T7 Memory` and orientation explicit state coordinates.

---

## 10. Exact Gate for a local tuple

Given \(F_1,\dots,F_r\):

```text
C = intersection(F_i)
P_i = F_i - C
E = sum_{i<j} |P_i ∩ P_j|
```

Decision:

```text
ALLOW_LOCAL_SUNFLOWER iff E == 0
```

For a projected tuple, additionally require:

```text
distinct source ids
valid transform provenance
successful lift
lifted parents satisfy the same sunflower predicate
```

If lower-rank structure exists but lift is not verified:

```text
HOLD
```

If lift fails:

```text
BLOCK
```

---

## 11. What would count as a real result

A result becomes mathematically interesting if one of the following appears independently in exact experiments:

1. A rank-reduction rule with loss bounded independently of \(k\).
2. A nontrivial invariant preserved by oriented reduction.
3. A global potential with provable monotone descent.
4. A recurrence across extremal families that predicts unseen \(k\).
5. A structural classification of false-green projections.
6. A lift theorem stronger than direct rechecking of the original family.

Merely plotting a spiral is **not** a result.

Merely recovering Fibonacci-looking numbers from selected examples is **not** a result.

---

## 12. Current verdict

```text
Flower:
    many candidate decompositions

Sri3D:
    role/orientation of each reduction

Memory:
    exact provenance of deleted coordinates

Shadow:
    petal overlap + failed lift + lost provenance

Bindu:
    verified local sunflower or verified structural theorem

Status:
    HOLD
```

The current research target is:

\[
\boxed{
\text{Does a provenance-preserving rank trajectory expose
a recurrence or descent law that flat set projection hides?}
}
