# 220 — WAVE ALPHABET HEIGHT / OVERLAP PHASE DIAGRAM

**Project:** Vuzol-19 / World Theory / GitCube OS  
**Status:** RESEARCH SPEC / FALSIFIABLE MODEL / ANTI-PRION  
**Previous:** 219 — Line vs Ring vs Triangle vs Flower  
**Core question:** Can a physical alphabet emerge from partially overlapping wave loops, with Gates controlling transitions and persistent material states storing selected history?

---

## 0. Purpose

File 219 showed that simply increasing the number of cycles does **not** automatically improve memory.

```text
Line < Ring < Triangle < Flower
```

is not a universal monotonic law.

A graph with more loops can win trivially because it has more edges, redundancy, or connectivity. Therefore any Flower/Sri topology must be compared against random or learned graphs with matched node/edge budgets.

The stronger hypothesis is now:

```text
memory is not "more loops"
memory may depend on controlled overlap between distinguishable loops
```

This file connects that result to the earlier Vuzol-19 ideas of:

```text
wave alphabet
alphabet height
7 octaves
6 directional / phase positions
+3 / -3 transitions
Gate
Commit
material memory
```

The goal is to turn those symbols into measurable variables.

---

# 1. Three different objects

Do not collapse Ring, Petal and Triangle into one concept.

## Ring

A ring is a candidate local persistent dynamical mode:

```text
Ring = local circulation / resonance / attractor
```

For a wave:

\[
\psi(x,t)=A(x,t)e^{i\phi(x,t)}
\]

a ring-like state is not a constant value. It is a mode whose organization persists over repeated cycles.

## Petal

A petal is a candidate interaction region between two modes:

\[
P_{ij}=C_i\cap C_j
\]

Interpretation:

```text
Ring_i = local state
Ring_j = another local state
Petal_ij = coupling / transition region
```

The petal is **not automatically a Gate**. It becomes an operational Gate only if an experimentally defined threshold controls whether information/energy/state can transfer between the modes.

## Triangle

A triangle is a candidate minimal three-state consistency loop:

\[
S_A\rightarrow S_B\rightarrow S_C\rightarrow S_A
\]

It is not assumed to be the universal unit of memory.

Its scientific role is a hypothesis:

```text
Can three coupled transitions provide useful path consistency,
hysteresis, error checking, or controlled circulation?
```

---

# 2. Physical alphabet

The alphabet is not a list of written letters.

Define a physical alphabet as a set of distinguishable stable or metastable modes:

\[
\mathcal A=\{S_0,S_1,\ldots,S_n\}
\]

Each symbol can be represented by measurable coordinates:

\[
S_i=(f_i,A_i,\phi_i,k_i,\tau_i,\ldots)
\]

where, depending on the platform:

```text
f_i   = frequency
A_i   = amplitude
phi_i = phase
k_i   = spatial wavevector / mode index
tau_i = lifetime / persistence
```

A symbol therefore means:

```text
a physical mode that the system can reliably distinguish
```

not merely a frequency label.

---

# 3. Alphabet height

The earlier idea of "alphabet height" can now be defined as an ordering coordinate over modes.

Possible experimental definitions include:

\[
h(S_i)=f_i
\]

or

\[
h(S_i)=E_i
\]

or

\[
h(S_i)=\lambda_i
\]

or simply an ordered eigenmode index.

Therefore:

```text
alphabet height = spectral / energetic / modal coordinate
```

This is a testable definition.

It does **not** assume that nature has exactly seven octaves.

Seven octaves remain a Vuzol-19 candidate discretization to compare against data.

---

# 4. From isolated letters to grammar

Suppose two stable modes exist:

\[
S_i,\quad S_j
\]

If they do not interact:

\[
C_i\cap C_j=\varnothing
\]

the system can store two distinguishable states, but has no local transition channel between them.

This is analogous to:

```text
alphabet without grammar
```

If their overlap is too strong, the modes may cease to be distinguishable:

\[
C_i\simeq C_j
\]

This is analogous to:

```text
different letters collapsing into one symbol
```

