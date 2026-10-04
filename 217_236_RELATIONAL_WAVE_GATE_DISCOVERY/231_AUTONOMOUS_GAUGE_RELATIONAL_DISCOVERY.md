# 231 — AUTONOMOUS GAUGE & RELATIONAL DISCOVERY

**Status:** executed synthetic falsification experiment.

## Important correction
Cross-geometry stability is evidence for invariance within the tested family, not proof of a universal physical grammar. Likewise, "gauge" is used here as a computational analogy unless an actual gauge symmetry/action and covariant observables are explicitly defined.

## Design
Three synthetic modal geometries A/B/C have different observation bases, spectral scales, and noise. Discovery receives neither the true leader nor the latent regime labels.

Pipeline:
1. rolling unsupervised local spectral estimate of a reference state;
2. relational projection `(S-L)/(|L|+eps)` plus transition vector;
3. blind K scan from 3 through 16;
4. train clusters on geometry A only;
5. transfer unchanged centroids to B and C;
6. compare transition matrices by Jensen-Shannon divergence;
7. negative control uses a temporally permuted/wrong leader.

Selection score was declared as:
`normalized reconstruction + 1.5*mean(JS transfer) + 0.5*dead-cluster penalty + 0.015*K`.

The exact weights are policy choices, so the full Pareto table is preserved.

## Selected models
| representation           |   K |   norm_reconstruction |    JS_A_B |    JS_A_C |   occupancy_B |   occupancy_C |   selection_score |
|:-------------------------|----:|----------------------:|----------:|----------:|--------------:|--------------:|------------------:|
| absolute                 |   4 |              0.536346 | 0.127338  | 0.0783659 |          0.75 |          0.25 |          1.00062  |
| self_discovered_relative |   8 |              0.464859 | 0.0472417 | 0.103346  |          1    |          1    |          0.6978   |
| wrong_leader_control     |   5 |              0.324624 | 0.143367  | 0.140087  |          0.8  |          0.6  |          0.762214 |

## Post-hoc hidden-regime evaluation
Hidden generator regimes were used only after model selection:
| representation           |   selected_K |   hidden_regime_purity_A |
|:-------------------------|-------------:|-------------------------:|
| absolute                 |            4 |                 0.310952 |
| self_discovered_relative |            8 |                 0.646429 |
| wrong_leader_control     |            5 |                 0.239762 |

Mean relative leader estimation error on geometry A:
`0.034795`

## Interpretation
This test is intentionally harder than 230 because the reference is estimated from the observed stream. If the relational representation still wins transfer while the wrong-leader control degrades, that supports the proposition that an inferred local reference can expose more transferable transition structure than absolute coordinates.

Failure to recover the generator's hidden K=5 is not automatically failure: the observable minimal alphabet can merge or split latent regimes. Conversely, recovering K=5 alone would not prove universality.

## Anti-PRION
ALLOW only what the measured transfer/reconstruction results support.
HOLD the term "gauge symmetry" until an explicit group action/covariance test is implemented.
HOLD universal alphabet claims until independent physical datasets reproduce the structure.
BLOCK treating synthetic cross-geometry success as proof about nature.
