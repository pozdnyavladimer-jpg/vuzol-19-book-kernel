# 17_MAYAN_MEMORY_CLOCK.md
# Вузол-19 — Mayan Memory Clock v0.1

> **Цей файл описує календарі Майя як ритмічний Memory Clock для роману.**  
> Це не пророцтво і не фаталізм.  
> У “Вузлі-19” Mayan Memory Clock — це **часова сітка replay**, яка показує, коли певний намір, ресурс або тінь знову входять у фазу.

---

## 1. Одне речення

**Mayan Memory Clock — це система вкладених циклів, яка не передбачає події напряму, а сканує повернення станів: наміру, тіні, ресурсу, покоління, планетарної фази й цивілізаційної памʼяті.**

Коротко:

```text
Tzolk’in = внутрішня хвиля наміру
Haab’ = земна / соціальна хвиля
Calendar Round = поколінний replay
Long Count = deep archive
Venus / 819 Count = planetary overlay
Flower = audit
Human Gate = permission
```

Фраза:

> **Майя рахували не кінець світу.  
> Вони рахували, коли світ знову забуде, що вже проходив цю тінь.**

---

## 2. Головна межа

У цьому романі календар Майя не означає:

```yaml
NOT_THIS:
  - "магічний наказ"
  - "фатальна доля"
  - "автоматичне передбачення війни"
  - "дата, яка змушує людину діяти"
  - "заміна Human Gate"
```

Він означає:

```yaml
THIS:
  - "фазовий audit часу"
  - "memory replay цивілізації"
  - "сітка повернення патернів"
  - "інструмент бачення повторної тіні"
  - "календар наміру, ресурсу і наслідку"
```

Головне правило:

> **Час відкриває фазу.  
> Але тільки Human Gate дозволяє дію.**

---

## 3. Чому календар саме такий

Календар Майя сильний тим, що це не один календар, а система коліс.

```yaml
MAYAN_CLOCK_LAYERS:
  inner_cycle:
    name: "Tzolk’in"
    length: 260
    function: "намір / тон / знак / внутрішній ритм"

  earth_cycle:
    name: "Haab’"
    length: 365
    function: "сонячний рік / тіло / сезон / соціум"

  generational_cycle:
    name: "Calendar Round"
    length: 18980
    function: "52-річний replay / покоління / повернення комбінації"

  deep_archive:
    name: "Long Count"
    function: "довга памʼять / цивілізаційна адреса"

  planetary_overlay:
    names:
      - "Venus Table"
      - "819-day Count"
    function: "планетарні фази / resource overlay / видимі цикли"
```

Фраза:

> **Це не календар днів.  
> Це машина синхронізації шарів.**

---

## 4. Tzolk’in — 260 днів

Tzolk’in складається з:

```text
13 tones × 20 day-signs = 260 unique states
```

У “Вузлі-19”:

```yaml
TZOLKIN:
  role: "inner intent wave"
  reads:
    - "який тон наміру активний"
    - "яка форма знаку несе цей тон"
    - "чи це слухання, дія, очищення, межа або replay"

  maps_to:
    flower_layer: "internal Flower"
    human_layer: "psychological phase"
    ai_layer: "intent precheck"
```

Тобто Tzolk’in не питає:

```text
яка сьогодні дата?
```

Він питає:

```text
який тип наміру сьогодні легше прокидається?
```

Фраза:

> **Tzolk’in не рахував дні.  
> Він рахував, у якій формі намір входить у людину.**

---

## 5. 13 тонів

13 тонів можна читати як хвилю розвитку наміру.

```yaml
THIRTEEN_TONES:
  1:
    name: "seed / start"
    function: "намір народжується"

  2:
    name: "polarity"
    function: "зʼявляється інша сторона"

  3:
    name: "motion"
    function: "намір отримує рух"

  4:
    name: "form"
    function: "ставиться межа"

  5:
    name: "power"
    function: "зʼявляється ресурс"

  6:
    name: "flow"
    function: "намір входить у ритм"

  7:
    name: "mirror / midpoint"
    function: "центр хвилі, перевірка відображення"

  8:
    name: "harmony"
    function: "баланс і корекція"

  9:
    name: "completion_pressure"
    function: "сенс вимагає зрілості"

  10:
    name: "manifest"
    function: "форма майже отримує тіло"

  11:
    name: "release"
    function: "очищення зайвого"

  12:
    name: "understanding"
    function: "інтеграція"

  13:
    name: "transition"
    function: "перехід у нову хвилю"
```