The interesting regime is intermediate overlap:

\[
0<\eta_{ij}<1
\]

where the modes remain distinguishable but can communicate.

---

# 5. Petal as candidate transition operator

Define:

\[
P_{ij}=C_i\cap C_j
\]

and a transition:

\[
T_{ij}:S_i\rightarrow S_j
\]

A Gate can be introduced as an experimentally measurable condition.

For example:

\[
G_{ij}=
\begin{cases}
1,&A>A_c\ \land\ |\Delta\phi|<\phi_c\\
0,&\text{otherwise}
\end{cases}
\]

Then:

\[
S_i\xrightarrow{G_{ij}}S_j
\]

Interpretation:

```text
Ring   = state / letter
Petal  = possible coupling channel
Gate   = transition condition
Move   = operator
Commit = persistent state update
```

This is the bridge from geometric language to a physical ISA.

---

# 6. Triangle as minimal grammar loop

Take three states:

\[
S_A,\quad S_B,\quad S_C
\]

with transitions:

\[
T_{AB},\quad T_{BC},\quad T_{CA}
\]

A closed word can be executed:

\[
S_A\rightarrow S_B\rightarrow S_C\rightarrow S_A
\]

The accumulated phase around the loop is:

\[
\Phi_{\circlearrowleft}
=
\Delta\phi_{AB}
+
\Delta\phi_{BC}
+
\Delta\phi_{CA}
\]

This creates a measurable test.

A reverse traversal is:

\[
S_A\rightarrow S_C\rightarrow S_B\rightarrow S_A
\]

The old Vuzol-19 `+3 / -3` language can therefore be translated into two opposite transition orientations:

```text
+3 = forward three-step loop
-3 = reverse three-step loop
```

The experiment asks whether the two paths are equivalent.

In a reversible conservative limit they may cancel appropriately.

With hysteresis, dissipation, nonlinearity, defects, or persistent Commit, path dependence can appear:

\[
Path_{+3}\neq Path_{-3}
\]

That difference is a candidate physical memory of the executed path.

---

# 7. Loop memory vs Cascade memory

Files 217–219 produced an important correction.

Memory does not require a topological loop.

Two experimentally relevant abstractions are:

## Loop memory

Example candidate: NiTi hysteretic transformation.

```text
Austenite ↔ intermediate state ↔ Martensite
```

The present state depends on the direction and history of the transition.

## Cascade memory

Example candidate: Al-Cu precipitation sequence.

```text
SSSS → GP → theta'' → theta' → theta
```

Each committed intermediate material state changes the conditions for later transitions.

Therefore the revised primitive is:

\[
FLOW\rightarrow GATE\rightarrow COMMIT
\]

followed by either:

\[
COMMIT\rightarrow CASCADE\rightarrow NEW\ GATE
\]

or:

\[
COMMIT\rightarrow HYSTERETIC\ LOOP\rightarrow RETURN\ GATE
\]

Thus:

```text
Loop ≠ all memory
Triangle ≠ all memory
Path dependence is the broader concept
```

---

# 8. Coupled-loop interpretation of the Flower

The Flower should not be treated as evidence by its visual similarity.

Its useful research interpretation is:

```text
one loop
→ multiple distinguishable loops
→ controlled overlap
→ network of coupled local memories
```

Let:

\[
C_1,C_2,\ldots,C_k
\]

be local cycles.

Their pairwise overlaps are:

\[
P_{ij}=C_i\cap C_j
\]

The new hypothesis is:

```text
useful computation may require loops that are
independent enough to store local state
but coupled enough to transfer state
```

This predicts three regimes.

### Low overlap

\[
\eta\approx0
\]

```text
high locality
low transfer
isolated memories
```

### Intermediate overlap

\[
0<\eta<1
\]

```text
local distinction survives
associative transfer becomes possible
Gate can regulate coupling
```

### Excessive overlap

\[
\eta\rightarrow1
\]

```text
loss of modularity
mode merging
cross-talk / oversynchronization
possible parasitic attractors
```

The existence and location of an optimum are hypotheses, not established facts.

