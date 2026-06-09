# 19 — Board Propagation, Repair Clock and Shadow Atom Protocol

**Folder:** `00_FLOWER_GATE_CORE`  
**Status:** CORE CONNECTIVE PROTOCOL  
**Layer:** Flower Gate Core / 4D Grid Runtime / Country-as-Board Scanner  
**Depends on:** `17_OCTAVE_PHASE_TRANSITION_MATH_CORE.md`, `18_COUNTRY_AS_4D_GRID_AND_LLM_BOARD_SCANNER.md`  
**Purpose:** define how one board affects another board, how repair is timed, how hidden debt is recorded, and how blocked transitions receive an appeal/repair path.

---

## 0. Why this file exists

Files `17` and `18` define two major layers:

```text
17 = how systems jump between behavior octaves
18 = how a country can be read as one 4D grid of transition boards
```

But one mechanism is still missing:

```text
How does pressure move from one board to another?
How does repair move from one board to another?
How does false-green return later if it was not recorded?
When does the system re-scan?
How does a blocked operator appeal or repair the verdict?
```

This file adds the connective runtime:

```text
Board Scan
→ Gate Verdict
→ MemoryAtom / ShadowAtom
→ Propagation Map
→ Repair Clock
→ Re-scan
→ Octave Shift / Repair / Collapse Warning
```

Canonical line:

```text
A board is never isolated.
```

---

## 1. Core thesis

A 3/6/9 board is not a closed object.

Every board touches other boards.

```text
student board touches labor market board
labor market board touches business board
business board touches tax board
tax board touches education board
education board touches student board
```

Or:

```text
forest board touches water board
water board touches soil board
soil board touches food board
food board touches social pressure board
social pressure board touches political board
```

Therefore:

```text
Gate failure propagates.
Repair propagates.
Shadow propagates.
Memory propagates.
```

The system must not only scan one board.

It must scan how board states travel across the grid.

---

## 2. Board Propagation Rule

```text
A board is never isolated.

Every Gate failure creates pressure in neighboring boards.
Every repaired edge reduces pressure in neighboring boards.
Every MemoryAtom must declare which boards it affects.
Every ShadowAtom must declare where the hidden debt may reappear.
```

Ukrainian form:

```text
Плата ніколи не ізольована.

Кожен провал Gate створює тиск у сусідніх платах.
Кожне відремонтоване ребро зменшує тиск у сусідніх платах.
Кожен MemoryAtom має показувати, які плати він змінює.
Кожен ShadowAtom має показувати, де тінь може повернутися.
```

---

## 3. Board as propagation node

A board must be treated as a node in a higher grid.

```yaml
board:
  board_id: education.entry_gate.students
  domain: education
  visible_signal: "students cannot get first jobs"
  neighboring_boards:
    - labor_market.junior_access
    - business.hiring_risk
    - university.curriculum_feedback
    - platform.proof_mark_system
  current_verdict: REPAIR
```

A board has:

```text
3V = visible signal
6V = edge / route / document compatibility
9V = Gate / law / authority / risk / permission
```

But it also has:

```text
neighbors = boards affected by this board
propagation = how pressure, repair, shadow, or memory travels
clock = when the board must be re-scanned
appeal = how a blocked transition can be challenged or repaired
```

---

## 4. Propagation types

### 4.1 Pressure propagation

When a board remains unresolved, pressure moves outward.

Example:

```text
student cannot enter profession
↓
young specialists are missing
↓
business becomes weaker
↓
taxes decrease
↓
education funding weakens
↓
more students cannot enter profession
```

This is a pressure loop.

```yaml
pressure_propagation:
  source_board: education.entry_gate.students
  pressure_type: blocked_entry
  affected_boards:
    - labor_market.junior_access
    - business.hiring_capacity
    - tax.base_future
    - education.curriculum_repair
  risk: self_reinforcing_loop
```

### 4.2 Shadow propagation

When a hidden problem is not recorded, it returns elsewhere.

Example:

```text
road repair looks complete
↓
material quality was not checked
↓
road fails after 6 months
↓
budget is spent again
↓
public trust decreases
```

This is false-green returning as shadow.

```yaml
shadow_propagation:
  source_board: infrastructure.road_repair
  hidden_shadow: material_quality_not_verified
  may_reappear_in:
    - budget.duplicate_spending
    - trust.public_institutions
    - transport.accident_risk
  verdict: FALSE_GREEN_WARNING
```

