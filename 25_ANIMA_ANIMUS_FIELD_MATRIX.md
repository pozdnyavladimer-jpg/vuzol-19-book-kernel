# 25_ANIMA_ANIMUS_FIELD_MATRIX.md
# Вузол-19 — Anima / Animus Field Matrix v0.1

> **Цей файл поглиблює Relationship Runtime.**  
> Він описує Anima / Animus не як “чоловіче проти жіночого”, а як **дві внутрішні функції кожної людини**: прийняття / Unknown / контакт і межа / дія / структура.  
> Числа тут — не психологічний діагноз і не тест сумісності. Це **runtime-ваги персонажа** для письма, scene audit і relationship field.

---

## 1. Одне речення

**Anima / Animus Field Matrix — це числова карта внутрішнього балансу персонажа: як він приймає, ставить межу, проектує тінь, шукає партнера поля і проходить repair.**

Коротко:

```text
caregiver imprint
+ body memory
+ shadow history
+ anima function
+ animus function
+ attachment style
+ repair capacity
= relationship field behavior
```

Головна фраза:

> **Стосунки стають рівними не тоді, коли персонажі однакові.  
> Вони стають рівними тоді, коли кожен має власний центр, власну межу і право не бути функцією для чужої рани.**

---

## 2. Важлива межа

Ця модель не є клінічним тестом.

```yaml
NOT_CLINICAL:
  - "не діагноз"
  - "не тест сумісності"
  - "не біологічна формула"
  - "не доказ, хто кому підходить"
  - "не фатальна доля"

USE_AS:
  - "інструмент для роману"
  - "карта персонажа"
  - "relationship audit"
  - "AI writing helper"
  - "пошук тіні і межі в сцені"
```

AI не має казати:

```text
вони сумісні на 87%, отже це любов
```

AI має казати:

```text
їхні поля резонують у контакті, але ламаються на межі;
потрібен repair або boundary scene
```

---

## 3. Jung Bridge

У Jungian-шарі:

```yaml
JUNG_BRIDGE:
  anima:
    role: "внутрішній образ прийняття, душі, контакту, Unknown, образності"

  animus:
    role: "внутрішній образ слова, структури, межі, дії, принципу"

  shadow:
    role: "те, що не інтегровано і проектується на іншого"

  individuation:
    role: "процес, де людина повертає проєкцію собі і стає ціліснішою"
```

Але в каноні “Вузла-19” ми не привʼязуємо це жорстко до статі.

```text
кожна людина має Anima-function
кожна людина має Animus-function
кожна людина має Shadow
кожна людина має Human Gate
```

---

## 4. Modern Psychology Bridge

Для більш сучасної психологічної мови ця модель ближче до:

```yaml
MODERN_BRIDGE:
  attachment_working_model:
    meaning: "ранній досвід із доглядальниками формує очікування про себе, інших і стосунки"

  gender_schema:
    meaning: "людина вчиться обробляти 'маскулінні' й 'фемінні' ролі через культуру, сімʼю, приклади"

  psychological_androgyny:
    meaning: "адаптивність може зростати, коли людина має доступ і до мʼякості/контакту, і до межі/дії"

  interpersonal_schema:
    meaning: "людина приносить у звʼязок очікування: чи мене почують, чи покинуть, чи поглинуть, чи контролюватимуть"
```

У нашій мові:

```text
attachment = як я очікую контакт
gender schema = які ролі я вважаю дозволеними собі
anima/animus = внутрішні функції прийняття і межі
relationship field = що відбувається між двома такими системами
```

---

## 5. Базові осі

```yaml
PERSON_FIELD_AXES:
  anima_receptivity:
    scale: "0-100"
    question: "наскільки персонаж може слухати, приймати Unknown, відчувати контакт?"

  animus_boundary:
    scale: "0-100"
    question: "наскільки персонаж може діяти, ставити межу, називати форму?"

  shadow_pressure:
    scale: "0-100"
    question: "наскільки сильно неінтегрована тінь тисне на звʼязок?"

  attachment_security:
    scale: "0-100"
    question: "наскільки безпечно персонаж переносить близькість, паузу і відмову?"

  repair_capacity:
    scale: "0-100"
    question: "наскільки персонаж може повертати контакт після збою?"

  projection_load:
    scale: "0-100"
    question: "наскільки персонаж бачить у партнері образ, а не реальну людину?"

  human_gate_strength:
    scale: "0-100"
    question: "наскільки персонаж не дозволяє іншому або AI вирішити за себе?"
```

