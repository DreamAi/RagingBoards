import subprocess
import time

agents = [

"ai/auditor_agent.py",
"ai/optimizer_agent.py",
"ai/self_heal.py",
"marketing/marketing_engine.py"

]

while True:

    for agent in agents:

        subprocess.Popen(["python", agent])

    time.sleep(3600)
