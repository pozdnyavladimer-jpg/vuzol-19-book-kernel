from __future__ import annotations

from collections import defaultdict, deque
from typing import Dict, Iterable, List, Set

from .models import Edge, ReasoningNode


class ReasoningGraph:
    """Small deterministic dependency graph for the first prototype."""

    def __init__(self) -> None:
        self.nodes: Dict[str, ReasoningNode] = {}
        self.edges: List[Edge] = []

    def add_node(self, node: ReasoningNode) -> None:
        self.nodes[node.id] = node

    def add_edge(self, edge: Edge) -> None:
        if edge.source not in self.nodes or edge.target not in self.nodes:
            raise KeyError("Both edge endpoints must exist before adding an edge.")
        self.edges.append(edge)

    def outgoing(self, node_id: str) -> List[Edge]:
        return [e for e in self.edges if e.source == node_id]

    def incoming(self, node_id: str) -> List[Edge]:
        return [e for e in self.edges if e.target == node_id]

    def critical_edges(self) -> List[Edge]:
        return [e for e in self.edges if e.critical]

    def boundary_edges(self, node_ids: Iterable[str]) -> List[Edge]:
        inside = set(node_ids)
        return [
            e for e in self.edges
            if (e.source in inside) ^ (e.target in inside)
        ]

    def internal_edges(self, node_ids: Iterable[str]) -> List[Edge]:
        inside = set(node_ids)
        return [
            e for e in self.edges
            if e.source in inside and e.target in inside
        ]

    def dependents(self, node_id: str) -> Set[str]:
        adjacency = defaultdict(list)
        for edge in self.edges:
            adjacency[edge.source].append(edge.target)

        seen: Set[str] = set()
        queue = deque([node_id])

        while queue:
            current = queue.popleft()
            for nxt in adjacency[current]:
                if nxt not in seen:
                    seen.add(nxt)
                    queue.append(nxt)
        seen.discard(node_id)
        return seen

    def topological_order(self) -> List[str]:
        indegree = {nid: 0 for nid in self.nodes}
        adjacency = defaultdict(list)

        for edge in self.edges:
            adjacency[edge.source].append(edge.target)
            indegree[edge.target] += 1

        queue = deque(sorted([nid for nid, deg in indegree.items() if deg == 0]))
        order: List[str] = []

        while queue:
            node = queue.popleft()
            order.append(node)
            for nxt in sorted(adjacency[node]):
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    queue.append(nxt)

        if len(order) != len(self.nodes):
            raise ValueError("Dependency graph contains a cycle.")
        return order
