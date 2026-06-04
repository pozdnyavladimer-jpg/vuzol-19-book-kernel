01_MISSING_EDGE_CODE_REPAIR_PLAN.md

Status: "SCHEMA_PLAN"
Layer: "GitCube / Flower Code Architecture"
Purpose: detect missing service edges before code becomes false-green.

---

0. Core Idea

Bad code is not always badly written.

Often it is written for an incomplete customer field.

The feature works locally, but one room of the business is not connected.

Example:

payment works
customer sees success
order is created

but:

accounting is not updated
warehouse does not reserve items
fraud review is skipped
refund path is missing

This is not only a bug.

This is a missing edge in the 6V board.

---

1. Three Boards

9V = base board / law / rules / permissions / Gate
6V = edge board / service routes / nervous system
3V = signal board / UI / status / user-visible actions

Code must not be created only from 3V.

Code must be created from the full field:

3V signal
→ 6V route
→ 9V Gate
→ Bindu verdict
→ memory update

---

2. Example Problem

Customer asks:

"Add payment"

Bad implementation starts from the button.

async function handlePaymentSuccess(payment) {
  const order = await createOrder(payment)
  await sendCustomerNotification(order)
  return order
}

This looks finished.

But it missed business rooms:

accounting
warehouse
fraud
refund
audit
support

So the code is false-green.

---

3. Required Customer Field Map

Before coding, create the map of rooms:

nodes:
  customer:
    role: user_action_source

  payment:
    role: payment_processor

  order:
    role: order_state_owner

  accounting:
    role: financial_memory

  warehouse:
    role: inventory_state_owner

  fraud:
    role: risk_gate

  notification:
    role: customer_signal

  refund:
    role: reverse_transition

  audit:
    role: memory_and_trace

---

4. Edge Board / 6V Routes

Every important transition must be written as an edge.

edges:
  payment_success_to_order:
    from: payment
    to: order
    trigger: payment_success
    action: create_order
    gate: payment_confirmed
    rollback: cancel_order

  payment_success_to_accounting:
    from: payment
    to: accounting
    trigger: payment_success
    action: create_accounting_entry
    gate: accounting_policy_check
    rollback: void_accounting_entry

  payment_success_to_warehouse:
    from: payment
    to: warehouse
    trigger: payment_success
    action: reserve_items
    gate: inventory_available
    rollback: release_reserved_items

  payment_success_to_notification:
    from: payment
    to: notification
    trigger: payment_success
    action: notify_customer
    gate: order_created
    rollback: notify_payment_review

  payment_suspicious_to_fraud:
    from: payment
    to: fraud
    trigger: payment_suspicious
    action: open_fraud_review
    gate: risk_threshold_exceeded
    rollback: close_fraud_review

Rule:

No important signal should travel without an explicit edge.

---

5. Missing Edge Detection

AI scans code and asks:

Which signals are emitted?
Which rooms should receive them?
Which edges exist?
Which required edges are missing?
Which Gate is missing?

Example scan result:

scan:
  signal_detected: payment_success

  current_code_reaches:
    - order
    - notification

  expected_rooms:
    - order
    - accounting
    - warehouse
    - notification
    - audit

  missing_edges:
    - payment_success_to_accounting
    - payment_success_to_warehouse
    - payment_success_to_audit

  verdict: HOLD

  reason:
    - payment shows GREEN on UI
    - but business field is incomplete
    - 6V board has missing routes

---

6. Safe Router Pattern

Instead of hardcoding all rooms inside one function, use an edge router.

type Signal = {
  type: string
  payload: Record<string, unknown>
}

type Edge = {
  id: string
  from: string
  to: string
  trigger: string
  gate: (signal: Signal) => Promise<boolean>
  action: (signal: Signal) => Promise<void>
  rollback?: (signal: Signal) => Promise<void>
}

export async function routeSignal(signal: Signal, edges: Edge[]) {
  const matchedEdges = edges.filter(edge => edge.trigger === signal.type)

  if (matchedEdges.length === 0) {
    throw new Error(`MISSING_EDGE: no edge for signal ${signal.type}`)
  }

  for (const edge of matchedEdges) {
    const allowed = await edge.gate(signal)

    if (!allowed) {
      throw new Error(`GATE_BLOCKED: ${edge.id}`)
    }

    await edge.action(signal)
  }
}

