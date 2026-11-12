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




def casr_shadow_solve(instance, max_rounds=30, triad_depth=14):
    """
    Upgraded Flower Gate / CASR workflow supplied for this experiment:
    adaptive Shadow-Pressure seed, +3 bundle expansion, and -3 reverse
    dependency/conflict unwinding. Final feasibility is independently audited
    by main_casr().
    """
    resources, uncertainty, robust, value, risk, utility, deps, conflicts, caps, risk_cap = instance
    n_proj = len(utility)
    caps_4d = np.append(caps, risk_cap)
    loads_4d = np.column_stack([robust, risk])

    def fwd_closure(i):
        found, stack = set(), [i]
        while stack:
            j = stack.pop()
            if j not in found:
                found.add(j)
                stack.extend(deps.get(j, []))
        return found

    fwd_closures = [fwd_closure(i) for i in range(n_proj)]
    rev_deps = {i: set() for i in range(n_proj)}
    for child, parents in deps.items():
        for parent in parents:
            rev_deps[parent].add(child)

    def rev_closure(i, active_set):
        found, stack = set(), [i]
        while stack:
            j = stack.pop()
            if j in found or j not in active_set:
                continue
            found.add(j)
            stack.extend(rev_deps[j] & active_set)
        return found

    conf_adj = [set() for _ in range(n_proj)]
    for a, b in conflicts:
        conf_adj[a].add(b)
        conf_adj[b].add(a)

    # Phase 1: adaptive seed.
    weights = np.array([1.0, 1.0, 1.0, 0.45])
    best_seed, best_seed_obj = set(), -1.0
    for _ in range(4):
        cost_score = (loads_4d / caps_4d) @ weights
        order = sorted(
            range(n_proj),
            key=lambda i: utility[i] / max(cost_score[i], 1e-6),
            reverse=True,
        )
        cand_set, cand_load = set(), np.zeros(4)
        for i in order:
            bundle = fwd_closures[i] - cand_set
            if not bundle or any(
                y in conf_adj[x] for x in bundle for y in (cand_set | bundle)
            ):
                continue
            bundle_load = loads_4d[list(bundle)].sum(axis=0)
            if np.all(cand_load + bundle_load <= caps_4d + 1e-7):
                cand_set |= bundle
                cand_load += bundle_load
        obj = float(utility[list(cand_set)].sum())
        if obj > best_seed_obj:
            best_seed_obj, best_seed = obj, set(cand_set)
        saturation = cand_load / caps_4d
        weights = weights * (saturation ** 3)
        weights /= weights.mean()

    # Phase 2: +3 bundle proposals and -3 subtree removals.
    current_set = best_seed
    current_load = loads_4d[list(current_set)].sum(axis=0)
    history = [float(utility[list(current_set)].sum())]

    for _ in range(max_rounds):
        best_gain, best_new_set = 1e-9, None
        slack_ratio = np.maximum(0.01, (caps_4d - current_load) / caps_4d)
        shadow_price = 1.0 / (slack_ratio ** 1.5)
        shadow_price /= shadow_price.sum()

        rem_units = {
            frozenset(rev_closure(x, current_set)) for x in current_set
        }
        rem_info = []
        for unit in rem_units:
            unit_list = list(unit)
            unit_utility = float(utility[unit_list].sum())
            unit_load = loads_4d[unit_list].sum(axis=0)
            shadow_cost = float((unit_load / caps_4d) @ shadow_price)
            rem_info.append((
                unit_utility / max(shadow_cost, 1e-6),
                unit, unit_utility, unit_load
            ))
        rem_info.sort(key=lambda item: item[0])
        weak_rems = rem_info[:25]

        unselected = sorted(
            [i for i in range(n_proj) if i not in current_set],
            key=lambda i: utility[i] / max(
                float((loads_4d[i] / caps_4d) @ shadow_price), 1e-6
            ),
            reverse=True,
        )
        add_bundles, seen = [], set()
        for i in unselected:
            bundle = frozenset(fwd_closures[i] - current_set)
            if bundle and bundle not in seen and not any(
                y in conf_adj[x] for x in bundle for y in bundle
            ):
                seen.add(bundle)
                add_bundles.append(bundle)

        top_s = add_bundles[:26]
        for b1, b2 in itertools.combinations(top_s, 2):
            bundle = b1 | b2
            if bundle not in seen and not any(
                y in conf_adj[x] for x in bundle for y in bundle
            ):
                seen.add(bundle)
                add_bundles.append(bundle)

        for b1, b2, b3 in itertools.combinations(top_s[:triad_depth], 3):
            bundle = b1 | b2 | b3
            if bundle not in seen and not any(
                y in conf_adj[x] for x in bundle for y in bundle
            ):
                seen.add(bundle)
                add_bundles.append(bundle)

        for bundle in add_bundles:
            bundle_list = list(bundle)
            mandatory_rem = set()
            for x in bundle:
                for conflict in conf_adj[x] & current_set:
                    mandatory_rem |= rev_closure(conflict, current_set)

            if any(
                prerequisite in mandatory_rem
                for x in bundle for prerequisite in fwd_closures[x]
            ):
                continue

            rem_list = list(mandatory_rem)
            base_gain = float(utility[bundle_list].sum()) - (
                float(utility[rem_list].sum()) if rem_list else 0.0
            )
            if base_gain <= best_gain:
                continue

            base_load = (
                current_load
                + loads_4d[bundle_list].sum(axis=0)
                - (loads_4d[rem_list].sum(axis=0) if rem_list else 0.0)
            )

            if np.all(base_load <= caps_4d + 1e-7):
                best_gain = base_gain
                best_new_set = (current_set - mandatory_rem) | bundle
                continue

            bundle_prereqs = set().union(*(fwd_closures[x] for x in bundle))
            valid_extra = [
                (unit, unit_utility, unit_load)
                for (_, unit, unit_utility, unit_load) in weak_rems
                if not (unit & mandatory_rem)
                and not (unit & bundle_prereqs)
                and (base_gain - unit_utility > best_gain)
            ]

            for idx1, (u1, u1_utility, u1_load) in enumerate(valid_extra):
                load1 = base_load - u1_load
                gain1 = base_gain - u1_utility
                if np.all(load1 <= caps_4d + 1e-7):
                    if gain1 > best_gain:
                        best_gain = gain1
                        best_new_set = (current_set - mandatory_rem - u1) | bundle
                else:
                    for idx2 in range(idx1 + 1, len(valid_extra)):
                        u2, u2_utility, u2_load = valid_extra[idx2]
                        if gain1 - u2_utility <= best_gain or (u1 & u2):
                            continue
                        if np.all(load1 - u2_load <= caps_4d + 1e-7):
                            best_gain = gain1 - u2_utility
                            best_new_set = (
                                current_set - mandatory_rem - u1 - u2
                            ) | bundle

        if best_new_set is None:
            break
        current_set = best_new_set
        current_load = loads_4d[list(current_set)].sum(axis=0)
        history.append(float(utility[list(current_set)].sum()))

    return current_set, history


