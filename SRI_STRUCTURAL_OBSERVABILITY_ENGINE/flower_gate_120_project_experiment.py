"""
Flower Gate 120-project experiment — reproducible synthetic benchmark.

Compares:
1) Greedy heuristic
2) Flower Gate workflow: greedy seed + Shadow-style neighborhood repair
3) Exact MILP optimum (SciPy HiGHS)

This is NOT a CP-SAT run. It is an exact mixed-integer linear optimization
baseline. The benchmark data are synthetic and generated from a fixed seed.

Model:
- 120 projects
- 3 scarce resources: labor, budget, energy
- project prerequisites
- mutually exclusive project pairs
- risk budget
- conservative resource envelopes for uncertain consumption
- objective = total value - 1.8 * total risk

Flower Gate here is an orchestration/audit workflow around a transparent
local-search heuristic, not a new solver or a proven novel algorithm.
"""

import itertools
import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds


SEED = 20261112
N = 120
RISK_PENALTY = 1.8
MAX_ROUNDS = 30


def build_instance():
    rng = np.random.default_rng(SEED)
    resources = rng.integers([2, 1, 1], [18, 14, 12], size=(N, 3)).astype(float)
    uncertainty = rng.uniform(0.03, 0.22, size=(N, 3))
    robust_resources = resources * (1.0 + uncertainty)
    value = rng.integers(18, 110, size=N).astype(float)
    risk = rng.uniform(0.2, 8.0, size=N)
    utility = value - RISK_PENALTY * risk

    dependencies = {}
    for i in range(N):
        if i >= 15 and rng.random() < 0.28:
            dependencies[i] = [int(rng.integers(0, i))]

    conflicts = set()
    while len(conflicts) < 28:
        a, b = sorted(rng.choice(N, 2, replace=False).tolist())
        if b not in dependencies.get(a, []) and a not in dependencies.get(b, []):
            conflicts.add((a, b))

    capacities = robust_resources.sum(axis=0) * 0.34
    risk_capacity = float(risk.sum() * 0.34)
    return (resources, uncertainty, robust_resources, value, risk, utility,
            dependencies, sorted(conflicts), capacities, risk_capacity)


def solve(instance):
    resources, uncertainty, robust, value, risk, utility, deps, conflicts, caps, risk_cap = instance

    def closure(i):
        found, stack = set(), [i]
        while stack:
            j = stack.pop()
            if j in found:
                continue
            found.add(j)
            stack.extend(deps.get(j, []))
        return found

    def metrics(selected):
        ids = sorted(selected)
        loads = robust[ids].sum(axis=0) if ids else np.zeros(3)
        total_risk = float(risk[ids].sum()) if ids else 0.0
        total_value = float(value[ids].sum()) if ids else 0.0
        objective = float(utility[ids].sum()) if ids else 0.0
        feasible = bool(np.all(loads <= caps + 1e-7) and total_risk <= risk_cap + 1e-7)
        feasible = feasible and all(p in selected for c, ps in deps.items()
                                    if c in selected for p in ps)
        feasible = feasible and all(not (a in selected and b in selected)
                                    for a, b in conflicts)
        return {"ids": set(ids), "count": len(ids), "resources": loads,
                "risk": total_risk, "value": total_value, "objective": objective,
                "feasible": bool(feasible)}

    # Greedy baseline, with prerequisites added as a bundle.
    normalized_cost = (robust / caps).sum(axis=1) + 0.45 * risk / risk_cap
    order = sorted(range(N), key=lambda i: utility[i] / normalized_cost[i], reverse=True)
    greedy = set()
    for i in order:
        bundle = closure(i)
        if metrics(greedy | bundle)["feasible"]:
            greedy |= bundle

    # Flower Gate local repair:
    # Generate a candidate + prerequisites; try adding it while removing up to
    # two existing projects; accept the best feasible positive improvement.
    flower = set(greedy)
    history = [metrics(flower)["objective"]]
    for _ in range(MAX_ROUNDS):
        current = metrics(flower)["objective"]
        best_gain, best_set = 1e-9, None
        existing = sorted(flower)
        removals = [()]
        removals.extend((x,) for x in existing)
        removals.extend(itertools.combinations(existing, 2))

        for i in range(N):
            if i in flower:
                continue
            base = flower | closure(i)
            for remove in removals:
                candidate = base - set(remove)
                m = metrics(candidate)
                gain = m["objective"] - current
                if m["feasible"] and gain > best_gain:
                    best_gain, best_set = gain, candidate
        if best_set is None:
            break
        flower = best_set
        history.append(metrics(flower)["objective"])

    # Exact MILP reference.
    rows, lower, upper = [], [], []
    for k in range(3):
        rows.append(robust[:, k]); lower.append(-np.inf); upper.append(caps[k])
    rows.append(risk); lower.append(-np.inf); upper.append(risk_cap)
    for child, parents in deps.items():
        for parent in parents:
            row = np.zeros(N); row[child] = 1; row[parent] = -1
            rows.append(row); lower.append(-np.inf); upper.append(0)
    for a, b in conflicts:
        row = np.zeros(N); row[a] = 1; row[b] = 1
        rows.append(row); lower.append(-np.inf); upper.append(1)

    matrix = np.vstack(rows)
    result = milp(
        c=-utility,
        integrality=np.ones(N),
        bounds=Bounds(np.zeros(N), np.ones(N)),
        constraints=LinearConstraint(matrix, np.array(lower), np.array(upper)),
        options={"time_limit": 60},
    )
    if not result.success:
        raise RuntimeError(f"MILP did not prove optimum: {result.message}")
    exact = set(np.where(result.x > 0.5)[0].tolist())

    return metrics(greedy), metrics(flower), metrics(exact), history, result, {
        "dependencies": deps, "conflicts": conflicts, "capacities": caps,
        "risk_capacity": risk_cap, "closure": closure
    }