У романі це можна спростити:

```text
1-3   = birth / outward impulse
4-6   = structure / movement
7     = mirror / Bindu check
8-10  = harmony / manifestation
11-13 = release / memory / transition
```

---

## 6. 20 знаків

20 знаків можна читати як алфавіт форм.

У каноні не треба жорстко копіювати історичні значення.  
Для AI достатньо зробити функціональний шар:

```yaml
TWENTY_SIGNS_AS_FUNCTIONS:
  1_imix:
    function: "первинна вода / матриця / народження"

  2_ik:
    function: "вітер / голос / сигнал"

  3_akbal:
    function: "ніч / внутрішній простір / тінь"

  4_kan:
    function: "зерно / ресурс / потенціал"

  5_chicchan:
    function: "життєва сила / тіло / інстинкт"

  6_cimi:
    function: "смерть форми / перехід"

  7_manik:
    function: "рука / дія / healing"

  8_lamat:
    function: "зірка / краса / гармонія"

  9_muluk:
    function: "вода / обмін / жертва"

  10_ok:
    function: "собака / вірність / звʼязок"

  11_chuwen:
    function: "мавпа / гра / мистецтво / код"

  12_eb:
    function: "дорога / людина / шлях"

  13_ben:
    function: "очерет / вісь / дім / канал"

  14_ix:
    function: "ягуар / інтуїція / нічний Guard"

  15_men:
    function: "орел / бачення / масштаб"

  16_kib:
    function: "сова / памʼять / очищення"

  17_kaban:
    function: "земля / рух / тектоніка"

  18_etznab:
    function: "кремінь / дзеркало / різання брехні"

  19_kawak:
    function: "буря / очищення / грім"

  20_ajaw:
    function: "сонце / центр / влада / Bindu"
```

Фраза:

> **13 давало хвилю.  
> 20 давало форму.  
> 260 давало мову наміру.**

---

## 7. Haab’ — 365 днів

Haab’ — сонячний рік.

```yaml
HAAB:
  length: 365
  structure: "18 × 20 + 5 Wayeb"
  role: "Earth/social body wave"
  reads:
    - "сезон"
    - "побут"
    - "міський такт"
    - "соціальний ритм"
    - "тіло року"
```

У “Вузлі-19” Haab’ — це не внутрішній намір, а зовнішній ритм:

```text
їжа
робота
місто
площа
ритуал
транспорт
погода
соціальна памʼять
```

Фраза:

> **Tzolk’in показував, що входить у людину.  
> Haab’ показував, у яке тіло року це входить.**

---

## 8. Wayeb — 5 днів

Wayeb — пʼять додаткових днів.

У романі це дуже сильний режим:

```yaml
WAYEB:
  role: "purge / reset / unstable unknown"
  danger:
    - "старі Guard слабшають"
    - "памʼять піднімає незакриті патерни"
    - "false-green легко маскується під очищення"
    - "тінь хоче швидкий commit"

  clean_use:
    - "HOLD"
    - "audit"
    - "memory review"
    - "не запускати великі дії без Human Gate"
```

Руна:

```text
∅✓
HOLD
```

Фраза:

> **Wayeb був не порожнечею.  
> Wayeb був пʼятьма дверима, які не можна відкривати поспіхом.**

---

## 9. Calendar Round — 52 роки

Tzolk’in і Haab’ разом повторюють ту саму комбінацію через:

```text
18,980 days = 73 × 260 = 52 × 365
```

У “Вузлі-19” це:

```yaml
CALENDAR_ROUND:
  role: "generational memory replay"
  meaning:
    - "людина встигає прожити цикл і побачити повернення патерну"
    - "суспільство повторює не подію, а тінь"
    - "мода, війни, ідеології, технології повертаються в новому костюмі"
```

Фраза:

> **52 роки — це не просто повтор дати.  
> Це час, за який тінь встигає забути власне імʼя і повернутися як нова ідея.**

---

## 10. Long Count — Deep Archive

Long Count потрібен, бо 52-річний replay сам по собі повторюється.

```yaml
LONG_COUNT:
  role: "deep archive / civilization memory address"
  function:
    - "дати події абсолютну адресу"
    - "не загубити цикл у повторенні"
    - "зберегти цивілізаційну памʼять"
```

У системі Вузла:

```text
Calendar Round = Memory Replay
Long Count = Memory Ledger Address
```

Фраза:

> **Без Long Count повтор виглядає як новина.  
> З Long Count повтор стає памʼяттю.**

---

## 11. Venus Table — ресурс Венери

Venus cycle у романі — це не “любовний гороскоп”.

Це resource overlay:

```yaml
VENUS_TABLE:
  symbolic_metal: "Copper / Cu"
  resource:
    - "звʼязок"
    - "краса"
    - "престиж"
    - "любов"
    - "приваблення"
    - "соціальний магнетизм"

  shadow:
    - "красива згода"
    - "любов без межі"
    - "естетична війна"
    - "культура як DLC"
```

Фраза:

> **Венера не наказувала любити.  
> Вона відкривала ресурс звʼязку.  
> А тінь вирішувала, чи стане звʼязок любовʼю, пасткою або війною за красу.**

---

## 12. 819-day Count — Planetary Overlay

819-day Count у каноні можна подати як складніший планетарний overlay.

```yaml
EIGHT_ONE_NINE_COUNT:
  role: "planetary overlay grid"
  function:
    - "накласти видимі планетарні цикли на довшу фазу"
    - "побачити не одну орбіту, а систему повторів"
    - "знайти resource glyph, який не видно в короткому відрізку"
```

Фраза:

> **Короткий цикл показував рух.  
> Довгий overlay показував форму руху.**

Це прямо зʼєднується з `16_PLANETARY_RESOURCE_CLOCK.md`.

---

## 13. Mayan Clock + Planetary Resource Clock

```yaml
MAYAN_PLUS_PLANETARY:
  planetary_resource_clock:
    asks: "який ресурс активний?"
    examples:
      - "Mars / Fe / action"
      - "Venus / Cu / contact"
      - "Saturn / Pb / boundary"
      - "Mercury / Hg / signal"

  mayan_memory_clock:
    asks: "коли цей ресурс входить у replay?"
    examples:
      - "Tzolk’in phase"
      - "Haab body"
      - "Wayeb purge"
      - "52-year repeat"
      - "Long Count address"
```

Коротко:

```text
Planet = resource
Orbit = rhythm
Mayan Calendar = memory cycle
Flower = audit
Human Gate = permission
```

---

## 14. Flower + Mayan Clock

Квітка перевіряє простір і психологію.

Mayan Clock перевіряє час і replay.

```yaml
FLOWER_AND_MAYAN_CLOCK:
  Flower:
    asks:
      - "хто хоче діяти?"
      - "яка тінь активна?"
      - "чи є Human Gate?"
      - "чи дія має право пройти?"

  Mayan_Clock:
    asks:
      - "яка зараз фаза?"
      - "який патерн повторюється?"
      - "який ресурс входить у час?"
      - "чи це стара тінь у новій формі?"
```

Фраза:

> **Квітка питає: хто хоче діяти?  
> Календар питає: чи цей намір має правильний час?**

---

## 15. Mayan Phase Audit

Перед великою дією AI або герой має зробити Mayan Phase Audit.

```yaml
MAYAN_PHASE_AUDIT:
  current_scene: ""
  tzolkin_state:
    tone: ""
    sign: ""
    intent_wave: ""

  haab_state:
    season_body: ""
    social_pressure: ""

  wayeb_status:
    active: false
    purge_warning: ""

  calendar_round:
    replay_detected: ""
    similar_generation_pattern: ""

  long_count:
    deep_memory_address: ""

  planetary_overlay:
    dominant_resource: ""
    metal: ""
    shadow_risk: ""

  flower_crosscheck:
    human_gate: ""
    shadow: ""
    verdict: ""
```

---

## 16. Приклад audit: дія проти піраміди

```yaml
MAYAN_PHASE_AUDIT_EXAMPLE:
  current_scene: "герой хоче втрутитися в Pyramid Grid"

  tzolkin_state:
    tone: "manifest pressure"
    sign: "flint / mirror"
    intent_wave: "дія хоче різати брехню"

  haab_state:
    season_body: "місто у фазі публічного спокою"
    social_pressure: "люди не готові бачити біль"

  wayeb_status:
    active: true
    purge_warning: "велика дія може стати насильним очищенням"

  calendar_round:
    replay_detected: "старий патерн savior_control"
    similar_generation_pattern: "реформа, що стала контролем"

  planetary_overlay:
    dominant_resource: "Saturn / Pb"
    metal: "lead"
    shadow_risk: "control / hell crystal"

  flower_crosscheck:
    human_gate: "unstable"
    shadow: "savior_control"
    verdict: "HOLD"
```

