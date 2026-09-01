# Local Repair Scaling Report

**Project:** Vuzol-19 / Hexagram Simplicial Reasoning  
**Experiment:** Balanced ternary tree, one changed leaf  
**State:** MEASURED PROTOTYPE RESULT

## Question

How many internal nodes must be recomputed after one local leaf changes?

Compare:

```text
naive full restart:
recompute every internal node

local repair:
recompute only ancestors of the changed leaf
```

## Results

| Leaves | Depth | Full Internal Nodes | Local Recompute | Saved | Recompute Fraction | Node-Count Ratio |
|---:|---:|---:|---:|---:|---:|---:|
| 27 | 3 | 13 | 3 | 10 | 23.08% | 4.33x |
| 81 | 4 | 40 | 4 | 36 | 10.00% | 10.00x |
| 243 | 5 | 121 | 5 | 116 | 4.13% | 24.20x |
| 729 | 6 | 364 | 6 | 358 | 1.65% | 60.67x |

## Observed scaling

For a full balanced ternary tree with `N` leaves:

```math
I(N) = \frac{N-1}{2}
```

internal nodes.

For one isolated leaf change, the prototype recomputes exactly one ancestor per level:

```math
R(N) = \log_3 N
```

for tested exact powers of three.

Measured sequence:

```text
27  leaves -> 3 internal recomputations
81  leaves -> 4
243 leaves -> 5
729 leaves -> 6
```

At `729` leaves:

```text
full internal recomputation = 364 nodes
local repair = 6 nodes
recompute fraction = 1.65%
node-count ratio = 60.67x
```

## Important limitation

This does **not** prove that arbitrary AI reasoning becomes `O(log N)`.

The result holds for this controlled case:

```text
balanced ternary hierarchy
one isolated changed leaf
no extra cross-branch invalidation
constant-cost local recomputation
```

Dense cross-branch coupling can increase the affected region substantially.

Therefore the next experiment should vary:

```text
cross-edge density
number of simultaneous local errors
tree imbalance
shared DAG dependencies
```

## Verdict

```text
MEASURED:
local ancestor-path repair scales with tree depth
in this deterministic balanced-tree prototype.

NOT YET ESTABLISHED:
the same scaling advantage for realistic LLM reasoning graphs.
```
