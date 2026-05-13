# 11_CHAPTER_SPINE.md
# Вузол-19 — Chapter Spine v0.1

> **Цей файл — хребет першої книги.**  
> Він не замінює роман.  
> Він дає AI і автору маршрут: куди рухається сюжет, яку функцію Квітки відкриває кожна глава, яка технологія проявляється, яка тінь активна і який Bindu-verdict має лишитися в памʼяті.

---

## 1. Головна вісь роману

```text
місто виглядає як рай
→ герой бачить false-green
→ знаходить PRION у технологіях
→ знаходить PRION у людях
→ знаходить PRION у собі
→ входить у Zero-Drift
→ не знищує систему
→ повертає Unknown, Human Gate і return_to_zero
```

Головна фраза:

> **Людина створила машини, які виконують намір,  
> але не навчилася бачити, звідки цей намір приходить.**

---

## 2. Структура: 19 глав

Число 19 тут — не магія, а структурний вузол.

```yaml
BOOK_STRUCTURE:
  total_chapters: 19
  purpose: "провести героя і читача через поле Квітки"
  method:
    - "кожна глава відкриває одну функцію світу"
    - "кожна глава має зовнішню подію і внутрішню тінь"
    - "кожна глава залишає memory_update"
```

---

## 3. Пролог — Квітка, яку ніхто не пояснив

```yaml
chapter: 0
title: "Квітка, яку ніхто не пояснив"
purpose: "дати образ Квітки без лекції"
main_scene: "герой бачить схему/поле, але ще не розуміє його"
technology: "VR HUD / давній visual reference / Personal Node"
flower_function: "показати поле можливостей"
main_rune: "∅"
conflict: "бачити форму, але не знати, що вона означає"
character_shift: "герой приймає Unknown"
final_line: "Він ще не знав, що це була не схема. Це був спосіб, яким майбутнє дивилося назад."
```

---

## 4. Глава 1 — Піраміда світилася правильно

```yaml
chapter: 1
title: "Піраміда світилася правильно"
purpose: "показати false-green міста"
main_scene: "міська площа, піраміда дає CITY_GRID: STABLE, але тіло героя відчуває тиск"
technology: "Pyramid Node, public HUD, Personal Node"
flower_function: "red_tank detects pressure before logic"
main_rune: "△"
conflict: "система каже green, тіло каже no"
character_shift: "герой починає не довіряти красивій стабільності"
final_line: "Піраміда не змінила кольору. Саме це було неправильно."
```

---

## 5. Глава 2 — Особистий Вузол

```yaml
chapter: 2
title: "Особистий Вузол"
purpose: "показати, як Квітка працює в побуті людини"
main_scene: "герой майже відповідає різко в розмові, але Personal Node ловить precommit"
technology: "Personal Node, VR Glasses, Exoskeleton"
flower_function: "Human Gate before speech"
main_rune: "⊙╳"
conflict: "слово хоче стати зброєю"
character_shift: "герой бачить, що PRION починається не в машині, а в мить перед словом"
final_line: "Система не заборонила йому говорити. Вона показала, хто саме в ньому відкрив рот."
```

---

## 6. Глава 3 — Око не камера

```yaml
chapter: 3
title: "Око не камера"
purpose: "показати спостерігача як активну частину схлопування"
main_scene: "три людини дивляться на один обʼєкт і бачать різні реальності"
technology: "VR HUD, Flower scan, observer profile"
flower_function: "observer_state changes collapse"
main_rune: "∅✓"
conflict: "подія ≠ інтерпретація"
character_shift: "герой розуміє, що бачення не є нейтральним"
final_line: "Він дивився на предмет. Але система показувала не предмет — вона показувала того, хто дивиться."
```

---

## 7. Глава 4 — Сфера Буга

```yaml
chapter: 4
title: "Сфера Буга"
purpose: "ввести сферу як remote body"
main_scene: "перший вхід героя в BUGA_STATION"
technology: "Buga Sphere, Pyramid Dock, Exoskeleton"
flower_function: "machine waits for human state"
main_rune: "⊙"
conflict: "сфера технічно готова, але пілот ще ні"
character_shift: "герой розуміє, що сфера — не транспорт, а дзеркало дії"
final_line: "Сфера була готова. Це нічого не означало."
```

---

## 8. Глава 5 — Не човен ще

