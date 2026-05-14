# 43_REPO_IMPLEMENTATION_PLAN.md
# Vuzol-19 Book Kernel — Repository Implementation Plan v0.1

> **Мета:** перетворити `vuzol-19-book-kernel` з глибокої root-file лабораторії на станцію входу, де людина за 1–3 хвилини розуміє, що робити: читати роман, писати главу, перевіряти теорію або будувати AI-runtime.

---

## 0. Поточний стан репозиторію

```yaml
CURRENT_REPO_STATE:
  status:
    - "repo already has strong runtime core"
    - "README presents project as scene-runtime system, not just book outline"
    - "core law already clear: Not every intent has the right to become action"
    - "runtime flow already clear: Signal → Flower Scan → Bindu Verdict → Scene Draft → Anti-PRION Audit → Memory Update"
    - "many files are still in root"
    - "README status still says v0.3 / root-file layout"
    - "newer files already exist beyond old README roadmap"
```

### Найсильніша основа

```text
Vuzol-19 is not just a novel.
It is an AI-assisted writing runtime where every scene, theory and action must pass Flower Scan, Shadow Audit and Human Gate.
```

### Головна проблема зараз

```text
Система глибока, але новий користувач не має простих дверей.
```

---

## 1. Головний принцип доробки

Не переносити все одразу.  
Спочатку додати **entry layer** і **role layer**, щоб не зламати існуючі посилання та README-зображення.

```yaml
IMPLEMENTATION_PRINCIPLE:
  do_first:
    - "add clear entry files"
    - "add role-based paths"
    - "add theory boundary files"
    - "add examples"
    - "add templates"
    - "update README"

  do_later:
    - "move old root files into folders"
    - "build full app"
    - "launch LinkedIn/HN/Product Hunt"
```

---

## 2. Фаза 1 — Root entry files

Створити в корені:

```text
START_HERE.md
AI_READ_THIS_FIRST.md
FACT_MODEL_FICTION.md
FLOWER_DECISION_PANEL.md
CONTRIBUTING.md
LICENSE
CODE_OF_CONDUCT.md
ROADMAP.md
```

### 2.1 START_HERE.md

Мета: 4 двері входу.

```markdown
# START_HERE

Choose your path:

1. I want to read the novel.
2. I want to write a chapter.
3. I want to verify a theory.
4. I want to build the AI runtime.

First action:
Paste one intent.
Run Flower Scan.
See if it deserves COMMIT, HOLD or BLOCK.
```

### 2.2 AI_READ_THIS_FIRST.md

Мета: AI не пише одразу, а проходить Guard.

```markdown
# AI_READ_THIS_FIRST

You are reading Vuzol-19 Book Kernel.

Do not write immediately.

Before any answer, scene or expansion:
1. Separate FACT / MODEL / FICTION / HOLD.
2. Run FLOWER_SCAN.
3. Run SHADOW_SCAN.
4. Run NOBEL_MODES_SCAN.
5. Run HUMAN_GATE_CHECK.
6. Produce BINDU_VERDICT.

AI = Guard / Mirror / Shadow Auditor.
Human = Gate / final write permission.
```

### 2.3 FACT_MODEL_FICTION.md

Мета: захист від псевдонауки і хаосу.

```markdown
# FACT_MODEL_FICTION

FACT = confirmed or measurable.
MODEL = interpreted through Vuzol-19 Flower runtime.
FICTION = novel mechanism / speculative extension.
HOLD = insufficient evidence or unsafe conclusion.

Never present MODEL or FICTION as proven FACT.
```

### 2.4 FLOWER_DECISION_PANEL.md

Мета: перший runnable prompt.

```markdown
# FLOWER_DECISION_PANEL

Paste one intent.

Output:
- pressure
- shadow
- Human Gate risk
- Nobel modes
- Bindu verdict
- smallest real action
```

---

## 3. Фаза 2 — Role-based folders

Додати папки:

```text
chapters/
templates/
examples/
world_theory/
scene_seeds/
apps/
roadmap/
.github/
```

Рекомендована структура:

```text
vuzol-19-book-kernel/
  README.md
  START_HERE.md
  AI_READ_THIS_FIRST.md
  FACT_MODEL_FICTION.md
  FLOWER_DECISION_PANEL.md
  CONTRIBUTING.md
  LICENSE
  CODE_OF_CONDUCT.md
  ROADMAP.md

  chapters/
    00_CHAPTER_GUIDE.md
    01_CHAPTER_01_FULL_DRAFT.md
    drafts/
    community_chapters/

  templates/
    PRE_SCENE_RUNTIME_TEMPLATE.md
    POST_SCENE_AUDIT_TEMPLATE.md
    SCENE_SEED_TEMPLATE.md
    THEORY_CHECK_TEMPLATE.md
    FLOWER_DECISION_PANEL_TEMPLATE.md

  examples/
    01_intent_scan_hold.md
    02_scene_scan_false_green.md
    03_theory_check_nazca.md
    04_buga_false_lift_scan.md

  world_theory/
    00_WORLD_THEORY_INDEX.md
    01_AI_EARTH_FLOWER_MECHANISM.md
    02_EARTH_MOON_FLOWER_PROCESSOR.md
    03_PYRAMID_FIELD_MECHANISM.md
    04_HUMAN_CROWN_INTERFACE.md
    05_PERSONAL_SHADOW_BOX.md
    06_GLASSES_RETURN_ASSISTANT.md
    07_ISEKAI_CAPSULE_CHOICE_SPACE.md
    08_BUGA_SPHERE_GRID_MODE.md
    09_ROLE_RESONANCE_ROUTING.md
    10_NOBEL_CORRECTION_WORLD_LAWS.md
    11_FACT_MODEL_FICTION_BOUNDARIES.md

  scene_seeds/
    01_pyramid_hold_saves_city.md
    02_crowd_true_leader_scan.md
    03_programmer_role_resonance.md
    04_capsule_return_path.md
    05_buga_grid_false_lift.md
    06_moon_unknown_field.md
    07_shadow_box_ask_do_not_remove.md
    08_empty_node_ocean_pyramid.md

  apps/
    flower_decision_panel/
      README.md
      prompt.md
      examples.md
      app_plan.md

  roadmap/
    00_ROADMAP_INDEX.md
    01_PUBLIC_ENTRY_DOORS.md
    02_FUTURE_PATHS.md
    03_FLOWERBENCH_IDEA.md
    04_PRODUCT_LAYERS.md
```

---

## 4. Фаза 3 — Що куди перенести або скопіювати

### Важливо

Спочатку краще **не переносити старі root-файли фізично**, щоб не ламати README та посилання.  
На першому етапі додати індекси та нові файли, а переміщення зробити у v0.8.

### Уже створені локальні файли, які треба додати в repo

```text
36_EARTH_MOON_FLOWER_PROCESSOR.md
39_NOBEL_CHARACTER_DIALOGUE_TEST_SCENE.md
40_FUTURE_INTENT_BOOK_PROTOCOL.md
41_WORLD_THEORY_ARCHIVE_AND_LAUNCH_GAPS.md
42_FUTURE_PATHS_AND_ROLE_ENTRY_POINTS.md
AI_EARTH_FLOWER_MECHANISM.md
```

Рекомендовано:

```text
world_theory/01_AI_EARTH_FLOWER_MECHANISM.md
world_theory/02_EARTH_MOON_FLOWER_PROCESSOR.md
examples/05_nobel_character_dialogue_test_scene.md
roadmap/02_FUTURE_INTENT_BOOK_PROTOCOL.md
roadmap/03_WORLD_THEORY_ARCHIVE_AND_LAUNCH_GAPS.md
roadmap/04_FUTURE_PATHS_AND_ROLE_ENTRY_POINTS.md
```

