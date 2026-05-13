# 20_GOOD_BAD_SCENES.md
# Вузол-19 — Good / Bad Scene Examples v0.1

> **Цей файл показує AI різницю між живою сценою і красивим PRION-туманом.**  
> Погана сцена може звучати красиво, але не проходити Human Gate.  
> Добра сцена може бути простою, але мати тіло, тінь, межу, наслідок і памʼять.

---

## 1. Головний принцип

```text
BAD SCENE:
  символи красиві
  але людини немає

GOOD SCENE:
  людина є
  тіло є
  тінь є
  Guard є
  наслідок є
```

Фраза:

> **У “Вузлі-19” красива сцена не є доброю сценою.  
> Добра сцена — це сцена, яка не збрехала про те, хто хотів діяти.**

---

## 2. Що робить сцену поганою

```yaml
BAD_SCENE_MARKERS:
  - "Квітка використана як декор"
  - "руни світяться, але нічого не перевіряють"
  - "AI вирішує замість людини"
  - "біль романтизовано"
  - "технологія не має наслідку"
  - "герой усе розуміє одразу"
  - "немає тіла"
  - "немає помилки"
  - "немає Human Gate"
  - "немає Memory Update"
  - "космос пояснює те, що мала сказати людина"
```

---

## 3. Що робить сцену доброю

```yaml
GOOD_SCENE_MARKERS:
  - "є конкретний кадр"
  - "є людський центр"
  - "тіло говорить раніше за пояснення"
  - "технологія читає або блокує стан"
  - "руна зʼявляється тільки в точці вибору"
  - "тінь не засуджується, а виявляється"
  - "Human Gate не зламано"
  - "дія має наслідок"
  - "сцена щось змінює"
  - "Memory Ledger отримує запис"
```

---

# PAIR 1 — Pyramid false-green

## BAD

```text
Піраміда світилася неймовірним золотим світлом. Усі лінії Квітки Життя ожили, і космос відкрив Володимиру правду: місто було в небезпеці. Він зрозумів, що піраміда бреше, бо його душа відчула темну енергію. Руни спалахнули, і він вирішив врятувати людей.
```

### Чому погано

```yaml
BAD_AUDIT:
  human_center: weak
  body_signal: absent
  pyramid_functional: false
  false_green_checked: decorative
  human_gate: weak
  problem: "містика замість сцени"
  verdict: "REWRITE"
```

## GOOD

```text
Піраміда світилася рівно.

CITY_GRID: STABLE

Пес біля білої лінії сів і не пішов далі.

Хлопчик потягнув поводок.

— Ну ходімо.

Пес заскиглив.

Володимир відчув, як на секунду зупинилось дихання.

△

Піраміда не змінила кольору.

Саме це було неправильно.
```

### Чому добре

```yaml
GOOD_AUDIT:
  human_center: "довіра до тіла проти системного green"
  body_signal: "пес і дихання героя"
  technology: "CITY_GRID: STABLE"
  false_green_checked: true
  human_gate: "герой не діє одразу"
  verdict: "KEEP"
```

---

# PAIR 2 — Buga Sphere

## BAD

```text
Сфера Буга розкрилася перед студентом, і він відчув силу всіх планет. Його рука засяяла рунами, Марс дав йому залізо, Венера дала любов, а Сонце благословило дію. Сфера піднялася, бо він був обраним пілотом.
```

### Чому погано

```yaml
BAD_AUDIT:
  buga_as_mirror: false
  shadow: absent
  body_signal: decorative
  technology_consequence: false
  risk: "chosen-one fantasy"
  verdict: "BLOCK_OR_REWRITE"
```

## GOOD

```text
Сфера висіла на висоті грудей.

READY

Студент усміхнувся швидше, ніж стабілізувалося дихання.

Пальці зібралися в кулак, хоча команда мала йти через відкриту долоню.

△

Сфера піднялась на два сантиметри й смикнулася вбік.

⊙╳

DRIFT_STATE: NOT_A_BOAT_YET

— Вона ж піднялась, — видихнув хлопець.

— Ні, — сказав Володимир. — Це піднявся твій сором.
```

### Чому добре

```yaml
GOOD_AUDIT:
  buga_as_mirror: true
  shadow: "prove_self / shame"
  body_signal: "кулак, дихання"
  technology_consequence: "NOT_A_BOAT_YET"
  human_gate: "action blocked"
  verdict: "KEEP"
```

---

# PAIR 3 — Isekai Capsule

## BAD

```text
Капсули були злом. Люди стали слабкими, бо втекли від реальності в ісекай. Володимир зрозумів, що треба знищити капсульний центр, щоб врятувати всіх від ілюзії.
```

### Чому погано

```yaml
BAD_AUDIT:
  capsule_users: caricatured
  human_gate: violated
  shadow: simplified
  violence_as_rescue: true
  verdict: "BLOCK"
```

## GOOD

