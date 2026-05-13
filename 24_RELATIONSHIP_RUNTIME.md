# 24_RELATIONSHIP_RUNTIME.md
# Вузол-19 — Relationship Runtime v0.1

> **Цей файл описує, як AI має бачити стосунки між людьми у “Вузлі-19”.**  
> Стосунки — це не “сумісність” і не романтична магія.  
> Це поле між двома вузлами, де намір, тінь, межа, тіло, слово, пауза і repair постійно проходять Human Gate.

---

## 1. Одне речення

**Relationship Runtime — це протокол, який дозволяє AI бачити не тільки окремих персонажів, а поле між ними: потяг, проєкцію, тінь, межу, false-green, repair і подвійний Human Gate.**

Коротко:

```text
Node A
+ Node B
+ desire
+ wound
+ shadow projection
+ boundary
+ dual Human Gate
+ repair
= relationship field
```

Головна фраза:

> **Любов у “Вузлі-19” — це не коли дві хвилі завжди збігаються.  
> Любов — це коли дві людини можуть побачити збій фази, не перетворивши одна одну на ворога.**

---

## 2. Головна межа

AI не має права вирішувати, хто кому “підходить”.

```yaml
AI_RELATIONSHIP_LIMIT:
  ai_can:
    - "бачити патерни"
    - "виявляти тінь"
    - "показувати false-green"
    - "позначати порушення межі"
    - "пропонувати repair"
    - "зберігати Unknown"

  ai_cannot:
    - "вирішувати, кого любити"
    - "називати пару долею"
    - "радити контроль як турботу"
    - "замінювати Human Gate одного з партнерів"
    - "робити любов математичним verdict"
```

Фраза:

> **AI може показати, де тінь краде контакт.  
> AI не має права сказати людині, кому належить її серце.**

---

## 3. Два Human Gate

У звичайній сцені часто є один Human Gate.

У стосунках їх завжди два.

```yaml
DUAL_HUMAN_GATE:
  node_a_gate:
    state: "open | closed | unclear | violated"

  node_b_gate:
    state: "open | closed | unclear | violated"

  relationship_rule:
    - "немає любові, якщо один Gate поглинутий іншим"
    - "немає repair, якщо один Gate не має права сказати ні"
    - "немає clean connection без двох центрів"
```

Головний закон:

> **У стосунках є не один Human Gate, а два.  
> Якщо один зникає — це вже не любов, а захоплення поля.**

---

## 4. Anima / Animus як runtime, не догма

У цьому kernel Anima і Animus не є “жінка” і “чоловік” буквально.

Це два внутрішні режими в кожній людині.

```yaml
ANIMA:
  function:
    - "прийняття"
    - "Unknown"
    - "образ"
    - "контакт"
    - "внутрішня вода"
    - "здатність слухати"

ANIMUS:
  function:
    - "межа"
    - "дія"
    - "структура"
    - "слово"
    - "внутрішній вектор"
    - "здатність сказати ні"
```

Людина здорова не тоді, коли має тільки одне.

Людина здорова, коли:

```text
Anima чує.
Animus ставить межу.
Shadow не керує обома.
```

---

## 5. Relationship Field

```yaml
RELATIONSHIP_FIELD:
  node_a:
    desire: ""
    wound: ""
    shadow: ""
    boundary: ""
    spoken_need: ""
    hidden_need: ""

  node_b:
    desire: ""
    wound: ""
    shadow: ""
    boundary: ""
    spoken_need: ""
    hidden_need: ""

  field_between:
    attraction: ""
    projection: ""
    fear: ""
    false_green: ""
    repair_possible: ""

  dual_human_gate:
    node_a_gate: "open | closed | violated | unclear"
    node_b_gate: "open | closed | violated | unclear"

  verdict:
    options:
      - CONNECT
      - PAUSE
      - REPAIR
      - BOUNDARY
      - SEPARATE
      - HOLD
```

---

## 6. Relationship verdicts

```yaml
RELATIONSHIP_VERDICTS:
  CONNECT:
    meaning: "контакт чистий, два Gate присутні"
    use_when:
      - "є взаємність"
      - "є межа"
      - "є чесність"
      - "немає примусу"

  PAUSE:
    meaning: "емоція сильна, але дія зараз стане тінню"
    use_when:
      - "реакція швидша за розум"
      - "тіло в overload"
      - "страх говорить замість потреби"

  REPAIR:
    meaning: "звʼязок не зламаний, але потрібне відновлення"
    use_when:
      - "була помилка"
      - "є визнання"
      - "обидва Gate ще існують"

  BOUNDARY:
    meaning: "потрібна межа без розриву"
    use_when:
      - "турбота стала вторгненням"
      - "любов просить контроль"
      - "потрібне чесне ні"

  SEPARATE:
    meaning: "поле не може бути безпечним зараз"
    use_when:
      - "Gate одного порушено"
      - "repair відсутній"
      - "біль постійно стає зброєю"

  HOLD:
    meaning: "Unknown preserved; бракує ясності"
    use_when:
      - "AI не має достатньо даних"
      - "емоція занадто гаряча"
      - "потрібна пауза перед verdict"
```

