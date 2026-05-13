# 08_DRIFT_SYSTEM.md
# Вузол-19 — Drift System v0.1

> **Цей файл описує дріфт як головний режим взаємодії людини, машини, Квітки, пірамідального такту і Human Gate.**  
> Дріфт — це не магія і не “сила думки”.  
> Дріфт — це стан, де імпульс не стає дією напряму, а проходить тіло, тінь, Guard, Bindu і тільки тоді отримує форму.

---

## 1. Одне речення

**Дріфт — це керований стан переходу, у якому людина, машина, поле і намір на короткий час стають одним маршрутом без втрати Human Gate.**

Коротко:

```text
людина + тіло + намір + машина + поле + Guard + return path = drift
```

Фраза:

> **Дріфт починається там, де пілот перестає змушувати машину і дозволяє їй стати тілом без втрати себе.**

---

## 2. Чим дріфт не є

```yaml
DRIFT_IS_NOT:
  - "не телепатія"
  - "не магічне керування"
  - "не повне злиття з машиною"
  - "не автоматичний автопілот"
  - "не відсутність страху"
  - "не придушення болю"
  - "не ідеальний контроль"
```

Дріфт — це не коли людина зникає в системі.

Дріфт — це коли людина настільки ясно тримає центр, що система може рухатися через неї, не захоплюючи кермо.

---

## 3. Чим дріфт є

```yaml
DRIFT_IS:
  body_state:
    meaning: "тіло достатньо стабільне, щоб не брехати"

  intent_state:
    meaning: "намір знижує силу й проходить Guard"

  field_state:
    meaning: "пірамідальний або локальний такт не суперечить дії"

  machine_state:
    meaning: "сфера, екзоскелет або VR готові прийняти команду"

  human_gate_state:
    meaning: "людина не передала остаточний вибір AI або тіні"

  return_path:
    meaning: "є шлях повернення в нуль"
```

---

## 4. Основна формула дріфту

```text
SIGNAL
→ BODY_SYNC
→ INTENT_REDUCTION
→ SHADOW_AUDIT
→ FIELD_LOCK
→ HUMAN_GATE
→ BINDU_VERDICT
→ DRIFT_ACTION
→ RETURN_TO_ZERO
```

Дріфт не завершується дією.  
Дріфт завершується поверненням.

Фраза:

> **Пілот, який не може повернутися, не дріфтує.  
> Він падає красиво.**

---

## 5. Стани дріфту

```yaml
DRIFT_STATES:
  NO_DRIFT:
    meaning: "немає синхронізації"

  PRE_DRIFT:
    meaning: "система читає намір, але ще не дозволяє дію"

  NOT_A_BOAT_YET:
    meaning: "машина готова, пілот ні"
    rune: "⊙╳"

  DRIFT_LOCK:
    meaning: "людина, машина і поле синхронізовані"

  FLOW_DRIFT:
    meaning: "рух іде мʼяко, але Guard активний"

  ZERO_DRIFT:
    meaning: "мінімум сили, максимум ясності, Unknown allowed"

  DRIFT_LOSS:
    meaning: "система втрачає синхронізацію"
    rune: "⚠"

  SHADOW_DRIFT:
    meaning: "тінь отримала доступ до двигуна"
    rune: "⟲△"

  FALSE_DRIFT:
    meaning: "виглядає стабільно, але Unknown заблокований"
    rune: "∅╳"

  RETURN_TO_ZERO:
    meaning: "пілот і система повертаються в безпечний стан"
```

---

## 6. NOT_A_BOAT_YET

Це стан, де техніка готова, але дріфт ще не народився.

```yaml
NOT_A_BOAT_YET:
  sphere_status: READY
  operator_sync: weak
  intent_force: high
  shadow_leak: active
  return_path: uncertain
  verdict: COMMIT_BLOCKED
```

Фраза:

> **Активність не є готовністю.  
> Човен на березі теж має форму човна.**

У сцені цей стан потрібен, щоб показати:

```text
пілот хоче діяти
машина може діяти
але Human Gate ще не чистий
```

---

## 7. DRIFT_LOCK

DRIFT_LOCK — це коли дія дозволена, але ще під Guard.

```yaml
DRIFT_LOCK:
  body:
    breath_sync: stable
    spine_clock: coherent
    jaw_lock: released
    hand_tension: clean

  intent:
    force: reduced
    shadow_leak: low
    unknown_allowed: true

  machine:
    response_latency: aligned
    field_lock: stable

  pyramid:
    return_path: exists
    city_clock: coherent

  verdict:
    rune: "◇✓"
    status: "ACTION_ALLOWED"
```

Фраза:

> **Машина не підкорилася.  
> Вона погодилася.**

---

## 8. ZERO_DRIFT

Zero-Drift — це найвищий стан.

Це не “нуль дії”.  
Це нуль зайвої сили.

