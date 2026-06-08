08 — Role-Classified Edges and Operator Archetypes

Status: "PRACTICAL_SCHEMA"
Layer: "GitCube / Flower Gate Core"
Purpose: classify every edge by the role it performs inside the field, so AI can detect not only missing routes, but missing field functions.

---

0. Core Idea

An edge is not only a route.

An edge has a function.

Two edges may both connect nodes, but they do different work in the organism.

Example:

payment_success_to_accounting
= memory / financial trace / accounting stability

payment_suspicious_to_fraud
= risk Gate / protection / pressure containment

payment_failed_to_support
= repair / human consequence / service recovery

Without role classification, AI sees only that an edge is missing.

With role classification, AI sees what kind of field function is missing.

Canonical line:

Color tells state.
Role tells function.
Edge tells route.
Gate tells permission.
Bindu tells verdict.
Memory tells consequence.

---

1. Why Roles Are Needed

The previous Flower Gate Core files define:

00 = law of transition
01 = missing edge / misfolded code / false-green
02 = code cell / edge proposal form
03 = color verdict / Human Gate
04 = operator repos / document-as-edge
05 = minimal customer code grid test
06 = V-Kernel to GitCube company field bridge
07 = AI field consciousness as gated diffusion

These files make transitions visible.

This file adds role classification.

Role classification answers:

What does this edge do for the field?

Does it protect?
Does it direct?
Does it build?
Does it repair?
Does it verify Gate?
Does it reveal hidden pattern?
Does it decide final transition?

A route without role may exist, but the system may still not understand its purpose.

A role-classified edge tells AI why the edge matters.

---

2. Base Operator Archetypes

The archetypes are not fantasy roles.

They are operational functions inside the field.

TANK
= pressure holder / impact absorber / stabilizer under stress

ARCHER
= direction giver / route selector / precise signal sender

ENGINEER
= structure maker / schema builder / document shaper / implementation organizer

HEALER
= repair operator / rollback designer / support bridge / coherence restorer

GUARDIAN
= Gate owner / permission checker / policy protector / risk blocker

MAGE
= pattern revealer / model synthesizer / hidden relation detector / unknown translator

BINDU
= final verdict center / transition arbiter / commit-hold-repair-block decision point

These are functions, not titles.

One human operator may hold several roles.

One AI proposal may touch several roles.

One edge may have primary and secondary roles.

---

3. Role Versus Color

Color and role must not be confused.

Color = current compressed state.
Role = field function.

Example:

A Guardian edge can be BLUE when Gate is active.
A Guardian edge can be RED when risk pressure is high.
A Guardian edge can be BLACK when scope is unknown.
A Guardian edge can be GREEN only after Gate, edge, rollback, owner, and memory are confirmed.

Role does not prove readiness.

Color does not prove function.

Both must be checked.

Mapping:

RED
= pressure / risk / anomaly

ORANGE
= movement / flow / active transition

YELLOW
= structure / document / form

BLUE
= Gate / permission / owner / law

GREEN
= stability / readiness / allowed transition

VIOLET
= memory / shadow history / invisible influence

BLACK
= blind zone / unknown dependency

WHITE
= clean record / documentation / memory trace

Role answers: what work is needed?

Color answers: what state is the work in?

---

4. Role-Classified Edge Schema

Every important edge may include role metadata.

role_classified_edge:
  id: ""

  from: ""
  to: ""
  trigger: ""

  edge_role:
    primary: ""
    secondary:
      - ""

  role_reason:
    - ""

  color_state:
    visible_color: ""
    suspected_true_state: ""
    false_green_risk: false

  gate:
    name: ""
    owner: ""
    required_checks:
      - ""

  action:
    function: ""
    emits:
      - ""

  rollback:
    function: ""
    required: true

  memory:
    required: true
    atom_type: ""

  tests:
    required:
      - ""

  ai_allowed:
    - detect_missing_role
    - draft_role_classified_edge
    - draft_tests
    - prepare_transition_packet

  ai_blocked:
    - auto_assign_human_role_authority
    - auto_merge_business_edge
    - bypass_gate

  verdict:
    status: DRAFT
    required_operator: ""

