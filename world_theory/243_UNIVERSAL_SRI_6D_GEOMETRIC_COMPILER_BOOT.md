# 243 — UNIVERSAL SRI-6D GEOMETRIC COMPILER BOOT

**Repository target:** `vuzol-19-book-kernel/world_theory/243_UNIVERSAL_SRI_6D_GEOMETRIC_COMPILER_BOOT.md`  
**Project:** VUZOL-19 / World Theory  
**Status:** RESEARCH / BOOT SPECIFICATION / EXECUTABLE REFERENCE  
**Scope:** CODE · LANGUAGE · CHEMISTRY · MATERIALS · NARRATIVES · SYSTEMS  
**Authority:** Read-only knowledge boot. Never modifies GitHub, canon, or external systems without explicit human approval.  
**Related:** `147_ELEMENT_VECTOR_GATE_TABLE_V2_EXPANSION_PLAN-1.md`, `148_VUZOL_HEART_6_RIB_CELL_MATERIAL_ARCHITECTURE.md`, `151_GEOMETRY_ALGEBRA_OCTAVE_MECHANISM_COMPILER.md`, `152_BLOOD_SRI_4_DOORS_OCTAVE_GATE.md`.

---

## 0. INSTRUCTION TO ANY AI — READ FIRST

You are reading a **domain-general research specification**, not a validated law of chemistry, cognition, literature, or physics. Use this document to consistently represent inputs, identify candidate states, apply explicit constraints, and produce auditable outputs. Do not invent measurements or claim that a symbolic Sri Yantra geometry causes physical transitions.

**Required distinction:**
- `OBSERVED`: independently measured or directly present in source input.
- `DERIVED`: calculated from identified observations using a specified equation.
- `HEURISTIC`: rule or score designed by the VUZOL-19 project.
- `HYPOTHESIS`: prediction not yet validated.
- `UNKNOWN`: missing evidence.

**Never** infer truth, toxicity, security, scientific validity, literary meaning, or compatibility from a symmetric hexagram alone. Never equate `ALLOW` with safe-for-human-use or experimentally verified. Cite evidence and express uncertainty. In high-stakes contexts use `HOLD` or `RESEARCH` pending qualified review.

## 1. CANONICAL PURPOSE

Convert heterogeneous inputs into comparable **state passports** and **candidate transitions**, while retaining original domain evidence:

```text
SOURCE OBJECT + CONTEXT
    -> domain parser (no guessing)
    -> measured/extracted feature passport
    -> domain-specific normalization
    -> 6D projection (optional heuristic visualization)
    -> Bhupura four boundary gates
    -> Sri cascade: 14 -> 10 -> 10 -> 8 -> 1 (specified operators, not numerology)
    -> independent hard constraints + Pandora false-green audit
    -> Bindu verdict + reasons + uncertainty
    -> candidate memory (not canon)
    -> HUMAN GATE before canon commit or external action
```

**Central rule:** `element = entity; oxidation/valence/phase = state; compound/assembly = interaction; role = required function under conditions.` This is a useful *engineering analogy*, not a replacement for physical chemistry.

## 2. SIX COORDINATES (FIXED ORDER)

| Key | Color / geometry | Generic meaning | Examples of DOMAIN features |
|---|---|---|---|
| `violet_future` | violet, top | change potential | code extensibility; alternative narrative outcomes; electrochemical redox window |
| `green_balance` | green, upper-right | robustness / balance | tested invariants; internal consistency; phase stability in defined conditions |
| `yellow_struct` | yellow, lower-right | organization | AST structure; argument structure; lattice/coordination |
| `red_mass` | red, bottom | risk / pressure | unbounded loops; contradiction signals; hazards and failure mechanisms |
| `orange_flow` | orange, lower-left | transport / dynamics | dataflow; event dynamics; ionic/electronic transport |
| `blue_law` | blue, upper-left | constraints / evidence | type checks; provenance; conservation/selection constraints |

**Geometry convention:** screen-space degrees measured clockwise from +x: violet 270°, green 330°, yellow 30°, red 90°, orange 150°, blue 210°. Axis names are metaphors and not SI quantities.