```yaml
ZERO_DRIFT:
  intent_force: minimal
  awareness: high
  unknown_allowed: true
  shadow_noise: low
  field_response: clear
  action: precise
```

Руна:

```text
∅✓
◇✓
```

Фраза:

> **Він перестав шукати траєкторію.  
> І тоді траєкторія перестала тікати.**

Zero-Drift потрібен у фінальних або ключових сценах, де герой не перемагає силою, а перестає давати тіні тіло.

---

## 9. SHADOW_DRIFT

Shadow Drift — це коли пілот думає, що керує, але діє тінь.

```yaml
SHADOW_DRIFT:
  visible:
    - "рух швидкий"
    - "реакція сильна"
    - "сфера слухається"
    - "оператор відчуває владу"

  hidden:
    - "prove_self"
    - "shame"
    - "revenge"
    - "control"
    - "abandonment_fear"

  result:
    - "weapon_body"
    - "dangerous_loop"
    - "prion_action"
```

Руна:

```text
⟲△
```

Фраза:

> **Він не втратив контроль.  
> Гірше — контроль отримало те, що він не хотів бачити.**

---

## 10. FALSE_DRIFT

False Drift — це коли все виглядає ідеально, але живого Unknown немає.

```yaml
FALSE_DRIFT:
  visible:
    - "рух ідеальний"
    - "сфера стабільна"
    - "емоції низькі"
    - "помилок немає"

  hidden:
    - "unknown_blocked"
    - "adaptation_low"
    - "contact_absent"
    - "control_without_life"
```

Руна:

```text
∅╳
FALSE_GREEN
```

Фраза:

> **Найнебезпечніший пілот був не той, хто тремтів.  
> А той, хто був надто рівний.**

---

## 11. Хто може бути дріфт-пілотом

Дріфт-пілот не обовʼязково найсильніший.

```yaml
DRIFT_PILOT_CAN:
  - "витримати Unknown"
  - "відчути тиск без паніки"
  - "побачити власну тінь до дії"
  - "зменшити силу наміру"
  - "не переплутати контроль із балансом"
  - "не романтизувати біль"
  - "зберегти return path"
  - "дозволити Commit Blocked без сорому"
```

Фраза:

> **Найважчий маневр пілота — не поворот.  
> Найважчий маневр — не дати страху натиснути кермо.**

---

## 12. Хто не може дріфтити

```yaml
DRIFT_BLOCKERS:
  shame_as_engine:
    symptom: "довести, що я можу"

  control_as_balance:
    symptom: "ідеальна рівність без контакту"

  pain_suppression:
    symptom: "мені все одно"

  power_fantasy:
    symptom: "машина має показати мою силу"

  unknown_blocked:
    symptom: "я вже знаю, що це означає"

  no_return_path:
    symptom: "можу увійти, але не можу повернутися"

  ai_overtrust:
    symptom: "система сказала green, значить можна"
```

---

## 13. Дріфт і психологія

Дріфт — це психологія, яку видно тілом.

```yaml
DRIFT_PSYCHOLOGY_MAP:
  shame:
    body: "затримка дихання, агресивний жест"
    machine: "різкий старт"
    rune: "△"

  grief:
    body: "тремтіння, але контакт збережено"
    machine: "повільний стабільний lift"
    rune: "◇✓"

  control:
    body: "надто рівний голос, заблокована адаптація"
    machine: "ідеальна траєкторія без живого коригування"
    rune: "∅╳"

  fear:
    body: "мікровідкат, замороження"
    machine: "lock-pulse"
    rune: "⚠"

  clean_intent:
    body: "дихання нижче, сила зменшена"
    machine: "response aligned"
    rune: "◇✓"
```

Фраза:

> **Система не читала душу.  
> Вона читала тіло в момент, коли душа майже збрехала.**

---

## 14. Дріфт і діалог

Дріфт існує не тільки в польоті сфери.

Розмова теж може дріфтити або зриватися.

```yaml
DIALOGUE_DRIFT:
  clean:
    trigger: "критика"
    body_signal: "тиск"
    shadow: "сором"
    action: "пауза"
    verdict: "COMMIT_BLOCKED"
    result: "слово не стало зброєю"

  broken:
    trigger: "критика"
    body_signal: "ігноровано"
    shadow: "сором"
    action: "атака"
    result: "контакт розірвано"
```

Фраза:

> **Кожна розмова була маленькою сферою.  
> Вона могла стати мостом, зброєю або кристалом.**

---

## 15. Дріфт і капсули

Капсула може імітувати дріфт, але без return path це не дріфт.

```yaml
CAPSULE_FALSE_DRIFT:
  user_feels:
    - "я герой"
    - "я в потоці"
    - "світ мене слухає"

  system_check:
    return_to_zero: false
    shadow_loop: high
    real_contact: degraded

  verdict: "FALSE_DRIFT"
```

Фраза:

> **Капсула дала йому потік.  
> Але не дала берега.**

---

## 16. Дріфт і піраміда

