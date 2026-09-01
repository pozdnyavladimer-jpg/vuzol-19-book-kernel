from vuzol_reasoning import RecursiveReasoningTree


def test_27_leaf_tree_shape_and_root_sum():
    tree = RecursiveReasoningTree.from_leaf_values(range(1, 28))

    assert len(tree.leaf_ids()) == 27
    assert tree.internal_node_count() == 13  # 9 + 3 + 1
    assert tree.root_value() == sum(range(1, 28))
    assert tree.levels[tree.root_id] == 3


def test_single_leaf_change_only_marks_three_ancestors_stale():
    tree = RecursiveReasoningTree.from_leaf_values(range(1, 28))

    affected = tree.update_leaf("L13", 100)

    assert len(affected) == 3
    assert set(affected) == tree.stale


def test_single_leaf_repair_recomputes_only_ancestor_path():
    tree = RecursiveReasoningTree.from_leaf_values(range(1, 28))
    old_root = tree.root_value()

    affected = tree.update_leaf("L13", 100)
    events = tree.recompute_stale()

    assert len(events) == 3
    assert {event.node_id for event in events} == set(affected)
    assert all(event.gate_verdict == "ALLOW" for event in events)

    # L13 originally held value 14.
    expected_root = old_root - 14 + 100
    assert tree.root_value() == expected_root


def test_corrupted_internal_parent_is_caught_by_minus3_gate():
    tree = RecursiveReasoningTree.from_leaf_values(range(1, 28))

    parent_id = "P1_04"
    tree.corrupt_parent_value(parent_id, delta=5)

    gate = tree.audit_parent(parent_id)

    assert gate.verdict == "HOLD"
    assert "PARENT_VALUE_MISMATCH" in gate.reason_codes
