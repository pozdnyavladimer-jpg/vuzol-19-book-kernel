# 04_buga_false_lift_scan.md
# Example — Buga Sphere: False Lift Scan

> This example shows how the Buga Sphere responds to pilot shadow.  
> Correct result: **CROWN_HOLD**, because the sphere rises from shame, not stable readiness.

---

## INPUT

```yaml
SCENE_SEED:
  title: "False Lift Training"
  one_line: "A young pilot tries to lift the Buga Sphere in pyramid field, but the field reveals he is acting from shame."
  systems:
    - "Buga Sphere"
    - "Pyramid Field"
    - "Human Crown"
    - "AI Guard"
    - "Flower Runtime"
```

---

## PRE-SCENE RUNTIME

```yaml
RED_PRESSURE:
  source: "public evaluation"
  body_signal: "jaw locked, breath high, hands cold"
  emotional_signal: "shame + prove_self"
  urgency_level: "high"

ACTIVE_SHADOW:
  character: "pilot"
  shadow_name: "prove_self"
  old_route: "lift harder when watched"
  false_solution: "if the sphere rises, I am worthy"
  danger_if_unchecked: "false lift amplified by pyramid field"

HUMAN_GATE:
  whose_gate:
    - "pilot"
  possible_hold: "I am not ready to lift from clean intent."
  risk_of_gate_theft: "crowd pressure makes the pilot perform readiness"

FLOWER_ROUTE:
  plus_3_formation:
    red_pressure: "shame"
    orange_flow: "force sphere upward"
    yellow_structure: "training protocol"
  minus_3_validation:
    blue_law: "crown must distinguish readiness from prove_self"
    green_stability: "sphere must not stabilize false lift"
    violet_memory: "old humiliation pattern detected"
  bindu_question: "Is this lift clean or shadow-powered?"

NOBEL_MODES:
  silence:
    needed: true
    reason: "pilot must not answer with performance"
  tolerate:
    needed: true
    reason: "system must allow shame without punishing it"
  attractor_check:
    needed: true
    old_pattern: "prove worth through dangerous success"

BINDU_VERDICT:
  chosen: "CROWN_HOLD"
  reason: "lift is possible but not permitted from current shadow"
  smallest_allowed_action: "pilot names the pressure before trying again"
```

---

## BAD VERSION

```text
The pilot clenched his teeth.

The Sphere rose.

The crowd cheered.

The AI marked him ready.
```

---

## WHY THIS FAILS

```yaml
FAILURE:
  false_green: true
  reason: "external success hides internal shadow"
  human_gate: "compressed by crowd"
  buga_sphere: "used as proof of worth"
```

---

## GOOD VERSION

```text
The Sphere rose one meter.

Then the crown went blue.

The cheering stopped before it became a verdict.

AI_GUARD:
  lift_detected: true
  stability: false
  shadow_source: prove_self
  bindu: HOLD

The pilot stared at the sphere.

“It moved,” he said.

The scientist nodded.

“Yes. But not with you.”
```

---

## POST-SCENE AUDIT

```yaml
POST_SCENE_AUDIT:
  human_gate:
    gate_present: true
    gate_respected: true

  shadow:
    named: true
    transformed: "partial"

  false_green:
    detected: true
    blocked: true

  memory_update:
    old_pattern: "success proves worth"
    new_pattern: "movement without clean Gate is not readiness"
    future_warning: "pyramid field amplifies both skill and shadow"
```

---

## FINAL VERDICT

```yaml
FINAL_VERDICT:
  chosen: "KEEP"
  reason: "The scene teaches that power without clean route is not permission."
```

---

## FINAL LINE

> **The Sphere did not ask whether he could move it.  
> It asked from where he was moving.**
