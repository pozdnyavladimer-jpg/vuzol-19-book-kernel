# 26_CHARACTER_ARC_ENGINE.md
# Вузол-19 — Character Arc Engine v0.1

> **Цей файл описує, як персонаж змінюється в романі “Вузол-19”.**  
> Персонаж не змінюється тому, що “зрозумів ідею”.  
> Персонаж змінюється, коли його стара тінь більше не може проходити через Human Gate без audit.

---

## 1. Одне речення

**Character Arc Engine — це протокол розвитку персонажа: рана → маска → тінь → false-green → помилка → Guard → repair → нова дія → Memory Update.**

Коротко:

```text
WOUND
→ MASK
→ SHADOW STRATEGY
→ FALSE-GREEN SUCCESS
→ PRESSURE
→ BREAK / MISREAD
→ GUARD
→ REPAIR OR BLOCK
→ NEW ACTION
→ MEMORY UPDATE
```

Головна фраза:

> **Персонаж росте не тоді, коли отримує силу.  
> Персонаж росте тоді, коли стара сила більше не має права діяти без правди.**

---

## 2. Для чого потрібен Character Arc Engine

AI має бачити не тільки сцену, а довгу зміну людини.

```yaml
CHARACTER_ARC_ENGINE_USE:
  - "не робити героя завжди правим"
  - "не робити антагоніста просто злим"
  - "вести персонажа через повторювану тінь"
  - "показувати, як змінюється Human Gate"
  - "оновлювати Memory Ledger після ключових сцен"
  - "звʼязувати глави з внутрішньою дугою"
  - "давати AI карту розвитку, а не випадкові реакції"
```

---

## 3. Базова дуга персонажа

```yaml
CHARACTER_ARC_BASE:
  wound:
    question: "яка стара рана формує реакції?"

  mask:
    question: "якою роллю персонаж прикриває рану?"

  shadow_strategy:
    question: "як він намагається не відчути біль?"

  false_green:
    question: "де ця стратегія виглядає успішною?"

  pressure:
    question: "яка ситуація робить стару стратегію небезпечною?"

  misread:
    question: "що персонаж читає неправильно?"

  guard_event:
    question: "де дія блокується?"

  repair:
    question: "чи може персонаж повернути контакт / правду / межу?"

  new_action:
    question: "яка дія стала можлива тільки після audit?"

  memory_update:
    question: "що система запамʼятала?"
```

---

## 4. Arc verdicts

```yaml
ARC_VERDICTS:
  STABLE:
    meaning: "персонаж діє з центру"

  PRESSURE:
    meaning: "тінь активна, але ще не керує"

  MISREAD:
    meaning: "персонаж читає ситуацію через стару рану"

  FALSE_GREEN:
    meaning: "стара стратегія виглядає як успіх"

  BLOCKED:
    meaning: "Guard зупинив стару дію"

  REPAIRING:
    meaning: "персонаж визнає свою частину і повертає контакт"

  INTEGRATED:
    meaning: "персонаж робить нову дію без крадіжки Human Gate"

  REGRESSED:
    meaning: "персонаж повернувся до старого патерну"
```

---

## 5. Character Arc Card

```yaml
CHARACTER_ARC_CARD:
  character_name: ""
  core_wound: ""
  public_mask: ""
  private_fear: ""
  main_shadow: ""
  false_green_strategy: ""
  human_gate_problem: ""
  missing_axis: ""
  strongest_petal: ""
  weakest_petal: ""

  arc_start:
    state: ""
    belief: ""
    behavior: ""

  arc_pressure_points:
    - chapter: ""
      pressure: ""
      old_response: ""
      new_possible_response: ""

  arc_turning_points:
    - chapter: ""
      event: ""
      guard: ""
      memory_update: ""

  arc_end:
    state: ""
    new_belief: ""
    new_action: ""
```

---

## 6. Flower Arc Mapping

Кожен персонаж має свою сильну й слабку пелюстку.

