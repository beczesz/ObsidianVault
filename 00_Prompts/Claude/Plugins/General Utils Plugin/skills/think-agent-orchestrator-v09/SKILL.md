---
name: think-agent-orchestrator-v09
description: >
  Semi-autonomous multi-AI orchestration engine with API-first hybrid mode.
  Claude coordinates a configurable team of AI tools either via direct API
  calls (Anthropic Claude, OpenAI GPT/o-series, Perplexity Sonar) for 5-10x
  speed over browser automation, or via Chrome MCP for AIs without API keys,
  voice-mode ChatGPT context extraction, Perplexity Pro browser sessions,
  and Microsoft 365 Copilot. The user assembles the thinking team at session
  start, choosing members, roles, and per-member transport (api or browser).
  Includes guided API-key onboarding when a configured provider has no key
  in the shell environment. Maintains persistent brainstorming state files
  with structured findings JSON per AI per round. Activate when the user
  mentions "think engine", "orchestrator", "brainstorm", "multi-AI",
  "gondolkodj", "jardd koorbe", "kutasd ki", "piackutatas", "kockazatelemzes",
  "copilot", "gemini", or any complex analytical task that benefits from
  multi-AI collaboration. Also activate when any AI platform URL is provided.
id: cb9a554d-2467-4197-8fd3-fe748696c978
index_schema_version: 1
---

# Think Agent Orchestrator v0.9

Semi-autonomous multi-AI orchestration engine with **API-first hybrid mode**.

**v0.9 changelog (from v0.8):**
- **Hybrid transport** — every team member has a `transport` field: `api` (curl-based direct call) or `browser` (Chrome MCP). Set per member at team assembly.
- **API provider registry** — Anthropic, OpenAI, Perplexity Sonar pre-wired with curl templates, env-var conventions, and Response Contract handling.
- **Unified Adapter Pattern** — both transports return the same `findings` JSON shape; synthesis is transport-agnostic.
- **API key onboarding tutorial** (NEW) — when a configured API provider has no env-var key, the skill offers a guided setup flow (console URL → create key → save to `~/.zshenv` → verify) before falling back to browser mode.
- **Lenient Response Contract parser** — accepts ```findings and ```json blocks, both the canonical `{summary, answers:[...]}` shape and flat `{Q1, Q2, ...}` shape (GPT-5 tends to emit the latter).
- **Provider presets** — `Premium`, `Fast`, `Solo Claude`, `Browser-Only` quick-start configurations.
- **Reasoning model handling** — for OpenAI o-series and GPT-5, `max_completion_tokens` is set to ≥4000 to leave room after reasoning_tokens consumption.

---

## Part 1: Roles & Responsibilities

(Unchanged from v0.8. Human is decision authority; AI team is dynamically assigned roles; Claude orchestrates and executes.)

---

## Part 2: Core Principles

1. **Semi-Autonomous Orchestration**
2. **Local-First Reasoning**
3. **Persistent Cognition**
4. **Source Trust Hierarchy** — Human > Local files > AI team > Claude inference
5. **Flow over Friction**
6. **Open Toolchain**
7. **Throughput Discipline** (v0.8) — fat prompts, structured responses, parallel activation
8. **Transport Pragmatism (v0.9 NEW)** — use the fastest transport available for each AI: API where a key exists and the task fits, browser where the user wants account state, voice mode, enterprise data, or has no API key.
9. **State File is Canonical Memory (v0.9 NEW)** — see Part 2.5. The brainstorm state file is the durable brain; AIs are interchangeable thinking surfaces. AI-side memory (Chrome MCP threads) is bonus, not source-of-truth.

---

## Part 2.5: Transport Decision Principle (NEW in v0.9)

### The Foundational Insight

> **The brainstorm state file is the durable brain. AIs are thinking surfaces.**

If you accept this, the "stateful vs stateless" distinction between Chrome MCP and API becomes secondary — because the durable context lives in the state file either way, regardless of which transport delivered the thinking.

