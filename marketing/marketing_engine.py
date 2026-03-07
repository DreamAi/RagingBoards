import subprocess

agents = [

"marketing/campaign_manager.py"

]

def start():

    for a in agents:

        subprocess.Popen(["python",a])

if __name__ == "__main__":

    start()
