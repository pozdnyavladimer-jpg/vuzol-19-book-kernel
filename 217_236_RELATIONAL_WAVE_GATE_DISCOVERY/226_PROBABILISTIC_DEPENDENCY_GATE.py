"""226 — Probabilistic Dependency Gate."""
from dataclasses import dataclass
@dataclass
class DependencyEdge:
    parent_id: str
    child_id: str
    probability: float
    downstream_impact: float
    version: int = 1
    @property
    def risk(self):
        return self.probability * self.downstream_impact

def should_propagate(edge, threshold):
    return edge.risk >= threshold