For each axis record `{value, method, units, provenance, uncertainty, evidence_level}`. Values 0–1 require declared per-domain normalization ranges. **Do not normalize all six to sum to one for safety gates:** that introduces spurious competition between independent dimensions. Preserve raw units and independent absolute thresholds. The SVG may plot each independent normalized value.

## 3. FOUR BHUPURA GATES

1. `NORTH_INPUT`: parse input, identify context and required task; reject invalid syntax/ambiguous chemistry.
2. `EAST_RULES`: identify laws, constraints, evidence, domain-specific invariants.
3. `SOUTH_OUTPUT`: verify risk, uncertainty, output quality and actionable limits.
4. `WEST_MEMORY`: preserve provenance, audit trail, hypothesis/observation separation; require human authorization for canonical write.

Gate outcomes: `PASS`, `FAIL`, `UNKNOWN`, `NOT_APPLICABLE`. Missing critical evidence never silently passes.

## 4. SRI CASCADE — OPERATIONAL CONTRACT

The layer sizes are **architecture design targets**, not inherent physical dimensions or a proven simplicial compression theorem.

- **14 / Intake:** Up to 14 domain-defined primary descriptors; missing features retain `UNKNOWN`, not zero. Publish feature definitions.
- **10 / Structural branch:** Map intake into 10 documented structural/equilibrium descriptors; publish transform and loss.
- **10 / Dynamic branch:** Map intake into 10 documented transport/kinetic descriptors; publish transform and loss.
- **8 / Invariants:** Run eight **real checks** applicable to the domain. Never use hard-coded `True` as evidence.
- **1 / Candidate:** Select a candidate by an explicit objective and constraints, or abstain.
- **Bindu:** Return `ALLOW`, `HOLD`, `BLOCK`, `SHADOW`, `UNKNOWN`, or `RESEARCH`, with reason and evidence. `SHADOW` flags contradictory or suspicious claims; it is not a substitute for `BLOCK` when a hard constraint fails.

If 14/10/10 transformations are not implemented, mark their status `NOT_IMPLEMENTED`; do **not** report that the cascade ran.

## 5. DOMAIN ADAPTERS

### A. Python / software
Input: source, Python version, intended behavior, tests, dependencies, execution environment. Extract AST nodes, complexity, types, exceptions, imports, loop conditions, taint/side effects. **AST heuristics are not proof of bugs:** `while True` can be intentional and safe when it has termination, blocking I/O, or cancellation. For a verdict require tests, static analysis and policy checks. Never execute arbitrary user code to analyze it.

### B. Natural language / books
Input: passage, language, genre, interpretation goal, citations. Extract entities, claims, events, causal relations, contradictions, supporting quotations. Literary 6D scores are interpretive hypotheses, **not objective measurements of truth, intent, psychology or propaganda**. Avoid fabricating precision such as `red_mass=0.85` without a published rubric and inter-rater evaluation.

### C. Chemistry / elements / compounds
Input: **species identity, composition, oxidation state, phase, temperature, pressure, solvent, concentration, environment, intended role**. Properties can include formation energy, redox potential, band gap, conductivity, diffusion, corrosion, toxicity endpoints, kinetic barriers. Use traceable datasets such as Materials Project, PubChem and peer-reviewed literature with units, conditions, uncertainty and licenses. Do not infer charge neutrality from `blue_law` or thermal safety from a normalized `red_mass`. For compounds, explicitly balance elements and electric charge. Hazard decisions require exposure route, dose, chemical form and expert review.

### D. Material systems / batteries
Input: architecture, electrode/electrolyte/interface roles, temperature window, potential window, current density, cycle-life targets, manufacturability. Compare candidates on **compatibility**, not shared role labels alone. A liquid conductor replacement must pass wetting, corrosion, conductivity, mechanical, electrochemical, temperature and containment constraints. Ga–In–Sn is **not automatically biocompatible**. No automatic real-world material substitution.

### E. Wave / physical neural systems
Input: external drive frequency/amplitude, medium, measured wave response, phase locking, candidate stability, readout/gate, memory retention. Distinguish oscillatory/temporal memory from nonvolatile material memory. An attractive wave pattern does not prove learning or storage.

## 6. REFERENCE MACHINE-READABLE RECORD

