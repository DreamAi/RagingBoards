import subprocess

def restart(service):

    subprocess.run(["docker","restart",service])
