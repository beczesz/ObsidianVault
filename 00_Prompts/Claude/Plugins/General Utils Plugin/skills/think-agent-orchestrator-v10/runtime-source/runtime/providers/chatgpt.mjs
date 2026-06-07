// ChatGPT provider. Targets chatgpt.com (and the legacy chat.openai.com).
//
// Selectors strategy: prefer ARIA role + accessible name (resilient across
// UI redesigns), fall back to data attributes that have been stable for
// 1+ year. Plain CSS class selectors are AVOIDED.
//
// Last tested: 2026-05-26.

const SELECTORS = {
  // The composer textarea. ChatGPT uses a contenteditable div with role=textbox
  // and aria-label that varies by locale.
  textbox: 'div[contenteditable="true"][role="textbox"], textarea#prompt-textarea',

  // The "Send message" button. While streaming, it changes to "Stop generating".
  sendButton: 'button[data-testid="send-button"]',
  stopButton: 'button[data-testid="stop-button"]',

  // Each assistant message has a stable data-message-author-role attribute.
  assistantMessage: 'div[data-message-author-role="assistant"]',

  // Login indicators.
  loginButton: 'button:has-text("Log in"), a:has-text("Log in")',
};

export default {
  name: 'chatgpt',

  urlPatterns: [/^https?:\/\/(www\.)?chatgpt\.com\//, /^https?:\/\/chat\.openai\.com\//],

  startUrl: 'https://chatgpt.com/',

  async loginCheck(page) {
    const loginPresent = await page.locator(SELECTORS.loginButton).first().isVisible().catch(() => false);
    return !loginPresent;
  },

  async submitPrompt(page, prompt) {
    // Wait for the composer to be ready
    const textbox = page.locator(SELECTORS.textbox).first();
    await textbox.waitFor({ state: 'visible', timeout: 30000 });
    await textbox.click();

    // Paste via clipboard for reliability vs. keystroke-by-keystroke (which
    // can race with SPA re-renders on long prompts).
    await page.evaluate(async (text) => {
      await navigator.clipboard.writeText(text);
    }, prompt).catch(() => { /* clipboard write may need a focused doc; we fall back below */ });

    // Try clipboard paste first (Ctrl/Cmd+V); if that doesn't populate, fall back to typing.
    const isMac = process.platform === 'darwin';
    const pasteCombo = isMac ? 'Meta+V' : 'Control+V';
    await textbox.press(pasteCombo);

    // Verify content arrived; if empty, fall back to direct fill/type.
    await page.waitForTimeout(150);
    const currentText = (await textbox.innerText().catch(() => '')) || '';
    if (!currentText.includes(prompt.slice(0, 40))) {
      // Fallback: clear and type (slower but always works)
      await textbox.click();
      await page.keyboard.press(isMac ? 'Meta+A' : 'Control+A');
      await page.keyboard.press('Backspace');
      await textbox.type(prompt, { delay: 0 });
    }

    // Submit
    const sendBtn = page.locator(SELECTORS.sendButton).first();
    if (await sendBtn.isVisible().catch(() => false)) {
      await sendBtn.click();
    } else {
      await page.keyboard.press('Enter');
    }
  },

  async waitForCompletion(page, { timeout = 120000 } = {}) {
    // Primary signal: the stop-button disappears when generation ends. But that
    // button's data-testid has drifted before, leaving the locator stuck "visible"
    // forever. So we also run a text-stability fallback: once the last assistant
    // message stops growing for a few consecutive polls, treat it as done.
    const stop = page.locator(SELECTORS.stopButton).first();
    try {
      await stop.waitFor({ state: 'visible', timeout: 5000 });
    } catch {
      // Response may have been fast enough that we never saw the stop button.
    }

    const deadline = Date.now() + timeout;
    let lastLen = -1, stableTicks = 0;
    while (Date.now() < deadline) {
      const stopHidden = await stop.isHidden().catch(() => true);
      const msgs = page.locator(SELECTORS.assistantMessage);
      const n = await msgs.count().catch(() => 0);
      const text = n ? (await msgs.nth(n - 1).innerText().catch(() => '')) : '';
      const len = text.length;

      if (stopHidden && len > 0) {
        // Confirm with one short settle: the canonical "done" state.
        await page.waitForTimeout(400);
        return;
      }
      // Fallback: text has not grown for ~6s and we have content.
      if (len > 0 && len === lastLen) {
        stableTicks++;
        if (stableTicks >= 4) { await page.waitForTimeout(300); return; }
      } else {
        stableTicks = 0;
        lastLen = len;
      }
      await page.waitForTimeout(1500);
    }
    throw new Error(`Timed out after ${timeout}ms waiting for ChatGPT to finish responding`);
  },

  async extractResponse(page) {
    const messages = page.locator(SELECTORS.assistantMessage);
    const count = await messages.count();
    if (count === 0) return '';
    const last = messages.nth(count - 1);
    // innerText gives a clean rendered text; if you need markdown, use innerHTML and post-process.
    return (await last.innerText()).trim();
  },
};