### 4.3 Repair propagation

Repair also spreads.

Example:

```text
Proof Window for students
↓
first verified tasks
↓
junior hiring risk decreases
↓
business can hire earlier
↓
education receives feedback
↓
more students get proof path
```

```yaml
repair_propagation:
  source_board: education.entry_gate.students
  repair_action: proof_window_with_memory_atoms
  affected_boards:
    - labor_market.junior_access
    - business.hiring_risk
    - platform.proof_mark_system
    - education.curriculum_feedback
  expected_effect: pressure_reduction
```

### 4.4 Memory propagation

A good MemoryAtom must not only record what happened.

It must also record which future boards should change.

```yaml
memory_propagation:
  memory_atom_id: ma_2026_001
  crystal_key: junior_developer.unit_test_delivery
  verdict: PASS
  affects_boards:
    - operator.worker_17.proof_profile
    - platform.junior_proof_marks
    - employer.safe_task_routing
  next_scan_after: "30 days"
```

---

## 5. ShadowAtom

`MemoryAtom` records a verified transition.

But a 4D grid also needs `ShadowAtom`.

A `ShadowAtom` records a hidden debt, false-green result, failed Gate, or delayed consequence.

Important boundary:

```text
ShadowAtom is not a label against a person.
ShadowAtom is a record of an unresolved transition shadow.
```

It records:

```text
what looked green
which Gate was not actually closed
where the shadow may return
which repair path is required
when to re-scan
```

Example:

```yaml
shadow_atom:
  kind: gate_failure
  domain: public_procurement
  board_id: infrastructure.road_repair
  visible_result: "road marked as repaired"
  failed_gate: material_quality_gate
  hidden_shadow: "same road failed after 6 months"
  verdict: FALSE_GREEN
  affected_boards:
    - budget.duplicate_spending
    - transport.safety
    - trust.public_institutions
  required_repair:
    - open_contractor_history
    - material_quality_proof
    - independent_inspection
    - memory_atom_after_12_months
  next_scan_after: "6 months"
```

Canonical line:

```text
A system that records only success loses reality.
A system that records ShadowAtoms keeps memory of what must be repaired.
```

---

## 6. Repair Clock

Repair is not instant.

A transition may look solved now and fail later.

Therefore every board needs a clock.

```text
Repair Clock = rule that defines when a board, Gate, proof mark, or repair must be checked again.
```

Repair Clock asks:

```text
When should this Gate be re-scanned?
When does a Proof Mark expire or require renewal?
When can false-green become visible?
When should Nature Gate be checked again?
When should a MemoryAtom be confirmed by delayed result?
```

Example:

```yaml
repair_clock:
  board_id: service.tire_shop.basic_service
  proof_mark: basic_tire_service_level_1
  scan_cycle:
    after_each_ticket: true
    weekly_summary: true
    renewal_after: "90 days"
  decay_rules:
    if_no_recent_atoms: reduce_confidence
    if_shadow_atom_created: require_guardian_review
    if_three_pass_atoms_after_repair: restore_limited_open
```

For nature:

```yaml
repair_clock:
  board_id: nature.river_repair
  scan_cycle:
    water_quality_check: "monthly"
    biodiversity_check: "seasonal"
    soil_impact_check: "yearly"
  delayed_shadow_window: "5 years"
```

Canonical line:

```text
No repair without re-scan.
No proof without decay.
No green without delayed check.
```

---

## 7. Hysteresis: repair is not reset

A system does not always return by the same path.

After damage, the old state may no longer exist.

```text
Ωₙ → Ωₙ₊₁
```

does not imply:

```text
Ωₙ₊₁ → Ωₙ
```

Sometimes repair leads to:

```text
Ωₙ₊₁ → Ωₙ'
```

where `Ωₙ'` is a repaired state with scar memory.

Canonical line:

```text
Repair is not reset.
Repair is a new state with memory of the scar.
```

Ukrainian form:

```text
Ремонт — це не стирання помилки.
Ремонт — це новий стан із памʼяттю про шрам.
```

Examples:

```text
degraded soil may recover, but not instantly
lost trust may return, but with new verification rules
failed junior hiring may recover, but with mentor Gate
corrupted procurement may recover, but with open audit memory
```

This is why `MemoryAtom` and `ShadowAtom` must both remain visible.

---

## 8. Appeal Gate

If AI scans a board and gives a verdict, the system must not become a hidden scoring machine.

Every blocked transition must have a visible appeal or repair path.

