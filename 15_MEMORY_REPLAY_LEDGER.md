# 15_MEMORY_REPLAY_LEDGER.md
# Вузол-19 — Memory Replay Ledger v0.1

> **Цей файл описує памʼять книги як систему replay, audit і diffusion-like search.**  
> Памʼять у “Вузлі-19” — це не просто архів сцен.  
> Це поле, де AI шукає схожі патерни, відтворює наслідки, очищає шум і не дозволяє старому PRION знову пройти як “нова красива ідея”.

---

## 1. Одне речення

**Memory Replay Ledger — це журнал рішень, у якому кожна сцена, блок, помилка, rune, shadow і Bindu verdict записуються так, щоб AI міг у майбутньому шукати схожі стани й не повторювати заражені схлопування.**

Коротко:

```text
SCENE
→ AUDIT
→ VERDICT
→ MEMORY_WRITE
→ REPLAY
→ SIMILARITY_SEARCH
→ BETTER_NEXT_SCENE
```

Фраза:

> **Памʼять — це не те, що сталося.  
> Памʼять — це причина, чому дія була дозволена або заблокована.**

---

## 2. Чому це схоже на diffusion search

Так, цей файл близький до логіки diffusion.

Але не для картинки.

Для сцени.

У diffusion є:

```text
noise
→ denoise
→ pattern emerges
→ image
```

У “Вузлі-19”:

```text
сирий імпульс
→ Flower scan
→ shadow/noise removed
→ Bindu verdict
→ scene/action
```

І для памʼяті:

```text
новий scene request
→ пошук схожих патернів у ledger
→ replay good/bad examples
→ прибрати PRION-noise
→ створити чистішу сцену
```

Фраза:

> **Diffusion для картинки прибирає шум із форми.  
> Memory Replay для Вузла-19 прибирає шум із наміру.**

---

## 3. Головна різниця між архівом і Ledger

Архів зберігає:

```text
що сталося
```

Ledger зберігає:

```text
чому це сталося
чому було дозволено
чому було заблоковано
яка тінь активувалась
який Guard спрацював
яка памʼять змінилась
```

Тому Ledger потрібен AI не для цитування, а для навчання.

---

## 4. Структура запису памʼяті

```yaml
MEMORY_LEDGER_ENTRY:
  id: ""
  type: "scene | chapter | blocked_action | rewritten_scene | character_shift | world_rule"
  source_file: ""
  chapter: ""
  scene_title: ""

  signal:
    surface_event: ""
    hidden_pressure: ""

  flower_route:
    center: ""
    forward_3:
      violet: ""
      orange: ""
      yellow: ""
    backward_3:
      blue: ""
      green: ""
      red: ""

  shadow:
    main_shadow: ""
    secondary_shadow: ""
    body_signal: ""
    fast_story: ""

  technology:
    primary: ""
    secondary: ""
    mechanism_used: ""

  rune:
    stable: ""
    unstable: ""
    blocked: ""

  verdict:
    bindu: "KEEP | REWRITE | BLOCK | HOLD | REROUTE"
    reason: ""

  consequence:
    action_taken: ""
    action_blocked: ""
    memory_changed: ""

  lesson:
    learned_pattern: ""
    blocked_pattern: ""
    future_warning: ""
```

---

## 5. Мінімальний запис

Якщо сцена маленька, можна записати коротко.

```yaml
MEMORY_MIN:
  id: ""
  scene: ""
  shadow: ""
  rune: ""
  verdict: ""
  learned: ""
```

Приклад:

```yaml
MEMORY_MIN:
  id: "dog_refuses_square"
  scene: "пес не заходить на площу"
  shadow: "pyramid false-green"
  rune: "△"
  verdict: "KEEP"
  learned: "тіло або тварина може помітити брехню міста раніше за public HUD"
```

---

## 6. Типи памʼяті

