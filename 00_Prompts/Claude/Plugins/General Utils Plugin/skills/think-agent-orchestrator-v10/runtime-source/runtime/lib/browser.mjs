// Browser bootstrap.
//
// IMPORTANT (Chrome 136+ security): Chrome silently disables the remote
// debugging port/pipe when --user-data-dir points to the default profile.
// This blocks the "reuse the user's normal Chrome" path. Workaround: we use
// a DEDICATED profile under ~/.think-engine/chrome-profile/ — a second
// Chrome instance that runs in parallel with the user's normal Chrome, with
// its own logins. One-time login cost, zero ongoing disruption.
//
// Strategy:
//   1. Try CDP-attach to localhost:9222 if the user has already launched
//      Chromium with debugging on (advanced path). If found, use that.
//   2. Otherwise launchPersistentContext against ~/.think-engine/chrome-profile/.
//      This is the default path. The first run opens an empty profile and
//      the user logs into each AI service once.

import { chromium } from 'playwright';
import { existsSync, mkdirSync } from 'node:fs';
import { homedir, platform } from 'node:os';
import { join } from 'node:path';
import { log } from './log.mjs';

const CDP_PORT = parseInt(process.env.THINK_ENGINE_CDP_PORT || '9222', 10);
const CDP_URL = `http://localhost:${CDP_PORT}`;

// Dedicated profile under the think-engine root (NOT the user's default Chrome).
export const DEDICATED_PROFILE_DIR = join(homedir(), '.think-engine', 'chrome-profile');

export function defaultChromeExecutable() {
  switch (platform()) {
    case 'darwin':
      return '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome';
    case 'win32':
      return 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';
    case 'linux':
      return '/usr/bin/google-chrome';
    default:
      return null;
  }
}

/**
 * Try to connect to a running Chrome via CDP. Returns null if nothing on port.
 * Advanced path: user has manually launched a Chromium instance with debugging
 * enabled and a non-default profile.
 */
async function tryCdpAttach() {
  try {
    log.debug(`Attempting CDP attach at ${CDP_URL}`);
    const browser = await chromium.connectOverCDP(CDP_URL, { timeout: 2000 });
    log.info(`CDP attached to running Chromium on ${CDP_URL}`);
    return browser;
  } catch (e) {
    log.debug(`CDP attach failed: ${e.message.split('\n')[0]}`);
    return null;
  }
}

/**
 * Launch a persistent context against the dedicated think-engine profile.
 * First run creates an empty profile; user logs in to each provider once.
 * The profile persists across runs.
 */
async function launchPersistent() {
  const userDataDir = DEDICATED_PROFILE_DIR;
  if (!existsSync(userDataDir)) {
    log.info(`Creating dedicated Chrome profile at ${userDataDir}`);
    mkdirSync(userDataDir, { recursive: true });
  }
  const executable = defaultChromeExecutable();
  const isFirstRun = !existsSync(join(userDataDir, 'Default'));

  log.info(`Launching Chromium with dedicated profile: ${userDataDir}${isFirstRun ? ' (FIRST RUN - log in to each AI)' : ''}`);
  const ctx = await chromium.launchPersistentContext(userDataDir, {
    executablePath: executable && existsSync(executable) ? executable : undefined,
    channel: executable && existsSync(executable) ? undefined : 'chrome',
    headless: false,
    viewport: null,
    // Run with the real Chrome sandbox and WITHOUT --enable-automation/--no-sandbox.
    // Cloudflare Turnstile detects those markers and loops the "verify you are human"
    // challenge forever, which blocks both login and normal use. See applyStealth().
    chromiumSandbox: true,
    ignoreDefaultArgs: ['--enable-automation', '--no-sandbox'],
    args: ['--disable-blink-features=AutomationControlled', '--no-default-browser-check', '--no-first-run'],
  });
  await applyStealth(ctx);
  return { ctx, isPersistent: true, isFirstRun };
}

/**
 * Hide navigator.webdriver before any page script runs. Combined with the launch
 * flags above, this lets Cloudflare/Google bot checks treat the automated Chrome
 * like a normal browser. Best-effort: ignored if the context disallows init scripts.
 */
async function applyStealth(ctx) {
  try {
    await ctx.addInitScript(() => {
      Object.defineProperty(navigator, 'webdriver', { get: () => undefined });
    });
  } catch (e) {
    log.debug(`applyStealth skipped: ${e.message}`);
  }
}

/**
 * Get a browser context for the run, preferring CDP attach over launch.
 * Returns { ctx, browser?, isPersistent, mode, isFirstRun? }.
 */
export async function getContext() {
  // Try CDP first (advanced users with their own debug-Chromium running)
  const browser = await tryCdpAttach();
  if (browser) {
    const contexts = browser.contexts();
    const ctx = contexts[0] || (await browser.newContext());
    await applyStealth(ctx);
    return { ctx, browser, isPersistent: false, mode: 'cdp' };
  }

  // Default path: dedicated persistent profile
  const { ctx, isFirstRun } = await launchPersistent();
  return { ctx, isPersistent: true, mode: 'persistent', isFirstRun };
}

/**
 * Find an existing page that matches one of the provider's URL patterns,
 * or open a new page at the provider's startUrl.
 */
export async function findOrOpenProviderPage(ctx, provider, { mode = 'continue' } = {}) {
  const pages = ctx.pages();
  if (mode === 'continue') {
    for (const p of pages) {
      const url = p.url();
      if ((provider.urlPatterns || []).some(re => re.test(url))) {
        log.info(`Reusing existing ${provider.name} tab: ${url}`);
        await p.bringToFront();
        return { page: p, reused: true };
      }
    }
    log.info(`No existing ${provider.name} tab found; opening new at ${provider.startUrl}`);
  } else {
    log.info(`Opening new ${provider.name} tab at ${provider.startUrl}`);
  }
  // Reuse the first blank/about:blank tab if present (avoid stacking tabs on first run)
  let page = pages.find(p => p.url() === 'about:blank' || p.url() === '');
  if (!page) {
    page = await ctx.newPage();
  }
  await page.goto(provider.startUrl, { waitUntil: 'domcontentloaded' });
  return { page, reused: false };
}