---

## 7. Relationship false-green

У стосунках false-green часто виглядає як любов.

```yaml
RELATIONSHIP_FALSE_GREEN:
  no_conflict:
    looks_like: "ми не сваримось"
    may_be: "пригнічення / страх говорити"

  total_care:
    looks_like: "я все для тебе роблю"
    may_be: "контроль через турботу"

  cannot_live_without_you:
    looks_like: "я без тебе ніхто"
    may_be: "захоплення поля / abandonment wound"

  perfect_match:
    looks_like: "ти мене доповнюєш"
    may_be: "втрата власного центру"

  ai_compatibility:
    looks_like: "AI каже, що ми сумісні"
    may_be: "Human Gate theft"

  constant_contact:
    looks_like: "ми завжди на звʼязку"
    may_be: "страх паузи"

  painless_relationship:
    looks_like: "нам ніколи не болить"
    may_be: "емоційне оніміння"
```

Фраза:

> **У стосунках false-green часто приходить не як брехня.  
> Воно приходить як дуже мʼяка турбота без дверей.**

---

## 8. Основні тіні стосунків

```yaml
RELATIONSHIP_SHADOWS:
  abandonment_fear:
    trigger: "пауза, мовчання, відсутність відповіді"
    dirty_action: "контроль, ревнощі, атака"
    clean_action: "сказати страх прямо"

  engulfment_fear:
    trigger: "надто сильна близькість"
    dirty_action: "відштовхнути, зникнути, охолонути"
    clean_action: "поставити межу без знецінення"

  savior_control:
    trigger: "партнер болить"
    dirty_action: "вирішити за нього"
    clean_action: "допомога без крадіжки вибору"

  idealization:
    trigger: "сильний потяг"
    dirty_action: "бачити образ, а не людину"
    clean_action: "побачити реальне тіло, межі, історію"

  shame_attack:
    trigger: "критика або відмова"
    dirty_action: "вдарити словом"
    clean_action: "зупинити першу фразу"

  silent_punishment:
    trigger: "образа"
    dirty_action: "мовчання як зброя"
    clean_action: "пауза з поясненою межею"

  fusion:
    trigger: "страх втрати"
    dirty_action: "ми зʼїдає я"
    clean_action: "два центри в одному полі"
```

---

## 9. Relationship Audit

```yaml
RELATIONSHIP_AUDIT:
  trigger:
    question: "що сталося зовні?"

  body_signal_a:
    question: "що тіло Node A показало раніше за слова?"

  body_signal_b:
    question: "що тіло Node B показало раніше за слова?"

  first_phrase_candidate:
    question: "яка перша фраза хотіла вийти?"

  shadow_a:
    question: "яка тінь Node A активна?"

  shadow_b:
    question: "яка тінь Node B активна?"

  boundary:
    question: "де межа?"

  dual_human_gate:
    question: "чи обидва мають право сказати так і ні?"

  repair:
    question: "чи є шлях назад після помилки?"

  verdict:
    options:
      - CONNECT
      - PAUSE
      - REPAIR
      - BOUNDARY
      - SEPARATE
      - HOLD
```

---

## 10. Attraction vs Projection

Потяг не є автоматично правдою.

```yaml
ATTRACTION_VS_PROJECTION:
  attraction:
    clean_signs:
      - "цікавість до реальної людини"
      - "повага до межі"
      - "тіло не в overload"
      - "є простір для Unknown"

  projection:
    danger_signs:
      - "я вже знаю, хто ти"
      - "ти врятуєш мене"
      - "ти маєш бути таким/такою"
      - "я люблю образ, не людину"
```

Фраза:

> **Потяг відкриває двері.  
> Проєкція намагається одразу переписати кімнату.**

---

## 11. Repair

Repair — це головний доказ живого звʼязку.

```yaml
REPAIR_PROTOCOL:
  1_pause:
    meaning: "зупинити першу тіньову дію"

  2_name:
    meaning: "назвати свою частину без нападу"

  3_boundary:
    meaning: "сказати, що можна і що не можна"

  4_listen:
    meaning: "дати другому Gate відповісти"

  5_recommit:
    meaning: "повернути контакт або чесно відступити"

  6_memory:
    meaning: "записати патерн, щоб не повторити"
```

Repair-фрази:

