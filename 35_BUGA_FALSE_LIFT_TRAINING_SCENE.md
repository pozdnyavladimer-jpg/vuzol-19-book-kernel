# 35_BUGA_FALSE_LIFT_TRAINING_SCENE.md
# Вузол-19 — Buga False Lift Training Scene v0.1

> **Жива сцена тренування пілота Сфери Буга.**  
> Тут показано головний закон: пілот не підкорює сферу — він перестає заважати природному маршруту дії.  
> Сцена демонструє false lift, тінь “prove_self”, +3 / -3 гексаграму пілота, HOLD, soft drift і перший малий октавний зсув.

---

## PRE_SCENE_RUNTIME

```yaml
SCENE_ID: "35_buga_false_lift_training_scene"
LOCATION: "Flower Lab / Buga Training Ring"
TIME: "після першої сцени з вченим"
MAIN_CHARACTER: "молодий пілот"
OBSERVERS:
  - "Володимир"
  - "Фрактальний вчений"
  - "AI sandbox observer"
SYSTEMS:
  - "Buga Sphere"
  - "Flower Runtime"
  - "Pilot Body Monitor"
  - "Octave Ascension Engine"
ACTIVE_SHADOW:
  pilot: "prove_self / shame_pressure"
  scientist: "wants to explain before listening"
  ai: "wants to classify too early"
HUMAN_GATE:
  status: "pilot must not be forced into clean drift"
BUGA_STATE:
  initial: "idle / listening"
FLOWER_ROUTE:
  +3_forward:
    - "red_tank: shame in body"
    - "orange_archer: impulse to launch"
    - "yellow_engineer: grip and posture create trajectory"
  -3_backward:
    - "blue_guardian: HOLD before unsafe lift"
    - "green_healer: breath returns"
    - "violet_mage: new pilot form becomes possible"
BINDU_VERDICT:
  expected_start: "FALSE_LIFT"
  possible_shift: "DRIFT_LOCK: SOFT"
```

---

# Сцена

Сфера Буга висіла на рівні грудей.

Вона не світилася яскраво.  
Не оберталася.  
Не кликала.

Вона просто чекала.

Під нею на підлозі було нанесене мале кільце Квітки — не повна лабораторна схема, а тренувальна версія: шість тонких ліній, один чорний центр і три вузли, що світилися слабким червоним.

Молодий пілот стояв навпроти сфери.

Його звали Тимур.

Він тримав плечі занадто рівно.  
Пальці — занадто зібрано.  
Дихання — занадто високо.

Володимир помітив це раніше, ніж HUD.

Потім HUD підтвердив.

```yaml
PILOT_BODY:
  shoulders: locked
  jaw: compressed
  breath: upper_chest
  pulse: elevated
  hand_pressure: increasing

SHADOW_CANDIDATE:
  prove_self: active
  shame_pressure: active
```

Вчений стояв збоку, біля синьої пелюстки. Він уже хотів щось сказати, але зупинився.

Володимир глянув на нього.

Вчений повільно прибрав руку від панелі.

Не час.

Сфера чекала.

— Підніми її, — сказав інструктор.

Тимур кивнув.

Надто швидко.

Його права рука піднялась до сфери. Пальці зібрались у майже кулак, хоча ніхто не просив кулак. Плечі пішли вперед. Дихання стало коротшим.

Сфера здригнулась.

Тонке помаранчеве кільце пробігло по її поверхні.

На HUD зʼявилось:

```yaml
BUGA_RESPONSE:
  lift: 0.12
  drift: unstable
  source: pressure
  status: FALSE_LIFT
```

Тимур усміхнувся.

— Вона піднялась.

Вчений закрив очі.

— Ні.

Усмішка застигла.

— Але ж...

— Це піднявся твій сором, — сказав вчений.

Тимур почервонів.

Сфера смикнулась ще раз.

```yaml
BUGA_RESPONSE:
  lift: 0.18
  tremor: rising
  shadow_coupling: high
  verdict: NOT_A_BOAT_YET
```

Цього разу HUD загорівся червоним.

Володимир зробив крок ближче, але не втрутився.

Тимур подивився на сферу так, ніби вона зрадила його перед усіма.

— Я можу, — сказав він тихо.

Це було не до них.

Це було до когось старішого в його памʼяті.

До батька.  
До тренера.  
До всіх, хто колись дивився на нього й чекав, поки він доведе право стояти в кімнаті.

Сфера це теж почула.

Не словами.

Станом.

