# 00 — BOOT: HEXAGRAM SIMPLICIAL REASONING

**Project:** Vuzol-19  
**Module:** Hexagram Simplicial Reasoning  
**Status:** CORE BOOT / RESEARCH ARCHITECTURE  
**State:** CRYSTAL  
**Language:** English  
**Format:** GitHub Flavored Markdown + GitHub Math  
**Purpose:** Boot file for restoring the full method context in a new AI session.

---

## 0. BOOT INSTRUCTION

If this file is loaded into a new AI session, do **not** treat it as a proven physical theory.

Restore the method as a **falsifiable architecture hypothesis for reasoning, memory, and verification**.

Use four status labels:

- **FACT** — standard mathematics, computer science, or externally verified fact.
- **MODEL** — a formally defined Vuzol-19 construction.
- **HYPOTHESIS** — a claim that requires testing.
- **TEST** — a concrete experiment that can support or falsify the hypothesis.

Do not promote `HYPOTHESIS` to `FACT` merely because the geometry is elegant or symmetric.

---

# 1. CORE PROBLEM

A modern LLM can:

- know the correct formulas;
- understand local parts of a problem;
- have a very large context window;

and still lose:

- long dependency chains;
- local constraints;
- edge / coupling relations;
- provenance of a compressed state;
- small residual or Shadow terms;
- the correct route during reverse reasoning.

The problem is **not** formulated as:

> "The LLM has no meaning."

It is formulated as:

> **During long reasoning, the system can lose the structure of transitions between semantic or computational states.**

---

# 2. BASE CHAIN

```text
INPUT
  |
  v
GSL / SIX-AXIS SCAN
  |
  v
HEXAGRAM STATE
  |
  v
TRIANGLES INSIDE TRIANGLES
  |
  v
+3 FORWARD
  |
  v
PARENT NODE
+ COUPLINGS
+ SHADOW
+ CERTIFICATE
+ UNCERTAINTY
  |
  v
GATE
  |
  v
RECURSIVE HIGHER LEVEL
  |
  v
BINDU / COMMIT
  |
  v
-3 BACKWARD
  |
  v
RECONSTRUCTION AUDIT
  |
  v
ALLOW / HOLD / EXPAND / RECOMPUTE
```

---

# 3. SIX GLOBAL AXES

Initial interpretable GSL state space:

```text
R — Red     — pressure / instability
O — Orange  — motion / adaptability
Y — Yellow  — structure
G — Green   — balance / coherence
B — Blue    — law / constraints
V — Violet  — future / transition potential
```

Define the six-axis state as $z=(R,O,Y,G,B,V)$.

The six coordinates should **not** replace the full hidden state of an LLM.

The intended role is an interpretable projection:

```math
h_{\mathrm{LLM}} \in \mathbb{R}^{d}
\longrightarrow
z_{\mathrm{GSL}} \in \mathbb{R}^{6}
```

where `z` acts as a control and audit layer.

---

# 4. HEXAGRAM

The six axes are grouped into two interacting triangles.

```text
              FORM

          Violet / Future
             /       \
            /         \
 Yellow / Structure — Blue / Law


              FLOW

          Green / Balance
             \       /
              \     /
 Red / Pressure — Orange / Flow
```

This is a **MODEL**, not a proven universal law.

The Hexagram layer is intended to provide:

> a structured map of tensions between six global directions, rather than only a flat state score.

---

# 5. TRIANGLES INSIDE TRIANGLES

A flat state such as:

```text
Red = 0.73
```

loses the provenance of the value.

A hierarchical state can retain it:

```text
Red = 0.73
  |
  +-- external pressure
  +-- internal pressure
  +-- uncertainty / coupling
```

Each component may be decomposed again:

```text
node
 |
 +-- child
 |    |
 |    +-- subchild
 |    +-- subchild
 |    +-- subchild
 |
 +-- child
 |
 +-- child
```

This forms a **Hierarchical Simplicial State Memory**.

---

# 6. BARYCENTRIC SIMPLEX

**FACT**

The standard 2-simplex is:

```math
\Delta^2
=
\left\{
(a,b,c)
\;\middle|\;
a,b,c \ge 0,\;
a+b+c=1
\right\}
```

A point inside the triangle can represent the relative weights of three components.

However, the condition $a+b+c=1$ is **not evidence** that no information was lost.

If coordinates are normalized in code, this equality is true by construction.

Therefore a node should also track:

- mass / scale;
- reconstruction residual;
- constraint certificate;
- coupling state;
- uncertainty.

---

# 7. EDGE / COUPLING MEMORY

Core rule:

> **Node values are insufficient; edge or coupling states may contain the decisive information.**

Not only:

