# Install a Scheduled Task so the Ideas Vault dashboard server (dash-server.mjs,
# port 4321) starts at logon and self-restarts (5-minute supervisor). Windows
# equivalent of install-autostart.sh. Reversible with uninstall-autostart.ps1.
$ErrorActionPreference = 'Stop'
$dir = $PSScriptRoot
$wrapper = Join-Path $dir 'server-launch.ps1'
$taskName = 'BDOS Dashboard Server'

# Seed the token file (chmod-equivalent: user profile, not in the synced vault).
$bdos = Join-Path $env:USERPROFILE '.bdos'
$envFile = Join-Path $bdos 'anthropic.env'
if (-not (Test-Path $bdos)) { New-Item -ItemType Directory -Path $bdos | Out-Null }
if (-not (Test-Path $envFile)) {
@'
# Alfred / dashboard-server auth (Windows, headless Task Scheduler context).
# Use your Claude SUBSCRIPTION token (no API cost):
#   1) In a terminal:  claude setup-token   (requires your Claude subscription)
#   2) Uncomment + paste below:
# CLAUDE_CODE_OAUTH_TOKEN=
#   3) Re-run this task:  Start-ScheduledTask -TaskName "BDOS Dashboard Server"
# (Optional metered-API alternative:)
# ANTHROPIC_API_KEY=sk-ant-api03-REPLACE_ME
'@ | Set-Content -Path $envFile -Encoding utf8
  Write-Host "Created token file: $envFile"
}

# Port-4321 deduplication is handled by server-launch.ps1 (it exits if already
# listening) plus -MultipleInstances IgnoreNew, so no manual node-kill is needed.

$psExe = "$env:SystemRoot\System32\WindowsPowerShell\v1.0\powershell.exe"
$action = New-ScheduledTaskAction -Execute $psExe `
  -Argument "-NoProfile -WindowStyle Hidden -ExecutionPolicy Bypass -File `"$wrapper`""
$trigLogon  = New-ScheduledTaskTrigger -AtLogOn
$trigRepeat = New-ScheduledTaskTrigger -Once -At (Get-Date) `
  -RepetitionInterval (New-TimeSpan -Minutes 5)
$settings = New-ScheduledTaskSettingsSet -StartWhenAvailable `
  -MultipleInstances IgnoreNew -ExecutionTimeLimit ([TimeSpan]::Zero) -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries
$principal = New-ScheduledTaskPrincipal -UserId $env:USERNAME -LogonType Interactive -RunLevel Limited

Register-ScheduledTask -TaskName $taskName -Action $action `
  -Trigger $trigLogon, $trigRepeat -Settings $settings -Principal $principal -Force | Out-Null
Start-ScheduledTask -TaskName $taskName

Start-Sleep -Seconds 3
Write-Host ""
if (Get-NetTCPConnection -LocalPort 4321 -State Listen -ErrorAction SilentlyContinue) {
  Write-Host "OK - dashboard server is up at http://localhost:4321/ and will auto-start at logon."
} else {
  Write-Host "Task registered; server not listening yet. It retries every 5 min. Check Task Scheduler '$taskName'."
}
Write-Host "Set your subscription token: run 'claude setup-token', paste CLAUDE_CODE_OAUTH_TOKEN into $envFile, then: Start-ScheduledTask -TaskName '$taskName'"
Write-Host "To remove: powershell -ExecutionPolicy Bypass -File `"$dir\uninstall-autostart.ps1`""
