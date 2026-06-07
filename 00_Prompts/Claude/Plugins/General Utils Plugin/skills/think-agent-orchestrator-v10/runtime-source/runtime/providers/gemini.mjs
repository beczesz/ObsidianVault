// Google Gemini (gemini.google.com) provider. Last tested: 2026-05-26 — UNVERIFIED.

const SELECTORS = {
  textbox: 'rich-textarea div[contenteditable="true"], div[contenteditable="true"][role="textbox"]',
  sendButton: 'button[aria-label*="Send" i]',
  stopButton: 'button[aria-label*="Stop" i]',
  lastAnswer: 'model-response:last-of-type, [data-message-author="model"]:last-of-type',
  loginButton: 'a[href*="accounts.google.com"]:has-text("Sign in")',
};

export default {
  name: 'gemini',
  urlPatterns: [/gemini\.google\.com/],
  startUrl: 'https://gemini.google.com/app',

  async loginCheck(page) {
    return !(await page.locator(SELECTORS.loginButton).first().isVisible().catch(() => false));
  },

  // Google shows a CMP/cookie-consent overlay (cdk-overlay-container) that sits on
  // top of the composer and intercepts clicks. Dismiss it before interacting.
  async dismissConsent(page) {
    await page.waitForTimeout(2000);
    const labels = ['Accept all', 'Reject all', 'I agree', 'Az összes elfogadása', 'Az összes elutasítása', 'Elfogadom'];
    for (const label of labels) {
      const btn = page.getByRole('button', { name: new RegExp(label, 'i') }).first();
      if (await btn.isVisible().catch(() => false)) {
        await btn.click().catch(() => {});
        await page.waitForTimeout(1000);
        return;
      }
    }
  },

  async submitPrompt(page, prompt) {
    await this.dismissConsent(page);
    const textbox = page.locator(SELECTORS.textbox).first();
    await textbox.waitFor({ state: 'visible', timeout: 30000 });
    await textbox.click();
    const isMac = process.platform === 'darwin';
    await page.evaluate(async (text) => { await navigator.clipboard.writeText(text); }, prompt).catch(() => {});
    await textbox.press(isMac ? 'Meta+V' : 'Control+V');
    await page.waitForTimeout(150);
    const current = (await textbox.innerText().catch(() => '')) || '';
    if (!current.includes(prompt.slice(0, 40))) {
      await textbox.click();
      await page.keyboard.press(isMac ? 'Meta+A' : 'Control+A');
      await page.keyboard.press('Backspace');
      await textbox.type(prompt, { delay: 0 });
    }
    const send = page.locator(SELECTORS.sendButton).first();
    if (await send.isVisible().catch(() => false)) await send.click();
    else await page.keyboard.press('Enter');
  },

  async waitForCompletion(page, { timeout = 120000 } = {}) {
    // Stop-button-hidden is the primary signal; text-stability is the fallback
    // for when Gemini's aria-label-based selector drifts (see chatgpt.mjs).
    const stop = page.locator(SELECTORS.stopButton).first();
    try { await stop.waitFor({ state: 'visible', timeout: 5000 }); } catch {}

    const deadline = Date.now() + timeout;
    let lastLen = -1, stableTicks = 0;
    while (Date.now() < deadline) {
      const stopHidden = await stop.isHidden().catch(() => true);
      const ans = page.locator(SELECTORS.lastAnswer);
      const c = await ans.count().catch(() => 0);
      const text = c ? (await ans.nth(c - 1).innerText().catch(() => '')) : '';
      const len = text.length;

      if (stopHidden && len > 0) { await page.waitForTimeout(400); return; }
      if (len > 0 && len === lastLen) {
        stableTicks++;
        if (stableTicks >= 4) { await page.waitForTimeout(300); return; }
      } else {
        stableTicks = 0;
        lastLen = len;
      }
      await page.waitForTimeout(1500);
    }
    throw new Error(`Timed out after ${timeout}ms waiting for Gemini to finish responding`);
  },

  async extractResponse(page) {
    const ans = page.locator(SELECTORS.lastAnswer);
    const c = await ans.count();
    if (c === 0) return '';
    return (await ans.nth(c - 1).innerText()).trim();
  },
};
