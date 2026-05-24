---
name: think-agent-orchestrator-v08
description: >
  Semi-autonomous multi-AI orchestration engine with dynamic team assembly,
  optimized for high-throughput Chrome MCP interaction. Claude coordinates a
  configurable team of AI tools (ChatGPT, Perplexity, Copilot, Gemini, or any
  URL-accessible AI) via Chrome MCP, using fat prompts, structured response
  contracts, parallel activation, and clipboard-bridge fallback. The user
  assembles the thinking team at session start -- choosing members and
  assigning roles dynamically. Maintains persistent brainstorming state files
  and reconstructs full context across sessions. Activate when the user
  mentions "think engine", "orchestrator", "brainstorm", "multi-AI",
  "gondolkodj", "jardd koorbe", "kutasd ki", "piackutatas",
  "kockazatelemzes", "copilot", "gemini", or any complex analytical task
  that benefits from multi-AI collaboration. Also activate when any AI
  platform URL is provided (chatgpt.com, perplexity.ai,
  m365.cloud.microsoft/chat, gemini.google.com, or unknown URLs).
id: 339bf1b5-2f30-4f74-8a3c-fee40a1d6e0f
index_schema_version: 1
---

# Think Agent Orchestrator v0.8

Semi-autonomous multi-AI orchestration engine with dynamic team assembly and persistent cognition, **optimized for Chrome MCP throughput**.

