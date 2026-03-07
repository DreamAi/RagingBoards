#!/bin/bash

echo "Installing Raging Boards Platform"

python3 setup/detect_os.py
python3 setup/install_dependencies.py
python3 setup/verify_environment.py

pip install -r backend/requirements.txt

cd frontend
npm install
cd ..

docker-compose up -d

python3 monitoring/ai_manager.py &

echo "Platform running"
