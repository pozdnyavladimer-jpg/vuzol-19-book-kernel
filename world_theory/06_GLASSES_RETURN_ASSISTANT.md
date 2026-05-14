# 06_GLASSES_RETURN_ASSISTANT.md
# Vuzol-19 — Glasses Return Assistant v0.1

> **The glasses do not lead the person by force.**  
> They keep the return path visible.

---

## 1. Boundary

```yaml
FACT:
  - "Assistive visual interfaces are possible in modern and speculative technology."

MODEL:
  - "Vuzol-19 models glasses as a Return Assistant."

FICTION:
  - "In the novel, glasses help a person see when a path becomes a cage."

HOLD:
  - "Do not make the assistant a hidden controller."
  - "Do not replace user choice with navigation."
```

---

## 2. Core role

```text
CAPSULE shows possible worlds.
BOX remembers shadow patterns.
CROWN reads current state.
GLASSES show the way back.
AI GUARD warns.
HUMAN GATE chooses.
```

---

## 3. What glasses can say

```text
I see a repeated pattern.
This path is becoming a loop.
You can pause.
There is a return path.
This is a small action.
You do not need to decide the whole life now.
```

What glasses must not say:

```text
This is your destiny.
You must do this.
The system knows better.
Your fear proves you should obey.
```

---

## 4. Return path template

```yaml
RETURN_PATH:
  status:
    - VISIBLE
    - WEAK
    - HIDDEN
    - BROKEN

  smallest_step: ""
  real_world_anchor: ""
  body_anchor: ""
  human_contact: ""
  time_limit: ""
```

---

## 5. Scene use

```yaml
SCENE_SEEDS:
  capsule_exit:
    one_line: "The capsule offers three perfect lives, but the glasses show one imperfect door back."

  small_commit:
    one_line: "The glasses do not show destiny, only a 2-minute real-world action."

  assistant_refuses:
    one_line: "The user asks for the correct path, and the glasses answer: I can only show the door."
```

---

## 6. Main sentence

> **The assistant does not walk the path for the person.  
> It lights the door when the path starts becoming a prison.**