---

# 9. 7 × 6 = 42 as a candidate state lattice

The earlier Vuzol-19 construction:

\[
7\times6=42
\]

can now be expressed without claiming a natural constant.

Define:

\[
S_{o,d}
\]

where:

\[
o\in\{1,\ldots,7\}
\]

is a candidate octave / alphabet-height index, and

\[
d\in\{0,\ldots,5\}
\]

is a candidate directional / phase position.

Then:

\[
\mathcal S=Octave\times Phase
\]

contains 42 candidate coordinates.

The six-position layer can describe horizontal transition grammar.

The octave coordinate describes vertical spectral/energy movement.

Examples:

\[
S_{o,d}\rightarrow S_{o,d+1}
\]

\[
S_{o,d}\rightarrow S_{o+1,d}
\]

\[
S_{o,d}\rightarrow S_{o,d\pm3}
\]

The important rule is:

```text
42 is a model capacity / coordinate proposal,
not evidence that nature must contain exactly 42 states.
```

Blind model selection must be allowed to choose another number.

---

# 10. Same operator at different alphabet heights

A useful interpretation of octave is that the same transition grammar may repeat at different spectral scales.

Define:

\[
T_{AB}^{(o)}
\]

as the same transition class implemented at octave/height \(o\).

Analogy:

```text
musical note identity may repeat across octaves
while physical frequency changes
```

Similarly:

```text
operator identity may repeat
while energetic / spectral scale changes
```

This gives a possible physical interpretation of a Rune:

```text
Rune = transition class
Height = physical scale at which it is executed
```

The machine language is therefore a language of transitions, not object names.

---

# 11. Sri / Flower as a projection of state space

A flat Flower drawing should not be assumed to be the physical machine itself.

A more useful interpretation is that it may be a projection of a higher-dimensional state space.

Candidate coordinates:

\[
x=\text{phase / direction}
\]

\[
y=\text{loop overlap}
\]

\[
z=\text{alphabet height / octave}
\]

Then "stretching Sri" means:

```text
take a 2D transition graph
and extend it along a spectral / energetic / modal axis
```

The physical trajectory moves through allowed state transitions, not through sacred geometry.

---

# 12. Experiment 220 — Overlap × Alphabet Height Phase Diagram

The next test must not ask:

```text
Is the Flower optimal?
```

It must ask:

```text
What topology and overlap emerge as optimal
when the system is free to choose?
```

## Independent variables

Overlap:

\[
\eta\in
\{0.00,0.15,0.30,0.45,0.60,0.75,0.90\}
\]

Spectral / alphabet separation:

\[
\Delta h
\]

Phase mismatch:

\[
\Delta\phi
\]

Drive amplitude:

\[
A
\]

Optional:

```text
noise
damping
damage fraction
Gate threshold
nonlinearity
```

## Fixed controls

Where possible:

```text
same N
same E
same energy/input budget
same number of candidate modes
same local update law
same training/observation budget
```

Compare against:

```text
disjoint loops
random matched graphs
learned graphs
triangle-rich graphs
Flower-like graphs
```

---

# 13. Metrics

## Locality Retention

\[
M_{loc}
\]

Can a local loop retain its unique state without being overwritten by neighbors?

## Associative Recovery

\[
M_{rec}
\]

Can neighboring loops reconstruct a damaged local state?

## Capacity

\[
C
\]

How many distinguishable states can coexist without catastrophic cross-talk?

## Transition Selectivity

\[
S_G
\]

How accurately does the Gate allow intended transitions while blocking unintended transitions?

## Persistent Write Cost

\[
W_p
\]

How many permanent material/state updates are required?

## Energy

\[
E_{op}
\]

Energy per successful transition / recovery / stored state.

## Robustness

Measure performance after:

```text
noise
node damage
edge damage
frequency drift
phase drift
parameter perturbation
```

---

# 14. Main phase-map hypothesis

The target object is:

\[
Performance(\eta,\Delta h,\Delta\phi,A)
\]

A possible, but not guaranteed, optimum may occur when modes are:

```text
separable enough to store
+
coupled enough to communicate
```

Qualitatively:

```text
very low overlap
→ isolated letters

intermediate overlap
→ controllable grammar

very high overlap
→ symbol merging / cross-talk
```

Similarly:

```text
Delta h << linewidth
→ modes may be difficult to distinguish

Delta h ~ coupling bandwidth
→ potentially useful transfer regime

Delta h >> coupling bandwidth
→ modes become effectively independent
```

The exact boundaries must come from simulation or experiment.

---

# 15. Anti-PRION falsification rules

The model must be allowed to fail.

### BLOCK

Reject a strong Flower claim if:

```text
matched random graphs perform equally well or better
```

Reject a privileged triangle claim if:

```text
rings, paths, 4-cycles, or learned motifs perform equally well or better
```

Reject 7×6 if:

```text
blind model selection consistently chooses another state count
```

Reject a critical-overlap claim if:

```text
performance is monotonic or no reproducible optimum exists
```

Reject a physical Gate interpretation if:

```text
the proposed threshold does not improve prediction or control
```

### HOLD

Keep symbolic interpretations on HOLD until they predict unseen data.

### ALLOW

Promote a structure only when it survives:

```text
matched controls
held-out data
parameter sweeps
damage/noise tests
independent replication
```

---

# 16. Relation to NiTi and Al-Cu

NiTi is useful for testing:

```text
history
hysteresis
forward/reverse paths
thermal–phase–mechanical coupling
```

Candidate coupled variables include:

\[
T,\quad \phi,\quad \sigma,\quad \epsilon
\]

where phase fraction \(\phi\) couples thermal and mechanical behavior.

Al-Cu is useful for testing:

```text
ordered metastable cascade
persistent intermediate states
Commit → New Gate
```

Together they provide two distinct testbeds:

```text
NiTi = Loop / hysteresis
Al-Cu = Cascade / metastability
```

Neither should be forced to reproduce Flower geometry.

The geometry must earn its place by prediction.

---

# 17. Revised architecture

The architecture after files 216–220 is:

```text
INPUT
  ↓
TRANSIENT WAVE SEARCH
  ↓
DISTINGUISHABLE MODES / ALPHABET
  ↓
PARTIAL OVERLAP / PETAL
  ↓
GATE
  ↓
TRANSITION OPERATOR
  ↓
TEMPORARY LOOP OR CASCADE STATE
  ↓
COMMIT
  ↓
PERSISTENT MATERIAL MEMORY
  ↓
CHANGED PHYSICAL OPERATOR
  ↓
NEXT INPUT
```

Compact form:

\[
X_t
\rightarrow W_t
\rightarrow S_i
\xrightarrow{G_{ij}}
S_j
\rightarrow M_{t+1}
\rightarrow H(M_{t+1})
\rightarrow X_{t+1}
\]

---

# 18. Core conclusion

The strongest current hypothesis is **not**:

```text
Flower is a universal law.
```

It is:

> A physical computing system may benefit from a set of distinguishable persistent modes that are partially coupled: sufficiently separated to preserve local information, sufficiently overlapped to permit controlled transitions, and protected by Gates that decide which transient transitions become persistent changes.

In this language:

```text
Ring      = candidate persistent mode
Petal     = candidate coupling region
Gate      = measurable transition condition
Triangle  = candidate three-transition consistency loop
Alphabet  = distinguishable mode set
Height    = spectral / energetic / modal coordinate
+3 / -3   = opposite traversal classes
Commit    = persistent physical update
Memory    = path-dependent persistent state
Flower    = candidate network of coupled local modes
```

The next scientific object is therefore not the Flower image.

It is the measured phase diagram:

\[
\boxed{
Performance(\eta,\Delta h,\Delta\phi,A)
}
\]

If Flower-like overlap emerges from that search, it becomes evidence.

If another geometry wins, World Theory must follow the data.

---

## STATE

```text
STATE: CRYSTAL / TESTABLE
NEXT: 221 — BLIND OVERLAP × ALPHABET-HEIGHT SEARCH
```