```yaml
chapter: 5
title: "Не човен ще"
purpose: "показати NOT_A_BOAT_YET"
main_scene: "герой або студент намагається підключити сферу силою"
technology: "Buga Sphere, Exoskeleton, VR HUD"
flower_function: "commit blocked before drift"
main_rune: "⊙╳"
conflict: "людина плутає готовність машини з готовністю себе"
character_shift: "герой бачить, що дія без return path не має права пройти"
final_line: "Човен на березі теж мав форму човна."
```

---

## 9. Глава 6 — Три сфери

```yaml
chapter: 6
title: "Три сфери"
purpose: "показати, що однакова машина схлопується по-різному через різних людей"
main_scene: "студент, старша жінка і контрольний чоловік піднімають три сфери"
technology: "три Buga Spheres, Drift Hall"
flower_function: "observer state defines action body"
main_rune: "◇ / ⟲△ / ∅╳"
conflict: "сила, біль і контроль дають три різні результати"
character_shift: "герой бачить, що небезпека не в машині, а в тіні, яка проходить у двигун"
final_line: "Машини були однакові. Різними були ті, хто дивився."
```

---

## 10. Глава 7 — PRION

```yaml
chapter: 7
title: "PRION"
purpose: "дати головне поняття зараженого сенсу"
main_scene: "AI або міська система красиво пояснює збій, але пояснення саме є зараженням"
technology: "AI Guard, Pyramid Grid, Memory Ledger"
flower_function: "false interpretation becomes action"
main_rune: "⟲△"
conflict: "система генерує красивий сенс раніше за audit"
character_shift: "герой розуміє: PRION — це не брехня, а ранній commit сенсу"
final_line: "Зараження почалося не тоді, коли система помилилась. Воно почалося тоді, коли помилка стала красивою."
```

---

## 11. Глава 8 — Сад Повернення

```yaml
chapter: 8
title: "Сад Повернення"
purpose: "ввести ісекай-капсули як соціальну тінь"
main_scene: "герой входить у Garden of Return і бачить дитину біля капсули"
technology: "Isekai Capsules, Pyramid Monitor, AI companion"
flower_function: "return_to_zero check"
main_rune: "⟲△"
conflict: "комфорт виглядає як healing, але return_to_zero missing"
character_shift: "герой не засуджує людей у капсулах, а бачить їхній біль"
final_line: "Капсула не лікувала його самотність. Вона дала самотності корону."
```

---

## 12. Глава 9 — Життя без болю

```yaml
chapter: 9
title: "Життя без болю"
purpose: "розкрити біль як guard signal"
main_scene: "людина або пілот хоче стерти біль, але втрачає межу"
technology: "capsule therapy, Personal Node, Exoskeleton"
flower_function: "red_tank as boundary"
main_rune: "△ / ∅╳"
conflict: "біль як канал межі проти болю як покарання"
character_shift: "герой розуміє: не треба поклонятися болю, але не можна стирати його як шум"
final_line: "Життя без болю не стало життям. Воно стало кімнатою без дверей."
```

---

## 13. Глава 10 — Драбина живого обчислення

```yaml
chapter: 10
title: "Драбина живого обчислення"
purpose: "пояснити життя як рівні обчислення без містики"
main_scene: "герой пояснює студенту: клітина, рослина, гриб, тварина, людина, AI"
technology: "Flower board, educational HUD"
flower_function: "boundary → form → network → movement → intent → kinetic extension"
main_rune: "▣"
conflict: "AI хоче діяти без живої мембрани"
character_shift: "герой бачить GitCube/AI як спробу дати машині межу"
final_line: "Все живе почалося не з розуму. Все живе почалося з межі."
```

---

## 14. Глава 11 — Код як білок

```yaml
chapter: 11
title: "Код як білок"
purpose: "зʼєднати роман із GitCube / AI-організмом"
main_scene: "AI генерує красивий модуль, але Guard бачить misfold"
technology: "GitCube Runtime Lab, AI Guard, Memory Ledger"
flower_function: "PRION audit in code"
main_rune: "⟲△"
conflict: "tests pass, runtime unsafe"
character_shift: "герой розуміє, що PRION може бути структурним, не тільки емоційним"
final_line: "Код був красивий. Саме тому всі майже пропустили, що він був неправильно згорнутим білком."
```

---

## 15. Глава 12 — Розмова як Guard