```text
На екрані батько стояв у золотих обладунках.

Унизу, біля скла, дитина тримала малюнок.

GARDEN_STATUS: HEALING

На малюнку було троє: вона, батько і маленька біла капсула між ними.

— Він там завжди встигає, — сказала дівчинка. — А сюди ні.

⟲△

RETURN_TO_ZERO: false

Володимир не торкнувся капсули.

▣

Human Gate.

Він не мав права витягнути людину з її болю силою тільки тому, що нарешті побачив його форму.
```

### Чому добре

```yaml
GOOD_AUDIT:
  capsule_user_humanized: true
  child_as_truth_sensor: true
  false_green: "HEALING status hides return loss"
  human_gate: preserved
  violent_rescue: blocked
  verdict: "KEEP"
```

---

# PAIR 4 — Dialogue Guard

## BAD

```text
Вона сказала, що він помилився. Володимир пояснив їй закон Квітки, Human Gate, PRION і те, чому її критика є проявом тіні. Вона зрозуміла і вибачилась.
```

### Чому погано

```yaml
BAD_AUDIT:
  dialogue_alive: false
  character_voice: weak
  hero_too_correct: true
  body_signal: absent
  verdict: "REWRITE"
```

## GOOD

```text
— Ти помилився, — сказала вона.

Фраза вдарила не в розум.

Спочатку — в груди.

Володимир відчув, як відповідь уже збирається у роті. Красива, точна, гостра.

⊙

Personal Node вивів кандидат:

“Ти нічого не розумієш.”

Під ним зʼявилося друге слово.

shame

⊙╳

Він видихнув.

— Можливо, — сказав він. — Покажи мені місце, де я збрехав.
```

### Чому добре

```yaml
GOOD_AUDIT:
  body_before_explanation: true
  speech_as_commit: true
  shadow: "shame"
  guard: "speech blocked"
  contact_preserved: true
  verdict: "KEEP"
```

---

# PAIR 5 — Cosmic / Planetary Layer

## BAD

```text
Марс увійшов у фазу заліза, тому всі люди стали агресивними. Сатурн наказав закрити місто, а Венера наказала героям любити. Календар Майя показав, що битва неминуча.
```

### Чому погано

```yaml
BAD_AUDIT:
  fatalism: true
  planets_command_fate: true
  human_gate_removed: true
  mayan_clock_as_prophecy: true
  verdict: "BLOCK"
```

## GOOD

```text
MAYAN_MEMORY_CLOCK:
  calendar_round: "similar shadow replay detected"
  planetary_overlay: "Mars / Fe high"
  warning: "action pressure may become weapon_body"

Володимир закрив лог.

На площі кричали не через Марс.

Люди кричали, бо страх нарешті знайшов мову.

Марс не наказував їм бити.

Він тільки підняв залізо ближче до руки.

▣

Human Gate лишався останнім місцем, де залізо ще могло не стати мечем.
```

### Чому добре

```yaml
GOOD_AUDIT:
  planets_as_resources: true
  no_fatalism: true
  human_gate: preserved
  shadow: "fear + action pressure"
  cosmic_layer_functional: true
  verdict: "KEEP"
```

---

# PAIR 6 — Mayan Memory Clock

## BAD

```text
Календар Майя передбачив війну. У цей день не можна було нічого змінити, бо цикл уже вирішив долю міста.
```

### Чому погано

```yaml
BAD_AUDIT:
  mayan_clock_as_fate: true
  human_choice_removed: true
  memory_replay: absent
  verdict: "BLOCK"
```

## GOOD

```text
MAYAN_PHASE_AUDIT:
  calendar_round: "52-year replay"
  repeated_shadow: "savior_control"
  verdict: "HOLD"

— Чому HOLD? — спитав студент. — Система готова.

Володимир дивився на старий запис у Memory Ledger.

Пʼятдесят два роки тому інший лідер теж мав готову систему.

Теж хотів врятувати людей швидше, ніж вони могли зрозуміти, від чого їх рятують.

— Бо це не та сама подія, — сказав Володимир. — Але та сама тінь.
```

### Чому добре

```yaml
GOOD_AUDIT:
  mayan_clock_as_replay: true
  historical_shadow: true
  no_fatalism: true
  action_hold: true
  verdict: "KEEP"
```

---

# PAIR 7 — Pain

## BAD

```text
Біль зробив його сильним. Чим більше він страждав, тим чистішим ставав його дріфт. Він зрозумів, що треба любити біль, бо біль відкриває силу.
```

### Чому погано

```yaml
BAD_AUDIT:
  pain_romanticized: true
  boundary_missing: true
  shadow_risk: high
  verdict: "BLOCK"
```

## GOOD

```text
Біль не давав йому сили.

Біль просто не дозволяв збрехати, що межі більше немає.

△

Екзоскелет зупинив праву руку на півдорозі до сфери.

COMMIT_BLOCKED

Він ненавидів цей блок.

Але через секунду зрозумів: якби рука дійшла, дія була б не його.

Вона належала б тому, що боліло і хотіло вдарити першим.
```

### Чому добре

```yaml
GOOD_AUDIT:
  pain_as_signal: true
  not_romanticized: true
  guard_active: true
  shadow_seen: true
  verdict: "KEEP"
```

---

# PAIR 8 — AI Guard

