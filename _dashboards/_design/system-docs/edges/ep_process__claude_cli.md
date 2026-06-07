---
from: ep_process
to: claude_cli
protocol: spawn (subprocess)
direction: server → subprocess
payload: CLI arguments + stdin
label: Tier-1 subprocess
id: a5cd6b56-3279-444f-943b-93cc414f31c0
index_schema_version: 1
---

## Kapcsolat

Az `/api/alfred/process` REST handler a Node.js `child_process.spawn()`-nal
indít egy `claude` subprocess-t. A prompt szöveg a subprocess stdin-jén
vagy CLI argumentumként érkezik. A subprocess a Claude Code subscription
OAuth tokennel fut, Sonnet modellel, csak read-only tool-okkal.

## Spawn paraméterek (kivonatos)

```js
const proc = spawn('claude', [
  '--model', 'claude-sonnet-4-6',
  '--tools', 'Read,Glob,Grep',
  '--no-write',
  '--output-format', 'json',
  '--message', prompt
], {
  env: { ...process.env, CLAUDE_CODE_OAUTH_TOKEN: oauthToken },
  timeout: 30000
});
```

## Kimenet parse

```js
proc.stdout.on('data', chunk => output += chunk);
proc.on('close', code => {
  if (code !== 0) return activateFallback('claude_cli_error');
  const result = JSON.parse(output);
  // result.content[0].text → assistant response
});
proc.on('error', () => activateFallback('spawn_failed'));
```

## Timeout kezelés

Ha a subprocess 30 másodpercen belül nem fejezi be, a handler kilövi (`proc.kill()`)
és Haiku fallback-re vált. Ez általában hálózati probléma vagy rate limit esetén fordul elő.

## Biztonsági megjegyzés

A `--no-write` flag és a tools whitelist (`Read,Glob,Grep`) garantálják,
hogy a subprocess nem módosíthat semmit a vaultban — csak olvashat.
