---
title: Sage Scheduling — macOS launchd Setup
date: 2026-05-24
status: ready-for-user-install
description: Sage automatikus ütemezés beállítása macOS launchd segítségével. Két plist fájl (daily 06:00 harvest + hétfő 06:05 curate) — a felhasználónak egyszer kell betöltenie, utána automatikusan futnak.
id: 0957674a-6c84-4cd6-a93f-72a9f9bfdc94
index_schema_version: 1
---

# Sage Scheduling — Setup Instructions

> A két plist fájl készen áll. **A felhasználónak kell egyszer betöltenie** — utána automatikusan futnak.

## Mit fog tenni a két cron

| Plist | Mikor | Mit |
|---|---|---|
| `com.becze.sage-daily-harvest.plist` | minden nap 06:00 (Europe/Bucharest) | `/sage-harvest` futtatás |
| `com.becze.sage-weekly-curate.plist` | hétfő 06:05 | `/sage-curate` futtatás |

A Sage `chrome MCP`-vel olvassa a "Referencia chat"-et, és az `Ideas/` alá ír.

## Setup — 3 parancs

### 1. Helyezd el a plist fájlokat
```bash
cp "/Users/becze-mac/My Drive (beczesz.szabolcs@gmail.com)/0. Ideas Vault/00_Prompts/BDOS/agents/sage/scheduling/com.becze.sage-daily-harvest.plist" ~/Library/LaunchAgents/
cp "/Users/becze-mac/My Drive (beczesz.szabolcs@gmail.com)/0. Ideas Vault/00_Prompts/BDOS/agents/sage/scheduling/com.becze.sage-weekly-curate.plist" ~/Library/LaunchAgents/
```

### 2. Betöltés a launchd-be
```bash
launchctl load ~/Library/LaunchAgents/com.becze.sage-daily-harvest.plist
launchctl load ~/Library/LaunchAgents/com.becze.sage-weekly-curate.plist
```

### 3. Verifikáció
```bash
launchctl list | grep sage
```

Várt output:
```
-	0	com.becze.sage-daily-harvest
-	0	com.becze.sage-weekly-curate
```

## Előfeltételek

1. **Claude Code CLI telepítve:**
   ```bash
   which claude
   ```
   Várt output: `/usr/local/bin/claude` vagy `/opt/homebrew/bin/claude`.
   Ha más a path → a plist `ProgramArguments` szekciójában javítsd.

2. **Authentikáció érvényes:** futtass egy `claude --print "ping"` parancsot manuálisan, ellenőrizd hogy működik (nem kéri újra a login-t).

3. **Chrome MCP elérhető:** ha a Sage `/sage-harvest` futna headless mód-ban, akkor a Chrome `claude-in-chrome` extension a "work" browseren elérhető legyen. Lokálisan futó cron-ban a felhasználó session-jében ez működik.

4. **Log mappa létezik:**
   ```bash
   mkdir -p ~/Library/Logs
   ```

## Eltávolítás (ha nem kell)

```bash
launchctl unload ~/Library/LaunchAgents/com.becze.sage-daily-harvest.plist
launchctl unload ~/Library/LaunchAgents/com.becze.sage-weekly-curate.plist
rm ~/Library/LaunchAgents/com.becze.sage-daily-harvest.plist
rm ~/Library/LaunchAgents/com.becze.sage-weekly-curate.plist
```

## Hibakeresés

- **Cron nem fut:**
  - `tail -f ~/Library/Logs/sage-daily-harvest-stderr.log` — nézd a hibákat
  - Mac-en a launchd nem indítja el az ütemezett feladatot, ha a gép alszik. Reggeli ébredés után pótolja-e a megspórolt futást? Nem mindig — ezért a `RunAtLoad: false` a default, és kézzel is lehet futtatni manuálisan a `/sage-harvest` slash command-dal.
- **Chrome MCP nem érhető el a cron-ból:**
  - A Chrome extension a felhasználó interaktív session-jéhez kötött. Ha a cron nem-interaktív shell-ben fut, Chrome MCP nem indul el. Megoldás: scheduled time-kor a felhasználó legyen bejelentkezve a Mac-jébe (alvó állapotban is OK, ébredés után fut).

## Time zone megjegyzés

A launchd `StartCalendarInterval` **lokális idő** (Europe/Bucharest). Tehát 06:00 lokál = pontosan reggel 6.

## Status / next steps

- [ ] **User:** futtassa le a 3 setup parancsot
- [ ] **User:** ellenőrizze `launchctl list | grep sage`-gel
- [ ] **Sage smoke test először** — futtassa kézzel `/sage-harvest`-et hogy validálva legyen a pipeline mielőtt cron is rányom
- [ ] Első automatikus futás: másnap reggel 06:00
