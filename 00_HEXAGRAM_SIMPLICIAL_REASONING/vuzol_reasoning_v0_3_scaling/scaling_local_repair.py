from __future__ import annotations

import json
from pathlib import Path

from vuzol_reasoning.scaling import run_scaling_series


def main():
    sizes = [27, 81, 243, 729]
    points = run_scaling_series(sizes)

    payload = {
        "experiment": "single_leaf_local_repair_scaling",
        "branching_factor": 3,
        "sizes": sizes,
        "results": [
            {
                "leaves": p.leaves,
                "depth": p.depth,
                "internal_nodes": p.internal_nodes,
                "local_recompute_nodes": p.local_recompute_nodes,
                "saved_internal_recomputations": p.saved_internal_recomputations,
                "recompute_fraction": p.recompute_fraction,
                "speedup_by_node_count": p.speedup_by_node_count,
            }
            for p in points
        ],
    }

    out = Path("experiments/results/local_repair_scaling.json")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(payload, indent=2), encoding="utf-8")

    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