```yaml
FLOWER_ARC_MAPPING:
  violet_mage:
    gift: "бачить можливість"
    shadow: "тікає в образ без дії"
    growth: "дати образу пройти Guard"

  orange_archer:
    gift: "рухає сцену"
    shadow: "діє швидше за правду"
    growth: "не плутати швидкість із правильністю"

  yellow_engineer:
    gift: "будує механізм"
    shadow: "ховається в системі"
    growth: "побачити людину за протоколом"

  blue_guardian:
    gift: "тримає межу"
    shadow: "робить межу тюрмою"
    growth: "межа без контролю"

  green_healer:
    gift: "відновлює контакт"
    shadow: "робить комфорт без повернення"
    growth: "healing with return_to_zero"

  red_tank:
    gift: "витримує тиск"
    shadow: "перетворює біль на броню"
    growth: "дати тілу говорити без війни"
```

---

## 7. Arc через 4D → 3D

Персонаж має багато можливостей у 4D.

Але тільки частина може стати 3D дією.

```yaml
ARC_COLLAPSE:
  4d_possibility:
    question: "ким персонаж міг би стати?"

  shadow_collapse:
    question: "яка тінь хоче схлопнути можливість у стару дію?"

  human_gate:
    question: "чи має дія право перейти в 3D?"

  new_3d_action:
    question: "що персонаж робить інакше цього разу?"
```

Фраза:

> **Дуга персонажа — це історія про те, як 4D-можливість перестає схлопуватись у стару травму.**

---

## 8. Arc через Memory Replay

Персонаж повторює не події, а патерни.

```yaml
CHARACTER_MEMORY_REPLAY:
  repeated_pattern:
    question: "яка тінь повертається в різних сценах?"

  first_time:
    question: "коли персонаж уперше зробив так?"

  current_trigger:
    question: "що активувало патерн зараз?"

  new_response:
    question: "чи зʼявилась нова дія?"

  ledger_update:
    question: "що змінилось у памʼяті?"
```

---

## 9. Рівні зміни персонажа

```yaml
ARC_CHANGE_LEVELS:
  level_0_no_change:
    meaning: "персонаж повторює стару дію"

  level_1_awareness:
    meaning: "персонаж бачить тінь, але ще діє старо"

  level_2_block:
    meaning: "Guard блокує стару дію"

  level_3_repair:
    meaning: "персонаж повертає контакт після помилки"

  level_4_new_action:
    meaning: "персонаж робить нову дію"

  level_5_teaches_without_control:
    meaning: "персонаж може допомогти іншому, не крадучи Gate"
```

---

# 10. Arc A — Володимир

## 10.1. Character Arc Card

```yaml
CHARACTER_ARC_CARD:
  character_name: "Володимир"

  core_wound: "страх, що система без Guard знову дасть тіні кермо"

  public_mask: "архітектор / той, хто бачить структуру"

  private_fear: "якщо він зупиниться, хаос пройде; якщо натисне, він сам стане контролем"

  main_shadow:
    - "savior_control"
    - "over-responsibility"
    - "trusting system structure over body signal"

  false_green_strategy:
    - "зробити правильну систему, яка не помиляється"
    - "вірити, що якщо Guard повний, люди не зламаються"

  human_gate_problem:
    - "не вирішити за інших навіть тоді, коли бачить ризик раніше за них"

  missing_axis:
    - "довіра до малих людських сигналів"
    - "прийняття Unknown без негайного протоколу"

  strongest_petal: "blue_guardian / yellow_engineer"
  weakest_petal: "green_healer / anima_receptivity"

  arc_start:
    state: "бачить систему краще, ніж контакт"
    belief: "якщо побудувати правильний Guard, поле витримає"
    behavior: "зупиняє ризик через протокол"

  arc_end:
    state: "бачить людину раніше за систему"
    new_belief: "Guard має берегти Human Gate, а не замінювати його"
    new_action: "він може HOLD, навіть коли система технічно готова"
```

## 10.2. Key pressures

