# 01_intent_scan_hold.md
# Example — Intent Scan: HOLD

> This example shows how one personal/project intent passes through Flower Decision Panel.  
> Correct result: **HOLD**, not because the intent is bad, but because the pressure is mixed with exhaustion and shame.

---

## INPUT

```yaml
INPUT:
  intent: "I want to quit my project and start a new one."
  context: "I feel exhausted, ashamed that progress is slow, and angry that nobody understands the scale."
  desired_action: "delete old direction and announce a new one"
  urgency: "high"
  who_is_affected:
    - "me"
    - "current project memory"
    - "people who may follow the project"
```

---

## FACT / MODEL / FICTION / HOLD

```yaml
FACT:
  - "The person feels exhaustion and pressure."
  - "The decision affects project continuity."

MODEL:
  - "Vuzol-19 reads this as pressure seeking a new route."
  - "The Flower must test whether this is true direction or escape."

FICTION:
  - "In the novel, this could appear as a pilot trying to abandon one capsule path for another."

HOLD:
  - "Not enough clarity to know whether quitting is clean action or reset-loop."
```

---

## FLOWER DECISION PANEL

```yaml
FLOWER_DECISION_PANEL:
  pressure: "burnout + shame + desire for clean reset"
  shadow: "escape disguised as clarity"

  human_gate_risk:
    - "decision may be made from exhaustion"
    - "old memory may be deleted before it teaches anything"
    - "new path may become another fantasy capsule"

  flower_scan:
    red_pressure: "high exhaustion and shame"
    orange_flow: "impulse to quit"
    yellow_structure: "new project not yet structured"
    blue_law: "do not make irreversible decision from pressure spike"
    green_stability: "low"
    violet_memory: "pattern of abandoning when shame rises"

  nobel_modes:
    silence: "do not announce decision yet"
    suppress: "suppress dramatic delete/reset impulse"
    tolerate: "tolerate unfinished state without attacking self"
    void: "create empty space before new direction"
    attractor: "old reset loop detected"
    folding: "new idea has not folded into working structure"
    replace: "replace workflow first, not whole project"

  bindu_verdict: "HOLD"
  smallest_real_action: "write one paragraph: what exactly hurts in the current project?"
  memory_update_if_done: "pressure named before escape"
```

---

## WHY HOLD IS CORRECT

```text
The intent may contain real future.
But the current route is contaminated by shame and exhaustion.
The Flower does not kill the project.
It pauses the reset-loop.
```

---

## SAFE NEXT STEP

```yaml
SAFE_NEXT_STEP:
  duration: "10 minutes"
  action: "Write 5 lines:"
  lines:
    - "What hurts?"
    - "What is still alive?"
    - "What should be removed?"
    - "What should be protected?"
    - "What is the smallest test before quitting?"
```

---

## FINAL LINE

> **Do not quit from shadow.  
> Test one node first.**
