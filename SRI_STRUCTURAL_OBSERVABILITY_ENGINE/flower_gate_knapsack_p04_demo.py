"""
Flower Gate demonstration on a published 0/1 knapsack benchmark (P04).

Source data:
- weights/profits: published table reproduced in the cited 2025 paper;
- capacity 50 and claimed optimum 107: classic P04 benchmark as listed
  in the cited GitHub benchmark README.
This script independently enumerates all 2^7 subsets and checks the result.

Flower Gate is used here as an auditable decision workflow, not claimed as a
new optimization algorithm:
State -> Pressure -> Shadow -> Generate(+3) -> Audit(-3) -> 9V -> Gate -> Bindu -> Memory
"""

from itertools import product

WEIGHTS = (31, 10, 20, 19, 4, 3, 6)
VALUES = (70, 20, 39, 37, 7, 5, 10)
CAPACITY = 50
NAMES = tuple(f"Item {i}" for i in range(1, 8))


def score(bits):
    weight = sum(w * b for w, b in zip(WEIGHTS, bits))
    value = sum(v * b for v, b in zip(VALUES, bits))
    return weight, value


def exact_search():
    feasible = []
    for bits in product((0, 1), repeat=len(WEIGHTS)):
        weight, value = score(bits)
        if weight <= CAPACITY:
            feasible.append((value, weight, bits))
    return sorted(feasible, reverse=True), len(feasible)


def greedy_by_value_density():
    order = sorted(
        range(len(WEIGHTS)),
        key=lambda i: VALUES[i] / WEIGHTS[i],
        reverse=True,
    )
    bits = [0] * len(WEIGHTS)
    used = 0
    for i in order:
        if used + WEIGHTS[i] <= CAPACITY:
            bits[i] = 1
            used += WEIGHTS[i]
    return tuple(bits), score(bits), order


def chosen_items(bits):
    return [i + 1 for i, bit in enumerate(bits) if bit]


def main():
    ranked, feasible_count = exact_search()
    greedy_bits, (gw, gv), order = greedy_by_value_density()
    best_value, best_weight, best_bits = ranked[0]

    print("STATE")
    print("weights:", WEIGHTS)
    print("values: ", VALUES)
    print("capacity:", CAPACITY)
    print()
    print("PRESSURE")
    print("constraint: total weight <= 50")
    print()
    print("GREEDY CANDIDATE")
    print("density order:", [i + 1 for i in order])
    print("items:", chosen_items(greedy_bits), "weight:", gw, "value:", gv)
    print()
    print("SHADOW")
    print("Greedy has weight slack", CAPACITY - gw,
          "but misses a better combination.")
    print("Greedy items 2, 5, 6 have weight 17 and value 32.")
    print("Replacing them with item 4 (weight 19, value 37)")
    print("increases total weight by 2 and total value by 5.")
    print()
    print("GENERATE (+3) / AUDIT (-3)")
    print("candidate items:", chosen_items(best_bits))
    print("candidate weight:", best_weight, "candidate value:", best_value)
    print("capacity check:", best_weight <= CAPACITY)
    print()
    print("EXACT ENUMERATION")
    print("subsets checked:", 2 ** len(WEIGHTS))
    print("feasible subsets:", feasible_count)
    print("top 3 (value, weight, items):")
    for value, weight, bits in ranked[:3]:
        print(value, weight, chosen_items(bits))
    print()
    print("9V / GATE")
    print("feasible:", best_weight <= CAPACITY)
    print("slack:", CAPACITY - best_weight)
    print("value gain over greedy:", best_value - gv)
    print("verdict: ALLOW for this deterministic benchmark")
    print("caution: zero slack; any weight increase would violate capacity")
    print()
    print("BINDU / MEMORY")
    print("commit candidate:", chosen_items(best_bits))
    print("record exact inputs, constraints, search count, and audit result")


if __name__ == "__main__":
    main()
