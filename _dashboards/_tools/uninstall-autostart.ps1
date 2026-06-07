# Remove the dashboard-server Scheduled Task installed by install-autostart.ps1.
# After this the server no longer auto-starts; run start.ps1 manually.
$taskName = 'BDOS Dashboard Server'
Stop-ScheduledTask -TaskName $taskName -ErrorAction SilentlyContinue
Unregister-ScheduledTask -TaskName $taskName -Confirm:$false -ErrorAction SilentlyContinue
Write-Host "Removed scheduled task '$taskName'. (Any running server was left to exit on its own; close it via Task Manager if needed.)"
