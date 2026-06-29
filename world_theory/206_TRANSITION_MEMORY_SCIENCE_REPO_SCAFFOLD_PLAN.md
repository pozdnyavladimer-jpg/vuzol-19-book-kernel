# 206 — Transition Memory Science Repo Scaffold Plan

**Ukrainian name:** Каркас репозиторію для Transition Memory Science / Науки памʼяті переходу  
**Status:** Vuzol‑19 / GitCube OS / research-program scaffold  
**Layer:** method crystallization / reproducible Hello World polygon  
**Mode:** TEXT_ONLY / no image generation  

---

## 0. Purpose

This file defines the first clean repository scaffold for turning Vuzol‑19 from a strong symbolic-transition language into a reproducible discipline:

```text
Transition Memory Science
```

Ukrainian:

```text
Наука памʼяті переходу
```

Main idea:

```text
Not to prove everything.

To create one narrow reproducible protocol
where a transition can be:

defined,
audited,
blocked,
repaired,
verified,
repeated,
and recorded.
```

---

## 1. Why This Repo Exists

Vuzol‑19 already has:

```text
Bindu
Gate
Shadow
PRION
MemoryAtom
ShadowAtom
route memory
false-green audit
FACT / MODEL / HYPOTHESIS / HOLD / PRION / COMMIT
```

But to become a discipline, it needs:

```text
definitions
metrics
protocols
cases
failure boundaries
replication
```

This repo is the first “Hello World” polygon.

It should not start from cosmic physics, clinical psychology, or laboratory materials.

Best first polygon:

```text
Git / documents / small repo transition audit
```

Reason:

```text
Git already has:
files,
states,
diffs,
commits,
tests,
false-green,
missing edges,
route memory,
and reproducible history.
```

---

## 2. Proposed Repository Name

Recommended:

```text
transition-memory-science
```

Alternative:

```text
vuzol-transition-memory-lab
gate-transition-studies
vuzol19-transition-method
```

Best clean name:

```text
transition-memory-science
```

Reason:

```text
It sounds like a research program,
not a mystical system.
```

---

## 3. Root Repo Structure

```text
transition-memory-science/
│
├── README.md
├── LICENSE
├── CITATION.cff
├── CHANGELOG.md
├── ROADMAP.md
│
├── docs/
│   ├── 00_MANIFESTO.md
│   ├── 01_DEFINITIONS.md
│   ├── 02_METHOD_OVERVIEW.md
│   ├── 03_SAFETY_BOUNDARIES.md
│   ├── 04_FACT_MODEL_HYPOTHESIS_HOLD_PRION_COMMIT.md
│   ├── 05_TRANSITION_MEMORY_SCIENCE.md
│   └── 06_RELATION_TO_VUZOL19_WORLD_THEORY.md
│
├── protocols/
│   ├── GATE_AUDIT_PROTOCOL.md
│   ├── SHADOW_SCAN_PROTOCOL.md
│   ├── PRION_FALSE_GREEN_AUDIT.md
│   ├── MEMORY_ATOM_PROTOCOL.md
│   ├── REPLICATION_PROTOCOL.md
│   └── FAILURE_BOUNDARY_PROTOCOL.md
│
├── metrics/
│   ├── METRICS_SPEC.md
│   ├── route_trace_complete.md
│   ├── missing_edge_count.md
│   ├── shadow_pressure_score.md
│   ├── false_green_risk.md
│   ├── gate_verdict_score.md
│   └── post_verification_status.md
│
├── schemas/
│   ├── transition_case.schema.json
│   ├── gate_audit.schema.json
│   ├── memory_atom.schema.json
│   ├── shadow_atom.schema.json
│   └── prion_audit.schema.json
│
├── cases/
│   ├── README.md
│   ├── 000_TEMPLATE/
│   │   ├── input_state.md
│   │   ├── expected_route.md
│   │   ├── gate_audit.md
│   │   ├── shadow_scan.md
│   │   ├── prion_audit.md
│   │   ├── repair_plan.md
│   │   ├── post_verification.md
│   │   └── memory_atom.json
│   │
│   ├── 001_hello_world_missing_edge/
│   ├── 002_false_green_readme_config/
│   ├── 003_test_pass_route_broken/
│   └── 004_human_review_gate_required/
│
├── examples/
│   ├── simple_document_edge/
│   ├── small_git_repo/
│   └── business_process_stub/
│
├── tools/
│   ├── gate_audit_cli.py
│   ├── prion_scan.py
│   ├── memory_atom_writer.py
│   └── validate_case.py
│
├── tests/
│   ├── test_schema_validation.py
│   ├── test_hello_world_case.py
│   ├── test_false_green_detection.py
│   └── test_memory_atom_required.py
│
└── world_theory_links/
    ├── INDEX_LINKS.md
    ├── PART_4_170_195_BRIDGE.md
    ├── PART_5_196_205_BRIDGE.md
    └── FILE_147_ELEMENT_GATE_TABLE_BRIDGE.md
```

