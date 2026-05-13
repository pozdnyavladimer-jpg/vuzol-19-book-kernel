# 07_BUGA_SPHERES.md
# Вузол-19 — Buga Spheres v0.1

> **Цей файл описує сферу Буга як транспорт, remote body, дріфт-тіло і тест стану пілота.**  
> Сфера Буга — не просто машина. Вона стає тим, що в людині проходить через неї.

---

## 1. Одне речення

**Сфера Буга — це remote body, який отримує функцію тільки тоді, коли оператор, поле, намір, Guard і return path входять у правильний дріфт.**

Коротко:

```text
сфера на станції ≠ тіло
сфера + пілот + дріфт + Guard = дія
```

Фраза:

> **Сфера не була тілом.  
> Вона ставала тим, що в пілоті проходило через неї.**

---

## 2. Чому “Буга”

Назва “Буга” у каноні може мати кілька рівнів:

```yaml
BUGA_NAME_LAYERS:
  surface:
    meaning: "модель сферичного транспорту / remote body"

  mythic:
    meaning: "щось давнє, важке, річкове, земне, повʼязане з рухом і межею"

  technical:
    meaning: "B.U.G.A. як скорочення для системи"
    possible_decode:
      - "Bindu Unified Geometric Apparatus"
      - "Bio-User Geometric Anchor"
      - "Boundary-User Gradient Actuator"
```

Вибір розшифровки можна залишити відкритим.

> **У романі назва може спершу звучати як побутове слово, а потім відкриватися як технічний протокол.**

---

## 3. Основна роль

Сфера Буга може виконувати кілька функцій:

```yaml
BUGA_SPHERE_FUNCTIONS:
  transport:
    meaning: "переміщення оператора або вантажу через поле"

  remote_body:
    meaning: "дія в іншому місці без прямої присутності тіла"

  repair_unit:
    meaning: "ремонт інфраструктури, пірамідальних вузлів, підводних систем"

  rescue_body:
    meaning: "аварійний доступ у небезпечні зони"

  drift_trainer:
    meaning: "тренажер наміру і Human Gate"

  weapon_risk:
    meaning: "якщо тінь проходить у двигун, сфера стає зброєю"

  mirror:
    meaning: "показує, хто в людині хоче діяти"
```

---

## 4. Чим сфера відрізняється від транспорту

Старий транспорт:

```text
пілот → кермо → машина → рух
```

Сфера Буга:

```text
пілот → тіло → намір → Flower scan → Guard → drift → sphere body → дія
```

Фраза:

> **У старих машинах пілот рухав важіль.  
> У сфері Буга пілот рухав межу між собою і дією.**

---

## 5. Підключення до сфери

Підключення проходить не через кнопку, а через стан.

```yaml
BUGA_CONNECTION_SEQUENCE:
  1_presence:
    meaning: "оператор фізично або нейроінтерфейсно присутній"

  2_body_scan:
    reads:
      - breath
      - spine
      - hand_microtension
      - eye_focus
      - pelvic_pressure
      - jaw_tension

  3_intent_detection:
    question: "що саме хоче діяти?"

  4_shadow_audit:
    question: "тінь, страх, сором, контроль або clean intent?"

  5_pyramid_anchor:
    question: "чи є стабільний такт і return path?"

  6_bindu_verdict:
    options:
      - BOAT_FORMED
      - NOT_A_BOAT_YET
      - ROUTE_BLOCKED
      - DRIFT_LOCK
      - DRIFT_LOSS
```

---

## 6. Головні стани сфери

```yaml
BUGA_STATES:
  OFFLINE:
    meaning: "сфера не активна"

  READY:
    meaning: "сфера технічно готова"

  LISTENING:
    meaning: "сфера читає оператора"

  NOT_A_BOAT_YET:
    meaning: "сфера готова, але стан пілота не дозволяє зробити її тілом"
    rune: "⊙╳"

  BOAT_FORMED:
    meaning: "оператор, сфера, поле і return path зійшлись"
    rune: "◇✓"

  DRIFT_LOCK:
    meaning: "стабільна синхронізація"

  DRIFT_LOSS:
    meaning: "розсинхронізація"
    rune: "⚠"

  WEAPON_BODY:
    meaning: "сфера схлопнулась через тінь сили"

  CRYSTAL_BODY:
    meaning: "сфера схлопнулась через контроль і blocked Unknown"

  GHOST_BODY:
    meaning: "сфера рухається, але Human Gate слабкий"

  RETURNING:
    meaning: "сфера повертається в безпечний стан"

  MEMORY_WRITE:
    meaning: "система записує, чому drift був дозволений або заблокований"
```

---

## 7. NOT_A_BOAT_YET

Це один із найважливіших станів.

```yaml
NOT_A_BOAT_YET:
  sphere_status: READY
  operator_status: unstable
  reason_examples:
    - "intent_force too high"
    - "shadow_leak: prove_self"
    - "breath_sync weak"
    - "return_path unclear"
    - "unknown_blocked"
  verdict: "COMMIT_BLOCKED"
```