На підлозі червона пелюстка спалахнула.

```yaml
RED_TANK:
  pressure: shame
  body_location:
    - "chest"
    - "jaw"
    - "right hand"
  question: "what is the real pressure?"
```

Вчений уже відкрив рот.

Володимир підняв руку.

— Не пояснюй.

Вчений різко глянув на нього.

— Він зараз...

— Я знаю.

— Тоді...

— Не кради його Gate.

Синя пелюстка відповіла першою.

```yaml
BLUE_GUARDIAN:
  intervention_blocked: true
  reason: "pilot must name pressure before scientist explains it"
```

Тимур стояв навпроти сфери. Його рука тремтіла.

— Що я роблю не так? — спитав він.

Вчений мовчав.

Це мовчання було для нього важчим за формулу.

Володимир відповів замість нього, але дуже тихо:

— Ти не підіймаєш сферу.

Тимур стиснув зуби.

— А що?

— Ти намагаєшся підійняти себе в очах тих, кого тут немає.

Сфера впала на два сантиметри.

Не аварійно.  
Наче видихнула.

```yaml
BUGA_RESPONSE:
  lift: 0.04
  tremor: lower
  shadow_named: partial
```

Тимур опустив очі.

Його пальці ще тримали стару форму.

Вчений нарешті сказав:

— Не розтискай їх для мене.

Тимур не рухався.

— І не для сфери, — додав вчений.

Володимир закінчив:

— Для себе.

Довга пауза.

Потім перший палець розтиснувся.

Нічого не сталося.

Потім другий.

Сфера не піднялась.

Третій.

На HUD змінився тільки один рядок.

```yaml
HAND_PRESSURE:
  decreasing: true
  command_force: falling
```

Тимур стояв у тиші.

Його сором нікуди не зник.

Це було важливо.

Якби сором зник одразу, це знову була б красива брехня.

Він лишився.

Але вперше не мав керма.

```yaml
SHADOW:
  prove_self: active
  control_over_action: reduced
```

Вчений тихо видихнув.

— Ось.

Тимур подивився на нього.

— Що “ось”?

— Тінь ще тут. Але вона вже не веде руку.

Зелена пелюстка на підлозі спалахнула мʼяко.

```yaml
GREEN_HEALER:
  return_to_zero: partial
  breath_recovery: beginning
  false_comfort: blocked
```

— Тепер дихання, — сказав Володимир.

Тимур вдихнув.

Погано.

Занадто швидко.

Видихнув.

Краще.

Сфера не рухалась.

Ще один вдих.

Ще один видих.

На третьому видиху плечі впали на пів сантиметра.

Сфера вирівняла світло.

Не піднялась.

Вирівняла.

```yaml
BUGA_RESPONSE:
  tremor: low
  lift: 0.00
  drift_field: aligning
  status: LISTENING_CLEANER
```

Тимур розсердився.

— Вона не рухається.

— Добре, — сказав вчений.

— Як це добре?

— Бо тепер вона не рухається твоєю тінню.

На підлозі помаранчева пелюстка змінила колір із різкого на теплий.

```yaml
ORANGE_ARCHER:
  old_motion: "prove_self launch"
  new_motion: "wait for clean vector"
```

Володимир підійшов ближче до Тимура.

— Тепер не піднімай її.

Тимур підняв очі.

— Що?

— Не піднімай.

— Це ж тренування.

— Так.

— І що я маю робити?

Володимир подивився на сферу.

— Дозволь їй не рухатись, поки ти не готовий.

Це речення було важче за команду.

Тимур стояв навпроти сфери й уперше не намагався перемогти кімнату.

Жовта пелюстка засвітилась.

```yaml
YELLOW_ENGINEER:
  posture: open
  trajectory_candidate: none
  structure: stable_wait
```

Вчений наблизився до панелі.

— AI, дай поточну гексаграму пілота.

На екрані зʼявилось:

```yaml
PILOT_HEXAGRAM:
  +3_FORMATION:
    red_pressure: 0.72
    orange_flow: 0.31
    yellow_structure: 0.44

  -3_VALIDATION:
    blue_law: 0.81
    green_balance: 0.52
    violet_memory: 0.38

  HEX_LOCK: 0.44
  SHADOW_GAP: 0.28
  VERDICT: HOLD
```

Тимур прочитав.

— Погано?

Вчений похитав головою.

— Чесно.

— Це різні речі?

— Найрізніші.

Володимир сказав:

— Погано було, коли сфера піднялась красиво.

Тимур довго мовчав.

