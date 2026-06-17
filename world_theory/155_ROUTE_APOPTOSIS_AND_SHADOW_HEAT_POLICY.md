# 155 — Route Apoptosis and ShadowHeat Policy

**Ukrainian name:** Апоптоз маршруту, ShadowHeat і Human Gate policy для V-KERNEL / GitCube OS  
**Status:** GitCube OS bridge / Flower Gate Core policy / AI guarded autonomy  
**Mode:** TEXT_ONLY / no image generation  
**Version:** v1.0

---

## 0. Purpose

This file defines how a living route, petal, document-edge, workflow, AI action path or system transition is degraded, quarantined, repaired or retired.

The key rule:

```text
AI may detect damage.
AI may quarantine a dangerous route.
AI may propose repair.
AI may not permanently rewrite topology without Human Gate.
```

This is the cybernetic analogue of biological apoptosis, but applied to system routes.

---

## 1. Core Distinction

```yaml
TOPOLOGY:
  meaning: "which routes can exist"
  change_requires: "Human Gate / explicit structural review"

METRIC:
  meaning: "current route weight, cost, friction, risk, trust and wear"
  change_can_be: "automatic, measured, reversible"

ROUTE_APOPTOSIS:
  meaning: "planned retirement or blocking of a degraded route"
  permanent_change_requires: "Human Gate"
```

Canon:

```text
AI may change route weight.
AI may not erase the map.
```

---

## 2. ShadowHeat

ShadowHeat is accumulated route damage.

It is not only physical heat.
It is a generalized cost signal.

```yaml
SHADOW_HEAT_SOURCES:
  physical:
    - "friction"
    - "thermal overload"
    - "corrosion"
    - "fatigue"
    - "gradient loss"

  biological:
    - "ATP overcost"
    - "membrane drift"
    - "protein misfolding"
    - "senescence signal"
    - "inflammation"

  software:
    - "false-green test"
    - "hidden edge"
    - "bug debt"
    - "unsafe automation route"
    - "unverified dependency"

  business:
    - "dead contract"
    - "operator overload"
    - "missing document-edge"
    - "unowned decision"
    - "shadow debt"
```

Vuzol phrase:

```text
ShadowHeat = ціна проходу,
який система більше не може чесно утримувати.
```

---

## 3. Route Lifecycle

```text
CANDIDATE
→ ALLOW_SMALL
→ ACTIVE
→ WATCH
→ DEGRADED
→ QUARANTINE
→ REPAIR
→ RETIRE_PROPOSAL
→ HUMAN_GATE
→ RETIRE / RESTORE / REPLACE
```

YAML:

```yaml
ROUTE_LIFECYCLE:
  CANDIDATE:
    meaning: "possible route, not yet trusted"

  ALLOW_SMALL:
    meaning: "small commit allowed"

  ACTIVE:
    meaning: "route is currently used"

  WATCH:
    meaning: "metrics show early drift"

  DEGRADED:
    meaning: "ShadowHeat increasing"

  QUARANTINE:
    meaning: "route disabled for normal flow, still preserved for audit"

  REPAIR:
    meaning: "route may be corrected"

  RETIRE_PROPOSAL:
    meaning: "AI proposes planned route death"

  HUMAN_GATE:
    meaning: "human decides irreversible topology change"

  RETIRE:
    meaning: "route removed or archived"

  RESTORE:
    meaning: "route returns with lower weight or new guard"

  REPLACE:
    meaning: "new route opens after repair design"
```

---

## 4. AI Permissions

```yaml
AI_CAN:
  - "detect ShadowHeat"
  - "mark route as DEGRADED"
  - "reduce route weight"
  - "quarantine route"
  - "emergency block if safety threshold is crossed"
  - "write ShadowAtom"
  - "write MemoryAtom"
  - "propose repair"
  - "propose retirement"
  - "explain affected edges"
  - "request Human Gate"
```

```yaml
AI_CANNOT:
  - "permanently delete a core route"
  - "rewrite octave mask"
  - "bypass Human Gate"
  - "execute irreversible apply"
  - "commit structural mutation without review"
  - "hide ShadowHeat"
  - "convert quarantine into permanent deletion by itself"
```

Canon:

```text
AI is macrophage, not nucleus.
AI audits damage.
Human Gate owns organism-level commit.
```

---

## 5. Macrophage Analogy

In this model AI behaves like a system macrophage.

```yaml
AI_AS_MACROPHAGE:
  scan:
    meaning: "detects damage-associated patterns"
    vuzol: "ShadowHeat / ShadowAtom / false-green"

  local_response:
    meaning: "quarantine / emergency block / inflammation"
    vuzol: "HOLD / BLOCK"

  cleanup:
    meaning: "marks debris and proposes repair"
    vuzol: "REPAIR / MemoryAtom / ShadowAtom"

  limitation:
    meaning: "does not rewrite DNA or remove organs"
    vuzol: "Human Gate required"
```