Фраза:

> **Сфера була готова.  
> Пілот — ні.  
> Човен на березі теж має форму човна.**

---

## 8. BOAT_FORMED

BOAT_FORMED — це момент, коли сфера стає справжнім тілом дії.

```yaml
BOAT_FORMED:
  operator:
    breath_sync: stable
    spine_clock: coherent
    intent_force: reduced
    shadow_leak: low
    unknown_allowed: true

  sphere:
    field_lock: stable
    response_latency: aligned

  pyramid:
    return_path: exists
    guard_schema: active

  verdict:
    rune: "◇✓"
    action: "ACTION_ALLOWED"
```

Фраза:

> **Вона не полетіла.  
> Вона стала човном.**

---

## 9. Три результати одного підключення

Одна й та сама сфера може стати різним залежно від спостерігача.

```yaml
THREE_OPERATOR_TEST:
  student:
    shadow: "prove_self"
    result: "WEAPON_BODY"
    rune: "⟲△"
    lesson: "сила без Guard стає зброєю"

  older_woman:
    shadow: "grief_seen_not_suppressed"
    result: "BOAT_BODY"
    rune: "◇✓"
    lesson: "чесний біль може пройти дріфт"

  control_man:
    shadow: "control_without_contact"
    result: "CRYSTAL_BODY"
    rune: "∅╳"
    lesson: "ідеальний порядок без Unknown стає кристалом"
```

Фраза:

> **Одна сфера стала зброєю.  
> Одна стала човном.  
> Одна стала кристалом.  
> Машини були однакові. Різними були ті, хто дивився.**

---

## 10. Сфера як атомна метафора

Сферу можна описувати через метафору станів, але не видавати це за буквальну фізику.

```yaml
BUGA_ATOMIC_METAPHOR:
  before_connection:
    meaning: "superposition of functions"

  during_scan:
    meaning: "probability field of possible actions"

  bindu_verdict:
    meaning: "collapse into one allowed function"

  after_action:
    meaning: "3D consequence and memory"
```

Коротко:

```text
до пілота:
  сфера може бути всім

після Bindu:
  сфера стає конкретною дією
```

Фраза:

> **Поки пілот не зібрав центр, сфера була всім одразу: тілом, зброєю, втечею, мостом, помилкою.**

---

## 11. Сфера і Law of Collapse

Сфера Буга — один із головних прикладів закону 4D → 3D.

```yaml
BUGA_COLLAPSE:
  4d_possibility:
    - transport
    - weapon
    - bridge
    - repair_body
    - escape
    - boat

  human_intent:
    source: "operator state"

  body_signal:
    source: "exoskeleton / breath / spine"

  shadow_audit:
    source: "Personal Node / Flower"

  guard:
    source: "Pyramid Grid / AI Guard"

  bindu:
    verdict: "BOAT_FORMED | BLOCK | REROUTE"

  3d_action:
    result: "actual sphere behavior"
```

Фраза:

> **4D давало сфері всі можливі тіла.  
> Bindu дозволяв тільки одне.**

---

## 12. Сфера і піраміда

Сфера потребує пірамідального якоря.

```yaml
PYRAMID_TO_BUGA_LINK:
  pyramid_provides:
    - field_clock
    - civic_guard
    - return_path
    - route_permission
    - public_memory

  buga_provides:
    - remote_action
    - drift_feedback
    - body_state_data
    - local_field_repair
```

Якщо піраміда false-green:

```yaml
BUGA_RISK_UNDER_FALSE_GREEN:
  route_looks_safe: true
  return_path: weak
  human_gate: degraded
  drift_risk: high
  verdict: "ROUTE_BLOCKED"
```

---

## 13. Сфера і екзоскелет

Екзоскелет — це тіло-перекладач між людиною і сферою.

```yaml
EXOSKELETON_TO_BUGA:
  reads:
    - spine_clock
    - breath_sync
    - hand_tension
    - jaw_lock
    - pelvis_pressure
    - eye_focus

  translates_to:
    - drift_vector
    - pressure_warning
    - intent_force
    - shadow_leak
    - abort_signal
```

Фраза:

> **Екзоскелет чув команду раніше, ніж пілот встиг назвати її думкою.**

---

## 14. Сфера і VR

VR-окуляри показують не “красивий інтерфейс”, а стан дріфту.

```yaml
BUGA_VR_HUD:
  displays:
    - sphere_status
    - operator_sync
    - pyramid_clock
    - return_path
    - rune
    - Bindu verdict
    - drift_vector
    - false_green_warning
```

Приклад:

```yaml
BUGA_HUD:
  SPHERE_STATUS: READY
  FIELD_LOCK: AVAILABLE
  OPERATOR_SYNC: 0.48
  SHADOW_LEAK: "prove_self"
  DRIFT_STATE: "NOT_A_BOAT_YET"
  VERDICT: "COMMIT_BLOCKED"
```

