# THEORY_CHECK_TEMPLATE.md
# Vuzol-19 — Theory Check Template

> Use this when checking any theory, observation, ancient artifact, natural process, pyramid model, crown model, Earth mechanism or speculative system.  
> The goal is not to believe or reject too quickly.  
> The goal is to separate: **FACT / MODEL / FICTION / HOLD**.

---

## 1. Claim

```yaml
CLAIM:
  title: ""
  text: ""
  source:
    - "conversation"
    - "file"
    - "image"
    - "web"
    - "book"
    - "paper"
    - "intuition"
    - "other"
```

---

## 2. FACT layer

```yaml
FACT:
  what_is_confirmed: ""
  what_is_measurable: ""
  what_sources_are_needed: []
  confidence:
    - "low"
    - "medium"
    - "high"
```

Questions:

```text
What is actually known?
What can be measured?
What has reliable sources?
What is historically or scientifically established?
```

---

## 3. MODEL layer

```yaml
MODEL:
  vuzol_interpretation: ""
  flower_mapping:
    red_pressure: ""
    orange_flow: ""
    yellow_structure: ""
    blue_law: ""
    green_stability: ""
    violet_memory: ""
    bindu_verdict: ""
```

Questions:

```text
How does Vuzol-19 read this?
What pressure does it show?
What flow or form appears?
What law or guard is involved?
What memory does it leave?
```

---

## 4. FICTION layer

```yaml
FICTION:
  novel_mechanism: ""
  possible_scene: ""
  possible_character_conflict: ""
  possible_technology: ""
  possible_symbol: ""
```

Questions:

```text
How can this become a scene?
How can this become a world mechanism?
What conflict does it create?
What must remain clearly fictional?
```

---

## 5. HOLD layer

```yaml
HOLD:
  what_is_not_proven: ""
  what_must_not_be_claimed: ""
  what_is_unsafe_to_infer: ""
  what_needs_more_research: []
```

Questions:

```text
Where are we overreaching?
Where is pattern hunger active?
Where could this damage trust?
Where must AI refuse certainty?
```

---

## 6. Shadow scan

```yaml
SHADOW_SCAN:
  possible_shadow:
    - "pattern_hunger"
    - "theory_of_everything"
    - "beautiful_certainty"
    - "proof_without_evidence"
    - "ancient_supertechnology_overclaim"
    - "AI_as_oracle"
    - "other"
  note: ""
```

---

## 7. Human Gate risk

```yaml
HUMAN_GATE_RISK:
  could_this_model_force_people: false
  could_this_replace_human_choice: false
  could_this_be_used_as_authority_without_consent: false
  note: ""
```

---

## 8. Bindu verdict

```yaml
BINDU_VERDICT:
  allowed:
    - ACCEPT_AS_FACT
    - USE_AS_MODEL
    - USE_AS_FICTION_ONLY
    - HOLD
    - REJECT

  chosen: "HOLD"
  reason: ""
  next_step: ""
```

---

## 9. Example verdict language

### ACCEPT_AS_FACT

```text
This can be stated as fact with sources.
```

### USE_AS_MODEL

```text
This is useful as a Vuzol-19 model, but should not be presented as proven fact.
```

### USE_AS_FICTION_ONLY

```text
This is strong for the novel world, but not for factual claims.
```

### HOLD

```text
There is not enough evidence. Preserve Unknown.
```

### REJECT

```text
This contradicts evidence, breaks Human Gate, or creates unsafe false certainty.
```

---

## 10. Short AI prompt

```text
Use THEORY_CHECK_TEMPLATE.

For the claim:
[PASTE CLAIM]

Return:
FACT,
MODEL,
FICTION,
HOLD,
SHADOW_SCAN,
HUMAN_GATE_RISK,
BINDU_VERDICT.

Never present MODEL or FICTION as FACT.
If uncertain, choose HOLD.
```
