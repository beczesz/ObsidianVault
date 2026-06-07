# BDOS vault-indexing — status (Windows wrapper around launch.py)
$ErrorActionPreference = "Stop"
$dir = Split-Path -Parent $MyInvocation.MyCommand.Path
$py = (Get-Command python -ErrorAction SilentlyContinue).Source
if (-not $py) { $py = (Get-Command py -ErrorAction SilentlyContinue).Source }
if (-not $py) { Write-Error "Python not found on PATH."; exit 1 }
& $py (Join-Path $dir "launch.py") status
