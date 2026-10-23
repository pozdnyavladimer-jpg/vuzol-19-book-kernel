# Flower Evolution Engine v6.0

Python prototype of the **Sri-6D / Flower Evolution** decision engine, with `+3` candidate selection, `-3` reverse-loss evaluation, a Bindu score and optional loss-signature memory.

## Quick start

Requires **Python 3.9+**. No third-party packages required.

```bash
python flower_evolution_engine.py
```

This prints a seeded synthetic benchmark and runs the three built-in `unittest` checks. An unsuccessful test run returns a nonzero exit code.

## Components

- `DomainAdapters`: converts supplied material-property records and Python AST features to 14-dimensional inputs.
- `FlowerEvolutionEngine`: `14 → 10▲ / 10▽ → 8 invariants → 6D`, followed by `plus3`, `minus3_and_gate`, and `remember_outcome`.
- `GreedyRiskMinimizer` and `MultiObjectiveScalarizer`: benchmark comparators.
- `BlindEnvironmentSimulator`: generates synthetic tasks with latent failure parameters and evaluates simulated outcomes.
- `run_full_scientific_benchmark(seed=20261023, n_tasks_per_domain=60)`: reproduces the default 120-task example.

## Interpretation / limitations

**The reported performance is from a designed synthetic simulation, not an externally validated prediction of real-world material behavior or software reliability.** The hard-coded material-property records are example inputs, not independently sourced datasets. The AST adapter produces heuristic feature scores; it is not a substitute for static analysis, execution, or security testing. The benchmark's two domains use a shared synthetic task generator, so success here does not on its own establish cross-domain transfer in real systems. Some tests assert outcomes for one fixed random seed.

## GitHub Actions

The included workflow runs the script, including its embedded unit tests, on pushes and pull requests. Upload the entire ZIP contents to the root of a repository to enable it. To upload just the engine, use `flower_evolution_engine.py` alone.