### Why Chrome MCP "memory" is not a free advantage

API mode is stateless: every call starts from zero, so you MUST inject relevant context from the state file into every prompt.

Chrome MCP mode is stateful: the AI carries its own conversational memory in the user's account. This sounds like an advantage but introduces **drift risk** — the AI builds up understanding that the state file does not capture, and when you later switch to API mode (or a different browser AI), that understanding is lost or contradicts the state file.

**Therefore:** Chrome MCP memory is useful *only* when continuously synchronized back to the state file. Treat it as cache, not as truth.

### The Default Principle

**Default: API. Use Chrome MCP only when it adds something the API cannot.**

The "something the API cannot" reduces to exactly four cases:

| # | Value Chrome MCP adds | Examples |
|---|----------------------|----------|
| 1 | **Voice mode** | ChatGPT voice conversations (no API equivalent) |
| 2 | **Account-side data** | Custom GPT, ChatGPT Projects, saved memories; Copilot M365 enterprise access; Perplexity Spaces |
| 3 | **No API alternative** | Copilot, account-bound Gemini |
| 4 | **Live human interaction** | User is actively chatting with the AI and wants to extract that conversation |

If NONE of these apply -> use API. It is faster, structured, and more reliable.

### Decision Tree

```
For each sub-task / team role assignment:

├─ Is the user in voice mode with ChatGPT?       -> Chrome MCP (ChatGPT)
├─ Does the task need account-side data?         -> Chrome MCP
│   (Copilot M365, Custom GPT, Perplexity Spaces)
├─ Does the task need web search with citations? -> Perplexity (Chrome MCP for now;
│                                                   Sonar API later if user adds key)
├─ Premium strategic thinking?                   -> Opus 4.7 (API)
├─ Sharp validator / second-opinion?             -> GPT-5 (API)
├─ Fast general thinking / batch work?           -> Sonnet 4.5 (API)
└─ Continuing a long-running AI thread where
    the AI "already knows" the context?         -> Check state file FIRST.
                                                   If state file has it -> API + injection.
                                                   If not -> Chrome MCP, then SYNC BACK.
```

### The Drift Rule

When using Chrome MCP, **at the end of every session, sync back to the state file** any insight the AI produced. Otherwise the AI's account-side memory becomes a hidden parallel knowledge base that no other AI can see.

Concrete protocol after a Chrome MCP round:
1. Extract the findings JSON (or the raw response if no contract)
2. Add to the state file's Raw Notes
3. Update Key Insights section if anything is durable
4. Note the conversation URL so future sessions can re-open it if needed

### The Memory Illusion Warning

A subtle failure mode: if you always brainstorm via the same ChatGPT browser thread, you may start to feel "ChatGPT knows me" — but it only knows that one conversation window. Open a new chat or switch to API and that understanding evaporates. **The state file is what knows you. Build the durable brain there.**

### Practical Default Team (revised in light of this principle)

```
Strategist  -> Opus 4.7 (API)        — stateless is fine; state file feeds context
Validator   -> GPT-5 (API)           — stateless is fine; sharp second opinion
Researcher  -> Perplexity Pro (Chrome MCP) — Case 2: account Spaces + history value
Voice / live -> ChatGPT (Chrome MCP)  — Case 1: voice mode, on-demand context import
Enterprise data -> Copilot (Chrome MCP) — Case 3: no API alternative
```

API is the default backbone. Chrome MCP is reserved for the four specific cases above.

---

## Part 3: Team Assembly & Transport Selection

### Step 1 — Propose default team

Claude proposes a default based on the task type, the user's known API key situation (env-var check, Part 4), and the Transport Decision Principle (Part 2.5).

**Default team (Hybrid mode, post-v0.9 principle):**