```yaml
VOLODYMYR_PRESSURE_POINTS:
  chapter_1:
    event: "Піраміда зелена, пес не переходить"
    old_response: "довірити public system"
    new_response: "HOLD через body disagreement"

  capsule_episode:
    event: "батько в капсулі, дитина чекає"
    old_response: "виправити систему"
    new_response: "не витягнути людину силою"

  relationship_episode:
    event: "слово хоче стати зброєю"
    old_response: "точно пояснити"
    new_response: "спитати, де він збрехав"

  cosmic_phase_episode:
    event: "система готова, Mayan replay показує savior_control"
    old_response: "зробити правильну дію зараз"
    new_response: "HOLD, бо час підняв стару тінь"
```

## 10.3. Головна зміна

```text
Володимир починає як той, хто хоче захистити Human Gate системою.

Він має прийти до того, що Human Gate іноді захищається від самої системи.
```

Фраза:

> **Його найбільша перемога — не запустити ідеальну дію.  
> Його найбільша перемога — зупинити правильну дію, коли вона починає красти чужий вибір.**

---

# 11. Arc B — Студент / молодий пілот

## 11.1. Character Arc Card

```yaml
CHARACTER_ARC_CARD:
  character_name: "Студент / молодий пілот"

  core_wound: "страх бути слабким або невидимим"

  public_mask: "швидкий, талановитий, готовий"

  private_fear: "якщо я зупинюсь, усі побачать, що я нічого не вартий"

  main_shadow:
    - "prove_self"
    - "shame_attack"
    - "speed_as_identity"

  false_green_strategy:
    - "технічний успіх = внутрішня готовність"
    - "якщо сфера піднялась, я пілот"

  human_gate_problem:
    - "він делегує свою цінність машині"

  missing_axis:
    - "red_tank body patience"
    - "blue_guardian boundary"

  strongest_petal: "orange_archer"
  weakest_petal: "red_tank / blue_guardian"

  arc_start:
    state: "швидкість без межі"
    belief: "я існую, якщо можу довести"
    behavior: "тисне на сферу через сором"

  arc_end:
    state: "пілот, який може не запускати"
    new_belief: "затримка не принижує; вона зберігає тіло"
    new_action: "сам ставить BLOCK, коли тінь хоче керувати"
```

## 11.2. Key pressures

```yaml
STUDENT_PRESSURE_POINTS:
  first_drift:
    event: "сфера смикається, NOT_A_BOAT_YET"
    lesson: "рух не дорівнює дріфт"

  public_failure:
    event: "інші бачать його блок"
    lesson: "сором хоче зробити помилку війною"

  repair_scene:
    event: "він визнає, що хотів довести, а не пілотувати"
    lesson: "правда не вбила його"

  final_drift:
    event: "він сам зупиняє запуск"
    lesson: "пілот — це той, хто може не дати машині тіло"
```

Фраза:

> **Він хотів стати пілотом, щоб ніхто не бачив його сорому.  
> Справжнім пілотом він став тоді, коли сам побачив сором раніше за сферу.**

---

# 12. Arc C — Контрольний чоловік

## 12.1. Character Arc Card

```yaml
CHARACTER_ARC_CARD:
  character_name: "Контрольний чоловік"

  core_wound: "памʼять хаосу, де свобода коштувала життів"

  public_mask: "раціональний захисник порядку"

  private_fear: "якщо дозволити Unknown, біль повернеться"

  main_shadow:
    - "control_as_care"
    - "fear_of_unknown"
    - "order_as_anesthesia"

  false_green_strategy:
    - "якщо система стабільна, люди в безпеці"
    - "біль треба не слухати, а запобігати"

  human_gate_problem:
    - "він хоче захистити людей, забравши у них ризик вибору"

  missing_axis:
    - "green_healer contact"
    - "anima_receptivity"
    - "trust in repair"

  strongest_petal: "blue_guardian / yellow_engineer"
  weakest_petal: "green_healer / violet_mage"

  arc_start:
    state: "контроль як турбота"
    belief: "вільний Unknown повертає сирени"
    behavior: "вирівнює поле, прибирає тремтіння"

  arc_end_possible:
    state: "межа без тюрми"
    new_belief: "безпека без Human Gate стає повільною смертю"
    new_action: "дозволяє контрольований Unknown, де люди можуть навчитися repair"
```

