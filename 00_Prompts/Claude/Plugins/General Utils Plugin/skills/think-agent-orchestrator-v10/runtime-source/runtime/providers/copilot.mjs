// Microsoft 365 Copilot provider. Last tested: 2026-05-26 — UNVERIFIED.
// The M365 Copilot lives at m365.cloud.microsoft/chat and is iframe-heavy.
// You may need to use page.frameLocator() for the textbox.

const SELECTORS = {
  textbox: 'textarea[placeholder*="Ask" i], div[contenteditable="true"][role="textbox"]',
  sendButton: 'button[aria-label*="Send" i], button[aria-label*="Submit" i]',
  stopButton: 'button[aria-label*="Stop" i]',
  lastAnswer: '[data-testid="assistant-message"]:last-of-type, [role="region"]:last-of-type',
  loginButton: 'button:has-text("Sign in"), a:has-text("Sign in")',
};

export default {
  name: 'copilot',
  urlPatterns: [/m365\.cloud\.microsoft/, /copilot\.microsoft\.com/, /copilot\.cloud\.microsoft/],
  startUrl: 'https://m365.cloud.microsoft/chat',

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
    await page.waitForTimeout(200);
    const current = (await textbox.innerText().catch(() => '')) || (await textbox.inputValue().catch(() => '')) || '';
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

  async waitForCompletion(page, { timeout = 180000 } = {}) {
    const stop = page.locator(SELECTORS.stopButton).first();
    try { await stop.waitFor({ state: 'visible', timeout: 8000 }); } catch {}
    await stop.waitFor({ state: 'hidden', timeout });
    await page.waitForTimeout(500);
  },

  async extractResponse(page) {
    const ans = page.locator(SELECTORS.lastAnswer);
    const c = await ans.count();
    if (c === 0) return '';
    return (await ans.nth(c - 1).innerText()).trim();
  },
};
