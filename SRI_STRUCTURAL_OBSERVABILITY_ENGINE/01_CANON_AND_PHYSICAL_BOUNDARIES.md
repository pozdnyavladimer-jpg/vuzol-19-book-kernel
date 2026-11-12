# 01 — CANON AND PHYSICAL BOUNDARIES
## Terminology, software meaning, and limits on physical interpretation

**File:** `01_CANON_AND_PHYSICAL_BOUNDARIES.md`  
**Role:** Preserve the project's vocabulary and prevent category errors  
**Status:** Working canon; formal definitions belong in `02_MATHEMATICAL_MODEL.md`

---

## 1. Why this document exists

This document defines how the project's central words are to be interpreted inside the SRI Structural Observability Engine.

The terms Flower, Sri, Bindu, Shadow, Gate, +3, and −3 are used as names for geometric abstractions, data structures, operators, or software responsibilities.

They must not be treated as proof that the same structures exist literally inside atoms, nuclei, photons, brains, or other physical systems.

When a term has more than one possible meaning, the implementation must use the formal definition in the mathematical model. If that definition is missing, mark the term `OPEN` rather than inventing one.

## 2. Canonical architecture

The intended conceptual flow is:

```text
STATE
  |
  v
PRESSURE / DEVIATION
  |
  v
SHADOW
  |
  v
CANDIDATE TRANSITION
  |
  v
GATE
  |
  v
BINDU VERDICT
  |
  +----> ALLOW
  +----> HOLD
  +----> REPAIR
  +----> REWRITE
  +----> BLOCK
  |
  v
MEMORY
```

This is a decision-support architecture. It describes how the software should organize information and decisions, not a proven universal law of nature.

## 3. Canonical terms

### 3.1 Flower / Flower Grid

**Project meaning:** A structured map of states and permitted or proposed transitions. The Flower may be represented as a graph, grid, adjacency structure, or other explicitly defined state-space object.

**Required implementation meaning:**

- nodes represent states, state components, or defined positions;
- edges represent explicitly defined relations or transitions;
- allowed and forbidden transitions must be represented as data or rules;
- the graph must be inspectable and testable.

**Boundary:** A Flower of Life drawing or a 19-circle arrangement is a geometric inspiration or chosen graph topology. Its use in software does not prove that nature uses that exact graph.

### 3.2 Nineteen-node Flower

**Project meaning:** A selected 19-node arrangement used as one possible structural layout for organizing states and relations.

**Implementation requirement:** Define the node identifiers, coordinates or abstract positions, adjacency rules, and transition rules in code or a machine-readable specification.

**Boundary:** The number 19 is a design choice in this model unless a specific mathematical or empirical derivation establishes a stronger claim. Do not describe 19 nodes as a universal physical constant.

### 3.3 Sri / Sri geometry

**Project meaning:** A geometric organization or projection used to arrange roles, directions, layers, or candidate relations in the model.

**Implementation requirement:** Any Sri-derived structure used by an algorithm must be specified through exact coordinates, incidence relations, transformations, or constraints.

**Boundary:** A geometric correspondence is not automatically a physical decomposition. A mapping between Sri geometry and a physical system is a hypothesis until it is derived from an appropriate physical model and tested.

### 3.4 Sri Cube / 3D state geometry

**Project meaning:** A three-dimensional geometric representation used to organize state directions or transformations.

A proposed cube may use six oriented faces:

```text
+X, -X, +Y, -Y, +Z, -Z
```

The six directions are geometric labels. If the implementation uses the 24 proper rotations of a cube, it must define the rotation group and its action on the represented state.

**Boundary:** Do not silently mix spatial coordinates with phase, octave, time, or confidence. Those should be separate state variables unless the mathematical model explicitly defines a joint space.

### 3.5 Bindu

**Project meaning:** The decision or convergence point at which a candidate is evaluated and receives a controlled verdict.

Bindu is not simply the highest score and is not an automatic commit operation.

A Bindu decision must consider:

- required constraints;
- forward proposal results;
- reverse-audit results;
- Shadow items;
- consequence checks;
- uncertainty and evidence quality;
- the applicable human-approval policy.

Possible outputs include `ALLOW`, `HOLD`, `REPAIR`, `REWRITE`, and `BLOCK`.

**Boundary:** Bindu is a software decision abstraction. It is not a claim about a physical point, particle, or cosmic center.

