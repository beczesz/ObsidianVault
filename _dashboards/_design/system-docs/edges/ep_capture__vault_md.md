---
from: ep_capture
to: vault_md
protocol: file write
direction: server → filesystem
payload: markdown append
label: Alfred inbox
id: 99251b3c-4d83-4901-ba0d-ff1973b34f59
index_schema_version: 1
---

## Kapcsolat

Az `/api/alfred/capture` endpoint a vault `inbox.md` fájljába ír append
művelettel. Ez az egyetlen REST endpoint, amely direktben ír a vault
markdown-ba — minden más végpont read-only.

## File write logika

```js
const INBOX_PATH = path.join(VAULT_ROOT,
  '02_Areas/Personal Growth/Alfred/inbox.md');

async function appendToInbox(message) {
  const timestamp = new Date().toISOString().slice(0, 19).replace('T', ' ');
  const line = `\n- ${timestamp} ${message}`;
  await fs.appendFile(INBOX_PATH, line, 'utf8');
}
```

## Biztonsági korlátok

- **Path hardcoded** — nincs path traversal lehetőség
- **Append-only** — nem olvas, nem töröl, nem módosít meglévő sorokat
- **Localhost-only** — a dash-server nem fogad külső hálózati kéréseket
- **Max message length** — 2000 karakter (szerver-oldalon truncate)

## Eredmény a vaultban

```markdown
<!-- inbox.md részlet -->
- 2026-05-30 14:32:00 Megnézni a Deák havi számokat
- 2026-05-30 15:11:23 [UNPROCESSED] Holnap reggel 9-re call
```

A `[UNPROCESSED]` tag az AI parse nélküli capture_fallback útvonalon
keletkező soroknál jelenik meg — jelzi Alfred-nek, hogy feldolgozást igényel.
