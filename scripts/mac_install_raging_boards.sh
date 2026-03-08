#!/bin/bash

echo "======================================="
echo "RAGING BOARDS PLATFORM - MAC INSTALLER"
echo "======================================="

sleep 2

# -------------------------
# Detect OS
# -------------------------

OS="$(uname)"

if [[ "$OS" != "Darwin" ]]; then
  echo "This installer is for macOS only."
  exit 1
fi

echo "macOS detected"

# -------------------------
# Install Homebrew
# -------------------------

if ! command -v brew &> /dev/null
then
    echo "Installing Homebrew..."

    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

    echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile
    eval "$(/opt/homebrew/bin/brew shellenv)"

else
    echo "Homebrew already installed"
fi

# -------------------------
# Install Python
# -------------------------

if ! command -v python3 &> /dev/null
then
    echo "Installing Python"
    brew install python
else
    echo "Python detected"
fi

# -------------------------
# Install pip
# -------------------------

if ! command -v pip3 &> /dev/null
then
    echo "Installing pip"
    python3 -m ensurepip
else
    echo "pip detected"
fi

# -------------------------
# Install Node
# -------------------------

if ! command -v node &> /dev/null
then
    echo "Installing Node.js"
    brew install node
else
    echo "Node detected"
fi

# -------------------------
# Install npm
# -------------------------

if ! command -v npm &> /dev/null
then
    echo "Installing npm"
    brew install npm
else
    echo "npm detected"
fi

# -------------------------
# Install Docker
# -------------------------

if ! command -v docker &> /dev/null
then
    echo "Installing Docker"

    brew install --cask docker

    echo "Please start Docker Desktop once after installation."
else
    echo "Docker detected"
fi

# -------------------------
# Install Netlify CLI
# -------------------------

if ! command -v netlify &> /dev/null
then
    echo "Installing Netlify CLI"
    npm install -g netlify-cli
fi

# -------------------------
# Install backend deps
# -------------------------

echo "Installing backend dependencies"

pip3 install -r backend/requirements.txt

# -------------------------
# Install frontend deps
# -------------------------

echo "Installing frontend dependencies"

cd frontend
npm install
cd ..

# -------------------------
# Build Docker
# -------------------------

echo "Building Docker environment"

docker-compose build

echo "Starting containers"

docker-compose up -d

# -------------------------
# Start AI monitor
# -------------------------

echo "Launching AI monitoring"

python3 monitoring/self_healing.py &

# -------------------------
# Create Oracle deploy script
# -------------------------

mkdir -p deploy

cat <<EOF > deploy/oracle_cloud_deploy.sh
#!/bin/bash

echo "Oracle Cloud deployment started"

sudo apt update

sudo apt install docker docker-compose git nodejs npm python3 python3-pip -y

git clone https://github.com/YOUR_USERNAME/raging-boards

cd raging-boards

docker-compose build

docker-compose up -d

echo "Raging Boards running"
EOF

chmod +x deploy/oracle_cloud_deploy.sh

# -------------------------
# Create Netlify deploy script
# -------------------------

cat <<EOF > deploy/netlify_deploy.sh
#!/bin/bash

echo "Deploying frontend to Netlify"

cd frontend

npm run build

netlify deploy --prod
EOF

chmod +x deploy/netlify_deploy.sh

# -------------------------
# Launch platform
# -------------------------

echo "======================================="
echo "RAGING BOARDS PLATFORM RUNNING"
echo "======================================="

echo ""
echo "Frontend:"
echo "http://localhost:3000"

echo ""
echo "Backend:"
echo "http://localhost:5000"

echo ""
echo "AI Operations Center:"
echo "http://localhost:3000/operations"

echo ""
echo "To deploy:"
echo ""
echo "Oracle:"
echo "deploy/oracle_cloud_deploy.sh"
echo ""
echo "Netlify:"
echo "deploy/netlify_deploy.sh"
echo ""

echo "Setup complete"
