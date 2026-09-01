from __future__ import annotations

from collections import Counter
from numbers import Number
from typing import Iterable, List

from .models import BackwardResult, CandidateParent, Edge
from .shadow import ShadowStore


def _edge_key(edge: Edge):
    return (edge.source, edge.target, edge.relation, edge.critical)


def _multiset_edge_error(expected: Iterable[Edge], actual: Iterable[Edge]) -> float:
    exp = Counter(_edge_key(e) for e in expected)
    act = Counter(_edge_key(e) for e in actual)
    missing = sum((exp - act).values())
    extra = sum((act - exp).values())
    denom = max(1, sum(exp.values()))
    return (missing + extra) / denom


def _reduce(values, operation: str):
    if operation == "SUM":
        return sum(values)
    if operation == "PRODUCT":
        out = 1
        for value in values:
            out *= value
        return out
    if operation == "MEAN":
        return sum(values) / len(values)
    raise ValueError(f"Unsupported operation: {operation}")


def _numeric_error(expected, actual) -> float:
    if isinstance(expected, Number) and isinstance(actual, Number):
        return float(abs(expected - actual))
    return 0.0 if expected == actual else 1.0


def minus3_backward(
    candidate: CandidateParent,
    *,
    shadow_store: ShadowStore | None = None,
) -> BackwardResult:
    """
    Deterministic audit reconstruction from provenance + retained edges + Shadow.

    Important:
    - This is not claimed to be a mathematical inverse.
    - It checks whether the candidate parent is still consistent with the
      child state preserved in provenance.
    """
    expected_child_ids = list(candidate.provenance.get("child_ids", []))
    child_values = list(candidate.provenance.get("child_values", []))
    expected_edges: List[Edge] = list(candidate.provenance.get("internal_edges", []))

    reconstructed_edges = list(candidate.retained_edges)

    if shadow_store is not None:
        for sid in candidate.shadow_ids:
            record = shadow_store.get(sid)
            if record.kind == "omitted_edge":
                reconstructed_edges.append(record.payload)

    hard_failures = []
    notes = []

    if len(expected_child_ids) != 3:
        hard_failures.append("INVALID_CHILD_PROVENANCE")

    # Verify parent value against the child values that created it.
    reconstruction_error = 0.0
    if len(child_values) == 3:
        try:
            expected_parent_value = _reduce(child_values, candidate.operation)
            reconstruction_error = _numeric_error(
                expected_parent_value,
                candidate.value,
            )
            if reconstruction_error > 0:
                hard_failures.append("PARENT_VALUE_MISMATCH")
        except ValueError:
            hard_failures.append("UNSUPPORTED_FORWARD_OPERATION")
            reconstruction_error = 1.0
    else:
        reconstruction_error = 1.0
        hard_failures.append("MISSING_CHILD_VALUES")

    edge_error = _multiset_edge_error(expected_edges, reconstructed_edges)
    if edge_error > 0:
        hard_failures.append("EDGE_RECONSTRUCTION_MISMATCH")

    ambiguity = 0.0
    if not candidate.provenance.get("child_ids"):
        ambiguity = 1.0
        hard_failures.append("MISSING_PROVENANCE")

    if candidate.shadow_ids and shadow_store is None:
        notes.append("Shadow references exist but no ShadowStore was provided.")
        if expected_edges and "EDGE_RECONSTRUCTION_MISMATCH" not in hard_failures:
            hard_failures.append("EDGE_RECONSTRUCTION_MISMATCH")

    return BackwardResult(
        reconstructed_child_ids=expected_child_ids,
        reconstructed_edges=reconstructed_edges,
        reconstruction_error=reconstruction_error,
        edge_error=edge_error,
        ambiguity=ambiguity,
        hard_failures=hard_failures,
        notes=notes,
    )