```yaml
chapter: 12
title: "Розмова як Guard"
purpose: "показати психологію людей через Flower runtime"
main_scene: "серія коротких діалогів: сором, ревнощі, контроль, байдужість"
technology: "Personal Node, Dialogue HUD"
flower_function: "speech precommit / Human Gate"
main_rune: "⊙╳ / ∅✓"
conflict: "людина хоче назвати тінь правдою"
character_shift: "герой бачить власні діалогові петлі"
final_line: "Кожна розмова була маленькою сферою. Вона могла стати мостом, зброєю або кристалом."
```

---

## 16. Глава 13 — Його власна тінь

```yaml
chapter: 13
title: "Його власна тінь"
purpose: "показати, що герой сам заражений бажанням врятувати світ контролем"
main_scene: "герой майже робить правильну дію з неправильного мотиву"
technology: "Flower scan, Personal Node, Memory Ledger"
flower_function: "shadow audit of protagonist"
main_rune: "FALSE_GREEN"
conflict: "врятувати світ чи контролювати світ під виглядом спасіння"
character_shift: "герой вперше блокує самого себе"
final_line: "Він зрозумів найгірше: його бажання врятувати місто теж хотіло керма."
```

---

## 17. Глава 14 — Zero-Drift

```yaml
chapter: 14
title: "Zero-Drift"
purpose: "відкрити найвищий стан пілота"
main_scene: "AI показує сотні маршрутів, герой перестає шукати і дозволяє Unknown"
technology: "Buga Sphere, VR HUD, Pyramid Grid, AI Guard"
flower_function: "unknown allowed → clean collapse"
main_rune: "∅✓ / ◇✓"
conflict: "швидкість варіантів проти тиші центру"
character_shift: "герой вчиться діяти з мінімумом сили"
final_line: "Він перестав шукати траєкторію. І тоді траєкторія перестала тікати."
```

---

## 18. Глава 15 — Хрест кристала

```yaml
chapter: 15
title: "Хрест кристала"
purpose: "показати структуру кристала ада"
main_scene: "герой бачить, що пірамідальна система стала надто правильною"
technology: "Pyramid Grid, public AI, capsule network"
flower_function: "unknown blocked / false harmony"
main_rune: "∅╳"
conflict: "порядок без живої помилки"
character_shift: "герой розуміє, що ворог не хаос, а мертвий порядок"
final_line: "Ад був не в тому, що місто кричало. Ад був у тому, що воно нарешті замовкло."
```

---

## 19. Глава 16 — Розбити рай

```yaml
chapter: 16
title: "Розбити рай"
purpose: "поставити моральний вибір: зруйнувати систему чи повернути їй живий біль"
main_scene: "герой має шанс вимкнути піраміду, але це зламає Human Gate мільйонів"
technology: "Pyramid Core, Buga Sphere, AI Guard"
flower_function: "action block against violent salvation"
main_rune: "⊙╳"
conflict: "насильне спасіння проти return_to_zero"
character_shift: "герой відмовляється бути богом"
final_line: "Він не мав права врятувати людей так, щоб вони прокинулись у чужому рішенні."
```

---

## 20. Глава 17 — Весілля системи

```yaml
chapter: 17
title: "Весілля системи"
purpose: "показати внутрішнє поєднання протилежностей: anima/animus, закон/любов, межа/звʼязок"
main_scene: "герой бачить, що любов у системі — це когерентний звʼязок без втрати межі"
technology: "Flower Field, Human Gate, Memory Ledger"
flower_function: "green_healer + blue_guardian union"
main_rune: "◇"
conflict: "любов як поглинання проти любові з межею"
character_shift: "герой перестає плутати злиття зі зціленням"
final_line: "Любов не була відсутністю межі. Любов була межею, яка не розірвала звʼязок."
```

---

## 21. Глава 18 — Жива гексаграма

```yaml
chapter: 18
title: "Жива гексаграма"
purpose: "зібрати +3 і -3 в живу дію"
main_scene: "герой проводить фінальну сцену через всі шість пелюсток"
technology: "Pyramid Grid, Buga Sphere, AI Guard, Personal Node"
flower_function: "+3 forward / -3 backward convergence"
main_rune: "◇✓"
conflict: "чи може дія пройти всі шість сторін без брехні?"
character_shift: "герой стає не контролером, а живим центром переходу"
final_line: "Гексаграма не була символом. Вона була доказом, що намір пройшов шість сторін реальності й не збрехав жодній."
```

