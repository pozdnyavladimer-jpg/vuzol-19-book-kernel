# 14_SCENE_PROTOCOL.md
# Вузол-19 — Scene Protocol v0.1

> **Цей файл — практичний протокол написання сцени.**  
> Він потрібен, щоб AI не просто “писав у стилі”, а проходив сцену через канон, Квітку, тінь, технологію, Human Gate, audit і memory.

---

## 1. Одне речення

**Scene Protocol перетворює ідею сцени на живий епізод роману через маршрут: центр → +3 → -3 → Bindu verdict → текст → audit → memory.**

Коротко:

```text
SCENE_IDEA
→ CENTER
→ FORWARD_3
→ BACKWARD_3
→ BINDU_VERDICT
→ SCENE_TEXT
→ POST_SCENE_AUDIT
→ MEMORY_UPDATE
```

Головне правило:

> **AI не пише сцену одразу.  
> AI спочатку перевіряє, чи сцена має право стати текстом.**

---

## 2. Коли використовувати цей файл

Цей файл використовується для:

```yaml
USE_SCENE_PROTOCOL_FOR:
  - "головна глава"
  - "життєва проміжна сцена"
  - "сцена з пірамідою"
  - "сцена зі сферою Буга"
  - "сцена дріфту"
  - "сцена капсули"
  - "діалогова сцена"
  - "сцена коду / AI Guard"
  - "фінальна сцена"
```

---

## 3. Вхідний формат

Автор може дати сцену дуже коротко.

```yaml
SCENE_REQUEST:
  place: ""
  people: ""
  technology: ""
  conflict: ""
  shadow: ""
  desired_result: ""
```

Приклад:

```yaml
SCENE_REQUEST:
  place: "BUGA_STATION біля піраміди"
  people: "Володимир, студент, старша жінка, контрольний чоловік"
  technology: "три сфери Буга, VR-окуляри, екзоскелет"
  conflict: "усі троє підключаються до однакових сфер"
  shadow: "сила, горе, контроль"
  desired_result: "сфери стають зброєю, човном і кристалом"
```

Якщо деяких полів немає, AI має позначити:

```yaml
UNKNOWN_FIELDS:
  - "..."
```

і не вигадувати як факт.

---

## 4. Крок 1 — Center

Перед написанням знайти людський центр сцени.

```yaml
CENTER:
  human_core: ""
  scene_question: ""
  what_not_to_focus_on: ""
```

### Питання

```text
Про що ця сцена на людському рівні?
Який біль або вибір у центрі?
Що виглядає ефектно, але не є центром?
```

Приклад:

```yaml
CENTER:
  human_core: "людина хоче довести силу, бо боїться бути слабкою"
  scene_question: "чи має сором право керувати сферою?"
  what_not_to_focus_on: "не про красиву технологію польоту"
```

Якщо центру немає:

```yaml
BINDU_PRECHECK:
  verdict: HOLD
  reason: "human center missing"
```

---

## 5. Крок 2 — Forward 3

Forward 3 народжує можливість сцени.

```yaml
FORWARD_3:
  violet_mage:
    future_gate: ""
    temptation: ""
    possibility: ""

  orange_archer:
    movement: ""
    action_candidate: ""
    scene_vector: ""

  yellow_engineer:
    technology: ""
    mechanism: ""
    visible_interface: ""
```

### Violet Mage

Питає:

```text
Яка можливість відкривається?
Яка спокуса?
Який майбутній стан тягне сцену?
```

### Orange Archer

Питає:

```text
Куди сцена рухається?
Що хоче стати дією?
Який імпульс рухає персонажа?
```

### Yellow Engineer

Питає:

```text
Яка технологія в сцені?
Як вона читає стан?
Що видно в HUD, логах, рунах або механіці?
```

---

## 6. Крок 3 — Backward 3

Backward 3 перевіряє сцену.

```yaml
BACKWARD_3:
  blue_guardian:
    human_gate: ""
    consent_or_boundary: ""
    unknown_status: ""
    false_green_check: ""

  green_healer:
    contact: ""
    return_to_zero: ""
    healing_or_comfort: ""

  red_tank:
    pressure: ""
    body_signal: ""
    cost: ""
```

### Blue Guardian

Питає:

```text
Хто має право діяти?
Чи AI не замінює людину?
Чи Unknown не заблоковано?
Чи немає false-green?
```

### Green Healer

Питає:

```text
Чи є контакт?
Чи є return_to_zero?
Це healing чи просто комфорт?
```

### Red Tank

Питає:

```text
Де тіло?
Де біль?
Яка ціна дії?
Що зламається, якщо дія пройде?
```

---

