# Rebuilds the dashboard data from the office files.
Set-Location (Split-Path -Parent $PSScriptRoot)
python scripts\refresh_dashboard.py
