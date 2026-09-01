# Vuzol-19 Deterministic Prototype

This is the first executable prototype for the
`00_HEXAGRAM_SIMPLICIAL_REASONING` specification.

Implemented:

```text
ReasoningNode
Edge
Triad
ReasoningGraph
+3 Forward
ShadowStore
-3 Backward
Gate
Metrics
local error repair demo
```

Not implemented yet:

```text
Bindu / MemoryAtom persistence
recursive multi-level tree runtime
LLM adapter
GSL 6D
Hexagram controller
14/10/10/8 funnel
GSM-Infinity adapter
```

## Run tests

```bash
pytest -q
```

## Run demo

```bash
python examples/local_error_repair_demo.py
```

Expected behavior:

```text
healthy candidate -> ALLOW
corrupted critical edge -> HOLD / EXPAND
local repair -> ALLOW
```

The prototype intentionally starts with a deterministic control core.


## v0.2 recursive hierarchy

Added:

```text
recursive.py
27-leaf balanced ternary tree
27 -> 9 -> 3 -> 1
ancestor invalidation
bottom-up local recomputation
parent-value audit
```

Run:

```bash
python examples/recursive_27_node_demo.py
```

Key expected behavior:

```text
corrupted internal parent
-> -3 detects PARENT_VALUE_MISMATCH
-> Gate HOLD

single leaf update
-> exactly 3 ancestors become stale
-> exactly those 3 internal nodes are recomputed
-> unrelated branches are untouched
```
