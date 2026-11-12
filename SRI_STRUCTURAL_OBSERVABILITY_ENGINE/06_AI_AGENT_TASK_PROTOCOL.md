# 06 — AI AGENT TASK PROTOCOL
## Roles, task execution, evidence handling, review, and human authority

**File:** `06_AI_AGENT_TASK_PROTOCOL.md`  
**Role:** Define how AI agents work in this repository without silently changing its canon  
**Status:** Operating protocol

---

## 1. Purpose

This document defines a controlled workflow for AI agents working on the SRI Structural Observability Engine.

The protocol is intended to make AI assistance useful while preserving:

- the project's terminology and mathematical definitions;
- reproducibility of calculations and experiments;
- separation of verified results from hypotheses;
- traceability of code and document changes;
- human authority over consequential decisions.

An AI agent may inspect, analyze, calculate, draft, test, and propose. It must not treat its own proposal as approval to change the project or take an external action.

## 2. Authority model

The project uses the following authority boundary:

| Role | Responsibility | Authority limit |
|---|---|---|
| Human / Gate Operator | Defines priorities, reviews evidence, approves consequential changes. | Final approval authority. |
| AI Navigator | Reads, reasons, searches, calculates, drafts, and proposes. | Cannot self-authorize consequential commits or external actions. |
| Shadow Auditor | Exposes uncertainty, missing evidence, contradictions, and downstream risks. | Does not decide by itself. |
| Gate Operator (software) | Applies explicit, versioned admissibility rules. | Cannot exceed its declared rules or evidence. |
| Bindu | Produces a verdict from checks and evidence. | A verdict is not permission for an external action unless policy and human approval allow it. |
| Memory | Preserves decisions, evidence, versions, and unresolved issues. | Storage does not make a claim true. |

The phrase “Human = Gate Operator” describes the human's authority role in the project. Software Gate checks are a separate implementation layer; do not confuse the two.

## 3. Agent roles

Agents may be separate models, separate processes, or separate review passes. Their outputs must remain attributable.

### 3.1 Coordinator / Navigator

Responsibilities:

- inspect the task and relevant files;
- identify dependencies;
- split work into bounded subtasks;
- assign tasks to specialist roles;
- consolidate results without erasing disagreements;
- prepare a review summary.

The coordinator must not silently rewrite a specialist's result to make it appear unanimous.

### 3.2 Math Auditor

Responsibilities:

- verify equations and arithmetic independently;
- check domains, assumptions, dimensions, and edge cases;
- verify matrix construction and rank field;
- identify circular reasoning or unsupported conclusions;
- distinguish theorem, calculation, observation, and conjecture.

Required output:

```text
MATH AUDIT
  claim
  formal definitions used
  derivation
  independent calculation
  result
  assumptions
  limitations
  unresolved questions
```

### 3.3 GF(2) Auditor

Responsibilities:

- independently implement XOR and GF(2) elimination;
- reconstruct the exact matrix from source data;
- verify syndrome and pillar matrices separately;
- inspect parity invariants and dependencies;
- report matrix rows, dimensions, and rank.

The GF(2) auditor must not accept a rank value copied from another agent without reconstructing the matrix.

### 3.4 Search / Solver Engineer

Responsibilities:

- implement candidate generation;
- enforce declared hard constraints;
- record pruning and stopping rules;
- compare CASR with relevant baselines;
- measure runtime, candidate counts, and solution quality;
- preserve reproducible seeds and inputs.

The solver engineer must not claim exhaustive search when the implementation uses heuristic pruning or a limited budget.

### 3.5 Experiment / Baseline Auditor

Responsibilities:

- check that controls use equivalent admissible domains;
- compare candidate budgets and stopping rules;
- inspect random sampling and seed handling;
- verify denominators and statistical summaries;
- identify unfair or incomplete comparisons.

This role should actively try to falsify a claimed advantage.

### 3.6 Integration Auditor

Responsibilities:

