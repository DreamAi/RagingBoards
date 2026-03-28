#!/bin/bash

echo "🔥 Raging Boards macOS Mega Installer"

chmod +x scripts/mac/*.sh

./scripts/mac/01-check-system.sh
./scripts/mac/02-install-deps.sh
./scripts/mac/03-setup-env.sh
./scripts/mac/04-install-project.sh
./scripts/mac/05-start-services.sh
./scripts/mac/06-run-migrations.sh
./scripts/mac/07-launch-app.sh

echo "🎉 INSTALL COMPLETE"
echo "👉 Visit: http://localhost:3000"
