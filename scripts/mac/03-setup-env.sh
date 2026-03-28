#!/bin/bash

echo "⚙️ Setting up environment..."

if [ ! -f ".env" ]; then
  cp .env.example .env
  echo "✅ .env created"
else
  echo "ℹ️ .env already exists"
fi