Now payment code becomes simple:

async function handlePaymentSuccess(payment) {
  await routeSignal(
    {
      type: "payment_success",
      payload: { paymentId: payment.id, orderId: payment.orderId }
    },
    paymentEdges
  )
}

The business nervous system is in the edge board.

The button does not decide the whole company.

---

7. Adding a New Room

If the customer later adds a new room, for example "loyalty", do not rewrite the full payment function.

Add a node:

nodes:
  loyalty:
    role: customer_rewards

Add an edge:

edges:
  payment_success_to_loyalty:
    from: payment
    to: loyalty
    trigger: payment_success
    action: add_reward_points
    gate: customer_verified
    rollback: remove_reward_points

The Flower expands the grid:

payment_success
→ order
→ accounting
→ warehouse
→ notification
→ audit
→ loyalty

---

8. Gate Rule

AI may suggest missing edges.

AI may create draft edge definitions.

AI may create tests.

AI must not auto-merge a new business edge without operator review.

ai_allowed:
  - scan_code
  - detect_missing_edges
  - draft_edge_yaml
  - draft_tests
  - create_transition_packet

ai_blocked:
  - merge_edge_without_owner
  - bypass_gate
  - deploy_incomplete_route

---

9. Test Plan

Create tests that fail when an expected room is not connected.

describe("payment_success edge coverage", () => {
  it("routes payment success to all required rooms", async () => {
    const requiredTargets = [
      "order",
      "accounting",
      "warehouse",
      "notification",
      "audit"
    ]

    const actualTargets = paymentEdges
      .filter(edge => edge.trigger === "payment_success")
      .map(edge => edge.to)

    for (const target of requiredTargets) {
      expect(actualTargets).toContain(target)
    }
  })
})

This test catches the missing room before production.

---

10. Memory Atom After Repair

After adding missing edges, record memory.

memory_atom:
  id: payment_missing_edges_repair_001
  transition: payment_success
  missing_edges_found:
    - accounting
    - warehouse
    - audit

  repair:
    - added payment_success_to_accounting
    - added payment_success_to_warehouse
    - added payment_success_to_audit
    - added edge coverage test

  new_rule:
    payment_success cannot be considered GREEN unless all required business rooms receive the signal

  verdict: REPAIR_COMMITTED

---

11. Canonical Formula

Feature request is not enough.

Customer field must be mapped first.

Code must be generated from:

nodes
+ edges
+ gates
+ rollback
+ memory

If one room is missing, the system must not pretend the feature is finished.

No edge
→ no safe transition

No Gate
→ no commit

No memory
→ repeated shadow

---

12. Final Principle

A good codebase is not only functions.

A good codebase is a nervous system.

Every signal must know:

where it comes from
where it goes
which Gate it passes
who owns the transition
how to rollback
what memory remains

If a new room appears, the system grows by adding a node and an edge.

The Flower expands the grid without breaking the house.

13. Protein Folding Lens

A missing edge in code is similar to a missing contact in protein folding.

A protein is not defined only by its sequence.

A protein becomes functional when its chain creates the right contact network.

amino acid sequence
→ folding path
→ contact edges
→ stable structure
→ active function

Code behaves in a similar way.

A feature is not defined only by functions or files.

A feature becomes functional when its signals create the right service-edge network.

code sequence
→ workflow path
→ service edges
→ stable system behavior
→ business function

Therefore:

correct code locally
does not mean
correct system folding globally

Protein Analogy

In a protein:

amino acids = nodes
chemical contacts = edges
folding path = transition sequence
water / charge / pH = field conditions
chaperone = guided folding assistant
stable protein = functional structure
misfolded protein = false-green structure

In GitCube code architecture:

modules = nodes
service routes = edges
business workflow = transition sequence
customer rules / permissions = field conditions
AI / operator = folding assistant
working feature = functional structure
missing-edge feature = false-green structure

Misfolded Code

A feature can compile, pass local tests, and look finished in UI.

But if one required business room is not connected, the feature is misfolded.

Example:

payment_success
→ order created
→ customer notified

but missing:

→ accounting
→ warehouse
→ audit
→ refund path

This is not only incomplete code.

This is a misfolded transition.

The system has shape, but not full function.

Chaperone Rule

