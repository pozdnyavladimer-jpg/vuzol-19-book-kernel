# 02 — GSL 6D STATE SPACE

**Project:** Vuzol-19  
**Module:** Hexagram Simplicial Reasoning  
**Status:** STATE REPRESENTATION SPEC  
**State:** CRYSTAL  
**Language:** English  
**Depends on:** `01_PROBLEM_LLM_LONG_REASONING.md`

---

## 0. PURPOSE

The previous file defined the failure problem:

> Long reasoning can lose dependency structure, constraints, provenance, and residual information.

This file introduces the first compact state representation intended to help an AI track those changes.

The proposal is a six-axis interpretable state:

```text
R — pressure / instability
O — flow / adaptability
Y — structure
G — balance / coherence
B — law / constraints
V — future / transition potential
```

This is called the **GSL 6D State Space**.

The six axes are not assumed to be optimal.

They are a **testable state vocabulary**.

---

# 1. WHY A SMALL STATE SPACE IS USEFUL

A transformer hidden state may have hundreds or thousands of dimensions.

That representation is powerful, but difficult to inspect directly.

We therefore introduce a projection:

```math
\phi :
\mathbb{R}^{d}
\longrightarrow
\mathbb{R}^{6}
```

with:

```math
z
=
(R,O,Y,G,B,V)
```

where `z` is not intended to replace the full hidden state.

It acts as:

- a diagnostic projection;
- a routing signal;
- a transition summary;
- a Gate input;
- a memory index;
- an interpretable audit layer.

---

# 2. CORE PRINCIPLE

The 6D state should answer:

```text
What is happening to the system?
```

not only:

```text
What words are present?
```

The representation should therefore describe system behavior rather than lexical surface form.

Example:

```text
"The project is collapsing under unresolved failures."
```

and:

```text
"Accumulated defects are causing the system to lose stability."
```

should ideally produce similar state vectors even though the wording differs.

---

# 3. AXIS R — PRESSURE / INSTABILITY

`R` measures destabilizing pressure.

Possible signals include:

- contradiction;
- failure;
- overload;
- unresolved conflict;
- instability;
- resource shortage;
- increasing uncertainty;
- violation pressure;
- approaching boundary conditions.

Conceptually:

```text
low R  -> stable / low pressure
high R -> unstable / constrained / near failure
```

Example:

```text
"The loop never terminates."
```

may increase `R`.

Important:

`R` is not "negative emotion."

It is a system-level pressure coordinate.

---

# 4. AXIS O — FLOW / ADAPTABILITY

`O` measures motion through state space.

Possible signals include:

- adaptation;
- retry;
- exploration;
- transition;
- movement;
- search;
- reconfiguration;
- recovery;
- alternative path selection.

Conceptually:

```text
low O  -> static / stuck / rigid
high O -> active transition / adaptation
```

Example:

```text
"The agent retries using a different route."
```

may increase `O`.

---

# 5. AXIS Y — STRUCTURE

`Y` measures explicit organization.

Possible signals include:

- decomposition;
- hierarchy;
- plan;
- graph;
- sequence;
- typed structure;
- modularity;
- defined roles;
- explicit intermediate states.

Conceptually:

```text
low Y  -> weak organization
high Y -> explicit architecture / structure
```

Example:

```text
"First validate the input, then compute the dependency graph."
```

may increase `Y`.

---

# 6. AXIS G — BALANCE / COHERENCE

`G` measures whether active parts of the system remain mutually consistent.

Possible signals include:

- conservation;
- compatibility;
- agreement;
- stability;
- reconciliation;
- closure;
- consistency;
- successful constraint satisfaction.

Conceptually:

```text
low G  -> unresolved mismatch
high G -> coherent / mutually compatible state
```

Example:

```text
"Both conservation constraints are satisfied."
```

may increase `G`.

---

# 7. AXIS B — LAW / CONSTRAINTS

`B` measures the role of explicit rules and invariants.

Possible signals include:

- equations;
- formal constraints;
- type rules;
- logical conditions;
- conservation laws;
- protocol checks;
- validation rules;
- allowed / forbidden transitions.

Conceptually:

```text
low B  -> weakly constrained state
high B -> strongly rule-governed state
```

Example:

```text
"The result must satisfy x > 0 and preserve total mass."
```

may increase `B`.

---

# 8. AXIS V — FUTURE / TRANSITION POTENTIAL

`V` measures how strongly the current state points toward a future transition.

Possible signals include:

- unresolved next step;
- target state;
- potential;
- branch opening;
- planned transformation;
- opportunity;
- pending decision;
- future commitment.

Conceptually:

```text
low V  -> terminal / settled state
high V -> strong transition potential
```

Example:

```text
"The current state opens two possible next routes."
```

may increase `V`.

---

# 9. VECTOR FORM

The simplest representation is:

```math
z
=
(R,O,Y,G,B,V)
```

A bounded implementation may use:

```math
R,O,Y,G,B,V \in [0,1]
```

However, this does **not** require:

```math
R+O+Y+G+B+V=1
```

unless the six dimensions are explicitly treated as competing proportions.

Default recommendation:

> Treat the six axes as independent bounded features, not as a probability simplex.

Reason:

A state may simultaneously have:

```text
high pressure
high structure
high law
high future potential
```

without forcing one axis to reduce another.

---

# 10. OPTIONAL NORMALIZED VIEW

For some visualizations, a normalized view may be useful.

Given raw positive scores:

```math
s_i \ge 0
```

define:

```math
p_i
=
\frac{s_i}{
\sum_{j=1}^{6}s_j
}
```

Then:

```math
\sum_{i=1}^{6}p_i=1
```

This normalized representation is useful for:

- relative composition;
- visualization;
- comparison of dominant modes.

But it should not replace the raw feature values.

---

# 11. FLAT STATE VS STRUCTURED STATE

A flat 6D vector is:

```text
[0.70, 0.40, 0.80, 0.30, 0.90, 0.60]
```

This is compact.

But it does not explain:

- why `R = 0.70`;
- which constraints caused `B = 0.90`;
- which earlier state produced `V = 0.60`.

Therefore the 6D vector is only the **outer state shell**.

Later files will add:

```text
axis
 |
 +-- internal decomposition
 +-- provenance
 +-- coupling
 +-- Shadow
```

---

# 12. TRANSITION FORM

The important object is not only the state `z_t`.

It is the transition:

```math
z_t
\longrightarrow
z_{t+1}
```

Define a state delta:

```math
\Delta z_t
=
z_{t+1}-z_t
```

This tells us which axes changed.

Example:

```text
R: 0.80 -> 0.40
O: 0.20 -> 0.70
Y: 0.30 -> 0.60
G: 0.20 -> 0.65
B: 0.90 -> 0.90
V: 0.70 -> 0.50
```

Interpretation:

```text
pressure decreased
flow increased
structure increased
balance improved
constraints stayed active
future uncertainty decreased
```

This is closer to a reasoning trajectory than a static embedding.

---

# 13. STATE TRAJECTORY

For a long reasoning process:

```math
\mathcal{Z}
=
(z_1,z_2,\dots,z_T)
```

The AI can track:

- stable regions;
- sudden transitions;
- oscillations;
- unresolved pressure;
- repeated constraint violations;
- transition bottlenecks.

A long task becomes:

```text
state
  |
  v
state
  |
  v
state
  |
  v
state
```

instead of only:

```text
token
  |
  v
token
  |
  v
token
```

---

# 14. MINIMAL TRANSITION EXAMPLE

Input:

```text
"The system fails validation, retries with a new rule,
and reaches a consistent state."
```

Possible illustrative trajectory:

```text
Step 1:
R high
O low
Y medium
G low
B high
V high

Step 2:
R medium
O high
Y medium
G medium
B high
V high

Step 3:
R low
O medium
Y high
G high
B high
V low
```

