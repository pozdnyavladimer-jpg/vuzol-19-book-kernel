# SCENE_SEED_TEMPLATE.md
# Vuzol-19 — Scene Seed Template

> Use this to propose a new scene before writing it.  
> A scene seed is not a draft.  
> It is a possible pressure route.

---

## 1. Seed identity

```yaml
SCENE_SEED:
  id: ""
  title: ""
  author: ""
  date: ""
  status:
    - RAW
    - READY_FOR_FLOWER_SCAN
    - HOLD
    - APPROVED_FOR_DRAFT
```

---

## 2. One-line scene

```text
Write the scene in one sentence.
```

Example:

```text
A young pilot tries to lift the Buga Sphere, but the pyramid field reveals he is acting from shame, not readiness.
```

---

## 3. Why this scene matters

```yaml
SCENE_IMPORTANCE:
  plot_reason: ""
  character_reason: ""
  world_reason: ""
  reader_reason: ""
```

---

## 4. Characters

```yaml
CHARACTERS:
  main: ""
  secondary: []
  absent_but_present_as_memory: []
```

---

## 5. System or world mechanism involved

```yaml
SYSTEMS:
  - "Flower Runtime"
  - "Human Gate"
  - "Buga Sphere"
  - "Pyramid Field"
  - "Human Crown"
  - "Shadow Box"
  - "Glasses Return Assistant"
  - "Isekai Capsule"
  - "AI Guard"
  - "Earth–Moon Processor"
  - "Nazca Surface Protocol"
  - "Other: "
```

---

## 6. Pressure

```yaml
PRESSURE:
  source: ""
  visible_pressure: ""
  hidden_pressure: ""
  body_signal: ""
```

---

## 7. Shadow candidate

```yaml
SHADOW_CANDIDATE:
  name: ""
  route: ""
  false_solution: ""
  danger: ""
```

Examples:

```text
prove_self
false_green
repair_too_fast
savior_control
pattern_hunger
escape_disguised_as_clarity
forced_forgiveness
```

---

## 8. Human Gate risk

```yaml
HUMAN_GATE_RISK:
  who_may_be_overridden: ""
  what_choice_may_be_stolen: ""
  how_to_protect_gate: ""
```

---

## 9. Possible Bindu Verdict

```yaml
POSSIBLE_BINDU_VERDICT:
  best_guess:
    - COMMIT
    - HOLD
    - BLOCK
    - SILENCE
    - TOLERATE
    - REPLACE
    - OCTAVE_SHIFT
  why: ""
```

---

## 10. Scene promise

What should this scene prove?

```yaml
SCENE_PROMISE:
  not: ""
  but: ""
```

Example:

```yaml
SCENE_PROMISE:
  not: "The pilot becomes powerful."
  but: "The pilot learns not to move the sphere through shame."
```

---

## 11. Possible final image

```text
Describe one visual or emotional image that could end the scene.
```

Example:

```text
The sphere rises only one centimeter, but for the first time it does not tremble.
```

---

## 12. Memory update candidate

```yaml
MEMORY_UPDATE_CANDIDATE:
  old_pattern: ""
  new_pattern: ""
  future_warning: ""
```

---

## 13. Ready check

```yaml
READY_CHECK:
  pressure_defined: false
  shadow_defined: false
  human_gate_defined: false
  possible_verdict_defined: false
  memory_update_defined: false
```

If any field is false:

```text
BINDU_VERDICT = HOLD
```