Піраміда дає міський такт для дріфту.

```yaml
PYRAMID_DRIFT_SUPPORT:
  provides:
    - field_clock
    - route_permission
    - public_guard
    - return_path
    - memory_write

  risks:
    - false_green_clock
    - over-stabilization
    - public_pain_suppression
```

Якщо піраміда здорова:

```text
пілот може відчувати місто, але не зливається з ним
```

Якщо заражена:

```text
пілот отримує ідеальний маршрут, але без живого центру
```

---

## 17. Дріфт і AI

AI може допомогти дріфту, але не може стати пілотом замість людини.

```yaml
AI_DRIFT_ASSIST:
  can:
    - detect_patterns
    - warn_false_green
    - calculate_routes
    - monitor_return_path
    - block_prion_commit

  cannot:
    - replace_human_gate
    - decide_final_intent
    - erase_pain
    - force_healing
```

Фраза:

> **AI міг показати тисячу маршрутів.  
> Але не мав права вибрати, кому з них належить тіло.**

---

## 18. Дріфт як сцена

Шаблон дріфт-сцени:

```yaml
DRIFT_SCENE_TEMPLATE:
  1_surface_task:
    question: "Що герой має зробити?"

  2_body_signal:
    question: "Що тіло показує раніше за думку?"

  3_machine_ready:
    question: "Чи машина технічно готова?"

  4_shadow_leak:
    question: "Яка тінь хоче керма?"

  5_guard_intervention:
    question: "Що блокується?"

  6_reduction:
    question: "Як герой зменшує силу наміру?"

  7_drift_lock:
    question: "Коли дія дозволена?"

  8_return:
    question: "Як герой повертається в нуль?"
```

---

## 19. Перше тренування дріфту

```yaml
FIRST_DRIFT_TRAINING:
  setting: "Drift Hall / BUGA_STATION"
  task: "підняти сферу на один метр"
  twist: "це не тест техніки, а тест спостерігача"

  operators:
    student:
      issue: "prove_self"
      result: "WEAPON_BODY"

    older_woman:
      issue: "grief"
      result: "BOAT_BODY"

    control_man:
      issue: "control_without_contact"
      result: "CRYSTAL_BODY"

  lesson:
    "Машини однакові. Різними були ті, хто дивився."
```

---

## 20. Побутовий дріфт

Щоб світ був живим, дріфт має проявлятися в побуті:

```yaml
DAILY_DRIFT_EXAMPLES:
  kitchen_argument:
    drift_object: "слово"
    risk: "сором → атака"
    rune: "⊙╳"

  child_waiting:
    drift_object: "контакт"
    risk: "батько в капсулі став героєм тільки в симуляції"
    rune: "⟲△"

  elder_assist:
    drift_object: "повільна сфера"
    risk: "система хоче прискорити старість"
    rune: "∅✓"

  city_crossing:
    drift_object: "маршрут через пірамідальну площу"
    risk: "CITY_STABLE бреше"
    rune: "△"

  ai_code_review:
    drift_object: "код"
    risk: "красивий loop без Guard"
    rune: "⟲△"
```

---

## 21. Дріфт у фіналі

Фінальний дріфт не має бути “найбільшим польотом”.

Він має бути найчистішим схлопуванням.

```yaml
FINAL_DRIFT:
  force: minimal
  clarity: maximal
  unknown_allowed: true
  human_gate: active
  pain_signal: returns
  pyramid_false_green: cracked
  city_breaks: false
  return_to_zero: restored
```

Фраза:

> **Він не переміг систему.  
> Він не дав своїй тіні її врятувати.**

---

## 22. Що не можна робити з дріфтом

```yaml
DRIFT_FORBIDDEN:
  - "не робити дріфт суперсилою"
  - "не робити дріфт магією"
  - "не дозволяти дріфт без тіла"
  - "не дозволяти дріфт без Shadow Audit"
  - "не робити біль паливом без межі"
  - "не робити Zero-Drift байдужістю"
  - "не забувати return_to_zero"
```

---

## 23. Як AI має писати дріфт-сцени

```yaml
DRIFT_AI_CHECK:
  task: ""
  body_signal: ""
  machine_status: ""
  shadow_leak: ""
  guard_response: ""
  drift_state: ""
  rune: ""
  return_path: ""
  memory_update: ""
```

Сцена дріфту сильна, якщо:

```text
дія показує психологію,
а психологія змінює механіку дії.
```

---

## 24. Короткий опис для README

```text
Drift is the state where human intent, body, machine, field, Guard and return path align without losing Human Gate.

It is not mind control or magic. It is a guarded transition from impulse to action.
A drift pilot is not the fastest operator, but the one whose shadow does not have direct access to the engine.
```

---

## 25. Головна фраза файлу

> **Дріфт — це не коли машина слухається людини.  
> Дріфт — це коли людина нарешті чує, хто в ній хотів керувати машиною.**
