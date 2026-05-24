---
schema: sage.learnings.index.v1
generated_at: null
counts:
  active: 0
  proposed: 0
  retired: 0
description: Sage meta-kogníciós learnings élő indexe — user-reviewable, retirable tanulságok a saját munkáról. Heti curate frissíti. Olvasandó mielőtt Sage új learning-et javasol.
id: 429da7ab-bcf9-4d7e-b1f8-2a24df0892f2
index_schema_version: 1
---

# Sage — Learnings Index

Sage meta-kognicíós tanulságainak élő indexe. Heti curate frissíti.

## Active (0)

*Üres — Sage még nem futott, nincsenek confirmed learningek.*

## Proposed (0)

*Üres — nincsenek pending javaslatok user-review-ra.*

## Retired (0)

*Üres — még semmit sem archiváltunk.*

---

## Hogyan él egy learning

```
proposed  ──/sage-learning-accept──>  active  ──unused 4 weeks──>  retired
   │                                    │
   │                                    └──contradicts new──>  retired (auto)
   │
   └──/sage-learning-reject──>  retired (with reason)
```

## Learning fájlok helye

- Active: [`active/`](active/) — bekerül a következő Sage-futás promptjába
- Proposed: [`proposals/`](proposals/) — user-review vár
- Retired: [`retired/`](retired/) — archive, audit miatt megőrizve

## Cap

- Max **15 active learning** loadolódik egyidejűleg
- Max **2000 token** preamble méret
- Sorrend: `confidence DESC, last_applied_at DESC`