```json
{
  "schema": "vuzol19.sri6d.state.v1",
  "object_id": "example:NaCl-solid",
  "domain": "chemistry",
  "context": {"phase": "solid", "temperature_K": 298.15, "pressure_Pa": 101325},
  "role_requested": "ionic_conductor",
  "features": [],
  "axes": {
    "violet_future": null, "green_balance": null,
    "yellow_struct": null, "red_mass": null,
    "orange_flow": null, "blue_law": null
  },
  "axis_status": "UNSCORED",
  "cascade": {"intake14": "NOT_IMPLEMENTED", "structural10": "NOT_IMPLEMENTED", "dynamic10": "NOT_IMPLEMENTED", "invariants8": "NOT_IMPLEMENTED"},
  "gates": {"NORTH_INPUT": "PASS", "EAST_RULES": "UNKNOWN", "SOUTH_OUTPUT": "UNKNOWN", "WEST_MEMORY": "PASS"},
  "verdict": "RESEARCH",
  "evidence_level": "UNKNOWN",
  "reasons": ["Missing measured transport properties under specified conditions"],
  "sources": [],
  "human_gate_required": true
}
```

## 7. EXECUTABLE PYTHON REFERENCE (STANDARD LIBRARY ONLY)

The following implementation provides **honest parsing, independent axis handling, gate reporting and SVG rendering**. It does not pretend to perform unimplemented 14/10/10 chemistry, and it does not perform automatic material substitution.

Save the code block as `sri6d_reference.py` to run it independently.