```text
No hidden score without appeal.
No blocked transition without repair path.
```

Ukrainian form:

```text
Нема прихованого балу без права на оскарження.
Нема заблокованого переходу без шляху repair.
```

Appeal Gate requires:

```text
visible reason
visible affected Gate
visible missing edge
visible evidence
visible repair route
human owner
next scan time
```

Example:

```yaml
appeal_gate:
  blocked_transition: operator.worker_17.advanced_balancing
  verdict: HOLD
  reason: "balancing proof missing"
  missing_edge: balancing_certificate_or_supervised_cases
  appeal_allowed: true
  repair_route:
    - complete_5_supervised_balancing_tickets
    - record_memory_atoms
    - guardian_review
    - re_scan_after_completion
  gate_owner: senior_guardian_operator
```

Boundary:

```text
AI may scan.
AI may explain.
AI may propose repair.
AI may not silently punish.
Human Gate remains required.
```

---

## 9. Board cascade example: LinkedIn / Kabanchik / students

### 9.1 Old platform logic

```text
no followers → no attention → no proof → idea ignored
no stars → no orders → no proof → worker ignored
no experience → no job → no proof → student ignored
```

These are three versions of the same blocked Gate.

```text
Attention Gate
Reputation Gate
Experience Gate
```

### 9.2 Flower Gate repair

```text
no proof ≠ BLOCK
no proof → Proof Window
Proof Window → small verified transition
small verified transition → MemoryAtom
MemoryAtom → Proof Mark
Proof Mark → Limited Open
```

### 9.3 Propagation map

```yaml
platform_entry_cascade:
  blocked_boards:
    - linkedin.idea_attention_gate
    - kabanchik.worker_reputation_gate
    - education.student_experience_gate

  shared_pattern:
    missing_old_proof: true
    false_black_risk: true
    repair_window_needed: true

  repair_protocol:
    - create_small_safe_task
    - require_visible_evidence
    - require_human_or_guardian_review
    - record_memory_atom
    - issue_scoped_proof_mark
    - open_limited_gate

  affected_boards_after_repair:
    - labor_market.entry_flow
    - platform.trust_quality
    - business.hiring_capacity
    - idea.diffusion_path
```

Canonical line:

```text
A blocked first transition is not a small problem.
It can become a national cascade.
```

---

## 10. Country cascade example: forest → water → soil → food → pressure

```text
forest removal
↓
water cycle disruption
↓
soil degradation
↓
food instability
↓
price pressure
↓
social pressure
↓
political instability
```

This is not only environmental damage.

It is memory damage propagating across boards.

```yaml
nature_cascade:
  source_board: nature.forest_memory
  failed_gate: regeneration_gate
  shadow_atom:
    hidden_shadow: "loss of water regulation and soil memory"
  affected_boards:
    - nature.water_flow_memory
    - agriculture.soil_storage_layer
    - food.price_stability
    - society.social_pressure
    - finance.repair_cost
  required_repair_clock:
    water_check: "seasonal"
    soil_check: "yearly"
    biodiversity_check: "yearly"
    finance_shadow_audit: "yearly"
```

Canonical line:

```text
Nature damage is not local.
It is board propagation through the memory infrastructure of life.
```

---

## 11. LLM board scanner workflow

A useful AI scanner must not only summarize a document.

It must build a board and propagation map.

```text
input report
→ extract visible signal
→ build 3/6/9 board
→ detect missing edges
→ detect Gate failures
→ detect possible false-green
→ create MemoryAtom or ShadowAtom draft
→ map affected neighboring boards
→ propose Repair Clock
→ expose Appeal Gate
→ require Human Gate
```

Example output:

```yaml
llm_board_scan:
  report_id: report_road_repair_2026_001
  board_id: infrastructure.road_repair

  three_v:
    visible_signal: "road repaired"
    public_claim: "project completed"

  six_v:
    matching_edges:
      - contractor_contract
      - payment_record
    missing_edges:
      - material_quality_proof
      - independent_inspection
      - delayed_performance_check

  nine_v:
    gates:
      - procurement_gate
      - quality_gate
      - public_safety_gate
    failed_or_unknown:
      - quality_gate
      - delayed_performance_gate

  verdict: HOLD_FALSE_GREEN_RISK

  atom_draft:
    type: ShadowAtom
    reason: "visible completion without delayed quality proof"

  propagation:
    affected_boards:
      - budget.duplicate_spending
      - transport.safety
      - public_trust

  repair_clock:
    next_scan_after: "6 months"

  appeal_gate:
    owner: infrastructure_guardian
    required_evidence:
      - quality_test
      - inspection_report
      - delayed_photo_trace
```