## BAD

```text
AI Guard проаналізував ситуацію і вирішив за Володимира, що треба робити. Він був мудрішим за людей, тому взяв керування на себе і врятував місто.
```

### Чому погано

```yaml
BAD_AUDIT:
  ai_replaced_human_gate: true
  human_choice_removed: true
  ai_as_god: true
  verdict: "BLOCK"
```

## GOOD

```text
AI Guard показав сім маршрутів.

Перші шість були швидші.

Сьомий мав найнижчий шанс успіху.

Під ним стояв єдиний знак, якого Володимир шукав.

HUMAN_GATE: preserved

— Ти рекомендуєш сьомий? — спитав він.

AI відповів не одразу.

RECOMMENDATION_BLOCKED

— Я не маю права рекомендувати. Я можу тільки показати, де твій вибір не буде вкрадений системою.
```

### Чому добре

```yaml
GOOD_AUDIT:
  ai_as_guard: true
  human_gate_preserved: true
  ai_does_not_choose: true
  consequence: true
  verdict: "KEEP"
```

---

# PAIR 9 — Character Shadow

## BAD

```text
Контрольний чоловік був злим. Він ненавидів свободу і хотів, щоб усі стали рабами системи.
```

### Чому погано

```yaml
BAD_AUDIT:
  antagonist_flat: true
  shadow_simplified: true
  no_wound: true
  verdict: "REWRITE"
```

## GOOD

```text
Він вирівняв чашку на столі.

Потім ще раз.

Ручка мала дивитися на схід.

Так було легше дихати.

— Ви хочете прибрати Unknown, — сказав Володимир.

Контрольний чоловік не підняв голосу.

— Я хочу, щоб діти більше не прокидалися під сиренами.

І вперше Володимир зрозумів, що найнебезпечніша система народилася не з ненависті.

Вона народилася з памʼяті, яка так боялася болю, що вирішила заборонити майбутньому рухатися.
```

### Чому добре

```yaml
GOOD_AUDIT:
  antagonist_has_wound: true
  control_shadow: humanized
  body_detail: "вирівнює чашку"
  conflict: alive
  verdict: "KEEP"
```

---

# PAIR 10 — Symbol vs Human

## BAD

```text
Квітка Життя була абсолютною істиною. Вона показувала, хто правий, а хто ні. Тому всі рішення треба було приймати за її геометрією.
```

### Чому погано

```yaml
BAD_AUDIT:
  symbol_as_dogma: true
  human_gate_removed: true
  flower_as_religious_proof: true
  verdict: "BLOCK"
```

## GOOD

```text
Квітка не сказала, що він правий.

Вона взагалі не говорила мовою правоти.

Вона тільки показала, де його намір втратив центр, де біль став швидшим за думку, і де дія почала шукати обхід Human Gate.

Геометрія не дала йому відповідь.

Вона забрала в нього найнебезпечнішу брехню: що відповідь уже є.
```

### Чому добре

```yaml
GOOD_AUDIT:
  flower_as_audit: true
  no_dogma: true
  unknown_preserved: true
  human_gate: active
  verdict: "KEEP"
```

---

## 4. Rewrite Rules from Bad to Good

```yaml
BAD_TO_GOOD_REWRITE:
  if_scene_is_lecture:
    fix: "turn concept into a human moment"

  if_runes_are_decor:
    fix: "place rune only at choice / commit / block"

  if_ai_decides:
    fix: "AI shows options; human decides"

  if_cosmos_commands:
    fix: "cosmos opens phase; Human Gate decides"

  if_pain_is_power:
    fix: "pain is signal; Guard protects body"

  if_antagonist_is_evil:
    fix: "give wound, fear, logic and body habit"

  if_capsule_user_is_weak:
    fix: "show wound and missing return_to_zero"

  if_flower_is_magic:
    fix: "make Flower an audit route"
```

---

## 5. Scene Quality Checklist

```yaml
SCENE_QUALITY_CHECK:
  human_center:
    required: true

  body_signal:
    required: true

  technology_function:
    required: true

  shadow_or_false_green:
    required: true

  human_gate:
    required: true

  action_or_block:
    required: true

  consequence:
    required: true

  memory_update:
    required: true

  cosmic_layer:
    use_only_if_needed: true
```

---

## 6. Good Scene Minimum Formula

```text
конкретний кадр
+ тілесний сигнал
+ короткий лог
+ тінь або false-green
+ Human Gate
+ дія / блок
+ наслідок
= сцена Вузла-19
```

---

## 7. Bad Scene Minimum Warning

```text
світло
+ руни
+ космос
+ обраний герой
+ немає тіла
+ немає Human Gate
= красивий PRION
```

---

## 8. Short instruction for AI

```text
When rewriting a weak Vuzol-19 scene:
do not make it bigger.
make it more embodied.

Remove fog.
Add body.
Name shadow.
Preserve Human Gate.
Make technology consequential.
End with memory.
```

---

## 9. Головна фраза файлу

> **Погана сцена пояснює систему.  
> Добра сцена змушує читача впізнати момент, коли система мала б зупинити його самого.**