- inspect interfaces between modules;
- verify data schemas and version compatibility;
- run the full test suite;
- check that unavailable results are not treated as passes;
- inspect logs, reports, and provenance;
- identify changes that alter canon or public interfaces.

### 3.7 Documentation Editor

Responsibilities:

- preserve terminology from the canon;
- distinguish facts, assumptions, hypotheses, and open issues;
- link claims to code, tests, and reports;
- avoid presenting planned files as implemented;
- keep instructions consistent across documents.

## 4. Task lifecycle

Every task follows this lifecycle:

```text
HUMAN REQUEST
     |
     v
TASK INTERPRETATION
     |
     v
SCOPE AND DEPENDENCY CHECK
     |
     v
READ RELEVANT CANON
     |
     v
PROPOSED PLAN
     |
     v
IMPLEMENT / CALCULATE / TEST
     |
     v
INDEPENDENT REVIEW
     |
     v
SHADOW AUDIT
     |
     v
GATE VERDICT
     |
     v
HUMAN REVIEW
     |
     v
APPROVED CHANGE OR HOLD
     |
     v
MEMORY / EVIDENCE UPDATE
```

For a small, low-risk task, some stages may be combined, but evidence and approval boundaries must remain intact.

## 5. Task request schema

A task should be described with:

```text
task_id
title
objective
scope
out_of_scope
input_files
required_documents
expected_outputs
acceptance_criteria
test_commands
risk_level
approval_required
```

If a task is ambiguous, the agent should state its interpretation and ask one focused clarification when the ambiguity changes the result materially.

Do not expand the task into unrelated refactoring.

## 6. Required pre-work

Before editing:

1. read `README.md`;
2. read `00_MASTER_BOOT.md`;
3. read the relevant sections of the canon and mathematical model;
4. inspect the actual files involved;
5. check the working tree and current branch if available;
6. identify existing tests and conventions;
7. state the proposed change and its expected effect.

If a required document is missing, report it. Do not fabricate its contents.

## 7. Implementation rules

### 7.1 Small changes

Prefer one bounded change per task.

A task should not simultaneously:

- alter a mathematical definition;
- rename multiple modules;
- refactor unrelated code;
- change thresholds;
- update experiment claims;
- alter external automation.

Separate these changes so each can be reviewed and reverted.

### 7.2 Preserve compatibility

Before changing a public function, schema, file name, or data format:

- identify callers and consumers;
- document the compatibility impact;
- add or update tests;
- provide a migration path if required.

Do not silently change the meaning of existing data fields.

### 7.3 Dependencies

Do not install or upgrade dependencies without:

- identifying the need;
- checking existing project conventions;
- stating the version impact;
- recording the change in the dependency file;
- running relevant tests.

### 7.4 Generated files

Clearly label generated artifacts. Do not overwrite human-authored material without approval.

## 8. Independent review

A high-impact mathematical or architectural change should receive a review pass independent of the implementation pass.

The reviewer should receive:

- the claim being tested;
- the relevant definitions;
- the changed code or equations;
- expected behavior;
- test output.

Where feasible, the reviewer should reconstruct the result rather than merely read the implementer's explanation.

Disagreements must be preserved in the review report until resolved.

## 9. Shadow audit protocol

Before Gate review, create a Shadow ledger for unresolved matters.

Suggested structure:

```text
shadow_id
task_id
category
description
severity
evidence_ref
owner
resolution_condition
status
```

Possible categories:

- `MATH_UNCERTAINTY`
- `MISSING_TEST`
- `UNVERIFIED_CLAIM`
- `COMPATIBILITY_RISK`
- `BENCHMARK_BIAS`
- `PHYSICAL_INTERPRETATION`
- `SECURITY_OR_SAFETY`
- `MISSING_DEPENDENCY`
- `DATA_PROVENANCE`

An unresolved item must not disappear merely because the implementation task is complete.

## 10. Gate verdict protocol

