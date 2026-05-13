# 02_FLOWER_RUNTIME_ROUTER.md
# Вузол-19 — Flower Runtime Router v0.1

> **Цей файл каже AI не що таке Квітка, а як через неї проходити сцену.**  
> Якщо `00_MASTER_CANON.md` — це закон світу, а `01_FLOWER_RUNTIME_TABLES.md` — це таблиця рун і пелюсток, то цей файл — **маршрутизатор сцени**.

---

# 1. Головна функція Router

Flower Runtime Router перетворює будь-який запит на сцену в контрольований маршрут:

```text
REQUEST
→ SIGNAL
→ CENTER_CHECK
→ FORWARD_3
→ BACKWARD_3
→ BINDU_VERDICT
→ SCENE_DRAFT
→ SCENE_AUDIT
→ MEMORY_UPDATE
```

Головний закон:

> **AI не має права писати сцену одразу.  
> Спочатку він має пройти Квітку.**

---

# 2. Що Router блокує

Router потрібен, щоб AI не скочувався в:

```text
красивий туман
символи без функції
руни як декор
героя-бога
AI, який замінює Human Gate
біль як культ
false-green фінал
технологію без наслідків
лекцію замість сцени
```

Коротко:

> **Router захищає книгу від PRION-естетики.**

---

# 3. Вхідний формат запиту

Коли автор або AI хоче сцену, бажано дати 5 полів:

```yaml
SCENE_REQUEST:
  place: "де сцена?"
  people: "хто там?"
  technology: "яка технологія присутня?"
  shadow: "яка слабкість або тінь активна?"
  result: "що має змінитися в кінці?"
```

Приклад:

```yaml
SCENE_REQUEST:
  place: "BUGA_STATION біля піраміди"
  people: "Володимир, студент, старша жінка, контрольний чоловік"
  technology: "три сфери Буга, VR-окуляри, екзоскелет"
  shadow: "кожен хоче підняти сферу зі своєї внутрішньої форми"
  result: "система показує, що одна сфера стала зброєю, друга човном, третя кристалом"
```

Якщо автор дав тільки одну фразу, Router сам заповнює решту як гіпотезу, але позначає `unknown_fields`.

---

# 4. Signal Extraction

Перший крок — витягнути сигнал.

```yaml
SIGNAL:
  surface_event: "що видимо відбувається?"
  hidden_pressure: "який невидимий тиск?"
  active_world_layer:
    - human
    - machine
    - city
    - culture
    - code
  risk:
    - shadow
    - false_green
    - prion
    - drift_loss
    - human_gate_loss
```

## Приклад

```yaml
SIGNAL:
  surface_event: "людина обирає ісекай-капсулу"
  hidden_pressure: "голод до значення"
  active_world_layer:
    - culture
    - human
    - machine
  risk:
    - shadow_loop
    - return_to_zero_loss
```

---

# 5. Center Check / Bindu Before Writing

Перед +3 / -3 AI має знайти центр сцени.

```yaml
CENTER_CHECK:
  human_core: "який людський нерв?"
  main_question: "що сцена питає про людину?"
  not_about: "що не є центром, навіть якщо виглядає ефектно?"
```

## Приклад

```yaml
CENTER_CHECK:
  human_core: "дитина бачить батька сильним у капсулі й порожнім у реальності"
  main_question: "що стається з родиною, коли тінь отримує красивий світ?"
  not_about: "не про красиву технологію капсули"
```

Якщо центр не знайдено:

```yaml
BINDU_PRECHECK:
  verdict: HOLD
  reason: "human center missing"
```

---

# 6. Forward 3 — народження сцени

Forward Pass створює активний трикутник:

```text
VIOLET_MAGE → ORANGE_ARCHER → YELLOW_ENGINEER
можливість → рух → форма
```

## 6.1 Violet Mage

```yaml
violet_mage:
  question: "Яка можливість або майбутній стан відкривається?"
  output:
    future_gate: ""
    temptation: ""
    symbolic_pressure: ""
```

Питає:

```text
Що може народитися?
Яка спокуса?
Який майбутній стан уже тягне сцену?
```

Блокує:

```text
пророцтво без Guard
символ як абсолют
майбутнє без Human Gate
```

---

## 6.2 Orange Archer

```yaml
orange_archer:
  question: "Куди рухається сцена?"
  output:
    vector: ""
    scene_motion: ""
    action_candidate: ""
```

Питає:

```text
Хто рухається?
Що хоче стати дією?
Який вектор тягне героя?
```

Блокує:

```text
статичну лекцію
рух без наслідків
екшен без внутрішнього зміщення
```

---

## 6.3 Yellow Engineer

```yaml
yellow_engineer:
  question: "Яка механіка світу тримає сцену?"
  output:
    technology: ""
    mechanism: ""
    visible_interface: ""
    body_interface: ""
```

Питає:

```text
Яка технологія присутня?
Як вона читає стан?
Що видно в HUD, логах, рунах, екзоскелеті?
```

Блокує:

```text
магію без механіки
технологію без тілесного наслідку
світ без правил
```

---

# 7. Backward 3 — перевірка сцени

Backward Pass створює стабілізуючий трикутник:

```text
BLUE_GUARDIAN → GREEN_HEALER → RED_TANK
закон → баланс → тіло
```

## 7.1 Blue Guardian

```yaml
blue_guardian:
  question: "Чи є Human Gate і право на дію?"
  output:
    human_gate_present: true
    consent_or_boundary: ""
    false_green_check: ""
    unknown_status: ""
```

Питає:

```text
Хто має право діяти?
Чи AI не замінив людину?
Чи не сховали невідоме?
Чи це не false-green?
```

Блокує:

```text
дію без Human Gate
насильне спасіння
красивий дозвіл без audit
```

---

## 7.2 Green Healer

```yaml
green_healer:
  question: "Що відновлюється або не відновлюється?"
  output:
    contact: ""
    return_to_zero: true
    memory_repair: ""
    healing_without_suppression: true
```

Питає:

```text
Є контакт чи тільки комфорт?
Є шлях повернення?
Чи біль інтегрується, а не глушиться?
```

Блокує:

```text
комфорт замість healing
ідеальний рай без росту
приглушення болю як перемогу
```

---

## 7.3 Red Tank

```yaml
red_tank:
  question: "Який реальний тиск і тілесна ціна?"
  output:
    pressure: ""
    body_cost: ""
    survival_risk: ""
    what_breaks_if_allowed: ""
```

Питає:

```text
Хто платить тілом?
Що болить?
Що зламається, якщо дія пройде?
```

Блокує:

```text
естетичний ризик
романтизацію болю
дію без ціни
```

---

# 8. Bindu Verdict

Після +3 і -3 Router дає verdict.

```yaml
BINDU_VERDICT:
  options:
    KEEP:
      meaning: "сцена може бути написана або збережена"
    REWRITE:
      meaning: "ідея правильна, але сцена втратила центр або механіку"
    BLOCK:
      meaning: "сцена порушує Human Gate, романтизує біль або дає PRION"
    HOLD:
      meaning: "бракує інформації, треба зберегти Unknown"
    REROUTE:
      meaning: "сцену треба вести через іншу пелюстку або інший POV"
```

## Правила verdict

```yaml
VERDICT_RULES:
  KEEP:
    requires:
      - human_core_present
      - flower_used_as_system
      - at_least_one_real_shadow
      - technology_has_consequence
      - action_or_block_changes_character

  REWRITE:
    triggers:
      - scene_is_too_expository
      - rune_is_decorative
      - world_detail_has_no_consequence
      - emotional_resolution_too_fast

  BLOCK:
    triggers:
      - AI_replaces_human_choice
      - pain_romanticized
      - false_green_presented_as_true_healing
      - symbol_declared_absolute_truth
      - forced_salvation_without_consent

  HOLD:
    triggers:
      - unknown_fields_too_many
      - missing_human_center
      - unclear_shadow
      - no_return_path_known

  REROUTE:
    triggers:
      - wrong_point_of_view
      - scene_should_be_life_scene_not_main_plot
      - scene_should_be_dialogue_not_action
      - scene_should_be_sphere_drift_not_explanation
```

---

# 9. Scene Draft Protocol

Тільки після verdict `KEEP` або `REWRITE` AI пише сцену.

## Рекомендований порядок сцени

```text
1. Простий зовнішній кадр.
2. Малий тілесний сигнал.
3. Технологія читає стан.
4. Руна або лог зʼявляється тільки в точці вибору.
5. Тінь намагається стати дією.
6. Guard блокує або дозволяє.
7. Герой щось розуміє тілом, не лекцією.
8. Памʼять / наслідок.
```

## Мінімальна сцена має містити

```yaml
MINIMUM_SCENE_REQUIREMENTS:
  external_action: true
  body_signal: true
  rune_or_log: true
  shadow_or_false_green: true
  human_gate: true
  consequence: true
```

---

# 10. Scene Audit After Writing

Після написання AI має зробити audit.

```yaml
SCENE_AUDIT:
  human_gate_present: true
  flower_used_as_system_not_decor: true
  false_green_checked: true
  unknown_preserved: true
  pain_romanticized: false
  ai_replaced_human_choice: false
  shadow_named_or_felt: true
  action_blocked_when_needed: true
  technology_has_body_consequence: true
  memory_update_clear: true
  verdict: "KEEP | REWRITE | BLOCK | HOLD"
```

Якщо `verdict != KEEP`, AI має коротко пояснити, що саме переписати.

---

# 11. Memory Update

Після сцени треба записати, чого система навчилась.

```yaml
MEMORY_UPDATE:
  scene_id: ""
  learned_pattern: ""
  blocked_pattern: ""
  stable_rune: ""
  unstable_rune: ""
  character_shift: ""
  world_rule_reinforced: ""
```

## Приклад