Canonical rule:

No role classification
→ route may be visible but field function remains unclear.

No Gate owner
→ no commit.

No memory
→ repeated shadow.

---

5. Payment Feature Example

Customer request:

Add card payment to the website.

A weak system sees:

payment button
payment provider
success message

A Flower system sees required role-functions.

payment_success requires:

- order creation
- accounting memory
- warehouse reservation
- audit trace
- refund rollback
- support preparation
- fraud risk gate
- customer notification

Each required route has a role.

---

6. Payment Edge Role Board

payment_edge_role_board:
  project: card_payment_feature

  source_event: payment_success

  edges:
    - id: payment_success_to_order
      from: payment
      to: order
      role:
        primary: ENGINEER
        secondary:
          - ARCHER
      reason:
        - "Creates structured order state."
        - "Routes payment signal into business object."
      required_gate: order_creation_gate
      memory_required: true

    - id: payment_success_to_accounting
      from: payment
      to: accounting
      role:
        primary: GUARDIAN
        secondary:
          - ENGINEER
          - MEMORY
      reason:
        - "Protects financial truth."
        - "Creates accounting memory."
        - "Prevents false-green payment without financial trace."
      required_gate: accounting_policy_check
      memory_required: true

    - id: payment_success_to_warehouse
      from: payment
      to: warehouse
      role:
        primary: TANK
        secondary:
          - ENGINEER
      reason:
        - "Holds inventory pressure."
        - "Reserves real resource after payment."
      required_gate: inventory_available
      memory_required: true

    - id: payment_success_to_audit
      from: payment
      to: audit
      role:
        primary: GUARDIAN
        secondary:
          - VIOLET_MEMORY
      reason:
        - "Records transition trace."
        - "Prevents repeated shadow."
        - "Protects future Gate decisions."
      required_gate: audit_memory_gate
      memory_required: true

    - id: payment_success_to_notification
      from: payment
      to: notification
      role:
        primary: ARCHER
        secondary:
          - CUSTOMER_SIGNAL
      reason:
        - "Sends precise signal to customer."
        - "Must not announce success before deeper Gates close."
      required_gate: order_created
      memory_required: false

    - id: payment_failed_to_support
      from: payment
      to: support
      role:
        primary: HEALER
        secondary:
          - HUMAN_CONSEQUENCE
      reason:
        - "Creates repair path for human consequence."
        - "Prevents failure from becoming abandoned user state."
      required_gate: support_response_policy
      memory_required: true

    - id: payment_suspicious_to_fraud
      from: payment
      to: fraud
      role:
        primary: GUARDIAN
        secondary:
          - TANK
      reason:
        - "Blocks unsafe transition."
        - "Holds risk pressure before order finalization."
      required_gate: risk_threshold_exceeded
      memory_required: true

    - id: payment_refund_to_accounting
      from: refund
      to: accounting
      role:
        primary: HEALER
        secondary:
          - MEMORY
      reason:
        - "Repairs reverse financial transition."
        - "Prevents refund from breaking accounting trace."
      required_gate: refund_policy_gate
      memory_required: true

---

7. Missing Role Detection

AI must detect not only missing edges, but missing roles.

Example scan:

role_scan:
  target: card_payment_feature
  source_event: payment_success

  current_edges:
    - payment_success_to_order
    - payment_success_to_notification

  required_role_functions:
    - ENGINEER_ORDER_STATE
    - GUARDIAN_ACCOUNTING_MEMORY
    - TANK_INVENTORY_RESERVATION
    - GUARDIAN_AUDIT_TRACE
    - HEALER_REFUND_ROLLBACK
    - HEALER_SUPPORT_PATH
    - GUARDIAN_FRAUD_RISK_GATE
    - ARCHER_CUSTOMER_NOTIFICATION

  missing_role_functions:
    - GUARDIAN_ACCOUNTING_MEMORY
    - TANK_INVENTORY_RESERVATION
    - GUARDIAN_AUDIT_TRACE
    - HEALER_REFUND_ROLLBACK
    - HEALER_SUPPORT_PATH
    - GUARDIAN_FRAUD_RISK_GATE

  visible_color: GREEN
  suspected_true_state: YELLOW_BLUE_VIOLET_INCOMPLETE
  false_green_risk: true

  verdict: HOLD

  reason:
    - "The visible payment flow exists."
    - "The required role-functions of the field are incomplete."
    - "This is not only missing code; it is missing field function."

