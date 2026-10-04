# 233 — LOCAL GAUGE, CONNECTION, AND HOLONOMY

**Status:** executed synthetic U(1)-like field test.

## Construction
Each lattice node has a phase `phi_i`. A local gauge transformation independently changes every node:
`phi_i -> phi_i + theta_i`.

An oriented edge carries a connection:
`A_ij -> A_ij + theta_j - theta_i`.

The covariant edge observable is:
`C_ij = wrap(phi_j - phi_i - A_ij)`.

Unlike experiment 232, this is a local transformation: every node may have a different theta.

## Results
| test                               |   mean_circular_error |         p95 |         max |
|:-----------------------------------|----------------------:|------------:|------------:|
| naive_edge_phase_after_local_gauge |           1.53498     | 3.01285     | 3.13115     |
| covariant_edge_after_local_gauge   |           2.59737e-16 | 8.88178e-16 | 1.77636e-15 |
| wrong_connection_control           |           1.53498     | 3.01285     | 3.13115     |
| holonomy_after_local_gauge         |           4.08746e-16 | 8.88178e-16 | 1.77636e-15 |

## Holonomy
For a closed loop, connection holonomy is the oriented sum of edge connections modulo 2pi.
| case                          |   mean_abs_holonomy |   p95_abs_holonomy |
|:------------------------------|--------------------:|-------------------:|
| pure_gauge_connection         |          1.9208e-16 |        8.88178e-16 |
| curved_connection_before      |          0.12       |        0.12        |
| curved_connection_after_gauge |          0.12       |        0.12        |

Pure-gauge connections generated as `A_ij = chi_j-chi_i` have zero elementary-loop holonomy up to floating-point precision. A connection with injected curvature/flux has nonzero holonomy, and that holonomy survives arbitrary local gauge transformations.

## Learning transport
A fixed unknown local gauge transformation was inferred from 120 noisy paired phase snapshots using circular statistics:
|   paired_snapshots |   mean_connection_error |   p95_connection_error |   max_connection_error |
|-------------------:|------------------------:|-----------------------:|-----------------------:|
|                120 |              0.00330887 |             0.00806798 |              0.0124779 |

## Interpretation
This establishes the expected mathematical distinction:
- ordinary local phase differences are gauge-dependent;
- a connection allows covariant comparison between different local reference frames;
- closed-loop holonomy is gauge-invariant;
- pure coordinate change gives zero curvature/holonomy, while injected curvature survives gauge changes.

This is a synthetic implementation of U(1)-like geometry, not evidence that Chladni plates or nature's "alphabet" literally use this gauge field.

## Consequence for the relational alphabet
The natural extension is no longer a Rune attached only to a node. A relational symbol can live on an edge:
`Rune_ij = F(State_i, State_j, A_ij)`.
A loop then carries a higher-order invariant:
`Holonomy(loop) = product/sum of transports around the loop`.

This supplies a rigorous candidate meaning for the earlier Flower/cycle intuition: not "a cycle automatically stores memory", but "a connection can possess gauge-invariant loop structure when curvature is present."

## Anti-PRION
ALLOW: local-reference comparison mathematically requires transport information if local gauges differ.
ALLOW: loop holonomy is invariant under the explicit U(1)-like transformation tested here.
ALLOW: pure-gauge and curved connections are distinguishable by loop holonomy.
HOLD: learned connections arising spontaneously in physical Chladni/reservoir data.
HOLD: Flower geometry as privileged topology.
BLOCK: claiming any graph cycle automatically has physical memory or curvature.
BLOCK: treating this synthetic gauge construction as empirical evidence of a new force/law.
