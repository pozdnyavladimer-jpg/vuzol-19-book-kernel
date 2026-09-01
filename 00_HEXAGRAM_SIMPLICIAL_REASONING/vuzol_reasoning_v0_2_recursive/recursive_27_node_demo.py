import json

from vuzol_reasoning import RecursiveReasoningTree


def main():
    tree = RecursiveReasoningTree.from_leaf_values(range(1, 28))

    initial_root = tree.root_value()

    # 1) Corrupt one internal parent and verify that -3/Gate catches it.
    corrupted_parent = "P1_04"
    tree.corrupt_parent_value(corrupted_parent, delta=5)
    corrupted_gate = tree.audit_parent(corrupted_parent)

    # Restore that parent by marking/recomputing only it and its ancestors.
    # A real runtime would derive this from dependency invalidation.
    tree.stale.update([corrupted_parent] + tree.ancestor_path(corrupted_parent))
    internal_repair_events = tree.recompute_stale()

    # 2) Now change one leaf and recompute only its ancestor path.
    changed_leaf = "L13"
    old_leaf_value = tree.nodes[changed_leaf].value
    affected = tree.update_leaf(changed_leaf, 100)
    leaf_repair_events = tree.recompute_stale()

    expected_root = initial_root - old_leaf_value + 100

    report = {
        "tree": {
            "leaf_count": len(tree.leaf_ids()),
            "internal_count": tree.internal_node_count(),
            "levels": 3,
            "initial_root": initial_root,
        },
        "internal_corruption": {
            "node": corrupted_parent,
            "gate": corrupted_gate.verdict,
            "reason_codes": corrupted_gate.reason_codes,
            "repair_nodes": [e.node_id for e in internal_repair_events],
            "repair_count": len(internal_repair_events),
        },
        "leaf_change": {
            "leaf": changed_leaf,
            "old_value": old_leaf_value,
            "new_value": 100,
            "affected_ancestors": affected,
            "recomputed_nodes": [e.node_id for e in leaf_repair_events],
            "recompute_count": len(leaf_repair_events),
        },
        "final": {
            "root_value": tree.root_value(),
            "expected_root": expected_root,
            "root_correct": tree.root_value() == expected_root,
            "full_restart_nodes_if_naive": tree.internal_node_count(),
            "actual_internal_nodes_recomputed": len(leaf_repair_events),
            "saved_internal_recomputations": (
                tree.internal_node_count() - len(leaf_repair_events)
            ),
        },
    }

    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
