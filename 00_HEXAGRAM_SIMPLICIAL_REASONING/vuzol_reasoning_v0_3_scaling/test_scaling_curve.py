from vuzol_reasoning.scaling import (
    full_ternary_internal_nodes,
    run_scaling_series,
    ternary_depth,
)


def test_ternary_depth_and_internal_count():
    assert ternary_depth(27) == 3
    assert ternary_depth(81) == 4
    assert ternary_depth(243) == 5
    assert ternary_depth(729) == 6

    assert full_ternary_internal_nodes(27) == 13
    assert full_ternary_internal_nodes(81) == 40
    assert full_ternary_internal_nodes(243) == 121
    assert full_ternary_internal_nodes(729) == 364


def test_local_recompute_matches_tree_depth():
    points = run_scaling_series([27, 81, 243, 729])

    assert [p.local_recompute_nodes for p in points] == [3, 4, 5, 6]
    assert [p.internal_nodes for p in points] == [13, 40, 121, 364]


def test_recompute_fraction_falls_with_scale():
    points = run_scaling_series([27, 81, 243, 729])
    fractions = [p.recompute_fraction for p in points]

    assert fractions == sorted(fractions, reverse=True)
    assert fractions[-1] < 0.02
