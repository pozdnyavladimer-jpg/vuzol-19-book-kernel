04 — Operator Repo Document-as-Edge Protocol

Purpose

This file defines how a real company becomes a Flower Field through operator repositories and documents.

In GitCube OS, a document is not only a file.

A document is an edge between operators.

A document carries state from one operator to another.

A document can open, close, block, or repair a transition.

The AI does not own the decision.

The AI reads operator repositories, detects missing edges, checks color verdicts, and shows which document must connect which operators.

The human operator owns the Gate.

---

Folder Logic

Inside "00_FLOWER_GATE_CORE", this file continues the previous core documents:

00 = law of transition
01 = missing edge / misfolded code / false-green
02 = edge proposal form / code as cell
03 = human as color operator / truth-check of state
04 = operator repos / documents as edges / company as Flower Field

This file answers four questions:

Where does the operator live?
Where is the operator state stored?
How does a document become an edge?
How does AI know which operators must be connected?

---

Core Rule

In GitCube OS, a document is not paper.

A document is an edge between operators of the field.

A business transition cannot safely continue only because a document exists.

The system must check:

document exists
document is fresh
document has authority
document belongs to the correct operator scope
document connects the correct operators
document closes or supports the required Gate
memory will be recorded after the transition

If any of these are missing, the verdict must be HOLD.

---

Company as Flower Field

A company is not only a hierarchy.

A company is a field of operators, documents, Gates, colors, octaves, and transitions.

company = field
operator = node / room / organ / color holder
document = edge
process = route
policy = Gate
decision = Bindu
incident = shadow
record = memory
AI = scanner / navigator
GitCube OS = transition router

The company fails when it treats a local green as global truth.

The system is safer when every business transition is routed through visible operator repos and document edges.

---

Operator Repo

Each operator keeps a repository of current project documents.

An operator repo is not the private soul of a human.

An operator repo is a working node of a role.

The operator repo contains only the documents, states, Gates, and memory traces needed for that role.

Minimal structure:

operator_repo/
  README_OPERATOR.md
  OPERATOR_STATE.yaml

  CURRENT_DOCUMENTS/
    client_request.md
    invoice.md
    tech_spec.md
    contract.md
    payment_confirmation.md
    release_note.md

  EDGES/
    edge_proposals.yaml
    approved_edges.yaml
    blocked_edges.yaml
    missing_edges.yaml

  GATES/
    gate_status.yaml
    gate_owners.yaml
    approval_log.md

  MEMORY_ATOMS/
    memory_atoms.jsonl

  BINDU_LOG.md

The repo does not exist to control the person.

The repo exists to make the role visible inside the project field.

---

Operator State

Each operator repo must expose a minimal machine-readable state.

Example:

operator_state:
  operator_id: finance_operator
  project_id: card_payment_feature

  role: finance
  current_color: BLUE
  current_octave: 5

  owns:
    - invoice
    - payment_confirmation
    - refund_rule
    - accounting_memory

  current_documents:
    - CURRENT_DOCUMENTS/invoice.md
    - CURRENT_DOCUMENTS/payment_terms_confirmation.md

  gates:
    - finance_approval
    - refund_policy_check
    - accounting_record_check

  open_edges:
    - from: sales_operator
      document: commercial_offer.md
      status: received

    - to: dev_operator
      document: payment_requirements.md
      status: missing

  verdict: HOLD

This allows AI to read the role without pretending to read the human.

---

Document as Edge

A document is an edge when it connects operators and allows state to move.

Examples:

contract → allows payment route
technical specification → allows development route
invoice → allows finance route
act of completion → allows project closure
security approval → allows deploy route
payment confirmation → allows accounting route
refund policy → allows rollback route
audit note → allows memory route

A document can be:

required
missing
draft
stale
approved
blocked
superseded
out_of_scope
memory_only

The AI must never treat a found file as an automatically valid edge.

A document must be checked for freshness, authority, scope, and Gate relevance.

---

Document Freshness

A document can exist but no longer hold the real state.

Example:

document_status:
  document: payment_terms_confirmation.md
  exists: true
  fresh: false
  reason: "Contract was updated after this document was created."
  verdict: HOLD

Rule:

A stale document cannot open Gate.

A stale document can only trigger repair, update, or review.

This protects the company from false-green.

A file exists, but the field has moved.

---

Document Authority

Not every document has the authority to open a Gate.

