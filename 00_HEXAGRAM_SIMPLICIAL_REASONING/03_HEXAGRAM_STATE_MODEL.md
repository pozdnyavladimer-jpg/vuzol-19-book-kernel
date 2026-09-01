# 03 — HEXAGRAM STATE MODEL

**Project:** Vuzol-19  
**Module:** Hexagram Simplicial Reasoning  
**Status:** GEOMETRIC STATE ORGANIZATION SPEC  
**State:** CRYSTAL  
**Language:** English  
**Depends on:** `02_GSL_6D_STATE_SPACE.md`

---

## 0. PURPOSE

The previous file defined a six-axis interpretable state:

```text
R — pressure / instability
O — flow / adaptability
Y — structure
G — balance / coherence
B — law / constraints
V — future / transition potential
```

This file asks a new question:

> Does arranging the six axes into two interacting triangles add useful structure beyond a flat 6D vector?

The proposed organization is called the **Hexagram State Model**.

It is a **MODEL** and must be tested against the flat 6D baseline.

---

# 1. FROM FLAT 6D TO TWO TRIANGLES

The flat state is:

```math
z=(R,O,Y,G,B,V)
```

The proposed grouping is:

```text
FORM TRIANGLE
Y — Structure
B — Law
V — Future

FLOW TRIANGLE
R — Pressure
O — Flow
G — Balance
```

Define:

```math
F=(Y,B,V)
```

and:

```math
Q=(R,O,G)
```

The complete state is still the same six-dimensional information:

```math
z=(F,Q)
```

The geometry does not create new information by itself.

Its purpose is to impose an interpretable organization on the six dimensions.

---

# 2. WHY TWO TRIANGLES

The proposed distinction is:

```text
FORM
=
what organizes or constrains the state

FLOW
=
what moves, stresses, or stabilizes the state
```

More explicitly:

```text
FORM:
Structure
Law
Future

FLOW:
Pressure
Motion
Balance
```

This gives two complementary questions.

### FORM asks:

```text
What shape is the system trying to maintain or reach?
```

### FLOW asks:

```text
What is happening to the system while it moves toward or away from that shape?
```

---

# 3. BASIC HEXAGRAM VIEW

A simple ASCII representation is:

```text
                    FORM

                 V / Future
                  /       \
                 /         \
                /           \
       Y / Structure ----- B / Law


                    FLOW

              G / Balance
                \         /
                 \       /
                  \     /
        R / Pressure --- O / Flow
```

The two triangles should be interpreted as **interacting subsystems**, not as decorative symbols.

---

# 4. WHAT GEOMETRY MAY ADD

A flat vector contains:

```text
six values
```

The Hexagram representation explicitly adds three types of organization:

```text
1. intra-triangle relations
2. inter-triangle relations
3. center / commit relation
```

This produces:

```text
nodes
+
edges
+
higher-order local structure
```

The hypothesis is that some reasoning failures occur because the model preserves node values but loses relations.

---

# 5. INTRA-TRIANGLE EDGES

Inside the FORM triangle:

```text
Y <-> B
B <-> V
V <-> Y
```

Possible interpretations:

```text
Structure <-> Law
Law       <-> Future
Future    <-> Structure
```

Inside the FLOW triangle:

```text
R <-> O
O <-> G
G <-> R
```

Possible interpretations:

```text
Pressure <-> Flow
Flow     <-> Balance
Balance  <-> Pressure
```

These relations should be represented explicitly if they matter to the task.

---

# 6. INTER-TRIANGLE COUPLINGS

The two triangles also interact.

In the general case, every FORM axis may couple to every FLOW axis.

Define a coupling matrix:

```math
K
\in
\mathbb{R}^{3\times 3}
```

with:

```math
K=
\begin{bmatrix}
k_{YR} & k_{YO} & k_{YG} \\
k_{BR} & k_{BO} & k_{BG} \\
k_{VR} & k_{VO} & k_{VG}
\end{bmatrix}
```

Examples:

- `k_YR` — how pressure affects structure;
- `k_BO` — how flow interacts with rules;
- `k_VG` — how future transition potential interacts with present balance.

The exact meaning of each coupling must be defined by the task or learned from data.

---

# 7. DEFAULT PAIRINGS ARE NOT UNIVERSAL

A visualization may choose three visually opposite pairs, for example:

```text
Structure <-> Pressure
Law       <-> Flow
Future    <-> Balance
```

But this is only a **display convention** unless experiments justify those pairings.

The full model should allow all pairwise interactions through `K`.

This prevents a visual layout from being mistaken for a universal law.

---

# 8. RAW STATE MUST BE PRESERVED

The Hexagram layer must not destroy the original six-axis values.

Store:

```math
H_{\mathrm{raw}}
=
(R,O,Y,G,B,V)
```

and optionally add:

```math
K
```

for coupling information.

A minimal Hexagram state is therefore:

```math
H
=
(z,K)
```

where:

- `z` contains the six node values;
- `K` contains inter-triangle relations.

---

# 9. OPTIONAL TRIANGLE NORMALIZATION

For visualization only, each triangle may be normalized separately.

For FORM:

```math
\tilde{F}
=
\frac{
(Y,B,V)
}{
Y+B+V
}
```

if the denominator is positive.

For FLOW:

```math
\tilde{Q}
=
\frac{
(R,O,G)
}{
R+O+G
}
```

This produces barycentric coordinates for drawing points inside two triangles.

However:

> The normalized coordinates must not replace the raw values.

Reason:

```text
F = (0.9, 0.9, 0.9)
```

and:

```text
F = (0.1, 0.1, 0.1)
```

have the same normalized composition but very different absolute intensity.

Therefore retain both:

```text
raw magnitude
+
normalized shape
```

---

# 10. MAGNITUDE AND SHAPE

For each triangle define a magnitude.

FORM magnitude:

```math
m_F
=
Y+B+V
```

FLOW magnitude:

```math
m_Q
=
R+O+G
```

Then preserve:

```text
triangle shape
+
triangle magnitude
```

The state becomes:

```math
H
=
(\tilde{F},m_F,\tilde{Q},m_Q,K)
```

This separates:

```text
how the triangle is internally distributed
```

from:

```text
how strongly that triangle is activated
```

---

# 11. TRIANGLE INTERNAL BALANCE

A triangle with equal coordinates has a different shape from one dominated by a single vertex.

A simple imbalance measure for a normalized triangle `p` is:

```math
I(p)
=
\sum_{i=1}^{3}
\left|
p_i-\frac{1}{3}
\right|
```

Low `I` means a relatively even triangle.

High `I` means one or two vertices dominate.

This is a descriptive metric only.

It does not imply that a balanced triangle is always better.

---

# 12. ENTROPY VIEW

For normalized positive coordinates, triangle entropy may be defined as:

```math
S(p)
=
-\sum_{i=1}^{3}
p_i \log p_i
```

Interpretation:

```text
high entropy
=
distributed activation

low entropy
=
concentrated activation
```

This may help detect whether a state is:

- diffuse;
- specialized;
- dominated by one role.

Again, this is a **measurement**, not a normative rule.

---

# 13. FORM-FLOW RELATION

The Hexagram model should not assume that FORM and FLOW must be equal.

Instead, define a relation function:

```math
C_{FQ}
=
g(F,Q,K)
```

where `g` may be:

- hand-defined for a simple prototype;
- learned from task data;
- computed from constraint satisfaction;
- derived from graph structure.

The important point is:

> FORM and FLOW should be compared through explicit relations, not through visual intuition alone.

---

# 14. EXAMPLE: SOFTWARE FAILURE

Consider:

```text
"The service is under heavy load.
A retry mechanism is active.
The architecture is well defined.
Validation rules remain strict.
The system is not yet stable.
A recovery route is available."
```

Illustrative state:

```text
R = 0.85
O = 0.75
Y = 0.80
G = 0.25
B = 0.90
V = 0.70
```

Flat interpretation:

```text
six high/low values
```

Hexagram interpretation:

```text
FORM:
strong structure
strong law
strong future route

FLOW:
high pressure
high movement
low balance
```

The useful observation is not simply:

```text
"the state is bad"
```

but:

> the system has a strong FORM layer while the FLOW layer remains unstable.

That distinction can be useful for control.

---

# 15. EXAMPLE: SAME PRESSURE, DIFFERENT FORM

State A:

```text
R = 0.80
O = 0.20
Y = 0.20
G = 0.20
B = 0.20
V = 0.20
```

State B:

```text
R = 0.80
O = 0.20
Y = 0.90
G = 0.20
B = 0.90
V = 0.80
```

Both have the same pressure.

But:

```text
State A:
high pressure + weak FORM

State B:
high pressure + strong FORM
```

A controller may reasonably choose different actions.

For example:

```text
State A -> EXPAND / SEARCH
State B -> HOLD / APPLY STRUCTURED RECOVERY
```

This illustrates why one scalar pressure score is insufficient.

---

# 16. TRANSITION THROUGH THE HEXAGRAM

At time `t`:

```math
H_t
=
(z_t,K_t)
```

At the next reasoning step:

```math
H_{t+1}
=
(z_{t+1},K_{t+1})
```

The transition is:

```math
\Delta H_t
=
H_{t+1}-H_t
```

Operationally, track:

```text
node changes
+
coupling changes
```

A transition may be important even when node values barely change but edge relationships change strongly.

---

# 17. EDGE-FIRST CHANGE

Example:

```text
R = 0.7
O = 0.7
```

at both `t` and `t+1`.

But:

```text
t:
pressure blocks flow

t+1:
pressure drives adaptive flow
```

The node values are unchanged.

The coupling changed.

Therefore:

```math
z_t \approx z_{t+1}
```

while:

```math
K_t \ne K_{t+1}
```

This is one of the main reasons to introduce explicit edge memory.

---

# 18. CENTER STATE

The visual center of the Hexagram is reserved for a later commit mechanism called **Bindu**.

At this stage, the center should not be treated as an additional seventh semantic axis.

Instead, it represents:

```text
the result of evaluating
the complete six-axis state
and its relations
```

Conceptually:

```math
c
=
\Gamma(z,K)
```