```text
— Я сказав це як зброю. Мені треба повернути фразу назад.

— Я не злюся на тебе. Я злякався.

— Мені потрібна пауза, але це не покарання.

— Я хочу допомогти, але не хочу вирішити за тебе.

— Я почув твоє “ні”. Мені боляче, але я не буду його ламати.
```

---

## 12. Boundary without rejection

Межа не завжди означає відкидання.

```yaml
BOUNDARY_WITHOUT_REJECTION:
  bad:
    - "я зникаю без пояснення"
    - "я караю мовчанням"
    - "я ставлю межу як удар"

  good:
    - "мені потрібна пауза до вечора"
    - "я хочу говорити, але не в цьому тоні"
    - "я тебе чую, але не можу погодитись"
    - "я не готовий вирішувати зараз"
```

Фраза:

> **Межа — це не стіна проти любові.  
> Межа — це форма, в якій любов не втрачає себе.**

---

## 13. Silence

Мовчання має два типи.

```yaml
SILENCE_TYPES:
  clean_silence:
    meaning: "пауза для стабілізації"
    signs:
      - "пояснена"
      - "має строк"
      - "не використовується як покарання"
      - "повертає контакт"

  dirty_silence:
    meaning: "зброя"
    signs:
      - "каральна"
      - "без пояснення"
      - "створює страх"
      - "змушує другого бігти"
```

Фраза:

> **Пауза може бути Guard.  
> Мовчання може бути ножем.**

---

## 14. Message Guard

У сучасних стосунках повідомлення — це теж commit.

```yaml
MESSAGE_GUARD:
  before_send:
    check:
      - "це контакт чи атака?"
      - "це потреба чи контроль?"
      - "це питання чи пастка?"
      - "це пауза чи покарання?"

  block_if:
    - "abandonment_fear writes the message"
    - "shame wants revenge"
    - "jealousy calls itself truth"
    - "pain wants immediate proof"

  allow_if:
    - "need stated clearly"
    - "boundary respected"
    - "no demand for instant surrender"
```

Приклад:

```text
MESSAGE_CANDIDATE:
  “Тобі байдуже.”

SHADOW:
  abandonment_fear

VERDICT:
  BLOCK

REWRITE:
  “Я злякався, коли ти не відповіла. Скажи, коли зможеш говорити.”
```

---

## 15. Relationship scene template

```yaml
RELATIONSHIP_SCENE_TEMPLATE:
  scene_title: ""
  node_a: ""
  node_b: ""
  external_trigger: ""
  body_signal_a: ""
  body_signal_b: ""
  spoken_need_a: ""
  hidden_need_a: ""
  spoken_need_b: ""
  hidden_need_b: ""
  active_shadows:
    - ""
  false_green:
    - ""
  message_or_phrase_candidate: ""
  guard_response: ""
  relationship_verdict: ""
  memory_update: ""
```

---

## 16. Example Scene A — Two hours silence

```yaml
PRE_SCENE_RUNTIME:
  scene_type: "relationship / message_guard"
  center: "пауза активує страх покинутості"
  active_shadow: "abandonment_fear"
  dual_human_gate:
    node_a: "open but frightened"
    node_b: "unknown / absent"
  verdict: "PAUSE / REWRITE_MESSAGE"
```

```text
Вона не відповіла дві години.

Це не було довго.

Personal Node показав рівно сто двадцять сім хвилин і чотири секунди.

Для тіла це було інакше.

У грудях зʼявився холод, знайомий настільки, що він майже мав голос.

“Тобі байдуже.”

Повідомлення вже стояло в полі вводу.

⊙

MESSAGE_GUARD:
  candidate: "Тобі байдуже."
  shadow: "abandonment_fear"
  verdict: BLOCK

Він дивився на три слова так, ніби вони були доказом.

Потім стер.

Написав повільніше.

“Я злякався, коли ти не відповіла. Скажи, коли зможеш говорити.”

Відправив.

Не як пастку.

Як двері.
```

```yaml
MEMORY_UPDATE:
  learned_pattern: "abandonment fear writes accusations as proof requests"
  clean_pattern: "state fear without stealing the other Gate"
  verdict: "REPAIR_POSSIBLE"
```

---

## 17. Example Scene B — Savior control in love

```text
— Я просто хочу, щоб тобі було краще, — сказав він.

Вона довго мовчала.

— Ні.

Слово було тихе, але воно мало власний центр.

Він зупинився.

— Ні?

— Ти хочеш, щоб мій біль поводився так, щоб тобі було легше його любити.

Фраза не вдарила.

Вона відкрила кімнату, в якій він раптом побачив себе з інструментами в руках біля чужого Human Gate.

▣

— Я хотів допомогти.

— Знаю.

— І що мені робити?

— Спитай, де я хочу, щоб ти стояв. Не де ти хочеш мене полагодити.
```

