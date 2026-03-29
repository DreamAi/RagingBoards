import subprocess
import re

def run_tests():
    result = subprocess.run("pytest", shell=True, capture_output=True, text=True)
    return result.stdout

def detect_errors(log):
    errors = re.findall(r"Error.*", log)
    return errors

def auto_fix():
    log = run_tests()
    errors = detect_errors(log)

    if not errors:
        print("No bugs found")
        return

    print("Fixing errors...")

    for err in errors:
        print(f"Detected: {err}")
        # simple auto-fix logic example
        if "import" in err:
            subprocess.run("pip install -r requirements.txt", shell=True)

    subprocess.run("git add .", shell=True)
    subprocess.run('git commit -m "AI auto-fix"', shell=True)
    subprocess.run("git push", shell=True)

if __name__ == "__main__":
    auto_fix()