---

## 15. Сфера і психологія

Сфера показує психологію не словами, а поведінкою.

```yaml
PSYCHOLOGICAL_BUGA_PATTERNS:
  shame:
    sphere_behavior: "jerky acceleration / overcorrection"
    rune: "△"

  control:
    sphere_behavior: "too perfect, low adaptation"
    rune: "∅╳"

  grief_seen:
    sphere_behavior: "slow stable lift"
    rune: "◇✓"

  fear:
    sphere_behavior: "lock-pulse / hesitation"
    rune: "⚠"

  power_fantasy:
    sphere_behavior: "fast rise, unstable hover"
    rune: "⟲△"
```

Фраза:

> **Сфера не читала душу.  
> Вона читала момент, коли тінь торкнулася двигуна.**

---

## 16. Побутове використання сфер

Сфери мають бути частиною живого світу.

```yaml
BUGA_DAILY_USES:
  city_transport:
    scene: "сфера перевозить людину через місто під пірамідальним тактом"

  remote_work:
    scene: "інженер ремонтує вузол через сферу"

  rescue:
    scene: "сфера входить у небезпечну зону замість людини"

  school_training:
    scene: "діти вчаться, що не кожен імпульс має право рухати тіло"

  elder_assist:
    scene: "старша людина використовує сферу повільно, без силового дріфту"

  capsule_recovery:
    scene: "сфера допомагає повернути людину з ісекай-зони без насильства"
```

---

## 17. Основні місця для сфер

```yaml
BUGA_LOCATIONS:
  BUGA_STATION:
    meaning: "станція підключення, тренування, видачі сфер"

  DRIFT_HALL:
    meaning: "зал навчання пілотів"

  PYRAMID_DOCK:
    meaning: "вузол, де сфери синхронізуються з міським тактом"

  REMOTE_NODE:
    meaning: "далека точка роботи сфери"

  UNDERWATER_NODE:
    meaning: "підводний або ізольований ремонтний вузол"

  CAPSULE_DISTRICT_EDGE:
    meaning: "місце, де сфери працюють з поверненням людей із капсул"
```

---

## 18. Сцена першого тренування

Шаблон:

```yaml
FIRST_BUGA_TRAINING_SCENE:
  visible:
    - "три сфери стоять у залі"
    - "система каже READY"
    - "оператори вважають, що це тест техніки"

  hidden:
    - "це тест стану спостерігача"

  required_moments:
    - "студент піднімає сферу силою"
    - "старша жінка піднімає через чесний біль"
    - "контрольний чоловік піднімає ідеально, але отримує FALSE_GREEN"
    - "герой пояснює, що машини однакові, різні спостерігачі"

  final_line:
    "Пілот майбутнього вчиться не піднімати сферу. Він вчиться бачити, що саме в ньому хоче її підняти."
```

---

## 19. Сфера як фінальний інструмент

У фіналі сфера не має бути просто зброєю.

Вона має допомогти герою зробити дію, яка:

```text
не руйнує піраміду
не рятує людей силою
не блокує біль
не дає PRION тіло
повертає return_to_zero
зберігає Human Gate
```

Фінальний стан:

```yaml
FINAL_BUGA_USE:
  action_type: "repair / reroute / unlock_unknown"
  weapon_use: false
  human_gate: active
  city_pain: returns
  city_breaks: false
  pyramid_false_green: cracked
  verdict: "◇✓ ACTION_ALLOWED"
```

Фраза:

> **Він не вдарив сферою по піраміді.  
> Він провів через неї те, що піраміда давно перестала пропускати: живий біль.**

---

## 20. Що не можна робити зі сферами

```yaml
BUGA_FORBIDDEN:
  - "не робити сферу просто магічним транспортом"
  - "не робити сферу суперзброєю без наслідків"
  - "не давати дріфт без психологічного стану"
  - "не дозволяти сфері вирішувати замість Human Gate"
  - "не робити BOAT_FORMED автоматичним"
  - "не забувати return_path"
  - "не ігнорувати тіло оператора"
```

---

## 21. Як AI має писати сцени зі сферою

```yaml
BUGA_SCENE_CHECK:
  sphere_status: ""
  operator_body_signal: ""
  active_shadow: ""
  pyramid_anchor: ""
  return_path: ""
  drift_state: ""
  rune: ""
  bindu_verdict: ""
  consequence: ""
```

Сцена зі сферою сильна, якщо:

```text
сфера показує не техніку,
а правду про пілота.
```

---

## 22. Короткий опис для README

```text
Buga Spheres are remote bodies in the world of Vuzol-19.
They are not vehicles in the old sense.
A sphere becomes transport, weapon, bridge, crystal or boat depending on the operator's state, Flower scan, Guard, Pyramid anchor and return path.
```

---

## 23. Головна фраза файлу

> **Сфера Буга — це дзеркало дії.  
> Вона не показує, що людина вміє.  
> Вона показує, хто в людині хоче діяти.**