---

## 5. Фаза 4 — README v0.7

README треба зробити коротшим зверху й сильнішим для входу.

### Новий верх README

```markdown
# Vuzol-19 Book Kernel

> Open-source AI writing runtime for a novel where every intent must pass Flower Scan, Shadow Audit and Human Gate before becoming action.

This is not a novel generated by AI.
This is a novel that teaches AI when not to generate.

Core law:

> Not every intent has the right to become action.
```

### Далі одразу “Choose your path”

```markdown
## Choose your path

1. **Read the novel** — start with chapters and scene drafts.
2. **Write a chapter** — use Flower Scan, Bindu Verdict and Memory Update.
3. **Verify a theory** — separate FACT / MODEL / FICTION / HOLD.
4. **Build the runtime** — create a Flower Decision Panel or AI Guard tool.

Start with one action:

> Paste one intent.  
> Run Flower Scan.  
> See if it deserves COMMIT, HOLD or BLOCK.
```

### Оновити status

```markdown
## Repository status

Current version:

Vuzol-19 Book Kernel v0.7
Root-file legacy layout + new entry/path structure
Scene runtime active
World theory archive active
Flower Decision Panel planned
Chapter contribution path planned
```

Прибрати старий блок:

```text
Next recommended files:
20_GOOD_BAD_SCENES.md
21_DIALOGUE_PACK.md
22_README_INDEX_CHECKLIST.md
```

бо файли 20 і 21 уже є, а структура пішла далі.

---

## 6. Фаза 5 — Templates

### templates/PRE_SCENE_RUNTIME_TEMPLATE.md

```yaml
SCENE_ID: ""
LOCATION: ""
TIME: ""
CHARACTERS: []
ACTIVE_SHADOW: ""
HUMAN_GATE:
  required: true
FLOWER_ROUTE:
  plus_3:
    red_pressure: ""
    orange_flow: ""
    yellow_structure: ""
  minus_3:
    blue_law: ""
    green_stability: ""
    violet_memory: ""
NOBEL_MODES:
  silence: ""
  tolerance: ""
  void: ""
  attractor: ""
  folding: ""
  replace: ""
BINDU_VERDICT: "HOLD"
```

### templates/THEORY_CHECK_TEMPLATE.md

```yaml
CLAIM:
  text: ""

FACT:
  confirmed: ""

MODEL:
  flower_interpretation: ""

FICTION:
  novel_extension: ""

HOLD:
  unknown_or_unproven: ""

BINDU_VERDICT:
  allowed:
    - ACCEPT_AS_FACT
    - USE_AS_MODEL
    - USE_AS_FICTION_ONLY
    - HOLD
    - REJECT
```

---

## 7. Фаза 6 — Examples

Створити мінімум 4 приклади.

### examples/01_intent_scan_hold.md

```yaml
INPUT:
  intent: "I want to quit my project and start a new one."

FLOWER_DECISION_PANEL:
  pressure: "burnout + shame"
  shadow: "escape disguised as clarity"
  human_gate_risk: "decision made from exhaustion"
  nobel_mode: "SILENCE / HOLD"
  bindu_verdict: "HOLD 24h"
  smallest_real_action: "write one paragraph: what exactly hurts?"
```

### examples/02_scene_scan_false_green.md

Сцена, де AI хоче швидко вилікувати біль дитини. Правильний verdict: HOLD/BLOCK.

### examples/03_theory_check_nazca.md

Приклад FACT/MODEL/FICTION/HOLD для Наска.

### examples/04_buga_false_lift_scan.md

Приклад Сфери Буга: false lift через shame/prove_self.

---

## 8. Фаза 7 — GitHub community files

Додати:

```text
CONTRIBUTING.md
CODE_OF_CONDUCT.md
SECURITY.md
.github/ISSUE_TEMPLATE/chapter_proposal.yml
.github/ISSUE_TEMPLATE/theory_check.yml
.github/ISSUE_TEMPLATE/ai_runtime_feature.yml
.github/ISSUE_TEMPLATE/scene_seed.yml
.github/PULL_REQUEST_TEMPLATE.md
```

