# SRI Structural Observability Engine

**Research scaffold for testing structured state search, GF(2) observability, consequence checks, and gated decisions.**

> AI may propose transitions. Shadow must expose unresolved consequences. Gate must verify admissibility. Bindu may commit only verified states. Memory must preserve the evidence.

## 1. Purpose

This repository develops and tests a computational framework for exploring structured state spaces.

The project brings together several ideas:

- **CASR** — constrained/admissible state search and candidate ranking.
- **+3 / −3** — paired forward-proposal and reverse-audit operations.
- **Shadow** — a record of unresolved differences, dependencies, uncertainty, and failed checks.
- **GF(2) observability** — binary parity and matrix-rank checks used to inspect whether selected signals are independent.
- **9V Consequence Tensor** — a proposed downstream-consequence audit before a candidate is accepted.
- **Gate** — an explicit admissibility check.
- **Bindu** — the final decision point: allow, hold, repair, rewrite, or block.
- **MemoryAtom** — a durable record of the decision and its evidence.

These names describe software roles and research abstractions. They do not, by themselves, establish a physical mechanism in atoms, nuclei, photons, or biological systems.

## 2. What this repository is — and is not

### It is

- A reproducible computational research project.
- A place to formalize state representations, constraints, candidate transitions, and audit rules.
- A place to compare the proposed method against fair, clearly specified baselines.
- A place to preserve test results, assumptions, and unresolved questions.

### It is not

- Proof that the Flower or Sri geometry is a fundamental physical structure.
- Proof that a GF(2) rank result implies physical observability in a laboratory system.
- Proof of a computational advantage until matched benchmarks demonstrate one.
- An autonomous system authorized to make real-world changes without human approval.

## 3. Core processing model

The intended logical pipeline is:

```text
INPUT
  |
  v
STATE REPRESENTATION
  |
  +----> SHADOW AUDIT: uncertainty, dependencies, residuals
  |
  v
+3 FORWARD PROPOSALS
  |
  v
CANDIDATE TRANSITIONS
  |
  v
-3 REVERSE / INVERSE AUDIT
  |
  v
CONSTRAINTS + GF(2) CHECKS + 9V CONSEQUENCE CHECK
  |
  v
GATE
  |
  v
BINDU VERDICT
  |       |        |         |
 ALLOW   HOLD    REPAIR    BLOCK
  |
  v
MEMORY RECORD
```

The diagram is a software workflow. It should be implemented as explicit functions and tested at each boundary.

## 4. Decision principles

1. A generated candidate is not automatically an admissible state.
2. Forward search and reverse audit must be evaluated separately.
3. A passing parity check is not sufficient evidence of physical observability.
4. Every threshold must have a documented meaning and a sensitivity test.
5. A benchmark must compare methods under the same constraints and search budget.
6. Failed, rejected, and uncertain candidates must remain visible in the audit record.
7. Human approval is required before any consequential external action.

## 5. Evidence labels

Every result in this repository should use one of these labels:

| Label | Meaning |
|---|---|
| `VERIFIED` | Reproduced by an executable test or independently checked derivation. |
| `OBSERVED` | Produced by an experiment, but not yet independently established. |
| `HYPOTHESIS` | A proposed explanation or expected relationship that still needs testing. |
| `ASSUMPTION` | A condition deliberately imposed by the model or experiment. |
| `OPEN` | An unresolved question, limitation, or missing test. |

Do not describe a hypothesis or a single experimental observation as a proven theorem.

## 6. Repository map

The planned documentation sequence is:

| File | Responsibility |
|---|---|
| `00_MASTER_BOOT.md` | Instructions and execution order for a new AI/research agent. |
| `01_CANON_AND_PHYSICAL_BOUNDARIES.md` | Project terminology, definitions, and limits on physical interpretation. |
| `02_MATHEMATICAL_MODEL.md` | Formal state space, operators, invariants, and equations. |
| `03_CASR_SEARCH_ENGINE.md` | Candidate generation, constraints, scoring, and search procedure. |
| `04_GF2_OBSERVABILITY_AND_9V.md` | Binary parity, matrix rank, observability checks, and consequence audit. |
| `05_EXPERIMENTS_AND_BASELINES.md` | Reproducible experiments, controls, metrics, and benchmark rules. |
| `06_AI_AGENT_TASK_PROTOCOL.md` | Roles, task boundaries, evidence requirements, and review protocol. |

Planned implementation areas:

```text
src/
  state_space.py
  shadow_engine.py
  casr_solver.py
  gf2_engine.py
  consequence_tensor.py
  gate_operator.py
  memory_atoms.py

tests/
  test_xor_invariant.py
  test_gf2_rank.py
  test_nine_rotations.py
  test_36_permutations.py
  test_random_baselines.py

experiments/
  v1_reproduction.py
  v2_observability.py
  monte_carlo_control.py

reports/
  VERIFIED_RESULTS.md
  OPEN_HYPOTHESES.md
```

This is the intended structure; files and modules should be marked as planned until they actually exist.

## 7. Initial research questions

The first research stage should answer these questions:

1. Can the stated integer examples and their derived values be reproduced exactly?
2. Which invariants follow mathematically from the definitions, independently of the search algorithm?
3. Does the proposed search find valid candidates more efficiently than matched baselines?
4. Does the GF(2) audit reveal independent information, or does an invariant force one syndrome to depend on the others?
5. Do the 9V checks reject candidates that pass local constraints but fail downstream requirements?
6. Are the results robust to changes in thresholds, input distributions, and search budgets?

## 8. Minimum standard for a reported result

A result is not ready to be called verified until its report includes:

- exact input data;
- exact algorithm and version;
- constraints and thresholds;
- random seed, where randomness is used;
- number of attempts and accepted samples;
- expected result and observed result;
- a reproducible command;
- tests or an independent calculation;
- known limitations.

For comparisons, use matched controls: the same admissible input space, constraints, candidate configurations, and computational budget. If an unrestricted random baseline is also useful, report it separately rather than presenting it as the only control.

## 9. Safety and authority boundary

This repository is a research and decision-support scaffold. AI agents may inspect, calculate, propose, and prepare changes. They must not silently commit consequential changes, publish external actions, or treat their own generated conclusions as verified evidence.

The intended authority model is:

- **AI:** navigator and proposer.
- **Shadow:** exposes missing evidence and unresolved consequences.
- **Gate:** checks admissibility against explicit rules.
- **Human:** reviews consequential decisions and authorizes commits.
- **Memory:** records what was decided and why.

## 10. Current status

**Status: research scaffold / specification in progress.**

No computational advantage, physical interpretation, or laboratory effect is claimed by this README. Those claims require separate derivations and reproducible experiments.

The next document, `00_MASTER_BOOT.md`, will define how an AI agent should enter the project, inspect the repository, reproduce existing results, and proceed without changing the project's definitions silently.
