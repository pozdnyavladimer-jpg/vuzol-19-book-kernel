# 225 — CORRUPTED DEPENDENCY MAP / PHASE BOUNDARY

**Status:** EXECUTED SYNTHETIC FALSIFICATION BENCHMARK  
**Previous:** 224 — Bindu State Engine Minimal Runtime

## Purpose
224 assumed a perfect reasoning DAG. 225 deliberately corrupts only the rollback map while preserving the true hidden computation graph.

`p_miss` deletes true dependency edges.  
`p_false` adds spurious dependency edges relative to the true edge count.

Design: 180 nodes, 24 roots, 160 seeds per grid point, 48 grid conditions = 7,680 trials.

## Reference — perfect dependency map
- final accuracy: **1.0000**
- affected-branch accuracy: **1.0000**
- invalidation recall: **1.0000**
- exact repair rate: **1.0000**
- savings vs full recomputation: **0.7295**

## Missing true edges
At `p_miss=0.10, p_false=0`:
- final accuracy: **0.9876**
- affected-branch accuracy: **0.9450**
- invalidation recall: **0.7907**
- exact repair rate: **0.4875**

A missed edge can hide a true descendant from rollback, leaving stale state alive.

## False edges
At `p_miss=0, p_false=0.20`:
- final accuracy: **1.0000**
- affected-branch accuracy: **1.0000**
- invalidation precision: **0.7510**
- collateral invalidations: **13.83**
- savings vs full: **0.6409**

With correct node semantics, extra conservative invalidation preserves correctness but wastes recomputation.

## Main asymmetry
For this benchmark:

`False-negative dependency → correctness risk`

`False-positive dependency → efficiency cost`

So a dependency extractor should prefer high recall, then prune uncertain edges when independence is established.

## Marginal summaries

### Missing edges
|   p_miss |   Final_accuracy |   Affected_accuracy |   Invalidation_recall |   Savings_vs_full |   Exact_repair_rate |
|---------:|-----------------:|--------------------:|----------------------:|------------------:|--------------------:|
|     0    |         1        |            1        |              1        |          0.672062 |            1        |
|     0.01 |         0.998681 |            0.994835 |              0.981855 |          0.678499 |            0.925    |
|     0.02 |         0.997211 |            0.987246 |              0.958921 |          0.685717 |            0.833333 |
|     0.05 |         0.993594 |            0.968772 |              0.903662 |          0.702517 |            0.677083 |
|     0.1  |         0.987934 |            0.946318 |              0.815272 |          0.731751 |            0.504167 |
|     0.2  |         0.977703 |            0.892551 |              0.61231  |          0.799559 |            0.25625  |
|     0.3  |         0.96794  |            0.843061 |              0.432718 |          0.855816 |            0.147917 |
|     0.4  |         0.958374 |            0.797377 |              0.306549 |          0.89773  |            0.096875 |

### False edges
|   p_false |   Final_accuracy |   Affected_accuracy |   Invalidation_precision |   Savings_vs_full |   Collateral_invalidations |   Exact_repair_rate |
|----------:|-----------------:|--------------------:|-------------------------:|------------------:|---------------------------:|--------------------:|
|      0    |         0.984948 |            0.927693 |                 0.991406 |          0.804337 |                   0        |            0.546875 |
|      0.02 |         0.984974 |            0.927775 |                 0.96145  |          0.7971   |                   0.969531 |            0.547656 |
|      0.05 |         0.984987 |            0.92781  |                 0.917479 |          0.785767 |                   2.56875  |            0.547656 |
|      0.1  |         0.985148 |            0.928344 |                 0.859109 |          0.7685   |                   4.91406  |            0.552344 |
|      0.2  |         0.985382 |            0.929379 |                 0.749176 |          0.726502 |                  10.6242   |            0.560156 |
|      0.4  |         0.985638 |            0.931618 |                 0.576829 |          0.635532 |                  23.1953   |            0.575781 |

## Exploratory safe boundary
Defined *before reading this table* as:
- final accuracy >= 99%
- affected-branch accuracy >= 95%

|   p_false |   max_p_miss_meeting_threshold |
|----------:|-------------------------------:|
|      0    |                           0.05 |
|      0.02 |                           0.05 |
|      0.05 |                           0.05 |
|      0.1  |                           0.05 |
|      0.2  |                           0.05 |
|      0.4  |                           0.05 |

This boundary is synthetic and not universal.

## Anti-PRION
**ALLOW:** Cascade Unwind tolerates some dependency-map corruption.  
**ALLOW:** false negatives are more dangerous to correctness than conservative false positives here.  
**HOLD:** tolerated error rate for LLM-generated DAGs.  
**BLOCK:** treating this phase boundary as a cognitive constant.

## Consequence
Binary edges are too crude. The next engine should use versioned probabilistic dependencies:

`CERTAIN / PROBABLE / SHADOW / REJECTED`

with:

`Risk(edge) = P(dependency) × downstream impact`.

## NEXT
**226 — PROBABILISTIC DEPENDENCY GATE / RISK-WEIGHTED CASCADE UNWIND**
