#!/usr/bin/env bash
# Rebuilds the dashboard data from the office files.
cd "$(dirname "$0")/.." && python3 scripts/refresh_dashboard.py
