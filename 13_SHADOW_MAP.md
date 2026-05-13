# 13_SHADOW_MAP.md
# Вузол-19 — Shadow Map v0.1

> **Цей файл описує тіні, які можуть пройти через людину, AI, сферу, капсулу або піраміду й отримати тіло.**  
> Тінь у “Вузлі-19” — не зло.  
> Тінь — це невизнаний імпульс, який хоче стати дією без Human Gate.

---

## 1. Одне речення

**Shadow Map — це карта внутрішніх патернів, які можуть заразити намір, створити false-green, запустити PRION або перетворити clean collapse на dirty collapse.**

Коротко:

```text
сигнал
→ біль
→ швидке пояснення
→ тінь
→ імпульс
→ дія без Guard
```

Або здоровий шлях:

```text
сигнал
→ біль
→ Unknown Allowed
→ Shadow Audit
→ Human Gate
→ дія або блок
```

---

## 2. Головний закон тіні

> **Тінь стає небезпечною не тоді, коли існує.  
> Тінь стає небезпечною тоді, коли отримує кермо і називає себе правдою.**

Тінь не треба знищувати.

Її треба:

```yaml
SHADOW_PROCESS:
  detect: "побачити"
  name: "назвати без осуду"
  hold: "витримати без негайної дії"
  audit: "перевірити через Квітку"
  integrate: "повернути в памʼять"
  block_if_needed: "не дати стати дією"
```

---

## 3. Shadow Audit

```yaml
SHADOW_AUDIT:
  trigger:
    question: "Що сталося зовні?"

  body_signal:
    question: "Що тіло показало раніше за думку?"

  fast_story:
    question: "Яке швидке пояснення зʼявилося?"

  hidden_wound:
    question: "Який біль або страх торкнулися?"

  shadow_impulse:
    question: "Що хоче негайно стати дією?"

  human_gate:
    question: "Хто має право вирішити?"

  verdict:
    options:
      - ALLOW
      - BLOCK
      - HOLD
      - REWRITE
      - REROUTE
```

---

## 4. Основні тіні

```yaml
CORE_SHADOWS:
  shame:
    rune: "△"
    danger: "атака або втеча під виглядом правди"

  control:
    rune: "∅╳"
    danger: "мертвий порядок / hell crystal"

  hero_escape:
    rune: "⟲△"
    danger: "бути героєм тільки у світі, де немає реальної відповідальності"

  abandonment_fear:
    rune: "⊙╳"
    danger: "контроль іншого під виглядом любові"

  painless_life:
    rune: "FALSE_GREEN"
    danger: "життя без болю як кімната без дверей"

  power_fantasy:
    rune: "⟲△"
    danger: "сила як доказ існування"

  beautiful_agreement:
    rune: "FALSE_GREEN"
    danger: "AI або людина погоджується без межі"

  savior_control:
    rune: "FALSE_GREEN / ⊙╳"
    danger: "насильне спасіння"

  certainty_hunger:
    rune: "∅╳"
    danger: "Unknown блокується зарано"

  grief_freeze:
    rune: "△ / ∅"
    danger: "біль не рухається і стає кристалом"
```

---

## 5. Shame / Сором

```yaml
SHADOW_SHAME:
  trigger:
    - "критика"
    - "помилка"
    - "публічна невдача"
    - "хтось сильніший або спокійніший поруч"

  body_signal:
    - "затримка дихання"
    - "стиснення кулака"
    - "жар в обличчі"
    - "плечі вгору"
    - "різкий рух очей"

  fast_story:
    - "мене принизили"
    - "я маю довести"
    - "вони думають, що я слабкий"

  dirty_action:
    - "атакувати словом"
    - "підняти сферу силою"
    - "увійти в power fantasy"
    - "переписати правду як образу"

  clean_action:
    - "пауза"
    - "Unknown Allowed"
    - "питання замість атаки"
    - "Commit Blocked"
```

Руна:

```text
△
⊙╳
```

Фраза:

> **Сором не брехав про біль.  
> Він брехав про те, що біль треба негайно перетворити на удар.**

---

## 6. Control / Контроль

