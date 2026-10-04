# 222 — GATED + SHADOW OSCILLATORS

**Status:** SYNTHETIC DYNAMICAL FALSIFICATION TEST  
**Model:** Stuart–Landau coupled oscillators  
**Previous:** 221 — Blind Overlap × Alphabet-Height Search

## Hypothesis

221 showed that passive overlap can create cross-talk. 222 asks whether adding:

1. a nonlinear selective Gate, and
2. a suppressive/common-mode Shadow term

creates a non-zero optimum in overlap eta.

The canonical equal-circle Flower overlap under the fixed lens-area / one-circle-area definition is:

`eta_F = 0.3910` (~39.1%).

**This number is not used by the dynamics or objective.**

## Experimental design

- 12 local Stuart–Landau oscillators
- fixed ring-neighbor topology
- 25% damaged modules
- 60 seeds per eta
- eta scan: [np.float64(0.0), np.float64(0.1), np.float64(0.2), np.float64(0.3), np.float64(0.35), np.float64(0.39), np.float64(0.42), np.float64(0.5), np.float64(0.6), np.float64(0.75), np.float64(0.9)]
- FLOW condition: excitatory/diffusive coupling only
- GATE+SHADOW: nonlinear coherence Gate + suppressive common-mode term
- same weak external cue on surviving modules
- metrics:
  - M_loc: retention of undamaged phase-coded states
  - M_rec: recovery of erased modules
  - Mode separation: resistance to global synchronization
  - Balanced score: geometric mean

## Results

| Mode        |   eta |    M_loc |    M_rec |   Mode_separation |   Balanced_score |   Score_SD |
|:------------|------:|---------:|---------:|------------------:|-----------------:|-----------:|
| flow        |  0    | 0.998148 | 0.427778 |         0.968122  |         0.579478 |  0.386896  |
| flow        |  0.1  | 0.961111 | 0.577778 |         0.867107  |         0.735614 |  0.218484  |
| flow        |  0.2  | 0.825926 | 0.65     |         0.465888  |         0.59646  |  0.161003  |
| flow        |  0.3  | 0.672222 | 0.688889 |         0.20495   |         0.393802 |  0.165048  |
| flow        |  0.35 | 0.62037  | 0.666667 |         0.117956  |         0.314483 |  0.130604  |
| flow        |  0.39 | 0.588889 | 0.666667 |         0.0852994 |         0.270802 |  0.124032  |
| flow        |  0.42 | 0.566667 | 0.672222 |         0.0739005 |         0.248064 |  0.11926   |
| flow        |  0.5  | 0.527778 | 0.661111 |         0.0558517 |         0.199785 |  0.11761   |
| flow        |  0.6  | 0.511111 | 0.65     |         0.0319581 |         0.159175 |  0.0890109 |
| flow        |  0.75 | 0.496296 | 0.666667 |         0.0225193 |         0.132634 |  0.0727112 |
| flow        |  0.9  | 0.483333 | 0.672222 |         0.021705  |         0.116644 |  0.07086   |
| gate+shadow |  0    | 0.998148 | 0.427778 |         0.968122  |         0.579478 |  0.386896  |
| gate+shadow |  0.1  | 1        | 0.533333 |         0.957328  |         0.696452 |  0.32426   |
| gate+shadow |  0.2  | 0.996296 | 0.561111 |         0.948817  |         0.742748 |  0.263192  |
| gate+shadow |  0.3  | 0.974074 | 0.55     |         0.933936  |         0.71767  |  0.292385  |
| gate+shadow |  0.35 | 0.968519 | 0.561111 |         0.937713  |         0.737919 |  0.259138  |
| gate+shadow |  0.39 | 0.968519 | 0.55     |         0.943217  |         0.724199 |  0.275723  |
| gate+shadow |  0.42 | 0.959259 | 0.555556 |         0.946201  |         0.74061  |  0.242455  |
| gate+shadow |  0.5  | 0.931481 | 0.516667 |         0.947325  |         0.71517  |  0.24029   |
| gate+shadow |  0.6  | 0.898148 | 0.533333 |         0.940713  |         0.710873 |  0.239873  |
| gate+shadow |  0.75 | 0.827778 | 0.55     |         0.933957  |         0.685459 |  0.268431  |
| gate+shadow |  0.9  | 0.75     | 0.527778 |         0.977465  |         0.654274 |  0.270346  |

## Best by mode

| Mode        |   eta |    M_loc |    M_rec |   Mode_separation |   Balanced_score |   Score_SD |
|:------------|------:|---------:|---------:|------------------:|-----------------:|-----------:|
| flow        |   0.1 | 0.961111 | 0.577778 |          0.867107 |         0.735614 |   0.218484 |
| gate+shadow |   0.2 | 0.996296 | 0.561111 |          0.948817 |         0.742748 |   0.263192 |

## Verdict rules

- If GATE+SHADOW develops a reproducible interior optimum while FLOW does not, that supports the weaker claim that selective excitation + inhibition can make partial coupling useful.
- A peak near 0.391 would **not** prove Flower geometry; it would require replication under independent equations, tasks, parameters, and matched random topologies.
- If the optimum moves strongly when Shadow/Gate parameters move, then it is a dynamical tuning result, not a universal geometric constant.
- The statement "39.1% is a critical percolation point" is **not assumed** here and requires independent derivation/evidence.

## Anti-PRION

`ALLOW`: Gate/inhibition can be tested as mechanisms that protect distinguishability while allowing transfer.

`HOLD`: a privileged 35–42% overlap window.

`BLOCK`: claiming that the equal-circle overlap is a universal percolation threshold without independent proof.

## Next

222B should sweep Gate threshold and Shadow strength, not just eta, and test whether any eta optimum is stable:

`Performance(eta, gate_threshold, shadow_strength, frequency_spacing)`.

Then compare ring, random matched graph, triangular lattice, and Flower-like coupling using equal node/edge/energy budgets.