---

## 4. Minimum Viable Repo

If the full structure is too large, start with this:

```text
transition-memory-science/
│
├── README.md
├── docs/
│   ├── 01_DEFINITIONS.md
│   ├── 02_METHOD_OVERVIEW.md
│   └── 03_SAFETY_BOUNDARIES.md
│
├── protocols/
│   ├── GATE_AUDIT_PROTOCOL.md
│   ├── PRION_FALSE_GREEN_AUDIT.md
│   └── MEMORY_ATOM_PROTOCOL.md
│
├── cases/
│   ├── 000_TEMPLATE/
│   └── 001_hello_world_missing_edge/
│
└── schemas/
    └── transition_case.schema.json
```

This is enough for the first public commit.

---

## 5. README.md Skeleton

```markdown
# Transition Memory Science

Transition Memory Science is a reproducible framework for studying how a state becomes another state through route, Gate, Shadow, audit, commit, and memory.

It does not replace existing sciences.

It provides a transition-memory layer:

- What state existed before?
- What route was taken?
- Where was the Gate?
- What Shadow blocked or distorted the route?
- Was there PRION / false-green?
- What passed commit?
- What memory changed the next transition?

## Core Principle

A result without route memory is not a complete result.

## First Polygon

This repository begins with a small Git/document transition audit.

Why Git?

Because Git already has files, diffs, commits, tests, history, missing edges, false-green risk, and reproducible states.

## Status

MODEL / HYPOTHESIS / EARLY PROTOCOL

Not a finished science yet.

## Goal

Create a repeatable protocol that another operator can run without the original author and reach the same Gate verdict.
```

---

## 6. Definitions File

File:

```text
docs/01_DEFINITIONS.md
```

Must define:

```yaml
Bindu:
  short: "center of transition reading before commit"
  test_question: "Where is the decision/verdict point?"

Gate:
  short: "permission boundary before a transition is allowed to become commit"
  test_question: "What condition must be passed before the action is valid?"

Shadow:
  short: "hidden boundary, blocked route, or unexamined pressure"
  test_question: "What part of the route is missing, hidden, blocked, or unnamed?"

PRION:
  short: "broken transition that imitates truth or center and repeats false commit"
  test_question: "What conclusion/result looks valid but hides a broken route?"

False_Green:
  short: "local success with broken global transition"
  test_question: "What passed locally while the route remained invalid?"

MemoryAtom:
  short: "recorded transition that changes future route"
  test_question: "What changed after the commit?"

ShadowAtom:
  short: "recorded unresolved shadow or blocked transition"
  test_question: "What remains HOLD/BLOCK and must not be treated as ALLOW?"
```

---

## 7. Core Method File

File:

```text
docs/02_METHOD_OVERVIEW.md
```

Method:

```text
1. Define State A.
2. Define desired State B.
3. Map route A → B.
4. Identify missing edges.
5. Scan Shadow.
6. Scan PRION / false-green.
7. Assign Gate verdict.
8. Apply minimal repair.
9. Post-verify.
10. Write MemoryAtom or ShadowAtom.
```

Canonical formula:

```text
State A
→ Route Map
→ Shadow Scan
→ PRION Audit
→ Gate Verdict
→ Repair
→ Post Verification
→ MemoryAtom / ShadowAtom
→ State B
```

---

## 8. FACT / MODEL / HYPOTHESIS / HOLD / PRION / COMMIT File

File:

```text
docs/04_FACT_MODEL_HYPOTHESIS_HOLD_PRION_COMMIT.md
```

Definitions:

```yaml
FACT:
  meaning: "supported by actual observation, test, source, or file state"

MODEL:
  meaning: "Vuzol‑19 interpretation layer applied to the fact"

HYPOTHESIS:
  meaning: "possible explanation or route not yet verified"

HOLD:
  meaning: "interesting but not enough Gate evidence for commit"

PRION:
  meaning: "false center, false-green, or broken route pretending to be valid"

COMMIT:
  meaning: "verified transition recorded into memory"
```

