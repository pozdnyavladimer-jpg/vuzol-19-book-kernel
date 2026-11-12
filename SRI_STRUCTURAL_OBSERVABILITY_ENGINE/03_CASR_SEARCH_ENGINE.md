# 03 — CASR SEARCH ENGINE
## Candidate generation, constraint filtering, scoring, and reproducible search

**File:** `03_CASR_SEARCH_ENGINE.md`  
**Role:** Specify the computational search layer  
**Status:** Architecture specification; algorithmic details marked `OPEN` where not yet fixed

---

## 1. Purpose

The CASR component is the search layer of the SRI Structural Observability Engine.

Its responsibility is to:

1. receive a formally defined problem and source state;
2. generate candidate states or transitions;
3. apply hard constraints;
4. run forward and reverse checks;
5. record unresolved issues in Shadow;
6. calculate documented metrics;
7. return candidates with evidence and an explicit status.

CASR must not silently accept a candidate because it has a high score. Hard constraints and required audits take precedence over optimization.

The acronym `CASR` is retained as the project name. Its exact expansion and any claim that it denotes a unique established algorithm remain `OPEN` until explicitly defined by the project.

## 2. Inputs and outputs

### 2.1 Search request

A search request should be represented as structured data:

```text
SearchRequest
  request_id
  source_state
  state_schema
  variable_domains
  hard_constraints
  soft_objectives
  forward_operator
  reverse_audit
  candidate_budget
  time_budget
  random_seed
  model_version
  evidence_refs
```

Fields that are not applicable may be null, but their absence must be explicit. Do not silently invent default constraints or objectives.

### 2.2 Candidate record

Each candidate should carry:

```text
Candidate
  candidate_id
  source_state_ref
  state
  generation_method
  generation_parameters
  hard_constraint_results
  forward_audit
  reverse_audit
  shadow_items
  metric_values
  gate_verdict
  evidence_refs
```

A candidate must retain enough provenance to reproduce how it was generated.

### 2.3 Search result

The search result should report:

```text
SearchResult
  request_id
  status
  candidates_generated
  candidates_evaluated
  candidates_rejected
  candidates_held
  candidates_accepted
  rejection_counts_by_rule
  elapsed_time
  random_seed
  stopping_reason
  candidate_records
```

Use counts and denominators, not percentages alone.

## 3. Search pipeline

The intended pipeline is:

```text
SEARCH REQUEST
     |
     v
VALIDATE REQUEST SCHEMA
     |
     v
GENERATE CANDIDATES (+3 / proposal operator)
     |
     v
DEDUPLICATE (only if identity rules permit)
     |
     v
HARD CONSTRAINT FILTER
     |
     v
FORWARD METRICS
     |
     v
REVERSE / ROLLBACK AUDIT (-3)
     |
     v
SHADOW RECORD
     |
     v
CONSEQUENCE AUDIT (9V, when formally defined)
     |
     v
GATE
     |
     v
RANK / GROUP / REPORT
     |
     v
MEMORY RECORD
```

The order is a proposed execution design. If the implementation changes the order, it must document why and demonstrate that the change does not bypass required checks.

## 4. Candidate generation

Candidate generation is delegated to a domain-specific proposal operator:

\[
F_{+3}(s,\theta)\rightarrow\{c_1,c_2,\ldots,c_k\}
\]

where:

- \(s\) is the source state;
- \(\theta\) contains explicit generation parameters;
- \(c_i\) is a candidate;
- \(k\) may be zero or more.

The operator must document:

- how candidates are generated;
- whether generation is deterministic;
- how duplicates are handled;
- whether the search is exhaustive or heuristic;
- what candidate budget applies;
- what states may be omitted by pruning.

Do not claim completeness for a heuristic generator.

### 4.1 Search modes

Implementations should identify the mode they use:

| Mode | Meaning |
|---|---|
| `EXHAUSTIVE` | Every state in the explicitly defined finite admissible search domain is enumerated. |
| `BOUNDED` | Enumeration stops at a stated candidate or time budget. |
| `HEURISTIC` | A heuristic proposes a subset; completeness is not guaranteed. |
| `STOCHASTIC` | Candidates are sampled using a specified random process. |
| `HYBRID` | A documented combination of the above. |

A search mode must be included in every report.

## 5. Hard constraints and early rejection

Let the hard constraints be \(g_1,\ldots,g_m\).

A candidate \(c\) is admissible only if:

\[
g_j(c)=\text{true}\quad\forall j\in\{1,\ldots,m\}
\]

The implementation may evaluate inexpensive constraints before expensive ones, but it must record which checks were skipped because an earlier hard constraint failed.

Suggested rejection record:

```text
candidate_id
rule_id
rule_version
result = FAIL
observed_value
expected_condition
evidence_ref
```

A candidate that fails a hard constraint must not re-enter the accepted set through a high soft score.

## 6. Forward metrics and scoring

Metrics are calculated only after their definitions are fixed.

For a candidate \(c\), a metric may be represented as:

\[
m_i(c)\in\mathbb{R}
\]

A multi-objective search should preserve the metric vector:

\[
\mathbf{m}(c)=(m_1(c),m_2(c),\ldots,m_r(c))
\]

Do not collapse the vector into one scalar unless the objective and weights are documented.

### 6.1 Optional weighted score

If a scalar score is justified, define:

\[
J(c)=\sum_{i=1}^{r}w_i\widetilde{m_i(c)}
\]

where:

- \(w_i\) is an explicit weight;
- \(\widetilde{m_i}\) is a documented normalized metric;
- the direction of preference is known.

The report must include the original metric values, not only \(J(c)\).

A weighted score is not a substitute for hard constraints, uncertainty reporting, or Gate checks.

### 6.2 Pareto comparison

When objectives conflict, a Pareto frontier may be more appropriate than a single weighted score.

Candidate \(a\) dominates candidate \(b\) for minimization objectives if:

\[
m_i(a)\leq m_i(b)\quad\forall i
\]

and:

\[
m_j(a)<m_j(b)\quad\text{for at least one }j
\]

The objective directions and units must be made consistent before applying this rule.

## 7. Reverse audit (−3)

The reverse audit checks whether a proposed transition remains consistent with its source, constraints, and declared rollback requirements.

It may test:

- source-to-candidate differences;
- invariant preservation;
- reversibility, where required;
- rollback feasibility;
- dependency consistency;
- resource or state changes that cannot be undone.

The reverse audit must return structured results:

```text
audit_id
candidate_id
checks
passed
failed
not_evaluated
rollback_available
unresolved_items
evidence_refs
```

Do not assume that every proposal is reversible. If reversibility is not required for a task, state that explicitly.

## 8. Shadow generation

Shadow collects unresolved or potentially consequential information.

Possible item types include:

- `MISSING_EVIDENCE`
- `UNKNOWN_DEPENDENCY`
- `CONSTRAINT_CONFLICT`
- `UNCERTAINTY`
- `DRIFT`
- `ROLLBACK_RISK`
- `DOWNSTREAM_EFFECT`
- `MODEL_LIMITATION`

Each item should be linked to the candidate and the check that produced it.

Do not add arbitrary Shadow penalties to the score unless the penalty function is defined and experimentally justified. Keep categorical unresolved issues visible even if a score is also used.

## 9. 9V consequence audit

The 9V Consequence Tensor is an optional stage until its nine components and equations are formally specified.

When implemented, it should accept:

- candidate state;
- source state;
- relevant dependency graph;
- declared consequence dimensions;
- model and threshold versions.

It should return:

- component-wise consequence values;
- dependencies between components;
- uncertainty;
- failed or unavailable calculations;
- references to the evidence used.

It must not return a single unexplained “safety score”.

If the 9V model is not available, report `NOT_EVALUATED`. Do not treat missing 9V results as a successful pass.

## 10. Gate integration

The Gate receives:

- hard-constraint results;
- forward metrics;
- reverse-audit results;
- Shadow items;
- 9V output, if required and available;
- evidence quality and task policy.

A candidate can receive `ALLOW` only when all required checks for the declared task have passed.

Suggested behavior:

| Condition | Suggested verdict |
|---|---|
| Hard prohibition violated | `BLOCK` |
| Required test unavailable or evidence incomplete | `HOLD` |
| Localized correctable defect | `REPAIR` |
| Candidate representation invalid | `REWRITE` |
| All required checks passed | `ALLOW` |

The actual precedence policy is governed by `02_MATHEMATICAL_MODEL.md` and the task protocol. Do not create a conflicting local policy.

## 11. Stopping rules

A search must have an explicit stopping condition.

Possible stopping rules:

- all states in a finite search domain have been evaluated;
- candidate budget exhausted;
- time budget exhausted;
- an acceptable candidate has been found and the request allows early stopping;
- no new candidates are being generated;
- a required dependency or tool is unavailable;
- a safety or integrity condition requires the run to stop.

The result must include `stopping_reason`.

If a bounded or heuristic search stops early, report that the result is not an exhaustive optimum.

## 12. Baseline interfaces

CASR must be compared against existing approaches appropriate to the problem.

Potential baselines include:

- direct exhaustive enumeration for small domains;
- a simple random search;
- constraint programming / CP-SAT;
- SMT solving such as Z3;
- MiniZinc models;
- domain-specific deterministic heuristics.

