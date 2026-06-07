#!/usr/bin/env node
// Think Engine v0.10 — orchestrator entry point.
//
// Usage:
//   node orchestrator.mjs --provider chatgpt --mode continue --prompt-file PATH --output PATH
//   node orchestrator.mjs --provider chatgpt --mode new --prompt "literal text"
//   node orchestrator.mjs --healthcheck
//   node orchestrator.mjs --list-providers
//
// Exit codes:
//   0 — success (response written to --output or printed to stdout)
//   1 — provider failure (selectors broken, login expired, timeout)
//   2 — setup needed (Playwright/Chrome not installed)
//   3 — bad invocation (missing args, unknown provider)

import { readFile, writeFile, mkdir } from 'node:fs/promises';
import { existsSync } from 'node:fs';
import { join, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';
import { log } from './lib/log.mjs';

const __dirname = dirname(fileURLToPath(import.meta.url));
const ROOT = join(__dirname, '..');

// -- Arg parsing (minimal, no deps) --
function parseArgs(argv) {
  const out = { _: [] };
  for (let i = 2; i < argv.length; i++) {
    const a = argv[i];
    if (a.startsWith('--')) {
      const key = a.slice(2);
      const next = argv[i + 1];
      if (next && !next.startsWith('--')) {
        out[key] = next;
        i++;
      } else {
        out[key] = true;
      }
    } else {
      out._.push(a);
    }
  }
  return out;
}

const args = parseArgs(process.argv);

// -- Pre-flight: Playwright installed? --
function setupNeeded() {
  if (!existsSync(join(ROOT, 'node_modules', 'playwright'))) return 'Playwright not installed';
  if (!existsSync(join(ROOT, 'version'))) return 'version stamp missing';
  return null;
}

const setupErr = setupNeeded();
if (setupErr) {
  process.stderr.write(`SETUP_NEEDED: ${setupErr}\n`);
  process.stderr.write(`  Run: bash ${join(ROOT, 'setup.sh')}\n`);
  process.exit(2);
}

// -- List providers --
if (args['list-providers']) {
  const { listProviders } = await import('./lib/provider-loader.mjs');
  const names = await listProviders();
  process.stdout.write(JSON.stringify({ providers: names }, null, 2) + '\n');
  process.exit(0);
}

// -- Healthcheck --
if (args.healthcheck) {
  const result = { ok: true, version: (await readFile(join(ROOT, 'version'), 'utf8')).trim() };
  try {
    const { listProviders } = await import('./lib/provider-loader.mjs');
    result.providers = await listProviders();
  } catch (e) {
    result.ok = false;
    result.error = e.message;
  }
  try {
    const pw = await import('playwright');
    result.playwright_version = pw.default?.version || pw._impl?.version || 'unknown';
  } catch (e) {
    result.ok = false;
    result.playwright_error = e.message;
  }
  process.stdout.write(JSON.stringify(result, null, 2) + '\n');
  process.exit(result.ok ? 0 : 1);
}

// -- Validate run args --
const providerName = args.provider;
if (!providerName) {
  process.stderr.write('Missing --provider. Run with --list-providers to see options.\n');
  process.exit(3);
}

const mode = args.mode || 'continue';
if (!['continue', 'new'].includes(mode)) {
  process.stderr.write(`Invalid --mode '${mode}'. Use 'continue' or 'new'.\n`);
  process.exit(3);
}

let prompt = args.prompt;
if (!prompt && args['prompt-file']) {
  prompt = await readFile(args['prompt-file'], 'utf8');
}
if (!prompt) {
  process.stderr.write('Missing --prompt or --prompt-file.\n');
  process.exit(3);
}

const timeout = parseInt(args.timeout || '180000', 10);
const traceOnFailure = args['no-trace'] !== true;

// -- Load provider --
const { loadProvider } = await import('./lib/provider-loader.mjs');
let provider;
try {
  provider = await loadProvider(providerName);
} catch (e) {
  process.stderr.write(`Failed to load provider '${providerName}': ${e.message}\n`);
  process.exit(3);
}

log.info(`Provider: ${provider.name} | mode: ${mode} | timeout: ${timeout}ms`);

// -- Run --
const { getContext, findOrOpenProviderPage } = await import('./lib/browser.mjs');
const startTime = Date.now();
let ctx, browser, mode_used, page, traceStarted = false;

try {
  const conn = await getContext();
  ctx = conn.ctx;
  browser = conn.browser;
  mode_used = conn.mode;
  log.info(`Browser ready (mode: ${mode_used})`);

  // Tracing (only when launching a new context; CDP-attach contexts may not allow tracing)
  if (traceOnFailure && conn.isPersistent) {
    try {
      await ctx.tracing.start({ screenshots: true, snapshots: true });
      traceStarted = true;
    } catch (e) {
      log.warn(`Tracing failed to start: ${e.message}`);
    }
  }

  // Find or open page
  const { page: p, reused } = await findOrOpenProviderPage(ctx, provider, { mode });
  page = p;
  log.info(`Page ${reused ? 'reused' : 'opened'}: ${page.url()}`);

  // Login check
  if (provider.loginCheck) {
    const loggedIn = await provider.loginCheck(page);
    if (!loggedIn) {
      throw new Error(`Not logged in to ${provider.name}. Open ${provider.startUrl} in Chrome and log in, then retry.`);
    }
  }

  // Submit
  log.info(`Submitting prompt (${prompt.length} chars)`);
  await provider.submitPrompt(page, prompt);

  // Wait for completion
  log.info(`Waiting for response (timeout: ${timeout}ms)`);
  await provider.waitForCompletion(page, { timeout });

  // Extract
  const response = await provider.extractResponse(page);
  const url = page.url();
  const elapsed = Date.now() - startTime;
  log.info(`Done in ${elapsed}ms (${response.length} chars)`);

  const result = {
    ok: true,
    provider: provider.name,
    mode: mode_used,
    page_reused: reused,
    elapsed_ms: elapsed,
    response,
    page_url: url,
  };

  if (args.output) {
    await mkdir(dirname(args.output), { recursive: true }).catch(() => {});
    await writeFile(args.output, JSON.stringify(result, null, 2));
    log.info(`Result written to ${args.output}`);
  } else {
    process.stdout.write(JSON.stringify(result, null, 2) + '\n');
  }

  // Clean shutdown
  if (traceStarted) await ctx.tracing.stop().catch(() => {});
  // Don't close persistent context — keep browser alive for next call.
  // For CDP attached, don't close either.
  process.exit(0);

} catch (e) {
  log.error(`FAILURE: ${e.message}`);
  if (traceStarted && ctx) {
    const tracePath = join(ROOT, 'state', 'traces', `trace-${Date.now()}.zip`);
    try {
      await ctx.tracing.stop({ path: tracePath });
      log.error(`Trace saved: ${tracePath}`);
      log.error(`  View with: npx playwright show-trace ${tracePath}`);
    } catch (tErr) {
      log.error(`Trace save failed: ${tErr.message}`);
    }
  }
  const errResult = {
    ok: false,
    provider: providerName,
    error: e.message,
    elapsed_ms: Date.now() - startTime,
  };
  if (args.output) {
    await writeFile(args.output, JSON.stringify(errResult, null, 2)).catch(() => {});
  } else {
    process.stdout.write(JSON.stringify(errResult, null, 2) + '\n');
  }
  process.exit(1);
}
