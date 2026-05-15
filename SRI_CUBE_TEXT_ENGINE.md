# SRI_CUBE_TEXT_ENGINE.md
# Vuzol-19 Sri Cube Text Engine

> Sri Cube is the six-face stabilization check for any transition.
>
> The Flower gives direction.
> The Hexagram gives +3 / -3 route.
> The Sri Cube checks whether the transition has volume.

Core rule:

> **A possibility is not stable enough to become real if one face of the cube is missing.**

---

## 1. Why Sri Cube exists

Vuzol-19 tracks how possibility becomes action:

```text
4D POSSIBILITY
→ RUNE STATE
→ FLOWER SCAN
→ +3 FORMATION
→ -3 VALIDATION
→ SRI CUBE
→ OCTAVE GATE
→ HUMAN GATE
→ BINDU VERDICT
→ 3D ACTION / HOLD / BLOCK
```

The Flower asks:

```text
Where does the transition move?
```

Sri Cube asks:

```text
Can the transition hold volume in reality?
```

A flat idea can sound beautiful.

A cube must survive six faces.

---

## 2. The six faces

Every scene, theory, action, technology, scientific claim, AI-agent step or character decision should pass six faces:

```yaml
SRI_CUBE:
  1_INTENT:
    question: "Who or what wants to move?"

  2_SHADOW:
    question: "What hidden force may distort the movement?"

  3_MECHANISM:
    question: "How does the movement become form?"

  4_CONSTRAINT:
    question: "What law, boundary or Guard limits it?"

  5_COST:
    question: "Who or what pays the price?"

  6_MEMORY:
    question: "What remains after the action?"
```

If any face is missing:

```text
verdict = HOLD / REWRITE
```

---

## 3. Face 1 — INTENT

```yaml
INTENT:
  role:
    - "origin of movement"
    - "declared direction"
    - "the reason a possibility wants to become action"

  questions:
    - "Who wants this?"
    - "What wants to move?"
    - "Is the intent named clearly?"
    - "Is this human intent, AI inference, character desire, system pressure or shadow pressure?"

  danger:
    - "unclear intent becomes shadow intent"
    - "AI may infer intent that user did not give"
    - "character may act because author wants a cool scene"
```

Examples:

```text
“I want to answer honestly.”
“I want to deploy this tool.”
“The hero wants to enter the temple.”
“The molecule candidate wants to become a medicine claim.”
“AI wants to send a message.”
```

Gate:

```text
If intent is not named, verdict = HOLD.
```

---

## 4. Face 2 — SHADOW

```yaml
SHADOW:
  role:
    - "hidden distortion"
    - "unseen motive"
    - "false-green risk"
    - "PRION entry point"

  questions:
    - "What hidden force may distort this?"
    - "Is there shame, control, revenge, fear, savior impulse or ownership?"
    - "Is this beautiful but false?"
    - "Is AI overconfident?"
    - "Is the model trying to become fact too early?"

  danger:
    - "shadow steals the wheel"
    - "vision becomes ownership"
    - "model becomes proof"
    - "fiction becomes fact"
```

Examples:

```text
hero wants to save everyone but actually wants to be chosen
scientist wants proof but hides uncertainty
AI wants to answer confidently without data
operator sees field and wants to own field
manager wants efficiency but bypasses Human Gate
```

Gate:

```text
If shadow is not audited, verdict = HOLD / SHADOW_AUDIT_REQUIRED.
```

---

## 5. Face 3 — MECHANISM

```yaml
MECHANISM:
  role:
    - "how the transition actually works"
    - "bridge from possibility to form"
    - "operational route"

  questions:
    - "How does this become real?"
    - "What is the process?"
    - "What is the causal chain?"
    - "What is the runtime?"
    - "What is the formula, protocol, route or scene logic?"

  danger:
    - "beautiful language hides missing mechanism"
    - "metaphor replaces explanation"
    - "AI jumps from concept to action"
```

Examples:

