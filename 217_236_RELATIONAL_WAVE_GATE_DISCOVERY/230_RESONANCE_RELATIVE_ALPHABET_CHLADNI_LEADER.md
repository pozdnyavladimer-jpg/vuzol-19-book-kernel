# 230 — RESONANCE-RELATIVE ALPHABET / CHLADNI-LEADER TEST

**Status:** executed synthetic falsification experiment; Chladni is used as a physical analogy to modal/nodal structure, not as evidence for a universal cosmic language.

## Hypothesis
A useful transition alphabet may not live at fixed absolute frequencies/phases. It may be defined relative to the currently dominant resonant mode ("leader") of the bounded system.

`absolute symbol = weak hypothesis`
`operator relative to leader mode = tested hypothesis`

## Synthetic systems
Six heterogeneous resonant systems were generated with different:
- base resonant frequency,
- phase/orientation,
- gain,
- persistence time scale.

Five hidden transition roles were generated only for scoring:
FOLLOW, OPPOSE, CROSS, LOCK, RELEASE.

Two representations were compared blindly:
1. Absolute: `(f, phase, amplitude, persistence)`
2. Leader-relative: `(Δf/f_leader, Δphase_to_leader, A/A_leader, τ/τ_system)`

K-means received no role labels.

## Blind clustering
|   noise |   absolute_purity |   absolute_sd |   leader_relative_purity |   relative_sd |
|--------:|------------------:|--------------:|-------------------------:|--------------:|
|    0.03 |          0.496347 |     0.0742554 |                 0.85776  |     0.105732  |
|    0.06 |          0.510773 |     0.0710254 |                 0.914293 |     0.0967481 |
|    0.1  |          0.475187 |     0.061752  |                 0.87484  |     0.0929639 |
|    0.15 |          0.485293 |     0.0437624 |                 0.91924  |     0.091954  |

## Transfer to unseen shifted resonant geometry
|   noise |   absolute_transfer |   absolute_sd |   leader_relative_transfer |   relative_sd |
|--------:|--------------------:|--------------:|---------------------------:|--------------:|
|    0.03 |            0.405267 |      0.194717 |                   1        |   0           |
|    0.06 |            0.41055  |      0.208124 |                   0.999983 |   0.000165831 |
|    0.1  |            0.416383 |      0.209195 |                   0.99905  |   0.00120773  |
|    0.15 |            0.410733 |      0.207673 |                   0.989167 |   0.00381153  |

## Falsification by corrupting the leader estimate
|   leader_estimation_error |   relative_cluster_purity |        sd |
|--------------------------:|--------------------------:|----------:|
|                      0    |                  0.869417 | 0.108654  |
|                      0.02 |                  0.872681 | 0.10957   |
|                      0.05 |                  0.887347 | 0.113476  |
|                      0.1  |                  0.926306 | 0.086985  |
|                      0.2  |                  0.815292 | 0.0589727 |
|                      0.35 |                  0.552625 | 0.0250166 |

## Interpretation
If leader-relative representation clusters and transfers better, the result supports a *relational alphabet*: symbols are invariant transition roles relative to a local resonant reference, not fixed global frequencies.

If corrupting the leader destroys clustering, that is also informative: the alphabet is conditional on correctly estimating the dominant mode. The "leader" is therefore not mystical; it is an experimentally estimable reference state/eigenmode/resonant mode.

## Connection to Chladni physics
Known Chladni figures are nodal patterns associated with resonant vibration modes of bounded plates. Different resonant frequencies produce different nodal forms, and experimental resonant modes need not be in one-to-one correspondence with ideal theoretical eigenmodes. Thus a physically defensible version of "leader creates rules of form" is:

`boundary conditions + material + drive -> resonant modal mixture -> dominant mode -> nodal/antinodal geometry`

not:

`frequency alone -> universal shape law`.

## Anti-PRION
ALLOW: relational coordinates can be more transferable than absolute coordinates in heterogeneous resonant systems.
ALLOW: a dominant mode can serve as a local reference frame for transition grammar.
HOLD: natural physical systems universally implement the five toy roles.
HOLD: this is a cosmic alphabet.
BLOCK: Chladni leader as an independent agency that creates physical laws.
BLOCK: fixed frequency uniquely determines form independent of boundary/material/drive.
