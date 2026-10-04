# 236 — LEADER COMPETITION / SPECTRAL-GAP COLLAPSE AS A GATE PREDICTOR

**Status:** executed synthetic driven-membrane falsification test.

## Independent measurements
Leader metrics come only from modal response weights:
- dominance = W1 / sum(W)
- normalized leader gap = (W1-W2)/(W1+W2)
- gap collapse = 1-gap
- modal entropy = normalized entropy of modal weights

Form/topology is measured independently from the spatial field using sign-boundary count and low-amplitude connected components.

## Prediction of the next major form transition
| predictor_t         |   AUC_next_major_transition |   shuffle_mean |   shuffle_p95 |   shuffle_p |
|:--------------------|----------------------------:|---------------:|--------------:|------------:|
| gap_collapse        |                    0.436535 |       0.502147 |      0.565932 |  0.96005    |
| dominance_loss      |                    0.388054 |       0.500844 |      0.565985 |  0.997503   |
| modal_entropy       |                    0.386412 |       0.501116 |      0.566936 |  0.998752   |
| defect_count        |                    0.502155 |       0.499387 |      0.563713 |  0.480649   |
| current_form_change |                    0.716195 |       0.50095  |      0.563679 |  0.00124844 |

## One-step rank correlations
| predictor_t         | target_t_plus_1         |   spearman_r |     p_value |
|:--------------------|:------------------------|-------------:|------------:|
| gap_collapse        | future_form_change      |  0.0519235   | 0.289548    |
| gap_collapse        | future_component_change | -0.000401592 | 0.993469    |
| dominance_loss      | future_form_change      | -0.00330026  | 0.946365    |
| dominance_loss      | future_component_change |  0.045753    | 0.350764    |
| modal_entropy       | future_form_change      | -0.00161894  | 0.973674    |
| modal_entropy       | future_component_change |  0.104069    | 0.0334121   |
| defect_count        | future_form_change      |  0.0304496   | 0.534716    |
| defect_count        | future_component_change |  0.473775    | 8.92122e-25 |
| current_form_change | future_form_change      |  0.401309    | 1.3201e-17  |
| current_form_change | future_component_change |  0.0270175   | 0.581757    |

## Strongest positive lead for each candidate
| predictor      |   lag_positive_means_predictor_leads |   spearman_r |
|:---------------|-------------------------------------:|-------------:|
| gap_collapse   |                                    8 |    0.0811    |
| dominance_loss |                                    8 |    0.0672972 |
| modal_entropy  |                                    8 |    0.0269795 |
| defect_count   |                                    4 |    0.0366938 |

## Incremental held-out value
A simple combination of current form inertia and gap collapse was tuned only on even-index sweep steps and evaluated on odd-index steps:
|   best_alpha_gap_from_even_steps |   train_AUC |   heldout_odd_AUC |   heldout_current_form_only_AUC |   heldout_gap_only_AUC |
|---------------------------------:|------------:|------------------:|--------------------------------:|-----------------------:|
|                                0 |    0.690924 |          0.740045 |                        0.740045 |               0.406631 |

## Interpretation rule
Evidence for `Leader competition -> Gate` requires all of:
1. AUC above shuffled controls;
2. positive-lag association (competition precedes form change);
3. incremental held-out value beyond current form-change inertia.

If one or more fail, the strong Gate interpretation remains HOLD/BLOCK for this model.

## Anti-PRION
ALLOW only measured predictive relations.
HOLD causal interpretation without intervention.
HOLD extension to real plates.
BLOCK treating a small spectral gap as universally sufficient for a phase transition.