## 12.2. Key pressures

```yaml
CONTROL_MAN_PRESSURE_POINTS:
  cup_scene:
    event: "вирівнює чашку, щоб легше дихати"
    lesson: "контроль має тілесну рану"

  pyramid_conflict:
    event: "Володимир зупиняє потік через пса"
    lesson: "малий сигнал загрожує великому порядку"

  child_scene:
    event: "дитина плаче в стабільному місті"
    lesson: "green не чує всіх"

  final_choice:
    event: "може закрити місто або дати йому пройти Unknown"
    lesson: "межа без свободи стає Hell Crystal"
```

Фраза:

> **Він не хотів влади.  
> Він хотів світу, де сирени більше не мають звуку.  
> Саме тому був небезпечний.**

---

# 13. Arc D — Дитина біля капсули

## 13.1. Character Arc Card

```yaml
CHARACTER_ARC_CARD:
  character_name: "Дитина біля капсули"

  core_wound: "дорослий присутній у віртуальному світі, але відсутній у живому контакті"

  public_mask: "тиха, слухняна, чекає"

  private_fear: "якщо просити повернення, вона стане тягарем"

  main_shadow:
    - "self-erasure"
    - "waiting_as_love"

  false_green_strategy:
    - "якщо не заважати, батько колись повернеться сам"

  human_gate_problem:
    - "дитина ще не має мови для свого Gate"

  missing_axis:
    - "permission_to_need"
    - "voice"

  strongest_petal: "green_healer"
  weakest_petal: "blue_guardian"

  arc_start:
    state: "чекає без вимоги"
    belief: "любити = не заважати"
    behavior: "тримає малюнок біля скла"

  arc_end:
    state: "може назвати потребу"
    new_belief: "моє чекання теж правда"
    new_action: "говорить дорослому прямо: сюди ти не встигаєш"
```

Фраза:

> **Вона не звинувачувала.  
> Вона просто чекала так тихо, що система назвала це стабільністю.**

---

# 14. Arc E — Батько в ісекай-капсулі

## 14.1. Character Arc Card

```yaml
CHARACTER_ARC_CARD:
  character_name: "Батько в капсулі"

  core_wound: "у реальному світі він не знає, як бути потрібним без ролі героя"

  public_mask: "втомлений, але функціональний дорослий"

  private_fear: "дитина побачить, що він не герой"

  main_shadow:
    - "hero_escape"
    - "comfort_without_return"
    - "role_addiction"

  false_green_strategy:
    - "у капсулі я сильний, значить я відновлююсь"
    - "якщо показники стабільні, я healing"

  human_gate_problem:
    - "він обирає світ, де його Gate не тестує реальна дитина"

  missing_axis:
    - "return_to_zero"
    - "ordinary_presence"

  strongest_petal: "violet_mage / orange_archer"
  weakest_petal: "green_healer / red_tank"

  arc_start:
    state: "герой там, відсутній тут"
    belief: "краще бути сильним у капсулі, ніж безпорадним у коридорі"
    behavior: "повертається втомленим, не присутнім"

  arc_end:
    state: "присутній без обладунків"
    new_belief: "дитині не потрібен мій perfect hero; їй потрібні мої двері назад"
    new_action: "скорочує цикл капсули і будує real return ritual"
```

Фраза:

> **Там він рятував міста.  
> Тут не міг встигнути до однієї дитини.**

---

# 15. Arc F — Жінка з сильним Animus-boundary

## 15.1. Character Arc Card

