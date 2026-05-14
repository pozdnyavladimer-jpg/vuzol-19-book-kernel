# 09_ROLE_RESONANCE_ROUTING.md
# Vuzol-19 — Role Resonance Routing v0.1

> **The system does not search by title.**  
> It searches by task geometry and Human Gate.

---

## 1. Boundary

```yaml
FACT:
  - "People have different skills, patterns, states and readiness."

MODEL:
  - "Vuzol-19 reads a task as 4D need geometry."

FICTION:
  - "In the novel, crowns and boxes can help identify who currently fits a task."

HOLD:
  - "Do not force assignment."
  - "Do not reduce people to roles."
  - "Human Gate is mandatory."
```

---

## 2. Core runtime

```text
4D_NEED
→ GEOMETRIC_SIGNAL
→ CROWN_RESPONSE
→ SHADOW_BOX_CONTEXT
→ AI_GUARD_FILTER
→ FLOWER_SCAN
→ HUMAN_GATE
→ 3D_ACTION
```

---

## 3. Example task

```yaml
TASK_SIGNAL:
  need: "programmer"
  problem: "false-green loop in Pyramid Grid"
  required_shape:
    yellow_structure: "high"
    blue_guard: "high"
    violet_memory: "medium"
    red_pressure_tolerance: "high"
    ego_noise: "low"
    unknown_tolerance: "high"
```

---

## 4. Candidate scan

```yaml
CANDIDATES:
  person_04:
    skill_match: "high"
    ego_noise: "high"
    verdict: "HOLD"

  person_11:
    skill_match: "medium"
    unknown_tolerance: "high"
    guard_integrity: "high"
    verdict: "MATCH_CANDIDATE"

  person_22:
    skill_match: "high"
    shadow: "prove_self"
    verdict: "FALSE_MATCH"
```

---

## 5. Law

```text
The system may detect fit.
It may not command action.
The person must be asked.
```

---

## 6. Scene use

```yaml
SCENE_SEEDS:
  wrong_expert:
    one_line: "The official expert is not chosen because his shadow collapses Unknown."

  quiet_programmer:
    one_line: "A temporary worker is chosen because she can hold the bug without proving herself."

  consent_check:
    one_line: "The system finds the right node, then waits for yes, no or HOLD."
```

---

## 7. Main sentence

> **The system does not look for the most important person.  
> It looks for the person whose current geometry can hold the task without stealing the Gate.**
