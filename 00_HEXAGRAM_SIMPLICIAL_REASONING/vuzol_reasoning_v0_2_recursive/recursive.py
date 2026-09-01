from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, Iterable, List, Set, Tuple

from .gate import GatePolicy, evaluate_gate
from .minus3 import minus3_backward
from .models import CandidateParent, Edge, GateResult, ReasoningNode, Triad
from .plus3 import plus3_forward
from .shadow import ShadowStore


@dataclass
class RecomputeEvent:
    node_id: str
    level: int
    old_value: float
    new_value: float
    gate_verdict: str


@dataclass
class RecursiveReasoningTree:
    """
    Deterministic balanced ternary aggregation tree.

    The hierarchy answers:
        what was compressed from what

    It intentionally remains separate from a richer dependency graph:
        what influences what
    """
    nodes: Dict[str, ReasoningNode] = field(default_factory=dict)
    children: Dict[str, List[str]] = field(default_factory=dict)
    parent_of: Dict[str, str] = field(default_factory=dict)
    levels: Dict[str, int] = field(default_factory=dict)
    candidates: Dict[str, CandidateParent] = field(default_factory=dict)
    gate_results: Dict[str, GateResult] = field(default_factory=dict)
    stale: Set[str] = field(default_factory=set)
    shadow_store: ShadowStore = field(default_factory=ShadowStore)
    root_id: str | None = None

    @classmethod
    def from_leaf_values(
        cls,
        values: Iterable[float],
        *,
        leaf_prefix: str = "L",
        operation: str = "SUM",
    ) -> "RecursiveReasoningTree":
        values = list(values)
        if not values:
            raise ValueError("At least one leaf is required.")

        # First prototype intentionally requires a power of 3.
        n = len(values)
        power = 1
        while power < n:
            power *= 3
        if power != n:
            raise ValueError("First prototype requires leaf count to be a power of 3.")

        tree = cls()

        current_ids: List[str] = []
        for i, value in enumerate(values):
            nid = f"{leaf_prefix}{i:02d}"
            tree.nodes[nid] = ReasoningNode(
                id=nid,
                value=value,
                node_type="leaf",
                provenance={"source_index": i},
            )
            tree.levels[nid] = 0
            current_ids.append(nid)

        level = 1
        while len(current_ids) > 1:
            next_ids: List[str] = []
            for group_index in range(0, len(current_ids), 3):
                child_ids = current_ids[group_index:group_index + 3]
                parent_id = f"P{level}_{group_index // 3:02d}"

                triad = tree._triad_from_ids(child_ids, parent_id)
                candidate = plus3_forward(
                    triad,
                    parent_id=parent_id,
                    operation=operation,
                    shadow_store=tree.shadow_store,
                )
                backward = minus3_backward(
                    candidate,
                    shadow_store=tree.shadow_store,
                )
                gate = evaluate_gate(
                    candidate,
                    backward,
                    GatePolicy(),
                )
                if gate.verdict != "ALLOW":
                    raise RuntimeError(
                        f"Initial tree build failed at {parent_id}: {gate.reason_codes}"
                    )

                parent_node = ReasoningNode(
                    id=parent_id,
                    value=candidate.value,
                    node_type="parent",
                    provenance={"children": list(child_ids)},
                )

                tree.nodes[parent_id] = parent_node
                tree.children[parent_id] = list(child_ids)
                tree.levels[parent_id] = level
                tree.candidates[parent_id] = candidate
                tree.gate_results[parent_id] = gate

                for cid in child_ids:
                    tree.parent_of[cid] = parent_id

                next_ids.append(parent_id)

            current_ids = next_ids
            level += 1

        tree.root_id = current_ids[0]
        return tree

    def _triad_from_ids(self, child_ids: List[str], parent_id: str) -> Triad:
        children = [self.nodes[cid] for cid in child_ids]

        # A small explicit local dependency motif.
        # The edges are between children and are used to test coupling retention.
        internal_edges = [
            Edge(
                source=child_ids[0],
                target=child_ids[1],
                relation="co_aggregate",
                critical=True,
            ),
            Edge(
                source=child_ids[1],
                target=child_ids[2],
                relation="co_aggregate",
                critical=False,
            ),
        ]

        return Triad(
            children=children,
            internal_edges=internal_edges,
            boundary_edges=[],
        )

    def ancestor_path(self, node_id: str) -> List[str]:
        path: List[str] = []
        current = node_id
        while current in self.parent_of:
            current = self.parent_of[current]
            path.append(current)
        return path

    def update_leaf(self, leaf_id: str, new_value: float) -> List[str]:
        node = self.nodes[leaf_id]
        if node.node_type != "leaf":
            raise ValueError("update_leaf expects a leaf node.")

        self.nodes[leaf_id] = ReasoningNode(
            id=node.id,
            value=new_value,
            node_type=node.node_type,
            uncertainty=node.uncertainty,
            provenance=dict(node.provenance),
        )

        affected = self.ancestor_path(leaf_id)
        self.stale.update(affected)
        return affected

    def corrupt_parent_value(self, parent_id: str, delta: float) -> None:
        if parent_id not in self.candidates:
            raise KeyError(parent_id)
        candidate = self.candidates[parent_id]
        candidate.value = candidate.value + delta

    def audit_parent(self, parent_id: str) -> GateResult:
        candidate = self.candidates[parent_id]
        backward = minus3_backward(
            candidate,
            shadow_store=self.shadow_store,
        )
        gate = evaluate_gate(
            candidate,
            backward,
            GatePolicy(),
        )
        self.gate_results[parent_id] = gate
        return gate

    def recompute_stale(self) -> List[RecomputeEvent]:
        events: List[RecomputeEvent] = []

        # Bottom-up: lower parent levels before higher ancestors.
        for parent_id in sorted(
            self.stale,
            key=lambda nid: self.levels[nid],
        ):
            child_ids = self.children[parent_id]
            old_value = self.nodes[parent_id].value

            triad = self._triad_from_ids(child_ids, parent_id)
            candidate = plus3_forward(
                triad,
                parent_id=parent_id,
                operation="SUM",
                shadow_store=self.shadow_store,
            )
            backward = minus3_backward(
                candidate,
                shadow_store=self.shadow_store,
            )
            gate = evaluate_gate(
                candidate,
                backward,
                GatePolicy(),
            )

            if gate.verdict != "ALLOW":
                raise RuntimeError(
                    f"Recompute failed at {parent_id}: {gate.reason_codes}"
                )

            self.candidates[parent_id] = candidate
            self.gate_results[parent_id] = gate
            self.nodes[parent_id] = ReasoningNode(
                id=parent_id,
                value=candidate.value,
                node_type="parent",
                provenance={"children": list(child_ids)},
            )

            events.append(
                RecomputeEvent(
                    node_id=parent_id,
                    level=self.levels[parent_id],
                    old_value=old_value,
                    new_value=candidate.value,
                    gate_verdict=gate.verdict,
                )
            )

        self.stale.clear()
        return events

    def root_value(self):
        if self.root_id is None:
            raise RuntimeError("Tree has no root.")
        return self.nodes[self.root_id].value

    def internal_node_count(self) -> int:
        return len(self.children)

    def leaf_ids(self) -> List[str]:
        return sorted(
            nid for nid, node in self.nodes.items()
            if node.node_type == "leaf"
        )