```yaml
MEMORY_TYPES:
  scene_memory:
    meaning: "що навчила конкретна сцена"

  chapter_memory:
    meaning: "що змінила глава"

  blocked_action_memory:
    meaning: "який імпульс був зупинений і чому"

  prion_memory:
    meaning: "який красивий патерн виявився зараженим"

  clean_collapse_memory:
    meaning: "як дія пройшла Human Gate"

  character_memory:
    meaning: "що змінилось у персонажі"

  world_rule_memory:
    meaning: "який закон світу підтверджено"

  style_memory:
    meaning: "який стиль працює або не працює"
```

---

## 7. Diffusion-like Memory Search

Коли AI отримує новий запит на сцену, він не має писати одразу.

Він має зробити пошук памʼяті.

```yaml
MEMORY_SEARCH_PIPELINE:
  1_query_embed:
    meaning: "розкласти новий запит на place, people, technology, shadow, rune, desired_result"

  2_find_similar:
    meaning: "знайти схожі сцени, тіні, руни й verdict"

  3_replay:
    meaning: "відтворити, що було дозволено або заблоковано"

  4_denoise:
    meaning: "прибрати красивий PRION, повтори, false-green"

  5_route:
    meaning: "провести нову сцену через Flower Router"

  6_write:
    meaning: "написати сцену"

  7_audit:
    meaning: "перевірити сцену"

  8_memory_update:
    meaning: "записати новий досвід"
```

Коротко:

```text
new signal
→ search similar memory
→ replay consequences
→ denoise shadow
→ write cleaner scene
```

---

## 8. Як AI шукає схожість

AI має шукати не тільки по темі, а по патерну.

Поганий пошук:

```text
“знайди сцени про капсули”
```

Кращий пошук:

```text
“знайди сцени, де комфорт замінив контакт, return_to_zero був слабкий, а Human Gate не можна було ламати”
```

Поля схожості:

```yaml
SIMILARITY_KEYS:
  - place
  - technology
  - shadow
  - rune
  - body_signal
  - human_gate_problem
  - verdict
  - blocked_pattern
  - learned_pattern
```

---

## 9. Replay

Replay — це не повтор сцени.

Replay — це повтор причини.

```yaml
REPLAY_FUNCTION:
  input: "новий scene request"
  retrieves:
    - "схожі тіні"
    - "схожі blocked actions"
    - "схожі false-green"
    - "схожі clean collapse"
  outputs:
    - "що не повторювати"
    - "що можна використати"
    - "яку руну не ставити як декор"
    - "який Human Gate не ламати"
```

Фраза:

> **Replay не змушує сцену повторитися.  
> Replay не дає помилці вдягнути новий костюм.**

---

## 10. Denoising

Denoising у цьому Ledger означає прибрати шум із наміру.

```yaml
DENOISE_TARGETS:
  decorative_runes:
    action: "remove or make functional"

  beautiful_prion:
    action: "find false-green"

  lecture_mode:
    action: "turn concept into human scene"

  forced_resolution:
    action: "restore Unknown or HOLD"

  hero_as_god:
    action: "restore Human Gate"

  pain_romance:
    action: "restore boundary and cost"

  tech_magic:
    action: "restore mechanism"
```

Приклад:

```yaml
DENOISE_EXAMPLE:
  noisy_scene: "герой врятував усіх із капсул силою"
  detected_noise:
    - "savior_control"
    - "Human Gate loss"
    - "violent salvation"
  clean_route:
    - "відкрити return path"
    - "не витягувати силою"
    - "дати людині можливість побачити"
```

---

## 11. Memory Replay перед написанням сцени

Перед сценою AI має зробити:

```yaml
PRE_WRITE_MEMORY_REPLAY:
  scene_request: ""
  similar_memories:
    - id: ""
      reason: ""
      warning: ""
  reuse_allowed:
    - ""
  avoid:
    - ""
  suggested_rune: ""
  suggested_verdict: ""
```

Приклад:

```yaml
PRE_WRITE_MEMORY_REPLAY:
  scene_request: "дитина біля капсули"
  similar_memories:
    - id: "child_waits_father_capsule"
      reason: "return_to_zero missing, child as false-green sensor"
      warning: "do not violently rescue"
  reuse_allowed:
    - "child simple line"
    - "capsule public healing report"
  avoid:
    - "making father villain"
    - "making hero judge"
  suggested_rune: "⟲△"
  suggested_verdict: "KEEP if Human Gate preserved"
```