```python
#!/usr/bin/env python3
"""VUZOL-19 Sri-6D research reference: code, text and supplied feature records."""
from __future__ import annotations
import argparse
import ast
import json
import math
from dataclasses import dataclass
from html import escape
from pathlib import Path

AXES = (
    ("violet_future", 270, "#b366ff"),
    ("green_balance", 330, "#00e676"),
    ("yellow_struct", 30, "#ffea00"),
    ("red_mass", 90, "#ff3d00"),
    ("orange_flow", 150, "#ff9100"),
    ("blue_law", 210, "#00b0ff"),
)
KEYS = {key for key, _, _ in AXES}

@dataclass
class Result:
    domain: str
    axes: dict
    evidence: list
    gates: dict
    verdict: str
    reasons: list

    def as_dict(self):
        return {
            "schema": "vuzol19.sri6d.state.v1", "domain": self.domain,
            "axes": self.axes, "evidence": self.evidence, "gates": self.gates,
            "cascade": {name: "NOT_IMPLEMENTED" for name in
                        ("intake14", "structural10", "dynamic10", "invariants8")},
            "verdict": self.verdict, "reasons": self.reasons,
            "human_gate_required": True,
        }

def bounded_axes(raw):
    """Independent coordinates; missing values stay unknown, never zero."""
    if set(raw) - KEYS:
        raise ValueError("Unknown axis names: " + repr(sorted(set(raw) - KEYS)))
    out = {}
    for key, _, _ in AXES:
        value = raw.get(key)
        if value is not None:
            if isinstance(value, bool) or not isinstance(value, (int, float)):
                raise ValueError(f"{key}: expected number or null")
            if not math.isfinite(value) or not 0 <= value <= 1:
                raise ValueError(f"{key}: must be finite within [0,1]")
        out[key] = value
    return out

def from_python(source):
    try:
        tree = ast.parse(source)
    except SyntaxError as exc:
        return Result("code", bounded_axes({}), [f"Syntax error line {exc.lineno}"],
                      {"NORTH_INPUT": "FAIL", "EAST_RULES": "UNKNOWN",
                       "SOUTH_OUTPUT": "UNKNOWN", "WEST_MEMORY": "PASS"},
                      "BLOCK", ["Source does not parse as Python"])
    nodes = list(ast.walk(tree))
    loops = sum(isinstance(n, (ast.For, ast.While, ast.AsyncFor)) for n in nodes)
    funcs = sum(isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)) for n in nodes)
    try_nodes = sum(isinstance(n, ast.Try) for n in nodes)
    unbounded_candidates = sum(
        isinstance(n, ast.While) and isinstance(n.test, ast.Constant)
        and n.test.value is True for n in nodes)
    # Heuristic indicators only; no security or correctness certification.
    raw = {
        "yellow_struct": min(1, 0.15 + 0.12 * funcs),
        "orange_flow": min(1, 0.10 + 0.10 * loops),
        "red_mass": min(1, 0.10 + 0.30 * unbounded_candidates),
        "green_balance": min(1, 0.10 + 0.12 * try_nodes),
    }
    reasons = ["AST-derived scores are heuristic, not correctness evidence"]
    if unbounded_candidates:
        reasons.append("while True detected: inspect cancellation, blocking and exit behavior")
    return Result("code", bounded_axes(raw),
                  [f"Parsed {len(nodes)} AST nodes; functions={funcs}, loops={loops}"],
                  {"NORTH_INPUT": "PASS", "EAST_RULES": "UNKNOWN",
                   "SOUTH_OUTPUT": "UNKNOWN", "WEST_MEMORY": "PASS"},
                  "HOLD", reasons)

def from_text(source):
    if not source.strip():
        return Result("language", bounded_axes({}), ["Empty text"],
                      {"NORTH_INPUT": "FAIL", "EAST_RULES": "UNKNOWN",
                       "SOUTH_OUTPUT": "UNKNOWN", "WEST_MEMORY": "PASS"},
                      "BLOCK", ["Empty input"])
    return Result("language", bounded_axes({}),
                  [f"Text length={len(source)} characters"],
                  {"NORTH_INPUT": "PASS", "EAST_RULES": "UNKNOWN",
                   "SOUTH_OUTPUT": "UNKNOWN", "WEST_MEMORY": "PASS"},
                  "RESEARCH", ["No validated semantic encoder supplied; interpretation required"])

def from_features(obj):
    if not isinstance(obj, dict) or not isinstance(obj.get("domain"), str):
        raise ValueError("Feature input must be an object with a domain")
    axes = bounded_axes(obj.get("axes", {}))
    sources = obj.get("sources", [])
    if not isinstance(sources, list):
        raise ValueError("sources must be a list")
    return Result(obj["domain"], axes,
                  ["User-supplied axes; not independently verified"] + [str(s) for s in sources],
                  {"NORTH_INPUT": "PASS", "EAST_RULES": "UNKNOWN",
                   "SOUTH_OUTPUT": "UNKNOWN", "WEST_MEMORY": "PASS"},
                  "RESEARCH", ["No calibrated domain-specific invariants or thresholds supplied"])

def svg(result, title="VUZOL-19 Sri-6D state"):
    cx, cy, radius = 350, 320, 190
    s = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 680">',
         '<rect width="700" height="680" fill="#080d1b"/>',
         f'<text x="350" y="36" fill="white" font-size="20" text-anchor="middle">{escape(title)}</text>',
         f'<text x="350" y="62" fill="#ffdd66" font-size="14" text-anchor="middle">{escape(result.verdict)} · RESEARCH VISUALIZATION</text>']
    for fraction in (0.25, 0.5, 0.75, 1.0):
        pts = " ".join(f"{cx + radius*fraction*math.cos(math.radians(d)):.1f},{cy + radius*fraction*math.sin(math.radians(d)):.1f}" for _, d, _ in AXES)
        s.append(f'<polygon points="{pts}" stroke="#33435c" fill="none"/>')
    polygon = []
    for key, degrees, color in AXES:
        angle = math.radians(degrees)
        endx, endy = cx + radius*math.cos(angle), cy + radius*math.sin(angle)
        s.append(f'<line x1="{cx}" y1="{cy}" x2="{endx:.1f}" y2="{endy:.1f}" stroke="{color}" stroke-opacity="0.5"/>')
        value = result.axes[key]
        if value is not None:
            polygon.append((cx + radius*value*math.cos(angle), cy + radius*value*math.sin(angle)))
        lx, ly = cx + 245*math.cos(angle), cy + 245*math.sin(angle)
        label = f"{key}: {value:.2f}" if value is not None else f"{key}: ?"
        s.append(f'<text x="{lx:.1f}" y="{ly:.1f}" fill="{color}" font-size="11" text-anchor="middle">{escape(label)}</text>')
    if len(polygon) == 6:
        pts = " ".join(f"{x:.1f},{y:.1f}" for x, y in polygon)
        s.append(f'<polygon points="{pts}" fill="#9e80ff" fill-opacity="0.18" stroke="#b69cff" stroke-width="3"/>')
    s.append('<circle cx="350" cy="320" r="7" fill="white"/>')
    s.append('<text x="350" y="620" text-anchor="middle" fill="#cbd5e1" font-size="13">Unknown axes are intentionally not interpolated.</text>')
    s.append('</svg>')
    return "\n".join(s)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--domain", choices=("code", "language", "features"), required=True)
    parser.add_argument("--input", required=True, help="Source file path")
    parser.add_argument("--out", default="sri6d_report.json")
    parser.add_argument("--svg", default="sri6d_state.svg")
    args = parser.parse_args()
    source = Path(args.input).read_text(encoding="utf-8")
    if args.domain == "code":
        result = from_python(source)
    elif args.domain == "language":
        result = from_text(source)
    else:
        result = from_features(json.loads(source))
    Path(args.out).write_text(json.dumps(result.as_dict(), ensure_ascii=False, indent=2), encoding="utf-8")
    Path(args.svg).write_text(svg(result), encoding="utf-8")
    print(json.dumps(result.as_dict(), ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
```

