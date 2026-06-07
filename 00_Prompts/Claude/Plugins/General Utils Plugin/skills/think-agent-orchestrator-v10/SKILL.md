---
name: think-agent-orchestrator-v10
description: >
  v0.10 — Playwright-based browser AI driver for ChatGPT, Claude.ai,
  Perplexity, Copilot, Gemini. Uses a dedicated automation Chrome profile
  at ~/.think-engine/state/chrome-profile/ (Chrome 137+ blocks remote
  debugging against the default profile, so we run alongside the user's
  normal Chrome instead of inside it). One-time browser login per service,
  then it persists. Long-running Chrome stays open across calls via CDP
  attach. Generic provider system: add a new browser AI by dropping one
  .mjs file. Runtime lives at ~/.think-engine/ (OUTSIDE the vault) and is
  bootstrapped on first use from the runtime-source/ folder shipped
  alongside this SKILL. Cross-platform (Windows + macOS + Linux). Activate
  when the user wants to talk to ChatGPT / Claude / Perplexity / Copilot /
  Gemini through the browser (for conversation history, Custom GPTs,
  Projects, voice context import, enterprise data) rather than via API.
  For API-only multi-AI orchestration use v0.9 instead — v0.10 focuses on
  making the browser path reliable. v0.9 may shell out to v0.10 for the
  browser leg of a hybrid round.
id: 8a1c3f7e-4b29-4d5a-9e63-2f8c7b6a4d11
index_schema_version: 1
---

# Think Agent Orchestrator v0.10

Playwright-based browser AI driver. The vault holds this SKILL.md plus a `runtime-source/` folder; everything else lives at `~/.think-engine/` on the user's machine.

> **v0.10.1 (2026-05-29) — reliability fixes folded back from a live BDOS research run:**
> - **Anti-Cloudflare stealth** in `lib/browser.mjs`: persistent Chrome now launches with `chromiumSandbox: true`, `ignoreDefaultArgs: ['--enable-automation','--no-sandbox']`, `--disable-blink-features=AutomationControlled`, plus a `navigator.webdriver` init-script shim. Without this, Cloudflare Turnstile loops the "verify you are human" check forever and login never sticks.
> - **Completion-detection fallback** in `chatgpt.mjs` and `gemini.mjs`: `waitForCompletion` no longer relies solely on the stop-button going hidden (its selector has drifted, causing 10-min false timeouts). It now also returns when the last answer's text stops growing for ~6s.
> - **Cookie-consent dismissal** in `gemini.mjs`: dismisses the Google CMP overlay (which intercepts composer clicks) before submitting.
> - Note: `start-browser.mjs` / `stop-browser.mjs` / `login-helper.mjs` referenced below are NOT shipped in this runtime yet; the orchestrator self-launches a persistent context instead, and login is a one-time manual step in that headed window. Concurrent same-profile runs are not supported (single profile lock) — run providers sequentially or implement the long-running browser helpers.

**Key design points:**
- **Runtime is at `~/.think-engine/`** — node_modules, profile, traces. NOT in the vault.
- **Dedicated automation Chrome profile** — at `~/.think-engine/state/chrome-profile/`. Chrome 137+ refuses `--remote-debugging-port` and `--remote-debugging-pipe` when `--user-data-dir` points at the OS default profile path ("DevTools remote debugging requires a non-default data directory"), so we run automation in a separate profile that lives alongside the user's normal Chrome. One-time manual login per service.
- **Long-running Chrome** — start once via `start-browser.mjs`, attach via CDP for many orchestrator calls, stop when done. CDP attach is ~5× faster than launching Chrome per call.
- **Generic provider system** — one `.mjs` per AI; the orchestrator is provider-agnostic.

---

## When to use v0.10 vs v0.9

| Need | Use |
|---|---|
| Continue an existing ChatGPT conversation (history, Custom GPT, Project) | **v0.10** |
| Voice mode context import | **v0.10** |
| Enterprise Copilot M365 | **v0.10** |
| API-only multi-AI orchestration (no browser needed) | v0.9 (or v0.10 with API providers added later) |
| Fastest possible: pure API parallel calls | v0.9 |

v0.10 is a **transport upgrade**, not a replacement of v0.9's orchestration model. v0.9 can shell out to v0.10 for the browser leg of a hybrid round (see Part 8).