---

## 6. Чому числа корисні

Числа потрібні не для того, щоб “порахувати любов”.

Вони потрібні, щоб AI не робив усіх персонажів однаковими.

```yaml
NUMBER_USE:
  good:
    - "дати персонажу стабільний психологічний профіль"
    - "побачити, де він зламається в сцені"
    - "зберегти рівність персонажів"
    - "не робити жінку тільки Anima, а чоловіка тільки Animus"
    - "бачити, що кожен має власний центр"

  bad:
    - "робити рейтинг людей"
    - "вирішувати любов"
    - "ставити діагноз"
    - "казати, що 85/15 = доля"
```

Фраза:

> **Число не каже, кого любити.  
> Число показує, де сцена має натиснути, щоб персонаж перестав брехати собі.**

---

## 7. Caregiver Imprint Matrix

Батько, мати або будь-який доглядальник можуть давати різні функції.

Не так:

```text
father = only animus
mother = only anima
```

А так:

```yaml
CAREGIVER_IMPRINT:
  father_field:
    may_give:
      - "boundary"
      - "permission to act"
      - "fear of authority"
      - "absence wound"
      - "softness"
      - "emotional silence"
      - "witnessing"

  mother_field:
    may_give:
      - "contact"
      - "safety"
      - "fusion"
      - "control through care"
      - "emotional weather"
      - "permission to feel"
      - "fear of engulfment"

  other_caregivers:
    may_give:
      - "repair model"
      - "trust model"
      - "body safety"
      - "language of conflict"
```

Головне:

> **Не важливо, хто “мав” дати функцію.  
> Важливо, хто реально став джерелом цієї функції в памʼяті персонажа.**

---

## 8. Приклад: чоловік із сильним материнським полем

```yaml
CHARACTER_FIELD_EXAMPLE_A:
  character: "male_node_A"

  caregiver_imprint:
    father_field:
      presence: 15
      gave:
        boundary: 20
        emotional_witness: 5
        permission_to_act: 25
      wound:
        - "absence"
        - "weak masculine mirror"

    mother_field:
      presence: 85
      gave:
        contact: 80
        emotional_weather: 90
        care: 75
        fusion_risk: 70
      wound:
        - "love mixed with anxiety"
        - "difficulty separating without guilt"

  current_axes:
    anima_receptivity: 78
    animus_boundary: 42
    attachment_security: 48
    shadow_pressure: 63
    repair_capacity: 55
    projection_load: 68
    human_gate_strength: 46

  relationship_risk:
    - "шукає партнера як межу, якої не вистачило"
    - "може плутати близькість із поглинанням"
    - "може боятися твердої межі, але одночасно її потребувати"

  clean_growth:
    - "розвинути власний Animus-boundary"
    - "не вимагати, щоб партнер став батьківською функцією"
    - "навчитися говорити 'ні' без провини"
```

Фраза для сцени:

> **Він не шукав жінку.  
> Він шукав межу, яка не покине його, коли він нарешті скаже “ні”.**

---

## 9. Приклад: жінка з сильним батьківським вектором

```yaml
CHARACTER_FIELD_EXAMPLE_B:
  character: "female_node_B"

  caregiver_imprint:
    father_field:
      presence: 80
      gave:
        discipline: 75
        speech: 70
        action: 85
        emotional_distance: 65
      wound:
        - "love must be earned through competence"
        - "softness feels unsafe"

    mother_field:
      presence: 35
      gave:
        comfort: 40
        emotional_permission: 25
      wound:
        - "weak softness mirror"
        - "difficulty receiving care"

  current_axes:
    anima_receptivity: 38
    animus_boundary: 82
    attachment_security: 52
    shadow_pressure: 58
    repair_capacity: 49
    projection_load: 54
    human_gate_strength: 74

  relationship_risk:
    - "може знецінювати потребу в ніжності"
    - "може чути прохання як слабкість"
    - "може любити через контроль як ефективність"

  clean_growth:
    - "розвинути прийняття без втрати сили"
    - "дозволити собі care, не називаючи це слабкістю"
    - "вчитися repair без перемоги"
```