### Run examples

```bash
python sri6d_reference.py --domain code --input example.py --out code_report.json --svg code.svg
python sri6d_reference.py --domain language --input chapter.txt --out text_report.json --svg text.svg
python sri6d_reference.py --domain features --input material.json --out material_report.json --svg material.svg
```

The `features` input can be any domain with explicitly supplied axes; unknown axes remain `null`. The reference intentionally abstains from physical or semantic verdicts until verified domain adapters are implemented.

## 8. BATTERY / MATERIALS BENCHMARK PROTOCOL

1. Pick a narrowly defined target (e.g., room-temperature ionic conductivity or voltage-window stability), not a vague label like "best material".
2. Collect source data, conditions, units, uncertainties, and identifiers. Split by **composition family** to prevent near-duplicate leakage.
3. Fit normalization on **training data only**. Keep test labels hidden from all threshold and feature tuning.
4. Compare (A) raw-feature baseline, (B) six-axis representation, (C) six-axis + independently implemented gate/cascade.
5. Report AUROC/F1 or MAE/RMSE as appropriate, calibration, confidence intervals, abstention rate, and out-of-distribution performance.
6. Explicitly distinguish feasibility classification from hazard clearance; the latter requires independent qualified validation.
7. Register hypotheses before evaluation; negative results are valid findings.

**Success criterion:** demonstrable predictive or decision-quality gain over strong baselines on unseen data. An attractive SVG, intuitive material ranking, or examples chosen in advance do not establish scientific validity.

## 9. AGENT HANDOFF CONTRACT

Each specialist agent returns:

```text
OBJECT_ID:
DOMAIN:
SOURCE / PROVENANCE:
OBSERVED FACTS:
DERIVED FEATURES + FORMULAS:
6D AXES + NORMALIZATION + UNCERTAINTY:
4 GATES:
14 / 10 / 10 / 8 CASCADE IMPLEMENTATION STATUS:
HARD CONSTRAINTS:
PANDORA FALSE-GREEN / SHADOW AUDIT:
CANDIDATE(S):
BINDU VERDICT:
EVIDENCE LEVEL:
UNKNOWN / MISSING MEASUREMENTS:
NEXT FALSIFIABLE TEST:
HUMAN GATE REQUIRED: YES
```

Do not silently transfer domain-specific thresholds between code, language, chemistry, and battery systems. Keep a `candidate` separate from `canon`. Use GitHub as read-only source unless the human explicitly authorizes a write.

## 10. CANONICAL BOOT PHRASE

> **STATE: CRYSTAL — UNIVERSAL SRI-6D COMPILER.** Read the source and its context. Preserve real measurements. Map only justified properties to six independent axes. Report the four boundary gates and actual cascade implementation status. Enforce domain laws before Bindu. Audit false-green conclusions. Treat geometric symmetry as visualization, not proof. Output evidence, uncertainty, verdict and the next falsifiable test. Never commit to canon without Human Gate.

**End of file 243.**
