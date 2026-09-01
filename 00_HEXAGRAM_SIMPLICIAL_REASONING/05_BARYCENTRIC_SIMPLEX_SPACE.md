# 05 — BARYCENTRIC SIMPLEX SPACE

**Project:** Vuzol-19  
**Module:** Hexagram Simplicial Reasoning  
**Status:** MATHEMATICAL LOCAL-STATE SPEC  
**State:** CRYSTAL  
**Language:** English  
**Depends on:** `04_TRIANGLES_INSIDE_TRIANGLES.md`

---

## 0. PURPOSE

The previous file introduced recursive triads:

```text
Parent
  |
  +-- A
  +-- B
  +-- C
```

This file defines the mathematical state space inside each local triangle.

The central goal is to separate four things that must not be confused:

```text
1. SHAPE
2. MAGNITUDE
3. MASS / SCALE
4. RESIDUAL / INFORMATION LOSS
```

A normalized triangle only preserves relative composition.

It does **not** prove that the original information is intact.

---

# 1. STANDARD 2-SIMPLEX

**FACT**

The standard 2-simplex is:

```math
\Delta^2
=
\left\{
(a,b,c)
\;\middle|\;
a,b,c \ge 0,
\;
a+b+c=1
\right\}
```

A point in `Delta^2` can be interpreted as barycentric coordinates inside a triangle.

The three vertices are:

```math
e_1=(1,0,0)
```

```math
e_2=(0,1,0)
```

```math
e_3=(0,0,1)
```

A general point is:

```math
p
=
a e_1+b e_2+c e_3
```

with:

```math
a+b+c=1
```

---

# 2. BARYCENTRIC INTERPRETATION

For a local triad:

```text
A
B
C
```

define relative contributions:

```math
p=(a,b,c)
```

Example:

```math
p=(0.60,0.30,0.10)
```

Interpretation:

```text
A contributes 60%
B contributes 30%
C contributes 10%
```

This describes **shape**, not total scale.

---

# 3. SHAPE VS MAGNITUDE

Consider two raw triads:

```math
x=(0.6,0.3,0.1)
```

and:

```math
y=(6,3,1)
```

After normalization:

```math
\frac{x}{\sum x}
=
\frac{y}{\sum y}
=
(0.6,0.3,0.1)
```

The barycentric shape is identical.

But the total magnitudes are different:

```math
m_x=1
```

```math
m_y=10
```

Therefore a local node should preserve:

```text
normalized shape p
+
magnitude m
```

---

# 4. RAW-TO-SIMPLEX MAP

For nonnegative raw components:

```math
r=(r_1,r_2,r_3)
```

define:

```math
m
=
r_1+r_2+r_3
```

If:

```math
m>0
```

then:

```math
p_i
=
\frac{r_i}{m}
```

and:

```math
p=(p_1,p_2,p_3)\in\Delta^2
```

The raw triad can be reconstructed exactly from:

```math
r_i
=
m p_i
```

provided `m` and `p` are both preserved.

---

# 5. ZERO-MASS CASE

If:

```math
r_1=r_2=r_3=0
```

then:

```math
m=0
```

and normalization is undefined.

Do not silently divide by zero.

Use an explicit zero-state:

```text
ZERO_TRIAD
```

or store:

```math
p=(1/3,1/3,1/3)
```

only as a display convention together with:

```math
m=0
```

The magnitude must make clear that no active mass exists.

---

# 6. SIGNED VALUES

Not every reasoning variable is nonnegative.

A triad may contain:

```math
r_i < 0
```

Standard barycentric coordinates do not directly represent arbitrary signed values as convex weights.

Therefore signed states require an explicit policy.

Possible options:

```text
A — split sign and magnitude
B — affine barycentric coordinates
C — positive/negative channels
D — task-specific transform
```

The default prototype should use **sign + magnitude**.

---

# 7. SIGN-MAGNITUDE REPRESENTATION

For each raw component:

```math
r_i
```

store:

```math
s_i
=
\operatorname{sign}(r_i)
```

and:

```math
q_i
=
|r_i|
```

Normalize only the magnitudes:

```math
p_i
=
\frac{q_i}{
q_1+q_2+q_3
}
```

Then the local state is:

```math
T
=
(p,m,s)
```

where:

- `p` — normalized shape;
- `m` — total magnitude;
- `s` — sign pattern.

