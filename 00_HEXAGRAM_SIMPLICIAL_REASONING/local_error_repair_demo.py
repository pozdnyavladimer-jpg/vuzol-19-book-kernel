from copy import deepcopy
import json

from vuzol_reasoning import (
    Edge,
    ReasoningNode,
    ShadowStore,
    Triad,
    evaluate_gate,
    minus3_backward,
    plus3_forward,
)
from vuzol_reasoning.gate import GatePolicy
from vuzol_reasoning.metrics import edge_recall


def main():
    a = ReasoningNode("A", 4)
    b = ReasoningNode("B", 7)
    c = ReasoningNode("C", 2)

    expected_edges = [
        Edge("A", "B", "supports", critical=True),
        Edge("B", "C", "feeds", critical=False),
    ]

    triad = Triad(
        children=[a, b, c],
        internal_edges=expected_edges,
        boundary_edges=[],
    )

    shadow = ShadowStore()
    parent = plus3_forward(
        triad,
        parent_id="P1",
        operation="SUM",
        shadow_store=shadow,
    )

    # Healthy audit.
    healthy_backward = minus3_backward(parent, shadow_store=shadow)
    healthy_gate = evaluate_gate(parent, healthy_backward, GatePolicy())

    # Inject a local structural error by corrupting a retained critical edge.
    corrupted = deepcopy(parent)
    corrupted.retained_edges = [
        Edge("A", "C", "supports", critical=True)
    ]

    broken_backward = minus3_backward(corrupted, shadow_store=shadow)
    broken_gate = evaluate_gate(corrupted, broken_backward, GatePolicy())

    # Repair only the corrupted local edge, not the entire task.
    repaired = deepcopy(corrupted)
    repaired.retained_edges = [
        Edge("A", "B", "supports", critical=True)
    ]

    repaired_backward = minus3_backward(repaired, shadow_store=shadow)
    repaired_gate = evaluate_gate(repaired, repaired_backward, GatePolicy())

    report = {
        "root_value": parent.value,
        "healthy_gate": healthy_gate.verdict,
        "broken_gate": broken_gate.verdict,
        "broken_repair_action": broken_gate.repair_action,
        "broken_reason_codes": broken_gate.reason_codes,
        "repaired_gate": repaired_gate.verdict,
        "edge_recall_after_repair": edge_recall(
            expected_edges,
            repaired_backward.reconstructed_edges,
        ),
        "shadow_records": len(shadow),
        "nodes_recomputed": 1,
        "error_detected": broken_gate.verdict != "ALLOW",
    }

    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
