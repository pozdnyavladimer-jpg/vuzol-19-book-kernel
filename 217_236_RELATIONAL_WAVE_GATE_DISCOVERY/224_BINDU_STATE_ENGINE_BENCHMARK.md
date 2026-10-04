# 224 — BINDU STATE ENGINE MINIMAL RUNTIME

**Status:** EXECUTED SYNTHETIC BENCHMARK  
**Previous:** 223 — Bindu Epistemic State Engine

## What was tested

This experiment isolates one claim from 223:

> When an old premise is falsified, can a dependency DAG repair only the affected branch while preserving exact correctness?

The benchmark uses synthetic Boolean DAGs with hidden ground truth, so invalidation and repair can be scored exactly without asking an LLM to judge itself.

### Conditions

- 500 random DAG trials
- 160 nodes per DAG
- 20 roots
- derived nodes use AND / OR / XOR / majority operators
- one previously accepted root is later flipped by reliable new evidence
- Full baseline recomputes every derived node
- No-rollback baseline updates the root but leaves cached descendants untouched
- Bindu engine invalidates descendants and recomputes only that subgraph

## Aggregate result

| Metric                        |   Full recompute |   No rollback / cached summary |   Bindu selective DAG |
|:------------------------------|-----------------:|-------------------------------:|----------------------:|
| Final accuracy                |                1 |                       0.917513 |              1        |
| Affected-branch accuracy      |                1 |                       0.701709 |              1        |
| Mean recomputed derived nodes |              140 |                       0        |             47.086    |
| Recompute saved vs full       |                0 |                       1        |              0.663671 |

Mean affected subgraph size: **47.09 / 160 nodes**.

The Bindu DAG retained exact oracle accuracy in this controlled benchmark while recomputing, on average, only **47.09** derived nodes instead of **140.00**.

Mean recomputation reduction:

\[
66.4\%
\]

The no-rollback cached baseline was cheap but its accuracy inside the actually affected branch fell to **70.2%** on average.

## Dependency-density stress test

|   Max parents |   Mean affected nodes |   Bindu recompute |   Full recompute |   Bindu savings |   No-rollback affected accuracy |
|--------------:|----------------------:|------------------:|-----------------:|----------------:|--------------------------------:|
|             1 |               46.4067 |           46.4067 |              175 |        0.734819 |                        0.691561 |
|             2 |               49.78   |           49.78   |              175 |        0.715543 |                        0.720667 |
|             3 |               49.2467 |           49.2467 |              175 |        0.71859  |                        0.683957 |
|             4 |               46.74   |           46.74   |              175 |        0.732914 |                        0.69909  |
|             5 |               47.6667 |           47.6667 |              175 |        0.727619 |                        0.700985 |

## Interpretation

This is a positive result for **selective dependency repair**, not yet for LLM reasoning.

The result is expected in a DAG with perfect dependency metadata: an incremental computation system should outperform full recomputation whenever the affected subgraph is small.

What remains unproven is the difficult part:

1. Can an LLM extract the correct dependencies?
2. Can Shadow generate valid falsifiers rather than plausible-sounding objections?
3. Can Gate classify KEEP / HOLD / REWRITE / BLOCK reliably?
4. Does MemoryAtom compression preserve information needed much later?
5. Does the architecture still save tokens/model calls after the cost of dependency extraction, Shadow and Gate is included?

## Anti-PRION verdict

**ALLOW:** Cascade Unwind / selective recomputation is mechanically valid when dependency links are correct.

**HOLD:** net token/compute advantage around a real LLM.

**HOLD:** reduction of hallucination/context drift.

**BLOCK:** interpreting this synthetic benchmark as evidence that +3/-3 is a universal cognitive law.

## Next experiment — 225

Inject **dependency extraction errors** deliberately.

Sweep false-negative and false-positive dependency rates.

Measure the failure boundary at which selective repair loses its advantage:

\[
Performance(p_{miss},p_{false-edge})
\]

This directly tests the weakest assumption of 224: perfect knowledge of the reasoning DAG.