where `Gamma` is a future Gate / commit function.

The center is therefore derived from the state.

It is not an independent primitive.

---

# 19. HEXAGRAM AS A LOCAL STATE CONTAINER

A minimal local reasoning object may be:

```text
HexagramState
|
+-- six axis values
|
+-- FORM triangle
|
+-- FLOW triangle
|
+-- intra-triangle edges
|
+-- inter-triangle coupling matrix
|
+-- uncertainty
|
+-- provenance pointer
```

Possible abstract structure:

```python
HexagramState(
    axes=z,
    form=(Y, B, V),
    flow=(R, O, G),
    coupling=K,
    uncertainty=u,
    provenance=source_id,
)
```

This is only an interface specification.

---

# 20. WHAT THE HEXAGRAM DOES NOT YET SOLVE

The Hexagram model alone does not solve:

- long-term provenance;
- recursive decomposition;
- information loss during compression;
- local reconstruction;
- Shadow memory;
- Gate validation;
- long-chain complexity.

It only organizes the outer six-axis state and makes relations explicit.

The next layers are needed for reasoning memory.

---

# 21. FLAT 6D VS HEXAGRAM TEST

**TEST**

Compare:

```text
A — flat 6D vector z
B — z grouped into FORM/FLOW only
C — z + explicit coupling matrix K
```

Use the same downstream predictor or controller.

Measure:

- next-state prediction;
- error prediction;
- constraint violation detection;
- branch selection;
- long-reasoning accuracy.

If `C` does not outperform `A`, explicit geometric coupling may not be useful.

---

# 22. COUPLING ABLATION

Train or evaluate the same system with:

```text
full K
```

versus:

```text
K = 0
```

If performance does not change, edge memory may be unnecessary for that task.

This is important because the architecture should not retain extra structure without measurable benefit.

---

# 23. TRIANGLE GROUPING ABLATION

Compare the proposed grouping:

```text
FORM = (Y,B,V)
FLOW = (R,O,G)
```

against random or alternative groupings.

Examples:

```text
(Y,R,V) / (B,O,G)
```

or:

```text
learned grouping
```

If random groupings perform equally well, the FORM/FLOW interpretation is not empirically privileged.

---

# 24. ROTATION / PERMUTATION TEST

A geometry can accidentally benefit from implementation details rather than semantic meaning.

Therefore permute axis positions while keeping the same values.

If performance changes only because of display order or parameter indexing, the model may be learning artifacts.

A robust implementation should separate:

```text
semantic identity
```

from:

```text
visual position
```

---

# 25. CROSS-DOMAIN HEXAGRAM TEST

Apply the same state definition to:

```text
natural language reasoning
mathematical derivations
code execution traces
planning tasks
system logs
```

The hypothesis is:

> FORM/FLOW roles remain interpretable across domains even if the encoder changes.

If the grouping works only in one narrow domain, it should be treated as domain-specific.

---

# 26. FAILURE CONDITIONS

The Hexagram State Model should be revised or rejected if:

1. grouping adds no predictive value over flat 6D;
2. explicit couplings add no measurable value;
3. the FORM/FLOW split is unstable across domains;
4. random axis groupings perform equally well;
5. normalization destroys useful magnitude information;
6. the geometry creates artificial correlations;
7. the center is treated as valid before Gate verification;
8. the representation becomes more expensive without improving control or reasoning.

---

# 27. RESEARCH STATUS

```text
FACT:
A six-dimensional state can be partitioned into two triples.
Pairwise relations can be represented explicitly.

MODEL:
FORM = (Y, B, V)
FLOW = (R, O, G)

MODEL:
Use a coupling matrix K between the two triangles.

HYPOTHESIS:
This organization improves reasoning control
relative to a flat 6D representation.

TEST:
Compare flat 6D, grouped 6D, and grouped 6D + coupling
under matched compute.
```

---

# 28. TRANSITION TO RECURSIVE GEOMETRY

The Hexagram currently contains six outer nodes.

The next step is to ask:

```text
Where did each axis value come from?
```

Instead of:

```text
R = 0.73
```

represent:

```text
R
|
+-- source A
+-- source B
+-- coupling / uncertainty
```

and allow each source to decompose again.

This leads to:

> **triangles inside triangles**

and to a hierarchical simplex memory.

---

# 29. NEXT FILE

Next:

```text
04_TRIANGLES_INSIDE_TRIANGLES.md
```

Its purpose is to formalize recursive decomposition:

```text
outer axis
   |
   v
local triad
   |
   v
sub-triads
   |
   v
hierarchical provenance
```

and to show how two equal outer values can retain different internal histories.

---

## FILE VERDICT

```text
STATE: CRYSTAL

DEFINED:
Hexagram State Model

FORM:
(Y, B, V)

FLOW:
(R, O, G)

ADDED:
explicit intra-triangle relations
explicit inter-triangle coupling matrix K
raw magnitude + normalized shape
derived center / future Bindu interface

NOT CLAIMED:
the geometry is universal
the proposed grouping is optimal

NEXT:
04_TRIANGLES_INSIDE_TRIANGLES.md
```