Rule:

```text
Bindu separates state labels before commit.
```

---

## 9. Gate Audit Protocol

File:

```text
protocols/GATE_AUDIT_PROTOCOL.md
```

Protocol:

```text
Input:
- current state
- desired state
- route description
- files/evidence
- expected output

Steps:
1. Identify nodes.
2. Identify edges.
3. Find missing edges.
4. Identify Gate.
5. Define Gate pass condition.
6. Run Shadow scan.
7. Run PRION scan.
8. Assign verdict:
   - ALLOW
   - HOLD
   - BLOCK
   - ASK
   - REPAIR_REQUIRED
9. Record reason.
10. Write MemoryAtom or ShadowAtom.
```

Verdict rules:

```yaml
ALLOW:
  condition: "route complete, Gate passed, no unresolved PRION"

HOLD:
  condition: "insufficient data, unclear edge, unresolved hypothesis"

BLOCK:
  condition: "unsafe, false-green, critical missing edge"

ASK:
  condition: "human decision required"

REPAIR_REQUIRED:
  condition: "route can be fixed before commit"
```

---

## 10. PRION / False-Green Audit

File:

```text
protocols/PRION_FALSE_GREEN_AUDIT.md
```

Detection questions:

```text
1. What looks green?
2. What route was not checked?
3. What local success hides global failure?
4. What conclusion sounds final but lacks route evidence?
5. What status, authority, or style is imitating truth?
6. What repeated pattern is being reinforced?
7. What would prove this is not PRION?
```

PRION markers:

```text
always
never
obvious
done
green
no need to check
everyone knows
it passed once
looks correct
too beautiful to question
```

System formula:

```text
local pass
+ missing route audit
+ repeated commit
= possible false-green PRION
```

---

## 11. MemoryAtom Protocol

File:

```text
protocols/MEMORY_ATOM_PROTOCOL.md
```

MemoryAtom fields:

```yaml
id: ""
timestamp: ""
case_id: ""
state_before: ""
state_after: ""
route_taken: ""
gate_verdict: ""
shadow_found: ""
prion_risk: ""
repair_action: ""
post_verification: ""
future_route_change: ""
human_owner: ""
```

Rule:

```text
No commit without MemoryAtom.
```

---

## 12. JSON Schema Example

File:

```text
schemas/transition_case.schema.json
```

```json
{
  "title": "Transition Case Schema",
  "type": "object",
  "required": [
    "case_id",
    "state_a",
    "state_b",
    "route",
    "gate",
    "shadow_scan",
    "prion_audit",
    "verdict"
  ],
  "properties": {
    "case_id": { "type": "string" },
    "state_a": { "type": "string" },
    "state_b": { "type": "string" },
    "route": {
      "type": "array",
      "items": { "type": "string" }
    },
    "gate": {
      "type": "object",
      "properties": {
        "name": { "type": "string" },
        "pass_condition": { "type": "string" }
      }
    },
    "shadow_scan": {
      "type": "array",
      "items": { "type": "string" }
    },
    "prion_audit": {
      "type": "array",
      "items": { "type": "string" }
    },
    "verdict": {
      "type": "string",
      "enum": ["ALLOW", "HOLD", "BLOCK", "ASK", "REPAIR_REQUIRED"]
    }
  }
}
```

---

## 13. First Hello World Case

Folder:

```text
cases/001_hello_world_missing_edge/
```

Scenario:

```text
README says the project can run.

A config file exists.

A test file exists.

But the run command is missing from README.

The test can pass locally,
but a new operator cannot reproduce the route.

This is a missing edge.
```

Case files:

```text
input_state.md
expected_route.md
gate_audit.md
shadow_scan.md
prion_audit.md
repair_plan.md
post_verification.md
memory_atom.json
```

Verdict before repair:

```text
HOLD / REPAIR_REQUIRED
```

Shadow:

```text
route exists in author's memory,
but not in repo memory
```

PRION risk:

```text
"tests pass, so project is ready"
```

Repair:

```text
add run command
add expected output
add verification step
```

Post-verification:

```text
new operator can reproduce route
```

MemoryAtom:

```text
missing edge repaired;
future onboarding route changed
```

