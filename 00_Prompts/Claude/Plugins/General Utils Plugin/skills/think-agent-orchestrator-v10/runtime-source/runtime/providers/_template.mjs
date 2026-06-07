// Template for adding a new browser-based AI provider.
// Copy this file to providers/<name>.mjs and fill in.
//
// The orchestrator drives this contract:
//   1. Browser is attached / launched (see lib/browser.mjs)
//   2. findOrOpenProviderPage(ctx, provider, {mode}) returns a `page`
//   3. await provider.submitPrompt(page, prompt)
//   4. await provider.waitForCompletion(page, {timeout})
//   5. text = await provider.extractResponse(page)
//
// Helpers you can use from playwright:
//   page.getByRole('textbox', { name: /message/i })
//   page.getByRole('button', { name: /send|stop/i })
//   page.locator('css=selector >>> shadow-piercing')
//   page.waitForFunction(predicate, { timeout })

export default {
  name: 'template',

  // Tabs whose URL matches any of these will be considered "this provider".
  urlPatterns: [/example\.com/],

  // Used when opening a new tab (mode=new) or when no matching tab is found.
  startUrl: 'https://example.com/',

  // Optional: detect login state. Return true if logged in.
  async loginCheck(page) {
    return true;
  },

  // REQUIRED: paste/type the prompt and submit.
  async submitPrompt(page, prompt) {
    throw new Error('submitPrompt not implemented');
  },

  // REQUIRED: wait until the response is fully rendered.
  // Resolve when done; throw on timeout.
  async waitForCompletion(page, { timeout = 120000 } = {}) {
    throw new Error('waitForCompletion not implemented');
  },

  // REQUIRED: return the response text (string).
  async extractResponse(page) {
    throw new Error('extractResponse not implemented');
  },
};
