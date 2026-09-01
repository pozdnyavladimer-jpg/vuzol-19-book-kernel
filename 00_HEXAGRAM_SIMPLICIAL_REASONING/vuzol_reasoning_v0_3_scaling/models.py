from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass(frozen=True)
class ReasoningNode:
    id: str
    value: Any
    node_type: str = "value"
    uncertainty: float = 0.0
    provenance: Dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class Edge:
    source: str
    target: str
    relation: str
    weight: float = 1.0
    critical: bool = False


@dataclass(frozen=True)
class Triad:
    children: List[ReasoningNode]
    internal_edges: List[Edge] = field(default_factory=list)
    boundary_edges: List[Edge] = field(default_factory=list)

    def __post_init__(self) -> None:
        if len(self.children) != 3:
            raise ValueError("Triad requires exactly three children.")


@dataclass
class ShadowRecord:
    id: str
    parent_id: str
    kind: str
    payload: Any
    critical: bool = False
    uncertainty: float = 0.0
    provenance: Dict[str, Any] = field(default_factory=dict)


@dataclass
class CandidateParent:
    id: str
    value: Any
    operation: str
    child_ids: List[str]
    retained_edges: List[Edge]
    boundary_edges: List[Edge]
    shadow_ids: List[str]
    uncertainty: float
    certificate: Dict[str, Any]
    provenance: Dict[str, Any]


@dataclass
class BackwardResult:
    reconstructed_child_ids: List[str]
    reconstructed_edges: List[Edge]
    reconstruction_error: float
    edge_error: float
    ambiguity: float
    hard_failures: List[str]
    notes: List[str] = field(default_factory=list)


@dataclass
class GateResult:
    verdict: str
    hard_failures: List[str]
    soft_failures: List[str]
    reason_codes: List[str]
    repair_action: Optional[str]
    scores: Dict[str, float] = field(default_factory=dict)
