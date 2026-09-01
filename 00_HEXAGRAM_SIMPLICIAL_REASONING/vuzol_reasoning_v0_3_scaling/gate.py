from __future__ import annotations

from dataclasses import dataclass

from .models import BackwardResult, CandidateParent, GateResult


@dataclass(frozen=True)
class GatePolicy:
    max_reconstruction_error: float = 0.0
    max_edge_error: float = 0.0
    max_uncertainty: float = 1.0
    require_critical_edge_integrity: bool = True


def evaluate_gate(
    candidate: CandidateParent,
    backward: BackwardResult,
    policy: GatePolicy | None = None,
) -> GateResult:
    policy = policy or GatePolicy()

    hard = list(backward.hard_failures)
    soft = []

    if backward.reconstruction_error > policy.max_reconstruction_error:
        soft.append("RECONSTRUCTION_TOO_HIGH")

    if backward.edge_error > policy.max_edge_error:
        if policy.require_critical_edge_integrity:
            if "EDGE_RECONSTRUCTION_MISMATCH" not in hard:
                hard.append("EDGE_RECONSTRUCTION_MISMATCH")
        else:
            soft.append("EDGE_ERROR_TOO_HIGH")

    if candidate.uncertainty > policy.max_uncertainty:
        soft.append("UNCERTAINTY_TOO_HIGH")

    if hard:
        # Missing/mismatched edges imply more detail is needed first.
        repair = "EXPAND" if "EDGE_RECONSTRUCTION_MISMATCH" in hard else "RECOMPUTE"
        verdict = "HOLD"
    elif soft:
        verdict = "EXPAND"
        repair = "EXPAND"
    else:
        verdict = "ALLOW"
        repair = None

    return GateResult(
        verdict=verdict,
        hard_failures=hard,
        soft_failures=soft,
        reason_codes=hard + soft,
        repair_action=repair,
        scores={
            "reconstruction_error": backward.reconstruction_error,
            "edge_error": backward.edge_error,
            "uncertainty": candidate.uncertainty,
        },
    )
