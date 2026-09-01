from __future__ import annotations

from collections import Counter
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


def minus3_backward(
    candidate: CandidateParent,
    *,
    shadow_store: ShadowStore | None = None,
) -> BackwardResult:
    """
    Deterministic audit reconstruction from provenance + retained edges + Shadow.
    It does not claim a mathematical inverse.
    """
    expected_child_ids = list(candidate.provenance.get("child_ids", []))
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

    edge_error = _multiset_edge_error(expected_edges, reconstructed_edges)
    if edge_error > 0:
        hard_failures.append("EDGE_RECONSTRUCTION_MISMATCH")

    # For this first prototype, child identity is reconstructed exactly from provenance.
    reconstruction_error = 0.0 if len(expected_child_ids) == 3 else 1.0

    ambiguity = 0.0
    if not candidate.provenance.get("child_ids"):
        ambiguity = 1.0
        hard_failures.append("MISSING_PROVENANCE")

    if candidate.shadow_ids and shadow_store is None:
        notes.append("Shadow references exist but no ShadowStore was provided.")
        if expected_edges:
            # Missing Shadow may make edge reconstruction incomplete.
            if "EDGE_RECONSTRUCTION_MISMATCH" not in hard_failures:
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
