---
title: "_dashboards"
date: 2026-05-20
author: Becze Szabolcs
status: active
description: "Code repository for Ideas Vault dashboards, including the launcher, individual dashboard HTML files, Node server, and startup scripts for Windows, macOS, and Linux. Developers use this to run and modify real-time markdown-driven dashboards locally."
description_source: auto
description_hash: 5d31b72f597f28fb
id: f72cd7cc-27e0-48b8-9525-b9148a2baf28
index_schema_version: 1
bdos_index: true
---
# _dashboards

All Ideas Vault dashboard code lives here: the launcher, the individual dashboards, the server, and the run scripts. **Markdown content stays in the Areas** (`02_Areas/...`); this folder is code only.

```
_dashboards/
├── index.html          launcher (tree of Areas), served at /
├── sales.html          CPS Sales pipeline board
├── partnerships.html   CPS Partnerships health board
├── README.md           this file
└── _tools/
    ├── dash-server.mjs  Node static server + file-watcher push (SSE)
    ├── start.ps1        Windows (PowerShell)
    ├── start.bat        Windows (double-click)
    └── start.sh         macOS / Linux
```

## Run it

You need Node installed (`node --version`). No `npm install` required, the server is pure Node.

**Windows**
- Double-click `_tools/start.bat`, or
- In PowerShell: `_dashboards\_tools\start.ps1`

**macOS / Linux**
- `bash _dashboards/_tools/start.sh` (or `chmod +x` it once and run `./start.sh`)

**Any platform, manually**
- `node _dashboards/_tools/dash-server.mjs` (from anywhere; the server finds the vault root from its own location)
- Override the port: `PORT=8000 node _dashboards/_tools/dash-server.mjs`

Then open: **http://localhost:4321/** (default port). The root redirects to the launcher.

## Auto-start at login (macOS, 2026-05-29)

To run the server automatically (start at login, self-restart on crash) instead of a manual terminal:

- Install: `bash _dashboards/_tools/install-autostart.sh` (creates a per-user LaunchAgent `com.bdos.dash-server`, loads it, stops any manual instance).
- Remove: `bash _dashboards/_tools/uninstall-autostart.sh`.
- Once installed, do NOT run `start.sh` manually (port conflict); launchd owns the server. Logs: `~/Library/Logs/bdos-dash-server.{out,err}.log`.

**Alfred Sonnet tier under launchd (use your subscription, no API cost):** a background agent cannot use your interactive Claude subscription from the login keychain (it 401s headless), so give it a long-lived **subscription** token:

1. In your Terminal: `claude setup-token` (requires your Claude subscription; prints a token).
2. Paste it into `~/.bdos/anthropic.env` (chmod 600; the wrapper `server-launch.sh` sources it): uncomment `CLAUDE_CODE_OAUTH_TOKEN=` and add the token.
3. Reload: `launchctl kickstart -k gui/$(id -u)/com.bdos.dash-server`.

This uses your subscription, not metered API billing. The Alfred dashboard masthead pill shows the live tier (Sonnet / Haiku / capture-only). Without a token the agent still serves dashboards + capture-only; the Sonnet tier also works automatically when the server is launched from a Terminal (keychain reachable there). An `ANTHROPIC_API_KEY` is supported as an optional metered alternative.

## Auto-start at logon (Windows)

Same idea via Task Scheduler (start at logon + 5-minute self-restart supervisor):

- Install: `powershell -ExecutionPolicy Bypass -File _dashboards\_tools\install-autostart.ps1`
- Remove: `powershell -ExecutionPolicy Bypass -File _dashboards\_tools\uninstall-autostart.ps1`

It registers a task **"BDOS Dashboard Server"** running `server-launch.ps1` hidden; the wrapper exits if port 4321 is already listening (single instance) and loads `%USERPROFILE%\.bdos\anthropic.env`.

**Subscription token (no API cost), same as macOS:** run `claude setup-token`, then put `CLAUDE_CODE_OAUTH_TOKEN=<token>` into `%USERPROFILE%\.bdos\anthropic.env` (the install script seeds a commented template), then `Start-ScheduledTask -TaskName "BDOS Dashboard Server"`. The token is account-level, so the macOS token usually works on Windows too; regenerate with `claude setup-token` if needed.

> Scheduler single-owner rule (indexing daemon) is unchanged: the Mac owns the cron scheduler. The dashboard server runs independently on each machine and is safe to auto-start on both.

## What the server does

- Serves the whole vault root over HTTP, so dashboards fetch markdown via absolute paths like `/02_Areas/Sonrisa/CPS/Sales/Pipeline.md`.
- Watches `02_Areas/**/*.md` and pushes a Server-Sent Event the instant a file changes. Dashboards refresh sub-second, no polling lag.
- Each dashboard keeps an 8s poll timer as a fallback (relaxes to 30s while the live push is connected). So a dashboard still works if served by a plain static server (`npx serve .`), just without the instant push.

## Conventions

See `02_Areas/Sonrisa/CPS/Sales/DASHBOARD_CONTRACT.md` and the capability doc `00_Prompts/BDOS/capabilities/vault-dashboards/CLAUDE.md`. In short: edit markdown, not HTML. The HTML is a renderer. Bump a dashboard's version when you change its code.
