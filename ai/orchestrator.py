import time
import subprocess

def run_all():
    print("🧠 AI SYSTEM RUNNING...")

    subprocess.run("python ai/decision-engine/decision.py", shell=True)
    subprocess.run("python ai/bug-fixer/fixer.py", shell=True)
    subprocess.run("python ai/revenue-engine/scaler.py", shell=True)

if __name__ == "__main__":
    while True:
        run_all()
        print("Sleeping 5 minutes...")
        time.sleep(300)