## 7. Крок 4 — Bindu Verdict

Після +3 / -3 сцена отримує verdict.

```yaml
BINDU_VERDICT:
  verdict: "KEEP | REWRITE | BLOCK | HOLD | REROUTE"
  reason: ""
  required_change: ""
```

### KEEP

```yaml
KEEP:
  use_when:
    - "є людський центр"
    - "технологія має наслідок"
    - "тінь або false-green перевірено"
    - "Human Gate присутній"
    - "сцена змінює людину або памʼять"
```

### REWRITE

```yaml
REWRITE:
  use_when:
    - "ідея сильна, але текст став лекцією"
    - "руни стали декором"
    - "сцена занадто швидко вирішилась"
    - "немає тілесного сигналу"
```

### BLOCK

```yaml
BLOCK:
  use_when:
    - "AI замінив Human Gate"
    - "біль романтизовано"
    - "насильне спасіння подано як добро"
    - "false-green подано як healing"
    - "символ став догмою"
```

### HOLD

```yaml
HOLD:
  use_when:
    - "бракує інформації"
    - "людський центр неясний"
    - "тінь не визначена"
    - "немає return path"
```

### REROUTE

```yaml
REROUTE:
  use_when:
    - "краще писати з іншого POV"
    - "це має бути не екшен, а діалог"
    - "це має бути не головна сцена, а побутова"
    - "сцена потребує іншої пелюстки"
```

---

## 8. Крок 5 — Написання сцени

Після verdict `KEEP` або `REWRITE` AI пише сцену.

### Рекомендований ритм

```text
1. Простий зовнішній кадр.
2. Малий тілесний сигнал.
3. Технологія читає стан.
4. Руна або лог зʼявляється в точці вибору.
5. Тінь намагається стати дією.
6. Guard блокує або дозволяє.
7. Персонаж щось розуміє тілом, не лекцією.
8. Наслідок / памʼять.
```

### Заборонений ритм

```text
1. Довга лекція.
2. Пояснення канону.
3. Красиві символи.
4. Раптовий висновок.
5. Немає зміни персонажа.
```

---

## 9. Мінімальні вимоги до сцени

```yaml
MINIMUM_SCENE_REQUIREMENTS:
  external_event: true
  human_center: true
  body_signal: true
  technology_or_world_mechanic: true
  shadow_or_false_green: true
  human_gate_question: true
  action_or_block: true
  consequence: true
```

Якщо сцена не має хоча б 5 пунктів — її треба переписати.

---

## 10. Формат відповіді AI

Коли AI пише сцену для автора, відповідь має мати 4 частини.

```yaml
AI_SCENE_RESPONSE_FORMAT:
  1_pre_scene_runtime: "короткий runtime перед текстом"
  2_scene_text: "сама сцена"
  3_post_scene_audit: "перевірка після сцени"
  4_memory_update: "що запамʼятала система"
```

### Template

```yaml
PRE_SCENE_RUNTIME:
  center: ""
  forward_3:
    violet: ""
    orange: ""
    yellow: ""
  backward_3:
    blue: ""
    green: ""
    red: ""
  bindu_verdict: ""
```

Потім:

```text
SCENE:
  ...
```

Після:

```yaml
POST_SCENE_AUDIT:
  human_gate_present: true
  flower_used_as_system_not_decor: true
  false_green_checked: true
  unknown_preserved: true
  pain_romanticized: false
  ai_replaced_human_choice: false
  shadow_named_or_felt: true
  action_blocked_when_needed: true
  technology_has_body_consequence: true
  verdict: KEEP
```

І:

```yaml
MEMORY_UPDATE:
  learned_pattern: ""
  blocked_pattern: ""
  stable_rune: ""
  unstable_rune: ""
  character_shift: ""
  world_rule_reinforced: ""
```

---

## 11. Приклад: сцена зі сферою Буга

### Input

```yaml
SCENE_REQUEST:
  place: "Drift Hall"
  people: "студент, Володимир, сфера Буга"
  technology: "Buga Sphere, VR HUD, Exoskeleton"
  conflict: "студент хоче підняти сферу швидко"
  shadow: "prove_self"
  desired_result: "NOT_A_BOAT_YET"
```

### PRE_SCENE_RUNTIME

```yaml
PRE_SCENE_RUNTIME:
  center: "студент плутає силу з правом на дію"
  forward_3:
    violet: "можливість стати пілотом"
    orange: "різкий рух до сфери"
    yellow: "екзоскелет читає мікронапругу"
  backward_3:
    blue: "Human Gate нестабільний"
    green: "return_to_zero слабкий"
    red: "сором тисне в тіло"
  bindu_verdict: "KEEP"
```

