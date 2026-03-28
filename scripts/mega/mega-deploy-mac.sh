#!/bin/bash

echo "🔥 RAGING BOARDS FULL MEGA DEPLOY (macOS)"

chmod +x scripts/mac/*.sh

./scripts/mac/step-1-system.sh
./scripts/mac/step-2-deps.sh
./scripts/mac/step-3-env.sh
./scripts/mac/step-4-build.sh
./scripts/mac/step-5-docker.sh
./scripts/mac/step-6-db.sh
./scripts/mac/step-7-run.sh

echo "🎉 FULL PLATFORM LIVE"
echo "🌐 http://localhost:3000"
