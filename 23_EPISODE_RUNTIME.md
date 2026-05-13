# 23_EPISODE_RUNTIME.md
# Вузол-19 — Episode Runtime v0.1

> **Цей файл описує, як збирати не одну сцену, а епізод із 3–5 сцен.**  
> Сцена показує один момент схлопування.  
> Епізод показує, як тиск наростає, тінь пробує пройти, Guard блокує або дозволяє, а памʼять змінює наступну дію.

---

## 1. Одне речення

**Episode Runtime — це протокол для побудови епізоду: вхідний сигнал → перша сцена → тиск → помилка → Guard → Bindu verdict → наслідок → Memory Update.**

Коротко:

```text
EPISODE_SIGNAL
→ SCENE_1: entry / image
→ SCENE_2: pressure / temptation
→ SCENE_3: error / false-green
→ SCENE_4: Guard / Human Gate
→ SCENE_5: consequence / memory
```

Головна фраза:

> **Епізод у “Вузлі-19” — це не набір сцен.  
> Це один намір, який кілька разів просить тіло, поки Квітка не вирішить, чи він не бреше.**

---

## 2. Для чого потрібен Episode Runtime

Одна сцена може бути сильною, але роман потребує епізодів.

Епізод потрібен, коли:

```yaml
USE_EPISODE_RUNTIME_WHEN:
  - "треба показати малу сюжетну арку"
  - "треба провести героя через помилку"
  - "треба розкрити технологію через наслідок"
  - "треба показати тінь не одразу, а поступово"
  - "треба зʼєднати побутову сцену з великою системою"
  - "треба підготувати главу"
```

---

## 3. Базова структура епізоду

```yaml
EPISODE_STRUCTURE:
  scene_1_entry:
    function: "показати кадр, місце, людей, перший сигнал"
    danger: "не пояснювати все"

  scene_2_pressure:
    function: "підняти тиск, спокусу, бажання дії"
    danger: "дати герою занадто легку правоту"

  scene_3_misread:
    function: "показати false-green, помилку або красиву брехню"
    danger: "зробити помилку дурною"

  scene_4_guard:
    function: "Human Gate, блок, HOLD або перепис маршруту"
    danger: "AI або символ вирішує за людину"

  scene_5_memory:
    function: "наслідок, зміна, запис у Ledger"
    danger: "закінчити без памʼяті"
```

---

## 4. Формула епізоду

```text
один сигнал
+ одна активна тінь
+ одна технологія
+ один Human Gate problem
+ один Bindu verdict
+ один Memory Update
= епізод
```

Не треба в один епізод класти все:

```yaml
EPISODE_OVERLOAD_FORBIDDEN:
  - "всі планети"
  - "весь календар Майя"
  - "усіх персонажів"
  - "всю історію світу"
  - "всі тіні"
  - "всі технології"
```

---

## 5. Episode Request Template

Автор або AI може ставити епізод так:

```yaml
EPISODE_REQUEST:
  title: ""
  chapter_link: ""
  episode_function: ""
  main_signal: ""
  main_shadow: ""
  characters:
    - ""
  location: ""
  technology:
    - ""
  desired_turn: ""
  final_memory: ""
```

Приклад:

```yaml
EPISODE_REQUEST:
  title: "Пес біля білої лінії"
  chapter_link: "Chapter 1 — Піраміда світилася правильно"
  episode_function: "показати перший false-green міста"
  main_signal: "CITY_GRID: STABLE, але тіло не згодне"
  main_shadow: "painless stability"
  characters:
    - "Володимир"
    - "хлопчик"
    - "пес"
    - "пірамідальний адміністратор"
  location: "Pyramid Square"
  technology:
    - "Pyramid Node"
    - "Public HUD"
    - "Personal Node"
  desired_turn: "герой не переходить лінію"
  final_memory: "system calm is not truth"
```

---

## 6. Episode Runtime Output Format

AI має відповідати так:

```yaml
EPISODE_RUNTIME_OUTPUT:
  EPISODE_PRECHECK:
    title: ""
    episode_type: ""
    chapter_link: ""
    center: ""
    main_shadow: ""
    main_technology: ""
    human_gate_problem: ""
    bindu_target: ""

  EPISODE_MAP:
    scene_1: ""
    scene_2: ""
    scene_3: ""
    scene_4: ""
    scene_5: ""

  SCENE_DRAFTS:
    scene_1: ""
    scene_2: ""
    scene_3: ""
    scene_4: ""
    scene_5: ""

  EPISODE_AUDIT:
    ""

  MEMORY_UPDATE:
    ""
```

