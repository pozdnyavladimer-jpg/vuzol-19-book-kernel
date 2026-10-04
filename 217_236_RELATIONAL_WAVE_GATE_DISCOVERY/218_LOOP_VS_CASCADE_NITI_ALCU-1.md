# 218 — LOOP VS CASCADE: NiTi / Al-Cu

**Status:** PHYSICAL ANALOGY + SYNTHETIC PATH-MEMORY TEST  
**Project:** Vuzol-19 / World Theory

## 0. Question

If memory does not require a graph cycle, can two different physical architectures retain history:

1. a hysteretic loop;
2. an ordered transformation cascade?

## 1. Two abstractions

### NiTi-like hysteretic route

A simplified phase-path abstraction:

`B2 ↔ R ↔ B19'`

The important feature is not the exact phase diagram but path dependence: the current observable state can depend on the route by which the system arrived there.

Candidate grammar:

`FLOW → GATE → COMMIT → HYSTERETIC LOOP → RETURN GATE`

### Al–Cu-like cascade

Simplified precipitation sequence:

`SSSS → GP zones → θ'' → θ' → θ (Al2Cu)`

This is not naturally represented as one closed return loop. History is retained by ordered state transformation.

Candidate grammar:

`FLOW → GATE → COMMIT → CASCADE → NEW GATE`

## 2. Synthetic benchmark

Two deliberately simplified recognition tasks were used to ask whether the path/history variable matters.

### NiTi-like task

- memoryless state recognition: `0.862`
- loop/path-aware recognition: `1.000`

### Al–Cu-like task

- shortcut / order-insensitive model: `0.310`
- ordered cascade model: `1.000`

These values belong to the synthetic abstraction, not to measured alloy accuracy.

## 3. Result

Both architectures can encode history.

Therefore:

`memory ≠ loop only`

and

`history dependence` is more general than `closed topology`.

## 4. Turning point

Experiment 217 removed the universal requirement for a cycle.

218 made the alternative explicit:

`COMMIT → LOOP`

or

`COMMIT → CASCADE`.

This means that a Flower/triangle architecture cannot be justified merely by saying that it contains cycles. It must outperform appropriate controls.

That becomes experiment 219.

## 5. Verdict

**ALLOW**
- hysteretic loops as one form of path memory;
- ordered cascades as another form of path memory.

**HOLD**
- specific material phases as analogies for the Vuzol-19 transition grammar.

**BLOCK**
- universal loop requirement;
- claim that a triangle is the minimum universal physical memory unit.

## 6. Next

`219 — Line / Ring / Triangle / Flower topology control`