def main():
    instance = build_instance()
    resources, uncertainty, robust, value, risk, utility, deps, conflicts, caps, risk_cap = instance
    greedy, flower, exact, history, result, meta = solve(instance)

    print("BENCHMARK: synthetic / fixed seed", SEED)
    print("projects:", N, "| resource dimensions: labor, budget, energy")
    print("dependency edges:", sum(map(len, deps.values())), "| conflict pairs:", len(conflicts))
    print("uncertainty uplift per project/resource: 3%–22%; constraints use conservative envelope")
    print("risk cap:", round(risk_cap, 2))
    print("resource caps:", np.round(caps, 2).tolist())
    print()
    print(f"{'METHOD':<18} {'COUNT':>5} {'UTILITY':>10} {'VALUE':>9} {'RISK':>9} "
          f"{'LABOUR%':>9} {'BUDGET%':>9} {'ENERGY%':>9}")
    for name, m in [("Greedy", greedy), ("Flower Gate", flower), ("MILP optimum", exact)]:
        pct = m["resources"] / caps * 100
        print(f"{name:<18} {m['count']:>5} {m['objective']:>10.2f} {m['value']:>9.1f} "
              f"{m['risk']:>9.2f} {pct[0]:>8.1f}% {pct[1]:>8.1f}% {pct[2]:>8.1f}%")
    print()
    print("Flower Gate improvement over greedy:",
          f"{(flower['objective']/greedy['objective']-1)*100:.2f}%")
    print("Flower Gate gap to MILP optimum:",
          f"{(exact['objective']-flower['objective'])/exact['objective']*100:.2f}%")
    print("MILP solver status:", result.message)
    print("MILP relative gap:", result.get("mip_gap"))
    print("MILP nodes:", result.get("mip_node_count"))
    print("Flower Gate accepted objective path:", [round(x, 2) for x in history])
    print()
    print("SELECTED PROJECT IDS (1-based)")
    print("Greedy:", sorted(i + 1 for i in greedy["ids"]))
    print("Flower Gate:", sorted(i + 1 for i in flower["ids"]))
    print("MILP optimum:", sorted(i + 1 for i in exact["ids"]))
    print()
    print("AUDIT")
    print("all three plans feasible:", all(m["feasible"] for m in (greedy, flower, exact)))
    print("Flower Gate dependencies satisfied:",
          all(p in flower["ids"] for c, ps in deps.items() if c in flower["ids"] for p in ps))
    print("Flower Gate conflicts avoided:",
          all(not (a in flower["ids"] and b in flower["ids"]) for a, b in conflicts))
    print("Interpretation: this tests a Flower-Gate-inspired workflow, not a novel solver.")
    print("No CP-SAT comparison was run; the exact reference is MILP via SciPy/HiGHS.")


if __name__ == "__main__":
    main()
