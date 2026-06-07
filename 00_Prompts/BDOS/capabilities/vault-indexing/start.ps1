# BDOS vault-indexing — start (Windows wrapper around launch.py)
# This is the SECONDARY machine: --no-scheduler keeps the cron scheduler off so
# scheduled jobs don't double-fire (the Mac currently owns the scheduler).
# To make THIS machine the scheduler owner, delete the --no-scheduler argument.
$ErrorActionPreference = "Stop"
$dir = Split-Path -Parent $MyInvocation.MyCommand.Path
$py = (Get-Command python -ErrorAction SilentlyContinue).Source
if (-not $py) { $py = (Get-Command py -ErrorAction SilentlyContinue).Source }
if (-not $py) { Write-Error "Python not found on PATH."; exit 1 }
& $py (Join-Path $dir "launch.py") start --no-scheduler