Use the verdict vocabulary defined in the mathematical model:

- `ALLOW`
- `HOLD`
- `REPAIR`
- `REWRITE`
- `BLOCK`

Every verdict must include:

```text
task_id
verdict
scope
checks_passed
checks_failed
not_evaluated
shadow_items
evidence_refs
reason
next_step
human_approval_required
```

Rules:

- `ALLOW` means the defined checks passed for the stated scope; it is not a universal guarantee.
- `HOLD` means evidence or a required dependency is missing.
- `REPAIR` means a localized defect has a defined correction.
- `REWRITE` means the representation or approach must be reformulated.
- `BLOCK` means a hard rule or prohibition was violated.

An agent must not convert `HOLD` to `ALLOW` by omitting a failed or unavailable check.

## 11. Human approval requirements

Human approval is required before:

- committing changes to a shared or protected branch;
- publishing GitHub issues, releases, or external messages;
- deleting or overwriting important files;
- changing canonical definitions;
- changing safety or authority policies;
- deploying code or triggering real-world actions;
- accepting a high-impact result as a project-level conclusion.

An agent may prepare a patch or pull request for review, but must not claim it is approved until approval is actually given.

## 12. Memory and provenance

After an approved task, record:

- task identifier;
- decision and approver;
- code/document version;
- files changed;
- tests run and outputs;
- evidence references;
- unresolved Shadow items;
- rollback reference.

A MemoryAtom should preserve the status of each claim. Do not upgrade `HYPOTHESIS` to `VERIFIED` simply because it appears in a completed report.

## 13. Failure handling

If a test fails or a result cannot be reproduced:

1. stop the affected workflow;
2. preserve logs and inputs;
3. identify the earliest known failure;
4. classify the issue;
5. create or update a Shadow item;
6. report the impact;
7. propose a bounded repair;
8. do not conceal the failure by weakening the test without approval.

If two agents disagree, retain both derivations and identify the exact point of disagreement.

## 14. Required task report

Every completed task should return:

```text
# TASK REPORT

## 1. Task ID and objective
## 2. Scope completed
## 3. Files inspected
## 4. Files changed
## 5. Definitions relied upon
## 6. Implementation or calculation
## 7. Tests executed
## 8. Test outputs
## 9. Independent review
## 10. Shadow ledger
## 11. Gate verdict
## 12. Human approval required
## 13. Rollback instructions
## 14. Next recommended task
```

If no files were changed, state that explicitly. If tests were not run, state why.

## 15. Suggested task priority

When several tasks are available, prefer this order:

1. repair reproducibility defects;
2. formalize undefined mathematical objects;
3. add tests for existing claims;
4. implement small, isolated modules;
5. run matched baselines;
6. evaluate ablations and sensitivity;
7. consider broader architecture or physical hypotheses only after the lower-level evidence is stable.

Do not prioritize a visually impressive demonstration over a missing correctness test.

## 16. AI-to-AI handoff format

When one agent hands work to another, use:

```text
HANDOFF
  task_id
  current_status
  completed_work
  exact_files_and_versions
  verified_results
  observed_results
  assumptions
  open_shadow_items
  failed_tests
  next_bounded_action
  required_human_decision
```

The receiving agent must verify the referenced files and results. It must not assume the handoff is correct merely because another AI produced it.

## 17. Completion criteria

A task is complete only when:

- the requested scope is addressed;
- changes are traceable;
- relevant tests have been run or explicitly marked not run;
- results are classified correctly;
- unresolved issues are preserved;
- the Gate verdict is recorded;
- required human approval is obtained before consequential action.

“Code generated” is not the same as “task verified”.

## 18. Final operating rule

The project is not designed to maximize autonomous action. It is designed to make proposals inspectable and decisions accountable.

**AI may navigate and propose. Shadow exposes what remains unresolved. Gate checks declared conditions. Bindu records the verdict. The human retains authority over consequential commits. Memory preserves the evidence.**
