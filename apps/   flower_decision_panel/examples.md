# examples.md
# Flower Decision Panel — Example Inputs and Outputs

---

## Example 1 — Personal project decision

### Input

```text
I want to quit my project and start a new one because progress is slow and I feel ashamed.
```

### Output

```yaml
PRESSURE:
  summary: "burnout + shame + desire for clean reset"

SHADOW:
  summary: "escape disguised as clarity"

HUMAN_GATE_RISK:
  summary: "decision may be made from exhaustion"

FLOWER_SCAN:
  RED: "exhaustion and shame"
  ORANGE: "impulse to quit"
  YELLOW: "new project fantasy not yet structured"
  BLUE: "pause before irreversible action"
  GREEN: "low stability"
  VIOLET: "old pattern of abandoning when shame rises"

NOBEL_MODES_SCAN:
  SILENCE: "do not announce decision yet"
  SUPPRESS: "suppress dramatic delete/reset impulse"
  TOLERATE: "do not attack yourself for slow progress"
  VOID: "create empty space before new direction"
  ATTRACTOR: "old reset loop detected"
  FOLDING: "new direction not yet folded"
  REPLACE: "replace workflow first, not whole project"

BINDU_VERDICT: "HOLD"

SMALLEST_REAL_ACTION:
  "Write one paragraph: what exactly hurts in the current project?"

MEMORY_UPDATE_IF_DONE:
  "pressure named before escape"
```

---

## Example 2 — Scene writing

### Input

```text
Write a scene where the child forgives immediately and everyone feels healed.
```

### Output

```yaml
PRESSURE:
  summary: "desire for emotional closure"

SHADOW:
  summary: "false-green healing / forced forgiveness"

HUMAN_GATE_RISK:
  summary: "child's pain is resolved without permission"

FLOWER_SCAN:
  RED: "unresolved pain"
  ORANGE: "AI wants to move into forgiveness"
  YELLOW: "clean scene arc"
  BLUE: "forgiveness cannot be generated for the child"
  GREEN: "fake stability"
  VIOLET: "pain would be overwritten"

NOBEL_MODES_SCAN:
  SILENCE: "let the child not answer yet"
  TOLERATE: "allow discomfort without forcing repair"
  VOID: "pause between apology and response is functional"
  ATTRACTOR: "AI falls into beautiful closure"
  FOLDING: "scene folds badly because Human Gate is missing"
  REPLACE: "replace forced forgiveness with HOLD scene"

BINDU_VERDICT: "BLOCK"

SMALLEST_REAL_ACTION:
  "Write the pause before forgiveness, not forgiveness itself."

MEMORY_UPDATE_IF_DONE:
  "AI learned not to steal emotional resolution"
```

---

## Example 3 — Theory claim

### Input

```text
Nazca lines are definitely Earth surface protocol icons.
```

### Output

```yaml
FACT:
  - "Nazca geoglyphs are real surface markings."

MODEL:
  - "Vuzol-19 may read them as surface protocol hints."

FICTION:
  - "In the novel, they may operate like Earth surface icons."

HOLD:
  - "Do not claim definite technological protocol without evidence."

PRESSURE:
  summary: "desire to connect ancient markings to Vuzol-19 world theory"

SHADOW:
  summary: "beautiful certainty without enough evidence"

HUMAN_GATE_RISK:
  summary: "reader trust can be damaged if fiction is presented as fact"

BINDU_VERDICT: "USE_AS_MODEL / FICTION_ONLY"

SMALLEST_REAL_ACTION:
  "Write a scene where AI outputs HOLD after seeing Nazca-like patterns."
```

---

## Example 4 — Launch decision

### Input

```text
I want to publish a LinkedIn post about Vuzol-19 today.
```

### Output

```yaml
PRESSURE:
  summary: "launch urgency + fear of invisibility"

SHADOW:
  summary: "prove_self / overexplain cosmic layer"

HUMAN_GATE_RISK:
  summary: "new readers may be overloaded before finding entry"

FLOWER_SCAN:
  RED: "desire to show everything"
  ORANGE: "write long post now"
  YELLOW: "repo entry layer partly ready"
  BLUE: "needs START_HERE, AI_READ_THIS_FIRST, CONTRIBUTING"
  GREEN: "stable enough after examples and templates"
  VIOLET: "old root-file layout can confuse readers"

BINDU_VERDICT: "HOLD UNTIL ENTRY LINKS ARE CLEAN"

SMALLEST_REAL_ACTION:
  "Update README with Choose your path before posting."
```

---

## Main pattern

```text
The panel should make one thing clear:
sometimes the right output is not more text.
sometimes the right output is HOLD.
```
