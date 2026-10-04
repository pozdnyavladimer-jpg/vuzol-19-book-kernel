# 232 — GROUP-ACTION TEST OF THE RELATIONAL ALPHABET

**Status:** executed synthetic algebraic falsification test.

## Goal
Test the stronger statement suggested by 231:
`R(gS,gL) = R(S,L)`
for an explicitly defined group action, plus composition and inverse controls.

This is still not a claim that the system is a physical gauge theory. In actual gauge theories, local symmetry transformations can be position/time dependent and physical observables are invariant/equivalent under the gauge redundancy. Here we test a simpler global group-action analogue.

## Explicit transformation group
For positive frequency/amplitude/time scales and circular phase:
`g=(s_f,s_A,s_t,theta)`
acts as
- `f -> s_f f`
- `A -> s_A A`
- `tau -> s_t tau`
- `phi -> phi + theta (mod 2pi)`

Relational observable:
`R(S,L) = ((fS-fL)/fL, cos Δphi, sin Δphi, log(AS/AL), log(tS/tL))`.

## Exact algebraic tests
| test                        |   mean_abs_error |   p95_abs_error |   max_abs_error |
|:----------------------------|-----------------:|----------------:|----------------:|
| covariant_same_action       |      7.4432e-17  |     3.88578e-16 |     1.77636e-15 |
| composition_relational      |      1.02775e-16 |     4.44089e-16 |     3.10862e-15 |
| inverse_return              |      7.33211e-17 |     3.33067e-16 |     2.58127e-15 |
| state_only_negative_control |      0.63349     |     1.7458      |    19.9304      |

## Cluster/Rune identity stability
|   K |   same_action_rune_stability |   state_only_rune_stability |
|----:|-----------------------------:|----------------------------:|
|   3 |                            1 |                    0.329433 |
|   4 |                            1 |                    0.287833 |
|   5 |                            1 |                    0.259167 |
|   6 |                            1 |                    0.224867 |
|   7 |                            1 |                    0.199033 |
|   8 |                            1 |                    0.177867 |
|   9 |                            1 |                    0.160333 |
|  10 |                            1 |                    0.1502   |
|  11 |                            1 |                    0.136333 |
|  12 |                            1 |                    0.130067 |
|  13 |                            1 |                    0.118667 |
|  14 |                            1 |                    0.1129   |
|  15 |                            1 |                    0.109467 |
|  16 |                            1 |                    0.1008   |

## Imperfect reference estimate
|   leader_noise_sigma |   relational_MAE |   K8_rune_stability |
|---------------------:|-----------------:|--------------------:|
|                 0    |       7.4432e-17 |            1        |
|                 0.01 |       0.00681388 |            0.9743   |
|                 0.03 |       0.020392   |            0.9224   |
|                 0.05 |       0.0341116  |            0.875067 |
|                 0.1  |       0.0679271  |            0.761067 |
|                 0.2  |       0.136929   |            0.592467 |
|                 0.35 |       0.239761   |            0.447333 |

## Interpretation
For this explicitly constructed global action, the relational observable is mathematically designed to be invariant when State and Leader transform covariantly. Composition and inverse therefore test implementation consistency, not discovery of a new law.

The nontrivial falsifier is the state-only control: if State is transformed without its reference, relational identity should change. The noisy-Leader test measures robustness when the reference must be estimated rather than known exactly.

## Anti-PRION
ALLOW: the proposed relational coordinates form invariants under the explicitly defined global scale/phase group.
ALLOW: cluster/Rune identity can therefore be represented on equivalence classes (orbits) of this action.
HOLD: calling this a physical gauge theory.
HOLD: extension from global transformations to local g(x,t), which requires a connection/covariant derivative.
BLOCK: interpreting exact invariance here as empirical proof about nature; it follows from the chosen mathematical construction.

## Next decisive test
233 should use local transformations `g(x,t)` on a coupled spatial field. Ordinary differences cease to be invariant. Introduce or learn a connection/parallel-transport term and test whether a covariant relational alphabet transfers across local gauge choices. That would be the first test genuinely structurally analogous to gauge theory rather than global normalization.
