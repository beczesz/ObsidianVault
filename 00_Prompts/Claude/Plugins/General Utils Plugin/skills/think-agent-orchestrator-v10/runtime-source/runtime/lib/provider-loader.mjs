// Provider loader. Each provider is a single .mjs in providers/ that
// default-exports a provider definition object. The orchestrator passes the
// page and prompt; the provider implements the three actions.

import { readdir } from 'node:fs/promises';
import { fileURLToPath, pathToFileURL } from 'node:url';
import { dirname, join } from 'node:path';

const __dirname = dirname(fileURLToPath(import.meta.url));
const PROVIDERS_DIR = join(__dirname, '..', 'providers');

export async function listProviders() {
  const entries = await readdir(PROVIDERS_DIR);
  return entries
    .filter(f => f.endsWith('.mjs') && !f.startsWith('_'))
    .map(f => f.replace(/\.mjs$/, ''));
}

export async function loadProvider(name) {
  const safe = String(name).replace(/[^a-z0-9_-]/gi, '');
  const file = join(PROVIDERS_DIR, `${safe}.mjs`);
  const mod = await import(pathToFileURL(file).href);
  const provider = mod.default;
  validateProvider(provider, safe);
  return provider;
}

function validateProvider(p, name) {
  const required = ['name', 'urlPatterns', 'startUrl', 'submitPrompt', 'waitForCompletion', 'extractResponse'];
  for (const k of required) {
    if (p[k] === undefined || p[k] === null) {
      throw new Error(`Provider '${name}' missing required field: ${k}`);
    }
  }
  if (!Array.isArray(p.urlPatterns) || p.urlPatterns.length === 0) {
    throw new Error(`Provider '${name}' must define urlPatterns as a non-empty array of RegExp`);
  }
}
