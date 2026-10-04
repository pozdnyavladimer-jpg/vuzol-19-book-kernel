# 235 — PHASE DEFECTS AS PREDICTORS OF NODAL-TOPOLOGY TRANSITIONS

**Status:** executed numerical frequency-sweep prediction test.

## Generator
A driven damped rectangular membrane-like field was formed from 49 eigenmodes. Each mode has a complex Lorentzian response to sweep frequency. No phase defects, topology-transition labels, or predictive relation was inserted manually.

At each of 360 frequencies we measured independently:
- phase winding defects on plaquettes;
- connected low-amplitude/nodal regions;
- nearest-neighbor sign-boundary count of the real displacement field;
- amplitude statistics.

The primary question was temporal/order predictive:
does defect information at frequency step `t` predict a large topology change at `t+1`?

## One-step correlations
| predictor_t              | target_t_plus_1         |   spearman_r |     p_value |
|:-------------------------|:------------------------|-------------:|------------:|
| defect_map_change        | future_component_change |    0.579625  | 1.623e-33   |
| defect_map_change        | future_signedge_change  |    0.118788  | 0.024597    |
| defect_count             | future_component_change |    0.596144  | 8.00832e-36 |
| defect_count             | future_signedge_change  |    0.0503478 | 0.342165    |
| current_component_change | future_component_change |    0.451478  | 2.21522e-19 |
| current_component_change | future_signedge_change  |    0.0731371 | 0.167332    |
| current_signedge_change  | future_component_change |    0.133376  | 0.011535    |
| current_signedge_change  | future_signedge_change  |    0.434783  | 6.09256e-18 |
| mean_amp                 | future_component_change |   -0.348973  | 1.08641e-11 |
| mean_amp                 | future_signedge_change  |   -0.0643303 | 0.224676    |
| low_amp_threshold        | future_component_change |   -0.283217  | 4.98071e-08 |
| low_amp_threshold        | future_signedge_change  |   -0.090882  | 0.0859592   |

## Major-transition prediction
Major transition = top 15% of next-step sign-boundary changes.
| predictor               |   AUC_next_major_transition |   shuffle_mean |   shuffle_p95 |   shuffle_p |
|:------------------------|----------------------------:|---------------:|--------------:|------------:|
| defect_map_change       |                    0.499543 |       0.500007 |      0.563816 |  0.491018   |
| defect_count            |                    0.470245 |       0.499542 |      0.560365 |  0.772455   |
| current_signedge_change |                    0.654157 |       0.498882 |      0.558723 |  0.00199601 |
| inverse_mean_amp        |                    0.487275 |       0.503104 |      0.570842 |  0.650699   |

## Lead/lag
Positive lag means defect-map change is compared with a later topology change.
|   lag_positive_means_defects_lead |   spearman_r |
|----------------------------------:|-------------:|
|                                -6 |    0.058761  |
|                                -5 |    0.0810142 |
|                                -4 |    0.120888  |
|                                -3 |    0.116937  |
|                                -2 |    0.147085  |
|                                -1 |    0.154657  |
|                                 0 |    0.127961  |
|                                 1 |    0.118788  |
|                                 2 |    0.112928  |
|                                 3 |    0.0687984 |
|                                 4 |    0.0762674 |
|                                 5 |    0.042019  |
|                                 6 |    0.0265252 |

Best AUC predictor: `current_signedge_change`, AUC=0.6542.
Strongest absolute lead/lag correlation occurred at lag -1, r=0.1547.

## Interpretation
This test distinguishes simultaneous association from predictive ordering. A useful Shadow→Gate interpretation requires defects to lead future topology changes, not merely co-occur with low amplitude or resonance.

AUC near 0.5 or a peak at lag 0/negative lag falsifies the strong predictive claim. A reproducible positive-lag peak and AUC above shuffled controls would support defects as early-warning variables within this membrane model, but still would not establish causation.

## Anti-PRION
ALLOW only the measured predictive advantage over shuffled and baseline variables.
HOLD causal language unless intervention on defects changes the later topology.
HOLD extension to real Chladni plates until measured amplitude+phase data reproduce it.
BLOCK interpreting resonance co-occurrence alone as Shadow causing form change.