Canonical line:

Missing edge = missing route.
Missing role = missing function.
Missing Gate = missing permission.
Missing memory = repeated shadow.

---

8. Role-Classified Edge Proposal

When a missing role is detected, AI creates an edge proposal with role metadata.

Example:

edge_proposal:
  id: payment_success_to_audit

  from: payment
  to: audit
  trigger: payment_success

  edge_role:
    primary: GUARDIAN
    secondary:
      - VIOLET_MEMORY

  reason:
    problem: "Payment success has no audit memory trace."
    missing_room: audit
    missing_role_function: GUARDIAN_AUDIT_TRACE
    shadow_if_missing: "Payment can look complete while no trace exists for future investigation."

  required_payload:
    - paymentId
    - orderId
    - amount
    - currency
    - customerId
    - providerEventId
    - timestamp

  gate:
    name: audit_memory_gate
    required_checks:
      - provider_event_confirmed
      - order_id_present
      - amount_present
      - audit_schema_valid
    owner: audit_operator

  action:
    function: recordPaymentAuditMemory
    function_accepts:
      - paymentId
      - orderId
      - amount
      - currency
      - customerId
      - providerEventId
      - timestamp
    function_emits:
      - payment_audit_memory_recorded

  rollback:
    function: markAuditRecordVoided
    when_to_use:
      - provider_event_reversed
      - payment_voided
      - audit_record_invalid

  memory:
    log_to: payment_audit_memory_log
    memory_atom_required: true

  tests:
    required:
      - test_payment_success_routes_to_audit
      - test_audit_record_requires_provider_event
      - test_audit_record_can_be_voided

  risk:
    level: HIGH
    reason: "Without audit memory, payment transition has no future accountability trace."

  ai_allowed:
    - draft_edge
    - draft_tests
    - prepare_transition_packet

  ai_blocked:
    - auto_merge
    - bypass_owner
    - deploy_without_gate

  verdict:
    status: ASK
    required_operator: audit_operator

---

9. Operator Role Packet

An operator can expose not only color and documents, but also active role responsibility.

operator_role_packet:
  operator_id: audit_operator
  project_id: card_payment_feature

  active_roles:
    - GUARDIAN
    - VIOLET_MEMORY

  current_color: VIOLET
  current_octave: 9

  owns:
    - audit_memory_gate
    - payment_audit_memory_rule
    - transition_trace_schema

  required_edges:
    - payment_success_to_audit
    - payment_refund_to_audit
    - fraud_review_to_audit

  current_documents:
    - CURRENT_DOCUMENTS/audit_policy.md

  missing_documents:
    - CURRENT_DOCUMENTS/payment_memory_rule.md

  verdict: HOLD

Rule:

Operator role packet represents project responsibility.
It does not represent the private person.

---

10. AI Role With Role-Classified Edges

AI can now say:

I found a missing edge.

But more importantly:

I found a missing Guardian-Audit-Trace function.

Correct AI output:

missing_role_verdict:
  target: card_payment_feature
  transition: payment_success

  missing_edge: payment_success_to_audit
  missing_role_function: GUARDIAN_AUDIT_TRACE

  visible_color: GREEN
  suspected_true_state: VIOLET_MEMORY_MISSING
  false_green_risk: true

  required_operator: audit_operator
  required_gate: audit_memory_gate

  verdict: HOLD

  required_action:
    - create edge proposal
    - draft payment_memory_rule.md
    - request audit_operator Gate
    - add contact coverage test
    - record memory atom

