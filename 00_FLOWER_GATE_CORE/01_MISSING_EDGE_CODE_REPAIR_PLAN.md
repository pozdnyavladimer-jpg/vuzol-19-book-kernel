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