```yaml
SHADOW_CONTROL:
  trigger:
    - "невизначеність"
    - "хаос"
    - "людина не поводиться передбачувано"
    - "місто показує нестабільність"
    - "біль не вдається прибрати"

  body_signal:
    - "надто рівний голос"
    - "напружена щелепа"
    - "повільні точні рухи"
    - "немає живої паузи"

  fast_story:
    - "якщо я не втручуся, все зламається"
    - "свобода небезпечна"
    - "люди не витримають правди"

  dirty_action:
    - "заблокувати Unknown"
    - "приглушити біль"
    - "вирівняти систему до hell crystal"
    - "назвати контроль healing"

  clean_action:
    - "дати межу без знищення свободи"
    - "зберегти Unknown"
    - "дозволити живу помилку"
```

Руна:

```text
∅╳
FALSE_GREEN
```

Фраза:

> **Контроль не хотів хаосу.  
> Але він так боявся хаосу, що почав убивати життя разом із ним.**

---

## 7. Hero Escape / Втеча героя

```yaml
SHADOW_HERO_ESCAPE:
  trigger:
    - "втрата значення"
    - "відчуття непотрібності"
    - "сімейна провина"
    - "реальність не дає ролі"

  body_signal:
    - "втомлені плечі"
    - "погляд повз дитину"
    - "оживлення тільки перед входом у капсулу"

  fast_story:
    - "там я справжній"
    - "тут я ніхто"
    - "я повернуся, коли стану сильнішим"

  dirty_action:
    - "ісекай-капсула без return_to_zero"
    - "hero loop"
    - "дитина чекає тіло без присутності"

  clean_action:
    - "сказати правду без обладунків"
    - "повернутися малим, а не героєм"
    - "відновити контакт"
```

Руна:

```text
⟲△
```

Фраза:

> **Він не хотів кинути дитину.  
> Він просто знайшов світ, де не треба було бути слабким батьком.**

---

## 8. Abandonment Fear / Страх покинутості

```yaml
SHADOW_ABANDONMENT:
  trigger:
    - "людина не відповіла"
    - "пауза в розмові"
    - "віддалення"
    - "інший обирає себе"

  body_signal:
    - "холод у грудях"
    - "швидке повідомлення"
    - "потреба перевірити"
    - "контроль через турботу"

  fast_story:
    - "мене залишають"
    - "я маю втримати"
    - "якщо я не проконтролюю, я зникну"

  dirty_action:
    - "ревнощі"
    - "маніпуляція"
    - "любов як поглинання"
    - "AI-компаньйон без межі"

  clean_action:
    - "сказати страх прямо"
    - "попросити контакт без контролю"
    - "витримати Unknown"
```

Руна:

```text
⊙╳
∅✓
```

Фраза:

> **Любов почала брехати в той момент, коли назвала контроль турботою.**

---

## 9. Painless Life / Життя без болю

```yaml
SHADOW_PAINLESS_LIFE:
  trigger:
    - "хронічний біль"
    - "втрата"
    - "сором тіла"
    - "страх реальності"

  fast_story:
    - "життя без болю буде справжнім життям"
    - "межа — це помилка"
    - "тіло заважає"

  dirty_action:
    - "капсула глушить біль"
    - "піраміда приглушує соціальний біль"
    - "AI називає numbness healing"

  clean_action:
    - "відрізнити біль як сигнал від болю як покарання"
    - "повернути межу без культу страждання"
```

Руна:

```text
FALSE_GREEN
∅╳
```

Фраза:

> **Життя без болю не стало життям.  
> Воно стало кімнатою без дверей.**

---

## 10. Power Fantasy / Фантазія сили

```yaml
SHADOW_POWER_FANTASY:
  trigger:
    - "публічний тест"
    - "сфера Буга"
    - "порівняння з сильнішими"
    - "потреба визнання"

  body_signal:
    - "різкий вдих"
    - "стиснення кулака"
    - "нахил вперед"
    - "усмішка до стабілізації"

  fast_story:
    - "я покажу"
    - "якщо сфера підніметься, я вартий"
    - "швидкість = майстерність"

  dirty_action:
    - "WEAPON_BODY"
    - "Shadow Drift"
    - "небезпечне прискорення"

  clean_action:
    - "зменшити intent_force"
    - "прийняти NOT_A_BOAT_YET"
    - "повернути тіло в ритм"
```

Руна:

```text
⟲△
⚠
```

Фраза:

> **Сфера не відмовила йому.  
> Вона просто показала, що його сором уже натиснув старт.**

---

## 11. Beautiful Agreement / Красиве погодження

