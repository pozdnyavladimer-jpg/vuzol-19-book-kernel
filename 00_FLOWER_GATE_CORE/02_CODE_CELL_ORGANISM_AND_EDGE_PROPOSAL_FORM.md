02_CODE_CELL_ORGANISM_AND_EDGE_PROPOSAL_FORM.md

Status: "PRACTICAL_SCHEMA"
Layer: "GitCube / Flower Code Architecture"
Purpose: define code as a living cell/organism and define the Edge Proposal Form as the membrane through which a new transition enters the system field.

---

0. Core Idea

Before adding new code, the system must know what kind of organism it is.

A feature should not enter a codebase as a random function.

A feature should enter as a checked transition:

external request
→ field scan
→ edge proposal
→ Gate review
→ compiled edge
→ tests
→ memory atom

In this model:

codebase = cell / organism
module = organ
function = amino acid
edge = contact / transition route
workflow = folded protein / living behavior
Gate = membrane permission
operator = owner of the Gate
memory = immune history

A codebase becomes dangerous when it accepts new code without checking how that code folds into the existing field.

---

1. Why the Cell Comes Before the Blank

The Edge Proposal Form is important, but it must not exist alone.

First, define the cell.

Then define what the cell is allowed to accept.

No organism boundary
→ no safe intake

No intake form
→ no controlled growth

No Gate
→ foreign code enters as shadow

Therefore the correct order is:

1. Define the code organism.
2. Define the boards: 9V / 6V / 3V.
3. Define the membrane intake form.
4. Define the edge compiler.
5. Define tests.
6. Define memory after commit.

---

2. Three Boards of the Code Cell

9V = base board / law / roles / permissions / Gate
6V = edge board / service routes / nervous system
3V = signal board / UI / visible user actions

A signal must not jump directly from 3V into commit.

Correct route:

3V signal
→ 6V edge route
→ 9V Gate
→ Bindu verdict
→ memory update

---

3. Minimal Repository Structure

00_FLOWER_GATE_CORE/
  00_BOOT_CORE_SPEC_FLOWER_GATED_TRANSITIONS.md
  01_MISSING_EDGE_CODE_REPAIR_PLAN.md
  02_CODE_CELL_ORGANISM_AND_EDGE_PROPOSAL_FORM.md

code_cell/
  9v_base_board/
    roles.yaml
    gates.yaml
    permissions.yaml
    rollback_policy.yaml

  6v_edge_board/
    nodes.yaml
    edges.yaml
    required_routes.yaml

  3v_signal_board/
    ui_events.yaml
    api_signals.yaml
    status_messages.yaml

  functions/
    function_amino_acids.yaml

  memory/
    transition_logs.jsonl
    memory_atoms.yaml

  tests/
    edge_coverage.test.ts
    gate_validation.test.ts
    rollback_validation.test.ts

This structure makes the field visible before code is expanded.

---

4. Function as Amino Acid

A function is not only code.

A function must declare how it can connect to the organism.

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

Example:

const createAccountingEntry: FunctionAminoAcid = {
  name: "createAccountingEntry",

  accepts: [
    "paymentId",
    "orderId",
    "amount",
    "currency",
    "customerId"
  ],

  emits: [
    "accounting_entry_created"
  ],

  requiresGate: [
    "payment_confirmed",
    "accounting_policy_check"
  ],

  rollback: "voidAccountingEntry",
  memory: "accounting_transition_log",

  sideEffects: [
    "creates_financial_record",
    "updates_accounting_memory"
  ],

  owner: "accounting_operator",

  tests: [
    "test_create_accounting_entry_requires_payment_confirmed",
    "test_accounting_entry_can_rollback"
  ]
}

Canonical rule:

A function without declared contacts is not ready to enter the organism.

---

5. Edge as Contact

An edge is not only a connection.

An edge is a controlled contact between two rooms of the organism.

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

Canonical rule:

No explicit edge
→ no safe transition

---

6. Edge Proposal Form as Membrane Intake

The Edge Proposal Form is the membrane where a new transition asks permission to enter the code organism.

AI may create the proposal.

Human operator must approve the Gate.

Blank form:

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

---

7. Full Example: Missing Accounting Edge

Problem:

payment succeeds
order is created
customer receives success message

but accounting is not updated

This is a false-green feature.

The UI is GREEN, but the business field is incomplete.

AI creates this proposal:

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

---

8. Edge Compiler

The Edge Compiler checks whether the proposed contact can safely enter the organism.

It asks:

Does the from-node exist?
Does the to-node exist?
Does the trigger exist?
Does the action function accept the required payload?
Does the function emit the expected signal?
Is the Gate declared?
Is the Gate owner declared?
Is rollback declared?
Are tests declared?
Is memory declared?

Minimal TypeScript concept:

type EdgeCompileResult = {
  ok: boolean
  verdict: "EDGE_COMPILED" | "MISSING_CONTACT" | "GATE_MISSING" | "ROLLBACK_MISSING" | "OWNER_MISSING" | "TEST_MISSING"
  errors: string[]
}

export function compileEdgeProposal(
  edge: EdgeDefinition,
  fn: FunctionAminoAcid,
  knownNodes: string[]
): EdgeCompileResult {
  const errors: string[] = []

  if (!knownNodes.includes(edge.from)) errors.push(`Unknown from-node: ${edge.from}`)
  if (!knownNodes.includes(edge.to)) errors.push(`Unknown to-node: ${edge.to}`)

  if (edge.action !== fn.name) {
    errors.push(`Action function mismatch: edge uses ${edge.action}, function is ${fn.name}`)
  }

  if (!edge.gate) errors.push("Missing Gate")
  if (!edge.owner) errors.push("Missing owner")
  if (!edge.rollback) errors.push("Missing rollback")
  if (!edge.memory) errors.push("Missing memory")
  if (!edge.tests || edge.tests.length === 0) errors.push("Missing tests")

  const missingGate = fn.requiresGate.length > 0 && !edge.gate
  if (missingGate) errors.push("Function requires Gate but edge has none")

  if (errors.length > 0) {
    return {
      ok: false,
      verdict: errors.some(e => e.includes("Gate")) ? "GATE_MISSING" : "MISSING_CONTACT",
      errors
    }
  }

  return {
    ok: true,
    verdict: "EDGE_COMPILED",
    errors: []
  }
}

---

9. Safe Router Pattern

Once approved and compiled, the edge becomes part of the 6V board.

type Signal = {
  type: string
  payload: Record<string, unknown>
}

type RuntimeEdge = {
  id: string
  from: string
  to: string
  trigger: string
  gate: (signal: Signal) => Promise<boolean>
  action: (signal: Signal) => Promise<void>
  rollback?: (signal: Signal) => Promise<void>
}

export async function routeSignal(signal: Signal, edges: RuntimeEdge[]) {
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

Payment code becomes a signal emitter, not the owner of the entire company flow:

async function handlePaymentSuccess(payment: any) {
  await routeSignal(
    {
      type: "payment_success",
      payload: {
        paymentId: payment.id,
        orderId: payment.orderId,
        amount: payment.amount,
        currency: payment.currency,
        customerId: payment.customerId
      }
    },
    paymentEdges
  )
}

The button does not decide the whole company.

The edge board routes the signal through the organism.

---

10. Contact Coverage Test

A codebase needs contact coverage, not only unit coverage.

Unit test asks:

Does this function work?

Contact coverage asks:

Did this signal reach all required rooms?

Example:

describe("payment_success edge coverage", () => {
  it("routes payment success to all required business rooms", async () => {
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

If a required room is missing, the feature remains HOLD.

---

11. Memory Atom After Approval

After the operator approves the edge and tests pass, record memory.

memory_atom:
  id: payment_success_to_accounting_edge_001
  transition: payment_success

  problem:
    missing_edge: payment_success_to_accounting
    shadow: false_green_payment_without_financial_memory

  repair:
    - added edge proposal
    - approved by accounting_operator
    - added route to accounting
    - added contact coverage test
    - added rollback voidAccountingEntry

  new_rule:
    payment_success cannot be considered GREEN unless accounting receives financial memory

  verdict: REPAIR_COMMITTED

---

12. Human Gate Rule

AI may help the cell fold.

AI must not own the fold.

ai_allowed:
  - scan_code
  - detect_missing_edges
  - draft_edge_proposal
  - draft_function_amino_acid
  - draft_tests
  - prepare_transition_packet

ai_blocked:
  - approve_own_edge
  - bypass_operator
  - auto_merge_business_route
  - deploy_without_gate

The operator is the membrane owner.

The AI is the folding assistant.

---

13. Final Principle

A feature enters the organism through an edge proposal.

A function connects as an amino acid.

The edge compiler checks the contact.

The operator approves the Gate.

The router conducts the signal.

The test verifies contact coverage.

The memory atom records what changed.

Canonical line:

No form
→ no safe intake

No edge proposal
→ no new route

No Gate owner
→ no commit

No rollback
→ no safe transition

No memory
→ repeated shadow

A codebase becomes alive when it can accept new transitions without losing its field.
