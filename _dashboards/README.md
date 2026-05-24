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

## What the server does

- Serves the whole vault root over HTTP, so dashboards fetch markdown via absolute paths like `/02_Areas/Sonrisa/CPS/Sales/Pipeline.md`.
- Watches `02_Areas/**/*.md` and pushes a Server-Sent Event the instant a file changes. Dashboards refresh sub-second, no polling lag.
- Each dashboard keeps an 8s poll timer as a fallback (relaxes to 30s while the live push is connected). So a dashboard still works if served by a plain static server (`npx serve .`), just without the instant push.

## Conventions

See `02_Areas/Sonrisa/CPS/Sales/DASHBOARD_CONTRACT.md` and the capability doc `00_Prompts/BDOS/capabilities/vault-dashboards/CLAUDE.md`. In short: edit markdown, not HTML. The HTML is a renderer. Bump a dashboard's version when you change its code.