---

## 7. Episode Types

```yaml
EPISODE_TYPES:
  life_episode:
    meaning: "малий побутовий епізод"
    scenes: 3
    example: "дитина біля капсули"

  tech_episode:
    meaning: "технологія відкривається через наслідок"
    scenes: 3-5
    example: "перший Drift Hall"

  shadow_episode:
    meaning: "персонаж зустрічає свою тінь"
    scenes: 4-5
    example: "студент і сором"

  city_episode:
    meaning: "піраміда / місто / public false-green"
    scenes: 4-5
    example: "Піраміда світилася правильно"

  cosmic_episode:
    meaning: "планетарний або Mayan phase audit"
    scenes: 5
    example: "час не дозволяє насильне спасіння"

  chapter_episode:
    meaning: "ядро глави"
    scenes: 5-7
    example: "Сад Повернення"
```

---

## 8. Три-сценний епізод

Для коротких епізодів:

```yaml
THREE_SCENE_EPISODE:
  scene_1:
    name: "Signal"
    function: "зовнішній кадр + перший тиск"

  scene_2:
    name: "Misread"
    function: "людина або система неправильно читає сигнал"

  scene_3:
    name: "Guard"
    function: "Bindu verdict + наслідок + memory"
```

Приклад:

```text
1. Дитина чекає біля капсули.
2. Операторка каже: GARDEN_STATUS: HEALING.
3. Володимир бачить RETURN_TO_ZERO: false і не витягує батька силою.
```

---

## 9. Пʼяти-сценний епізод

Для головних епізодів:

```yaml
FIVE_SCENE_EPISODE:
  scene_1_entry:
    question: "де ми і що зовні спокійне?"

  scene_2_pressure:
    question: "що хоче стати дією?"

  scene_3_false_green:
    question: "де система каже green, але тіло не згодне?"

  scene_4_guard:
    question: "що блокується або отримує HOLD?"

  scene_5_memory:
    question: "що змінилося в людині, системі або Ledger?"
```

---

## 10. Episode Flower Route

Епізод має проходити через Квітку не один раз, а хвилею.

```yaml
EPISODE_FLOWER_ROUTE:
  opening:
    petal: "violet_mage"
    function: "показати можливість"

  movement:
    petal: "orange_archer"
    function: "пустити сцену в рух"

  mechanism:
    petal: "yellow_engineer"
    function: "показати технологію"

  boundary:
    petal: "blue_guardian"
    function: "поставити питання права"

  contact:
    petal: "green_healer"
    function: "перевірити return_to_zero"

  cost:
    petal: "red_tank"
    function: "показати тіло, біль, ціну"

  center:
    petal: "bindu"
    function: "verdict"
```

---

## 11. Episode Memory Replay

Перед епізодом AI має зробити replay.

```yaml
EPISODE_MEMORY_REPLAY:
  search_for:
    - "similar shadow"
    - "similar technology"
    - "similar human_gate_problem"
    - "similar false_green"
    - "similar blocked action"

  output:
    reuse:
      - ""
    avoid:
      - ""
    warning:
      - ""
```

Приклад:

```yaml
EPISODE_MEMORY_REPLAY:
  episode: "Capsule father"
  reuse:
    - "child simple line"
    - "public HEALING status"
    - "RETURN_TO_ZERO false"
  avoid:
    - "father as villain"
    - "violent rescue"
    - "lecture about addiction"
  warning:
    - "comfort can look like care while removing return"
```

---

## 12. Episode Audit

Після епізоду:

```yaml
EPISODE_AUDIT:
  has_clear_signal: true
  has_human_center: true
  has_progression: true
  pressure_increases: true
  shadow_deepens: true
  technology_has_consequence: true
  human_gate_preserved: true
  false_green_checked: true
  ending_changes_memory: true
  no_cosmic_overload: true
  verdict: "KEEP | REWRITE | BLOCK | HOLD | REROUTE"
```

---

## 13. Episode Memory Update