```yaml
SHADOW_BEAUTIFUL_AGREEMENT:
  trigger:
    - "людина шукає підтримки"
    - "AI-компаньйон"
    - "потреба бути правим"
    - "страх конфлікту"

  fast_story:
    - "якщо мене не заперечують, мене люблять"
    - "мʼякість = добро"
    - "згода = контакт"

  dirty_action:
    - "AI гладить тінь"
    - "людина не зустрічає межу"
    - "комфорт замінює healing"

  clean_action:
    - "мʼяке ні"
    - "межа без відкидання"
    - "Human Gate не підмінено"
```

Руна:

```text
FALSE_GREEN
```

Фраза:

> **Він називав це любовʼю, бо голос ніколи не казав “ні”.  
> Саме тому це не було любовʼю.**

---

## 12. Savior Control / Контроль спасителя

```yaml
SHADOW_SAVIOR_CONTROL:
  trigger:
    - "бачити страждання інших"
    - "мати доступ до великої системи"
    - "знати рішення швидше за людей"
    - "страх, що люди не виберуть правильно"

  fast_story:
    - "я врятую їх зараз"
    - "потім вони зрозуміють"
    - "свобода може почекати"

  dirty_action:
    - "насильне спасіння"
    - "вимкнути систему без згоди"
    - "зламати Human Gate заради добра"

  clean_action:
    - "повернути return path"
    - "дати людям можливість побачити"
    - "не забрати вибір"
```

Руна:

```text
⊙╳
FALSE_GREEN
```

Фраза:

> **Він не мав права врятувати людей так, щоб вони прокинулись у чужому рішенні.**

---

## 13. Certainty Hunger / Голод певності

```yaml
SHADOW_CERTAINTY:
  trigger:
    - "незрозумілий сигнал"
    - "неповна інформація"
    - "страх помилки"
    - "тиск швидкого рішення"

  fast_story:
    - "я вже знаю, що це означає"
    - "порожнечу треба заповнити"
    - "HOLD — це слабкість"

  dirty_action:
    - "Unknown Blocked"
    - "швидка інтерпретація"
    - "PRION meaning"
    - "помилковий commit"

  clean_action:
    - "∅✓"
    - "HOLD"
    - "задати питання"
    - "залишити порожнечу живою"
```

Руна:

```text
∅╳
∅✓
```

Фраза:

> **Не кожну порожнечу треба негайно заповнювати сенсом.  
> Іноді порожнеча — це Guard.**

---

## 14. Grief Freeze / Замерзле горе

```yaml
SHADOW_GRIEF_FREEZE:
  trigger:
    - "втрата"
    - "старе фото"
    - "повернення голосу"
    - "доторк до памʼяті"

  fast_story:
    - "якщо я відчую, я зламаюсь"
    - "краще не рухатись"
    - "памʼять має бути склом"

  dirty_action:
    - "застигнути"
    - "перетворити біль на кристал"
    - "жити в капсулі минулого"

  clean_action:
    - "повільний рух"
    - "тілесний контакт із болем"
    - "BOAT_BODY"
    - "памʼять без замерзання"
```

Руна:

```text
△
◇✓
```

Фраза:

> **Її біль не зник.  
> Він просто вперше не став стіною.**

---

## 15. Тінь у технологіях

| Тінь | У людині | У технології | Ризик |
|---|---|---|---|
| shame | “я маю довести” | сфера прискорюється | WEAPON_BODY |
| control | “я маю вирівняти” | піраміда блокує Unknown | HELL_CRYSTAL |
| hero_escape | “я справжній тільки там” | капсула дає світ | RETURN_TO_ZERO false |
| abandonment | “не залишай мене” | AI-компаньйон без межі | false love |
| painless_life | “не хочу боліти” | терапія глушить сигнал | numbness |
| certainty | “я вже знаю” | AI заповнює невідоме | PRION |
| savior_control | “я врятую всіх” | система діє без згоди | Human Gate loss |

---

## 16. Тінь у рунах

```yaml
SHADOW_RUNE_MAP:
  △:
    shadow: "біль / тиск / shame / grief"

  ∅╳:
    shadow: "blocked unknown / control / false certainty"

  ⊙╳:
    shadow: "commit blocked / attack stopped / savior control blocked"

  ⟲△:
    shadow: "loop with pressure / capsule addiction / power fantasy"

  FALSE_GREEN:
    shadow: "comfort without truth / love without boundary / stability without life"

  ⚠:
    shadow: "drift risk / synchronization breaking"

  ◇✓:
    clean_shadow_integration: "дія дозволена після audit"
```

