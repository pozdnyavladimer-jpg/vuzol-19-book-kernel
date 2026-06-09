# 14 — MemoryAtom Proof Mark and Repair Window Protocol

**Status:** PRACTICAL_SCHEMA  
**Layer:** GitCube / Flower Gate Core / Trust and Proof Ledger  
**Purpose:** replace fragile rating systems with verified transition memory, so new operators can enter through a controlled proof window instead of being blocked by missing stars.

---

## 0. Core Idea

A marketplace, company, franchise, or AI-to-AI operator system must not trust a person only because they have stars.

A star is often only an opinion.

A verified transition is stronger.

In Flower Gate Core:

```text
Rating = social signal
MemoryAtom = transition trace
Proof Mark = repeated verified transition
Repair Window = controlled path for missing proof
```

The system must not ask only:

```text
Does this operator have a rating?
```

It must ask:

```text
Which Gate did this operator close?
Which transition was performed?
What proof exists?
Who reviewed it?
What memory remains?
Does this proof match the current task?
```

Canonical line:

```text
Old system:
rating opens work

Flower Gate system:
verified transition creates proof
proof opens limited work
repeated proof opens wider Gate
```

---

## 1. Problem: Rating Gate Trap

Many service marketplaces create the same paradox:

```text
to get stars → operator needs work
to get work → operator needs stars
```

This creates a hidden Gate.

A new skilled operator cannot enter.

A client does not want to risk.

Old profiles accumulate power.

Visibility becomes a currency.

This may create corruption-like shadows:

```text
fake reviews
paid promotion
private deals
dumping prices
clan access
hero dependence
rating gate privatization
```

In Flower Gate language:

```text
Rating Gate privatized the transition.
```

The system must not turn trust into a closed caste.

---

## 2. Rating Is Not Proof

A rating may say:

```text
this person was liked
this person was visible
this person had previous clients
```

But it may not say:

```text
which Gate was closed
which checklist was completed
which risk was reduced
which evidence exists
whether the task type matches the rating
whether a supervisor reviewed it
whether the transition left memory
```

Therefore:

```text
Rating ≠ Gate proof
Opinion ≠ transition trace
Popularity ≠ compatibility
```

A system that uses rating as the main Gate can create false-green.

Example:

```text
profile looks green
reviews look good
price looks good
but the concrete task Gate is unknown
```

Verdict:

```text
ASK / REPAIR / HOLD
not automatic OPEN
```

---

## 3. MemoryAtom

A MemoryAtom is a recorded proof of a performed transition.

It does not store only feedback.

It stores:

```text
what transition happened
which Gate was tested
which operator performed it
which documents/checklists were used
which proof was collected
which verdict was given
what memory remains
```

Minimal schema:

```yaml
memory_atom:
  kind: service_transition
  atom_id: ""
  crystal_key: ""

  transition:
    from_state: ""
    to_state: ""
    service_type: ""

  operator:
    operator_id: ""
    status: PROOF_WINDOW
    role:
      primary: ""
      secondary: []

  gate:
    name: ""
    level: 1
    owner: ""

  proofs:
    ticket_exists: false
    checklist_complete: false
    photo_before_after: false
    client_confirmation: false
    senior_operator_review: false
    safety_failure: false

  metrics:
    punctuality: 0.0
    safety: 0.0
    communication: 0.0
    quality: 0.0

  verdict: HOLD

  memory:
    strength: 1
    false_green_risk: false
    notes: ""
```

Canonical rule:

```text
No MemoryAtom → no proof mark
No proof mark → no widened Gate
```

---

## 4. Crystal Key

`crystal_key` is the name of the repeated skill-transition.

It is not a generic category.

It names a stable proof pattern.

Examples for tire shop / shynomontazh:

```text
basic_tire_service.simple_wheel_change
basic_tire_service.pressure_check
basic_tire_service.patch_repair_supervised
advanced_tire_service.high_speed_balancing
guardian.safety_gate_check
communication.client_explanation
repair_after_complaint.client_recovery
```

The system should not say only:

```text
operator has 4.9 stars
```

It should say:

```text
simple_wheel_change      → OPEN level 1
pressure_check           → OPEN level 1
patch_repair_supervised  → ASK / supervised
high_speed_balancing     → HOLD
client_explanation       → REPAIR
safety_gate_check        → not enough atoms
```

This makes trust scoped and task-specific.

---

## 5. Proof Window / Repair Window

If a formal document is missing, the system should not always block the operator forever.

Correct verdict:

```text
No formal document
→ REPAIR_WINDOW / PROOF_WINDOW
→ controlled transition test
→ MemoryAtoms
→ proof mark
→ LIMITED_OPEN
```

A missing document means:

```text
the Gate is not yet closed
```

It does not always mean:

```text
the person is unfit
```

The system must test the transition safely.

Example:

```yaml
missing_document_repair_window:
  candidate: "worker_17"
  business_context: "shynomontazh_franchise"

  missing_documents:
    - balancing_certificate.md
    - franchise_training_complete.md

  status: PROOF_WINDOW

  allowed_tasks:
    - simple_wheel_change
    - pressure_check
    - supervised_patch_repair

  blocked_tasks:
    - high_speed_balancing_solo
    - expensive_tire_repair_solo
    - safety_critical_solo_work

  test_owner: senior_guardian_operator

  test_period:
    duration: "14 days"
    required_cases: 10

  pass_conditions:
    - ticket_created
    - checklist_complete
    - pressure_recorded
    - bolts_checked
    - client_risk_explained
    - no_safety_gate_fail
    - memory_atom_recorded

  verdict: ASK
```

---

## 6. Proof Mark

A Proof Mark is not a like.

It is a visible symbol created from repeated MemoryAtoms.

A Proof Mark means:

```text
this operator repeatedly closed this Gate
under defined conditions
with recorded proof
```

Example:

```yaml
proof_mark:
  gate: basic_tire_service
  crystal_key: basic_tire_service.simple_wheel_change
  level: 1
  symbol: "⭐"

  source:
    required_atoms: 5
    passed_atoms: 5
    failed_atoms: 0
    safety_failures: 0
    guardian_review_required: true
    guardian_approved: true

  verdict: LIMITED_OPEN

  scope:
    allowed:
      - simple_wheel_change
      - pressure_check
    not_allowed:
      - high_speed_balancing_solo
      - structural_wheel_repair_solo
```

The proof mark has scope.

It must not become universal authority.

---

## 7. Proof Mark Levels

Example levels:

```yaml
operator_proof_marks:
  basic_tire_service_level_1:
    symbol: "⭐"
    earned_by:
      - 5 verified tickets
      - 0 critical safety failures
      - all safety checklists complete
      - Guardian approved

  balancing_gate_level_2:
    symbol: "⭐⭐"
    earned_by:
      - 30 verified balancing cases
      - return complaints below threshold
      - senior operator approval

  guardian_safety_level_3:
    symbol: "⭐⭐⭐"
    earned_by:
      - can verify other operators
      - can close safety Gate
      - can issue REPAIR / HOLD verdict
```

A proof mark may decay if the operator stops practicing or if later incidents reveal risk.

```text
Proof must be alive.
Dead proof becomes stale document.
```

---

## 8. Nature Lens: Folding, Chaperone, Marking

In nature, a protein is not functional only because it exists.

It must fold correctly.

If the fold is unstable, the cell may use chaperone systems to help repair or stabilize it.

If it cannot be repaired, the system may mark it for recycling.

Flower Gate translation:

```text
operator without formal proof
→ not automatic BLOCK
→ chaperone / supervisor test
→ repeated safe transitions
→ proof mark
```

But the system must not label a person as a bad protein.

It labels only the state of a Gate:

```text
not "bad worker"

but:
"balancing Gate not yet closed"
"safety proof missing"
"supervised work required"
"REPAIR_WINDOW active"
```

This prevents the proof system from becoming a new caste.

---

## 9. Marketplace Repair

Old marketplace:

```text
profile → rating → client trust → work
```

Flower Gate marketplace:

```text
task packet
→ required Gates
→ candidate packet
→ document edge scan
→ missing proof
→ proof window
→ supervised transition
→ MemoryAtoms
→ proof mark
→ limited work
```

This solves the zero-star trap:

```text
0 stars ≠ BLOCK
0 stars → PROOF_WINDOW
PROOF_WINDOW → small safe tasks
small safe tasks → MemoryAtoms
MemoryAtoms → proof mark
proof mark → LIMITED_OPEN
```

The system does not force clients to risk blindly.

It creates controlled proof routes.

---

## 10. Packet-Lock Integration

The Document Packet Lock checks which document edges match and which are missing.

If formal documents are missing, the packet-lock can return:

```text
REPAIR_WINDOW
```

Example:

```yaml
packet_lock_scan:
  target: master_to_tire_shop_franchise

  matching_edges:
    - edge: safety_gate
      business_document: safety_checklist.md
      operator_document: safety_training.md
      status: MATCH

    - edge: work_skill
      business_document: tire_repair_protocol.md
      operator_document: tire_repair_cases.md
      status: PARTIAL_MATCH

  missing_edges:
    - edge: balancing_gate
      required_document: balancing_certificate.md
      status: MISSING

    - edge: franchise_training_gate
      required_document: completed_franchise_training.md
      status: MISSING

  verdict: REPAIR_WINDOW

  repair_window:
    allowed_tasks:
      - supervised_balancing_cases
    required_atoms: 10
    required_owner: senior_guardian_operator
```

The packet lock does not only reject.

It can generate a path to proof.

---

## 11. Anti-Fake Rating Rules

A fake review can be simple text.

A MemoryAtom requires linked evidence.

Required proof chain:

```text
ticket
→ task category
→ Gate
→ checklist
→ proof artifact
→ client confirmation
→ reviewer / Guardian when needed
→ verdict
→ memory atom
```

