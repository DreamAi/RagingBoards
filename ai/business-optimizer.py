import time
import subprocess

agents = [

"ai/auditor_agent.py",
"ai/optimizer_agent.py",
"ai/self_heal.py",
"marketing/marketing_engine.py"

]

def manage():

    for agent in agents:

        subprocess.Popen(["python",agent])

while True:

    manage()

    time.sleep(3600)
