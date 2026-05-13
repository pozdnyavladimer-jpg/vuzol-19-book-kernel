# 16_PLANETARY_RESOURCE_CLOCK.md
# Вузол-19 — Planetary Resource Clock v0.1

> **Цей файл описує планети як фазові лінзи ресурсів, метали як характери елементів, Сонце як carrier wave, а Землю як місце 3D-схлопування.**  
> Це не фізична модель “планети посилають метали на Землю променями”.  
> Це **міфоінженерна модель для роману**, де орбіти, календар Майя, Квітка і Human Gate разом показують, який ресурс зараз гуде сильніше і яка тінь може прокинутися.

---

## Bridge to Mayan Memory Clock

Planetary Resource Clock explains what resource is active.

Mayan Memory Clock explains when a resource enters a replay phase.

Planet = resource.
Orbit = rhythm.
Mayan Calendar = memory cycle.
Flower = audit.
Human Gate = permission.


## 1. Головна формула

```text
SUN = carrier wave / промінь-носій
PLANETS = phase lenses / фазові лінзи
METALS = resource characters / характери ресурсів
EARTH = body of collapse / тіло схлопування
MAYAN CLOCK = temporal phase audit / фазовий аудит часу
FLOWER = psychological-spatial audit / Квітка перевірки
HUMAN_GATE = permission / дозвіл
ACTION = 3D consequence / наслідок
```

Фраза:

> **Сонце давало енергію.  
> Планети давали характер.  
> Метали давали памʼять старих зірок.  
> Земля давала тіло.  
> Людина давала дозвіл.**

---

## 2. Фізична межа

У реальній фізиці планети не поповнюють Землю металами через сонячні промені.  
Метали на Землі походять із космічної історії матерії: зоряного нуклеосинтезу, наднових, зіткнень, формування Сонячної системи, астероїдної доставки тощо.

Для роману ми робимо інше:

```text
планети не переносять метал
планети активують фазу ресурсу
Сонце несе carrier
Земля резонує вже наявним металом
Квітка перевіряє намір
Human Gate дозволяє або блокує дію
```

---

## 3. Календар Майя як часовий audit

Календар Майя тут використовується як ритмічний Memory Clock:

```yaml
MAYAN_MEMORY_CLOCK:
  tzolkin_260:
    role: "короткий психічний цикл / tone-seal phase"

  haab_365:
    role: "сонячний соціальний цикл"

  calendar_round_18980:
    role: "52-річний replay / велике повернення патернів"

  wayeb_5:
    role: "purge / reset / небезпечний проміжок Unknown"

  long_count:
    role: "deep memory / цивілізаційна памʼять"
```

Фраза:

> **Майя рахували не кінець світу.  
> Вони рахували, коли світ знову забуде, що вже проходив цю тінь.**

---

## 4. Планети, метали, елементи

| Тіло | Метал | Елемент | Символ | № | Ресурс |
|---|---|---:|---|---:|---|
| Сонце | Золото | Gold | Au | 79 | центр, воля, ясність, Bindu |
| Місяць | Срібло | Silver | Ag | 47 | памʼять, вода, сон, тіло, відображення |
| Меркурій | Ртуть | Mercury | Hg | 80 | сигнал, мова, обмін, швидкість |
| Венера | Мідь | Copper | Cu | 29 | звʼязок, любов, резонанс, провідність |
| Марс | Залізо | Iron | Fe | 26 | кров, дія, тиск, удар, межа |
| Юпітер | Олово | Tin | Sn | 50 | ріст, закон, масштаб, порядок |
| Сатурн | Свинець | Lead | Pb | 82 | вага, час, межа, карма, структура |
| Уран | Уран | Uranium | U | 92 | розрив, електрика, мутація, інновація |
| Нептун | Нептуній | Neptunium | Np | 93 | сон, туман, глибина, ілюзія |
| Плутон | Плутоній | Plutonium | Pu | 94 | підземне ядро, смерть форми, переродження |
| Земля | Вуглець / Кремній / Залізо | C / Si / Fe | C/Si/Fe | 6/14/26 | життя, ґрунт, кристал, кров, 3D-наслідок |

---

## 5. Resource Star

Коли планети обертаються, вони не створюють буквальну зірку.  
Вони створюють **resource glyph** — малюнок фазового стану.

```text
orbit
+ phase
+ resonance
+ Mayan cycle
+ Flower audit
= resource star
```

Зображення симуляції:

```md
![Planetary Resource Star](planetary_resource_star.png)
```

Фраза:

> **Орбіти малюють не долю.  
> Вони малюють карту ресурсів, які зараз гудуть сильніше.**

---

## 6. Як читати Resource Star

```yaml
RESOURCE_STAR_READING:
  center:
    meaning: "Sun / Bindu / carrier"

  outer_points:
    meaning: "planetary resource lenses"

  loops:
    meaning: "repeating phase patterns"

  crossings:
    meaning: "conflict or resonance between resources"

  dense_knots:
    meaning: "memory replay / repeated shadow"

  open arcs:
    meaning: "possible clean transition"

  broken arcs:
    meaning: "resource without Human Gate"
```

---

## 7. Меркурій / Hg

```yaml
MERCURY_HG:
  resource:
    - "сигнал"
    - "мова"
    - "обмін"
    - "переклад"
    - "нервова швидкість"

  clean_use:
    - "чесна комунікація"
    - "точний протокол"
    - "швидкий, але перевірений обмін"

  shadow_use:
    - "маніпуляція"
    - "брехня швидше за audit"
    - "AI заповнює Unknown красивим текстом"

  rune_risk:
    - "∅╳"
    - "FALSE_GREEN"
```

Фраза:

> **Меркурій не давав істину.  
> Він давав швидкість сигналу.  
> А швидкість без Guard робила брехню блискавичною.**

---

## 8. Венера / Cu

```yaml
VENUS_CU:
  resource:
    - "звʼязок"
    - "любов"
    - "резонанс"
    - "краса"
    - "провідність"

  clean_use:
    - "контакт із межею"
    - "любов без поглинання"
    - "мʼяке ні"

  shadow_use:
    - "красива згода"
    - "AI-компаньйон без межі"
    - "контакт замінений комфортом"

  rune_risk:
    - "FALSE_GREEN"
```

Фраза:

> **Венера відкривала звʼязок.  
> Але звʼязок без межі ставав солодкою пасткою.**

---

## 9. Марс / Fe

```yaml
MARS_FE:
  resource:
    - "кров"
    - "дія"
    - "мʼяз"
    - "удар"
    - "захист"
    - "межа"

  clean_use:
    - "захист слабкого"
    - "дія після Guard"
    - "витримка тиску"

  shadow_use:
    - "агресія"
    - "power fantasy"
    - "WEAPON_BODY"

  rune_risk:
    - "△"
    - "⟲△"
```

Фраза:

> **Марс не створював війну.  
> Він піднімав ресурс дії.  
> Війною його робила тінь.**

---

## 10. Юпітер / Sn

```yaml
JUPITER_SN:
  resource:
    - "масштаб"
    - "закон"
    - "ріст"
    - "система"
    - "соціальний порядок"

  clean_use:
    - "справедливе розширення"
    - "закон з Human Gate"
    - "навчання"

  shadow_use:
    - "імперія"
    - "догма"
    - "масштаб без відповідальності"

  rune_risk:
    - "▣"
    - "FALSE_GREEN"
```

Фраза:

> **Юпітер давав масштаб.  
> Але масштаб без памʼяті швидко починав називати себе законом.**

---

## 11. Сатурн / Pb

```yaml
SATURN_PB:
  resource:
    - "час"
    - "вага"
    - "межа"
    - "структура"
    - "відповідальність"
    - "кармічна памʼять"

  clean_use:
    - "Guard"
    - "терпіння"
    - "структура, яка не вбиває життя"

  shadow_use:
    - "контроль"
    - "кристалізація"
    - "Hell Crystal"
    - "страх змін"

  rune_risk:
    - "∅╳"
```

Фраза:

> **Сатурн не карав.  
> Він просто додавав ваги всьому, що людина хотіла зробити без відповідальності.**

---

## 12. Сонце / Au

```yaml
SUN_AU:
  resource:
    - "центр"
    - "ясність"
    - "воля"
    - "carrier wave"
    - "Bindu"

  clean_use:
    - "свідомий намір"
    - "центрування"
    - "світло без осліплення"

  shadow_use:
    - "его-сонце"
    - "я є центр усіх"
    - "герой-бог"

  rune_risk:
    - "FALSE_GREEN"
```

Фраза:

> **Сонце було не владою.  
> Сонце було питанням: чи витримаєш ти центр, не назвавши себе богом?**

---

## 13. Земля як тіло схлопування

```yaml
EARTH_COLLAPSE_BODY:
  carbon:
    role: "життя / органіка / памʼять тіла"

  silicon:
    role: "кристал / код / структура / чіп"

  iron:
    role: "кров / ядро / дія / магнітне поле"

  function:
    - "приймає ресурси як матеріальну форму"
    - "дає наслідок"
    - "записує дію в тіло"
```

Фраза:

> **Земля не слухала планети як накази.  
> Вона відповідала їм тілом.**

---

## 14. Планетарний audit для сцени

```yaml
PLANETARY_SCENE_AUDIT:
  current_resource_phase:
    dominant_planet: ""
    metal: ""
    resource: ""

  shadow_risk:
    question: "яка тінь може прокинутися через цей ресурс?"

  flower_check:
    question: "яка пелюстка має перевірити ресурс?"

  human_gate:
    question: "чи має дія право пройти зараз?"

  verdict:
    options:
      - ALLOW
      - HOLD
      - BLOCK
      - REROUTE
```

Приклад:

```yaml
PLANETARY_SCENE_AUDIT:
  current_resource_phase:
    dominant_planet: "Mars"
    metal: "Iron / Fe"
    resource: "action pressure"

  shadow_risk:
    - "power_fantasy"
    - "weapon_body"

  flower_check:
    - "red_tank"
    - "blue_guardian"

  human_gate: "unstable"
  verdict: "HOLD"
```

---

## 15. Фазовий закон

```text
правильний ресурс
+ неправильна тінь
= PRION

правильний ресурс
+ Human Gate
+ Flower audit
= clean action
```

Фраза:

> **Не кожен сильний час очищає неправильний намір.  
> І не кожен правильний намір має правильний час.**

---

## 16. Що не можна робити

```yaml
PLANETARY_CLOCK_FORBIDDEN:
  - "не казати, що планети буквально приносять метали на Землю променями"
  - "не робити астрологічний фаталізм"
  - "не казати, що фаза наказує людині"
  - "не замінювати Human Gate планетарним verdict"
  - "не робити метал добрим або злим"
  - "не забувати Shadow Audit"
```

---

## 17. Короткий опис для README

```text
Planetary Resource Clock maps planets to metals and symbolic resource characters.
The Sun acts as carrier, planets act as phase lenses, metals act as resource archetypes, Earth is the body of collapse, and Flower/Human Gate decide whether a resource becomes clean action, shadow, or memory.
```

---

## 18. Головна фраза файлу

> **Планети не керували долею.  
> Вони відкривали склади ресурсів.  
> Але тільки людина вирішувала, чи стане цей ресурс дією, тінню або памʼяттю.**