---

## 6. Apoptosis Levels

```yaml
APOPTOSIS_LEVELS:
  LEVEL_0_SIGNAL:
    verdict: "WATCH"
    meaning: "route shows small drift"
    ai_action: "log MemoryAtom / increase monitoring"

  LEVEL_1_DECAY:
    verdict: "DEGRADED"
    meaning: "route works but cost rises"
    ai_action: "reduce weight / recommend repair"

  LEVEL_2_QUARANTINE:
    verdict: "HOLD"
    meaning: "normal use is unsafe"
    ai_action: "quarantine route / keep audit trail"

  LEVEL_3_EMERGENCY_BLOCK:
    verdict: "BLOCK"
    meaning: "continuation creates immediate high-risk damage"
    ai_action: "temporary safety block / notify Human Gate"

  LEVEL_4_RETIRE_PROPOSAL:
    verdict: "HUMAN_REVIEW_REQUIRED"
    meaning: "route may need planned death"
    ai_action: "prepare retirement packet"

  LEVEL_5_TOPOLOGY_CHANGE:
    verdict: "HUMAN_GATE_ONLY"
    meaning: "remove or replace route in base mask"
    ai_action: "cannot execute alone"
```

---

## 7. ShadowAtom Packet

```yaml
SHADOW_ATOM_PACKET:
  route_id: "required"
  source_layer: "physical | biological | software | business | AI_runtime"
  shadow_heat_score: "0.0-1.0"
  repeated_failures: "count"
  last_safe_commit: "timestamp or reference"
  affected_edges:
    - "edge id / document / workflow"
  risk_type:
    - "thermal"
    - "corrosion"
    - "fatigue"
    - "false_green"
    - "operator_overload"
    - "privacy"
    - "security"
    - "legal"
  recommended_action:
    - "WATCH"
    - "REPAIR"
    - "QUARANTINE"
    - "EMERGENCY_BLOCK"
    - "RETIRE_PROPOSAL"
  human_gate_required: true
```

---

## 8. Repair Packet

```yaml
ROUTE_REPAIR_PACKET:
  route_id: "required"
  current_status: "DEGRADED | QUARANTINE | BLOCK"
  cause:
    - "metric drift"
    - "hidden edge"
    - "missing operator"
    - "missing document"
    - "energy overcost"
    - "environment mismatch"
  repair_options:
    - "add missing edge"
    - "reduce route weight"
    - "add cooldown"
    - "add sensor"
    - "split route"
    - "merge route"
    - "retire route"
  rollback_plan: "required"
  test_plan: "required"
  human_gate: "required before irreversible apply"
```

---

## 9. Examples Across Octaves

### 9.1 Corrosion

```yaml
CORROSION_ROUTE:
  material: "Fe"
  shadow: "redox drift / oxygen-water Gate uncontrolled"
  memory: "rust as accumulated ShadowAtom"
  apoptosis: "remove route, coat, isolate, replace, repair boundary"
```

### 9.2 Biological aging

```yaml
CELL_AGING_ROUTE:
  route: "membrane / protein Gate"
  shadow: "high maintenance cost, damaged proteins, noisy signaling"
  apoptosis: "senescence / programmed cell death if organism-level Gate allows"
```

### 9.3 Business contract

```yaml
BUSINESS_ROUTE:
  route: "contract → operator → document-edge → delivery"
  shadow: "contract exists but operation is dead"
  apoptosis: "quarantine old route, audit, renegotiate or close"
```

### 9.4 AI automation

```yaml
AI_AUTOMATION_ROUTE:
  route: "proposal → tool → apply"
  shadow: "false-green / missing permission / irreversible risk"
  apoptosis: "AI blocks apply, writes report, requests Human Gate"
```

---

## 10. Runtime Formula

```text
route_health = coherence - shadow_heat - unresolved_edges - irreversible_risk
```

```text
if route_health > allow_threshold:
    verdict = ALLOW
elif route_health > repair_threshold:
    verdict = REPAIR
elif immediate_risk:
    verdict = EMERGENCY_BLOCK
else:
    verdict = HOLD_OR_QUARANTINE
```

But:

```text
permanent topology change requires Human Gate
```

---

## 11. Final Canon

```text
A living system must be able to close routes.
But route death must be gated.

AI may protect the field.
AI may not own the organism.

Quarantine is automatic safety.
Retirement is Human Gate.
```

Ukrainian:

```text
Жива система має вміти закривати маршрути.
Але смерть маршруту має проходити Gate.

AI може захищати поле.
AI не володіє організмом.

Карантин — це автоматична безпека.
Остаточне видалення — це Human Gate.
```
