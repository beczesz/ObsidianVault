#!/usr/bin/env bash
# Think Engine v0.10 — one-shot setup
# Idempotent: safe to re-run. Installs Playwright + Chromium browser.

set -e
cd "$(dirname "$0")"

echo "Think Engine setup starting..."
echo "Location: $(pwd)"
echo ""

# 1. npm install (Playwright)
if [ ! -d "node_modules/playwright" ]; then
  echo "[1/2] Installing Playwright (~50MB)..."
  npm install --no-audit --no-fund --loglevel=error
else
  echo "[1/2] Playwright already installed."
fi

# 2. Chromium browser binary
# Playwright bundles its own Chromium, but you can also reuse system Chrome.
# For default-profile reuse we'll use system Chrome (PLAYWRIGHT_CHROMIUM_CHANNEL=chrome),
# so we DON'T need to download Playwright's bundled Chromium.
# If user wants bundled Chromium: PLAYWRIGHT_BUNDLED=1 ./setup.sh
if [ "$PLAYWRIGHT_BUNDLED" = "1" ]; then
  echo "[2/2] Installing Playwright bundled Chromium (~200MB)..."
  npx playwright install chromium
else
  echo "[2/2] Skipping bundled Chromium — will use system Chrome instead."
  echo "      (Set PLAYWRIGHT_BUNDLED=1 to download bundled Chromium too.)"
fi

# 3. Stamp version
echo "0.10.0" > version

echo ""
echo "✓ Think Engine ready."
echo "  Test: node runtime/orchestrator.mjs --healthcheck"