Потім подивився на сферу не як на іспит.

Як на тварину, яку не можна обманути.

— Я не хочу доводити, — сказав він.

Слова вийшли погано.

Нерівно.

Майже злісно.

Але це були його слова.

Не команди.

Не кулак.

Не сором.

```yaml
HUMAN_GATE:
  pilot_statement: true
  phrase: "I do not want to prove"
  integrity: partial
```

Сфера піднялась на один сантиметр.

У кімнаті ніхто не заговорив.

Навіть вчений.

Особливо вчений.

Світло на сфері стало рівним.

```yaml
BUGA_RESPONSE:
  lift: 0.01
  tremor: none
  source: clean_statement
  status: DRIFT_LOCK_SOFT
```

Тимур завмер.

— Оце... я?

Вчений підійшов ближче.

— Ні.

Тимур знову напружився.

Вчений побачив це й одразу виправився.

— Не тільки ти.

Він показав на Квітку під ногами.

— Ти. Твоє тіло. Твоя тінь, якій не дали кермо. Закон, який не пустив її напряму. Дихання, яке повернуло баланс. Памʼять, яка тепер знає новий маршрут.

Сфера зависла рівно.

— Оце і є пілот?

Володимир відповів:

— Ні.

Тимур майже засміявся.

— Та що ж тоді?

Володимир подивився на сферу.

— Це перший раз, коли ти їй не заважав.

У центрі тренувальної Квітки загорілась чорна точка.

Не яскраво.

Просто достатньо, щоб її побачили.

```yaml
BINDU_VERDICT:
  KEEP_SMALL
  OCTAVE_SHIFT:
    from: "false lift through shame"
    to: "soft drift through named pressure"
  MEMORY_UPDATE:
    rule: "pilot can keep shame from becoming motion"
```

Вчений не плескав.

Не хвалив.

Не пояснював більше, ніж треба.

Він тільки сказав:

— Запамʼятай це. Не як перемогу.

Тимур дивився на сферу.

— А як що?

— Як маршрут назад до себе.

---

## POST_SCENE_AUDIT

```yaml
SCENE_RESULT:
  status: "KEEP"
  reason: "scene demonstrates Buga false lift, Human Gate, shadow route and soft octave shift"

WHAT_CHANGED:
  - "Тимур зрозумів, що false lift був соромом, а не майстерністю"
  - "Вчений був зупинений, щоб не пояснити замість пілота"
  - "Володимир захистив Human Gate пілота"
  - "Сфера Буга показала, що читає стан, не силу"
  - "Пілот зробив малий clean statement"
  - "DRIFT_LOCK_SOFT зʼявився без насильства"

ACTIVE_MEMORY:
  - "Buga Sphere listens to state, not command"
  - "false lift can look like success"
  - "shadow must be named before movement"
  - "pilot does not conquer sphere"
  - "first clean movement may be almost invisible"

OCTAVE_SHIFT:
  subject: "Tymur / young pilot"
  old_pattern: "prove_self → pressure → false lift"
  active_shadow: "shame_pressure"
  guard_event: "HOLD"
  new_action: "opens hand, breathes, says he does not want to prove"
  sphere_response: "DRIFT_LOCK_SOFT"
  new_octave: "octave_1_stable_flower beginning"
  status: "small but real"
```

---

## MEMORY_LEDGER_UPDATE

```yaml
MEMORY_ENTRY:
  id: "tymur_first_soft_drift"
  type: "pilot / Buga / octave"
  old_pattern: "hand pressure used to force lift"
  shadow: "prove_self"
  blocked_action: "false command through shame"
  guard: "HOLD before unsafe lift"
  new_action: "hand opens / breath lowers / statement becomes clean"
  buga_response: "DRIFT_LOCK_SOFT"
  new_rule: "first clean pilot action may look like almost no movement"
  future_warning: "do not confuse soft drift with mastery"
```

---

## AI WRITING NOTE

```yaml
AI_NOTE:
  use_this_scene_when:
    - "showing Buga training"
    - "showing false lift"
    - "showing shadow in body"
    - "showing small octave shift"
    - "showing scientist being stopped from overexplaining"

  avoid:
    - "making sphere magical"
    - "making pilot instantly healed"
    - "making clean drift dramatic too soon"
    - "letting scientist explain before pilot names pressure"
```

---

## Головна фраза сцени

> **Перший справжній рух Сфери Буга — це не коли вона злітає.  
> Це коли вона вперше не рухається твоєю тінню.**