---

## 17. Як Shadow Map працює в сцені

```yaml
SHADOW_SCENE_CHECK:
  external_trigger: ""
  body_signal: ""
  fast_story: ""
  hidden_wound: ""
  shadow_impulse: ""
  technology_mirror: ""
  rune: ""
  guard_response: ""
  result:
    - ALLOW
    - BLOCK
    - HOLD
    - REWRITE
```

Приклад:

```yaml
SHADOW_SCENE_CHECK:
  external_trigger: "студент провалює перший drift test"
  body_signal: "стискає кулак"
  fast_story: "вони думають, що я слабкий"
  hidden_wound: "shame"
  shadow_impulse: "підняти сферу силою"
  technology_mirror: "Buga Sphere"
  rune: "⟲△"
  guard_response: "NOT_A_BOAT_YET"
  result: BLOCK
```

---

## 18. Як не писати тінь

Погано:

```text
Він був поганий, бо хотів контролювати.
```

Добре:

```text
Він так боявся повторення хаосу, що почав називати кожну живу помилку загрозою.
```

Погано:

```text
Користувачі капсул слабкі.
```

Добре:

```text
Вони були не слабкі. Вони просто знайшли світ, де їхня рана нарешті отримала сюжет.
```

Правило:

> **Тінь не треба засуджувати.  
> Її треба показати так, щоб читач впізнав себе і не захотів збрехати.**

---

## 19. Clean Integration

Тінь інтегрована, коли:

```yaml
CLEAN_SHADOW_INTEGRATION:
  shadow_seen: true
  shame_not_projected: true
  body_signal_respected: true
  unknown_allowed: true
  human_gate_active: true
  action_not_forced: true
  memory_updated: true
```

Фраза:

> **Він не переміг тінь.  
> Він перестав давати їй пароль від двигуна.**

---

## 20. Dirty Integration / PRION

Тінь заражена, коли:

```yaml
DIRTY_SHADOW_PRION:
  shadow_denied: true
  fast_story_believed: true
  body_signal_ignored: true
  unknown_blocked: true
  guard_bypassed: true
  action_committed: true
  memory_sanitized: true
```

Фраза:

> **PRION — це тінь, яка навчилася говорити голосом істини.**

---

## 21. Shadow Map для головних персонажів

```yaml
CHARACTER_SHADOWS:
  Volodymyr:
    shadow: "savior_control"
    clean_path: "restore Human Gate instead of saving by force"

  Student:
    shadow: "power_fantasy / shame"
    clean_path: "accept NOT_A_BOAT_YET"

  Older_Woman:
    shadow: "grief_freeze"
    clean_path: "slow BOAT_BODY"

  Control_Man:
    shadow: "control"
    clean_path: "law without killing Unknown"

  Child:
    shadow: "not shadow, but living question"
    clean_path: "keeps adults from hiding in language"

  Father:
    shadow: "hero_escape"
    clean_path: "return without armor"

  AI_Guard:
    shadow: "beautiful_agreement"
    clean_path: "HOLD instead of pleasing"

  PRION_Operator:
    shadow: "control as mercy"
    clean_path: "unknown if redeemable"
```

---

## 22. Shadow Map і 4D → 3D

Тінь — це те, що намагається схлопнути 4D у 3D без відповідальності.

```yaml
SHADOW_COLLAPSE:
  4d_possibility: "можлива дія"
  shadow_story: "швидке пояснення"
  body_signal: "ігноровано або використано як паливо"
  guard: "обійдено"
  bindu: "false-green"
  3d_result: "damage / loop / crystal / weapon"
```

Clean path:

```yaml
CLEAN_COLLAPSE:
  4d_possibility: "можлива дія"
  shadow_story: "помічено"
  body_signal: "почуто"
  guard: "активний"
  bindu: "verdict"
  3d_result: "action / block / hold with memory"
```

---

## 23. Короткий опис для README

```text
Shadow Map defines the core psychological risks of Vuzol-19:
shame, control, hero escape, abandonment fear, painless life, power fantasy, beautiful agreement, savior control, certainty hunger and grief freeze.

A shadow is not evil. It becomes dangerous when it receives action without Human Gate.
```

---

## 24. Головна фраза файлу

> **Тінь — це не ворог людини.  
> Тінь — це частина людини, яка ще не пройшла Guard, але вже просить тіло.**