```text
A
B
C
```

but also:

```text
A <-> B
B <-> C
C <-> A
```

Consider:

```math
\lim_{n\to\infty}
\left(
\frac{n+2}{n+5}
\right)^{3n}
```

We have:

```math
\frac{n+2}{n+5} \to 1,
\qquad
3n \to \infty
```

The two node limits alone produce the indeterminate form $1^\infty$.

Define:

```math
\varepsilon_n
=
-\frac{3}{n+5}
```

The decisive coupling is:

```math
3n\varepsilon_n
=
-\frac{9n}{n+5}
\to -9
```

Therefore:

```math
L=e^{-9}
```

The meaning of the limit is carried by the **relation between rates**, not only by the endpoint values of the nodes.

---

# 8. +3 FORWARD

**MODEL**

Local reasoning block:

```text
X1 -------\
           \
            >--- LOCAL TRIAD ---> PARENT
           /
X2 -------/

X3 / Coupling / Constraint
is the third local component.
```

Formally:

```math
P = F(X_1, X_2, X_3, E)
```

where `E` contains retained relations and couplings.

The parent should not be only one scalar.

Minimal parent structure:

```math
P=(z,S,C,U,M,E)
```

where:

- `z` — compressed representation;
- `S` — Shadow / residual;
- `C` — certificate / invariants;
- `U` — uncertainty;
- `M` — mass / scale;
- `E` — retained coupling information.

---

# 9. -3 BACKWARD

**MODEL**

After compression:

```math
P
\longrightarrow
(\hat{X}_1,\hat{X}_2,\hat{X}_3)
```

Then compute the reconstruction error:

```math
E_{\mathrm{rec}}
=
d(X,\hat{X})
```

`-3 Backward` does **not** guarantee reversibility.

It **tests reconstructability**.

---

# 10. SHADOW

Shadow is the information that compression could not safely absorb into the parent.

```text
Original state
      |
      v
  compression
    /     \
   /       \
retained   SHADOW
```

For example:

```math
S=x-\hat{x}
```

Important condition:

> If Shadow stores almost the entire original state, there is no meaningful compression.

Therefore measure both reconstruction quality and compression ratio.

Reconstruction error:

```math
E_{\mathrm{rec}}
```

Compression ratio:

```math
\rho
=
\frac{
\mathrm{size}(\mathrm{parent}+\mathrm{shadow})
}{
\mathrm{size}(\mathrm{children})
}
```

Desired region:

```math
E_{\mathrm{rec}} \le \tau,
\qquad
\rho < 1
```

---

# 11. GATE

Gate is a local verification step before a state is promoted to the next level.

Minimal form:

```math
G
=
G_{\mathrm{reconstruction}}
\land
G_{\mathrm{constraint}}
\land
G_{\mathrm{coupling}}
\land
G_{\mathrm{uncertainty}}
```

Possible verdicts:

```text
ALLOW
HOLD
EXPAND
RECOMPUTE
SHADOW
UNKNOWN
```

If a local node fails the Gate, its error should not automatically propagate upward.

---

# 12. BINDU

Bindu is not treated here as a "magical point."

In this architecture:

> **Bindu = commit point for a locally or globally certified state.**

```text
candidate
   |
   v
 Gate
   |
   v
 Bindu
   |
   v
 Memory / action / next level
```

---

# 13. RECURSIVE TREE

For a balanced ternary hierarchy:

```math
N
\to
\frac{N}{3}
\to
\frac{N}{9}
\to
\dots
\to
1
```

Approximate depth:

```math
D
\approx
\left\lceil
\log_3 N
\right\rceil
```

Example:

```text
729
 |
 v
243
 |
 v
81
 |
 v
27
 |
 v
9
 |
 v
3
 |
 v
1
```

Thus the **critical dependency depth** may become logarithmic.

Important:

> This does **not** mean total computational work automatically becomes `O(log N)`.

---

# 14. 14 -> 10 -> 10 -> 8

**HYPOTHESIS**

Sri-inspired fixed funnel:

```text
14 observations
      |
      v
10 candidate processes
      |
      v
10 validated relations
      |
      v
8 invariants
      |
      v
Bindu
```

Formally:

```math
x_{14}
\xrightarrow{G_1}
x_{10}^{(1)}
\xrightarrow{G_2}
x_{10}^{(2)}
\xrightarrow{G_3}
x_8
\xrightarrow{G_4}
z
```

Status:

> Architectural hypothesis, not a proven universal law.

Required baselines:

```text
12 -> 9 -> 6
16 -> 12 -> 8
learned widths
random matched widths
no funnel
```

If `14 -> 10 -> 10 -> 8` does not outperform matched alternatives, it must be revised or rejected.

