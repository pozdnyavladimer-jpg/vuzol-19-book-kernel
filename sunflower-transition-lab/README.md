# SUNFLOWER_SRI3D_RESEARCH

Status: **RESEARCH / MODEL / HOLD**

This folder is a focused research branch for testing whether the Flower/Sri transition architecture can expose useful structure in the Erdős–Rado Sunflower problem.

It should remain separate from the main BOOT specification.

Why separate?

- `00_BOOT_FLOWER_SRI_TRANSITION_ARCHITECTURE_v0.3.0.md` defines the general architecture.
- This folder contains one speculative mathematical application.
- A failure here must not weaken or silently rewrite the generic BOOT contract.
- A successful result can later be promoted back into BOOT only after independent verification.

## Files

- `01_SUNFLOWER_SRI3D_TRANSITION_RESEARCH.md` — mathematical research note and current hypothesis.
- `02_EXPERIMENT_PLAN.md` — exact computational tests to run next.
- `sunflower_sri3d_toy.py` — small reproducible toy experiment for provenance-aware projection.

## Core rule

Do **not** assume Fibonacci.

The research question is:

> If sunflower-free set families are encoded as provenance-preserving transition trajectories, does a stable recurrence or descent law emerge across ranks?

Fibonacci is only one possible recurrence pattern. It must be discovered from data, not inserted by analogy.

## Relation to Vuzol-19

World Theory already uses the model-language:

```text
memory route
→ Sri rotations
→ Flower audit
→ 3D form
```

This folder asks whether an analogous representation is mathematically useful for set-family transitions:

```text
set family
→ choose role/orientation
→ core/petal decomposition
→ provenance-preserving reduction
→ Shadow/conflict audit
→ lift check
→ next rank
```

No claim is made that Sri Yantra geometry is literally present in combinatorics.
