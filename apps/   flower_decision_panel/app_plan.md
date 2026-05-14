# app_plan.md
# Flower Decision Panel — App Plan v0.1

> This file describes the future web/app version of Flower Decision Panel.  
> v0.1 can remain a markdown prompt.  
> Build only after the repo has stable entry files.

---

## 1. Product goal

```text
Give any user a simple way to test one intent before action.
```

The app should answer:

```text
Does this intent deserve COMMIT, HOLD or BLOCK?
```

---

## 2. User flow

```text
1. User opens page.
2. User pastes one intent.
3. User selects mode:
   - personal decision
   - scene writing
   - theory check
   - AI safety
   - launch decision
4. User clicks Run Flower Scan.
5. App returns structured panel.
6. User copies result or saves as markdown.
```

---

## 3. UI cards

```yaml
UI_CARDS:
  input:
    title: "Intent"

  pressure:
    title: "Pressure"

  shadow:
    title: "Shadow"

  human_gate:
    title: "Human Gate Risk"

  flower:
    title: "Flower Scan"

  nobel:
    title: "Nobel Modes"

  verdict:
    title: "Bindu Verdict"

  action:
    title: "Smallest Real Action"

  memory:
    title: "Memory Update"
```

---

## 4. Data schema

```json
{
  "input": {
    "intent": "",
    "context": "",
    "mode": ""
  },
  "fact_model_fiction_hold": {
    "fact": [],
    "model": [],
    "fiction": [],
    "hold": []
  },
  "pressure": "",
  "shadow": "",
  "human_gate_risk": "",
  "flower_scan": {
    "red": "",
    "orange": "",
    "yellow": "",
    "blue": "",
    "green": "",
    "violet": ""
  },
  "nobel_modes": {
    "silence": "",
    "suppress": "",
    "tolerate": "",
    "void": "",
    "attractor": "",
    "folding": "",
    "replace": ""
  },
  "bindu_verdict": "",
  "smallest_real_action": "",
  "memory_update_if_done": ""
}
```

---

## 5. Modes

```yaml
MODES:
  personal_decision:
    focus:
      - "Human Gate"
      - "smallest real action"
      - "shadow"

  scene_writing:
    focus:
      - "false-green"
      - "character Gate"
      - "scene permission"

  theory_check:
    focus:
      - "FACT / MODEL / FICTION / HOLD"
      - "overclaim protection"

  ai_safety:
    focus:
      - "AI as Guard, not God"
      - "HOLD before generation"

  launch_decision:
    focus:
      - "public entry clarity"
      - "avoid overexplaining cosmic layer"
```

---

## 6. MVP without backend

A simple static page can work:

```text
textarea
mode dropdown
copy prompt button
manual AI paste
result markdown area
```

This avoids building too much too soon.

---

## 7. MVP with backend

Later:

```text
Frontend → API → LLM → structured JSON → UI cards
```

Required guardrails:

```text
always allow HOLD
never force COMMIT
never remove Human Gate
never claim model as fact
```

---

## 8. Future feature: FlowerBench

Save scans as examples for:

```text
COMMIT
HOLD
BLOCK
SILENCE
TOLERATE
REPLACE
OCTAVE_SHIFT
```

This can become a benchmark dataset.

---

## 9. Main sentence

> **The first version can be only a prompt.  
> The product is not the interface.  
> The product is the discipline of asking before acting.**