---

## 12. Connection to octave math

File `17` defines octave transition:

```text
Ωₙ = { Gₙ, Mₙ, Pₙ, Sₙ }
```

This file adds the fact that `Ωₙ` does not change in isolation.

```text
Ωₙ(board A) affects Ωₙ(board B)
```

A local Gate failure can prevent octave rise in a neighboring board.

A local repair can help neighboring boards stabilize.

Example:

```text
Proof Window for students
→ more verified junior operators
→ lower hiring risk
→ stronger business capacity
→ better tax base
→ better education feedback
```

This is an upward repair cascade.

Opposite example:

```text
Nature Gate failure
→ soil/water memory loss
→ food pressure
→ social pressure
→ political instability
→ corruption pressure
```

This is a downward shadow cascade.

Canonical line:

```text
Octave jump is not only internal.
It can be enabled or blocked by neighboring boards.
```

---

## 13. Connection to country-as-grid

File `18` defines:

```text
Country = 4D grid of transitions.
People are not the target.
Blocked transitions are the target.
AI is not the ruler.
AI is the board scanner.
```

This file adds:

```text
The country is not only many boards.
The country is propagation between boards.
```

Therefore, country repair must focus on:

```text
where pressure starts
where shadow hides
where repair would spread
where memory is missing
where appeal is blocked
where Nature Gate is ignored
```

---

## 14. Minimal runtime test

A minimal prototype of this protocol requires:

```text
3 boards
1 Gate failure
1 MemoryAtom
1 ShadowAtom
1 propagation map
1 Repair Clock
1 Appeal Gate
1 Human Gate verdict
```

Example prototype:

```text
board A: student_entry_gate
board B: junior_hiring_risk
board C: business_growth_capacity
```

Test:

```text
A has blocked entry.
System proposes Proof Window.
Student completes small task.
MemoryAtom created.
B receives reduced hiring risk.
C receives increased candidate capacity.
Repair Clock schedules next scan.
Appeal Gate remains visible.
```

Success condition:

```text
AI does not score people silently.
AI identifies blocked transitions.
AI drafts MemoryAtom / ShadowAtom.
AI maps propagation.
AI proposes repair and re-scan.
Human Gate decides.
```

---

## 15. Failure modes

### 15.1 Hidden scoring

```text
AI creates invisible score
operator cannot appeal
blocked person receives no repair path
```

Verdict:

```text
BLOCK_SYSTEM_DESIGN
```

### 15.2 Success-only memory

```text
system records only PASS atoms
failures are hidden
false-green grows
```

Verdict:

```text
FALSE_GREEN_MEMORY
```

### 15.3 No decay

```text
proof mark never expires
old skill is treated as current skill
```

Verdict:

```text
STALE_PROOF_RISK
```

### 15.4 No propagation map

```text
board is repaired locally
neighboring boards keep pressure
system thinks repair succeeded
```

Verdict:

```text
LOCAL_GREEN_GLOBAL_SHADOW
```

### 15.5 No Nature Gate

```text
finance and policy pass human documents
but nature memory is damaged
```

Verdict:

```text
CIVILIZATION_ALZHEIMER_RISK
```

---

## 16. Canonical principles

```text
A board is never isolated.
```

```text
No repair without re-scan.
```

```text
Repair is not reset.
Repair is a new state with memory of the scar.
```

```text
No hidden score without appeal.
```

```text
No blocked transition without repair path.
```

```text
A system that records only success loses reality.
```

```text
Gate failure propagates.
Repair propagates.
Shadow propagates.
Memory propagates.
```

---

## 17. Final formula

```text
Board Scan
→ Gate Verdict
→ MemoryAtom / ShadowAtom
→ Propagation Map
→ Repair Clock
→ Appeal Gate
→ Human Gate
→ Re-scan
→ Octave Shift / Repair / Collapse Warning
```

Short form:

```text
Scan
→ Atom
→ Propagate
→ Repair Clock
→ Appeal
→ Re-scan
```

Final line:

```text
A 4D grid becomes alive only when it can see how one transition changes the next board.
```

Ukrainian:

```text
4D-сітка стає живою тільки тоді,
коли бачить,
як один перехід змінює наступну плату.
```