A draft is not approval.

A note is not a policy.

An AI summary is not an operator decision.

Example:

document_authority:
  document: payment_terms_confirmation.md
  owner: finance_operator
  approved_by: []
  authority_level: draft
  can_open_gate: false
  verdict: HOLD

Authority levels:

draft
operator_note
proposal
reviewed
approved
canonical
superseded
blocked

Rule:

No Gate from draft authority.

No commit from unapproved authority.

No transition from AI-generated authority without Human Gate.

---

Operator Scope

Operator scope protects the system from turning repos into surveillance or uncontrolled access.

An operator repo is role-bound.

Example:

operator_scope:
  operator: finance_operator

  reads:
    - finance_documents
    - payment_terms
    - invoice_status
    - refund_policy

  cannot_read:
    - private_hr_notes
    - unrelated_client_data
    - personal_messages
    - secret_keys

  can_approve:
    - payment_terms_confirmation
    - invoice_release
    - refund_rule

  cannot_approve:
    - legal_contract_final
    - production_deploy
    - security_policy_final

Rule:

Operator repo = role visibility.

Operator repo ≠ total control of a person.

Operator scope must be explicit.

If scope is unclear, AI must return HOLD.

---

Document Edge Verdict

AI must output a machine-readable verdict when a document is needed as an edge.

Example:

document_edge_verdict:
  edge: sales_operator_to_finance_operator
  project: card_payment_feature

  document: payment_terms_confirmation.md
  status: MISSING

  color: YELLOW_BLUE_INCOMPLETE
  false_green_risk: true

  from_operator: sales_operator
  to_operator: finance_operator

  required_operator: finance_operator
  required_gate: finance_payment_terms_gate

  reason: "Customer request reached development, but finance operator has no confirmed payment terms document."

  verdict: HOLD

  required_action:
    - create_document_edge
    - request_finance_operator_gate
    - update_6v_route
    - record_memory_atom

A document edge verdict must show:

edge
document
status
from_operator
to_operator
required_operator
required_gate
color
false_green_risk
verdict
required_action

No hidden routing.

No invisible Gate.

No commit from missing document edge.

---

AI Role

AI does not decide for operators.

AI reads the field and shows the missing transition.

The correct AI response:

I found a possible transition.

The required document edge is missing.

The transition touches finance_operator.

The visible color looks GREEN, but the deeper state is YELLOW_BLUE_INCOMPLETE.

Verdict: HOLD.

Required action:
create payment_terms_confirmation.md,
request finance Gate,
update route,
record memory atom.

The incorrect AI response:

I created the payment feature and everything is done.

AI must not:

invent approval
bypass operator Gate
treat stale documents as fresh
treat draft documents as canonical
read outside operator scope
commit from inferred green

---

GitCube OS Role

GitCube OS does not manage people.

GitCube OS manages gated transitions between operator repositories.

GitCube OS reads:

operator states
current documents
document edges
Gate status
color verdicts
octave level
memory atoms
Bindu log

GitCube OS routes:

missing document → required operator
missing Gate → Gate owner
false-green → HOLD
stale document → repair
unapproved document → review
approved edge → next route
closed Gate → Bindu

GitCube OS is the transition router.

Human operators are the Gates.

AI is the scanner and draft generator.

Memory atoms are the nervous trace.

---

3V / 6V / 9V Mapping

A customer request usually arrives as 3V.

3V = visible request / UI / task / local signal
6V = route / process / operator connection / document edge
9V = permission / owner / Gate / policy / authority

A document edge must be checked across all three layers.

Example:

document_edge_layers:
  target: payment_success_to_accounting

  3v_signal:
    status: present
    evidence:
      - customer_requested_card_payment
      - ui_payment_success_message

  6v_route:
    status: incomplete
    missing_edges:
      - payment_success_to_accounting_document
      - payment_success_to_audit_memory

  9v_gate:
    status: incomplete
    missing:
      - finance_operator_approval
      - audit_memory_rule

  verdict: HOLD

Rule:

No document edge is complete until 3V, 6V, and 9V are checked.

---

Business Example: Card Payment Feature

Customer request:

Add card payment to the website.

False simple interpretation:

Create payment button.
Connect payment provider.
Show success message.
Done.

Flower Field interpretation:

3V:
  customer sees payment button
  customer receives success message