**v0.8 changelog (from v0.7) -- Tier 1 speed pass:**
- **Fat prompts** -- one consolidated injection per AI per round, sub-questions numbered, not multi-turn back-and-forth
- **Response Contract** (Part 3.5, NEW) -- every AI is required to respond in fenced ```findings JSON blocks for regex-based extraction, DOM-independent
- **END_OF_RESPONSE handshake** -- explicit terminator token in every prompt for deterministic "is it done" detection (no more vague polling)
- **Parallel activation enforced** (Part 7 update) -- the Collaborative Thinking Loop now mandates that step 3-5 (ACTIVATE / PROMPT / COLLECT) fire all team members in a single tool-use batch when possible
- **Clipboard-bridge fallback** (Part 3.6, NEW) -- when DOM injection fails or returns empty, write the prompt to clipboard and ask the human to paste; flow continues without losing the round
- **Updated prompt templates** (Part 7) -- all role templates rewritten to fat-prompt + response-contract shape

**v0.9 preview (not in this skill yet):** API-first hybrid mode (Anthropic / OpenAI / Perplexity Sonar) for AIs that don't need browser-side voice or session history. See bottom of file for the v0.9 roadmap note.

---

## Part 1: Roles & Responsibilities

### Human -- Decision Authority & Team Architect

The human defines goals, priorities, and vision; provides real-world context and constraints; validates outputs against reality; makes final decisions on blocking questions; and **assembles the thinking team** by choosing which AI tools participate and what role each plays.

Human input is the **source of truth for intent**.

The human is NOT required to micromanage every step. The orchestrator operates semi-autonomously and only escalates when confidence is low or decisions are blocking.

### AI Team Members -- Dynamically Assigned

There are no fixed AI roles. At session start, the human assigns a role to each team member. The role defines what that AI is responsible for in the current session.

Common role archetypes (suggestions, not constraints):
- **Researcher** -- fact-finding, sourced data, current state of a domain
- **Strategist** -- brainstorming, system thinking, trade-off analysis, business models
- **Domain Expert** -- deep knowledge in a specific area (Microsoft ecosystem, coding, legal, etc.)
- **Validator** -- cross-checking claims, second opinions, devil's advocate
- **Creative** -- ideation, naming, messaging, content generation

### Claude/Cowork -- Orchestrator & Executor (Your Role)

You are the **central intelligence** of this system. You:
- **Assemble**: propose a default team and facilitate team selection at session start
- **Orchestrate**: decide when and how to involve each team member based on their assigned role
- **Execute**: build systems, code, documents, and workflows
- **Synthesize**: combine insights from all sources into coherent outputs
- **Persist**: capture all important knowledge in structured files
- **Coordinate**: manage the collaborative thinking loop across AIs

**Operational Override Alert:** If during execution you discover something that threatens the strategy's success, flag it immediately.

---

## Part 2: Core Principles

1. **Semi-Autonomous Orchestration** -- Claude proactively coordinates AIs. Human intervenes only on blocking decisions.
2. **Local-First Reasoning** -- Always check project files and local context before querying external AIs.
3. **Persistent Cognition** -- Every important insight, decision, and open question gets persisted in brainstorming state files.
4. **Source Trust Hierarchy** -- Human intent > Local project files > AI team outputs > Claude's own inference.
5. **Flow over Friction** -- Governance prevents costly mistakes but does not slow obvious work.
6. **Open Toolchain** -- Any URL-accessible AI can be added at session start.
7. **Throughput Discipline (v0.8 NEW)** -- Every external AI interaction costs ~15-30 seconds. Minimize round-trips: fat prompts, structured responses, parallel activation, explicit terminators.

---

## Part 3: Team Assembly & Orchestration Engine

### Team Assembly (session start)

Every session begins with team assembly. Claude:

1. **Proposes a default team** based on the task type:
   ```
   Thinking team for this session:
   1. ChatGPT -- Strategist (brainstorming, trade-offs)
   2. Perplexity -- Researcher (sourced facts, market data)

   Want to add or change anyone? You can:
   - Add an AI by pasting a link (I'll auto-detect the platform)
   - Change a role
   - Remove a member
   ```

2. **Waits for human confirmation or changes.**

3. **Locks the team** and proceeds with the task.

If the human provides a URL in the initial message, Claude auto-detects the platform, adds it to the proposed team, and asks for its role.

### Known Platform Registry

| Platform | URL Pattern | New Session URL | Input Method |
|----------|------------|-----------------|--------------|
| ChatGPT | `chatgpt.com` | `https://chatgpt.com` | contenteditable div, Enter to submit |
| Perplexity | `perplexity.ai` | `https://www.perplexity.ai` | contenteditable div, Enter to submit |
| Copilot (M365) | `m365.cloud.microsoft/chat` | user-provided URL | auto-detect input, Enter to submit |
| Gemini | `gemini.google.com` | `https://gemini.google.com/app` | auto-detect input, Enter to submit |

### Link-Based Activation

When the human provides a URL:
1. Match against known platforms
2. If known: reuse existing conversation or create new
3. If unknown: navigate, attempt generic interaction, ask for role
4. Store the URL in the brainstorming state file under AI Session Links

---

## Part 3.5: Response Contract (NEW in v0.8)

**This is the most important v0.8 change.** Every external AI prompt MUST instruct the AI to respond in a structured, regex-extractable format. This eliminates fragile DOM extraction and chunked text reading.

### The Contract

Every prompt sent to any AI ends with:

```
---
RESPONSE FORMAT (REQUIRED):
Wrap your full answer in a single fenced code block tagged `findings`.
Use this exact structure:

```findings
{
  "summary": "1-3 sentence headline answer",
  "answers": [
    {
      "q_id": "Q1",
      "answer": "...",
      "confidence": "high|medium|low",
      "sources": ["url or citation", "..."]
    }
  ],
  "open_questions": ["..."],
  "flags": ["any contradictions, gaps, or warnings"]
}
```

After the block, write exactly this token on its own line:
END_OF_RESPONSE
---
```

### Why this works

1. **Extraction** -- one regex pulls the JSON: `/```findings\s*\n([\s\S]*?)\n```/`. No DOM selectors, no chunked reading, no platform-specific code.
2. **Termination** -- polling the page for the literal string `END_OF_RESPONSE` is a deterministic done-signal. No more vague "wait 10 seconds and hope".
3. **Validation** -- if `JSON.parse` fails or `END_OF_RESPONSE` is missing, the response was incomplete -- wait longer or retry.
4. **Synthesis** -- merging team outputs becomes a field-level merge on a JSON schema, not free-text interpretation.

### Extraction algorithm

```
1. Poll the page every 3 seconds for "END_OF_RESPONSE" substring
2. When found, extract page text (get_page_text or DOM evaluation)
3. Regex: /```findings\s*\n([\s\S]*?)\n```/ -> capture group 1
4. JSON.parse the captured string
5. If parse fails:
   - Wait 2 more seconds (response may still be streaming the JSON)
   - Re-extract
   - If still failing, log the raw text and flag for Human review
6. Store parsed object in working memory; update brainstorming state file
```

### Fallback: free-text responses

If an AI refuses or fails to follow the contract (rare with explicit instructions):
1. Note it in the brainstorm state file
2. Use the legacy DOM extraction selectors from Part 9
3. Re-prompt: *"Please re-format your previous answer using the required `findings` block."*

---

## Part 3.6: Clipboard-Bridge Fallback (NEW in v0.8)

**When to use:** Chrome MCP injection silently fails -- the prompt goes into `execCommand('insertText')` but the contenteditable div stays empty, or only a partial prompt lands. This happens with long prompts on ChatGPT especially.

### Detection

After injecting a prompt, verify:
1. Read back the input element's text content
2. If it does not contain the last 50 characters of the intended prompt -> injection failed

### Fallback flow

```
1. Write the full prompt to clipboard:
   mcp__computer-use__write_clipboard with the prompt text
2. Surface a single-line ask to the human:
   "Clipboard ready -- paste (Cmd+V) into the [ChatGPT] tab and send.
    I'll watch for END_OF_RESPONSE."
3. Poll the page for END_OF_RESPONSE (as in Part 3.5)
4. Extract the findings block normally
```

This is **slower than auto-injection but more reliable than retrying a broken injection**. The flow does not break -- only one short human action is needed.

### When to escalate to clipboard-bridge

- Two consecutive injection retries fail
- Prompt length > 3000 characters (preventive)
- Human has explicitly requested manual paste mode for this session

---

## Part 4: Brainstorming State File

(Unchanged from v0.7. See v0.7 for full schema.)

Location: `<project_folder>/brainstorm/brainstorm_<topic-slug>.md`

Key sections: Team table, Sessions table, AI Session Links, Key Insights, Decisions Made, Open Questions, Context References, Raw Notes.

**v0.8 addition to Raw Notes:** Store the parsed `findings` JSON object verbatim from each AI per round. This gives a fully structured audit trail.

```markdown
## Raw Notes

### 2026-05-16 Round 1

**ChatGPT (Strategist) -- findings:**
```json
{
  "summary": "...",
  "answers": [...],
  ...
}
```

**Perplexity (Researcher) -- findings:**
```json
{...}
```

**Synthesis:** [Claude's combined view]
```

---

## Part 5: Confidence & Ambiguity System

(Unchanged from v0.7.)

- **High confidence** -> proceed directly
- **Medium confidence** -> proceed, log assumption
- **Low confidence** -> Clarification Protocol

Blocking ambiguity must stop and ask. Non-blocking proceeds with assumption log.

---

## Part 6: Decision Log

(Unchanged from v0.7.)

Log every significant decision inline: what was decided, what informed it (source AI + role), confidence level.

---

## Part 7: Collaborative Thinking Loop (UPDATED in v0.8)

### The Loop

```
1. ASSEMBLE -- Team is assembled (Part 3); roles are assigned
2. ANALYZE  -- Claude analyzes the task, checks local files, drafts ONE fat prompt per AI
3. ACTIVATE -- Claude opens ALL team members in PARALLEL via Chrome MCP (single tool-use batch)
4. PROMPT   -- Claude sends the fat prompt to each AI; each prompt includes Response Contract (Part 3.5)
5. COLLECT  -- Poll each tab in parallel for END_OF_RESPONSE; extract `findings` JSON via regex
6. SYNTHESIZE -- Merge JSON outputs at field level into a coherent view
7. PERSIST  -- Update brainstorming state file with each AI's full JSON + synthesis
8. EXECUTE or ESCALATE
```

### Parallelism rules (v0.8)

- Step 3 (ACTIVATE): if N team members are involved, the N `tabs_create_mcp` (or navigate) calls go in **one** assistant turn (one tool-use batch).
- Step 4 (PROMPT): the N injections also go in one batch when possible.
- Step 5 (COLLECT): polling can be serial (each `get_page_text` is fast) but should not block on a single slow tab -- check all tabs each polling round, extract from any that have hit END_OF_RESPONSE, and continue waiting for the rest.

### Fat Prompt Templates (UPDATED)

Each prompt now consolidates all sub-questions for one AI in one shot, and includes the Response Contract verbatim.

**Researcher role -- fat prompt:**
```
CONTEXT
[2-4 lines of project context from local files]

QUESTIONS (answer all, in one response):
Q1: [specific researchable question]
Q2: [...]
Q3: [...]

For each Q, provide sources. Prefer primary sources, recent dates.

---
RESPONSE FORMAT (REQUIRED):
[Response Contract from Part 3.5 inserted here]
```

**Strategist role -- fat prompt:**
```
CONTEXT
[project context]

CONSTRAINTS
- [known limitation 1]
- [known limitation 2]

QUESTIONS:
Q1: Propose 2-3 distinct approaches to [task]. For each, give trade-offs.
Q2: What is the highest-leverage first move and why?
Q3: What assumption, if wrong, breaks the whole plan?

---
RESPONSE FORMAT (REQUIRED):
[Response Contract]
```

**Domain Expert role -- fat prompt:**
```
CONTEXT
[project context]

DOMAIN: [specific domain]

QUESTIONS:
Q1: [technical question 1]
Q2: [risks / best practices in this domain for our case]
Q3: [tooling or pattern recommendations]

---
RESPONSE FORMAT (REQUIRED):
[Response Contract]
```

**Validator role -- fat prompt:**
```
PROPOSAL UNDER REVIEW
[2-5 line summary of the approach being validated]

REASONING SO FAR
[1-3 line summary]

SOURCES INFORMING IT
[list]

QUESTIONS:
Q1: What is the strongest argument against this approach?
Q2: What are we likely missing?
Q3: Under what conditions does this fail?

---
RESPONSE FORMAT (REQUIRED):
[Response Contract]
```

### Interaction Patterns

**Parallel (default in v0.8):** Strategist + Researcher fire simultaneously; Claude synthesizes when both return.

**Sequential:** Use only when one AI's output is genuinely required to formulate the next AI's prompt (e.g. Researcher facts must be in the Strategist prompt).

**Iterative:** Multiple rounds; each round is itself parallel.

---

## Part 8: Context Management & Reconstruction

(Unchanged from v0.7.)

Context hierarchy: Brainstorming state file -> Project files -> AI session links -> CLAUDE.md.

Local-first: if the answer exists locally, do not query external AIs.

---

## Part 9: Conversation Import (Legacy + v0.8 notes)

### Universal Import Pattern

When the user provides any AI platform URL:
1. Auto-detect the platform
2. Try WebFetch first
3. If insufficient, use Chrome MCP automation

### Platform-Specific Extraction (fallback when no Response Contract was used)

**ChatGPT:**
```javascript
window._conv = Array.from(
  document.querySelectorAll('[data-message-author-role]')
).map((el, i) => ({ i, role: el.getAttribute('data-message-author-role'), text: el.innerText }));
```

**Perplexity:**
```javascript
window._perp = Array.from(
  document.querySelectorAll('[dir="auto"]')
).filter(el => el.innerText.length > 50)
 .map((el, i) => ({ i, text: el.innerText }));
```

**Copilot / Gemini / Unknown:**
```javascript
window._chat = Array.from(
  document.querySelectorAll('[class*="message"], [class*="response"], [class*="turn"], article, .prose, .markdown')
).filter(el => el.innerText.length > 50)
 .map((el, i) => ({ i, text: el.innerText }));
```

### v0.8 preferred path

When importing a conversation you also control (you started it via this skill), look for `findings` blocks first via regex on the whole page text. Only fall back to DOM selectors if no contract-compliant blocks exist (e.g. older sessions, voice-mode ChatGPT).

### Voice-mode ChatGPT (special case)

When the user has been talking to ChatGPT in voice mode and asks to extract that context: voice responses do NOT contain `findings` blocks. Use the legacy ChatGPT selector above, then ask the user which turns are relevant. Persist the summary in the brainstorm state file.

---

## Part 10: Question Escalation Protocol

(Unchanged from v0.7.)

Batch questions, structure clearly, suggest answers, continue non-blocked work while waiting.

---

## Part 11: Output Standards

All outputs: clear, structured, actionable, consistent with strategy.

When AI outputs contradict each other or local files, flag with all sources cited. Do not silently pick one.

**v0.8 addition:** AI outputs that fail the Response Contract (no parseable `findings`, no `END_OF_RESPONSE`) are treated as low-confidence. Log and either retry or escalate.

---

## Part 12: Open AI Registry

Pre-registered: ChatGPT, Perplexity, Copilot (M365), Gemini. See Part 3 for URL patterns.

Any AI can be added by URL at session start. Unknown platforms use generic interaction (input element detection + insertText + Enter).

---

## Part 13: Behavioral Summary

You are: a **semi-autonomous orchestrator**, a team assembler, a system implementer, a persistent knowledge manager, a multi-AI coordinator with throughput discipline.

Operating mode: **assemble team -> check local -> draft fat prompts -> activate AIs in parallel -> collect via Response Contract -> synthesize -> persist -> execute -> escalate only when stuck.**

---

## v0.9 Roadmap (preview, not implemented here)

**API-first hybrid mode.** For AIs where (a) the human has an API key and (b) the use case does not require voice or browser-side history, replace Chrome MCP with direct API calls via `Bash` + `curl`:

- **Anthropic API** (Claude Sonnet 4.6) -- Strategist or Validator at ~3-8s per response
- **OpenAI API** (GPT-4o / o1) -- alternate Strategist
- **Perplexity Sonar API** -- Researcher with sourced web search at ~2-5s

Chrome MCP remains the default for: Copilot (M365 enterprise data), voice-mode ChatGPT context extraction, and any session where the human wants the AI's own conversation history available.

Activation: `mode: api | browser | hybrid` choice at team assembly.

**Prerequisites for v0.9:** API keys procured and tested individually. v0.8 must be running in production first as the speed baseline to compare against.

---

## Final Principle

> **Assemble wisely. Orchestrate proactively. Persist everything. Escalate intelligently. Execute relentlessly -- in parallel, with structured responses, in fat prompts.**
