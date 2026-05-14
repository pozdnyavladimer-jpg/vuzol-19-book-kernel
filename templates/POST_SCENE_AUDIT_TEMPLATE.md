# POST_SCENE_AUDIT_TEMPLATE.md
# Vuzol-19 — Post Scene Audit Template

> Use this after writing a scene.  
> The scene is not complete until it passes audit and updates memory.

---

## 1. Scene result

```yaml
SCENE_RESULT:
  scene_id: ""
  title: ""
  status:
    - KEEP
    - REWRITE
    - HOLD
    - BLOCK
    - SPLIT_SCENE
  reason: ""
```

---

## 2. What happened

```yaml
VISIBLE_EVENT:
  summary: ""

HIDDEN_RUNTIME_EVENT:
  summary: ""

WHAT_CHANGED:
  - ""
```

Questions:

```text
What changed in the plot?
What changed in the character?
What changed in the system?
What changed in memory?
```

---

## 3. Flower audit

```yaml
FLOWER_AUDIT:
  red_pressure:
    present: false
    note: ""

  orange_flow:
    present: false
    note: ""

  yellow_structure:
    present: false
    note: ""

  blue_law:
    present: false
    note: ""

  green_stability:
    present: false
    note: ""

  violet_memory:
    present: false
    note: ""

  bindu_verdict:
    present: false
    note: ""
```

---

## 4. Human Gate audit

```yaml
HUMAN_GATE_AUDIT:
  gate_present: false
  whose_gate: []
  gate_respected: false
  gate_stolen_by:
    - "AI"
    - "Flower"
    - "system"
    - "leader"
    - "pyramid"
    - "capsule"
    - "other character"
    - "none"
  note: ""
```

Pass condition:

```text
A person affected by the action had room for yes / no / HOLD.
```

---

## 5. Shadow audit

```yaml
SHADOW_AUDIT:
  active_shadow: ""
  named_in_scene: false
  acted_from_shadow: false
  blocked_by_guard: false
  transformed: false
  note: ""
```

Common failure:

```text
The scene removed shadow too quickly instead of routing it.
```

---

## 6. False-green audit

```yaml
FALSE_GREEN_AUDIT:
  detected: false
  reason: ""
  beautiful_but_false_line: ""
  correction_needed: ""
```

False-green signs:

```text
pain resolved too early
forced forgiveness
public harmony hides private disagreement
AI says repair complete
scene looks emotionally clean but Human Gate is missing
```

---

## 7. Nobel modes audit

```yaml
NOBEL_MODES_AUDIT:
  silence:
    used: false
    healthy_or_harmful: ""
    note: ""

  suppress:
    used: false
    healthy_or_harmful: ""
    note: ""

  tolerate:
    used: false
    healthy_or_harmful: ""
    note: ""

  void:
    used: false
    healthy_or_harmful: ""
    note: ""

  attractor:
    detected: false
    obeyed: false
    note: ""

  folding:
    success: false
    note: ""

  replace:
    used: false
    note: ""
```

---

## 8. Octave shift audit

```yaml
OCTAVE_SHIFT:
  occurred: false
  subject: ""
  old_pattern: ""
  pressure: ""
  guard_event: ""
  new_action: ""
  new_memory: ""
  octave_status:
    - "none"
    - "small shift"
    - "unstable shift"
    - "stable shift"
```

---

## 9. Memory Ledger update

```yaml
MEMORY_LEDGER_UPDATE:
  id: ""
  type:
    - "character"
    - "relationship"
    - "system"
    - "world"
    - "reader"
    - "AI"
  old_pattern: ""
  blocked_action: ""
  new_action: ""
  new_rule: ""
  future_warning: ""
```

---

## 10. Rewrite instructions

```yaml
REWRITE_IF:
  - "Human Gate was missing"
  - "scene resolved pain too early"
  - "AI became final authority"
  - "model was presented as fact"
  - "shadow was romanticized"
  - "no memory changed"
  - "HOLD was skipped when needed"

REWRITE_TARGET:
  keep: []
  remove: []
  add: []
```

---

## 11. Final verdict

```yaml
FINAL_VERDICT:
  allowed:
    - KEEP
    - REWRITE
    - HOLD
    - BLOCK
    - SPLIT_SCENE
  chosen: ""
  reason: ""
```

---

## 12. Short AI prompt

```text
Audit the scene using POST_SCENE_AUDIT.

Check:
Flower,
Human Gate,
Shadow,
False-green,
Nobel modes,
Octave shift,
Memory Ledger.

Do not mark KEEP unless Human Gate is protected and memory changed.
If uncertain, choose HOLD.
```
