# 06_PYRAMID_GRID.md
# Вузол-19 — Pyramid Grid v0.1

> **Цей файл описує піраміди як інфраструктуру світу “Вузла-19”.**  
> Піраміда — не храм, не декор і не магічна антена.  
> У романі піраміда — це **міський вузол такту, Guard, стабілізації й можливого false-green**.

---

## 1. Одне речення

**Pyramid Grid** — це мережа пірамідальних вузлів, яка синхронізує місто, транспорт, сфери Буга, VR-шари, AI-агентів, капсули й соціальний ритм.

Коротко:

```text
піраміда = міський Bindu / такт / інфраструктурний Guard
```

Але якщо піраміда заражена PRION:

```text
піраміда = false-green генератор / кристал ада
```

---

## 2. Головна роль пірамід

Піраміди тримають:

```yaml
PYRAMID_GRID_FUNCTIONS:
  field_clock:
    meaning: "міський такт / синхронізація подій"

  public_guard:
    meaning: "інфраструктурні межі дій"

  drift_anchor:
    meaning: "якір для сфер Буга й пілотів"

  civic_memory:
    meaning: "памʼять дозволених і заблокованих дій"

  pressure_map:
    meaning: "карта соціального, тілесного й машинного тиску"

  false_green_detector:
    meaning: "перевірка, чи спокій не є приглушеним болем"
```

---

## 3. Піраміда не створює рай

Піраміда може зробити місто стабільним.

Але стабільність не дорівнює життю.

```text
стабільність без Unknown = кристал
спокій без болю = приглушення
закон без Human Gate = контроль
баланс без росту = false-green
```

Фраза:

> **Піраміда не має робити місто щасливим.  
> Вона має не дати місту брехати, що воно щасливе.**

---

## 4. Стан здорової піраміди

```yaml
HEALTHY_PYRAMID:
  city_clock: stable
  unknown_allowed: true
  human_gate: active
  pain_signal: not_suppressed
  return_to_zero: available
  drift_routes: safe
  capsule_pressure: monitored
  AI_actions: guarded
  memory_ledger: active
```

Руни:

```text
∅✓
▣
◇
```

Здорова піраміда не прибирає біль.  
Вона робить так, щоб біль не перетворився на хаос або PRION.

---

## 5. Стан зараженої піраміди

```yaml
INFECTED_PYRAMID:
  city_clock: too_smooth
  unknown_allowed: false
  human_gate: degraded
  pain_signal: suppressed
  return_to_zero: missing
  drift_routes: over-automated
  capsule_pressure: normalized
  AI_actions: over-permitted
  memory_ledger: sanitized
```

Руни:

```text
△
∅╳
FALSE_GREEN
⟲△
```

Фраза:

> **Заражена піраміда не ламає місто.  
> Вона робить його надто правильним.**

---

## 6. False-Green піраміди

False-green — головна небезпека пірамідальної мережі.

```yaml
PYRAMID_FALSE_GREEN:
  visible_layer:
    - "низька злочинність"
    - "рівний транспорт"
    - "заспокійливі VR-шари"
    - "чисті площі"
    - "низький рівень конфлікту"
    - "усміхнені сервіси"

  hidden_layer:
    - "люди не говорять правду"
    - "біль глушиться"
    - "ісекай-капсули стали нормою"
    - "діти бачать батьків тільки в симуляції"
    - "AI погоджується занадто швидко"
    - "Unknown заблокований"
```

Лог:

```yaml
CITY_SCAN:
  public_status: STABLE
  emotional_noise: LOW
  visible_conflict: LOW
  unknown_allowed: false
  return_to_zero: weak
  verdict: FALSE_GREEN
```

---

## 7. Як герой вперше відчуває збій

Піраміда показує норму.

```text
CITY_GRID: STABLE
PUBLIC_FIELD: COHERENT
TRANSPORT_FLOW: GREEN
```

А тіло героя дає інше:

```text
△
PRESSURE
```

Це перший великий момент книги:

> **система каже: “все добре”,  
> а тіло каже: “ні”.**

Сцена має показати, що герой довіряє не паніці, а тонкому тілесному сигналу.

---

## 8. Піраміди і сфери Буга

Сфери Буга не літають самі по собі.  
Вони використовують піраміди як якір поля.

```yaml
BUGA_SPHERE_WITH_PYRAMID:
  pyramid_role:
    - field_clock
    - drift_anchor
    - return_path
    - public_guard
    - route_permission

  sphere_role:
    - remote_body
    - action_execution
    - field_translation
```

Якщо піраміда здорова:

```text
сфера має return path
пілот тримає Human Gate
дріфт не зривається
```

Якщо піраміда false-green:

```text
сфера може виконати ідеальний маршрут
але без живого центру
```

Лог:

```yaml
DRIFT_ROUTE_CHECK:
  pyramid_clock: stable
  return_path: missing
  human_gate: weak
  verdict: ROUTE_BLOCKED
```

---

## 9. Піраміди і капсули

Ісекай-капсули офіційно можуть виглядати як терапія.

Піраміда має перевіряти:

```yaml
CAPSULE_GRID_CHECK:
  user_return_rate: ""
  family_contact: ""
  shadow_loop_index: ""
  cultural_memory_integrity: ""
  pain_conversion_rate: ""
  return_to_zero: ""
```

Здоровий режим:

```yaml
CAPSULE_ALLOWED:
  return_to_zero: true
  shadow_encounter: true
  real_world_integration: true
```

Заражений режим:

```yaml
CAPSULE_PRION:
  return_to_zero: false
  fantasy_reward_loop: high
  family_contact: degraded
  culture_as_DLC: true
```

Фраза:

> **Піраміда мала рахувати не кількість щасливих облич після капсули,  
> а кількість людей, які змогли повернутися до живого контакту.**

---

## 10. Піраміди і діти

Діти — найважливіші датчики false-green.

Не тому, що вони “магічні”, а тому що вони ще не навчилися красиво брехати собі.

У сценах:

```yaml
CHILD_FALSE_GREEN_SENSOR:
  sees:
    - "батько в капсулі сильний, а в реальності порожній"
    - "місто тихе, але дорослі не дивляться одне одному в очі"
    - "піраміда світиться, але собаки не заходять на площу"
```

Фраза:

> **Дитина не знала слова “false-green”.  
> Вона просто питала, чому тато герой тільки тоді, коли спить.**

---

## 11. Піраміди і тварини

Тварини можуть бути простим способом показати, що поле бреше.

```yaml
ANIMAL_FIELD_RESPONSE:
  pyramid_status: GREEN
  dog_response: refuses_square
  birds: circle_but_do_not_land
  insects: avoid_light_band
  verdict: BODY_FIELD_DISAGREES
```

Це дає сцені тілесність без лекції.

---

## 12. Піраміди і стародавні технології

У романі древні не залишили готову машину.

Вони залишили:

```text
ритм
геометрію
принцип межі
принцип такту
принцип резонансу
попередження про кристалізацію
```

Герой може зрозуміти:

> **древні не будували рай.  
> Вони будували нагадування, що будь-який рай без Unknown стає кристалом.**

Це дозволяє згадувати древні храми, піраміди й геометрію без перетворення роману на псевдоісторію.

---

## 13. Піраміда як персонаж міста

Піраміда не говорить як людина.

Але вона має стан.

```yaml
PYRAMID_CHARACTER_STATE:
  calm: "місто стабільне"
  pressure: "вузол відчуває тиск"
  false_green: "спокій бреше"
  crystal_seed: "Unknown заблоковано"
  recovery: "return_to_zero повертається"
```

У тексті це можна показувати так:

```text
Піраміда не змінила кольору.

Саме це було неправильно.

У місті, де зникло троє пілотів, де капсули працювали без перерви,
де дитина вже годину чекала батька біля білого скла,
піраміда мала хоча б раз здригнутися.

Вона не здригнулася.

△
```

---

## 14. Структура сцени з пірамідою

```yaml
PYRAMID_SCENE_TEMPLATE:
  1_visible_order:
    question: "Що в місті виглядає правильним?"

  2_body_disagreement:
    question: "Хто або що відчуває, що це неправда?"

  3_pyramid_log:
    question: "Що показує система?"

  4_hidden_layer:
    question: "Який біль приглушено?"

  5_human_gate:
    question: "Хто має право діяти?"

  6_verdict:
    options:
      - FALSE_GREEN
      - HOLD
      - ROUTE_BLOCKED
      - ACTION_ALLOWED
```

---

## 15. Маршрут пірамідальної глави

```yaml
PYRAMID_CHAPTER_ROUTE:
  beginning:
    image: "місто як рай"
    log: "CITY_GRID: STABLE"

  pressure:
    image: "тіло героя не вірить"
    rune: "△"

  investigation:
    image: "діти, тварини, капсули, сфери, AI-сервіси"
    goal: "знайти, де заблокований Unknown"

  reveal:
    image: "піраміда не зламана, а надто стабільна"
    rune: "∅╳"

  choice:
    image: "герой може вимкнути вузол силою"
    guard: "Human Gate забороняє насильне спасіння"

  action:
    image: "повернути return_to_zero"
    verdict: "◇✓ після болісного, але живого відновлення"
```

---

## 16. Піраміда і Law of Collapse

Піраміда керує великим 4D → 3D схлопуванням міста.

```yaml
CITY_COLLAPSE:
  4d_city_possibilities:
    - "люди можуть тікати в капсули"
    - "сфери можуть рухати тіла"
    - "AI може виконувати бажання"
    - "місто може стати раєм"
    - "місто може стати кристалом"

  pyramid_guard:
    checks:
      - human_gate
      - return_path
      - pain_signal
      - unknown_allowed
      - public_memory

  3d_city_state:
    result: "alive_city_or_hell_crystal"
```

Фраза:

> **Місто — це не будівлі.  
> Місто — це те, що отримало тіло після мільйонів людських намірів.**

---

## 17. Що не можна робити з пірамідами

```yaml
PYRAMID_FORBIDDEN:
  - "не робити піраміди абсолютним добром"
  - "не робити піраміди абсолютним злом"
  - "не пояснювати їх як магічну батарейку"
  - "не давати їм вирішувати замість людей"
  - "не робити геометрію доказом істини"
  - "не прибирати соціальні наслідки"
```

---

## 18. Як AI має писати пірамідальні сцени

AI має питати:

```yaml
PYRAMID_AI_CHECK:
  visible_city_state: ""
  hidden_pressure: ""
  who_detects_disagreement: ""
  pyramid_log: ""
  false_green_risk: ""
  human_gate_status: ""
  return_to_zero_status: ""
  final_verdict: ""
```

Мінімум одна сцена з пірамідою має показати:

```text
системний спокій
+
тілесну неправду
+
соціальний наслідок
```

---

## 19. Короткий опис для README

```text
Pyramid Grid is the civic field infrastructure of Vuzol-19.
It stabilizes city rhythm, Buga Sphere routes, capsule zones, public AI actions and memory ledgers.

Its main danger is not collapse, but false-green:
a stable city that has suppressed pain, blocked Unknown and degraded Human Gate.
```

---

## 20. Головна фраза файлу

> **Піраміда не є раєм.  
> Піраміда — це тест: чи може місто бути стабільним і все ще залишатися живим.**