Фраза для сцени:

> **Вона не боялася болю.  
> Вона боялася, що ніжність забере в неї форму.**

---

## 10. Партнер не має бути “ліками”

```yaml
PARTNER_AS_MEDICINE_RISK:
  looks_like:
    - "ти мене доповнюєш"
    - "ти даєш мені те, чого не дав батько"
    - "з тобою я нарешті цілий"
    - "ти моя межа"
    - "ти моя мʼякість"

  danger:
    - "партнер стає функцією"
    - "людина перестає розвивати власну вісь"
    - "relationship field стає терапевтичною залежністю"

  clean_version:
    - "ти допомагаєш мені побачити, чого мені бракує"
    - "але я не роблю тебе відповідальним за мою відсутню частину"
```

Фраза:

> **Партнер може показати відсутню вісь.  
> Але якщо він стає цією віссю замість тебе — любов перетворюється на оренду душі.**

---

## 11. Relationship Field Compatibility

Сумісність — це не одна цифра.

```yaml
FIELD_COMPATIBILITY:
  contact_resonance:
    question: "чи можуть вони бути поруч без ролей?"

  boundary_respect:
    question: "чи витримують вони 'ні'?"

  repair_sync:
    question: "чи можуть повернути контакт після збою?"

  shadow_trigger_awareness:
    question: "чи бачать, коли запускають тінь одне одного?"

  projection_reduction:
    question: "чи бачать реальну людину, а не образ?"

  dual_growth:
    question: "чи обидва ростуть, а не один обслуговує поле іншого?"
```

---

## 12. Relationship Matrix

```yaml
RELATIONSHIP_MATRIX:
  node_a:
    anima_receptivity: 78
    animus_boundary: 42
    shadow_pressure: 63
    attachment_security: 48
    repair_capacity: 55
    projection_load: 68
    human_gate_strength: 46

  node_b:
    anima_receptivity: 38
    animus_boundary: 82
    shadow_pressure: 58
    attachment_security: 52
    repair_capacity: 49
    projection_load: 54
    human_gate_strength: 74

  field:
    attraction: "high"
    polarity: "strong"
    projection_risk: "high"
    boundary_conflict: "high"
    repair_potential: "medium"
    equality_risk: "node_a may outsource boundary; node_b may outsource softness"

  verdict:
    initial: "CONNECT_WITH_BOUNDARY"
    required_scenes:
      - "boundary without rejection"
      - "repair after silence"
      - "node_a says no"
      - "node_b receives care without losing power"
```

---

## 13. Equality Rule

Рівність персонажів означає:

```yaml
EQUALITY_RULE:
  each_character_has:
    - "own center"
    - "own wound"
    - "own shadow"
    - "own boundary"
    - "own repair path"
    - "own right to say no"
    - "own transformation"

  forbidden:
    - "один персонаж існує тільки для healing іншого"
    - "жінка як Anima-функція героя"
    - "чоловік як Animus-функція героїні"
    - "партнер як нагорода за розвиток"
```

Фраза:

> **Персонажі рівні не тому, що мають однакову силу.  
> Вони рівні тому, що жоден не є інструментом завершення іншого.**

---

## 14. Field Partner Search

Персонаж шукає не “тип людини”, а поле, яке торкає його незавершену вісь.

```yaml
FIELD_PARTNER_SEARCH:
  unconscious_query:
    - "хто дасть мені межу?"
    - "хто дозволить мені бути мʼяким?"
    - "хто не покине мене в паузі?"
    - "хто витримає моє 'ні'?"
    - "хто побачить мене без ролі?"

  shadow_version:
    - "хто стане моєю відсутньою частиною?"
    - "хто доведе, що я вартий?"
    - "хто не дасть мені відчути стару рану?"

  clean_version:
    - "хто допоможе мені побачити мою відсутню функцію?"
    - "хто не вкраде мій Human Gate?"
    - "з ким я зможу рости без поглинання?"
```

