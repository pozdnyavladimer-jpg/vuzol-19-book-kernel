from __future__ import annotations

from typing import Callable, Dict

from .models import CandidateParent, ShadowRecord, Triad
from .shadow import ShadowStore


def _default_reduce(values, operation: str):
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


def plus3_forward(
    triad: Triad,
    *,
    parent_id: str,
    operation: str = "SUM",
    shadow_store: ShadowStore | None = None,
    reducer: Callable | None = None,
) -> CandidateParent:
    """
    Deterministic first prototype.

    All child values are aggregated into one parent.
    Critical internal edges are retained.
    Non-critical internal edges are moved to Shadow.
    Boundary edges remain explicit.
    """
    values = [child.value for child in triad.children]
    reduce_fn = reducer or _default_reduce
    parent_value = reduce_fn(values, operation)

    retained_edges = [e for e in triad.internal_edges if e.critical]
    omitted_edges = [e for e in triad.internal_edges if not e.critical]

    shadow_ids = []
    if shadow_store is not None:
        for i, edge in enumerate(omitted_edges):
            sid = f"{parent_id}:edge:{i}"
            shadow_store.put(
                ShadowRecord(
                    id=sid,
                    parent_id=parent_id,
                    kind="omitted_edge",
                    payload=edge,
                    critical=False,
                    provenance={"source": "plus3_forward"},
                )
            )
            shadow_ids.append(sid)

    uncertainty = max(child.uncertainty for child in triad.children)

    certificate: Dict[str, object] = {
        "child_count": 3,
        "critical_edges_retained": len(retained_edges),
        "boundary_edges_retained": len(triad.boundary_edges),
        "operation": operation,
    }

    return CandidateParent(
        id=parent_id,
        value=parent_value,
        operation=operation,
        child_ids=[child.id for child in triad.children],
        retained_edges=list(retained_edges),
        boundary_edges=list(triad.boundary_edges),
        shadow_ids=shadow_ids,
        uncertainty=uncertainty,
        certificate=certificate,
        provenance={
            "child_values": values,
            "child_ids": [child.id for child in triad.children],
            "internal_edges": list(triad.internal_edges),
        },
    )
