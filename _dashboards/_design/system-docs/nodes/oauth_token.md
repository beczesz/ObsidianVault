---
id: oauth_token
title: OAuth token
layer: processing
purpose: |
  A Claude Code CLI OAuth hitelesítési tokenje. A `claude` subprocess
  az `~/.claude/` könyvtárból olvassa a tokent futáskor. A token
  a felhasználó Claude Code subscription-jához kötött,
  nem az Anthropic API key rendszerhez.
depends_on: []
status_endpoint: /health (component: oauth_token)
index_schema_version: 1
---

## Miért létezik

Az OAuth token az a hitelesítési alap, amely lehetővé teszi, hogy a
dash-server a felhasználó subscription-ja terhére futtasson Claude
subprocess-eket API kulcs expozíció nélkül. A token a `claude login`
paranccsal szerezhető meg, és az `~/.claude/` könyvtárban tárolódik.

## Token megújítás

Az OAuth token lejár, és automatikusan megújul, ha a `claude` CLI elérhető
és az internet connection aktív. Ha lejár és nincs internet, a /health
`warn` vagy `gap` státuszt mutat a `claude_cli` komponensen.

## Hibamód és javítás

Ha a token invalid:
```bash
claude setup-token
# másold a tokent
# ~/.bdos/anthropic.env fájlba:
# CLAUDE_CODE_OAUTH_TOKEN=<token>
launchctl kickstart -k gui/$(id -u)/com.bdos.dash-server
```

## Biztonsági megjegyzés

A token csak a helyi gépen él, soha nem kerül a vaultba, nem szinkronizálódik
Google Drive-on. A `.gitignore` és `.bdos/` mappa kizárja a sync-ből.