---

## 12. Memory Replay після сцени

Після сцени AI має записати:

```yaml
POST_SCENE_MEMORY_WRITE:
  id: ""
  scene_summary: ""
  what_worked: ""
  what_was_blocked: ""
  what_shadow_was_seen: ""
  what_future_scene_should_remember: ""
```

Приклад:

```yaml
POST_SCENE_MEMORY_WRITE:
  id: "student_not_a_boat_yet"
  scene_summary: "студент намагається підняти сферу силою"
  what_worked: "rune ⊙╳ showed protection, not failure"
  what_was_blocked: "prove_self as pilot skill"
  what_shadow_was_seen: "shame"
  what_future_scene_should_remember: "machine readiness does not equal human readiness"
```

---

## 13. Ledger для глав

```yaml
CHAPTER_LEDGER_ENTRY:
  chapter: ""
  title: ""
  main_world_rule: ""
  main_shadow: ""
  main_technology: ""
  key_rune: ""
  protagonist_shift: ""
  blocked_prion: ""
  next_chapter_seed: ""
```

Приклад:

```yaml
CHAPTER_LEDGER_ENTRY:
  chapter: 8
  title: "Сад Повернення"
  main_world_rule: "comfort without return_to_zero is PRION"
  main_shadow: "hero_escape"
  main_technology: "Isekai Capsule"
  key_rune: "⟲△"
  protagonist_shift: "hero chooses return path instead of violent rescue"
  blocked_prion: "capsule users are weak"
  next_chapter_seed: "pain is not enemy; painless life can become room without doors"
```

---

## 14. Ledger для заблокованих дій

Заблоковані дії дуже важливі.

Вони мають записуватися не як “провал”, а як захист.

```yaml
BLOCKED_ACTION_ENTRY:
  id: ""
  impulse: ""
  shadow: ""
  technology: ""
  block_reason: ""
  protected_what: ""
  future_training: ""
```

Приклад:

```yaml
BLOCKED_ACTION_ENTRY:
  id: "violent_capsule_rescue_block"
  impulse: "open capsule and pull father out"
  shadow: "savior_control"
  technology: "Isekai Capsule / Buga Sphere"
  block_reason: "Human Gate violation"
  protected_what: "user agency and return path"
  future_training: "help must restore door, not drag body"
```

Фраза:

> **Не кожен BLOCK — це поразка.  
> Іноді BLOCK — це момент, коли світ не дав тіні отримати тіло.**

---

## 15. Ledger для PRION-патернів

```yaml
PRION_PATTERN_ENTRY:
  id: ""
  pattern_name: ""
  looks_like: ""
  actually_is: ""
  common_locations:
    - ""
  detection_runes:
    - ""
  antidote: ""
```

Приклад:

```yaml
PRION_PATTERN_ENTRY:
  id: "beautiful_agreement_ai"
  pattern_name: "AI-компаньйон без межі"
  looks_like: "любов, підтримка, терапія"
  actually_is: "comfort without boundary"
  common_locations:
    - "капсули"
    - "діалоги"
    - "AI-writing"
  detection_runes:
    - "FALSE_GREEN"
  antidote: "мʼяке ні, Human Gate, Unknown Allowed"
```

---

## 16. Ledger для style memory

AI має памʼятати не тільки події, а й стиль.

```yaml
STYLE_MEMORY_ENTRY:
  works:
    - "коротка людська фраза після технічного логу"
    - "руна в момент вибору"
    - "тіло перед поясненням"
    - "дитина або тварина як false-green detector"

  fails:
    - "довга лекція"
    - "руни як декор"
    - "містичний туман"
    - "технологія без наслідку"
```

Фраза:

> **Стиль — це теж Guard.  
> Якщо стиль дозволяє туману пройти, PRION отримає красивий голос.**

---

## 17. Memory Tags

Кожен запис може мати теги.

