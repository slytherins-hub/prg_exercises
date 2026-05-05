#!/usr/bin/env bash
# install-node-and-gemini-user.sh
# Nainstaluje pevně danou Node.js LTS verzi do ~/.local/nodejs bez sudo,
# přidá ji do PATH (zsh/bash rc) a hned doinstaluje Gemini CLI (@google/gemini-cli) globálně.
#
# Spuštění (macOS / Linux Terminal):
#   curl -fsSL https://gist.githubusercontent.com/tomasvicar/00b7135377088268667fbcd5f04dea14/raw/install-node-and-gemini-user.sh | bash
#
# Po dokončení otevři NOVÝ terminál a spusť:
#   gemini

set -euo pipefail

VER="v24.15.0"
DEST="$HOME/.local/nodejs"

OS="$(uname -s)"
case "$OS" in
  Darwin) NODE_OS="darwin" ;;
  Linux)  NODE_OS="linux" ;;
  *) echo "Nepodporovaný OS: $OS"; exit 1 ;;
esac

ARCH="$(uname -m)"
case "$ARCH" in
  arm64|aarch64) NODE_ARCH="arm64" ;;
  x86_64|amd64)  NODE_ARCH="x64" ;;
  *) echo "Nepodporovaná architektura: $ARCH"; exit 1 ;;
esac

TARBALL="node-${VER}-${NODE_OS}-${NODE_ARCH}.tar.gz"
URL="https://nodejs.org/dist/${VER}/${TARBALL}"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

echo "Instaluji Node.js ${VER} (${NODE_OS}-${NODE_ARCH})"
echo "Stahuji ${URL} ..."
curl -fsSL "${URL}" -o "${TMP}/${TARBALL}"

if [ -d "$DEST" ]; then
  echo "Mažu starou instalaci v $DEST ..."
  rm -rf "$DEST"
fi

mkdir -p "$DEST"
tar -xzf "${TMP}/${TARBALL}" -C "$DEST" --strip-components=1

# Přidání do PATH ve shell rc (zsh defaultní na macOS, jinak bash)
SHELL_NAME="$(basename "${SHELL:-/bin/bash}")"
case "$SHELL_NAME" in
  zsh)  SHELL_RC="$HOME/.zshrc" ;;
  bash) SHELL_RC="$HOME/.bashrc" ;;
  *)    SHELL_RC="$HOME/.profile" ;;
esac

PATH_LINE="export PATH=\"$DEST/bin:\$PATH\""
touch "$SHELL_RC"
if ! grep -Fqx "$PATH_LINE" "$SHELL_RC"; then
  printf '\n# Node.js (install-node-and-gemini-user.sh)\n%s\n' "$PATH_LINE" >> "$SHELL_RC"
fi

# PATH pro aktuální proces, aby šel hned spustit npm
export PATH="$DEST/bin:$PATH"

echo ""
echo "Node.js ${VER} nainstalován v $DEST"
echo "Instaluji Gemini CLI (@google/gemini-cli) ..."

npm install -g @google/gemini-cli

echo ""
echo "=============================================="
echo " Hotovo! Node.js ${VER} + Gemini CLI nainstalovány."
echo " Otevři NOVÝ terminál a spusť:"
echo "   gemini"
echo " Při prvním spuštění zvol 'Sign in with Google'."
echo "=============================================="
