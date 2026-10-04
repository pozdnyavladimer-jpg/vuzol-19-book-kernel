"""
224 — BINDU STATE ENGINE MINIMAL RUNTIME
Synthetic reference implementation for Vuzol-19 experiment 223.

No LLM is required. This isolates the claimed architectural advantage:
dependency-aware invalidation and selective recomputation.
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, List, Set, Optional

class State(str, Enum):
    KEEP="KEEP"
    HOLD="HOLD"
    BLOCK="BLOCK"
    STALE="STALE"

@dataclass
class MemoryAtom:
    id: str
    claim: str
    value: bool
    parent_ids: List[str] = field(default_factory=list)
    child_ids: List[str] = field(default_factory=list)
    version: int = 1
    state: State = State.KEEP
    falsifier: Optional[str] = None

class BinduEngine:
    def __init__(self):
        self.nodes: Dict[str, MemoryAtom] = {}

    def add(self, atom: MemoryAtom):
        self.nodes[atom.id] = atom
        for p in atom.parent_ids:
            if p in self.nodes and atom.id not in self.nodes[p].child_ids:
                self.nodes[p].child_ids.append(atom.id)

    def descendants(self, root_id: str) -> Set[str]:
        seen=set()
        stack=list(self.nodes[root_id].child_ids)
        while stack:
            n=stack.pop()
            if n in seen: continue
            seen.add(n)
            stack.extend(self.nodes[n].child_ids)
        return seen

    def block(self, root_id: str):
        self.nodes[root_id].state=State.BLOCK
        for d in self.descendants(root_id):
            if self.nodes[d].state != State.BLOCK:
                self.nodes[d].state=State.STALE

    def repair(self, evaluator):
        """Recompute only STALE nodes in dependency order."""
        repaired=0
        progress=True
        while progress:
            progress=False
            for node in self.nodes.values():
                if node.state != State.STALE:
                    continue
                parents=[self.nodes[p] for p in node.parent_ids]
                if any(p.state == State.STALE for p in parents):
                    continue
                node.value=evaluator(node, parents)
                node.version += 1
                node.state=State.KEEP
                repaired += 1
                progress=True
        return repaired
