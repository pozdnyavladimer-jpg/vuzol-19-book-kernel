# 02 — Experiment Plan: Sunflower Sri3D

Status: **TEST PLAN / NOT YET GENERALIZED**

---

## 1. Goal

Do not try to prove the full conjecture first.

First test whether the proposed state representation reveals a repeatable transition law.

---

## 2. Enumerate small exact spaces

Start with small values such as:

```text
r = 3
k = 2, 3, 4
small n
```

For each \(k\)-uniform family:

1. determine whether it contains an \(r\)-sunflower;
2. enumerate candidate core/deletion orientations;
3. create provenance-preserving lower-rank states;
4. run lift checks;
5. record the transition graph.

Do not prune by the expected answer.

---

## 3. Record trajectory features

For each transition record:

```json
{
  "n": 0,
  "k": 0,
  "r": 0,
  "family_size": 0,
  "orientation": null,
  "source_ids": [],
  "removed_elements": [],
  "core_size": 0,
  "petal_conflict_E": 0,
  "frequency_histogram": {},
  "projection_size": 0,
  "lift_status": "ALLOW|HOLD|BLOCK",
  "sunflower_status_before": false,
  "sunflower_status_after": false
}
```

---

## 4. Search for recurrence after data collection

Test candidate relations only after generating the data.

Examples:

\[
X_{k+1}=aX_k+b
\]

\[
X_{k+1}=aX_k+bX_{k-1}
\]

\[
X_{k+1}\le cX_k
\]

\[
\log X_{k+1}-\log X_k\to c
\]

and piecewise rules conditioned on orientation/core statistics.

Fibonacci is one test among many:

\[
X_{k+1}=X_k+X_{k-1}.
\]

Reject it if residuals do not support it.

---

## 5. Strongest useful comparison

Compare four modes:

```text
A. flat family search
B. ordinary shadow/rank reduction
C. source-labelled projection
D. full oriented transition with lift contract
```

Measure:

- false sunflower detections,
- lost true sunflowers,
- number of candidate transitions,
- amount of provenance metadata,
- ability to reconstruct parent states,
- transition reuse,
- runtime,
- memory.

---

## 6. Required false-green tests

Inject cases where:

```text
different parent sets map to the same child
different removed elements produce identical payload
projection forms a sunflower but parents do not
compression/shift creates a sunflower absent in the source
```

A correct provenance Gate must not accept these as source-level proof.

---

## 7. Research success levels

```text
LEVEL 0:
visual pattern only

LEVEL 1:
reproducible small-case regularity

LEVEL 2:
predicts unseen small cases

LEVEL 3:
proved invariant or monotone potential

LEVEL 4:
proved constant-loss liftable rank reduction

LEVEL 5:
implication for the full Sunflower Conjecture
```

Current status:

```text
LEVEL 1 candidate / HOLD
```

The next target is not LEVEL 5.

It is to determine whether LEVEL 1 survives exact enumeration.