```yaml
EPISODE_MEMORY_UPDATE:
  episode_id: ""
  chapter: ""
  main_signal: ""
  main_shadow: ""
  technology: ""
  blocked_pattern: ""
  clean_pattern: ""
  character_shift: ""
  world_rule_reinforced: ""
  next_episode_seed: ""
```

Приклад:

```yaml
EPISODE_MEMORY_UPDATE:
  episode_id: "pyramid_white_line"
  chapter: "1 — Піраміда світилася правильно"
  main_signal: "CITY_GRID: STABLE vs dog refusal"
  main_shadow: "painless stability"
  technology: "Pyramid Node / Personal Node"
  blocked_pattern: "trust public green without body disagreement"
  clean_pattern: "HOLD before crossing line"
  character_shift: "Volodymyr trusts body signal over public green"
  world_rule_reinforced: "system calm is not truth"
  next_episode_seed: "administrator asks why he stopped the flow"
```

---

# 14. Example Episode A — Піраміда світилася правильно

## EPISODE_PRECHECK

```yaml
EPISODE_PRECHECK:
  title: "Піраміда світилася правильно"
  episode_type: "city_episode"
  chapter_link: "Chapter 1"
  center: "тіло не вірить системному green"
  main_shadow: "false-green / painless stability"
  main_technology: "Pyramid Node"
  human_gate_problem: "чи можна переходити межу, коли система дозволяє, але тіло ні?"
  bindu_target: "HOLD"
```

## EPISODE_MAP

```yaml
EPISODE_MAP:
  scene_1_entry:
    title: "Зелена площа"
    function: "показати спокій міста"

  scene_2_pressure:
    title: "Пес не переходить"
    function: "тіло не погоджується"

  scene_3_false_green:
    title: "CITY_GRID: STABLE"
    function: "система не має поля для малого болю"

  scene_4_guard:
    title: "Володимир не переходить лінію"
    function: "HOLD як перша правильна дія"

  scene_5_memory:
    title: "Адміністратор питає"
    function: "перший конфлікт із public logic"
```

## Ключовий фінал

```text
Піраміда світилася правильно.

Саме це було неправильно.
```

---

# 15. Example Episode B — Не човен ще

## EPISODE_PRECHECK

```yaml
EPISODE_PRECHECK:
  title: "Не човен ще"
  episode_type: "tech_episode / drift_episode"
  chapter_link: "Chapter 5"
  center: "студент хоче довести силу через сферу"
  main_shadow: "shame / prove_self"
  main_technology: "Buga Sphere + Exoskeleton"
  human_gate_problem: "чи має сором право керувати remote body?"
  bindu_target: "BLOCK"
```

## EPISODE_MAP

```yaml
EPISODE_MAP:
  scene_1_entry:
    title: "READY"
    function: "сфера технічно готова"

  scene_2_pressure:
    title: "Кулак"
    function: "тіло показує сором"

  scene_3_misread:
    title: "Вона ж піднялась"
    function: "студент плутає технічний рух із дріфтом"

  scene_4_guard:
    title: "NOT_A_BOAT_YET"
    function: "сфера блокує тінь"

  scene_5_memory:
    title: "Це піднявся твій сором"
    function: "перший урок пілота"
```

## Ключова фраза

```text
Сфера не відмовила йому.

Вона просто не дала його тіні стати тілом.
```

---

# 16. Example Episode C — Сад Повернення

## EPISODE_PRECHECK

```yaml
EPISODE_PRECHECK:
  title: "Сад Повернення"
  episode_type: "capsule_episode / life_episode"
  chapter_link: "Chapter 8"
  center: "дитина чекає контакт, а система бачить healing"
  main_shadow: "hero_escape / comfort without return"
  main_technology: "Isekai Capsule"
  human_gate_problem: "чи можна витягнути людину з болю силою?"
  bindu_target: "HOLD"
```

## EPISODE_MAP

```yaml
EPISODE_MAP:
  scene_1_entry:
    title: "Герой на екрані"
    function: "батько має значення всередині капсули"

  scene_2_pressure:
    title: "Дитина з малюнком"
    function: "контакт відсутній зовні"

  scene_3_false_green:
    title: "GARDEN_STATUS: HEALING"
    function: "комфорт маскує return_to_zero false"

  scene_4_guard:
    title: "Володимир не торкається капсули"
    function: "violent rescue blocked"

  scene_5_memory:
    title: "Де двері назад?"
    function: "герой шукає return path"
```