Rules:

```text
No ticket → no atom
No Gate → no proof mark
No evidence → weak atom
No reviewer for risky Gate → no level increase
No memory → repeated shadow
```

This does not make fraud impossible.

But it raises the cost of fake trust.

---

## 12. Transition Energy Link

MemoryAtoms can feed Transition Energy.

Energy should not follow popularity alone.

Energy should follow verified transition value.

Example:

```yaml
transition_energy_event:
  operator_id: worker_17
  source_atom: ticket_0001
  crystal_key: basic_tire_service.simple_wheel_change

  energy_awarded:
    base: 1.0
    safety_bonus: 0.5
    memory_bonus: 0.2
    client_trust_bonus: 0.2

  shadow_debt:
    safety_failure: 0.0
    missing_memory: 0.0
    complaint_repair_required: 0.0

  final_energy: 1.9
```

This prevents the old hero-shadow economy:

```text
energy should not feed private Gate control
energy should feed verified transition repair
```

---

## 13. AI Role

AI may:

```text
read task packet
read candidate packet
scan document edges
detect missing proof
propose Proof Window
create MemoryAtom draft
detect false-green risk
calculate proof mark eligibility
show required next Gate
```

AI must not:

```text
invent proof
fake client confirmation
assign final proof mark without Gate owner
auto-open risky tasks
hide failed atoms
convert HOLD into done
```

Canonical AI output:

```yaml
ai_proof_verdict:
  candidate: worker_17
  target_task: high_speed_balancing

  current_status: HOLD

  reason:
    - balancing certificate missing
    - only 2 supervised balancing atoms found
    - required proof mark level not reached

  allowed_path:
    status: REPAIR_WINDOW
    required:
      - 8 more supervised balancing tickets
      - Guardian review
      - no safety failures
      - memory atoms after each case

  verdict: ASK
```

---

## 14. Human Gate

The human operator or responsible Guardian owns the final Gate.

The AI can scan and propose.

The human decides whether proof is sufficient.

```text
AI scan = evidence map
Human Gate = responsibility
Bindu = verdict
Memory = consequence
```

No AI-generated proof mark may become authoritative without the defined Gate owner.

---

## 15. FACT / MODEL / HOLD

FACT:

```text
MemoryAtoms can record tickets, Gate names, proof artifacts, metrics, and verdicts.
Proof marks can be generated from repeated verified atoms.
Repair windows can provide a safe route for operators without formal documents.
```

MODEL:

```text
Rating systems can be replaced or strengthened by transition memory.
Marketplace trust can be rebuilt around proof marks instead of generic stars.
A service franchise can use MemoryAtoms to identify real operator skill by Gate.
```

HOLD:

```text
Do not claim perfect anti-fraud.
Do not claim proof marks replace legal certification where law requires certification.
Do not label a human as defective.
Do not let proof marks become a new caste.
Do not allow AI to issue final authority without Human Gate.
```

---

## 16. Minimal Test

Test scenario:

```text
new worker enters shynomontazh franchise
no rating
no balancing certificate
some informal experience
```

Expected Flower Gate behavior:

```text
not BLOCK forever
not full OPEN
return PROOF_WINDOW
allow small supervised tasks
record MemoryAtoms
create proof mark after enough verified transitions
allow LIMITED_OPEN for scoped tasks
```

Minimal packet:

```yaml
minimal_proof_window_test:
  candidate: worker_17
  initial_rating: 0

  target_gate: basic_tire_service_level_1

  status: PROOF_WINDOW

  required_atoms: 5
  completed_atoms: 0

  allowed_tasks:
    - simple_wheel_change
    - pressure_check

  blocked_tasks:
    - high_speed_balancing_solo

  proof_requirements:
    - ticket_exists
    - checklist_complete
    - photo_before_after
    - client_confirmation
    - guardian_review
    - no_safety_failure

  expected_verdict_after_5_pass:
    proof_mark: "⭐ basic_tire_service_level_1"
    access: LIMITED_OPEN
```

---

## 17. Canonical Formula

```text
formal document missing
≠ automatic BLOCK

formal document missing
→ REPAIR_WINDOW
→ supervised transition
→ MemoryAtom
→ repeated proof
→ Proof Mark
→ LIMITED_OPEN
```

Or shorter:

```text
Rating is opinion.
MemoryAtom is transition trace.
Proof Mark is repeated verified transition.
Repair Window is a safe path from missing proof to earned trust.
```

---

## 18. Final Principle

A fair system must not give full trust without proof.

But it must also not block skilled people forever because they lack initial stars.

The solution is not blind trust.

The solution is controlled transition proof.

```text
No stars → not BLOCK
No stars → Proof Window
Proof Window → MemoryAtoms
MemoryAtoms → Proof Mark
Proof Mark → scoped Gate opening
```

Trust should be born from recorded transitions, not from status, visibility, caste, or purchased attention.
