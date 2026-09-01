from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Iterable, List

from .recursive import RecursiveReasoningTree


@dataclass(frozen=True)
class ScalingPoint:
    leaves: int
    depth: int
    internal_nodes: int
    local_recompute_nodes: int
    saved_internal_recomputations: int
    recompute_fraction: float
    speedup_by_node_count: float


def ternary_depth(leaves: int) -> int:
    if leaves < 1:
        raise ValueError("leaves must be >= 1")
    depth = round(math.log(leaves, 3))
    if 3 ** depth != leaves:
        raise ValueError("leaves must be an exact power of 3")
    return depth


def full_ternary_internal_nodes(leaves: int) -> int:
    # For a full m-ary tree: I = (L - 1) / (m - 1), with m = 3.
    if leaves < 1:
        raise ValueError("leaves must be >= 1")
    return (leaves - 1) // 2


def run_single_leaf_repair(leaves: int, leaf_index: int | None = None) -> ScalingPoint:
    depth = ternary_depth(leaves)
    values = list(range(1, leaves + 1))
    tree = RecursiveReasoningTree.from_leaf_values(values)

    if leaf_index is None:
        leaf_index = leaves // 2

    leaf_id = f"L{leaf_index:02d}"
    # IDs use at least two digits, and naturally grow beyond that for larger trees.
    if leaf_id not in tree.nodes:
        leaf_id = f"L{leaf_index}"

    old_value = tree.nodes[leaf_id].value
    tree.update_leaf(leaf_id, old_value + 1000)
    events = tree.recompute_stale()

    internal = tree.internal_node_count()
    local = len(events)

    return ScalingPoint(
        leaves=leaves,
        depth=depth,
        internal_nodes=internal,
        local_recompute_nodes=local,
        saved_internal_recomputations=internal - local,
        recompute_fraction=local / internal,
        speedup_by_node_count=internal / local,
    )


def run_scaling_series(sizes: Iterable[int]) -> List[ScalingPoint]:
    return [run_single_leaf_repair(size) for size in sizes]