These are candidate baselines, not mandatory dependencies. Select them according to the actual problem and document why.

Every comparison must use matched constraints, candidate domains, stopping conditions, and computational budgets wherever possible.

## 13. Pseudocode

The following is interface-level pseudocode. It is not a claim that a complete implementation already exists.

```python
def run_casr(request, operators, constraints, metrics, gate, memory):
    validate_request(request)

    result = new_search_result(request)

    candidates = operators.forward_propose(
        request.source_state,
        request.generation_parameters,
        request.candidate_budget,
    )

    for candidate in candidates:
        result.candidates_generated += 1

        hard_results = evaluate_hard_constraints(
            candidate,
            constraints,
        )

        if not all_required_constraints_pass(hard_results):
            record_rejection(result, candidate, hard_results)
            continue

        forward_metrics = evaluate_metrics(candidate, metrics)

        reverse_result = operators.reverse_audit(
            request.source_state,
            candidate,
        )

        shadow_items = build_shadow(
            candidate,
            hard_results,
            forward_metrics,
            reverse_result,
        )

        consequence_result = evaluate_9v_if_required(
            request,
            candidate,
            shadow_items,
        )

        verdict = gate.evaluate(
            candidate=candidate,
            hard_results=hard_results,
            forward_metrics=forward_metrics,
            reverse_result=reverse_result,
            shadow_items=shadow_items,
            consequence_result=consequence_result,
        )

        record_candidate(
            result,
            candidate,
            hard_results,
            forward_metrics,
            reverse_result,
            shadow_items,
            consequence_result,
            verdict,
        )

    finalize_counts_and_stopping_reason(result)
    memory.record_search_result(result)
    return result
```

The helper functions are interfaces to be implemented and tested. In particular, `evaluate_9v_if_required` must return `NOT_EVALUATED` when the model is undefined or unavailable; it must not silently return success.

## 14. Required implementation modules

The planned source layout is:

```text
src/
  state_space.py
  shadow_engine.py
  casr_solver.py
  gf2_engine.py
  consequence_tensor.py
  gate_operator.py
  memory_atoms.py
```

Suggested responsibilities:

| Module | Responsibility |
|---|---|
| `state_space.py` | State schemas, domains, constraints, and identity. |
| `shadow_engine.py` | Structured unresolved-item creation and tracking. |
| `casr_solver.py` | Candidate generation, filtering, metrics, and search result. |
| `gf2_engine.py` | Binary encoding, XOR, and GF(2) matrix operations. |
| `consequence_tensor.py` | 9V model interface and explicit not-evaluated state. |
| `gate_operator.py` | Verdict policy and evidence checks. |
| `memory_atoms.py` | Provenance and durable result records. |

Keep modules independently testable. Avoid circular imports and avoid making the solver itself responsible for every policy.

## 15. Required tests

At minimum, add tests for:

1. invalid search requests are rejected before candidate generation;
2. candidate generation respects the declared domain;
3. hard constraint failures cannot be overridden by a score;
4. duplicate handling follows the declared identity rule;
5. forward and reverse audit results are separately recorded;
6. missing 9V implementation returns `NOT_EVALUATED`, not `PASS`;
7. every candidate has a reproducible provenance record;
8. stopping reasons are reported accurately;
9. bounded search is never labeled exhaustive;
10. matched baseline configuration is recorded;
11. a candidate with missing required evidence cannot receive `ALLOW`;
12. search result counts reconcile with candidate records.

## 16. Open design decisions

| Decision | Status | Required work |
|---|---|---|
| Exact CASR acronym expansion | `OPEN` | Confirm project-defined expansion or leave as name. |
| Canonical state schema | `OPEN` | Define per problem domain. |
| Candidate generator for 18D plate model | `OPEN` | Specify exact enumeration and pruning. |
| Metric equations | `OPEN` where not explicitly defined | Write equations and tests. |
| Multi-objective ranking policy | `OPEN` | Select Pareto, lexicographic, or justified scalar objective. |
| Shadow severity aggregation | `OPEN` | Avoid arbitrary aggregation. |
| 9V equations | `OPEN` | Define all nine components. |
| Search budget defaults | `OPEN` | Choose per experiment and report explicitly. |

## 17. Completion criteria

The CASR search engine is not complete merely because it can produce candidates.

A minimum acceptable implementation must:

- use explicit state and request schemas;
- produce traceable candidates;
- enforce hard constraints;
- keep forward and reverse audits distinct;
- expose unresolved Shadow items;
- report unavailable consequence checks honestly;
- apply an explainable Gate policy;
- record stopping conditions and provenance;
- pass the required tests;
- compare against fair baselines.

Until these criteria are met, describe CASR as a specification or prototype, not a validated search advantage.