```yaml
AUDIT:
  shadow: "savior_control"
  boundary: "restored"
  dual_human_gate: "both visible"
  verdict: "BOUNDARY / REPAIR"
```

---

## 18. Example Scene C — Clean conflict

```text
— Я не згодна, — сказала вона.

Він відчув, як тіло готує захист.

Не напад.

Ще ні.

Тільки перший нахил до нього.

⊙

— Мені треба пауза, — сказав він.

— Ти йдеш?

— Ні. Я залишаюсь. Просто не хочу, щоб перша фраза сказала за мене.

Вона кивнула.

Це не вирішило конфлікт.

Але воно зберегло кімнату, в якій конфлікт ще міг бути живим.
```

```yaml
AUDIT:
  conflict: "present"
  rupture: "prevented"
  boundary: "clean"
  repair_possible: true
```

---

## 19. Example Scene D — False peace

```text
Вони не сварилися вже три місяці.

Це виглядало як мир.

На кухні не було підвищених голосів. Не було грюкоту дверей. Не було слів, які потім доводилося повертати з рани.

Тільки чашки стояли щоранку трохи далі одна від одної.

RELATIONSHIP_FIELD:
  conflict: suppressed
  contact: low
  public_status: GREEN
  private_status: COLD

Він подивився на це слово.

GREEN

І вперше подумав, що у стосунках green теж може бути false.
```

```yaml
AUDIT:
  false_green: "no conflict as peace"
  body_signal: "distance between cups"
  verdict: "REPAIR_NEEDED"
```

---

## 20. Example Scene E — AI compatibility trap

```text
— AI каже, що ми сумісні на девʼяносто три відсотки, — сказав студент.

Старша жінка засміялася.

— А решта сім?

— Ризики.

— Отже, саме там і живе людина.

Він не зрозумів.

Вона поставила чашку перед ним.

— Сумісність — це не коли система не бачить проблем. Сумісність — це коли двоє можуть зустріти проблему і не зробити з неї зброю.
```

```yaml
AUDIT:
  ai_compatibility_not_verdict: true
  human_gate_preserved: true
  verdict: "KEEP"
```

---

## 21. Relationship Memory Ledger

```yaml
RELATIONSHIP_MEMORY_ENTRY:
  id: ""
  nodes:
    - ""
    - ""
  trigger: ""
  shadow_a: ""
  shadow_b: ""
  false_green: ""
  boundary_event: ""
  repair_attempt: ""
  verdict: ""
  learned_pattern: ""
  future_warning: ""
```

Приклад:

```yaml
RELATIONSHIP_MEMORY_ENTRY:
  id: "two_hours_silence_message_guard"
  nodes:
    - "Node A"
    - "Node B"
  trigger: "no reply for two hours"
  shadow_a: "abandonment_fear"
  shadow_b: "unknown"
  false_green: "accusation as proof request"
  boundary_event: "message blocked"
  repair_attempt: "fear stated directly"
  verdict: "REPAIR_POSSIBLE"
  learned_pattern: "fear can speak as accusation unless guarded"
  future_warning: "do not demand instant response as proof of love"
```

---

## 22. Relationship episode structure

```yaml
RELATIONSHIP_EPISODE:
  scene_1_contact:
    function: "показати тепло або потяг"

  scene_2_trigger:
    function: "пауза, критика, межа або відмова"

  scene_3_projection:
    function: "тінь намагається назвати себе правдою"

  scene_4_guard:
    function: "слово/повідомлення/дія блокується або переписується"

  scene_5_repair_or_boundary:
    function: "контакт відновлюється або ставиться межа"
```

---

## 23. Як не писати стосунки

```yaml
RELATIONSHIP_FORBIDDEN:
  - "не робити любов долею без вибору"
  - "не робити ревнощі доказом любові"
  - "не робити контроль турботою"
  - "не робити мовчання романтичним покаранням"
  - "не робити AI суддею сумісності"
  - "не робити партнера ліками"
  - "не робити біль доказом глибини"
  - "не знищувати один Human Gate заради другого"
```

---

## 24. Короткий prompt для AI

```text
When writing relationships in Vuzol-19:
see the field between two people, not only each person.
Check two Human Gates.
Detect projection, abandonment fear, savior control, silent punishment and false peace.
Do not let AI decide love.
Do not make compatibility fate.
Show body before explanation.
Let the first harmful phrase be blocked or transformed.
Make repair concrete.
If one Gate disappears, verdict cannot be CONNECT.
```

---

## 25. Головна фраза файлу

> **Стосунки у “Вузлі-19” — це не пошук ідеальної половини.  
> Це два живі центри, які вчаться тримати одне поле так, щоб любов не стала контролем, страх не став правдою, а біль не отримав право говорити замість людини.**