def main_casr():
    instance = build_instance()
    resources, uncertainty, robust, value, risk, utility, deps, conflicts, caps, risk_cap = instance

    # Reuse the same baseline and exact MILP reference as the previous run.
    greedy, previous_flower, exact, _, milp_result, meta = solve(instance)

    import time
    start = time.perf_counter()
    casr_ids, casr_history = casr_shadow_solve(instance, max_rounds=30, triad_depth=14)
    casr_seconds = time.perf_counter() - start

    def evaluate(ids):
        ids = set(ids)
        selected = sorted(ids)
        loads = robust[selected].sum(axis=0) if selected else np.zeros(3)
        total_risk = float(risk[selected].sum()) if selected else 0.0
        total_value = float(value[selected].sum()) if selected else 0.0
        objective = float(utility[selected].sum()) if selected else 0.0
        dependency_ok = all(
            parent in ids
            for child, parents in deps.items() if child in ids
            for parent in parents
        )
        conflicts_ok = all(not (a in ids and b in ids) for a, b in conflicts)
        feasible = bool(
            np.all(loads <= caps + 1e-7)
            and total_risk <= risk_cap + 1e-7
            and dependency_ok and conflicts_ok
        )
        return {
            "ids": ids, "count": len(ids), "resources": loads,
            "risk": total_risk, "value": total_value,
            "objective": objective, "feasible": feasible,
            "dependency_ok": dependency_ok, "conflicts_ok": conflicts_ok,
        }

    casr = evaluate(casr_ids)
    print("BENCHMARK: synthetic / fixed seed", SEED)
    print("projects:", N, "| dependencies:", sum(map(len, deps.values())),
          "| conflict pairs:", len(conflicts))
    print("resource caps:", np.round(caps, 2).tolist(),
          "| risk cap:", round(risk_cap, 2))
    print()
    print(f"{'METHOD':<18} {'COUNT':>5} {'UTILITY':>10} {'VALUE':>9} {'RISK':>9}")
    for name, result in [
        ("Greedy", greedy),
        ("Previous Flower", previous_flower),
        ("CASR Shadow", casr),
        ("MILP optimum", exact),
    ]:
        print(f"{name:<18} {result['count']:>5} {result['objective']:>10.2f} "
              f"{result['value']:>9.1f} {result['risk']:>9.2f}")
    print()
    print("CASR runtime:", round(casr_seconds, 3), "seconds")
    print("CASR improvement over greedy:",
          round((casr["objective"] / greedy["objective"] - 1) * 100, 3), "%")
    print("CASR gap to MILP optimum:",
          round((exact["objective"] - casr["objective"]) / exact["objective"] * 100, 4), "%")
    print("CASR accepted objective path:", [round(x, 2) for x in casr_history])
    print("CASR resource utilization:",
          np.round(casr["resources"] / caps * 100, 2).tolist(), "%")
    print("CASR risk utilization:", round(casr["risk"] / risk_cap * 100, 2), "%")
    print("CASR final feasibility:", casr["feasible"])
    print("Dependencies satisfied:", casr["dependency_ok"])
    print("Conflicts avoided:", casr["conflicts_ok"])
    print("MILP status:", milp_result.message)
    print("MILP relative gap:", milp_result.get("mip_gap"))
    print("Note: synthetic instance, one seed; MILP is exact reference, CASR is heuristic.")


if __name__ == "__main__":
    main_casr()