---

## Part 1 — Pre-flight check (every invocation)

Before any provider call, run a 3-line check (cross-platform — `~` expands to the OS home dir):

```bash
test -f ~/.think-engine/version || { echo "SETUP_NEEDED"; exit 2; }
test -d ~/.think-engine/node_modules/playwright || { echo "SETUP_NEEDED"; exit 2; }
```

PowerShell equivalent:
```powershell
Test-Path "$env:USERPROFILE\.think-engine\version"
Test-Path "$env:USERPROFILE\.think-engine\node_modules\playwright"
```

If `SETUP_NEEDED`, run the setup flow (Part 2) before anything else.

Healthcheck (cheap, runs without launching a browser):
```bash
node ~/.think-engine/runtime/orchestrator.mjs --healthcheck
```

Expected JSON output:
```json
{ "ok": true, "version": "0.10.0", "providers": ["chatgpt","claude","copilot","gemini","perplexity"], "node": "v24...", "platform": "win32|darwin|linux", "cdp_recovery": "..." }
```

---

## Part 2 — First-time setup (one-shot per machine)

If pre-flight returns `SETUP_NEEDED`, present this to the user:

> Think Engine v0.10 isn't installed yet. It needs to install Playwright at `~/.think-engine/` (~50 MB, outside your vault). One-time, ~2 minutes. Proceed? [Y/n]

On yes, **copy the runtime source from the vault to `~/.think-engine/`, then install deps:**

```bash
# Linux / macOS
mkdir -p ~/.think-engine
cp -R "<vault>/00_Prompts/Claude/Plugins/General Utils Plugin/skills/think-agent-orchestrator-v10/runtime-source/." ~/.think-engine/
bash ~/.think-engine/setup.sh
```

```powershell
# Windows
$src = "<vault>\00_Prompts\Claude\Plugins\General Utils Plugin\skills\think-agent-orchestrator-v10\runtime-source"
Copy-Item -Recurse -Force "$src\*" "$env:USERPROFILE\.think-engine\"
& "$env:USERPROFILE\.think-engine\setup.ps1"
```

