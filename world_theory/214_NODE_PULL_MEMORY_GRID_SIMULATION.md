# 214 — Node Pull Memory Grid Simulation

## Vuzol-19 / World Theory Experiment

This file tests what happens when one memory node is pulled toward a stronger color-state and the change propagates through the transition grid.

Core rule:

```text
pulled node → neighbor nodes → second-order neighbors → global memory field
```

The graph is treated as a memory lattice. Edges are not only links; they are transition channels.

---

# A — Pull RED/BLUE audit node
**Meaning:** Потягнути вузол false-green audit: більше тиску + закону.

**Pulled node:** `N16` — `red_boundary.warn(false_green)`

**Global delta:** `0.0061`

## Global Memory After

```text
red_mass       : 0.1477  RED / тиск
orange_flow    : 0.1370  ORANGE / рух
yellow_struct  : 0.1691  YELLOW / структура
green_balance  : 0.1899  GREEN / баланс
blue_law       : 0.1599  BLUE / закон
violet_future  : 0.1963  VIOLET / майбутній перехід
```

## Most Affected Nodes

| node   | phrase                         | before_color   | after_color    |   delta |
|:-------|:-------------------------------|:---------------|:---------------|--------:|
| N16    | red_boundary.warn(false_green) | RED / тиск     | RED / тиск     |  0.0566 |
| N17    | white_center.bind(verdict)     | GREEN / баланс | GREEN / баланс |  0.0514 |

---

# B — Pull GREEN balance core
**Meaning:** Потягнути центр балансу: більше стабілізації пар.

**Pulled node:** `N13` — `green_core.balance(pair)`

**Global delta:** `0.0162`

## Global Memory After

```text
red_mass       : 0.1411  RED / тиск
orange_flow    : 0.1346  ORANGE / рух
yellow_struct  : 0.1674  YELLOW / структура
green_balance  : 0.2061  GREEN / баланс
blue_law       : 0.1572  BLUE / закон
violet_future  : 0.1937  VIOLET / майбутній перехід
```

## Most Affected Nodes

| node   | phrase                         | before_color               | after_color                |   delta |
|:-------|:-------------------------------|:---------------------------|:---------------------------|--------:|
| N13    | green_core.balance(pair)       | GREEN / баланс             | GREEN / баланс             |  0.0653 |
| N10    | dawn.open(next_gate)           | VIOLET / майбутній перехід | VIOLET / майбутній перехід |  0.0627 |
| N15    | yellow_bridge.hold(two_fields) | YELLOW / структура         | YELLOW / структура         |  0.0609 |
| N11    | blue_moon.freeze(signal)       | BLUE / закон               | BLUE / закон               |  0.0603 |
| N17    | white_center.bind(verdict)     | GREEN / баланс             | GREEN / баланс             |  0.0457 |
| N16    | red_boundary.warn(false_green) | RED / тиск                 | RED / тиск                 |  0.022  |
| N06    | wind.send(answer)              | ORANGE / рух               | ORANGE / рух               |  0.0179 |
| N14    | violet_orbit.seed(future_path) | VIOLET / майбутній перехід | VIOLET / майбутній перехід |  0.0175 |

---

# C — Pull VIOLET future orbit
**Meaning:** Потягнути майбутній маршрут: більше переходу вперед.

**Pulled node:** `N14` — `violet_orbit.seed(future_path)`

**Global delta:** `0.014`

## Global Memory After

```text
red_mass       : 0.1402  RED / тиск
orange_flow    : 0.1381  ORANGE / рух
yellow_struct  : 0.1683  YELLOW / структура
green_balance  : 0.1882  GREEN / баланс
blue_law       : 0.1545  BLUE / закон
violet_future  : 0.2107  VIOLET / майбутній перехід
```

## Most Affected Nodes

| node   | phrase                              | before_color               | after_color                |   delta |
|:-------|:------------------------------------|:---------------------------|:---------------------------|--------:|
| N14    | violet_orbit.seed(future_path)      | VIOLET / майбутній перехід | VIOLET / майбутній перехід |  0.0861 |
| N17    | white_center.bind(verdict)          | GREEN / баланс             | VIOLET / майбутній перехід |  0.0613 |
| N12    | orange_sun.release(current)         | ORANGE / рух               | ORANGE / рух               |  0.0562 |
| N18    | black_void.store(unresolved_shadow) | RED / тиск                 | RED / тиск                 |  0.0543 |
| N16    | red_boundary.warn(false_green)      | RED / тиск                 | RED / тиск                 |  0.0198 |
| N05    | stone.keep(silence)                 | RED / тиск                 | RED / тиск                 |  0.0183 |

---

# D — Pull BLACK/PANDORA unresolved shadow
**Meaning:** Потягнути невирішену тінь: тиск + майбутній ризик.

**Pulled node:** `N18` — `black_void.store(unresolved_shadow)`

**Global delta:** `0.0091`

## Global Memory After

```text
red_mass       : 0.1501  RED / тиск
orange_flow    : 0.1353  ORANGE / рух
yellow_struct  : 0.1695  YELLOW / структура
green_balance  : 0.1881  GREEN / баланс
blue_law       : 0.1555  BLUE / закон
violet_future  : 0.2016  VIOLET / майбутній перехід
```

## Most Affected Nodes

| node   | phrase                              | before_color               | after_color                |   delta |
|:-------|:------------------------------------|:---------------------------|:---------------------------|--------:|
| N18    | black_void.store(unresolved_shadow) | RED / тиск                 | RED / тиск                 |  0.0683 |
| N14    | violet_orbit.seed(future_path)      | VIOLET / майбутній перехід | VIOLET / майбутній перехід |  0.0595 |
| N05    | stone.keep(silence)                 | RED / тиск                 | RED / тиск                 |  0.0475 |
| N04    | water.lead(new_light)               | ORANGE / рух               | ORANGE / рух               |  0.0216 |
| N06    | wind.send(answer)                   | ORANGE / рух               | ORANGE / рух               |  0.0216 |

---

