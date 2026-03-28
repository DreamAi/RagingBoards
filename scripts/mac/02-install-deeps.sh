#!/bin/bash

echo "📦 Installing dependencies..."

brew update

brew install node
brew install docker
brew install docker-compose
brew install git

echo "🚀 Starting Docker..."
open /Applications/Docker.app

echo "⏳ Waiting for Docker to start..."
sleep 20

echo "✅ Dependencies installed"