---

## 15. Anima / Animus Balance States

```yaml
BALANCE_STATES:
  balanced:
    description: "може слухати і ставити межу"
    risk: "low"

  high_anima_low_animus:
    description: "багато прийняття, слабка межа"
    risk:
      - "поглинання"
      - "залежність"
      - "важко сказати ні"

  high_animus_low_anima:
    description: "сильна межа, слабке прийняття"
    risk:
      - "контроль"
      - "емоційна дистанція"
      - "repair через перемогу"

  low_both:
    description: "немає ні контакту, ні межі"
    risk:
      - "хаос"
      - "завмирання"
      - "пасивна залежність"

  high_both:
    description: "потенційно зрілий вузол"
    risk:
      - "якщо shadow_pressure високий, сила може стати маніпуляцією"
```

---

## 16. Shadow corrections

```yaml
SHADOW_CORRECTIONS:
  if_high_anima_low_animus:
    scene_tests:
      - "персонаж має сказати ні"
      - "персонаж має витримати провину"
      - "персонаж має не шукати партнера як межу"

  if_high_animus_low_anima:
    scene_tests:
      - "персонаж має прийняти care"
      - "персонаж має програти без приниження"
      - "персонаж має не назвати мʼякість слабкістю"

  if_high_projection:
    scene_tests:
      - "партнер розбиває образ"
      - "персонаж бачить реальну межу іншого"
      - "потяг проходить Unknown"

  if_low_repair:
    scene_tests:
      - "після конфлікту треба повернути контакт"
      - "пауза має бути пояснена"
      - "слово має бути повернуте з рани"
```

---

## 17. Example Scene — Outsourced Boundary

```text
— Скажи мені, що робити, — попросив він.

Вона подивилась на нього довше, ніж було зручно.

— Ні.

Слово було коротке.

Воно не відкинуло його.

Саме тому вдарило сильніше.

— Ти ж бачиш, що я гублюсь.

— Бачу.

— Тоді чому не допоможеш?

Вона поставила чашку між ними.

Не як стіну.

Як межу.

— Бо ти просиш не допомогу. Ти просиш, щоб я стала твоєю формою.

Він хотів образитися.

Personal Node уже підняв першу фразу.

“Тобі байдуже.”

⊙╳

Він мовчав.

Уперше його мовчання не було пасткою.

— Я не знаю, як сказати “ні” без страху, — сказав він.

Вона кивнула.

— Тоді почни не зі мною. Почни з цієї фрази.
```

```yaml
SCENE_AUDIT:
  node_a:
    missing_axis: "animus_boundary"
    shadow: "abandonment_fear"
    growth: "names lack of boundary"

  node_b:
    strong_axis: "animus_boundary"
    risk: "coldness"
    growth: "sets boundary without rejection"

  relationship_verdict: "REPAIR / BOUNDARY"
```

---

## 18. Example Scene — Softness Without Collapse

```text
— Я не слабка, — сказала вона.

— Я цього не казав.

— Ти приніс мені чай.

Він глянув на чашку, ніби вона раптом стала доказом злочину.

— Це був чай.

— У моєму домі так починалися накази.

Він не торкнувся чашки.

HOLD

— Тоді я поставлю його тут, — сказав він. — І ти сама вирішиш, чи він має право бути ближче.

Вона дивилась на пару над чашкою.

Ніжність не рухалась.

Вперше вона не лізла через її Gate.
```

```yaml
SCENE_AUDIT:
  node_a:
    axis: "soft care"
    human_gate: "preserved"

  node_b:
    wound: "care became control in past"
    growth: "receives care without surrender"

  verdict: "CONNECT_SLOW"
```

---

## 19. Character Card Template