```yaml
CHARACTER_ARC_CARD:
  character_name: "Жінка з сильним батьківським вектором"

  core_wound: "ніжність у минулому приходила разом із контролем або слабкістю"

  public_mask: "сильна, точна, самодостатня"

  private_fear: "якщо прийму care, втрачу форму"

  main_shadow:
    - "softness_as_threat"
    - "control_through_competence"
    - "repair_as_defeat"

  false_green_strategy:
    - "я нікого не потребую, значить я вільна"
    - "якщо я перемагаю в конфлікті, я в безпеці"

  human_gate_problem:
    - "вона захищає Gate так жорстко, що не пускає живий контакт"

  missing_axis:
    - "anima_receptivity"
    - "care_without_control"

  strongest_petal: "blue_guardian / yellow_engineer"
  weakest_petal: "green_healer"

  arc_start:
    state: "межа як броня"
    belief: "ніжність забирає форму"
    behavior: "відхиляє care як вторгнення"

  arc_end:
    state: "межа як форма любові"
    new_belief: "я можу прийняти care і не здати свій Gate"
    new_action: "дозволяє близькість з умовою, а не зникає"
```

Фраза:

> **Вона не боялася болю.  
> Вона боялася, що ніжність забере в неї форму.**

---

# 16. Arc G — Чоловік із сильним Anima-field і слабким Animus-boundary

## 16.1. Character Arc Card

```yaml
CHARACTER_ARC_CARD:
  character_name: "Чоловік із сильним материнським полем"

  core_wound: "любов змішалась із тривогою і слабкою межею"

  public_mask: "чутливий, глибокий, розуміючий"

  private_fear: "якщо я скажу ні, мене покинуть"

  main_shadow:
    - "fusion"
    - "abandonment_fear"
    - "outsourced_boundary"

  false_green_strategy:
    - "якщо я все прийму, мене не залишать"
    - "партнер стане моєю формою"

  human_gate_problem:
    - "він дозволяє іншому стати його Gate, а потім злиться на втрату себе"

  missing_axis:
    - "animus_boundary"
    - "clean no"

  strongest_petal: "green_healer / violet_mage"
  weakest_petal: "blue_guardian / red_tank"

  arc_start:
    state: "контакт без межі"
    belief: "ні руйнує любов"
    behavior: "погоджується, потім накопичує образу"

  arc_end:
    state: "контакт із власною межею"
    new_belief: "ні може зберегти любов"
    new_action: "говорить межу без покарання"
```

Фраза:

> **Він не шукав жінку.  
> Він шукав межу, яка не покине його, коли він нарешті скаже “ні”.**

---

## 17. Arc across chapters

```yaml
CHAPTER_ARC_TRACKER:
  chapter_1:
    external_event: "перший false-green"
    inner_test: "чи довірити тілу проти системи?"
    arc_change: "awareness"

  chapter_2:
    external_event: "адміністратор вимагає доказ"
    inner_test: "чи може малий сигнал мати право?"
    arc_change: "pressure"

  chapter_3:
    external_event: "перша Buga / Drift помилка"
    inner_test: "швидкість vs готовність"
    arc_change: "blocked action"

  chapter_4:
    external_event: "ісекай-капсули"
    inner_test: "допомога vs насильне спасіння"
    arc_change: "Human Gate preserved"

  chapter_5:
    external_event: "relationship field trigger"
    inner_test: "слово як зброя"
    arc_change: "repair capacity"

  late_act:
    external_event: "Mayan / Planetary replay"
    inner_test: "правильний намір у неправильній фазі"
    arc_change: "HOLD as mature action"

  finale:
    external_event: "система готова до великого commit"
    inner_test: "чи не стала система новою тінню?"
    arc_change: "integrated action"
```

---

## 18. Arc audit before writing a scene

```yaml
CHARACTER_ARC_PRECHECK:
  character: ""
  current_arc_state: ""
  active_wound: ""
  active_shadow: ""
  false_green_strategy: ""
  old_action_candidate: ""
  guard_needed: ""
  new_action_possible: ""
  memory_update_if_successful: ""
```

---

## 19. Arc audit after writing a scene