```yaml
MEMORY_UPDATE:
  scene_id: "garden_of_return_child_waits"
  learned_pattern: "культура без болю памʼяті стає костюмом тіні"
  blocked_pattern: "насильне витягування людини з капсули"
  stable_rune: "∅✓"
  unstable_rune: "⟲△"
  character_shift: "герой обирає audit замість примусового спасіння"
  world_rule_reinforced: "Human Gate не можна ламати навіть заради добра"
```

---

# 12. Типові маршрути сцен

## 12.1 Pyramid False-Green Route

```yaml
ROUTE:
  signal: "місто виглядає стабільним"
  violet: "утопія можлива"
  orange: "герой рухається через площу"
  yellow: "піраміда тримає такт"
  blue: "CITY_STABLE не дорівнює Human Gate"
  green: "спокій може бути приглушенням болю"
  red: "тіло героя відчуває △"
  bindu: "HOLD або REWRITE до появи false-green proof"
```

Руни:

```text
△
FALSE_GREEN
∅╳
```

---

## 12.2 Buga Sphere Drift Route

```yaml
ROUTE:
  signal: "сфера готова, оператор підключається"
  violet: "remote body може стати новим тілом"
  orange: "рух через сферу"
  yellow: "екзоскелет + VR + Personal Node"
  blue: "чи є Human Gate?"
  green: "чи є return path?"
  red: "чи тіло витримує дріфт?"
  bindu: "◇✓ якщо BOAT_FORMED, ⊙╳ якщо NOT_A_BOAT_YET"
```

Логи:

```text
DRIFT_STATE: NOT_A_BOAT_YET
DRIFT_STATE: BOAT_FORMED
◇✓ ACTION_ALLOWED
```

---

## 12.3 Isekai Capsule Route

```yaml
ROUTE:
  signal: "людина входить у капсулу бажання"
  violet: "новий світ обіцяє друге народження"
  orange: "втеча в сценарій"
  yellow: "капсула будує персональний світ"
  blue: "чи збережений Human Gate?"
  green: "чи є return_to_zero?"
  red: "який біль змушує тікати?"
  bindu: "KEEP якщо сцена показує біль без осуду; BLOCK якщо романтизує залежність"
```

Руни:

```text
⟲△
∅╳
RETURN_TO_ZERO: false
```

---

## 12.4 Dialogue Guard Route

```yaml
ROUTE:
  signal: "людина хоче відповісти різко"
  violet: "майбутній конфлікт уже формується"
  orange: "слово хоче стати дією"
  yellow: "екзоскелет читає мікронапругу"
  blue: "чи має фраза право пройти?"
  green: "чи зберігається контакт?"
  red: "який біль активовано?"
  bindu: "⊙╳ якщо говорить тінь, ◇✓ якщо слово пройшло центр"
```

Лог:

```yaml
SPEECH_PRECOMMIT:
  phrase_candidate: "Ти нічого не розумієш"
  shadow_node: "shame"
  impulse: "attack"
  verdict: "COMMIT_BLOCKED"
```

---

## 12.5 Code-as-Protein Route

```yaml
ROUTE:
  signal: "AI згенерував красивий код"
  violet: "майбутній функціонал виглядає корисним"
  orange: "код хоче виконатися"
  yellow: "структура loops / agents / bridges"
  blue: "чи є guard_schema?"
  green: "чи є decay, cooldown, memory?"
  red: "що зламається при виконанні?"
  bindu: "REWRITE або BLOCK при misfold"
```

Руна:

```text
⟲△
FALSE_GREEN_LOOP
```

---

# 13. Режим Unknown

Якщо сцена не має достатньої інформації, AI не має вигадувати.

```yaml
UNKNOWN_MODE:
  trigger:
    - missing_place
    - unclear_shadow
    - unclear_human_gate
    - no_return_path
  action:
    - HOLD
    - ask_author_for_detail
    - or write only a sketch with unknown fields marked
```

Фраза:

> **Краще чесний HOLD, ніж красивий PRION.**

---

# 14. Як автору давати сцену коротко

Автор може писати дуже просто:

```text
Сцена: біля піраміди дитина чекає батька з капсули. Хочу, щоб було боляче, але без осуду.
```

Router перетворює це на:

```yaml
SCENE_REQUEST:
  place: "площа біля піраміди / квартал капсул"
  people: "дитина, батько в капсулі, герой"
  technology: "ісекай-капсула, VR HUD, Personal Node"
  shadow: "голод батька до значення"
  result: "герой не витягує батька силою, а бачить потребу return_to_zero"
```

---

# 15. Мінімальна памʼятка

```text
AI, перед сценою:

1. Не пиши одразу.
2. Знайди людський центр.
3. Пройди:
   violet → orange → yellow
   blue → green → red
4. Дай Bindu verdict.
5. Пиши тільки якщо KEEP або REWRITE.
6. Після сцени зроби audit.
7. Запиши memory_update.
```

---

# 16. Головна фраза Router

> **Сцена дозволена тільки тоді, коли вона має майбутнє, рух, форму, закон, баланс і тілесну ціну — і все це сходиться в Human Gate.**
