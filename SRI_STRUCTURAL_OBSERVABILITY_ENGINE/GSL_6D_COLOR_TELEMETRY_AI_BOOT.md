# GSL 6D COLOR TELEMETRY — AI REPOSITORY BOOT
Version: 0.1  
Status: Research / integration brief  
Purpose: Continue the GSL 6D telemetry idea in this repository without losing the existing CASR, GF(2), 9V, Sri-Cube, and V-Kernel boundaries.

---

## 0. Mission for the AI agent

You are entering an existing research repository. Your task is **not** to redesign the architecture from scratch.

First inspect the current repository and identify the files that were recently corrected, especially the mathematical/model documents commonly referred to as files **02, 04, and 05**. Confirm their actual paths and names before editing anything.

The immediate continuation is to connect the existing CASR experiment with the **GSL 6D numeric color telemetry**, then develop a diagnostic layer that explains *which measured dimension is problematic and why*.

Work incrementally. Do not rewrite canonical files wholesale. Preserve the user's terminology, record assumptions, and make small reviewable changes.

## 1. Core architecture

The six axes are:

| Axis | Color | Meaning | Example measurable inputs |
|---|---|---|---|
| R | Red | Pressure / risk / instability | resource pressure, shear, optical loss, phase drift |
| O | Orange | Active flow / transitions | accepted transitions, switching activity, path changes |
| Y | Yellow | Structure / observability | GF(2) rank, measurement-matrix rank, dependency visibility |
| G | Green | Balance / quality / progress | objective gap, forward/rollback balance, residual error |
| B | Blue | Hard law / admissibility | encoded hard-constraint pass/fail |
| V | Violet | Future transition potential | remaining feasible alternatives, open transition capacity |

These are **telemetry dimensions**, not literal physical colors and not universal laws. Each domain adapter must define its own raw metrics, units, scales, and evidence.

The core flow:

```text
physical or computational system
        ↓
raw measurements / solver state
        ↓
domain adapter
        ↓
GSL 6D raw vector [R,O,Y,G,B,V]
        ↓
diagnosis + Shadow evidence
        ↓
Gate: ALLOW / HOLD / REPAIR / BLOCK
        ↓
human-approved Bindu / commit
        ↓
MemoryAtom / run record
```

Principle: **AI may propose transitions; evidence must justify them; Gate decides admissibility; human approval controls consequential commits.**

## 2. Current known implementation — preserve these facts

The earlier CASR integration produced:

- `flower_gate_120_project_experiment.py`
- `gsl_6d_casr_telemetry_report.md`
- `gsl_6d_casr_telemetry_update.zip`

The integrated experiment was run with fixed seed `20261112`. The recorded example had:

- MILP optimum: `3426.73`
- CASR final objective: `3421.08`
- CASR accepted objective path: `[3276.67, 3386.85, 3410.35, 3415.99, 3418.46, 3421.08]`

Example telemetry at step 0:

```text
R=0.600 O=0.000 Y=0.286 G=0.113 B=1.000 V=0.876
```

At step 5:

```text
R=0.030 O=1.000 Y=0.250 G=0.942 B=1.000 V=0.080
```

Important implementation semantics:

- `B=1` means only that the hard constraints actually encoded in this CASR experiment passed. It is not proof that every real-world constraint is satisfied.
- `Y` in this CASR adapter is the satisfied prerequisite/dependency-edge fraction. It is **not** GF(2) rank in this adapter.
- `O` is currently an accepted-transition event indicator (0/1), not a calibrated transition rate.
- `R`, `G`, and `V` are declared engineering mappings / heuristics. Their scales and thresholds need validation.
- `FLOW = R + O + G` and `FORM = Y + B + V` are raw sums and may exceed 1. They are not probabilities.
- `simplex` is a normalized relative composition of the six axes. It must not replace or erase the raw vector.
- The telemetry-enabled run is a demonstration, not evidence of general superiority over MILP or other solvers.

Do not silently change these definitions. If you improve them, document the old and new semantics and add tests.

## 3. Corrected mathematical facts to preserve

For the specific B candidate:

```text
U9 = (14,10,12)
U6 = (11,7,13)
U3 = (7,11,5)

S = (U9[0] xor U6[0] xor U3[0],
     U9[1] xor U6[1] xor U3[1],
     U9[2] xor U6[2] xor U3[2])

S = (2,6,4)
```

Its syndrome rank is **2**, not 3, because:

```text
2 xor 6 xor 4 = 0
```

The syndrome vectors are linearly dependent over GF(2).

Do not confuse this with candidate A, whose previously calculated syndrome was `(2,2,0)`.

The 18D Sri-Cube / GF(2) calculations and CASR portfolio telemetry are different domain adapters. Do not mix their metrics or claim that the CASR `Y` value is the Sri-Cube syndrome rank.

Any claimed exhaustive search must match the actual implementation. Do not describe a constrained search as exhaustive over the full `20^18` space unless the code truly enumerates that space.

## 4. Color Diagnosis — next development target

Add a diagnostic layer after the 6D encoder. It should not merely say “red is high”. It should return:

- axis and color;
- measured raw metric(s);
- normalized axis value;
- threshold and threshold source;
- severity / status;
- evidence or source field;
- possible cause stated as a hypothesis, not a fact;
- recommended next measurement or safe action.

Example diagnostic record:

```json
{
  "axis": "R",
  "color": "RED",
  "status": "WARNING",
  "value": 0.60,
  "threshold": 0.50,
  "metric": "resource_pressure",
  "evidence": "resource_usage / resource_capacity",
  "interpretation": "resource pressure exceeds the configured warning threshold",
  "next_action": "inspect the resource with the largest utilization"
}
```

The example is illustrative. Do not adopt `0.50` as a universal threshold. Thresholds must be domain-specific and configurable.

### Diagnostic rules

1. Diagnose each axis independently before producing a combined verdict.
2. A high value is not always bad:
   - high R usually indicates pressure;
   - high O can mean productive activity or unstable switching;
   - high Y usually means stronger observability in the chosen metric;
   - high G usually means better balance/progress;
   - B is a hard pass/fail flag for explicitly encoded constraints;
   - high V can mean useful remaining options, but also unresolved work.
3. Define directionality per metric. Never assume all six axes share “higher is better”.
4. A green score must never override a failed blue hard constraint.
5. Do not infer causes from a color alone. Use Shadow evidence to retain the raw measurement and uncertainty.
6. If evidence is missing, return `UNKNOWN` or `HOLD`, not a fabricated diagnosis.
7. Separate:
   - measurement;
   - interpretation;
   - recommendation;
   - Gate decision.

## 5. Photonic / wave-computing research adapter — proposed, not implemented

Explore a separate adapter for a simulated or measured photonic system, initially a single Mach–Zehnder interferometer.

Possible physical measurements:

| GSL axis | Candidate photonic telemetry |
|---|---|
| R | insertion loss, phase drift, thermal drift, instability |
| O | switching events, reconfiguration activity, active paths |
| Y | observability / rank of the measurement model, distinguishability of modes |
| G | output error, target fidelity, energy or balance metric |
| B | configured physical tolerances and operating constraints pass/fail |
| V | available alternative configurations / feasible phase settings |

A basic interferometer model can use:

```text
E_out = E1 + E2 * exp(i * phi)
I_out ∝ |E_out|^2
```

The model must distinguish optical field from detector output:

- complex field contains amplitude and phase;
- a standard intensity photodetector measures intensity and does not automatically reveal phase;
- phase recovery may require a coherent reference or another phase-sensitive measurement arrangement.

Start with a simulation. Add controlled perturbations one at a time:

1. phase offset;
2. insertion loss;
3. thermal phase drift;
4. sensor noise;
5. partial loss of observability.

Check whether the adapter identifies the injected fault from evidence. Do not claim this demonstrates a real photonic chip until validated on hardware.

Keep this adapter separate from CASR and Sri-Cube adapters. Reuse the 6D interface, not domain-specific formulas.

## 6. Required repository workflow

Before editing:

1. List the repository tree and identify the actual files 02, 04, and 05 that the user corrected.
2. Inspect the first revised ZIP/module and the current `flower_gate_120_project_experiment.py` if present.
3. Check whether the updated telemetry code is already integrated. Avoid duplicating it.
4. Read the current README and boot instructions.
5. Produce a short audit report: existing / missing / conflicting / proposed.

Then implement in small steps:

### Step A — stabilize CASR telemetry

- Confirm the experiment runs from a clean environment.
- Preserve deterministic seed and print run metadata.
- Add unit tests for normalization, axis ranges, and hard-constraint semantics.
- Ensure raw metrics and normalized values are both saved.
- Do not modify the solver's decision logic just to improve the colors.

### Step B — add Color Diagnosis

- Add configurable domain-specific thresholds.
- Add tests for each axis, missing data, and conflicting signals.
- Add Shadow evidence records.
- Make Gate decisions explicit and explainable.
- Ensure failed hard constraints cause HOLD/BLOCK according to the documented policy.

### Step C — export machine-readable state packets

Prefer JSONL: one packet per iteration. Each packet should include:

```json
{
  "schema_version": "1.0",
  "domain": "casr",
  "run_id": "stable-run-id",
  "step": 0,
  "raw_metrics": {},
  "gsl6d": {
    "raw": {"R": 0.0, "O": 0.0, "Y": 0.0, "G": 0.0, "B": 0.0, "V": 0.0},
    "simplex": {}
  },
  "diagnosis": [],
  "shadow": {"unresolved": [], "evidence": []},
  "gate": {"verdict": "HOLD", "reasons": []},
  "provenance": {
    "seed": null,
    "code_version": null,
    "measurements": []
  }
}
```

Do not invent `run_id`, code hash, sensor values, or evidence. Populate them from actual run metadata or leave them null/unknown.

### Step D — photonic proof-of-concept

- Create a separate simulation module and tests.
- Begin with one interferometer, not a full chip.
- Inject known faults and measure diagnostic accuracy.
- Compare the diagnosis with a simple baseline threshold detector.
- Report false positives, false negatives, and unknown cases.
- Only after this should the photonic adapter be connected to a hardware interface.

## 7. Minimum acceptance tests

The work is not complete until:

- existing CASR experiment still runs;
- existing objective path and solver behavior are unchanged unless explicitly approved;
- all six raw axes are finite and within their documented ranges;
- simplex values are finite, nonnegative, and sum to 1 within tolerance;
- raw values are preserved independently of simplex values;
- B reflects only explicitly tested hard constraints;
- a failed hard constraint cannot be hidden by a high G value;
- a low Y can be reported even when B=1;
- missing measurements produce UNKNOWN/HOLD;
- each diagnosis points to evidence;
- JSONL export can be parsed back;
- photonic simulation tests correctly identify the injected phase/loss faults within declared tolerances.

## 8. Research discipline and safety

Label every statement as one of:

- **FACT** — established mathematical/physical result or directly verified code behavior;
- **MEASURED** — output from a named run, dataset, or sensor;
- **HYPOTHESIS** — proposed interpretation needing a test;
- **DESIGN CHOICE** — a selected convention, scale, threshold, or policy.

Do not:

- describe the Flower/Sri geometry as established particle physics;
- equate six telemetry axes with six physical wave modes;
- claim the photonic system is conscious or understands its own state;
- claim a color vector proves a fault without supporting measurements;
- claim universal predictive ability;
- replace human approval for consequential actions.

## 9. First response expected from the AI agent

Do not start by writing code.

Return:

1. repository tree relevant to this work;
2. exact identification of corrected files 02, 04, and 05;
3. whether the first revised ZIP/module is present and already integrated;
4. current status of CASR 6D telemetry;
5. missing tests and missing documentation;
6. a minimal ordered implementation plan;
7. any contradictions between the current code and this boot document.

Wait for user approval before broad refactoring or changing canonical formulas.

---

## Guiding principle

**Color is a compressed state indicator, not an explanation by itself.  
Shadow preserves the evidence. Gate checks admissibility. Bindu commits only what has been verified.**