---

## 14. Metrics v0

File:

```text
metrics/METRICS_SPEC.md
```

Start simple.

```yaml
route_trace_complete:
  type: "0 or 1"
  question: "Can another operator follow the route?"

missing_edge_count:
  type: "integer"
  question: "How many required route edges are absent?"

false_green_risk:
  type: "LOW / MEDIUM / HIGH"
  question: "Does local success hide global failure?"

gate_verdict_score:
  type: "ALLOW / HOLD / BLOCK / ASK / REPAIR_REQUIRED"

post_verification_status:
  type: "PASS / FAIL / NOT_RUN"

memory_atom_written:
  type: "0 or 1"
```

Minimum success condition:

```text
route_trace_complete = 1
missing_edge_count = 0
false_green_risk != HIGH
post_verification_status = PASS
memory_atom_written = 1
```

---

## 15. First 10 Cases

```text
001_hello_world_missing_edge
002_false_green_readme_config
003_tests_pass_but_docs_fail
004_docs_pass_but_runtime_fails
005_ai_answer_without_route_audit
006_human_review_gate_required
007_shadow_atom_unresolved_dependency
008_prion_status_green_without_evidence
009_memory_atom_after_repair
010_replication_by_second_operator
```

Goal:

```text
10 cases = first small gravity.

50 cases = statistical mass.
```

---

## 16. Roadmap

### Phase 0 — Repo Birth

```text
create repo
add README
add definitions
add method overview
add first protocol
add first case template
```

### Phase 1 — Hello World

```text
create one tiny broken repo/document case
run Gate audit manually
repair missing edge
write MemoryAtom
```

### Phase 2 — Metrics

```text
add metrics spec
score first 10 cases
make false-green visible
```

### Phase 3 — Tooling

```text
add simple CLI
validate schema
generate audit report
write memory atom
```

### Phase 4 — Replication

```text
give case to another operator
compare Gate verdicts
record disagreement
update definitions
```

### Phase 5 — Expansion

```text
AI reasoning
business process
psychological reflection protocol
material Gate reports
element vector Gate table
```

---

## 17. What Not To Do First

Do not start with:

```text
cosmology
theory of everything
clinical psychology
nuclear materials
claims about all science
large mystical manifesto
```

Start with:

```text
one broken transition
one missing edge
one audit
one repair
one MemoryAtom
one replicated result
```

Canon:

```text
The first proof is not scale.

The first proof is repeatability.
```

---

## 18. Connection to World Theory

World Theory remains the deep canon.

This repo is the method lab.

```text
world_theory = source canon / symbolic engine

transition-memory-science = reproducible protocol lab

gitcube-os = execution / runtime / guarded autonomy layer
```

Mapping:

```text
World Theory asks:
what is the mechanism?

Transition Memory Science asks:
can another operator reproduce the Gate verdict?

GitCube OS asks:
can the system execute safely without stealing Human Gate?
```

---

## 19. Final Canon

```text
A theory becomes a discipline
when its transitions can be repeated.

A transition becomes evidence
when its route is preserved.

A result becomes valid
when Gate is passed.

A commit becomes memory
when future routing changes.

A model becomes safe
when it knows where to HOLD.

A false-green becomes PRION
when it imitates truth without route audit.
```

Ukrainian:

```text
Теорія стає дисципліною,
коли її переходи можна повторити.

Перехід стає доказом,
коли його маршрут збережений.

Результат стає валідним,
коли Gate пройдений.

Commit стає памʼяттю,
коли змінює майбутній маршрут.

Модель стає безпечною,
коли знає, де треба HOLD.

False-green стає PRION,
коли імітує істину без аудиту маршруту.
```

---

## 20. Next Action

Create the repository with only the minimum viable structure:

```text
README.md
docs/01_DEFINITIONS.md
docs/02_METHOD_OVERVIEW.md
docs/03_SAFETY_BOUNDARIES.md
protocols/GATE_AUDIT_PROTOCOL.md
protocols/PRION_FALSE_GREEN_AUDIT.md
protocols/MEMORY_ATOM_PROTOCOL.md
cases/000_TEMPLATE/
cases/001_hello_world_missing_edge/
schemas/transition_case.schema.json
```

Then run the first manual audit.

No large claim.

Only one reproducible transition.

```text
STATE: CRYSTAL
NEXT_STEP: HELLO_WORLD_POLYGON
```