### SCENE

```text
Сфера висіла на висоті грудей, нерухома й тиха.

READY

Студент усміхнувся швидше, ніж стабілізувалося його дихання.

Володимир це побачив не очима. Окуляри лише підтвердили те, що вже сказала рука хлопця: пальці зібралися в кулак, хоча команда мала йти через відкриту долоню.

△

— Я можу, — сказав студент.

Сфера піднялася на два сантиметри й одразу різко смикнулася вбік.

Екзоскелет клацнув на його плечі.

⊙╳

DRIFT_STATE: NOT_A_BOAT_YET

— Вона ж піднялась, — видихнув хлопець.

— Ні, — сказав Володимир. — Це піднявся твій сором.

Сфера повільно опустилася назад у поле.

Вона не відмовила йому.

Вона просто не дала його тіні стати тілом.
```

### POST_SCENE_AUDIT

```yaml
POST_SCENE_AUDIT:
  human_gate_present: true
  flower_used_as_system_not_decor: true
  false_green_checked: true
  unknown_preserved: true
  pain_romanticized: false
  ai_replaced_human_choice: false
  shadow_named_or_felt: true
  action_blocked_when_needed: true
  technology_has_body_consequence: true
  verdict: KEEP
```

### MEMORY_UPDATE

```yaml
MEMORY_UPDATE:
  learned_pattern: "сфера може піднятися технічно, але дріфт не дозволено, якщо керує сором"
  blocked_pattern: "prove_self_as_pilot_skill"
  stable_rune: "⊙╳"
  unstable_rune: "△"
  character_shift: "студент вперше бачить, що сила не дорівнює дріфту"
  world_rule_reinforced: "NOT_A_BOAT_YET is a valid protection state"
```

---

## 12. Приклад: сцена з капсулою

### Input

```yaml
SCENE_REQUEST:
  place: "Garden of Return"
  people: "дитина, батько в капсулі, Володимир"
  technology: "Isekai Capsule, Pyramid Monitor"
  conflict: "батько герой у капсулі, але відсутній у реальності"
  shadow: "hero_escape"
  desired_result: "герой не витягує батька силою, а бачить проблему return_to_zero"
```

### SCENE

```text
На екрані батько стояв у золотих обладунках.

Навколо нього падали дракони, міста схиляли прапори, голоси називали його іменем так, ніби світ нарешті згадав, для чого він народився.

Під екраном сиділа дитина з аркушем паперу.

На аркуші було намальовано троє: вона, батько і маленька кругла капсула між ними.

GARDEN_STATUS: HEALING

Володимир подивився на лог довше, ніж треба.

Пірамідальний вузол не бачив конфлікту. Дитина не кричала. Медичний індекс був зелений. Капсула працювала в межах дозволеного циклу.

Потім дівчинка підняла малюнок до скла.

— Він там завжди встигає, — сказала вона. — А сюди ні.

На лівому полі окулярів знак змінився.

⟲△

RETURN_TO_ZERO: false

Володимир не торкнувся капсули.

Його рука навіть не піднялася.

▣

Human Gate.

Він не мав права витягнути людину з її болю силою тільки тому, що нарешті побачив його форму.

Але він мав право зробити інше.

— Покажи мені двері, через які він має повернутися, — тихо сказав він системі.

І вперше за весь час зелений статус Garden of Return здригнувся.
```

### MEMORY_UPDATE

```yaml
MEMORY_UPDATE:
  learned_pattern: "комфорт без return_to_zero є PRION"
  blocked_pattern: "violent rescue from capsule"
  stable_rune: "▣"
  unstable_rune: "⟲△"
  character_shift: "герой обирає return path замість насильного спасіння"
  world_rule_reinforced: "Human Gate applies even when helping"
```

---

## 13. Приклад: сцена з діалогом

```yaml
DIALOGUE_SCENE_PROTOCOL:
  trigger: "критика"
  body_signal: "затримка дихання"
  shadow: "shame"
  phrase_candidate: "Ти нічого не розумієш"
  guard: "Speech Commit Block"
  result: "контакт не зруйновано"
```

Фрагмент:

```text
— Ти помилився, — сказала вона.

Фраза вдарила не в розум.

Спочатку — в груди.

Володимир відчув, як відповідь уже збирається у роті. Красива, точна, гостра. Така, яку потім можна було б назвати правдою.

⊙

Personal Node вивів кандидат:

“Ти нічого не розумієш.”

Під ним зʼявилося друге слово.

shame

⊙╳

Він видихнув.

— Можливо, — сказав він. — Покажи мені місце, де я збрехав.
```

---

