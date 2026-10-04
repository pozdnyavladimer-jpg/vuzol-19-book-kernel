# 217 — MATERIAL STATE / MEMORY / TOPOLOGY

**Status:** RECONSTRUCTED FROM THE 217→220 EXPERIMENT CHAIN  
**Project:** Vuzol-19 / World Theory  
**Role:** physical-memory boundary test

## 0. Question

Does physical memory require a closed graph cycle, or can the material state itself preserve history?

## 1. Working model

A physical system can be represented as

`Wave/Input → Gate → Current/Action → Material Change → Boundary/Memory → Next Wave`

The important correction is:

`Current ≠ persistent memory`

Current is closer to action/commit. Persistent memory is carried by a changed material/boundary state when that state modifies later transitions.

A minimal closed update is

`Y_t = H_t(X_t)`

`G_t = G(Y_t, M_t, C_t)`

`I_t = I(Y_t)` if Gate allows the transition, otherwise `0`

`M_(t+1) = F(M_t, I_t)`

`H_(t+1) = H(M_(t+1))`

Thus the next input is processed by a physically changed operator.

## 2. Main test

Compare the claim

`memory requires a graph loop`

against known classes of history-dependent state:

- hysteresis;
- irreversible material transformation;
- defects;
- composition / phase history;
- path-dependent barriers and transition temperatures.

These mechanisms can retain information even when the abstract interaction graph is not a closed cycle.

## 3. Result

The universal identification

`cycle = memory`

does not survive.

A cycle can participate in memory, but topology alone is insufficient. Memory can be stored in the state variables and irreversible/history-dependent transition law.

## 4. Turning point

Before 217 the tempting picture was:

`closed path → retained state → memory`.

After 217 the safer formulation became:

`history-dependent state → changed future transition → memory`.

This opened the next question: if a loop is not mandatory, what is the difference between hysteretic loops and ordered transformation cascades?

That becomes experiment 218.

## 5. Verdict

**ALLOW**
- history-dependent material state as physical memory;
- hysteresis and irreversible transformation as memory mechanisms;
- changed material/boundary state changing future response.

**HOLD**
- cycles as one useful memory architecture.

**BLOCK**
- every graph cycle is memory;
- nonzero cycle rank is required for physical memory;
- topology alone proves memory.

## 6. Next

`218 — Loop vs Cascade: NiTi / Al-Cu`