The point is not the exact numbers.

The point is that the representation captures the **shape of the transition**.

---

# 15. FIRST IMPLEMENTATION — RULE-BASED

The simplest prototype may use hand-written rules.

Example:

```python
if "fail" in text:
    R += 0.3

if "retry" in text:
    O += 0.3

if "plan" in text:
    Y += 0.3

if "consistent" in text:
    G += 0.3

if "must" in text:
    B += 0.3

if "next" in text:
    V += 0.3
```

This is useful only as a bootstrap prototype.

It is not sufficient for serious semantic reasoning.

---

# 16. WHY KEYWORDS ARE NOT ENOUGH

A keyword encoder can fail on paraphrases.

Example:

```text
"The project collapsed."
```

and:

```text
"The system entered a severe failure state."
```

may express similar pressure.

But a keyword-only system may score them differently.

It can also fail on negation:

```text
"The system did not fail."
```

A naive keyword rule may still increase `R`.

Therefore the long-term encoder should infer semantics, not only words.

---

# 17. LEARNED PROJECTION

A stronger model is:

```math
z
=
\phi_{\theta}(h)
```

where:

- `h` is an LLM hidden representation or embedding;
- `phi_theta` is a learned projection;
- `z` is the six-axis interpretable state.

Possible implementations:

- linear probe;
- small MLP;
- contrastive encoder;
- supervised state predictor;
- multi-task probe.

The six axes should be independently evaluated.

---

# 18. SUPERVISION TARGETS

A dataset may label examples for:

```text
pressure
flow
structure
balance
law
future
```

Each label may be:

- binary;
- ordinal;
- continuous;
- pairwise preference.

Example:

```text
Text A has more structural organization than Text B.
```

This can train the `Y` axis.

---

# 19. CROSS-DOMAIN TEST

The six axes are intended as a cross-domain state vocabulary.

Candidate domains:

```text
natural language
code
mathematical reasoning
scientific procedures
planning
system logs
agent trajectories
```

The hypothesis is useful only if axis meanings remain reasonably stable across domains.

---

# 20. PARAPHRASE STABILITY TEST

**TEST**

Create semantic-equivalent pairs:

```text
A: "The solver retries after a failed validation."
B: "After validation fails, the solver makes another attempt."
```

Measure:

```math
d(
z_A,
z_B
)
```

Desired:

```math
d(
z_A,
z_B
)
\le
\tau_{\mathrm{para}}
```

If paraphrases produce very different state vectors, the representation is unstable.

---

# 21. CONTRADICTION SENSITIVITY TEST

**TEST**

Compare:

```text
A: "The system is stable."
B: "The system is not stable."
```

The representation should not collapse them into nearly identical states.

Expected difference:

```text
R
G
possibly V
```

should shift measurably.

---

# 22. CAUSAL ORDER TEST

Compare:

```text
A:
failure -> retry -> recovery
```

with:

```text
B:
recovery -> retry -> failure
```

The same words appear.

The order differs.

A good state-transition encoder should produce different trajectories:

```math
\mathcal{Z}_A
\ne
\mathcal{Z}_B
```

This is critical.

Otherwise the model is only a bag of semantic signals.

---

# 23. AXIS INDEPENDENCE TEST

The six axes must not collapse into one general "good / bad" score.

Example:

```text
high R + high Y + high B
```

should be possible.

A heavily constrained but well-structured crisis state may have:

```text
R = high
Y = high
B = high
G = low
```

If all axes become strongly correlated, the 6D design is not adding meaningful structure.

---

# 24. DISENTANGLEMENT METRIC

Let the learned axes form matrix:

```math
Z
\in
\mathbb{R}^{N\times 6}
```

Compute correlations between dimensions.

A simple warning condition is:

```math
|\mathrm{corr}(z_i,z_j)|
>
\tau_{\mathrm{corr}}
```

for many pairs.

This does not prove failure, but it signals that multiple axes may be redundant.

---

