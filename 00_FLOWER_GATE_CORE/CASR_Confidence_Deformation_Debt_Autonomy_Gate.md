# Confidence Deformation Debt: A CASR Control Layer for Neural-Network Autonomy

## A reproducible proposal for calibration-aware state routing

**Audience:** machine-learning researchers, neural-network engineers, AI-safety researchers, and developers working with calibration, uncertainty, and autonomous systems.

**Status:** a proposed control architecture with reproducible arithmetic. The numerical sequence below is synthetic and illustrative. It is not a benchmark result, not evidence of improved model accuracy, and not a claim that CASR is already validated.

---

## 1. The problem: confidence is not correctness

A classifier produces logits \(z=(2,1,0)\). Softmax converts them into a probability distribution:

\[
p_i(T)=\frac{\exp(z_i/T)}{\sum_j\exp(z_j/T)}.
\]

The temperature \(T>0\) changes the distribution but does not change the ranking of the logits:

\[
\arg\max_i z_i=\arg\max_i(z_i/T).
\]

For these logits:

| Temperature | \(P(A)\) | \(P(B)\) | \(P(C)\) | Top-1 class |
|---:|---:|---:|---:|---|
| 2.0 | 50.648% | 30.721% | 18.631% | A |
| 1.0 | 66.524% | 24.472% | 9.003% | A |
| 0.5 | 86.681% | 11.727% | 1.592% | A |
| 0.2 | 99.326% | 0.669% | 0.005% | A |

The model's top-1 decision remains A, while its reported confidence changes dramatically. Lowering temperature does not add evidence, improve the learned representation, or make an incorrect prediction correct.

This creates a control problem: **what should an autonomous system do when its confidence is persistently higher than its observed reliability?**

Ordinary temperature scaling can improve calibration when its parameter is fitted on a suitable held-out calibration set. The proposal here is different: track calibration error over time and let that history influence the system's permitted level of autonomy.

## 2. The proposed concept: Deformation Debt

We call the accumulated calibration-risk state **Deformation Debt**, denoted \(D_t\).

The analogy is structural: a model can continue producing the same top-1 answer while its confidence distribution becomes poorly aligned with observed outcomes. If the system ignores that mismatch, later decisions may inherit an unreliable confidence signal.

For batch \(t\), define:

- \(C_t\): mean predicted confidence for the selected class;
- \(A_t\): observed accuracy on the same labelled batch;
- \(\delta\): a tolerated confidence–accuracy gap;
- \(\rho\): debt-retention factor, \(0\leq\rho\leq1\).

For a simple overconfidence-only demonstrator:

\[
\epsilon_t=\max(0,C_t-A_t-\delta)
\]

\[
D_{t+1}=\rho D_t+\epsilon_t.
\]

Interpretation:

- \(\epsilon_t\) is newly observed excess overconfidence beyond the tolerance.
- \(\rho D_t\) carries part of the previous debt into the next batch.
- \(D_t\) is a controller state, not a probability and not a universal statistical metric.

This is a deliberately simple proposed state update. It must not replace established calibration metrics such as Expected Calibration Error (ECE), Brier score, and Negative Log-Likelihood (NLL). In particular, a single mean-confidence-minus-accuracy gap can hide subgroup errors and cancellation effects. A production implementation should retain per-bin and per-class calibration diagnostics.

## 3. Worked example: confidence stays high while accuracy collapses

Keep the same logits and \(T=0.2\), so the top-class confidence is approximately

\[
C=0.993262.
\]

Now imagine 20 sequential batches of 100 labelled predictions:

- batches 1–5: observed accuracy is 99%;
- batches 6–15: observed accuracy falls to 60%;
- batches 16–20: observed accuracy returns to 99%.

For this demonstration, set:

\[
\delta=0.05,\qquad \rho=0.8,\qquad D_1=0.
\]

During the first five batches:

\[
\epsilon=\max(0,0.993262-0.99-0.05)=0.
\]

No new debt is added.

During the next ten batches:

\[
\epsilon=\max(0,0.993262-0.60-0.05)
=0.343262.
\]

The recurrence is therefore:

\[
D_{t+1}=0.8D_t+0.343262.
\]

Starting from zero at the beginning of the degraded period, after ten degraded batches:

\[
D_{10}=0.343262\sum_{k=0}^{9}0.8^k
\]

\[
D_{10}=0.343262\frac{1-0.8^{10}}{1-0.8}
\approx1.532.
\]

When accuracy returns to 99%, the new excess term returns to zero, but old debt decays rather than disappearing instantly:

\[
D_{t+1}=0.8D_t.
\]

### Batch-by-batch result

Values are rounded to four decimal places. The index is the batch number; debt is updated after observing that batch.

| Batch | Accuracy | Confidence | New excess \(\epsilon_t\) | Debt after batch |
|---:|---:|---:|---:|---:|
| 1 | 99% | 99.326% | 0 | 0.0000 |
| 2 | 99% | 99.326% | 0 | 0.0000 |
| 3 | 99% | 99.326% | 0 | 0.0000 |
| 4 | 99% | 99.326% | 0 | 0.0000 |
| 5 | 99% | 99.326% | 0 | 0.0000 |
| 6 | 60% | 99.326% | 0.3433 | 0.3433 |
| 7 | 60% | 99.326% | 0.3433 | 0.6179 |
| 8 | 60% | 99.326% | 0.3433 | 0.8376 |
| 9 | 60% | 99.326% | 0.3433 | 1.0133 |
| 10 | 60% | 99.326% | 0.3433 | 1.1539 |
| 11 | 60% | 99.326% | 0.3433 | 1.2664 |
| 12 | 60% | 99.326% | 0.3433 | 1.3564 |
| 13 | 60% | 99.326% | 0.3433 | 1.4284 |
| 14 | 60% | 99.326% | 0.3433 | 1.4860 |
| 15 | 60% | 99.326% | 0.3433 | 1.5320 |
| 16 | 99% | 99.326% | 0 | 1.2256 |
| 17 | 99% | 99.326% | 0 | 0.9805 |
| 18 | 99% | 99.326% | 0 | 0.7844 |
| 19 | 99% | 99.326% | 0 | 0.6275 |
| 20 | 99% | 99.326% | 0 | 0.5020 |

The key observation is not that the classifier changed its answer. It did not. The observed reliability changed while the reported confidence stayed fixed. The controller accumulated a state that persisted after the observed accuracy recovered.

This persistence is a form of **hysteresis**: the system's control state depends on recent history, not only on the current batch.

## 4. From debt to autonomy: the Gate policy

A controller can map the debt state to an operational mode. For illustration only, define:

| Debt state | Example operating mode |
|---|---|
| \(D<0.10\) | Normal operation, subject to ordinary safeguards |
| \(0.10\leq D<0.30\) | Supervised operation; require additional checks |
| \(D\geq0.30\) | Restricted operation; no high-impact autonomous action |

Under the worked example, the first degraded batch produces \(D=0.3433\), so the illustrative controller immediately enters restricted mode. It remains restricted through the five recovery batches because the debt is still above 0.30.

These thresholds are **chosen demonstration values**, not scientifically established universal thresholds. They must be selected using validation data, risk analysis, and the cost of false restrictions versus unsafe actions.

A more careful production policy should use confidence intervals and minimum sample counts. A batch of 100 examples can be noisy; a small subgroup can be severely miscalibrated even when the overall batch looks acceptable.

## 5. CASR interpretation: state, Shadow, Gate, Bindu, Memory

The proposed architecture maps the controller into five responsibilities:

### State
Record logits, selected class, temperature, probability vector, model/version identifier, data slice, and prediction timestamp.

### Shadow
Track what the current confidence signal fails to reveal:
- confidence versus observed accuracy;
- calibration by confidence bin;
- per-class and per-group calibration;
- distribution shift indicators;
- sample count and uncertainty of the estimate;
- unresolved or delayed labels.

Shadow is not a claim that hidden truth has been discovered. It is a structured record of known uncertainty and missing evidence.

### Gate
Apply explicit policy constraints:
- Is there enough labelled evidence?
- Is calibration within the validated operating envelope?
- Is the prediction in-distribution?
- What is the impact of acting incorrectly?
- Does this action require human approval?

A high-impact action should not become permitted merely because a scalar debt score is low. Hard safety, legal, privacy, and human-rights constraints remain independent gates.

### Bindu
The commit point: allow a specified class of action, require human review, defer pending evidence, or block. Bindu should record which rule authorized the decision.

### Memory
Store the prediction, calibration diagnostics, debt update, Gate decision, later ground truth, and any recovery evidence. This makes the control decision auditable.

## 6. Forward and backward streams (+3 / −3)

The proposed stream metaphor can be made operational:

**Forward stream (+3):**
1. Estimate the next debt state under candidate operating conditions.
2. Predict how the autonomy mode would change.
3. Estimate the effect of a proposed temperature or calibration update.
4. Evaluate whether the candidate policy remains within its validated envelope.

