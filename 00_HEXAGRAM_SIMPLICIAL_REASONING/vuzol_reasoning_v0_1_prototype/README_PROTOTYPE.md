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