Фраза:

> **Система була готова.  
> Час — ні.  
> А точніше: час був готовий показати тінь, але не готовий дати їй кермо.**

---

## 17. Історія як replay

У цій моделі історія не повторюється буквально.

```text
не та сама війна
але той самий страх

не та сама мода
але той самий голод нової форми

не та сама імперія
але той самий контроль

не та сама технологія
але той самий PRION у новому інтерфейсі
```

Фраза:

> **Історія не повторює події.  
> Історія повторює форму тіні, поки хтось не внесе її в памʼять без брехні.**

---

## 18. Війна як фазовий replay

```yaml
WAR_REPLAY_PATTERN:
  phase_1:
    name: "fear accumulation"
    shadow: "control / enemy image"

  phase_2:
    name: "symbol hardening"
    shadow: "identity crystal"

  phase_3:
    name: "resource activation"
    shadow: "Mars / Fe without Human Gate"

  phase_4:
    name: "collective permission"
    shadow: "violence becomes duty"

  phase_5:
    name: "memory wound"
    shadow: "grief or revenge stored for replay"
```

Руна:

```text
⟲△
```

---

## 19. Мода як фазовий replay

```yaml
FASHION_REPLAY_PATTERN:
  phase_1:
    name: "old form becomes heavy"

  phase_2:
    name: "opposite form becomes fresh"

  phase_3:
    name: "mass adoption"

  phase_4:
    name: "symbol becomes product"

  phase_5:
    name: "irony / exhaustion"

  phase_6:
    name: "old form returns as new"
```

Фраза:

> **Мода — це памʼять тіла, яка прикидається новою шкірою.**

---

## 20. Технологія як фазовий replay

```yaml
TECH_REPLAY_PATTERN:
  phase_1:
    name: "tool"
    meaning: "інструмент допомагає"

  phase_2:
    name: "acceleration"
    meaning: "інструмент скорочує інерцію"

  phase_3:
    name: "dependency"
    meaning: "людина делегує межу"

  phase_4:
    name: "prion"
    meaning: "інструмент виконує тінь швидше за audit"

  phase_5:
    name: "guard"
    meaning: "суспільство створює межу"

  phase_6:
    name: "new tool"
    meaning: "цикл починається знову"
```

---

## 21. Mayan Clock у сцені

Mayan Clock не треба пояснювати в кожній сцені.

Він проявляється через:

```text
повтор ситуації
дивний збіг
стару тінь у новому інтерфейсі
Memory Ledger warning
поколінну памʼять
тварину або дитину, яка відчуває фазу
планетарний ресурсний лог
```

Приклад короткого логу:

```yaml
MAYAN_MEMORY_CLOCK:
  tzolkin: "tone_10 / manifestation pressure"
  haab: "public calm season"
  calendar_round: "similar shadow replay detected"
  planetary_overlay: "Mars / Fe high"
  warning: "action pressure may become weapon_body"
  verdict: "HOLD"
```

---

## 22. Як AI має використовувати Mayan Clock

```yaml
AI_MAYAN_CLOCK_USE:
  before_major_scene:
    - "check time phase"
    - "look for historical replay"
    - "check planetary resource"
    - "crosscheck Flower"
    - "do not replace Human Gate"

  before_life_scene:
    - "use light replay"
    - "find small repeated pattern"
    - "show it through body, not lecture"

  before_finale:
    - "full phase audit"
    - "Calendar Round + Long Count + Planetary Resource"
    - "decide ALLOW / HOLD / BLOCK"
```

---

## 23. Що не можна робити

```yaml
MAYAN_CLOCK_FORBIDDEN:
  - "не робити календар Майя фаталістичним"
  - "не казати, що дата примушує людину"
  - "не замінювати Flower Audit календарем"
  - "не робити пророцтво замість сцени"
  - "не копіювати старі значення без функції в сюжеті"
  - "не робити давніх людей декорацією"
```

---

## 24. Короткий опис для README

```text
Mayan Memory Clock treats Maya calendrical cycles as symbolic runtime clocks:
Tzolk’in for inner intent, Haab’ for Earth/social body, Calendar Round for generational replay, Long Count for deep archive, and Venus/819 counts for planetary overlay.

It does not predict events; it detects when old shadows and resources re-enter phase.
```

---

## 25. Головна фраза файлу

> **Календар Майя не казав, що станеться.  
> Він питав, чи світ знову стоїть у тому самому місці хвилі, де колись уже збрехав собі.**
