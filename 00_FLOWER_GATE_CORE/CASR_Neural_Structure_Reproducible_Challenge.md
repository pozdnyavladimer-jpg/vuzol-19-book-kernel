# CASR × Neural Network Structure: A Reproducible Mathematical Challenge

**Purpose:** an independent, reproducible technical response to the LinkedIn post about Jacobian products, residual blocks, RoPE, Mamba/associative scans, Mixture-of-Experts (MoE), and Singular Learning Theory.

**Status:** this is a small mathematical verification pack, not evidence that CASR improves neural-network training. It separates identities that can be checked exactly from hypotheses that require experiments.

---

## 1. What is being tested?

The post makes several different kinds of claims. They should not be mixed:

1. **Mathematical identities/bounds** — can be checked on explicit matrices and vectors.
2. **Algorithmic equivalence** — can be checked by comparing sequential and tree-composed state updates.
3. **Empirical training claims** — require actual neural-network training, controlled baselines, repeated seeds, and measurements.
4. **Architectural hypothesis** — CASR may organize structural checks as coordinated streams, but that is not a result until implemented and compared.

This document supplies reproducible calculations for the first two categories and a precise experiment plan for the remaining categories.

## 2. Experiment A — Jacobian products and directional contraction

For a depth-3 network, the local input-output Jacobian is

\[
J = J_3 J_2 J_1.
\]

The singular values of the product describe the maximum and minimum local stretching over all unit directions. They are **not generally the products of the corresponding singular values of the individual layers**, because singular-vector orientations matter.

Use these explicit matrices:

\[
J_1 =
\begin{bmatrix}
0.9&0\\
0&0.5
\end{bmatrix}
\]

\[
J_2=R(0.6)
\begin{bmatrix}
1.2&0\\
0&0.7
\end{bmatrix}
R(-0.6),
\quad
J_3=R(-0.35)
\begin{bmatrix}
1.1&0\\
0&0.4
\end{bmatrix}
R(0.35),
\]

where

\[
R(\theta)=
\begin{bmatrix}
\cos\theta&-\sin\theta\\
\sin\theta&\cos\theta
\end{bmatrix}.
\]

The individual singular values are:

| Matrix | Singular values |
|---|---:|
| \(J_1\) | 0.9, 0.5 |
| \(J_2\) | 1.2, 0.7 |
| \(J_3\) | 1.1, 0.4 |

Multiplying the matrices gives approximately

\[
J \approx
\begin{bmatrix}
0.90581784&0.02167810\\
-0.11002168&0.18098003
\end{bmatrix}.
\]

The singular values of the **product** are approximately

\[
\sigma(J)=(0.91247511,\;0.18227346).
\]

Interpretation: in this example, some directions are much more strongly contracted than others. A structural monitor could record the minimum singular value, maximum singular value, condition number, and the corresponding singular directions.

**CASR mapping (hypothesis, not proof):**
- Shadow: record directions with strong contraction/expansion.
- Gate: flag a transition if a predeclared stability threshold is crossed.
- Memory: preserve the measured matrix, seed, threshold, and outcome.
- Bindu: accept a claim only after recomputation from the stored inputs.

A useful caution: this one example does not establish vanishing gradients in a trained network. It demonstrates how the Jacobian product can be measured.

## 3. Experiment B — Residual-block lower bound

For a residual mapping \(y=x+F(x)\), its Jacobian is

\[
J=I+J_F.
\]

For any matrix \(A\), the singular-value perturbation inequality gives

\[
\sigma_{\min}(I+A)\geq 1-\|A\|_2.
\]

Choose

\[
J_F=
\begin{bmatrix}
0.2&0.1\\
0&-0.1
\end{bmatrix}.
\]

The spectral norm is

\[
\|J_F\|_2\approx0.22882456.
\]

Therefore the bound is

\[
\sigma_{\min}(I+J_F)\geq0.77117544.
\]

But

\[
I+J_F=
\begin{bmatrix}
1.2&0.1\\
0&0.9
\end{bmatrix}
\]

has actual singular values approximately

\[
(1.20930369,\;0.89307592).
\]

Thus the actual minimum singular value, 0.89307592, is above the lower bound, 0.77117544.