### 3.6 Gate

**Project meaning:** An explicit admissibility check between a proposed transition and its acceptance.

A Gate must be implemented as inspectable rules. Examples include:

- type and schema validity;
- hard constraints;
- resource limits;
- consistency checks;
- policy and safety constraints;
- required evidence;
- human approval requirements.

A Gate must explain which checks passed and which failed.

**Boundary:** A Gate is not a guarantee of correctness beyond the checks it actually performs.

### 3.7 Shadow

**Project meaning:** The audit representation of what is unresolved, hidden, missing, uncertain, or potentially affected by a candidate transition.

A Shadow record may include:

- unresolved dependencies;
- residual differences;
- uncertainty;
- failed or unavailable checks;
- downstream consequences;
- calibration or measurement drift;
- missing evidence;
- assumptions that affect the verdict.

Shadow is not a second hidden truth. It is an explicit record of what the current model cannot safely treat as settled.

**Implementation requirement:** Each Shadow item should have an identifier, description, severity or type, evidence reference, status, and proposed next action.

### 3.8 +3 — forward proposal

**Project meaning:** A forward operation that generates or explores candidate states according to a defined relation.

The notation `+3` must not be interpreted as “add the integer three” unless a specific algorithm says so.

For a six-node cyclic example with nodes `0..5`, one possible route is:

```text
0 -> 2 -> 4 -> 0
```

This is a graph operation over the chosen node arrangement. It is not, by itself, a particle trajectory or physical motion.

### 3.9 −3 — reverse / inverse audit

**Project meaning:** A reverse, inverse, or constraint-oriented operation used to inspect a candidate against prior state, required conditions, or rollback relations.

For the same six-node cyclic example, one possible route is:

```text
1 -> 5 -> 3 -> 1
```

The precise meaning depends on the graph and operator definitions. Do not assume that every `−3` operation is a mathematical inverse of `+3`; prove that property for the specific transition system if it is claimed.

### 3.10 Color verdict

**Project meaning:** A compact visual encoding of a state or decision status.

The project's initial color vocabulary is:

| Color | Intended compressed meaning |
|---|---|
| Red | Pressure, risk, pain, anomaly, or blocked condition. |
| Orange | Movement, flow, change, or active transition. |
| Green | Accepted or admissible corridor, subject to the defined checks. |

Color is a presentation layer, not the underlying evidence.

**Implementation requirement:** Every color must map to a machine-readable verdict or state code. The same color must not mean different things in different modules without an explicit namespace.

### 3.11 MemoryAtom

**Project meaning:** A durable, structured record of a state, event, decision, or verified result.

A MemoryAtom should preserve at least:

```text
atom_id
timestamp_or_sequence
subject
event_or_claim
status
evidence_refs
decision
unresolved_items
model_version
```

A memory record must preserve uncertainty and provenance. It must not convert an unverified statement into a fact merely because it was stored.

### 3.12 ShadowAtom

**Project meaning:** A structured memory record for an unresolved issue, risk, contradiction, missing dependency, or uncertainty.

A ShadowAtom should link to the relevant candidate or MemoryAtom and record what would resolve it.

### 3.13 CASR

**Project meaning:** The project's constrained state-search approach. The exact expansion of the acronym and its formal objective must be fixed in `02_MATHEMATICAL_MODEL.md` and `03_CASR_SEARCH_ENGINE.md`.

Until then, use `CASR` as the project name for the search component; do not invent an expansion or claim a unique algorithmic definition.

### 3.14 9V Consequence Tensor

**Project meaning:** A proposed structured audit of consequences across defined dimensions or directions.

The name `9V` does not by itself specify nine physical dimensions, nine independent variables, or a tensor with a particular rank.

The mathematical model must define:

- the nine components or axes;
- their domains and units, if applicable;
- how consequences are calculated;
- how dependencies between components are represented;
- thresholds and uncertainty;
- how its output affects Gate and Bindu.

Until those definitions and tests exist, label 9V as `HYPOTHESIS` or `OPEN`, not as a verified physical object.

## 4. Canonical decision sequence

The intended sequence is:

1. **State:** capture the current modeled condition.
2. **Pressure:** identify constraints, deviations, or conditions that may require a transition.
3. **Shadow:** expose missing evidence, dependencies, uncertainty, and possible consequences.
4. **Candidate:** generate one or more possible transitions.
5. **+3:** explore forward candidates according to the defined operator.
6. **−3:** audit candidates in reverse or against constraints.
7. **Gate:** evaluate explicit admissibility rules.
8. **Bindu:** produce a verdict.
9. **Memory:** record the result, evidence, and unresolved items.

The exact computational order may be refined in the implementation, but no stage may be silently treated as completed when its required evidence is missing.

## 5. Physical boundaries: established facts versus project encoding

The project may use physical systems as inspiration or test domains. It must preserve the difference between established physics and its own encodings.

### 5.1 Proton and neutron

Established particle-physics descriptions include:

- proton valence-quark content: `uud`;
- neutron valence-quark content: `udd`;
- proton electric charge: `+e`;
- neutron electric charge: `0`;
- proton and neutron spin: `1/2`;
- neutron has a nonzero magnetic moment.

A four-part or five-part geometric encoding in this project must not be presented as the composition of a neutron or proton.

### 5.2 Isospin

Isospin is a mathematical symmetry concept used to describe the proton-neutron relationship in an approximate symmetry framework.

It is not evidence that a nucleus contains a literal digital two-state switch or that the proposed Flower graph is physically embedded in the nucleus.

### 5.3 Electron

An electron in quantum theory is described by a quantum state and its interactions. A graph route in this repository is not automatically an electron orbit or hidden path.

Any physical interpretation requires a defined Hamiltonian or other appropriate physical model, measurable predictions, and comparison with accepted experimental results.

### 5.4 Photons and optical hardware

A graph or state-transition model may be mapped onto optical components such as waveguides, splitters, phase shifters, modulators, and detectors.

However:

- a software node is not automatically an optical mode;
- a graph edge is not automatically a waveguide;
- a simulated phase relation is not a measured phase relation;
- an algorithmic observability result is not automatically experimental observability;
- a proposed photonic architecture is not a demonstrated device.

A hardware claim requires a component-level design, physical parameters, noise and loss model, calibration procedure, and experimental evidence.

## 6. Modeling rules

When implementing any canonical term:

1. provide a short definition in code documentation;
2. define its input and output types;
3. identify its invariants;
4. state what it does not claim;
5. add tests for boundary cases;
6. link results to evidence and version information.

Do not use a metaphor as a substitute for an interface or mathematical definition.

## 7. Ambiguity register

The following points must be resolved by later formal documents or experiments:

| Topic | Current status | Required clarification |
|---|---|---|
| Exact 19-node adjacency | `OPEN` until specified in code/spec | Node IDs, coordinates, edges, symmetries. |
| Formal meaning of `+3` and `−3` | `OPEN` per operator | Domain, action, inverse properties, boundary behavior. |
| CASR acronym and objective | `OPEN` | Exact expansion, objective function, constraints. |
| 9V components | `OPEN` | Nine axes, domains, equations, thresholds. |
| Color-to-verdict mapping | Initial vocabulary defined | Machine-readable codes and conflict rules. |
| Shadow severity | `OPEN` | Severity scale and aggregation rules. |
| Bindu decision policy | Concept defined | Exact precedence, evidence requirements, approval policy. |
| Physical mapping | `HYPOTHESIS` unless experimentally supported | Physical model, predictions, controls, measurements. |

## 8. Non-negotiable interpretation rules

- Geometry is not automatically physics.
- A representation is not the thing represented.
- A candidate is not an accepted state.
- A score is not a proof.
- A parity relation is not automatically observability.
- A simulation is not an experiment.
- A stored statement is not automatically verified.
- A color is not a substitute for its underlying verdict.
- A human approval requirement cannot be removed by an AI agent.

## 9. Relationship to the next documents

- `02_MATHEMATICAL_MODEL.md` must formalize the state space, operators, invariants, and equations.
- `03_CASR_SEARCH_ENGINE.md` must define how candidates are generated and ranked.
- `04_GF2_OBSERVABILITY_AND_9V.md` must define the exact binary matrices, rank calculations, and consequence-audit model.
- `05_EXPERIMENTS_AND_BASELINES.md` must define reproducible tests and matched controls.
- `06_AI_AGENT_TASK_PROTOCOL.md` must define task execution and review rules.

This document preserves vocabulary and boundaries. It does not replace those formal specifications.
