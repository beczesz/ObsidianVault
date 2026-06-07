// Claude (claude.ai) provider. Pattern mirrors chatgpt.mjs.
// Last tested: 2026-05-26 — verify selectors before relying on this.

const SELECTORS = {
  textbox: 'div[contenteditable="true"][role="textbox"]',
  sendButton: 'button[aria-label="Send message" i], button[aria-label*="Send" i]',
  stopButton: 'button[aria-label*="Stop" i]',
  assistantMessage: 'div[data-is-streaming], [data-testid*="assistant"], div.font-claude-message',
  loginButton: 'button:has-text("Log in"), a:has-text("Log in")',
};

export default {
  name: 'claude',
  urlPatterns: [/^https?:\/\/(www\.)?claude\.ai\//],
  startUrl: 'https://claude.ai/new',

  async loginCheck(page) {
    return !(await page.locator(SELECTORS.loginButton).first().isVisible().catch(() => false));
  },

  async submitPrompt(page, prompt) {
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
    const stop = page.locator(SELECTORS.stopButton).first();
    try { await stop.waitFor({ state: 'visible', timeout: 5000 }); } catch {}
    await stop.waitFor({ state: 'hidden', timeout });
    await page.waitForTimeout(400);
  },

  async extractResponse(page) {
    const msgs = page.locator(SELECTORS.assistantMessage);
    const count = await msgs.count();
    if (count === 0) return '';
    return (await msgs.nth(count - 1).innerText()).trim();
  },
};
