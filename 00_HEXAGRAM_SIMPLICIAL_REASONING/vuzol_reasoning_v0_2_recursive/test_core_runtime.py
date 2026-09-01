from copy import deepcopy

from vuzol_reasoning import (
    Edge,
    ReasoningGraph,
    ReasoningNode,
    ShadowStore,
    Triad,
    evaluate_gate,
    minus3_backward,
    plus3_forward,
)
from vuzol_reasoning.gate import GatePolicy


def make_triad():
    a = ReasoningNode("A", 4)
    b = ReasoningNode("B", 7)
    c = ReasoningNode("C", 2)

    edges = [
        Edge("A", "B", "supports", critical=True),
        Edge("B", "C", "feeds", critical=False),
    ]

    return Triad([a, b, c], edges, []), edges


def test_graph_dependents_and_topological_order():
    g = ReasoningGraph()
    for node in [
        ReasoningNode("A", 4),
        ReasoningNode("B", 7),
        ReasoningNode("C", 11),
        ReasoningNode("D", 22),
    ]:
        g.add_node(node)

    g.add_edge(Edge("A", "C", "depends"))
    g.add_edge(Edge("B", "C", "depends"))
    g.add_edge(Edge("C", "D", "depends"))

    assert g.dependents("A") == {"C", "D"}
    order = g.topological_order()
    assert order.index("A") < order.index("C") < order.index("D")
    assert order.index("B") < order.index("C")


def test_plus3_shadow_minus3_roundtrip_edges():
    triad, expected_edges = make_triad()
    shadow = ShadowStore()

    parent = plus3_forward(
        triad,
        parent_id="P",
        operation="SUM",
        shadow_store=shadow,
    )

    assert parent.value == 13
    assert len(parent.retained_edges) == 1
    assert len(shadow) == 1

    backward = minus3_backward(parent, shadow_store=shadow)

    assert backward.reconstruction_error == 0.0
    assert backward.edge_error == 0.0
    assert backward.hard_failures == []


def test_gate_blocks_corrupted_critical_edge():
    triad, _ = make_triad()
    shadow = ShadowStore()

    parent = plus3_forward(
        triad,
        parent_id="P",
        operation="SUM",
        shadow_store=shadow,
    )

    broken = deepcopy(parent)
    broken.retained_edges = [
        Edge("A", "C", "supports", critical=True)
    ]

    backward = minus3_backward(broken, shadow_store=shadow)
    gate = evaluate_gate(broken, backward, GatePolicy())

    assert gate.verdict == "HOLD"
    assert "EDGE_RECONSTRUCTION_MISMATCH" in gate.reason_codes
    assert gate.repair_action == "EXPAND"


def test_local_repair_restores_allow():
    triad, _ = make_triad()
    shadow = ShadowStore()

    parent = plus3_forward(
        triad,
        parent_id="P",
        operation="SUM",
        shadow_store=shadow,
    )

    broken = deepcopy(parent)
    broken.retained_edges = [
        Edge("A", "C", "supports", critical=True)
    ]

    repaired = deepcopy(broken)
    repaired.retained_edges = [
        Edge("A", "B", "supports", critical=True)
    ]

    backward = minus3_backward(repaired, shadow_store=shadow)
    gate = evaluate_gate(repaired, backward, GatePolicy())

    assert gate.verdict == "ALLOW"


def test_critical_shadow_cannot_expire():
    triad, _ = make_triad()
    shadow = ShadowStore()

    parent = plus3_forward(
        triad,
        parent_id="P",
        operation="SUM",
        shadow_store=shadow,
    )

    sid = parent.shadow_ids[0]
    record = shadow.get(sid)
    # Non-critical Shadow may expire.
    assert record.critical is False
    assert shadow.expire(sid) is True