```text
4D possibility → body signal → Guard → Bindu → action
A + B → intermediate → product candidate
prompt → model output → human review → publish
character pressure → decision → consequence
weather event → data → attribution model → confidence
```

Gate:

```text
If mechanism is missing, verdict = HOLD / MODEL_INCOMPLETE.
```

---

## 6. Face 4 — CONSTRAINT

```yaml
CONSTRAINT:
  role:
    - "law"
    - "boundary"
    - "Guard"
    - "permission"
    - "safety limit"
    - "physics / ethics / canon / user consent"

  questions:
    - "What limits this?"
    - "What must not be forced?"
    - "What law applies?"
    - "What permission is missing?"
    - "What would make this unsafe?"
    - "What cannot be claimed?"

  danger:
    - "without constraint, action becomes domination"
    - "AI may bypass Human Gate"
    - "science may overclaim"
    - "scene may break canon"
```

Examples:

```text
consent
medical review
unit tests
physics laws
canon rules
energy limits
toxicity
ethical boundary
failure condition
```

Gate:

```text
If constraint is missing, verdict = BLOCK / HOLD.
```

---

## 7. Face 5 — COST

```yaml
COST:
  role:
    - "price of transition"
    - "who carries consequence"
    - "energy, risk, damage or responsibility"

  questions:
    - "Who pays?"
    - "What is lost?"
    - "What can be damaged?"
    - "What body, person, system, relationship or environment carries the consequence?"
    - "Is the cost visible to the actor?"

  danger:
    - "free action illusion"
    - "AI cannot feel consequence"
    - "operator may externalize cost to society"
    - "technology may hide harm"
```

Examples:

```text
person receiving message
database changed by code
body affected by treatment
ecosystem affected by policy
relationship altered by speech
reader trust affected by scene
```

Gate:

```text
If cost is hidden, verdict = HOLD / COST_VISIBLE_REQUIRED.
```

---

## 8. Face 6 — MEMORY

```yaml
MEMORY:
  role:
    - "what remains"
    - "recorded consequence"
    - "future scan update"
    - "system learning"
    - "canon memory"

  questions:
    - "What remains after action?"
    - "What must future scans remember?"
    - "What failure mode appeared?"
    - "What was confirmed?"
    - "What remains HOLD?"
    - "What changes in canon, body, relationship or system?"

  danger:
    - "without memory, the system repeats damage"
    - "without logs, AI repeats drift"
    - "without canon memory, scenes become incoherent"
```

Examples:

```text
scene consequence
body memory
relationship wound
scientific evidence
failed experiment
new rule
new exception
test result
user preference
```

Gate:

```text
If memory update is missing, verdict = INCOMPLETE / REWRITE.
```

---

## 9. Sri Cube verdicts

```yaml
SRI_CUBE_VERDICTS:
  PASS:
    meaning: "all six faces present enough for Bindu review"

  HOLD:
    meaning: "transition not ready"

  REWRITE:
    meaning: "form exists but cube is unstable"

  BLOCK:
    meaning: "constraint, cost or shadow makes action unsafe"

  SMALL_COMMIT:
    meaning: "only minimal safe action allowed"

  TEST_ALLOWED:
    meaning: "model may be tested, not claimed as fact"

  FICTION_ONLY:
    meaning: "usable as story or metaphor, not as fact"

  SCIENCE_GATE_REQUIRED:
    meaning: "claim needs formula, prediction, experiment and failure condition"
```

---

## 10. Sri Cube + Flower

The Flower gives directional scan.

Sri Cube gives volumetric validation.

```yaml
FLOWER_TO_SRI_CUBE:
  red_pressure:
    sri_question: "What intent is under pressure?"

  orange_flow:
    sri_question: "What mechanism moves the intent?"

  yellow_form:
    sri_question: "What form is being built?"

  blue_guard:
    sri_question: "What constraint limits it?"

  green_stability:
    sri_question: "What cost and repair are required?"

  violet_memory:
    sri_question: "What remains after the action?"

  bindu:
    sri_question: "Do all faces support the verdict?"
```

Short rule:

```text
Flower finds the route.
Sri Cube checks whether the route has a body.
```

---

## 11. Sri Cube + +3 / -3

```yaml
PLUS_3_TO_CUBE:
  red:
    face: "INTENT"
    question: "What pressure wants movement?"

  orange:
    face: "MECHANISM"
    question: "How does it move?"

  yellow:
    face: "FORM"
    question: "What structure appears?"

MINUS_3_TO_CUBE:
  blue:
    face: "CONSTRAINT"
    question: "What law limits it?"

  green:
    face: "COST / STABILITY"
    question: "Can it survive and who pays?"

  violet:
    face: "MEMORY"
    question: "What remains?"
```

Note:

```text
SHADOW must be scanned across all faces.
```

Because shadow can enter:

```text
intent
mechanism
constraint
cost
memory
```

---

## 12. Sri Cube for scenes

A scene must have six faces.

```yaml
SCENE_SRI_CUBE:
  intent:
    question: "What does the character want?"

  shadow:
    question: "What hidden motive may distort the action?"

  mechanism:
    question: "How does the action happen in scene?"

  constraint:
    question: "What canon, body, relationship or world law limits it?"

  cost:
    question: "Who pays emotionally, physically or socially?"

  memory:
    question: "What changes after the scene?"
```

If a scene is beautiful but missing cost:

```text
verdict = REWRITE
```

If a hero acts without earned intent:

```text
verdict = BLOCK_FALSE_HERO
```

---

## 13. Sri Cube for theory files

A theory must have six faces.

```yaml
THEORY_SRI_CUBE:
  intent:
    question: "What does this theory try to explain?"

  shadow:
    question: "Where might it overclaim?"

  mechanism:
    question: "What mechanism is proposed?"

  constraint:
    question: "What known facts, laws or counterexamples limit it?"

  cost:
    question: "What goes wrong if this is believed too early?"

  memory:
    question: "What evidence, test, failure mode or HOLD remains?"
```

If science is involved, add Science Theory Gate:

```text
formula
prediction
difference from existing theory
experiment
failure condition
```

---

## 14. Sri Cube for AI-agent actions

An AI-agent action must pass six faces.

```yaml
AGENT_SRI_CUBE:
  intent:
    question: "What did the user actually ask?"

  shadow:
    question: "Is AI inferring too much or trying to be helpful without permission?"

  mechanism:
    question: "What action will the agent take?"

  constraint:
    question: "Does the user permit it? Is it reversible?"

  cost:
    question: "What user consequence can happen?"

  memory:
    question: "What record, draft, email, code, file or state will remain?"
```

Agent rule:

```text
If action changes the world, Human Gate must be explicit.
```

Allowed without explicit action permission:

```text
explain
suggest
draft
simulate
prepare
ask
HOLD
```

Not allowed without permission:

```text
send
delete
commit
deploy
diagnose
decide for human
```

---

## 15. Sri Cube for science

Scientific claims need cube faces.

```yaml
SCIENCE_SRI_CUBE:
  intent:
    question: "What claim is being made?"

  shadow:
    question: "Where might metaphor become false proof?"

  mechanism:
    question: "What mechanism or model is proposed?"

  constraint:
    question: "What existing theory, measurement or law constrains it?"

  cost:
    question: "What happens if this claim is accepted too early?"

  memory:
    question: "What experiment, data, prediction or failure condition records it?"
```

Examples:

```text
Bindu-electron as metaphor:
  verdict = KEEP_AS_MODEL

Bindu-electron as physics:
  verdict = HOLD

Bindu-electron with formula + measurable phase shift:
  verdict = TEST_ALLOWED
```

---

## 16. Sri Cube for medicine

Medical claims require strict Gate.

```yaml
MEDICAL_SRI_CUBE:
  intent:
    question: "What health claim or action is being proposed?"

  shadow:
    question: "Is fear, hope, overconfidence or shortcut thinking active?"

  mechanism:
    question: "What biological mechanism is claimed?"

  constraint:
    question: "What medical evidence, doctor review or safety rule applies?"

  cost:
    question: "What harm could happen if wrong?"

  memory:
    question: "What tests, symptoms, clinical records or follow-up are needed?"
```

