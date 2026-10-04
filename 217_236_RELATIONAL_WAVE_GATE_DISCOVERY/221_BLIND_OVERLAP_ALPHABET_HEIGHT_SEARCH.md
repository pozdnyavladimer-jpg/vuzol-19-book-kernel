# 221 — BLIND OVERLAP × ALPHABET-HEIGHT SEARCH

**Status:** SYNTHETIC FALSIFICATION EXPERIMENT / NOT PHYSICAL EVIDENCE  
**Previous:** 220 — Wave Alphabet Height / Overlap Phase Diagram

## Question

Without encoding Flower geometry, does a coupled-mode memory toy model develop an interior optimum in:

`overlap eta × spectral/alphabet separation delta_h`?

## Search

- eta = [np.float64(0.0), np.float64(0.15), np.float64(0.3), np.float64(0.45), np.float64(0.6), np.float64(0.75), np.float64(0.9)]
- delta_h = [np.float64(0.25), np.float64(0.5), np.float64(0.75), np.float64(1.0), np.float64(1.5), np.float64(2.0), np.float64(3.0)] linewidth units
- 12 local modules
- 25% modules erased
- 80 random seeds per grid point
- topology fixed; Flower geometry not supplied
- metrics: locality retention, associative recovery, capacity proxy
- balanced score = geometric mean of the three metrics

## Best synthetic point

- eta = 0.00
- delta_h = 3.00
- M_loc = 0.887
- M_rec = 0.471
- Capacity = 1.000
- Balanced score = 0.668

## Important Flower comparison

For two equal circles of radius R whose centers are separated by R, the exact **area overlap fraction of one circle** is:

`eta_F = [2 acos(1/2) - sqrt(3)/2] / pi = 0.3910`

or about `39.1%`.

Therefore the earlier guess that canonical Flower overlap is 35–45% was incorrect **if eta means shared lens area divided by one circle's area**.

This experiment must not redefine eta after seeing the result.

## Top 10

|   eta |   delta_h |   M_loc |    M_rec |   Capacity |   Balanced_score |   Score_SD |
|------:|----------:|--------:|---------:|-----------:|-----------------:|-----------:|
|  0    |       3   |  0.8875 | 0.470833 |   1        |         0.667757 |   0.270111 |
|  0    |       2   |  0.8875 | 0.470833 |   0.999923 |         0.66774  |   0.270104 |
|  0    |       1.5 |  0.8875 | 0.470833 |   0.995134 |         0.666672 |   0.269672 |
|  0.3  |       2   |  0.8875 | 0.5125   |   0.935128 |         0.663895 |   0.294487 |
|  0.3  |       1.5 |  0.8875 | 0.516667 |   0.930649 |         0.658391 |   0.304276 |
|  0.3  |       3   |  0.8875 | 0.4875   |   0.9352   |         0.652622 |   0.289196 |
|  0    |       1   |  0.8875 | 0.470833 |   0.906226 |         0.646195 |   0.261389 |
|  0.15 |       1.5 |  0.8875 | 0.483333 |   0.979013 |         0.641577 |   0.32092  |
|  0.45 |       2   |  0.8875 | 0.5125   |   0.854134 |         0.639145 |   0.294568 |
|  0.15 |       2   |  0.8875 | 0.4625   |   0.983724 |         0.638616 |   0.307322 |

## Anti-PRION interpretation

1. An interior optimum can appear when the scoring function simultaneously rewards local retention, recovery and distinguishability.
2. This does **not** prove that nature chooses that optimum.
3. It does **not** prove Flower geometry.
4. The exact optimum depends on the chosen dynamics, noise model, spectral coupling law and capacity definition.
5. Under the explicit lens-area / one-circle-area definition, the canonical equal-circle Flower overlap is about 39.1%. Other definitions of overlap produce other percentages, so eta must be defined before testing.
6. The next test should replace the synthetic capacity proxy and hand-written coupling law with measured or independently simulated oscillator/material dynamics.

## Falsification target for 222

Use actual coupled-oscillator equations (e.g. Stuart-Landau or Kuramoto-type local oscillators) and infer:
- phase locking,
- recoverability after damage,
- mode distinguishability,
- energy/damping cost,

while eta changes only the physical coupling graph/strength. Compare against matched random coupling matrices.

