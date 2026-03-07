import psutil
import subprocess
import time

def server_running():

    for p in psutil.process_iter():

        if "uvicorn" in p.name().lower():

            return True

    return False

while True:

    if not server_running():

        subprocess.Popen([
            "python",
            "run_server.py"
        ])

    time.sleep(30)
