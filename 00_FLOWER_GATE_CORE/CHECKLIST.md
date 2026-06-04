Flower Gate Core Checklist

Use this checklist before allowing any important transition.

A transition may be:

code commit
business decision
document approval
AI tool call
deployment
customer feature
operator handoff
company workflow change

---

1. State Check

[ ] What is the current state?
[ ] What pressure is forcing movement?
[ ] What wants to change?
[ ] Is the request clear?
[ ] Is this FACT, MODEL, or HOLD?

Verdict:

FACT  = confirmed
MODEL = inferred
HOLD  = cannot move yet

---

2. 3V Signal Check

3V = visible request / UI / local signal.

[ ] Is the visible request present?
[ ] What does the user/customer/operator see?
[ ] What event is being produced?
[ ] Is this only a local green?

Warning:

No customer code from 3V alone.

---

3. 6V Route Check

6V = route / process / document edge / nervous system.

[ ] Which operators are affected?
[ ] Which nodes must receive the signal?
[ ] Which document connects them?
[ ] Which edges are confirmed?
[ ] Which edges are missing?
[ ] Is there contact coverage?

Warning:

No true-green without 6V route.

---

4. 9V Gate Check

9V = permission / authority / owner / policy / Gate.

[ ] Who owns the Gate?
[ ] Is the owner known?
[ ] Is approval required?
[ ] Is the approval fresh?
[ ] Is the document authoritative?
[ ] Is the operator scope clear?
[ ] Is Human Gate required?

Warning:

No commit without 9V Gate.

---

5. Color Verdict Check

[ ] What is the visible color?
[ ] What is the suspected true state?
[ ] Is there false-green risk?
[ ] What evidence supports the color?
[ ] Was 3V checked?
[ ] Was 6V checked?
[ ] Was 9V checked?

Rule:

No color verdict without evidence.
No GREEN without 6V and 9V check.
No commit from inferred GREEN.

---

6. Document Edge Check

[ ] Which document is required?
[ ] Does the document exist?
[ ] Is the document fresh?
[ ] Does the document have authority?
[ ] Does the document belong to correct operator scope?
[ ] Does the document connect the correct operators?
[ ] Can this document open Gate?

Rules:

No document → no visible edge.
No visible edge → HOLD.
Draft document ≠ approval.
Stale document ≠ Gate.

---

7. Shadow Check

[ ] What is hidden in this transition?
[ ] What can break after visible success?
[ ] What old incident may return?
[ ] What operator was not included?
[ ] What document was skipped?
[ ] What rollback is missing?
[ ] What memory is missing?

Warning:

Green can be false-green.

---

8. Rollback Check

[ ] Is this transition reversible?
[ ] Is rollback documented?
[ ] Who owns rollback?
[ ] Was rollback tested?
[ ] What happens if the transition fails?

Rule:

No risky transition without rollback.

---

9. AI Gate Check

AI must ask:

[ ] Am I allowed to answer directly?
[ ] Am I only allowed to draft?
[ ] Is this action irreversible?
[ ] Does this touch business, money, safety, legal, identity, people, production, or memory?
[ ] Is Human Gate required?

Allowed AI outputs:

ANSWER
DRAFT
HOLD
REPAIR
BLOCK
ASK
HUMAN_GATE_REQUIRED

AI must not:

[ ] silently commit
[ ] invent approval
[ ] bypass operator Gate
[ ] treat local green as truth
[ ] deploy from inferred state
[ ] read outside operator scope

---

10. Bindu Decision

Only after the field is visible:

[ ] 3V checked
[ ] 6V checked
[ ] 9V checked
[ ] color checked
[ ] document edges checked
[ ] Gate owner known
[ ] rollback checked
[ ] memory plan exists

Allowed Bindu decisions:

COMMIT
HOLD
REPAIR
BLOCK
ASK

---

11. Memory Atom Check

[ ] What happened?
[ ] What was the visible color?
[ ] Was there false-green risk?
[ ] Which edges were missing?
[ ] Which Gate decided?
[ ] What was the final verdict?
[ ] What should future AI remember?

Rule:

No important transition without memory atom.

---

Minimal Verdict Packet

flower_gate_verdict:
  target: example_transition

  three_v_signal:
    status: PRESENT

  six_v_route:
    status: INCOMPLETE
    missing_edges: []

  nine_v_gate:
    status: INCOMPLETE
    missing_gates: []

  color_verdict:
    visible_color: GREEN
    suspected_true_state: YELLOW_BLUE_INCOMPLETE
    false_green_risk: true

  document_edges:
    missing: []
    stale: []
    draft_only: []

  rollback:
    status: MISSING

  memory:
    required: true
    recorded: false

  verdict: HOLD

  required_action:
    - create_edge_proposal_form
    - request_operator_gate
    - add_contact_coverage_test
    - define_rollback
    - record_memory_atom

---

Final Rule

If edge is missing → HOLD.
If Gate is missing → HOLD.
If rollback is missing for risky action → HOLD.
If memory is missing for important transition → HOLD.
If GREEN is not checked through 6V and 9V → HOLD.
If AI is about to act without Human Gate → BLOCK or HUMAN_GATE_REQUIRED.