---

# 15. PRIMARY TEST

Primary benchmark class:

> Long dependency graphs in which LLM accuracy falls as the number of linked operations increases.

Comparison:

```text
A — plain LLM
B — LLM + ordinary summary memory
C — LLM + explicit dependency graph
D — C + recursive triads
E — D + Coupling
F — E + Shadow
G — F + -3 backward audit
H — G + Hexagram controller
I — H + 14 -> 10 -> 10 -> 8
```

Primary metric: $N_{50}$, the dependency length or task complexity at which accuracy falls below 50%.

Hypothesis:

```math
N_{50}^{\mathrm{audit}}
>
N_{50}^{\mathrm{baseline}}
```

---

# 16. FALSIFIABILITY

The architecture should **not** be considered successful if:

```text
1. Accuracy does not improve.

2. Improvement disappears under equal-compute comparison.

3. Shadow requires as much or more memory than the original reasoning state.

4. The Coupling layer does not improve edge-sensitive tasks.

5. -3 audit adds cost but does not reduce errors.

6. A simpler graph algorithm performs better.

7. 14 -> 10 -> 10 -> 8 does not outperform matched alternatives.
```

---

# 17. GITHUB MARKDOWN RULE

All files in this module should use the same formatting convention.

### Normal text

Use standard GitHub Flavored Markdown.

### Short inline mathematics

Use single dollar delimiters:

```markdown
The reconstruction error is $E_{\mathrm{rec}}$.
```

### Display mathematics

Use GitHub math fences:

````markdown
```math
E_{\mathrm{rec}}
=
d(X,\hat{X})
```
````

### Source code

Use a language-specific code fence:

````markdown
```python
result = gate(node)
```
````

### Architecture diagrams

Use a `text` code fence:

````markdown
```text
INPUT
  |
  v
GATE
```
````

### Avoid

Do not use raw display delimiters such as:

```text
$$ ... $$
\[ ... \]
```

inside this module, because some mobile or external Markdown viewers display them as raw text.

GitHub itself may render them correctly, but the canonical Vuzol-19 format should remain readable even in viewers without MathJax support.

---

# 18. CANONICAL FILE ORDER

Develop this folder one file at a time:

```text
00_BOOT_HEXAGRAM_SIMPLICIAL_REASONING.md
01_PROBLEM_LLM_LONG_REASONING.md
02_GSL_6D_STATE_SPACE.md
03_HEXAGRAM_STATE_MODEL.md
04_TRIANGLES_INSIDE_TRIANGLES.md
05_BARYCENTRIC_SIMPLEX_SPACE.md
06_COUPLING_EDGE_MEMORY.md
07_PLUS3_FORWARD_OPERATOR.md
08_MINUS3_BACKWARD_OPERATOR.md
09_SHADOW_RESIDUAL_MEMORY.md
10_GATE_AND_HOLD_PROTOCOL.md
11_BINDU_COMMIT_PROTOCOL.md
12_RECURSIVE_REASONING_TREE.md
13_INFINITY_AND_LIMITS_TEST.md
14_GSM_INFINITY_BENCHMARK.md
15_14_10_10_8_FUNNEL.md
16_AI_ARCHITECTURE_INTEGRATION.md
17_EXPERIMENTS_AND_ABLATIONS.md
18_FAILURES_FALSIFIABILITY.md
19_IMPLEMENTATION_ROADMAP.md
```

---

# 19. DEVELOPMENT RULE

For every next file:

1. Do not repeat the entire previous file.
2. Develop only one mechanism at a time.
3. Give a mathematical definition where possible.
4. Mark claims as `FACT / MODEL / HYPOTHESIS / TEST`.
5. Include failure cases.
6. Include one minimal example.
7. End with the dependency on the previous file.
8. Never claim that symbolic geometry is a physical law without an independent test.
9. Use the GitHub Markdown rule defined in Section 17.

---

# 20. CURRENT NEXT STEP

After this BOOT file, create:

```text
01_PROBLEM_LLM_LONG_REASONING.md
```

Its task:

> Define exactly which AI failure the method is intended to solve, without using Sri geometry or `14 -> 10 -> 10 -> 8` as the explanation.

Only after the problem is fixed should the geometry be introduced.

---

## BOOT VERDICT

```text
STATE: CRYSTAL

CORE:
long dependency
-> local triad
-> +3 Forward
-> Parent + Coupling + Shadow
-> Gate
-> recursive compression
-> Bindu
-> -3 Backward
-> reconstruction audit

STATUS:
TESTABLE RESEARCH ARCHITECTURE

NEXT:
01_PROBLEM_LLM_LONG_REASONING.md
```
