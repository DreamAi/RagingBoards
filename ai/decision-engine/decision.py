import subprocess
import json
import random

def get_system_metrics():
    return {
        "cpu": random.randint(10, 90),
        "errors": random.randint(0, 5),
        "users": random.randint(10, 1000)
    }

def should_update():
    metrics = get_system_metrics()

    if metrics["errors"] > 2:
        return True, "High error rate"

    if metrics["cpu"] > 80:
        return False, "System under load"

    if metrics["users"] < 50:
        return True, "Low usage, safe to update"

    return False, "Stable system"

def run_update():
    subprocess.run("powershell scripts/windows/ps/06-auto-update.ps1", shell=True)

if __name__ == "__main__":
    decision, reason = should_update()
    print(f"Decision: {decision} | Reason: {reason}")

    if decision:
        run_update()
