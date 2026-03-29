# ai/watchdog.py
import time

while True:
    try:
        subprocess.run("python ai/orchestrator.py", shell=True)
    except:
        print("System crashed → restarting...")
    time.sleep(10)
