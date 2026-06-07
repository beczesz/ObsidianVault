# Launch wrapper for the dashboard server (Windows, under Task Scheduler).
# Loads CLAUDE_CODE_OAUTH_TOKEN (subscription, no API cost) from
# %USERPROFILE%\.bdos\anthropic.env so the Alfred Sonnet tier works headless.
# Single-instance guard on port 4321. Mirrors server-launch.sh (macOS).
$ErrorActionPreference = 'SilentlyContinue'
$dir = $PSScriptRoot

# Already running? (port 4321 listening) -> no-op (lets the 5-min supervisor be idempotent).
$listening = Get-NetTCPConnection -LocalPort 4321 -State Listen -ErrorAction SilentlyContinue
if ($listening) { exit 0 }

# Load ~/.bdos/anthropic.env (KEY=VALUE lines, '#' comments) into this process env.
$envFile = Join-Path $env:USERPROFILE ".bdos\anthropic.env"
if (Test-Path $envFile) {
  Get-Content $envFile | ForEach-Object {
    $line = $_.Trim()
    if ($line -and -not $line.StartsWith('#') -and $line.Contains('=')) {
      $parts = $line.Split('=', 2)
      [Environment]::SetEnvironmentVariable($parts[0].Trim(), $parts[1].Trim(), 'Process')
    }
  }
}

$node = (Get-Command node -ErrorAction SilentlyContinue).Source
if (-not $node) { $node = 'node' }
& $node (Join-Path $dir 'dash-server.mjs')