## 14. Scene Audit чекліст

Перед тим як залишити сцену, AI має відповісти:

```yaml
SCENE_AUDIT_CHECKLIST:
  1_center:
    question: "Чи є людський центр?"

  2_body:
    question: "Чи є тілесний сигнал?"

  3_shadow:
    question: "Чи тінь проявилась у дії або імпульсі?"

  4_technology:
    question: "Чи технологія щось читає, блокує або відкриває?"

  5_rune:
    question: "Чи руна функціональна?"

  6_human_gate:
    question: "Чи людина не замінена системою?"

  7_unknown:
    question: "Чи Unknown не заблоковано зарано?"

  8_consequence:
    question: "Чи є наслідок?"

  9_memory:
    question: "Що система запамʼятала?"

  10_reader:
    question: "Чи читач може впізнати себе?"
```

---

## 15. Style rules

```yaml
SCENE_STYLE_RULES:
  do:
    - "починати з конкретного кадру"
    - "показувати тіло до пояснення"
    - "давати технології короткі логи"
    - "використовувати руни рідко, але точно"
    - "залишати просту людську фразу в центрі"
    - "закінчувати зміною або памʼяттю"

  avoid:
    - "довгі пояснення"
    - "містичний туман"
    - "надлишок великих слів"
    - "руни в кожному абзаці"
    - "герой як всезнаючий пророк"
    - "AI як бог"
```

---

## 16. Діалогові правила

```yaml
DIALOGUE_RULES:
  good_dialogue:
    - "людина говорить не те, що думає, а те, що може витримати"
    - "пауза має значення"
    - "коротка фраза сильніша за лекцію"
    - "Guard може зʼявитися між двома словами"

  bad_dialogue:
    - "персонажі пояснюють канон"
    - "усі говорять однаково"
    - "немає тіла"
    - "немає ризику"
```

Приклад сильної фрази:

```text
— Він там завжди встигає. А сюди ні.
```

---

## 17. Руни в сцені

```yaml
RUNE_USAGE:
  max_per_short_scene: 1-3
  must_appear_when:
    - "commit candidate"
    - "body pressure"
    - "false-green detected"
    - "unknown allowed or blocked"
    - "action allowed"

  must_not_appear_when:
    - "немає вибору"
    - "немає ризику"
    - "це просто опис"
```

---

## 18. Scene Memory Ledger

Кожна сцена має створювати маленький запис памʼяті.

```yaml
SCENE_MEMORY_LEDGER:
  scene_id: ""
  chapter: ""
  signal: ""
  main_shadow: ""
  technology: ""
  rune: ""
  verdict: ""
  consequence: ""
  learned_rule: ""
```

Приклад:

```yaml
SCENE_MEMORY_LEDGER:
  scene_id: "student_first_buga_block"
  chapter: "5 — Не човен ще"
  signal: "student wants to lift sphere"
  main_shadow: "shame / prove_self"
  technology: "Buga Sphere + Exoskeleton"
  rune: "⊙╳"
  verdict: "BLOCK"
  consequence: "sphere does not become weapon_body"
  learned_rule: "Commit Blocked can be an act of protection, not failure"
```

---

## 19. Як AI має переписувати слабку сцену

Якщо сцена слабка, AI має не просто сказати “погано”.

Він має дати:

```yaml
REWRITE_PLAN:
  issue: ""
  missing_element: ""
  suggested_fix: ""
  new_center: ""
  new_rune: ""
```

Приклад:

```yaml
REWRITE_PLAN:
  issue: "сцена стала лекцією про капсули"
  missing_element: "людський контакт"
  suggested_fix: "показати дитину, яка чекає біля скла"
  new_center: "батько герой у симуляції, але відсутній у контакті"
  new_rune: "⟲△"
```

---

## 20. Що не можна робити

```yaml
SCENE_FORBIDDEN:
  - "писати сцену без людського центру"
  - "ставити Квітку як декор"
  - "дозволяти дії без Human Gate"
  - "робити біль красивим паливом"
  - "робити AI остаточним суддею"
  - "перетворювати капсули на карикатурне зло"
  - "робити піраміди просто магічними батарейками"
  - "забувати наслідок"
  - "закінчувати сцену без memory_update"
```

---

## 21. Короткий опис для README

```text
Scene Protocol defines how any Vuzol-19 scene should be generated:
find the human center, run +3 forward and -3 backward Flower passes, produce a Bindu verdict, write the scene, audit it and update memory.
```

---

## 22. Головна фраза файлу

> **Сцена у “Вузлі-19” — це не опис події.  
> Це момент, коли можливість просить тіло, а Квітка вирішує, чи вона не бреше.**
