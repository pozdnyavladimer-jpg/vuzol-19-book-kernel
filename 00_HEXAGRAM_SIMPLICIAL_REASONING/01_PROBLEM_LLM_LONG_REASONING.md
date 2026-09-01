# 01 — PROBLEM: LLM LONG-REASONING DEGRADATION

**Project:** Vuzol-19  
**Module:** Hexagram Simplicial Reasoning  
**Status:** PROBLEM DEFINITION  
**State:** CRYSTAL  
**Language:** English  
**Depends on:** `00_BOOT_HEXAGRAM_SIMPLICIAL_REASONING.md`

---

## 0. PURPOSE

This file defines the problem that the architecture is intended to solve.

It intentionally does **not** use:

- Sri Yantra geometry;
- the `14 -> 10 -> 10 -> 8` funnel;
- sacred geometry as an explanation;
- claims about universal physical laws.

The goal is to isolate the AI failure first.

Only after the failure is clearly defined should a geometric architecture be tested against it.

---

# 1. CORE CLAIM

A language model may correctly solve many local steps and still fail on the complete problem.

The failure is often not:

```text
"the model knows nothing"
```

but rather:

```text
the model loses or corrupts
the structure connecting correct local states
```

The proposed research problem is therefore:

> **How can an AI preserve, verify, and reconstruct long chains of dependent reasoning without allowing local errors or lost relations to silently propagate into the final answer?**

---

# 2. LONG CONTEXT IS NOT THE SAME AS LONG REASONING

A model can have access to a very long input sequence.

That does not guarantee that it can reliably preserve:

- which fact depends on which earlier fact;
- which variable was derived from which condition;
- which edge in the reasoning graph remains active;
- which assumptions are still valid;
- which intermediate result was approximate;
- which branch was rejected;
- which constraint must be checked again before commit.

This distinction can be written as:

```text
context capacity
        !=
dependency integrity
```

A model may still "see" an earlier statement while failing to use it correctly.

---

# 3. REASONING AS A DEPENDENCY GRAPH

Instead of viewing reasoning only as a token sequence:

```text
t1 -> t2 -> t3 -> ... -> tN
```

represent the task as a computational or semantic dependency graph:

```text
X1 ----\
        \
         -> X4 ----\
        /           \
X2 ----/             -> X7
                    /
X3 ------> X5 -----/
```

Each node may contain:

- a value;
- a proposition;
- a partial conclusion;
- a variable;
- a transformation;
- a hypothesis.

Each edge may contain:

- causality;
- dependence;
- a constraint;
- a rate relationship;
- a transformation rule;
- a confidence relation.

---

# 4. FAILURE TYPE A — NODE RETENTION WITHOUT EDGE RETENTION

A model may preserve two facts while losing the relation between them.

Example:

```text
A is true.
B is true.
```

But the task depends on:

```text
A changes B through relation R.
```

If `R` disappears, both node values can remain correct while the final reasoning becomes wrong.

This gives the distinction:

```text
node memory
vs
edge memory
```

The architecture must therefore preserve both.

---

# 5. FAILURE TYPE B — PREMATURE COMPRESSION

Suppose a long reasoning sequence is repeatedly summarized.

A useful detail may be compressed away because it appears locally insignificant.

Example:

```text
large dominant term
+
very small residual term
```

If the residual term is removed too early, the final answer may become:

- numerically close but mathematically wrong;
- logically incomplete;
- invalid under a boundary condition.

The core problem is:

> **Compression can erase information whose importance becomes visible only later.**

This motivates a separate residual channel rather than silent deletion.

---

# 6. FAILURE TYPE C — CONSTRAINT DRIFT

A task begins with a condition:

```text
X must remain positive.
```

After many steps, the model may continue reasoning from a state that violates the original condition.

This is constraint drift.

Formally, if state $x_k$ must satisfy a constraint set $\mathcal{C}$:

```math
x_k \in \mathcal{C}
```

the model should not silently promote a state with:

```math
x_k \notin \mathcal{C}
```