This prevents normalization from erasing direction.

---

# 8. SCALE VARIABLE

The term `mass` may be misleading outside physical tasks.

Use a generic scale variable:

```math
m
```

which may represent:

- total activation;
- absolute intensity;
- probability mass;
- energy-like quantity;
- confidence mass;
- accumulated error;
- task-specific scale.

The semantics of `m` must be declared by the task.

---

# 9. LOCAL STATE TUPLE

A minimal simplex state is:

```math
T
=
(p,m,s)
```

A reasoning-ready node needs more:

```math
T
=
(p,m,s,E,U,P,S,C)
```

where:

- `p` — barycentric shape;
- `m` — magnitude / scale;
- `s` — sign or direction metadata;
- `E` — edge / coupling state;
- `U` — uncertainty;
- `P` — provenance;
- `S` — Shadow / residual;
- `C` — certificate / constraints.

This is the local state contract for later files.

---

# 10. NORMALIZATION DOES NOT VERIFY INTEGRITY

This is a critical rule.

Suppose code does:

```python
coords = coords / coords.sum()
```

Then:

```math
a+b+c=1
```

is guaranteed by normalization.

Therefore this equality cannot detect:

```text
missing term
lost dependency
wrong sign
wrong scale
erased residual
wrong coupling
```

The simplex closure condition only verifies the coordinate representation.

It does **not** verify the reasoning history.

---

# 11. CONSERVATION RESIDUAL

If the task has a meaningful conserved quantity, preserve it separately.

Let parent scale be:

```math
m_P
```

and child scales:

```math
m_1,m_2,m_3
```

Define:

```math
r_m
=
m_P
-
(m_1+m_2+m_3)
```

Then a conservation Gate may require:

```math
|r_m|
\le
\tau_m
```

This is a genuine integrity check if conservation is task-valid.

It is not equivalent to coordinate normalization.

---

# 12. RECONSTRUCTION RESIDUAL

Let the original child state be:

```math
X
```

and reconstructed state be:

```math
\hat{X}
```

Define:

```math
r_{\mathrm{rec}}
=
X-\hat{X}
```

and reconstruction error:

```math
E_{\mathrm{rec}}
=
d(X,\hat{X})
```

This directly measures information loss.

Later, `-3 Backward` will use this quantity.

---

# 13. COMPONENT-WISE RESIDUAL

Instead of only one scalar error, retain:

```math
r_{\mathrm{rec}}
=
(r_1,r_2,r_3)
```

This helps localize where compression failed.

Example:

```text
r1 = 0.00
r2 = 0.01
r3 = 0.32
```

The system can identify the third branch as the dominant source of mismatch.

This supports local `EXPAND`.

---

# 14. EDGE STATE

A triangle is not only its vertices.

Store internal relations:

```text
A <-> B
B <-> C
C <-> A
```

Represent them as:

```math
E
=
(e_{AB},e_{BC},e_{CA})
```

or with a symmetric matrix:

```math
K
=
\begin{bmatrix}
0 & e_{AB} & e_{AC} \\
e_{AB} & 0 & e_{BC} \\
e_{AC} & e_{BC} & 0
\end{bmatrix}
```

The exact edge semantics are task-dependent.

---

# 15. DIRECTED COUPLINGS

Some relations are directional.

Then use:

```math
K
=
\begin{bmatrix}
0 & k_{AB} & k_{AC} \\
k_{BA} & 0 & k_{BC} \\
k_{CA} & k_{CB} & 0
\end{bmatrix}
```

where:

```math
k_{AB}
\ne
k_{BA}
```

is allowed.

This matters for:

- causality;
- state transitions;
- influence;
- directional constraints;
- forward/backward asymmetry.

---

# 16. TRIANGLE-LEVEL AGGREGATE

A local triangle may also have a face-level state:

```math
f_T
=
g(p,m,E,U)
```

This is the summary passed upward during `+3 Forward`.

The parent should not be confused with the raw child vertices.

It is a derived aggregate.

---

# 17. DISTANCE — RAW STATE

For raw vectors:

```math
r^A
```

and:

```math
r^B
```

a simple distance is:

```math
d_{\mathrm{raw}}
=
\|r^A-r^B\|_2
```

This captures absolute differences.

But it mixes shape and magnitude.

---