```
Thinking team for this session:

1. Claude (Opus 4.7) — Strategist  · transport: API
2. ChatGPT (GPT-5)   — Validator   · transport: API
3. Perplexity Pro    — Researcher  · transport: Chrome MCP  (account Spaces + history)

Want to change anyone? You can:
- Swap a model (e.g. "use Sonnet instead of Opus")
- Swap transport (e.g. "ChatGPT via Chrome MCP for voice context")
- Add/remove a member
- Pick a preset: Premium / Fast / Solo Claude / Browser-Only
```

**Rationale (per Part 2.5):**
- Strategist + Validator -> API (faster, structured, no account-side value needed; state file provides context)
- Researcher -> Chrome MCP (Perplexity account features: Spaces, sourced search history; no Sonar key configured)

If the user has been voice-chatting with ChatGPT, the default shifts: ChatGPT becomes a Chrome MCP member with role "Voice Context Importer" instead of API Validator.

### Step 2 — Provider presets

| Preset | Strategist | Researcher | Validator | Cost/session est. |
|--------|-----------|-----------|-----------|-----------------|
| **Premium** | Opus 4.7 (API) | Perplexity Pro (browser) | GPT-5 (API) | $0.20-0.50 |
| **Fast** | Sonnet 4.5 (API) | Perplexity Pro (browser) | GPT-4o (API) | $0.03-0.10 |
| **Solo Claude** | Opus 4.7 (API) | — | Sonnet 4.5 (API, devil's advocate prompt) | $0.05-0.15 |
| **Browser-Only** | ChatGPT Plus (browser) | Perplexity Pro (browser) | Copilot (browser) | $0 |

### Step 3 — Lock the team

Once user confirms, write the locked team into the brainstorming state file under the Team table.

### Step 4 — API key check (NEW in v0.9)

For each `transport: api` member, check the relevant env var:
- Anthropic: `ANTHROPIC_API_KEY`
- OpenAI: `OPENAI_API_KEY`
- Perplexity Sonar: `PPLX_API_KEY` (or `PERPLEXITY_API_KEY`)

If missing, offer the onboarding tutorial (Part 4). If user declines, downgrade that member to `transport: browser` automatically, with a note in the state file.

---

## Part 4: API Key Onboarding Tutorial (NEW in v0.9)

When a required key is missing, Claude offers:

> *"I don't see an `ANTHROPIC_API_KEY` in your environment. Want me to walk you through getting one? Takes ~3 minutes."*

If yes, the flow:

### Step 1 — Console + key creation

Provider-specific URLs and notes:

| Provider | Console URL | Key prefix | Free tier? |
|----------|------------|-----------|-----------|
| Anthropic | console.anthropic.com → Settings → API Keys | `sk-ant-api03-...` | $5 promo for new accounts |
| OpenAI | platform.openai.com → API keys | `sk-proj-...` or `sk-...` | $5 promo sometimes; ChatGPT Plus does NOT include API |
| Perplexity Sonar | perplexity.ai/account/api/keys | `pplx-...` | Pro subscription includes $5/month |

Instruct user to: create a named key (e.g. `think-orchestrator-v09`), copy it once (only shown once), do NOT paste it into chat.

### Step 2 — Persist to ~/.zshenv (NOT ~/.zshrc)

**Critical:** macOS zsh non-interactive shells (which the Bash tool spawns) source `~/.zshenv`, NOT `~/.zshrc`. If the user has put the key in `~/.zshrc`, the skill will not see it.

The persistent save pattern (instruct user to run in Terminal):
```bash
# First, set it in the current session:
export PROVIDER_KEY="<paste here>"

# Then persist using the variable, not the literal value — avoids re-exposing the key:
echo "export PROVIDER_KEY=\"$PROVIDER_KEY\"" >> ~/.zshenv
```

If the user already saved to `~/.zshrc`, migrate it:
```bash
tail -1 ~/.zshrc >> ~/.zshenv
sed -i '' -e '$d' ~/.zshrc
```

### Step 3 — Verify

Claude verifies via a Bash check that does NOT echo the value:
```bash
if [ -n "$PROVIDER_KEY" ]; then echo "VISIBLE length=${#PROVIDER_KEY} prefix=${PROVIDER_KEY:0:12}"; else echo "NOT_VISIBLE"; fi
```

If visible: run a small ping (e.g. "Say PONG") to confirm the key is valid and measure baseline latency.

### Step 4 — Document in state file

Note in the brainstorming state file: which providers are now API-ready, baseline latency observed, any quirks (e.g. GPT-5 needs higher max_completion_tokens).

---

## Part 5: API Provider Registry

### Anthropic

```bash
curl -s https://api.anthropic.com/v1/messages \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "content-type: application/json" \
  -d '{"model": "claude-opus-4-7", "max_tokens": 2000, "messages": [{"role": "user", "content": "<FAT_PROMPT_WITH_RESPONSE_CONTRACT>"}]}'
```

Available models (verified 2026-05-16): `claude-opus-4-7`, `claude-opus-4-5`, `claude-sonnet-4-5`, `claude-haiku-4-5-20251001`.

Response extraction:
```bash
python3 -c "import json,sys; d=json.load(sys.stdin); print(d['content'][0]['text'])"
```

### OpenAI

```bash
curl -s https://api.openai.com/v1/chat/completions \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "gpt-5", "max_completion_tokens": 4000, "reasoning_effort": "medium", "messages": [{"role": "user", "content": "<FAT_PROMPT>"}]}'
```

Available models (verified 2026-05-16): `gpt-4o`, `gpt-4.1`, `gpt-5`, `o1`, `o3-mini`. NOT available: `o1-mini` (404).

**Reasoning-model quirk:** GPT-5, o1, o3-mini consume `max_completion_tokens` for internal reasoning_tokens FIRST, then output. If `max_completion_tokens=1024`, the entire budget may go to reasoning and you get empty `content`. Set ≥4000 for substantive output, or use `reasoning_effort: "low"` to reduce reasoning consumption.

Response extraction (note: write to file first to avoid JSON-in-bash newline corruption):
```bash
curl ... > /tmp/openai_resp.json
python3 -c "import json; d=json.load(open('/tmp/openai_resp.json')); print(d['choices'][0]['message']['content'])"
```

### Perplexity Sonar

```bash
curl -s https://api.perplexity.ai/chat/completions \
  -H "Authorization: Bearer $PPLX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "sonar-pro", "messages": [{"role": "user", "content": "<RESEARCH_PROMPT_WITH_RESPONSE_CONTRACT>"}]}'
```

Models: `sonar`, `sonar-pro`. Returns inline citations as a top-level `citations` array. **Not tested as of 2026-05-16** — user prefers browser-mode Perplexity Pro for now.

---

## Part 6: Response Contract (carried from v0.8, with v0.9 lenient parser)

Every prompt ends with the contract instruction (see v0.8 Part 3.5).

### Lenient parser (v0.9)

Accept any of these forms when extracting findings:

```python
import re, json

def extract_findings(text):
    # Try canonical form first
    for tag in ['findings', 'json']:
        m = re.search(rf'```{tag}\s*\n([\s\S]*?)\n```', text)
        if m:
            try:
                obj = json.loads(m.group(1))
            except json.JSONDecodeError:
                continue
            # Normalize to canonical shape
            if 'answers' in obj:
                return obj  # canonical
            # Flat shape like {"Q1": "...", "Q2": "..."} → normalize
            answers = [{"q_id": k, "answer": v, "confidence": "unknown"}
                       for k, v in obj.items() if k.startswith('Q')]
            return {"summary": obj.get("summary", ""), "answers": answers,
                    "open_questions": [], "flags": ["normalized from flat shape"]}
    return None  # contract failure → retry or escalate
```

**Done-signal:** look for `END_OF_RESPONSE` token after the fenced block. For API calls, the HTTP response completion is the done-signal — token-polling is browser-only.

---

## Part 7: Collaborative Thinking Loop (v0.9 hybrid)

```
1. ASSEMBLE   — Team + transports locked (Part 3)
2. ANALYZE    — Check local files; draft ONE fat prompt per member
3. ACTIVATE   — Parallel batch:
                · API members: prepare curl commands in a single tool-use turn
                · Browser members: open tabs via Chrome MCP in same turn
4. PROMPT     — Send all prompts in parallel:
                · API: fire curls (can run in background if slow)
                · Browser: inject prompts (with clipboard-bridge fallback)
5. COLLECT    — Wait for responses:
                · API: blocking on HTTP response (~3-20s each, parallel)
                · Browser: poll for END_OF_RESPONSE token
6. SYNTHESIZE — Parse all findings via lenient parser; merge at JSON field level
7. PERSIST    — Update brainstorming state file with each member's raw JSON
8. EXECUTE or ESCALATE
```

### Parallel API + Browser orchestration

When the team mixes transports, fire everything in the same orchestration turn:
- Multiple Bash curl calls in one assistant turn (parallel HTTP)
- Multiple Chrome MCP `tabs_create_mcp` / inject calls in the same turn
- Then collect: APIs return inline, browsers polled afterwards

Total wall-time = max(slowest API call, slowest browser response). With Opus 4.7 (~7s) + Perplexity browser (~30s), one round = ~30s.

### Fat prompt templates (per role, transport-agnostic)

Identical to v0.8 Part 7. Only the transport differs, not the prompt shape.

---

## Part 8-13: Unchanged from v0.8

- **Part 8** — Context Management & Reconstruction
- **Part 9** — Conversation Import (Chrome MCP-side fallback)
- **Part 10** — Question Escalation Protocol
- **Part 11** — Output Standards
- **Part 12** — Open AI Registry (browser side)
- **Part 13** — Behavioral Summary

See v0.8 SKILL.md for the full text of these parts; they apply unchanged.

---

## Part 14: Brainstorming State File schema (extended)

The Team table now includes transport:

```markdown
## Team
| AI | Role | Transport | Model / URL |
|----|------|-----------|-------------|
| Claude | Strategist | API | claude-opus-4-7 |
| GPT-5 | Validator | API | gpt-5 |
| Perplexity Pro | Researcher | Browser (Chrome MCP) | perplexity.ai/[session] |
```

The Raw Notes section stores findings JSON verbatim per round per member, as in v0.8.

---

## Part 15: Failure Modes & Recovery

| Failure | Detection | Recovery |
|---------|-----------|----------|
| API key missing | env-var check at team assembly | Offer onboarding tutorial (Part 4); else downgrade to browser |
| API rate limit (HTTP 429) | curl returns 429 | Exponential backoff (2s, 4s, 8s), max 3 retries, then escalate |
| API timeout | curl exits >60s without response | Retry once; if still failing, downgrade that member to browser this round |
| Reasoning model empty output | `completion_tokens == reasoning_tokens` | Re-prompt with higher max_completion_tokens (4000 → 8000) |
| Contract violation (no findings block) | parser returns None | Re-prompt: "Please re-format using the required findings block." |
| GPT-5 flat-shape response | parser normalizes automatically | Note in state file; no action needed |
| Browser injection empty | input element text doesn't contain prompt tail | Clipboard-bridge fallback (v0.8 Part 3.6) |
| Browser END_OF_RESPONSE never appears | 90s polling timeout | Extract whatever is on the page; flag as "incomplete" |

---

## Final Principle

> **Assemble wisely. Choose transport pragmatically. Orchestrate proactively. Persist everything. Escalate intelligently. Execute relentlessly — in parallel, with structured responses, across API and browser, in fat prompts.**

The system works because Claude is the always-on coordinator that:
- Never loses context (brainstorming state file)
- Never forgets a decision (decision log)
- Always knows the fastest path (API where available, browser where needed)
- Always guides the human through setup (onboarding tutorial)
- Always returns a coherent synthesis (transport-agnostic JSON merge)