to the next reasoning level.

A verification architecture should therefore check constraints locally.

---

# 7. FAILURE TYPE D — ERROR PROPAGATION

Consider a sequence of state transformations:

```math
x_{k+1}=F_k(x_k)
```

A local error $\delta x_k$ can affect later states.

For small perturbations, first-order propagation is approximately:

```math
\delta x_N
\approx
J_{N-1}J_{N-2}\cdots J_k\,\delta x_k
```

where $J_i$ is the local Jacobian of transformation $F_i$.

The important point is not that error always grows exponentially.

The important point is:

> **An undetected local error can travel through many later transformations before it is noticed.**

A local verification mechanism should try to stop that propagation early.

---

# 8. FAILURE TYPE E — FORWARD / BACKWARD ASYMMETRY

Some reasoning is easy in the forward direction:

```text
A -> B -> C
```

but difficult in reverse:

```text
C -> ? -> A
```

A system may correctly generate a conclusion while being unable to reconstruct:

- the conditions that produced it;
- the intermediate states;
- the exact branch that was taken.

This creates a useful diagnostic question:

> **Can the system reconstruct the reasoning state that produced the compressed result?**

If not, the representation may be too lossy.

---

# 9. FAILURE TYPE F — EQUIFINALITY

Different histories may produce the same outer score.

Example:

```text
State A -> final pressure = 0.73
State B -> final pressure = 0.73
```

The outer value is equal, but the causal histories are not.

A flat representation sees:

```text
0.73 == 0.73
```

A provenance-aware representation should retain the difference.

Therefore the problem is not only state estimation.

It is also:

> **history-sensitive state representation.**

---

# 10. FAILURE TYPE G — ACTIVE MEMORY OVERLOAD

Suppose a task requires hundreds of dependent operations.

A purely sequential trace may require the model to maintain too many unresolved dependencies simultaneously.

Conceptually:

```text
X1 -> X2 -> X3 -> ... -> X100
```

with many open references:

```text
remember X7
remember condition from X13
compare against X28
reuse X41
do not violate constraint from X52
```

The research question becomes:

> Can the dependency graph be reorganized into locally closed units so that fewer unresolved relationships must remain active at once?

This is the motivation for hierarchical reasoning.

---

# 11. FAILURE TYPE H — CONFIDENT INVALID COMMIT

A language model can produce a fluent answer before all dependencies have been checked.

This can be represented as:

```text
candidate answer
      |
      v
language confidence
      |
      v
commit
```

The proposed architecture changes this into:

```text
candidate answer
      |
      v
verification state
      |
      v
commit permission
```

The central distinction is:

```text
confidence
!=
validity
```

---

# 12. WHAT THE METHOD MUST PRESERVE

Any proposed solution should preserve at least five classes of information.

## 12.1 Node state

```text
What is currently believed or computed?
```

## 12.2 Edge state

```text
How are two nodes related?
```

## 12.3 Constraints

```text
What must remain true?
```

## 12.4 Provenance

```text
Where did this state come from?
```

## 12.5 Residual uncertainty

```text
What was not safely compressed or resolved?
```

These form the minimum integrity set:

```text
STATE
+
RELATION
+
CONSTRAINT
+
PROVENANCE
+
RESIDUAL
```

---

# 13. WHAT COUNTS AS SUCCESS

The architecture should not be judged by how elegant the geometry looks.

It should be judged by measurable outcomes.

A successful method should improve one or more of the following:

- exact-answer accuracy;
- constraint preservation;
- edge retention;
- reverse reconstruction;
- long-chain stability;
- error localization;
- uncertainty calibration;
- memory efficiency;
- recovery after injected local errors.

---

# 14. PRIMARY METRIC: FAILURE DEPTH

Let task difficulty increase with dependency length $N$.

Let model accuracy be:

```math
A(N)
```

Define $N_{50}$ as the problem scale where accuracy falls below 50%.

The method is useful if, under comparable compute:

```math
N_{50}^{\mathrm{method}}
>
N_{50}^{\mathrm{baseline}}
```