6V:
  payment connects to order
  payment connects to finance
  payment connects to warehouse
  payment connects to refund
  payment connects to audit
  payment connects to support

9V:
  finance approves accounting route
  legal approves payment terms
  security approves provider integration
  audit approves memory rule
  owner approves release

Document-as-edge verdict:

document_edge_verdict:
  project: card_payment_feature

  edge: dev_operator_to_finance_operator
  document: payment_success_accounting_event.md
  status: MISSING

  visible_color: GREEN
  suspected_true_state: YELLOW_BLUE_INCOMPLETE
  false_green_risk: true

  reason:
    - "UI can show payment success."
    - "Payment provider can return success event."
    - "Accounting document edge is missing."
    - "Audit memory rule is missing."

  required_operator: finance_operator

  verdict: HOLD

  required_action:
    - create payment_success_accounting_event.md
    - request finance_operator Gate
    - add contact coverage test
    - define refund rollback
    - record memory atom

The code must wait until the business edge is visible.

---

Document Edge States

MISSING:
  The required document does not exist.

DRAFT:
  The document exists but has no authority.

STALE:
  The document exists but no longer matches the current field.

OUT_OF_SCOPE:
  The document belongs to the wrong operator or cannot be used for this Gate.

APPROVED:
  The document has operator authority.

BLOCKED:
  The operator rejected the transition.

MEMORY_ONLY:
  The document records history but cannot open Gate.

CAN_OPEN_GATE:
  The document is fresh, scoped, authoritative, and connected to the required operator.

---

Decision Rules

No document → no visible edge.

No visible edge → HOLD.

No fresh document → HOLD.

No authority → HOLD.

No operator scope → HOLD.

No Gate owner → HOLD.

No rollback → HOLD for risky transitions.

No memory atom → repeated shadow.

No 6V route → no true-green.

No 9V Gate → no commit.

No Human Gate → AI must not execute.

---

Memory Atom Requirement

Every important document edge transition must leave memory.

Example:

{
  "memory_atom_id": "mem_payment_edge_001",
  "project": "card_payment_feature",
  "transition": "dev_operator_to_finance_operator",
  "document_edge": "payment_success_accounting_event.md",
  "previous_verdict": "HOLD",
  "final_verdict": "APPROVED",
  "gate_owner": "finance_operator",
  "reason": "Accounting route confirmed and audit memory rule added.",
  "timestamp": "YYYY-MM-DDTHH:MM:SSZ"
}

Memory prevents the same shadow from returning as a new problem.

---

Minimal Operator Repo Packet

Each operator repo should expose a packet like this:

operator_repo_packet:
  operator_id: finance_operator
  project_id: card_payment_feature

  current_color: BLUE
  current_octave: 5

  scope:
    can_read:
      - finance_documents
      - payment_terms
    can_approve:
      - invoice_release
      - payment_terms_confirmation
    cannot_approve:
      - legal_contract_final
      - production_deploy

  documents:
    - path: CURRENT_DOCUMENTS/payment_terms_confirmation.md
      status: DRAFT
      fresh: true
      authority_level: proposal
      can_open_gate: false

    - path: CURRENT_DOCUMENTS/invoice.md
      status: APPROVED
      fresh: true
      authority_level: approved
      can_open_gate: true

  gates:
    - name: finance_payment_terms_gate
      status: open
      owner: finance_operator

  edges:
    missing:
      - payment_success_to_accounting
    approved:
      - client_offer_to_invoice

  verdict: HOLD

This allows AI and GitCube OS to scan the field without guessing.

---

Canonical Formula

operator repo
→ current documents
→ document edges
→ color verdict
→ octave level
→ missing edge scan
→ required operator
→ Gate
→ Bindu
→ memory atom

---

Canonical Rule

Document is not paper.

Document is an edge.

An edge connects operators.

An operator holds Gate.

AI shows the missing edge.

Human gives Bindu.

Memory records the transition.

---

Short Form

Every operator keeps a repo of current project documents.

The AI reads those documents as edges in the company field.

If a required document is missing, stale, unauthorized, or outside scope, the transition becomes HOLD.

AI does not decide for the operator.

AI shows:

which document is missing
which edge is incomplete
which operator owns the Gate
which color is false-green
which action is required next

The human operator closes the Gate.

GitCube OS routes the transition.

Memory atom records the result.

---

Final Sentence

A company becomes safer when documents stop being passive files and start becoming visible edges between responsible operators.