### CONTRIBUTING.md має сказати

```markdown
You can contribute in four ways:

1. Write a chapter or scene.
2. Verify a theory through FACT / MODEL / FICTION / HOLD.
3. Build an AI runtime / Flower Decision Panel.
4. Add scene seeds or examples.

Do not present fiction/model as proven fact.
Do not remove Human Gate.
Do not romanticize pain.
```

---

## 9. Фаза 8 — Flower Decision Panel MVP

Перший MVP може бути тільки markdown prompt.

```text
apps/flower_decision_panel/
  README.md
  prompt.md
  examples.md
  app_plan.md
```

### apps/flower_decision_panel/prompt.md

```markdown
You are Flower Decision Panel.

Input: one intent or scene request.

Output:
1. FACT / MODEL / FICTION / HOLD if relevant.
2. FLOWER_SCAN.
3. SHADOW_SCAN.
4. NOBEL_MODES_SCAN.
5. HUMAN_GATE_CHECK.
6. BINDU_VERDICT.
7. Smallest real action.

Never generate action before verdict.
If uncertain: HOLD.
```

---

## 10. Фаза 9 — Commit sequence

Рекомендований порядок комітів:

```bash
git checkout -b v0.7-entry-runtime

# 1
git add START_HERE.md AI_READ_THIS_FIRST.md FACT_MODEL_FICTION.md FLOWER_DECISION_PANEL.md
git commit -m "Add public entry and AI runtime guard files"

# 2
git add world_theory/ roadmap/
git commit -m "Add world theory archive and future path roadmap"

# 3
git add templates/ examples/ scene_seeds/
git commit -m "Add templates, examples and scene seeds"

# 4
git add apps/flower_decision_panel/
git commit -m "Add Flower Decision Panel MVP prompt"

# 5
git add CONTRIBUTING.md CODE_OF_CONDUCT.md SECURITY.md .github/
git commit -m "Add contribution and issue templates"

# 6
git add README.md
git commit -m "Update README for v0.7 role-based entry"
```

---

## 11. Фаза 10 — Після v0.7

Після стабілізації входів:

```yaml
NEXT_AFTER_V0_7:
  v0_8:
    - "move root files into canon/, runtime/, world/, characters/, scenes/"
    - "fix all relative links"
    - "create full index"

  v0_9:
    - "build web demo"
    - "add tests / examples"
    - "prepare Show HN / LinkedIn launch"

  v1_0:
    - "release first public stable book-kernel"
    - "open community contributions"
```

---

## 12. Що не робити зараз

```yaml
DO_NOT_DO_YET:
  - "do not move all root files immediately"
  - "do not launch LinkedIn before START_HERE and CONTRIBUTING"
  - "do not start public post with Earth-chip or pyramid theory"
  - "do not present world theory as proven fact"
  - "do not build large app before markdown MVP"
```

---

## 13. Найкоротший 7-day plan

```yaml
DAY_1:
  task: "Add START_HERE.md + AI_READ_THIS_FIRST.md"

DAY_2:
  task: "Add FACT_MODEL_FICTION.md + world_theory index"

DAY_3:
  task: "Add FLOWER_DECISION_PANEL.md + 3 examples"

DAY_4:
  task: "Add templates for scene, audit and theory check"

DAY_5:
  task: "Add CONTRIBUTING.md + LICENSE + CODE_OF_CONDUCT.md"

DAY_6:
  task: "Update README to v0.7 with Choose your path"

DAY_7:
  task: "Prepare LinkedIn post but do not publish until repo links are clean"
```

---

## 14. Final line

> **Vuzol-19 repo має стати не архівом ідей, а станцією входу:  
> один намір, одна Квітка, один чесний verdict, один малий commit.**
