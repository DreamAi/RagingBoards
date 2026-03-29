import json
import subprocess

REVENUE_FILE = "data/revenue.json"

def get_revenue():
    try:
        with open(REVENUE_FILE) as f:
            data = json.load(f)
            return data.get("revenue", 0)
    except:
        return 0

def scale_system(revenue):
    if revenue > 1000:
        print("Scaling to medium tier...")
        subprocess.run("kubectl scale deployment raging-app --replicas=3", shell=True)

    if revenue > 10000:
        print("Scaling to high tier...")
        subprocess.run("kubectl scale deployment raging-app --replicas=6", shell=True)

    if revenue > 50000:
        print("Scaling to enterprise tier...")
        subprocess.run("kubectl scale deployment raging-app --replicas=10", shell=True)

if __name__ == "__main__":
    revenue = get_revenue()
    print(f"Revenue: {revenue}")
    scale_system(revenue)
