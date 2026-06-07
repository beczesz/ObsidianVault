import { getContext, findOrOpenProviderPage } from './runtime/lib/browser.mjs';
import { loadProvider } from './runtime/lib/provider-loader.mjs';

console.log('[1] Getting browser context...');
const conn = await getContext();
console.log(`[2] OK — mode: ${conn.mode}, isPersistent: ${conn.isPersistent}, firstRun: ${conn.isFirstRun}`);
console.log(`    Existing pages: ${conn.ctx.pages().length}`);

console.log('[3] Loading ChatGPT provider...');
const chatgpt = await loadProvider('chatgpt');

console.log('[4] Opening ChatGPT...');
const { page, reused } = await findOrOpenProviderPage(conn.ctx, chatgpt, { mode: 'continue' });
console.log(`[5] Page ${reused ? 'reused' : 'opened'}: ${page.url()}`);

// Wait briefly so the page loads, then check login state
console.log('[6] Waiting 4s for page to settle...');
await new Promise(r => setTimeout(r, 4000));

const loggedIn = await chatgpt.loginCheck(page);
console.log(`[7] Login check: ${loggedIn ? 'LOGGED IN ✓' : 'NOT LOGGED IN (this is normal on first run)'}`);

console.log(`[8] Current URL: ${page.url()}`);
console.log(`[9] Page title: ${await page.title().catch(() => '(none)')}`);

// Don't close the context — leave Chrome open for the user to log in if needed
console.log('[10] Leaving Chrome open. You can log in to ChatGPT now.');
process.exit(0);
