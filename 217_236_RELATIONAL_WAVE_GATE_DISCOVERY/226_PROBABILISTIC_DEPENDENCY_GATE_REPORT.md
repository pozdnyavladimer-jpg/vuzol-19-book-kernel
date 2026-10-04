# 226 — PROBABILISTIC DEPENDENCY GATE / RISK-WEIGHTED CASCADE UNWIND

**Status:** EXECUTED SYNTHETIC BENCHMARK  
**Previous:** 225

## Question
Can uncertain dependency edges preserve selective-repair correctness without collapsing to full recomputation?

Each candidate edge receives a noisy probability. True and false score distributions overlap. Two Gate policies are compared:

1. `probability >= threshold`
2. `probability × downstream_impact >= threshold`

No preferred threshold is encoded.

## Design
- 160 nodes, 20 roots
- extractor qualities: [0.6, 0.7, 0.8, 0.9]
- thresholds: [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
- 70 independent worlds per quality
- true and false candidate dependencies
- hidden true DAG used only for scoring

Exploratory utility was declared as:

`AffectedAccuracy - 0.20 × RecomputedFraction`

Safety frontier requires FinalAccuracy >= 0.99 and AffectedAccuracy >= 0.95, then maximizes savings.

## Best utility
|   Extractor_quality | Gate_mode     |   Threshold |   Final_accuracy |   Affected_accuracy |   Invalidation_recall |   Invalidation_precision |   Recompute_nodes |   Savings_vs_full |   Exact_repair_rate |   Collateral_invalidations |   Utility |
|--------------------:|:--------------|------------:|-----------------:|--------------------:|----------------------:|-------------------------:|------------------:|------------------:|--------------------:|---------------------------:|----------:|
|                 0.6 | probability   |         0.2 |         1        |            1        |              1        |                 0.649542 |           50.9571 |          0.63602  |            1        |                   15.5714  |  0.927204 |
|                 0.6 | risk-weighted |         0.1 |         1        |            1        |              1        |                 0.628902 |           52.8429 |          0.622551 |            1        |                   17.4571  |  0.92451  |
|                 0.7 | probability   |         0.3 |         0.999732 |            0.997185 |              0.99067  |                 0.733889 |           46.0714 |          0.670918 |            0.957143 |                   11.0571  |  0.931369 |
|                 0.7 | risk-weighted |         0.2 |         0.998929 |            0.994546 |              0.980269 |                 0.76441  |           44      |          0.685714 |            0.885714 |                    9.31429 |  0.931689 |
|                 0.8 | probability   |         0.3 |         1        |            1        |              0.999152 |                 0.780413 |           43.9429 |          0.686122 |            1        |                    8.6     |  0.937224 |
|                 0.8 | risk-weighted |         0.2 |         0.999911 |            0.999286 |              0.997984 |                 0.814634 |           42.5571 |          0.69602  |            0.985714 |                    7.25714 |  0.93849  |
|                 0.9 | probability   |         0.3 |         1        |            1        |              0.99949  |                 0.855058 |           40.9571 |          0.707449 |            1        |                    5.58571 |  0.94149  |
|                 0.9 | risk-weighted |         0.2 |         1        |            1        |              0.997253 |                 0.870538 |           40.5143 |          0.710612 |            1        |                    5.17143 |  0.942122 |

## Safe frontier
|   Extractor_quality | Gate_mode     |   Threshold |   Final_accuracy |   Affected_accuracy |   Invalidation_recall |   Invalidation_precision |   Recompute_nodes |   Savings_vs_full |   Exact_repair_rate |   Collateral_invalidations |   Utility |
|--------------------:|:--------------|------------:|-----------------:|--------------------:|----------------------:|-------------------------:|------------------:|------------------:|--------------------:|---------------------------:|----------:|
|                 0.6 | probability   |         0.4 |         0.990982 |            0.958933 |              0.888194 |                 0.816172 |           36.7143 |          0.737755 |            0.614286 |                   6.4      |  0.906484 |
|                 0.6 | risk-weighted |         0.2 |         0.994107 |            0.970721 |              0.942792 |                 0.746452 |           42.4143 |          0.697041 |            0.7      |                   9.37143  |  0.910129 |
|                 0.7 | probability   |         0.4 |         0.995625 |            0.977868 |              0.935228 |                 0.849847 |           38.0857 |          0.727959 |            0.771429 |                   5.35714  |  0.92346  |
|                 0.7 | risk-weighted |         0.2 |         0.998929 |            0.994546 |              0.980269 |                 0.76441  |           44      |          0.685714 |            0.885714 |                   9.31429  |  0.931689 |
|                 0.8 | probability   |         0.5 |         0.991161 |            0.959335 |              0.858408 |                 0.963928 |           30.9286 |          0.779082 |            0.7      |                   1.14286  |  0.915152 |
|                 0.8 | risk-weighted |         0.2 |         0.999911 |            0.999286 |              0.997984 |                 0.814634 |           42.5571 |          0.69602  |            0.985714 |                   7.25714  |  0.93849  |
|                 0.9 | probability   |         0.5 |         0.994554 |            0.97105  |              0.908663 |                 0.953322 |           32.7429 |          0.766122 |            0.8      |                   1.05714  |  0.924274 |
|                 0.9 | risk-weighted |         0.3 |         0.995089 |            0.96952  |              0.898915 |                 0.96052  |           32.8714 |          0.765204 |            0.728571 |                   0.871429 |  0.922561 |

## Result
The probabilistic representation creates an explicit accuracy–cost frontier. The benchmark does **not** reveal a universal threshold.

The risk-weighted rule is only justified if it beats probability-only at comparable extractor quality and safety. Otherwise its impact term is unnecessary complexity.

## Anti-PRION
- **ALLOW:** graded dependency confidence is mechanically usable for rollback.
- **ALLOW:** dependency policy can be calibrated against correctness and recomputation cost.
- **HOLD:** LLM calibration of dependency probabilities.
- **HOLD:** structural out-degree as epistemic impact.
- **BLOCK:** treating a threshold from this toy model as universal.

## Next — 227
Corrupt the complete epistemic loop independently:
`+3 claim → Shadow falsifier → Gate verdict → Bindu → dependency edge → repair`.

Measure which error source dominates and whether redundancy / asymmetric veto improves the failure boundary.