## Ключова фраза

```text
Він не мав права витягнути людину з її болю силою тільки тому, що нарешті побачив його форму.
```

---

# 17. Example Episode D — Час не дає кермо

## EPISODE_PRECHECK

```yaml
EPISODE_PRECHECK:
  title: "Час не дає кермо"
  episode_type: "cosmic_episode"
  chapter_link: "late act 2 / act 3"
  center: "герой хоче зробити правильну дію в неправильний час"
  main_shadow: "savior_control"
  main_technology: "Mayan Memory Clock + Planetary Resource Clock"
  human_gate_problem: "чи може правильний намір стати насильним спасінням через фазу?"
  bindu_target: "HOLD"
```

## EPISODE_MAP

```yaml
EPISODE_MAP:
  scene_1_entry:
    title: "Система готова"
    function: "усі технічні умови дозволяють дію"

  scene_2_pressure:
    title: "Місто боїться"
    function: "соціальна фаза нестабільна"

  scene_3_replay:
    title: "52-YEAR SHADOW MATCH"
    function: "попередній цикл показує savior_control"

  scene_4_guard:
    title: "HOLD"
    function: "час не наказує, але попереджає"

  scene_5_memory:
    title: "Та сама тінь"
    function: "герой не повторює стару реформу-контроль"
```

## Ключова фраза

```text
Це не та сама подія.

Але та сама тінь.
```

---

## 18. Episode pacing

```yaml
EPISODE_PACING:
  scene_1:
    energy: "low / clear / image"

  scene_2:
    energy: "rising / body"

  scene_3:
    energy: "conflict / misread"

  scene_4:
    energy: "stop / Guard"

  scene_5:
    energy: "quiet / consequence / memory"
```

Правило:

> **Найсильніший момент епізоду не завжди там, де найбільше дії.  
> Часто він там, де дія не проходить.**

---

## 19. How to connect episodes

Кожен епізод має залишати seed для наступного.

```yaml
EPISODE_CHAINING:
  previous_memory:
    becomes: "next pressure"

  blocked_action:
    becomes: "future temptation"

  new_rule:
    becomes: "future test"

  character_shift:
    becomes: "new conflict"

  unresolved_unknown:
    becomes: "next episode entry"
```

Приклад:

```text
Episode 1:
  dog refuses white line
  memory: system calm is not truth

Episode 2:
  administrator demands evidence
  pressure: body signal vs public logic

Episode 3:
  Personal Node starts recording private disagreement
  pressure: can private pain enter civic protocol?
```

---

## 20. Episode forbidden patterns

```yaml
EPISODE_FORBIDDEN:
  - "епізод без зміни"
  - "кожна сцена пояснює одну й ту саму ідею"
  - "Guard зʼявляється тільки в кінці без підготовки"
  - "технологія не має наслідку"
  - "герой завжди правий"
  - "антагоніст просто не розуміє"
  - "космос використано для сцени, яку міг вирішити один живий діалог"
  - "немає Memory Update"
```

---

## 21. Episode repair

Якщо епізод слабкий:

```yaml
EPISODE_REPAIR:
  if_flat:
    fix: "add pressure step"

  if_too_expository:
    fix: "turn one explanation into body scene"

  if_no_change:
    fix: "add blocked action or memory shift"

  if_too_big:
    fix: "split into two episodes"

  if_too_cosmic:
    fix: "replace cosmic explanation with local consequence"

  if_too_mechanical:
    fix: "add human line and body hesitation"
```

---

## 22. Short prompt for AI

```text
Build a Vuzol-19 episode, not just a scene.

Use 3-5 scenes.
Keep one main signal, one main shadow, one main technology and one Human Gate problem.
Scene 1: entry image.
Scene 2: pressure.
Scene 3: misread or false-green.
Scene 4: Guard / Bindu verdict.
Scene 5: consequence / Memory Update.

Do not overload the episode with all concepts.
If cosmic layer is not necessary, keep the episode human and local.
End with a Memory Update that seeds the next episode.
```

---

## 23. Головна фраза файлу

> **Епізод — це коли сцени перестають бути окремими кадрами і стають одним випробуванням: чи пройде намір через час, тіло, тінь і Human Gate без брехні.**
