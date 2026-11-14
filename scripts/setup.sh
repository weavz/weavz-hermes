#!/usr/bin/env bash
set -euo pipefail
root="$(cd "$(dirname "$0")/.." && pwd)"
cd "$root"
mkdir -p .local/hermes
export HERMES_HOME="$root/.local/hermes"
hermes mcp add weavz --url https://platform.weavz.io/mcp/weavz --auth oauth
hermes mcp list
hermes mcp test weavz
echo "Complete Weavz OAuth in the browser. This isolated profile lives under .local/hermes."