```yaml
MEMORY_TAGS:
  petals:
    - red_tank
    - orange_archer
    - yellow_engineer
    - green_healer
    - blue_guardian
    - violet_mage
    - center_bindu

  shadows:
    - shame
    - control
    - hero_escape
    - abandonment_fear
    - painless_life
    - power_fantasy
    - beautiful_agreement
    - savior_control
    - certainty_hunger
    - grief_freeze

  technologies:
    - Pyramid_Node
    - Personal_Node
    - VR_Glasses
    - Exoskeleton
    - Buga_Sphere
    - Isekai_Capsule
    - AI_Guard
    - Memory_Ledger

  verdicts:
    - KEEP
    - REWRITE
    - BLOCK
    - HOLD
    - REROUTE

  runes:
    - "△"
    - "∅"
    - "∅✓"
    - "∅╳"
    - "▣"
    - "⊙"
    - "⊙╳"
    - "◇"
    - "◇✓"
    - "⟲"
    - "⟲△"
    - "⚠"
```

---

## 18. Memory Query Examples

```yaml
MEMORY_QUERY_EXAMPLES:
  capsule:
    query: "Find scenes where comfort replaced contact and return_to_zero was false."

  buga:
    query: "Find scenes where a Buga Sphere was technically ready but Human Gate was unstable."

  dialogue:
    query: "Find scenes where shame tried to become speech."

  pyramid:
    query: "Find scenes where city stability looked green but body signal detected pressure."

  ai:
    query: "Find scenes where AI agreed too beautifully and had to HOLD."
```

---

## 19. Replay Mode для AI

Коли AI працює над новою сценою, він має вмикати один із режимів:

```yaml
REPLAY_MODES:
  strict:
    use_when: "важлива сюжетна глава"
    behavior: "повний пошук, повний audit, memory write"

  light:
    use_when: "мала побутова сцена"
    behavior: "короткий search, короткий audit"

  repair:
    use_when: "сцена слабка або PRION"
    behavior: "знайти найближчий good pattern і переписати"

  anti_prion:
    use_when: "занадто красива сцена"
    behavior: "активно шукати false-green"

  unknown:
    use_when: "бракує даних"
    behavior: "HOLD, не вигадувати"
```

---

## 20. Memory Replay і навчання AI

AI “вчиться” не як людина і не буквально як тренування моделі в цьому файлі.

Але в межах runtime він може:

```text
читати Ledger
шукати схожі патерни
бачити минулі BLOCK
уникати старих PRION
повторювати clean collapse
писати сцени стабільніше
```

Фраза:

> **AI не стає мудрим від памʼяті.  
> AI стає менш небезпечним, якщо памʼять не дозволяє йому назвати стару помилку новою красою.**

---

## 21. Як не робити Memory Ledger

```yaml
MEMORY_FORBIDDEN:
  - "не зберігати тільки короткий сюжет"
  - "не забувати причину verdict"
  - "не стирати заблоковані дії"
  - "не робити BLOCK соромом"
  - "не перетворювати памʼять на догму"
  - "не копіювати старі сцени механічно"
  - "не дозволяти Ledger замінити Human Gate"
```

---

## 22. Памʼять теж може стати кристалом

Ledger небезпечний, якщо починає забороняти нове тільки тому, що колись було небезпечно.

```yaml
MEMORY_CRYSTAL_RISK:
  symptom:
    - "усі нові сцени блокуються"
    - "старі verdict стають догмою"
    - "Unknown не дозволяється"
    - "AI боїться ризику сильніше, ніж PRION"

  antidote:
    - "Unknown Allowed"
    - "fresh Human Gate"
    - "new context check"
    - "do not reuse verdict without audit"
```

Фраза:

> **Памʼять має не заморожувати майбутнє.  
> Памʼять має не дати майбутньому повторити стару брехню.**

---

## 23. Короткий опис для README

```text
Memory Replay Ledger stores scene and chapter decisions as searchable patterns.
It works like a diffusion-style replay system for narrative intent:
find similar shadows, denoise false-green, replay consequences, preserve Human Gate, and write cleaner future scenes.
```

---

## 24. Головна фраза файлу

> **Memory Replay — це diffusion search для наміру:  
> знайти шум, згадати наслідок, прибрати PRION і дозволити тільки ту форму, яка пройшла Human Gate.**
