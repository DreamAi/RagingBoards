import subprocess
import platform
import shutil
import sys

print("===================================")
print("RAGING BOARDS AI PLATFORM INSTALLER")
print("===================================")

system = platform.system()

print("Detected OS:", system)


def command_exists(cmd):
    return shutil.which(cmd) is not None


def run(cmd):
    subprocess.run(cmd, shell=True)


# ----------------------------
# Python check
# ----------------------------

if not command_exists("python3"):
    print("Python3 not found")
    if system == "Windows":
        print("Please install Python from python.org")
        sys.exit()
    else:
        run("sudo apt install python3 -y")

# ----------------------------
# pip check
# ----------------------------

if not command_exists("pip3"):
    print("Installing pip")
    if system == "Linux":
        run("sudo apt install python3-pip -y")
    elif system == "Darwin":
        run("python3 -m ensurepip")
    else:
        print("Install pip manually")

# ----------------------------
# Node check
# ----------------------------

if not command_exists("node"):
    print("Installing Node")

    if system == "Linux":
        run("sudo apt install nodejs npm -y")

    elif system == "Darwin":
        run("brew install node")

    elif system == "Windows":
        print("Please install Node from nodejs.org")

# ----------------------------
# Docker check
# ----------------------------

if not command_exists("docker"):
    print("Installing Docker")

    if system == "Linux":
        run("sudo apt install docker.io docker-compose -y")

    elif system == "Darwin":
        print("Install Docker Desktop")

    elif system == "Windows":
        print("Install Docker Desktop")

# ----------------------------
# Install backend
# ----------------------------

print("Installing backend dependencies")

run("pip3 install -r backend/requirements.txt")

# ----------------------------
# Install frontend
# ----------------------------

print("Installing frontend dependencies")

run("cd frontend && npm install")

# ----------------------------
# Build docker containers
# ----------------------------

print("Building docker environment")

run("docker-compose build")

print("Starting containers")

run("docker-compose up -d")

# ----------------------------
# Start AI monitor
# ----------------------------

run("python3 monitoring/self_healing.py &")

print("Installation complete")
print("Backend running on port 5000")
print("Frontend running on port 3000")