# 25. PREDICTIVE VALUE TEST

The six-axis representation should help predict something useful.

Examples:

- next reasoning state;
- probability of constraint failure;
- need for recomputation;
- whether a branch will terminate;
- whether the final answer will be wrong.

Given:

```math
z_t
```

predict:

```math
y_{t+1}
```

If `z_t` has no predictive value beyond a standard embedding, it is only a visualization.

---

# 26. INFORMATION LOSS TEST

Because the 6D projection is a strong bottleneck, it necessarily loses information.

The question is not:

```text
Does it lose information?
```

It does.

The useful question is:

```text
Does it preserve the information needed
for reasoning control and verification?
```

Therefore compare:

```text
full embedding
vs
6D state
vs
6D state + hierarchical provenance
```

on downstream tasks.

---

# 27. 64-STATE DISCRETIZATION

Optional hypothesis:

If each axis is converted into a binary state:

```math
b_i
=
\mathbf{1}[z_i>\tau_i]
```

then:

```math
H
=
(b_R,b_O,b_Y,b_G,b_B,b_V)
```

There are:

```math
2^6=64
```

possible discrete states.

This may provide a compact symbolic codebook.

Important:

> The fact that `2^6 = 64` does not by itself establish a historical or causal relation to any traditional 64-symbol system.

This remains a separate hypothesis.

---

# 28. MULTI-LEVEL DISCRETIZATION

Binary states may be too coarse.

An alternative is three levels per axis:

```text
LOW
MEDIUM
HIGH
```

giving:

```math
3^6=729
```

possible combinations.

Or keep the vector continuous and only discretize when a Gate requires a symbolic state.

---

# 29. STATE CONFIDENCE

Every axis should optionally include confidence:

```math
z_i
=
(v_i,c_i)
```

where:

- `v_i` — estimated state value;
- `c_i` — confidence.

Example:

```text
Pressure:
value      = 0.80
confidence = 0.95

Future:
value      = 0.55
confidence = 0.30
```

Low confidence can later trigger:

```text
HOLD
EXPAND
RECOMPUTE
```

---

# 30. FROM 6D TO HIERARCHY

This file defines only the outer state:

```text
R O Y G B V
```

The next architecture step is to group the six dimensions geometrically:

```text
FORM triangle
FLOW triangle
```

Then each axis can itself be recursively decomposed.

The intended progression is:

```text
flat 6D
   |
   v
two interacting triangles
   |
   v
recursive sub-triangles
   |
   v
provenance + coupling + Shadow
```

---

# 31. FAILURE CONDITIONS

The 6D state model should be revised or rejected if:

1. paraphrases produce unstable states;
2. negation is handled poorly;
3. axes collapse into a single sentiment-like dimension;
4. the projection has no predictive value;
5. standard embeddings outperform it on every control task;
6. domain transfer fails;
7. the six axes cannot be independently labeled with reasonable agreement;
8. hierarchical provenance adds no value beyond the flat vector.

---

# 32. RESEARCH STATUS

```text
FACT:
LLMs use high-dimensional internal representations.

MODEL:
Project those representations into six interpretable axes.

HYPOTHESIS:
These six axes preserve useful reasoning-state information.

TEST:
Measure robustness, disentanglement, predictive value,
cross-domain stability, and downstream control performance.
```

---

# 33. NEXT FILE

Next:

```text
03_HEXAGRAM_STATE_MODEL.md
```

Its purpose is to define how the six state axes are arranged into two interacting triangles:

```text
FORM
and
FLOW
```

and to explain what geometric structure adds beyond a flat six-dimensional vector.

---

## FILE VERDICT

```text
STATE: CRYSTAL

DEFINED:
GSL 6D State Space

STATE:
(R, O, Y, G, B, V)

ROLE:
interpretable projection,
transition tracker,
audit signal,
memory index,
Gate input

NOT CLAIMED:
the six axes are universally optimal

NEXT:
03_HEXAGRAM_STATE_MODEL.md
```
