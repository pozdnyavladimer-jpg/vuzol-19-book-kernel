# 216 — HARDER BLIND ARCHITECTURE TEST

Synthetic falsification benchmark. This is **not evidence that 14/10/10/8 is a law of nature**.

## Task
42 noisy channels contain a hidden reliable subset. Persistent weights must accumulate experience. Fixed has no learning; Adaptive writes every candidate; Gate writes only strong local candidates; Cascade filters candidate evidence through compressed nonlinear spaces before commit.

## Results
| Mode | Accuracy | Seed SD | Mean writes |
|---|---:|---:|---:|
| Fixed | 0.5083 | 0.0000 | 0 |
| Adaptive | 0.9917 | 0.0000 | 58800 |
| Gate | 0.9917 | 0.0000 | 21928 |
| Proposed 42→14→10→8 | 0.9917 | 0.0000 | 16800 |
| Blind best 42→32→16→12 | 0.9917 | 0.0000 | 16800 |

## Anti-PRION reading
The blind search was not told to prefer 14/10/10/8. Therefore the proposed widths should only be interesting if they repeatedly outperform alternatives under fair validation, equal budgets, different tasks, and eventually a physical experiment.

This toy is a programming demonstration, not a scientific validation.