```yaml
CHARACTER_ARC_POSTCHECK:
  did_character_repeat_old_pattern: true_or_false
  did_character_notice_shadow: true_or_false
  did_guard_block_old_action: true_or_false
  did_character_repair: true_or_false
  did_character_make_new_action: true_or_false
  axis_changed:
    anima_receptivity: "+0 | +1 | +2"
    animus_boundary: "+0 | +1 | +2"
    repair_capacity: "+0 | +1 | +2"
    projection_load: "-0 | -1 | -2"
  new_arc_state: ""
  memory_update: ""
```

---

## 20. Axis update rules

```yaml
AXIS_UPDATE_RULES:
  anima_receptivity_increases_when:
    - "персонаж приймає care без втрати Gate"
    - "витримує Unknown"
    - "не називає мʼякість слабкістю"
    - "слухає до відповіді"

  animus_boundary_increases_when:
    - "персонаж каже чисте ні"
    - "не делегує межу партнеру"
    - "витримує провину"
    - "блокує власну тіньову дію"

  repair_capacity_increases_when:
    - "персонаж визнає свою частину"
    - "повертає фразу з рани"
    - "пояснює паузу"
    - "не самознищується після помилки"

  human_gate_strength_increases_when:
    - "персонаж не дозволяє AI / партнеру / системі вибрати за нього"
    - "витримує чужий Gate"
    - "не краде вибір навіть із добрим наміром"

  projection_load_decreases_when:
    - "персонаж бачить реальну людину замість образу"
    - "приймає межу іншого"
    - "не робить партнера ліками"
```

---

## 21. Scene pressure by arc state

```yaml
ARC_STATE_TO_SCENE_PRESSURE:
  STABLE:
    pressure: "додай малий дисонанс"

  PRESSURE:
    pressure: "дай тіні красивий шлях"

  MISREAD:
    pressure: "покажи, що стара стратегія наче працює"

  FALSE_GREEN:
    pressure: "публічний green, приватний біль"

  BLOCKED:
    pressure: "зупини дію, але залиш біль"

  REPAIRING:
    pressure: "дай персонажу сказати просту правду"

  INTEGRATED:
    pressure: "дай нову дію без пафосу"

  REGRESSED:
    pressure: "покажи ціну повтору"
```

---

## 22. How AI should use this file

```yaml
AI_CHARACTER_ARC_USE:
  before_scene:
    - "read character card"
    - "check current arc state"
    - "identify active shadow"
    - "decide what old action wants to happen"
    - "decide what new action may become possible"

  during_scene:
    - "show old impulse"
    - "show body signal"
    - "show Guard"
    - "do not jump to full healing"

  after_scene:
    - "update only what changed"
    - "do not over-upgrade character"
    - "record memory"
```

---

## 23. Forbidden character arc patterns

```yaml
FORBIDDEN_ARCS:
  - "герой завжди правий"
  - "персонаж зцілюється за одну сцену"
  - "антагоніст просто стає добрим після пояснення"
  - "любов автоматично лікує рану"
  - "AI пояснює персонажу його дугу і все вирішено"
  - "тінь зникає без ціни"
  - "нова сила без нової відповідальності"
  - "персонаж не має права на регрес"
```

---

## 24. Good arc pattern

```text
персонаж бачить тінь
але ще не може її зупинити

потім Guard зупиняє дію
але біль лишається

потім персонаж робить repair
але не стає ідеальним

потім у схожій сцені
він робить одну малу нову дію

саме це і є розвиток
```

---

## 25. Short prompt for AI

```text
When writing a Vuzol-19 character arc:
do not make the character transform through explanation.
Track wound, mask, shadow, false-green strategy, old action, Guard event, repair and new action.
Use Memory Replay to show repeated patterns.
Update only what the scene truly changed.
Do not make love, AI or technology heal the character automatically.
Growth must appear as one new embodied action under pressure.
```

---

## 26. Головна фраза файлу

> **Дуга персонажа — це не шлях від слабкості до сили.  
> Це шлях від сили, яка брехала, до сили, яка навчилась проходити Human Gate.**
