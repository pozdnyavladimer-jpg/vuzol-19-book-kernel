# 229 — BLIND DECOUPLED CONTACT SIMULATION

**Status:** executed synthetic falsification experiment. Not evidence of extraterrestrial language.

## Question
Can a receiver with no semantic labels infer a small procedural grammar from noisy physical tuples `(f, phase, duration, amplitude)`, and does explicit negative-example / BLOCK / UNWIND training add a capability absent from positive-only training?

## Physical correction
`H=f/f0` is invariant under a common multiplicative frequency shift applied to the whole local packet. This models an idealized common Doppler/redshift factor. It is not claimed to survive arbitrary time-varying, dispersive, multipath, or independently shifted channels.

## Setup
- Sender emits only numeric physical tuples.
- Receiver gets no `FLOW`, `BLOCK`, `UNWIND`, `COMMIT` labels.
- A blind 5-cluster k-means operates on circular phase features, normalized duration/amplitude, and normalized frequency.
- Cluster semantics are revealed only after training for evaluation.
- Common frequency multiplier is randomized per trial in `[0.65,1.55]`.
- Noise levels: 3%, 5%, 7%, 10%.
- 150 trials per condition.
- Positive-only control has arithmetic examples but no negative correction examples.
- Shadow condition includes wrong results followed by two distinct latent physical events (BLOCK and UNWIND) and a corrected result.
- Zero-shot arithmetic asks whether the inferred arithmetic rule predicts unseen `5+3`.
- Full zero-shot additionally requires distinct discovery of both correction event families.

## Results
|   noise | shadow_training   |   cluster_purity |   ratio_MAE |   arithmetic_success |   correction_vocab |   full_zero_shot |
|--------:|:------------------|-----------------:|------------:|---------------------:|-------------------:|-----------------:|
|    0.03 | False             |         0.938431 |   0.0731597 |             0.946667 |          0         |                0 |
|    0.03 | True              |         0.797749 |   0.0905813 |             0.666667 |          0.02      |                0 |
|    0.05 | False             |         0.938824 |   0.118655  |             0.853333 |          0         |                0 |
|    0.05 | True              |         0.779913 |   0.128703  |             0.46     |          0.0266667 |                0 |
|    0.07 | False             |         0.932059 |   0.1532    |             0.793333 |          0         |                0 |
|    0.07 | True              |         0.781212 |   0.163158  |             0.353333 |          0.0133333 |                0 |
|    0.1  | False             |         0.922941 |   0.181951  |             0.666667 |          0         |                0 |
|    0.1  | True              |         0.769957 |   0.194656  |             0.253333 |          0.02      |                0 |

## Common-shift ratio control
|   common frequency multiplier |   max ratio error |
|------------------------------:|------------------:|
|                          0.55 |       0           |
|                          0.8  |       4.44089e-16 |
|                          1    |       0           |
|                          1.35 |       4.44089e-16 |
|                          1.8  |       0           |

## Interpretation
The key comparison is positive-only vs Shadow training. Positive-only may infer arithmetic, but by construction it has no observational evidence from which to infer distinct BLOCK and UNWIND operations. Shadow training can make those event classes identifiable if the physical encoding remains separable under noise.

This demonstrates *identifiability in this toy protocol*, not universality. The phase/duration/amplitude event families were deliberately designed to be distinguishable, so discovering them is weaker than discovering a natural alphabet.

## Anti-PRION
ALLOW: dimensionless frequency ratios cancel a common multiplicative shift.
ALLOW: negative examples can transmit information about correction semantics unavailable in positive-only examples.
ALLOW: separate physical dimensions can solve delimiter/operator ambiguity in a designed protocol.
HOLD: this grammar is optimal for interstellar communication.
HOLD: five operator families are universal.
BLOCK: claiming this proves extraterrestrial civilizations communicate this way.
BLOCK: claiming H is invariant under arbitrary channel distortions.

## Next falsification
230 should remove the hand-designed phase prototypes. Sender should be optimized only for decodability under an energy/bandwidth budget, while Receiver jointly performs blind segmentation and grammar induction. If FLOW/BLOCK/UNWIND-like roles emerge repeatedly across random initializations and channel models, that would be substantially stronger evidence for the operator decomposition.