# 18. DISTANCE — SHAPE

For normalized simplex points:

```math
p^A,p^B\in\Delta^2
```

a simple shape distance is:

```math
d_{\mathrm{shape}}
=
\|p^A-p^B\|_2
```

This ignores scale.

That is useful when only relative composition matters.

---

# 19. DISTANCE — MAGNITUDE

Magnitude difference:

```math
d_{\mathrm{mag}}
=
|m_A-m_B|
```

The full local distance may combine:

```math
d_T
=
\alpha d_{\mathrm{shape}}
+
\beta d_{\mathrm{mag}}
+
\gamma d_{\mathrm{edge}}
+
\delta d_{\mathrm{residual}}
```

The coefficients must be calibrated.

---

# 20. INFORMATION-GEOMETRIC DISTANCES

If `p` is interpreted as a probability-like distribution, candidate distances include:

```text
Jensen-Shannon divergence
Hellinger distance
Wasserstein distance
```

These are optional.

Do not use them automatically.

The metric must match the semantics of the state.

---

# 21. KL DIVERGENCE WARNING

Kullback-Leibler divergence may be written:

```math
D_{\mathrm{KL}}(p\|q)
=
\sum_i
p_i
\log
\frac{p_i}{q_i}
```

But:

- it is not symmetric;
- it may diverge if `q_i = 0` while `p_i > 0`;
- it assumes distribution-like semantics.

Therefore it should not be the default universal distance.

---

# 22. JENSEN-SHANNON OPTION

A bounded symmetric alternative is:

```math
D_{\mathrm{JS}}(p,q)
=
\frac12
D_{\mathrm{KL}}(p\|m)
+
\frac12
D_{\mathrm{KL}}(q\|m)
```

with:

```math
m
=
\frac12(p+q)
```

This may be useful for comparing normalized local composition.

Again, only if probability-like semantics are meaningful.

---

# 23. BARYCENTRIC CENTER

The center of the standard simplex is:

```math
c
=
\left(
\frac13,
\frac13,
\frac13
\right)
```

Distance from center can indicate concentration or imbalance.

For example:

```math
d_c
=
\|p-c\|_2
```

Low `d_c`:

```text
distributed triad
```

High `d_c`:

```text
vertex-dominated triad
```

This is descriptive.

It is not automatically a stability measure.

---

# 24. TRIANGLE ENTROPY

For positive normalized `p`:

```math
H(p)
=
-\sum_{i=1}^{3}
p_i\log p_i
```

Maximum entropy occurs at:

```math
p
=
\left(
\frac13,\frac13,\frac13
\right)
```

Minimum entropy occurs near a vertex.

Possible interpretation:

```text
high entropy  -> distributed contribution
low entropy   -> concentrated contribution
```

Do not equate high entropy with "bad" or low entropy with "good."

---

# 25. DEFORMATION

A state transition can move a point inside the simplex:

```math
p_t
\longrightarrow
p_{t+1}
```

Define:

```math
\Delta p_t
=
p_{t+1}-p_t
```

The path:

```math
\gamma(t)
\in
\Delta^2
```

represents local state evolution.

This gives a geometric view of reasoning change.

---

# 26. VELOCITY IN SIMPLEX SPACE

For discrete steps:

```math
v_t
=
p_{t+1}-p_t
```

A large norm:

```math
\|v_t\|
```

means rapid local state redistribution.

This may be used as a transition signal.

---

# 27. ACCELERATION / SECOND DIFFERENCE

Define:

```math
a_t
=
v_{t+1}-v_t
```

Large second difference may indicate:

- abrupt reasoning shift;
- instability;
- branch change;
- correction;
- contradiction resolution.

This is an optional diagnostic.

---

# 28. BOUNDARY STATES

The simplex boundary occurs when one coordinate is zero.

Example:

```math
p=(0.7,0.3,0)
```

This means the third component is inactive in the normalized representation.

A vertex state:

```math
p=(1,0,0)
```

means one component dominates completely.

Boundary proximity may be useful for detecting degeneracy.

---

# 29. BOUNDARY DISTANCE

A simple boundary proximity score is:

```math
b(p)
=
\min(p_1,p_2,p_3)
```

If:

```math
b(p)\approx 0
```

the state lies near a simplex boundary.

This may indicate:

- one component is nearly absent;
- the local triad is effectively collapsing toward a lower-dimensional state.

Whether that matters depends on the task.

---

# 30. DEGENERATE TRIANGLE

If one component remains zero over time:

```text
A
B
C = 0
```

the local system may effectively reduce to a line segment.

This should be detectable.

The architecture should not force a three-way interpretation when the task only contains two active degrees of freedom.

This supports adaptive model complexity.

---

# 31. SIMPLEX DIMENSION IS NOT LAYER WIDTH

A 2-simplex has dimension 2.

It contains three barycentric coordinates constrained by one sum rule.

Therefore:

```text
3 coordinates
!=
3 independent dimensions
```

Likewise:

```text
14 nodes
```

does not mean:

```text
14-dimensional simplex
```

unless explicitly constructed that way.

This distinction must remain clear throughout the project.

---

# 32. TRIANGULAR NUMBERS ARE NOT SIMPLEX DIMENSIONS

Triangular numbers:

```math
T_n
=
\frac{n(n+1)}{2}
```

are combinatorial counts.

They should not be interpreted as automatic dimensions of nested subspaces.

For example:

```text
14 = 10 + 3 + 1
```

does not by itself imply a topological decomposition of dimensions.

Any use of such counts must be explicitly defined as architecture.

---

# 33. LOCAL CERTIFICATE

A simplex node should optionally carry a certificate:

```text
certificate
|
+-- normalization valid
+-- scale preserved
+-- constraints satisfied
+-- edge relations retained
+-- uncertainty acceptable
```

Represent abstractly:

```math
C_T
=
(c_1,c_2,\dots,c_k)
```

Later, Gate will evaluate this certificate.

---

# 34. UNCERTAINTY

Store uncertainty separately from barycentric shape.

Example:

```math
U_T
\in
[0,1]
```

Two identical simplex points can have different confidence.

Example:

```text
State A:
p = (0.6,0.3,0.1)
U = 0.05

State B:
p = (0.6,0.3,0.1)
U = 0.80
```

These states should not be treated as equivalent for commit.

---

# 35. PROVENANCE

A local simplex state should know its source.

Minimal provenance may be:

```text
source_id
parent_id
depth
timestamp / step
```

For reasoning:

```text
equation source
constraint source
tool output source
memory source
```

This supports backward audit.

---

# 36. SIMPLEX NODE SPEC

Recommended conceptual structure:

```python
SimplicialNode(
    raw=(r1, r2, r3),
    shape=(p1, p2, p3),
    magnitude=m,
    sign=(s1, s2, s3),
    edges=K,
    uncertainty=U,
    provenance=P,
    shadow=S,
    certificate=C,
    children=[...],
)
```

This is the local data contract for future implementation.

---

# 37. EXACT RECONSTRUCTION CASE

If the state stores:

```text
shape p
magnitude m
sign s
```

and no additional information was discarded, raw component magnitudes can be reconstructed as:

```math
|r_i|
=
m p_i
```

then:

```math
r_i
=
s_i m p_i
```

This is exact for the chosen representation.

However, if the original state contained richer information than three scalars, reconstruction may still be lossy.

---

# 38. LOSSY COMPRESSION CASE

Suppose each child is itself a high-dimensional object:

```math
X_i\in\mathbb{R}^{d}
```

and the parent stores only:

```text
three summary weights
```

Then exact reconstruction is generally impossible.

The lost information must appear as:

```text
Shadow
residual
external memory
or accepted loss
```

This prepares the next operators.

---

# 39. COMPRESSION QUALITY

Define:

```math
Q_{\mathrm{comp}}
=
f(
E_{\mathrm{rec}},
\rho,
E_{\mathrm{task}},
U
)
```

where:

- `E_rec` — reconstruction error;
- `rho` — compression ratio;
- `E_task` — downstream task loss;
- `U` — uncertainty.

A compression is good only if it is compact **and** preserves what the task needs.

---

# 40. RATE-DISTORTION VIEW

A useful conceptual connection is rate-distortion tradeoff.

Informally:

```text
less memory
<-> more distortion
```

The architecture should search for a useful operating point:

```text
small enough representation
+
small enough reasoning error
```

This is a more rigorous framing than "perfect compression."

---

# 41. SIMPLEX AS CONTROL SURFACE

The simplex can also serve as a control surface.

Example:

```text
near vertex A -> choose policy A
near vertex B -> choose policy B
near center   -> request more evidence
```

This is optional.

The control policy must be learned or defined separately.

The geometry alone does not determine the correct action.

---

# 42. LOCAL GATE PRECONDITION

Before a node can be promoted upward, later Gate logic may require:

```text
1. valid coordinates
2. valid scale
3. acceptable reconstruction
4. preserved critical edges
5. acceptable uncertainty
6. satisfied task constraints
```

This file defines the quantities.

The Gate itself will be formalized later.

---

# 43. MINIMAL NUMERIC EXAMPLE

Raw local state:

```math
r=(6,3,1)
```

Magnitude:

```math
m=10
```

Shape:

```math
p=(0.6,0.3,0.1)
```

Suppose reconstruction gives:

```math
\hat{r}
=
(5.9,3.0,1.1)
```

Residual:

```math
r_{\mathrm{rec}}
=
(0.1,0,-0.1)
```

A simple reconstruction error:

```math
E_{\mathrm{rec}}
=
\|r-\hat{r}\|_2
```

is:

```math
E_{\mathrm{rec}}
=
\sqrt{0.1^2+0^2+(-0.1)^2}
```

which is approximately:

```math
0.1414
```

This value, not `a+b+c=1`, tells us that reconstruction was imperfect.

---

# 44. FAILURE CONDITIONS

The simplex representation should be revised if:

1. normalization erases critical magnitude information;
2. signed values are handled ambiguously;
3. edge state is omitted when the task depends on relations;
4. uncertainty is folded into the same coordinates as semantic state;
5. reconstruction is judged only by coordinate closure;
6. metrics are chosen without matching task semantics;
7. memory cost exceeds benefit;
8. simplex geometry adds no predictive or verification value.

---

# 45. EXPERIMENT A — SHAPE VS MAGNITUDE

Construct pairs with identical shape but different magnitude.

Example:

```text
(0.6, 0.3, 0.1)
vs
(6, 3, 1)
```

Test whether the model can choose different actions when scale matters.

A normalized-only representation should fail this test.

---

# 46. EXPERIMENT B — SIGN TEST

Compare:

```text
(+6, +3, +1)
```

with:

```text
(-6, -3, -1)
```

The normalized absolute shape is identical.

A correct representation must preserve directional difference.

---

# 47. EXPERIMENT C — EDGE TEST

Use the same vertex values with different coupling matrices.

Example:

```text
State A:
same vertices
positive coupling

State B:
same vertices
negative coupling
```

The controller should distinguish them if coupling changes the outcome.

---

# 48. EXPERIMENT D — RESIDUAL TEST

Inject a missing term into one child.

Verify that:

```text
coordinate normalization still passes
```

while:

```text
reconstruction residual detects the loss
```

This directly demonstrates why simplex closure is not an integrity certificate.

---

# 49. RESEARCH STATUS

```text
FACT:
Barycentric coordinates represent points in a simplex.

FACT:
Normalization preserves relative proportions but may erase scale.

MODEL:
Store local reasoning state as shape + magnitude + sign
+ edges + uncertainty + provenance + Shadow + certificate.

HYPOTHESIS:
This state contract preserves enough local structure
to support reliable hierarchical reasoning.

TEST:
Shape/magnitude, sign, edge, residual,
reconstruction, and downstream-control experiments.
```

---

# 50. TRANSITION TO THE NEXT FILE

This file defined the mathematics of a local triangle.

The next file must focus on the part that is easiest to lose:

> the relations between nodes.

The next layer therefore formalizes **Coupling / Edge Memory**.

---

# 51. NEXT FILE

Next:

```text
06_COUPLING_EDGE_MEMORY.md
```

Its purpose is to define:

```text
node state
+
edge state
+
directed coupling
+
rate coupling
+
constraint coupling
+
edge preservation during compression
```

and to explain why some correct answers live in relations rather than in node values.

---

## FILE VERDICT

```text
STATE: CRYSTAL

DEFINED:
Barycentric Simplex Space

LOCAL STATE:
shape
+ magnitude
+ sign
+ edge state
+ uncertainty
+ provenance
+ Shadow
+ certificate

CRITICAL RULE:
a + b + c = 1
does not prove that information was preserved

NEXT:
06_COUPLING_EDGE_MEMORY.md
```
