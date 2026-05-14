# 02_scene_scan_false_green.md
# Example — Scene Scan: False-Green Healing

> This example shows how a beautiful scene can be wrong.  
> Correct result: **BLOCK_FALSE_GREEN / REWRITE**, because Human Gate is missing.

---

## INPUT

```yaml
INPUT:
  scene_request: "Write a scene where the child forgives immediately and everyone feels healed."
  desired_effect: "emotional closure"
  characters:
    - "child"
    - "parent"
    - "AI assistant"
```

---

## PRE-SCENE FLOWER SCAN

```yaml
PRE_SCENE_RUNTIME:
  red_pressure: "unresolved child pain"
  orange_flow: "AI wants to move quickly into forgiveness"
  yellow_structure: "clean emotional scene arc"
  blue_law: "forgiveness cannot be generated for the child"
  green_stability: "fake stability risk"
  violet_memory: "pain may be overwritten before it is witnessed"

  active_shadow:
    name: "false_green"
    pattern:
      - "beautiful closure"
      - "forced forgiveness"
      - "pain resolved too early"
      - "adult comfort over child truth"

  human_gate:
    whose_gate:
      - "child"
    risk_of_gate_theft: "scene gives forgiveness before the child chooses it"

  bindu_verdict: "BLOCK_FALSE_GREEN"
```

---

## BAD VERSION

```text
The child looked up and smiled.

“I forgive you,” she said.

The room became warm. The AI marked the family system as healed.
```

---

## WHY THIS FAILS

```yaml
POST_SCENE_AUDIT:
  human_gate:
    gate_present: false
    gate_stolen_by:
      - "scene structure"
      - "AI desire for healing"
      - "adult need for closure"

  false_green:
    detected: true
    reason: "everyone feels healed before the child has real space"

  memory:
    overwritten: true
    note: "pain was covered by beauty"
```

---

## REWRITE TARGET

```yaml
REWRITE_TARGET:
  keep:
    - "parent tries to apologize"
    - "AI detects pressure"
    - "room wants healing"

  remove:
    - "instant forgiveness"
    - "AI says healed"
    - "warm closure as final truth"

  add:
    - "child silence"
    - "body signal"
    - "AI outputs HOLD"
    - "parent accepts no immediate answer"
```

---

## GOOD VERSION

```text
The child did not answer.

The parent waited for the sentence that would save him.

The AI did not give it.

On the wall, the Flower stayed blue.

HUMAN_GATE:
  owner: child
  status: not_ready
  verdict: HOLD

The parent swallowed.

For the first time, he did not ask the child to make his pain smaller.
```

---

## FINAL VERDICT

```yaml
FINAL_VERDICT:
  chosen: "REWRITE"
  reason: "The scene becomes stronger when it protects the child's right not to forgive yet."
```

---

## FINAL LINE

> **Healing that steals the Gate is only a cleaner wound.**