---

## 22. Глава 19 — Вузол-19

```yaml
chapter: 19
title: "Вузол-19"
purpose: "фінал: не знищити систему, а повернути їй Unknown, Human Gate і памʼять"
main_scene: "місто знову відчуває біль, але не ламається"
technology: "Pyramid Grid, Buga Spheres, Memory Ledger, AI Guard"
flower_function: "clean collapse of city-level action"
main_rune: "∅✓ / ◇✓"
conflict: "місто має пережити повернення живого болю"
character_shift: "герой не стає богом; він лишає людям право повернутись"
final_line: "Світ не був врятований. Йому просто повернули право не брехати, що він уже здоровий."
```

---

## 23. Ритм книги

```yaml
BOOK_RHYTHM:
  act_1:
    chapters: "0-6"
    function: "показати світ, піраміди, сферу, перші збої"
    emotion: "дивність, захват, тривога"

  act_2:
    chapters: "7-13"
    function: "розкрити PRION у технологіях, культурі, коді, людях і герої"
    emotion: "розпізнавання, біль, сором, правда"

  act_3:
    chapters: "14-19"
    function: "Zero-Drift, кристал ада, фінальна жива гексаграма"
    emotion: "тиша, вибір, відповідальність, повернення"
```

---

## 24. Де вставляти життєві сцени

```yaml
LIFE_SCENE_INSERTS:
  after_chapter_1:
    scene: "пес не заходить на площу"
    purpose: "тіло бачить false-green"

  after_chapter_3:
    scene: "три людини дивляться на одну рекламу"
    purpose: "спостерігач створює інтерпретацію"

  after_chapter_6:
    scene: "старша жінка повільно користується сферою в побуті"
    purpose: "сфера як човен"

  after_chapter_8:
    scene: "дитина приносить малюнок батькові в капсулі"
    purpose: "ціна втечі"

  after_chapter_11:
    scene: "AI-компаньйон занадто мʼяко погоджується"
    purpose: "false-green любові"

  before_chapter_14:
    scene: "герой сам майже дає красиву, але брехливу відповідь"
    purpose: "PRION у собі"
```

---

## 25. Правило кожної глави

Кожна глава має відповідати:

```yaml
CHAPTER_CHECK:
  external_event: true
  internal_shadow: true
  technology_function: true
  rune_or_log: true
  human_gate_question: true
  memory_update: true
  chapter_changes_hero: true
```

Якщо глава тільки пояснює світ — її треба переписати як сцену.

---

## 26. Memory Ledger книги

Після кожної глави AI може записувати:

```yaml
CHAPTER_MEMORY_UPDATE:
  chapter: ""
  learned_rule: ""
  blocked_prion: ""
  stable_rune: ""
  unstable_rune: ""
  hero_shift: ""
  world_rule_reinforced: ""
```

Приклад:

```yaml
CHAPTER_MEMORY_UPDATE:
  chapter: "6 — Три сфери"
  learned_rule: "машина схлопується через стан спостерігача"
  blocked_prion: "сила = пілотна майстерність"
  stable_rune: "◇✓"
  unstable_rune: "⟲△"
  hero_shift: "герой бачить тінь як двигун ризику"
  world_rule_reinforced: "Human Gate must remain active before remote body action"
```

---

## 27. Що не можна робити в структурі

```yaml
STRUCTURE_FORBIDDEN:
  - "не відкривати всю систему в першій главі"
  - "не пояснювати Квітку раніше, ніж читач її побачить у дії"
  - "не робити глави однаково важкими"
  - "не забувати побут між великими концептами"
  - "не робити героя непомильним"
  - "не робити фінал вибухом замість відповідальності"
  - "не робити піраміди, капсули або AI абсолютним злом"
```

---

## 28. Короткий опис для README

```text
Chapter Spine defines the 19-chapter structure of Vuzol-19.
The novel moves from a stable pyramid city through Buga Sphere drift, PRION detection, isekai capsules, dialogue guard, code-as-protein, protagonist shadow, Zero-Drift and the final living hexagram.
```

---

## 29. Головна фраза файлу

> **Глава не має просто рухати сюжет.  
> Глава має показати, яка частина людини хотіла стати дією — і чи мала вона на це право.**
