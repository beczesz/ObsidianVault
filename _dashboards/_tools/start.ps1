# Start the Ideas Vault dashboard server (Windows, PowerShell).
# Usage:  right-click > Run with PowerShell,  or:  ./start.ps1
$ErrorActionPreference = "Stop"
$here = Split-Path -Parent $MyInvocation.MyCommand.Path
Write-Host "Starting Ideas Vault dashboard server..." -ForegroundColor Cyan
node (Join-Path $here "dash-server.mjs")
