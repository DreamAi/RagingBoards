import os
import subprocess
import sys

def run(cmd):
    print(f"Running: {cmd}")
    subprocess.call(cmd, shell=True)

def check_python():

    if sys.version_info < (3,9):
        print("Python 3.9+ required")
        sys.exit()

def install_dependencies():

    run("pip install -r requirements.txt")

def start_server():

    run("python run_server.py")

def start_ai():

    run("python ai/supervisor.py &")

def main():

    print("Installing Raging Boards Platform")

    check_python()

    install_dependencies()

    start_ai()

    start_server()

if __name__ == "__main__":
    main()
