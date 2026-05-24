---
schema: sage.chatgptsnapshot.v1
captured_at: null
projects: []
id: be73fd42-7b6b-4281-be70-2f19970f0f19
index_schema_version: 1
---

# Sage — ChatGPT Snapshot

A legutóbb látott ChatGPT projekt + chat sorrend. Sage minden harvest futás elején lemásolja az aktuális állapotot, hogy:

1. Detektálja az új chatek megjelenését (esetleg új gondolat-forrás)
2. A dashboard megmutathassa, hogyan változott a ChatGPT-tarballom heti szinten
3. Ha a user "az új chat"-et említi referenciában, Sage tudja azonosítani

**Státusz: üres** — első futás után töltődik fel.

## Várt schema (futás után)

```yaml
captured_at: 2026-05-25T06:00:42+02:00
projects:
  - name: "Személyes gondolatok"
    chats:
      - title: "ExarLabs - AI alapú operációs rendszer"
        last_message_ts: 2026-05-24T22:14:00+02:00
        url: https://chatgpt.com/g/g-p-.../c/6a106bcf-...
      - title: "Reggeli rutinok"
        last_message_ts: 2026-05-23T07:11:00+02:00
        url: https://chatgpt.com/g/g-p-.../c/...
  - name: "ExarLabs"
    chats: [...]
```