AI should act like a chaperone, not like an owner of the fold.

AI may help the system fold correctly by detecting missing contacts.

AI may suggest new edges.

AI may draft tests.

AI may prepare a transition packet.

AI must not force the fold through a missing Gate.

AI allowed:
- detect missing contacts
- draft missing edges
- propose repair
- create coverage tests

AI blocked:
- auto-merge missing-edge repair
- bypass owner review
- mark false-green as complete

Contact Coverage Test

A codebase needs not only unit tests.

It needs contact coverage tests.

Unit test asks:

Does this function work?

Contact coverage test asks:

Did this signal reach all required rooms?

Example:

payment_success must contact:
- order
- accounting
- warehouse
- notification
- audit

If one required contact is missing, the feature must remain HOLD.

Final Protein Principle

A protein becomes alive through correct folding.

A code feature becomes alive through correct edge connection.

Sequence is not enough.
Files are not enough.
Functions are not enough.

The system must fold into the customer field.

Canonical line:

Missing edge
= missing contact

Missing contact
= misfolded code

Misfolded code
= false-green feature

14. Edge Proposal Form

A new edge must not be added as raw code only.

Every new edge must first be created as a proposal form.

AI may create the proposal.

Human operator must approve the Gate.

TypeScript Schema

type EdgeDefinition = {
  id: string
  from: string
  to: string
  trigger: string

  gate: string
  action: string
  rollback: string
  owner: string

  memory: string
  tests: string[]
  risk: "LOW" | "MEDIUM" | "HIGH" | "CRITICAL"

  status: "DRAFT" | "ASK" | "APPROVED" | "BLOCKED"
}

type FunctionAminoAcid = {
  name: string

  accepts: string[]
  emits: string[]

  requiresGate: string[]
  rollback: string
  memory: string

  sideEffects: string[]
  owner: string
  tests: string[]
}

YAML Blank Form

edge_proposal:
  id: ""

  from: ""
  to: ""
  trigger: ""

  reason:
    problem: ""
    missing_room: ""
    shadow_if_missing: ""

  required_payload:
    - ""

  gate:
    name: ""
    required_checks:
      - ""
    owner: ""

  action:
    function: ""
    function_accepts:
      - ""
    function_emits:
      - ""

  rollback:
    function: ""
    when_to_use:
      - ""

  memory:
    log_to: ""
    memory_atom_required: true

  tests:
    required:
      - ""

  risk:
    level: ""
    reason: ""

  ai_allowed:
    - draft_edge
    - draft_tests
    - prepare_transition_packet

  ai_blocked:
    - auto_merge
    - bypass_owner
    - deploy_without_gate

  verdict:
    status: DRAFT
    required_operator: ""

Example

edge_proposal:
  id: payment_success_to_accounting

  from: payment
  to: accounting
  trigger: payment_success

  reason:
    problem: "Payment succeeds, but accounting may not receive the financial record."
    missing_room: accounting
    shadow_if_missing: "false-green payment: customer sees success, but financial memory is incomplete."

  required_payload:
    - paymentId
    - orderId
    - amount
    - currency
    - customerId

  gate:
    name: accounting_policy_check
    required_checks:
      - payment_confirmed
      - amount_present
      - currency_present
      - customer_id_present
    owner: accounting_operator

  action:
    function: createAccountingEntry
    function_accepts:
      - paymentId
      - orderId
      - amount
      - currency
      - customerId
    function_emits:
      - accounting_entry_created

  rollback:
    function: voidAccountingEntry
    when_to_use:
      - payment_refunded
      - order_cancelled
      - accounting_entry_invalid

  memory:
    log_to: accounting_transition_log
    memory_atom_required: true

  tests:
    required:
      - test_payment_success_routes_to_accounting
      - test_accounting_entry_requires_payment_confirmed
      - test_accounting_entry_can_rollback

  risk:
    level: HIGH
    reason: "Missing accounting edge creates financial mismatch after successful payment."

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
    required_operator: accounting_operator

Rule

No edge proposal
→ no new route

No Gate owner
→ no commit

No rollback
→ no safe transition

No memory
→ repeated shadow

Canonical Line

A function is an amino acid.

An edge is a contact.

A workflow is folding.

The Edge Proposal Form is the Gate
that decides whether this contact may become part of the living system.