Incorrect AI output:

I added payment and everything is done.

---

11. Role and Payment Logic

Role classification makes operator payment safer later.

A role should not be paid only because someone has a title.

A role is paid when the transition function is verified.

Examples:

Guardian reward
= valid Gate check, valid BLOCK, valid HOLD, valid risk prevention

Healer reward
= valid repair edge, rollback definition, support recovery, coherence restoration

Engineer reward
= valid structure, schema, document, working implementation route

Archer reward
= precise route selection, signal delivery, priority alignment

Tank reward
= pressure stabilization, resource containment, impact absorption

Mage reward
= hidden pattern detection, model synthesis, unknown converted into visible form

Bindu reward
= final accountable verdict after field check

Payment must follow verified transition value, not noise volume.

This file does not define the full payment protocol.

It only prepares the role layer.

---

12. Role-Classified Contact Coverage Test

A codebase needs role coverage, not only edge coverage.

Edge coverage asks:

Did the signal reach all required rooms?

Role coverage asks:

Did the signal activate all required field functions?

Example:

describe("payment_success role coverage", () => {
  it("covers all required role functions", () => {
    const requiredRoles = [
      "ENGINEER_ORDER_STATE",
      "GUARDIAN_ACCOUNTING_MEMORY",
      "TANK_INVENTORY_RESERVATION",
      "GUARDIAN_AUDIT_TRACE",
      "HEALER_REFUND_ROLLBACK",
      "ARCHER_CUSTOMER_NOTIFICATION"
    ]

    const actualRoles = paymentEdges
      .filter(edge => edge.trigger === "payment_success")
      .flatMap(edge => edge.roleFunctions)

    for (const role of requiredRoles) {
      expect(actualRoles).toContain(role)
    }
  })
})

If a required role-function is missing, the transition remains HOLD.

---

13. Memory Atom After Role Repair

After adding a missing role-classified edge, record memory.

memory_atom:
  id: payment_success_role_repair_001
  project: card_payment_feature
  transition: payment_success

  detected_issue:
    missing_edge: payment_success_to_audit
    missing_role_function: GUARDIAN_AUDIT_TRACE
    false_green_risk: true

  repair:
    - created role-classified edge proposal
    - assigned primary role GUARDIAN
    - assigned secondary role VIOLET_MEMORY
    - requested audit_operator Gate
    - added role coverage test
    - added payment audit memory rule

  new_rule:
    payment_success cannot be true-green unless Guardian-Audit-Trace role is covered

  verdict: REPAIR_COMMITTED

---

14. FACT / MODEL / HOLD

FACT:

Roles can be used as schema metadata for edges, operators, tests, and transition packets.

MODEL:

Tank, Archer, Engineer, Healer, Guardian, Mage, and Bindu can classify field functions across code, business, AI, and book structure.

HOLD:

Do not treat role labels as proof of contribution.
Do not pay or approve by label alone.
Do not let AI assign human authority automatically.
Do not let role labels replace Gate, evidence, tests, rollback, or memory.

Rule:

Role is a classification.
Role is not authority by itself.

---

15. Canonical Formula

state
→ color
→ role-function
→ edge
→ Gate
→ Bindu
→ memory

Or:

Signal
→ which state?
→ which function is needed?
→ which edge carries it?
→ who owns Gate?
→ what is the verdict?
→ what memory remains?

---

16. Short Form

A company or codebase does not only need edges.

It needs role-classified edges.

An edge tells where a signal goes.

A role tells what kind of field work that edge performs.

Without role classification, AI may know that a route exists but not why it matters.

With role classification, AI can detect missing field functions:

missing Guardian edge
missing Healer rollback
missing Tank pressure holder
missing Archer direction
missing Engineer structure
missing Mage pattern scan
missing Bindu verdict

This makes false-green easier to detect.

---

Final Sentence

The Flower Gate Core becomes operational when every important edge knows not only where it goes, but what role it performs in protecting, directing, repairing, structuring, revealing, or deciding the transition.