**Backward stream (−3):**
1. Recheck prior predictions after labels arrive.
2. Recompute calibration diagnostics.
3. Identify which earlier decisions were made under excessive confidence.
4. Verify that a proposed recovery is supported by enough new evidence.

The streams must not be confused with actual parallel threads unless implemented as such. They are functional roles in the algorithm. A later implementation can test sequential execution versus parallel execution.

## 7. Recovery: do not restore autonomy on one good batch

A debt state that simply decays may still be too permissive. Recovery should require evidence.

A more robust recovery policy could require all of the following:
- a minimum number of labelled examples;
- acceptable ECE and NLL on a recent held-out window;
- no severe per-class or high-impact subgroup failure;
- no detected distribution shift outside the validated range;
- successful re-evaluation after any calibration update.

Temperature scaling can be fitted on a held-out calibration set, but it does not change the model's learned knowledge or guarantee correctness. If the data distribution changes, the fitted temperature may become stale.

A controller should therefore distinguish:
- **calibration repair** — adjusting the mapping from logits to probabilities;
- **model repair** — retraining or changing the model when its predictions are wrong;
- **policy recovery** — restoring permission to take actions after sufficient evidence.

These are different operations.

## 8. Runnable Python calculation

The following script reproduces the softmax probabilities and the 20-batch debt sequence using only the Python standard library.

```python
import math

logits = [2.0, 1.0, 0.0]

def softmax(logits, temperature):
    scaled = [x / temperature for x in logits]
    m = max(scaled)  # numerical stability
    exps = [math.exp(x - m) for x in scaled]
    total = sum(exps)
    return [x / total for x in exps]

print("Softmax probabilities")
for T in [2.0, 1.0, 0.5, 0.2]:
    p = softmax(logits, T)
    print(T, [round(x * 100, 4) for x in p])

confidence = softmax(logits, 0.2)[0]
rho = 0.8
tolerance = 0.05
debt = 0.0

print("\\nBatch,accuracy,confidence,new_excess,debt")
for batch in range(1, 21):
    accuracy = 0.99 if batch <= 5 or batch >= 16 else 0.60
    new_excess = max(0.0, confidence - accuracy - tolerance)
    debt = rho * debt + new_excess
    print(
        batch,
        f"{accuracy:.4f}",
        f"{confidence:.6f}",
        f"{new_excess:.6f}",
        f"{debt:.6f}",
        sep=","
    )
```

## 9. How to test whether this is useful

The controller should be compared with simple baselines:

1. **No controller:** model confidence is used as usual.
2. **Static threshold:** require review whenever confidence or a standard calibration metric crosses a fixed threshold.
3. **Temperature scaling:** fit one temperature on held-out calibration data.
4. **CASR debt controller:** use calibration diagnostics, a history-dependent debt state, Gate modes, and evidence-based recovery.

Use identical model predictions and data streams for all policies. Measure:

- task accuracy (to ensure the controller does not pretend to improve the model);
- ECE, Brier score, and NLL;
- high-impact error rate;
- number of autonomous actions allowed, deferred, and blocked;
- false restriction rate;
- time to recover after a distribution shift;
- controller overhead and memory;
- performance across random seeds and data subgroups.

A key safety metric is **selective risk**: among predictions/actions the controller allows, how often are they wrong? Also report coverage: what fraction of cases remain eligible for autonomous action? A controller that blocks everything has low risk but no practical utility.

## 10. Research questions for independent review

1. Is the proposed debt recurrence a useful summary of calibration history, or does it discard important information?
2. Should debt be a scalar, a vector by class/group, or a structured tensor?
3. How should delayed labels and uncertain ground truth update the debt?
4. Can the Gate reduce high-impact errors at a useful level of coverage?
5. Does hysteresis improve safe recovery, or does it create unnecessary lock-in?
6. Does the controller add value beyond ECE/NLL monitoring, selective prediction, and existing abstention policies?
7. Can the entire result be reproduced from logged predictions and labels?

## Conclusion

The proposal does not claim that temperature scaling is a new discovery, or that a debt variable makes a neural network more accurate.

It proposes a different control layer:

**A model's autonomy is not treated as a permanent property. It is conditioned on observed reliability, uncertainty, and the history of calibration failures.**

The mathematical demonstration shows how a confidence–accuracy mismatch can accumulate and persist after a temporary failure period. The engineering question is whether this history-dependent Gate can reduce harmful autonomous actions while preserving useful coverage.

The idea should be judged by reproducible comparisons against calibration monitoring, temperature scaling, and selective prediction—not by terminology alone.
