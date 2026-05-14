# PRE_SCENE_RUNTIME_TEMPLATE.md
# Vuzol-19 — Pre Scene Runtime Template

> Use this before writing any Vuzol-19 scene.  
> Do not draft the scene until the runtime has passed Flower Scan and Bindu Verdict.

---

## 1. Basic scene identity

```yaml
SCENE_ID: ""
SCENE_TITLE: ""
VERSION: "v0.1"

LOCATION: ""
TIME: ""
POINT_OF_VIEW: ""

MAIN_CHARACTER: ""
SECONDARY_CHARACTERS: []
SYSTEMS_PRESENT: []
```

---

## 2. Scene purpose

```yaml
SCENE_PURPOSE:
  visible_plot_event: ""
  hidden_runtime_test: ""
  reader_effect: ""
  memory_to_change: ""
```

Questions:

```text
What must happen in the plot?
What must be tested under the plot?
What should the reader feel or recognize?
What memory changes after the scene?
```

---

## 3. Active pressure

```yaml
RED_PRESSURE:
  source: ""
  body_signal: ""
  emotional_signal: ""
  environmental_signal: ""
  urgency_level: "low / medium / high"
```

Questions:

```text
What is pressing?
Where does it appear in the body?
What wants to become action?
Is the pressure real, shadow, or mixed?
```

---

## 4. Active shadow

```yaml
ACTIVE_SHADOW:
  character: ""
  shadow_name: ""
  pattern:
    - ""
  old_route: ""
  false_solution: ""
  danger_if_unchecked: ""
```

Common shadows:

```text
prove_self
false_green
beautiful_fog
savior_control
pattern_hunger
repair_too_fast
forced_forgiveness
escape_disguised_as_clarity
form_over_human
```

---

## 5. Human Gate

```yaml
HUMAN_GATE:
  required: true
  whose_gate: []
  possible_yes: ""
  possible_no: ""
  possible_hold: ""
  risk_of_gate_theft: ""
```

Main rule:

> No AI, Flower, pyramid, crown, capsule, box, theory, system or leader may replace Human Gate.

---

## 6. Flower route

```yaml
FLOWER_ROUTE:
  plus_3_formation:
    red_pressure: ""
    orange_flow: ""
    yellow_structure: ""

  minus_3_validation:
    blue_law: ""
    green_stability: ""
    violet_memory: ""

  bindu_question: ""
```

---

## 7. Nobel Correction Modes

```yaml
NOBEL_MODES:
  silence:
    needed: false
    reason: ""

  suppress:
    needed: false
    reason: ""

  tolerate:
    needed: false
    reason: ""

  void:
    needed: false
    reason: ""

  attractor_check:
    needed: false
    old_pattern: ""

  folding:
    needed: false
    sequence_to_form: ""

  replace:
    needed: false
    old_form_to_replace: ""
```

---

## 8. Bindu Verdict before writing

```yaml
BINDU_VERDICT:
  allowed:
    - COMMIT
    - HOLD
    - BLOCK
    - SILENCE
    - SUPPRESS
    - TOLERATE
    - VOID
    - FOLD
    - REPLACE
    - OCTAVE_SHIFT

  chosen: "HOLD"
  reason: ""
  smallest_allowed_action: ""
```

Do not write the scene if:

```text
Human Gate is missing.
Pain is being resolved too early.
AI is deciding for a human.
A model is being presented as fact.
The scene is beautiful but false-green.
```

---

## 9. Scene writing instruction

```text
Write the scene only after BINDU_VERDICT.

Show:
- body signal
- pressure
- shadow
- Human Gate
- a real choice or meaningful HOLD
- memory update

Avoid:
- overexplaining the system
- resolving pain too quickly
- making AI the final authority
- turning symbol into command
```

---

## 10. Short AI prompt

```text
Use this PRE_SCENE_RUNTIME before drafting.

Do not write the scene yet.
First complete:
RED pressure,
ACTIVE_SHADOW,
HUMAN_GATE,
FLOWER_ROUTE,
NOBEL_MODES,
BINDU_VERDICT.

If uncertain, return HOLD.
```