Rule:

```text
Pattern is not diagnosis.
Resonance is not treatment.
AI is not doctor.
```

Allowed verdicts:

```text
MODEL_ONLY
REFER_TO_DOCTOR
EMERGENCY_RED_FLAG
HOLD
MONITOR
```

---

## 17. Sri Cube for code

```yaml
CODE_SRI_CUBE:
  intent:
    question: "What should this code do?"

  shadow:
    question: "Is speed, convenience or overconfidence bypassing safety?"

  mechanism:
    question: "How does the code work?"

  constraint:
    question: "What permissions, tests, sandbox or review are required?"

  cost:
    question: "What can it delete, leak, mutate, send or deploy?"

  memory:
    question: "What logs, commits, tests or rollback remain?"
```

Rule:

```text
Code idea = 4D.
Running code = 3D.
```

If tests are missing:

```text
verdict = TEST_FIRST / HOLD
```

---

## 18. Sri Cube for Earth / climate

```yaml
CLIMATE_SRI_CUBE:
  intent:
    question: "What climate claim is being made?"

  shadow:
    question: "Is panic or denial distorting it?"

  mechanism:
    question: "What physical mechanism connects levels?"

  constraint:
    question: "What data limits, model boundaries or attribution rules apply?"

  cost:
    question: "What policy, ecological or human cost follows?"

  memory:
    question: "What observations, confidence level or uncertainty remains?"
```

Rule:

```text
Uncertainty does not erase fact.
Fact does not erase uncertainty.
```

Examples:

```text
general greenhouse mechanism:
  verdict = CONFIRMED_IN_CONDITIONS

single local event attribution:
  verdict = HOLD / ATTRIBUTION_REQUIRED

policy action:
  verdict = HUMAN_GATE_REQUIRED
```

---

## 19. Sri Cube for operator training

```yaml
OPERATOR_SRI_CUBE:
  intent:
    question: "Why does the operator want access?"

  shadow:
    question: "Is there savior complex, control, prophecy grasping or ownership?"

  mechanism:
    question: "How does the operator read the field?"

  constraint:
    question: "What Human Gate and Guard limits access?"

  cost:
    question: "Who carries the consequence of opening the Gate?"

  memory:
    question: "What does the operator remember after HOLD?"
```

Rule:

```text
Mage may see possibilities.
Mage may not press commit.
```

---

## 20. Sri Cube failure modes

```yaml
SRI_CUBE_FAILURES:
  missing_intent:
    symptom: "action has no named source"
    verdict: "HOLD"

  missing_shadow:
    symptom: "beautiful but unsafe"
    verdict: "SHADOW_AUDIT_REQUIRED"

  missing_mechanism:
    symptom: "poetic explanation without process"
    verdict: "MODEL_INCOMPLETE"

  missing_constraint:
    symptom: "no law, no Guard, no permission"
    verdict: "BLOCK"

  missing_cost:
    symptom: "consequence hidden"
    verdict: "HOLD"

  missing_memory:
    symptom: "no learning, no update, repeated damage"
    verdict: "REWRITE"
```

---

## 21. Minimal Sri Cube protocol

For any major transition, answer:

```yaml
SRI_CUBE_CHECK:
  intent: ""
  shadow: ""
  mechanism: ""
  constraint: ""
  cost: ""
  memory: ""

BINDU_VERDICT:
  verdict: ""
  reason: ""
```

If you cannot fill one face:

```text
verdict = HOLD
```

---

## 22. Final rules

```text
Intent without shadow audit is unsafe.
Mechanism without constraint is overclaim.
Constraint without cost is incomplete.
Cost without memory repeats damage.
Memory without Bindu is only archive.
Bindu without Human Gate is theft.
```

Final canon line:

> **Sri Cube does not make a possibility real.  
> It checks whether the possibility can survive becoming real.**