```yaml
ANIMA_ANIMUS_CHARACTER_CARD:
  character_name: ""

  caregiver_imprint:
    father_field:
      presence: 0
      gave:
        boundary: 0
        emotional_witness: 0
        permission_to_act: 0
        softness: 0
      wound:
        - ""

    mother_field:
      presence: 0
      gave:
        contact: 0
        safety: 0
        boundary: 0
        emotional_permission: 0
      wound:
        - ""

    other_field:
      presence: 0
      gave:
        repair: 0
        trust: 0
        body_safety: 0

  current_axes:
    anima_receptivity: 0
    animus_boundary: 0
    attachment_security: 0
    shadow_pressure: 0
    repair_capacity: 0
    projection_load: 0
    human_gate_strength: 0

  relationship_behavior:
    seeks:
      - ""
    fears:
      - ""
    confuses:
      - ""

  growth_tests:
    - ""

  clean_love_rule: ""
```

---

## 20. Pair Card Template

```yaml
ANIMA_ANIMUS_PAIR_CARD:
  pair_id: ""

  node_a:
    name: ""
    dominant_axis: ""
    missing_axis: ""
    main_shadow: ""

  node_b:
    name: ""
    dominant_axis: ""
    missing_axis: ""
    main_shadow: ""

  attraction:
    source: ""
    projection_risk: ""

  conflict:
    main_trigger: ""
    repeating_loop: ""

  dual_human_gate:
    node_a: ""
    node_b: ""

  repair_path:
    - ""

  verdict:
    current: ""
    next_scene_needed: ""
```

---

## 21. AI use

```yaml
AI_USE:
  before_relationship_scene:
    - "build or read both character cards"
    - "check caregiver imprint"
    - "check current axes"
    - "detect projection"
    - "check two Human Gates"
    - "choose verdict"

  during_scene:
    - "show body before explanation"
    - "show first harmful phrase"
    - "block or transform phrase"
    - "make repair concrete"

  after_scene:
    - "update relationship memory"
    - "adjust axes only if scene changed behavior"
```

---

## 22. What changes after a scene

Не кожна сцена змінює числа.

Число змінюється тільки якщо персонаж реально зробив нову дію.

```yaml
AXIS_UPDATE_RULE:
  increase_animus_boundary_when:
    - "персонаж сказав чисте ні"
    - "витримав провину"
    - "не делегував межу партнеру"

  increase_anima_receptivity_when:
    - "персонаж прийняв care без контролю"
    - "витримав Unknown"
    - "не назвав мʼякість слабкістю"

  increase_repair_capacity_when:
    - "персонаж повернув фразу з рани"
    - "пояснив паузу"
    - "визнав свою частину без самознищення"

  decrease_projection_load_when:
    - "персонаж побачив партнера реальним"
    - "прийняв його/її межу"
    - "перестав робити партнера функцією"
```

---

## 23. Forbidden use

```yaml
FORBIDDEN:
  - "не робити числа біологічною долею"
  - "не казати, що мати завжди дає Anima, а батько завжди Animus"
  - "не робити партнера терапевтом за замовчуванням"
  - "не робити AI суддею сумісності"
  - "не писати жінку як функцію героя"
  - "не писати чоловіка як функцію героїні"
  - "не використовувати 85/15 як ярлик"
  - "не плутати мʼякість зі слабкістю"
  - "не плутати межу з холодністю"
```

---

## 24. Short prompt for AI

```text
Use Anima / Animus Field Matrix for relationship scenes.

Treat anima and animus as inner functions in every person:
anima = receptivity, Unknown, contact;
animus = boundary, action, structure.

Build both character cards.
Use caregiver imprint as memory, not destiny.
Use numbers as runtime weights, not diagnosis.
Check projection, boundary, repair, attachment security and two Human Gates.
Do not let one partner become the missing axis of the other.
Do not let AI decide love.
Make equality visible by giving both characters their own center, wound, boundary and growth path.
```

---

## 25. Головна фраза файлу

> **Людина шукає партнера не тому, що в ній немає половини.  
> Вона шукає поле, де її відсутня вісь стане видимою — але зріле кохання починається тільки тоді, коли вона перестає вимагати, щоб інший став цією віссю замість неї.**
