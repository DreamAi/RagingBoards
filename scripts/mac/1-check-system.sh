#!/bin/bash

echo "🔍 Checking macOS system..."

if [[ "$OSTYPE" != "darwin"* ]]; then
  echo "❌ This script is for macOS only"
  exit 1
fi

echo "✅ macOS detected"

# Check Homebrew
if ! command -v brew &> /dev/null
then
  echo "⚠️ Homebrew not found. Installing..."
  /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
fi

echo "✅ System check complete"