`setup.sh` / `setup.ps1` runs `npm install` with `PLAYWRIGHT_SKIP_BROWSER_DOWNLOAD=1` (we use the user's system Chrome, not bundled Chromium), writes a version stamp, and runs `--healthcheck`.

Replace `<vault>` with the actual vault path. On the canonical machine that's `C:\Users\EvoComputers\Obsidian\ideas-vault` (Windows) or `~/Obsidian/ideas-vault` (macOS). The skill folder is the same relative path everywhere.

---

## Part 3 — Automation Chrome profile

**Why a dedicated profile?** Chrome 137+ (mid-2025) refuses remote debugging when `--user-data-dir` is the platform's default profile path. Verified empirically on Chrome 148:

```
DevTools remote debugging requires a non-default data directory.
Specify this using --user-data-dir.
```

This affects both `--remote-debugging-port=9222` (CDP attach) and `--remote-debugging-pipe` (what Playwright's `launchPersistentContext` uses internally). It's a Google malware mitigation, no flag opts out.

So Think Engine creates and uses **`~/.think-engine/state/chrome-profile/`**. It's a regular Chrome user-data-dir: cookies, localStorage, extensions, IndexedDB, all persist between runs. The user's normal Chrome is untouched.

**Cookie/login carry-over:** Chrome 127+ uses App-Bound Encryption that ties cookie decryption to the user-data-dir path, so we cannot copy cookies from the default profile and have them decrypt elsewhere. The runtime best-effort copies non-cookie state (Preferences, Local State, IndexedDB) on first launch, then the user logs into each service once. Logins persist from then on.

### Starting / stopping the long-running Chrome

```bash
# Start (no-op if already up)
node ~/.think-engine/runtime/start-browser.mjs

# Stop gracefully
node ~/.think-engine/runtime/stop-browser.mjs
```

While `start-browser.mjs` is running's session, orchestrator calls attach via CDP (~0.3s overhead). When Chrome isn't already up, the orchestrator falls back to launching its own persistent context (~5s overhead per call, closes after). Both work; the former is what you want for interactive use.

### One-time login per provider

```bash
node ~/.think-engine/runtime/login-helper.mjs --provider chatgpt
node ~/.think-engine/runtime/login-helper.mjs --provider claude
node ~/.think-engine/runtime/login-helper.mjs --provider perplexity
node ~/.think-engine/runtime/login-helper.mjs --provider copilot
node ~/.think-engine/runtime/login-helper.mjs --provider gemini
```

The helper opens (or reuses) a Chrome window on the provider's URL, polls every 2s for the provider's `loginCheck` to return true (up to 10 min default), and closes the connection cleanly when login is detected. After this, the orchestrator can use `--mode continue` to reuse the authenticated session indefinitely.

---

## Part 4 — Invocation contract

The runtime is invoked via Bash / PowerShell. Single entry point:

```bash
node ~/.think-engine/runtime/orchestrator.mjs \
  --provider <name> \
  --mode <continue|new> \
  --prompt-file <path> \
  --output <path> \
  [--timeout <ms>]
```

**Args:**
- `--provider` — one of: `chatgpt`, `claude`, `perplexity`, `copilot`, `gemini` (extensible — see Part 6)
- `--mode continue` — reuse an existing tab matching the provider's URL pattern; if none, open a new tab. Use this for ChatGPT history.
- `--mode new` — always open a new tab. Use for a fresh conversation.
- `--prompt-file` — path to a file containing the prompt (preferred for long/multi-line)
- `--prompt` — literal prompt text (avoid for anything non-trivial — shell escaping)
- `--output` — write JSON result here. If omitted, JSON goes to stdout.
- `--timeout` — milliseconds to wait for the AI's response (default 180000 = 3 min)

**Convenience helpers:**
- `--list-providers` — print available providers
- `--healthcheck` — verify runtime + Playwright + providers (no browser launched)

**Output JSON shape (success):**
```json
{
  "ok": true,
  "provider": "chatgpt",
  "mode": "cdp" | "persistent",
  "page_reused": true,
  "elapsed_ms": 6500,
  "response": "...",
  "page_url": "https://chatgpt.com/c/abc-123..."
}
```

**Output JSON shape (failure):**
```json
{
  "ok": false,
  "provider": "chatgpt",
  "mode": "cdp" | "persistent",
  "error": "Timed out after 120000ms waiting for ChatGPT to finish responding",
  "elapsed_ms": 120500
}
```

Exit codes:
- `0` — success
- `1` — provider failure (timeout, login expired, selector miss). Trace ZIP saved to `~/.think-engine/state/traces/` when running in persistent mode.
- `2` — `SETUP_NEEDED`
- `3` — bad invocation (missing/invalid args)

---

## Part 5 — Typical orchestration loop

When the user wants to talk to ChatGPT:

1. **Pre-flight** (Part 1). If `SETUP_NEEDED`, run Part 2.
2. **Ensure browser is running:** `node ~/.think-engine/runtime/start-browser.mjs` (no-op if already up).
3. **Write the prompt** to a temp file (avoids shell-escaping issues):
   ```bash
   printf '%s' "$PROMPT" > /tmp/think-prompt.txt
   ```
   Windows:
   ```powershell
   Set-Content -Path "$env:TEMP\think-prompt.txt" -Value $prompt -Encoding utf8 -NoNewline
   ```
4. **Run orchestrator:**
   ```bash
   node ~/.think-engine/runtime/orchestrator.mjs \
     --provider chatgpt --mode continue \
     --prompt-file /tmp/think-prompt.txt \
     --output /tmp/think-response.json
   ```
5. **Parse the result file.** If `ok=false`, show `.error` and the trace path (only present for persistent mode) to the user.
6. **Persist to the brainstorm state file** (per v0.9 Part 7 step 5 when used in a hybrid round).

For multi-AI orchestration, run multiple orchestrator calls in parallel — each in its own Bash / PowerShell tool-use in the same assistant turn. Each call gets its own Chrome tab (when attached via CDP, tabs are independent within the long-running browser).

---

## Part 6 — Adding a new provider

Each provider is a single `.mjs` in `~/.think-engine/runtime/providers/`. Copy `_template.mjs` and fill in:

```js
export default {
  name: 'my-provider',
  urlPatterns: [/myai\.example\.com/],   // matches existing tabs in 'continue' mode
  startUrl: 'https://myai.example.com/',
  async loginCheck(page) { ... },         // optional, returns boolean
  async submitPrompt(page, prompt) { ... },
  async waitForCompletion(page, opts) { ... },
  async extractResponse(page) { ... },
};
```

Then mirror the file into `<vault>/.../v10/runtime-source/runtime/providers/` so it ships with the skill.

Verify with: `node ~/.think-engine/runtime/orchestrator.mjs --list-providers`.

**Selector tips:** prefer ARIA roles and `data-testid` attributes over CSS classes (which get hashed and break). For SPA login detection, give `loginCheck` a generous deadline (~20-25s) — `domcontentloaded` fires well before the composer renders. See `providers/chatgpt.mjs` for a reference that handles streaming + Cloudflare interstitials.

---

## Part 7 — Failure modes & recovery

| Failure | Detection | Recovery |
|---|---|---|
| `SETUP_NEEDED` | exit code 2, healthcheck reports missing | Run Part 2 setup flow |
| `DevTools remote debugging requires a non-default data directory` | persistent-context launch fails with this stderr | Means `THINK_ENGINE_DIR` was overridden to point at the user's default Chrome profile. Unset it and retry — runtime should use `~/.think-engine/state/chrome-profile/` |
| Login expired | `provider.loginCheck` returns false | Run `node ~/.think-engine/runtime/login-helper.mjs --provider <name>`, user logs in, retry |
| Automation profile locked | "ProcessSingleton" / "already in use" error | A previous Think Engine Chrome is still up. `stop-browser.mjs` to close it, or wait for it to close on its own, then retry |
| Selector miss | Playwright timeout exception in submit/wait | Trace ZIP saved to `~/.think-engine/state/traces/`. Inspect with `npx playwright show-trace <zip>` and update selectors in the provider file |
| Stop-button never appears (instant response) | swallowed by 5s catch | Normal path; we then check for stop-button hidden state anyway |
| Stop-button never disappears (model stuck) | 120s+ timeout | Returns whatever `extractResponse` can pull + `error: timed out` |
| Multiple tabs match provider | first match wins | Close extras, or use `--mode new` to force new tab |
| Chrome 148+ removes `--remote-debugging-pipe` for non-default profiles too | `launchPersistentContext` fails again | Future risk; mitigation is to use Playwright's bundled Chromium via `executablePath: undefined` (different binary, no policy) |

---

## Part 8 — Coexistence with v0.9

v0.10 does NOT touch v0.9. The v0.9 SKILL.md remains the orchestrator for:
- API-only multi-AI roundtables
- Brainstorm state file ownership
- Per-team-member transport routing

When a session needs both API providers AND browser providers, v0.9 calls API providers itself and shells out to v0.10's orchestrator for the browser ones:

```bash
# Inside a v0.9 orchestration round, for the browser leg:
node ~/.think-engine/runtime/orchestrator.mjs --provider chatgpt --mode continue \
     --prompt-file /tmp/p.txt --output /tmp/r.json
```

The output JSON merges into the v0.9 round's findings collection naturally (same `response` text field). The Chrome MCP transport in v0.9 is now deprecated — anywhere v0.9 says "use Chrome MCP," replace with a `v10/orchestrator.mjs` shellout.

---

## Part 9 — Out of scope (v0.11+)

- Vision-fallback for catastrophic selector breakage (browser-use style)
- Parallel multi-tab orchestration of the same provider
- Built-in retry-on-selector-miss with auto-healing
- Headless mode (we always run headed so the user can see + take over)
- Cookie migration from the default profile (would need a DPAPI/App-Bound-Encryption workaround per platform)

The principle: **make the common path bulletproof first; add cleverness only when justified by repeat failures.**

---

## Final invocation example

```bash
# 1. Make sure browser is running (no-op if already up)
node ~/.think-engine/runtime/start-browser.mjs

# 2. Write prompt
printf 'Summarize the BDOS positioning paragraph from yesterday into 3 bullets.' \
  > /tmp/p.txt

# 3. Run
node ~/.think-engine/runtime/orchestrator.mjs \
  --provider chatgpt --mode continue \
  --prompt-file /tmp/p.txt --output /tmp/r.json

# 4. Read
cat /tmp/r.json
```

That's the whole contract.
