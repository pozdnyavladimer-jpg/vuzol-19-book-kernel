from __future__ import annotations

from typing import Iterable

from .models import Edge


def edge_recall(expected: Iterable[Edge], actual: Iterable[Edge]) -> float:
    expected_keys = {(e.source, e.target, e.relation, e.critical) for e in expected}
    actual_keys = {(e.source, e.target, e.relation, e.critical) for e in actual}
    if not expected_keys:
        return 1.0
    return len(expected_keys & actual_keys) / len(expected_keys)


def edge_precision(expected: Iterable[Edge], actual: Iterable[Edge]) -> float:
    expected_keys = {(e.source, e.target, e.relation, e.critical) for e in expected}
    actual_keys = {(e.source, e.target, e.relation, e.critical) for e in actual}
    if not actual_keys:
        return 1.0 if not expected_keys else 0.0
    return len(expected_keys & actual_keys) / len(actual_keys)


def edge_f1(expected: Iterable[Edge], actual: Iterable[Edge]) -> float:
    p = edge_precision(expected, actual)
    r = edge_recall(expected, actual)
    if p + r == 0:
        return 0.0
    return 2 * p * r / (p + r)