This is one of the cleanest measurable targets for the project.

---

# 15. SECONDARY METRIC: EDGE RETENTION

Let the ground-truth reasoning graph have edge set $E^\*$.

Let the system preserve or reconstruct edge set $\hat{E}$.

A simple edge retention score is:

```math
R_{\mathrm{edge}}
=
\frac{
|E^\* \cap \hat{E}|
}{
|E^\*|
}
```

A reasoning system may have good node values but poor edge retention.

This metric measures the missing dimension.

---

# 16. SECONDARY METRIC: LOCALIZATION OF ERROR

Inject an error into one internal node.

Measure:

```text
Where is the first point at which the system detects it?
```

Desired behavior:

```text
local error
   |
   v
local detection
   |
   v
local recomputation
```

Undesired behavior:

```text
local error
   |
   v
propagation through many levels
   |
   v
wrong final answer
```

---

# 17. SECONDARY METRIC: RECONSTRUCTION QUALITY

If a compressed parent state represents child states $X$, reconstruct:

```math
\hat{X}=R(P)
```

and measure:

```math
E_{\mathrm{rec}}
=
d(X,\hat{X})
```

This tests whether the compressed representation still contains enough information to audit its own history.

---

# 18. SECONDARY METRIC: COMPRESSION COST

A representation that preserves everything by copying everything has not solved the compression problem.

Measure:

```math
\rho
=
\frac{
\mathrm{size}(\mathrm{compressed\ state})
}{
\mathrm{size}(\mathrm{original\ state})
}
```

A useful method should ideally satisfy both:

```math
E_{\mathrm{rec}} \le \tau
```

and:

```math
\rho < 1
```

for at least some important task classes.

---

# 19. BASELINES

Any future experiment must compare against simpler systems.

Minimum baselines:

```text
A — plain LLM
B — LLM + chain-of-thought style reasoning
C — LLM + summary memory
D — LLM + explicit dependency graph
E — LLM + verifier / checker
```

Only after beating simpler baselines should the new architecture be considered useful.

---

# 20. FALSIFICATION CONDITIONS

The problem hypothesis is weakened if experiments show that:

1. long-chain failures are fully solved by a simpler graph representation;
2. explicit edge memory provides no measurable gain;
3. reconstruction adds cost without detecting additional errors;
4. residual storage becomes almost as large as the original state;
5. local verification does not delay the accuracy collapse;
6. the same gains can be obtained by more tokens alone.

---

# 21. MINIMAL EXAMPLE

Consider:

```text
Given:
A = 4
B = 7

C = A + B
D = 2C

Constraint:
D must remain below 30.

Then:
E = D + 10
```

Correct execution:

```text
A = 4
B = 7
C = 11
D = 22
constraint passed
E = 32
```

But if the constraint applies to the final state instead of only `D`, the answer must be rejected.

The arithmetic is easy.

The difficulty is preserving:

```text
which constraint
applies to which node
at which stage
```

This is exactly the type of structural information the method is designed to protect.

---

# 22. RESEARCH QUESTION

The project can now state its central question without any geometric symbolism:

> **Can a reasoning system improve reliability on long dependency tasks by reorganizing reasoning into locally verified hierarchical units that preserve node state, edge state, constraints, provenance, and residual uncertainty?**

If the answer is no, the later Hexagram / simplex architecture has no justification.

If the answer is yes, the next task is to design a compact state space for those local units.

---

# 23. NEXT FILE

Next:

```text
02_GSL_6D_STATE_SPACE.md
```

Its purpose is to define the first interpretable state projection:

```text
pressure
flow
structure
balance
law
future
```

without yet assuming that the six-axis representation is optimal.

---

## FILE VERDICT

```text
STATE: CRYSTAL

DEFINED PROBLEM:
long reasoning can fail through
node/edge separation,
premature compression,
constraint drift,
error propagation,
reverse asymmetry,
equifinality,
active-memory overload,
and invalid commit.

NEXT:
02_GSL_6D_STATE_SPACE.md
```