**What this does and does not show:** the bound is valid for this example. It is useful only when \(\|J_F\|_2<1\), and it is a local bound for that block. It is not a universal guarantee for an arbitrarily deep network, its optimizer, or its training dynamics.

## 4. Experiment C — RoPE-style orthogonal rotation

Take \(v=(3,4)^T\). Its Euclidean norm is

\[
\|v\|_2=5.
\]

An orthogonal rotation gives \(v'=R(\theta)v\). Since

\[
R(\theta)^T R(\theta)=I,
\]

we have

\[
\|v'\|_2^2=v^T R(\theta)^T R(\theta)v=v^Tv,
\]

so the norm is preserved exactly in exact arithmetic.

For \(\theta=0.7\) radians:

\[
v'\approx(-0.173009,\;4.997000)^T
\]

(up to rounding), and its norm remains 5 up to floating-point precision.

This verifies the orthogonality property of a two-dimensional rotation. It does **not** prove that RoPE guarantees long-context reasoning, recall, or semantic correctness. Those require task-level benchmarks.

## 5. Experiment D — Sequential recurrence versus associative composition

Consider the scalar state update

\[
x_{t+1}=a_t x_t+b_t.
\]

Represent each step by a pair \((a,b)\). Applying \((a_1,b_1)\), then \((a_2,b_2)\), is equivalent to

\[
(a_2,b_2)\circ(a_1,b_1)
=(a_2a_1,\;a_2b_1+b_2).
\]

This operation is associative because it is composition of affine functions.

Choose \(x_0=2\), and three updates:

| Step | \(a_t\) | \(b_t\) |
|---|---:|---:|
| 1 | 0.8 | 1.0 |
| 2 | 0.5 | -0.2 |
| 3 | 1.2 | 0.3 |

Sequential calculation:

\[
x_1=0.8(2)+1=2.6
\]
\[
x_2=0.5(2.6)-0.2=1.1
\]
\[
x_3=1.2(1.1)+0.3=1.62.
\]

Composing the three affine maps gives

\[
(a_{\mathrm{total}},b_{\mathrm{total}})
=(0.48,\;0.66),
\]

so

\[
x_3=0.48(2)+0.66=1.62.
\]

The sequential and composed results match.

**Why this matters:** associative composition permits a parallel prefix/scan implementation. It does not mean every recurrence can be parallelized arbitrarily: the update must have an associative composition representation, and the practical speed depends on hardware, sequence length, memory traffic, and implementation overhead.

**CASR opportunity:** treat each state update as a typed transition; use a forward stream to compose candidates, a reverse/check stream to verify equivalence, and a Gate to reject invalid compositions. The key experiment is whether CASR adds useful verification at an acceptable computational cost—not whether it can rename an associative scan.

## 6. Experiment E — MoE routing balance

Suppose 1,000 tokens are routed to four experts.

Unbalanced counts:

\[
(700,\;200,\;80,\;20)
\]

Balanced counts:

\[
(250,\;250,\;250,\;250).
\]

For routing proportions \(p_i\), normalized entropy is

\[
H_{\mathrm{norm}}=
\frac{-\sum_i p_i\ln p_i}{\ln 4}.
\]

The unbalanced distribution has

\[
H_{\mathrm{norm}}\approx0.6145,
\]

while the balanced distribution has

\[
H_{\mathrm{norm}}=1.
\]

This is a simple load-distribution diagnostic. Entropy alone is not a complete MoE quality metric: routing quality, expert capacity, token dropping, communication cost, and task performance also matter.

**CASR opportunity:** Shadow records load concentration and overloaded experts; Gate checks explicit capacity constraints; Memory stores routing statistics by batch and training step. A useful ablation asks whether the CASR controller improves load balance without hurting loss or increasing total compute too much.

## 7. Reproducible Python script

The following script recomputes the numerical results above. It requires NumPy.

```python
import numpy as np

def rot(theta):
    return np.array([
        [np.cos(theta), -np.sin(theta)],
        [np.sin(theta),  np.cos(theta)]
    ], dtype=float)

# A. Jacobian product
J1 = np.diag([0.9, 0.5])
J2 = rot(0.6) @ np.diag([1.2, 0.7]) @ rot(-0.6)
J3 = rot(-0.35) @ np.diag([1.1, 0.4]) @ rot(0.35)
J = J3 @ J2 @ J1

print("A: singular values J1/J2/J3:",
      np.linalg.svd(J1, compute_uv=False),
      np.linalg.svd(J2, compute_uv=False),
      np.linalg.svd(J3, compute_uv=False))
print("A: product J =\n", J)
print("A: singular values product =", np.linalg.svd(J, compute_uv=False))

# B. Residual lower bound
JF = np.array([[0.2, 0.1], [0.0, -0.1]])
spectral_norm = np.linalg.norm(JF, 2)
J_res = np.eye(2) + JF
lower_bound = 1.0 - spectral_norm
actual_min = np.linalg.svd(J_res, compute_uv=False)[-1]
print("B: ||JF||_2 =", spectral_norm)
print("B: lower bound =", lower_bound)
print("B: actual sigma_min =", actual_min)
assert actual_min + 1e-12 >= lower_bound

# C. Orthogonal rotation / RoPE-style property
v = np.array([3.0, 4.0])
v_rot = rot(0.7) @ v
print("C: rotated vector =", v_rot)
print("C: original and rotated norms =", np.linalg.norm(v), np.linalg.norm(v_rot))
assert np.allclose(np.linalg.norm(v), np.linalg.norm(v_rot))

# D. Affine recurrence and associative composition
steps = [(0.8, 1.0), (0.5, -0.2), (1.2, 0.3)]
x0 = 2.0
x = x0
for a, b in steps:
    x = a * x + b
sequential = x

def compose(second, first):
    a2, b2 = second
    a1, b1 = first
    return (a2 * a1, a2 * b1 + b2)

total = steps[0]
for step in steps[1:]:
    total = compose(step, total)
parallel_form = total[0] * x0 + total[1]
print("D: composed affine map =", total)
print("D: sequential / composed =", sequential, parallel_form)
assert np.allclose(sequential, parallel_form)

# E. Normalized MoE routing entropy
def normalized_entropy(counts):
    p = np.asarray(counts, dtype=float)
    p = p / p.sum()
    nz = p > 0
    return -(p[nz] * np.log(p[nz])).sum() / np.log(len(p))

print("E: unbalanced entropy =", normalized_entropy([700, 200, 80, 20]))
print("E: balanced entropy =", normalized_entropy([250, 250, 250, 250]))
```

## 8. The experiment that would genuinely test CASR

The calculations above verify mathematical properties. They do not establish that CASR is faster or better. To test that claim, implement a controller and compare:

- Baseline 1: ordinary sequential calculation / ordinary training loop.
- Baseline 2: established associative scan or framework implementation where applicable.
- Candidate: the same computation with CASR's forward stream, reverse verification, Shadow diagnostics, Gate rules, and Memory records.

Measure at least:

1. Numerical agreement with the baseline.
2. Number of transitions/candidates examined.
3. Wall-clock time after warm-up, over repeated runs.
4. Peak memory.
5. Verification overhead.
6. Failure cases and numerical error.
7. Whether removing each CASR component changes the result (ablation).

For neural-network training, additionally report dataset, model, optimizer, learning rate, batch size, hardware, software versions, random seeds, training steps, validation metrics, and confidence intervals across runs.

### Suggested acceptance criteria

- No valid state transition is silently discarded.
- The CASR result agrees with the reference implementation within a declared numerical tolerance.
- Any speedup is measured on the same hardware and workload.
- Verification overhead is reported, not hidden.
- Claims are limited to the tested problem class.

## 9. Questions for the author

1. Which of the post's claims are intended as mathematical guarantees, and which are empirical observations?
2. Can the author share a minimal implementation or benchmark for the Jacobian, residual, RoPE, or scan claims?
3. What exact invariant should a structural controller preserve?
4. How should a method be evaluated when it improves stability but increases compute?
5. Would an independent CASR implementation be useful as a cross-check, provided all results and limitations are published?

---

## Bottom line

The strongest concrete connection is the affine state-update composition in Experiment D: it gives a precise mathematical example where a sequence of transitions can be composed associatively and evaluated with a parallel scan. The Jacobian and residual calculations provide measurable structural diagnostics; RoPE gives an exact norm-preservation check; MoE entropy gives a simple load-balance signal.

These are testable building blocks—not proof that CASR is novel, faster, or superior. The next meaningful result must come from an executable implementation, fair baselines, and reproducible measurements.
