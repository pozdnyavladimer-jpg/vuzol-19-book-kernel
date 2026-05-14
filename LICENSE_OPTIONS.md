# LICENSE_OPTIONS.md
# Vuzol-19 License Options

> **This file is not legal advice.**  
> It helps choose a license before public contribution grows.

Vuzol-19 includes both:

```text
code / prompts / app ideas
book text / canon / world theory / fiction
```

Because of that, a dual license may be better than one license for everything.

---

## Option 1 — MIT for code, CC BY-SA for text

```yaml
CODE:
  license: "MIT"
  applies_to:
    - "apps/"
    - "scripts/"
    - "runtime code"

TEXT:
  license: "CC BY-SA 4.0"
  applies_to:
    - "chapters/"
    - "world_theory/"
    - "templates/"
    - "examples/"
    - "scene_seeds/"
```

Meaning:

```text
People can use and modify code freely.
People can remix text if they credit and share alike.
```

---

## Option 2 — MIT for code, CC BY-NC-SA for text

```yaml
CODE:
  license: "MIT"

TEXT:
  license: "CC BY-NC-SA 4.0"
```

Meaning:

```text
Open collaboration is allowed.
Commercial reuse of text requires permission.
```

This may protect the novel/world IP more strongly.

---

## Option 3 — All Rights Reserved for fiction, MIT for tools

```yaml
CODE:
  license: "MIT"

FICTION_WORLD:
  license: "All rights reserved unless explicitly permitted"
```

Meaning:

```text
People can build tools.
But chapters/world canon stay controlled by the author.
```

This is safer for a novel, but less open for community writing.

---

## Recommended starting point

For Vuzol-19 right now:

```yaml
RECOMMENDATION:
  code_and_apps: "MIT"
  prompts_templates_examples: "CC BY-SA 4.0 or CC BY-NC-SA 4.0"
  novel_chapters_and_core_canon: "consider CC BY-NC-SA or author-controlled license"
```

---

## What to decide before LinkedIn

```text
Can others write chapters publicly?
Can others remix the world?
Can others build commercial tools from Flower runtime?
Can others train AI on the text?
Should attribution be required?
Should commercial use require permission?
```

---

## Main sentence

> **Before inviting the world to build, decide what they may copy, remix, sell, translate and train on.**
