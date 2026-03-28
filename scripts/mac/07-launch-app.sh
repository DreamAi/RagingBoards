#!/bin/bash

echo "🚀 Launching Raging Boards..."

npm run dev &

sleep 5

echo "🌐 Opening browser..."

open http://localhost:3000

echo "✅ Platform live"
