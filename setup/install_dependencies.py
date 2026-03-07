import shutil
import subprocess

def check(cmd):
    return shutil.which(cmd) is not None

if not check("node"):
    subprocess.run("sudo apt install nodejs npm -y", shell=True)

if not check("pip"):
    subprocess.run("sudo apt install python3-pip -y", shell=True)

if not check("docker"):
    subprocess.run("sudo apt install docker.io -y", shell=True)
