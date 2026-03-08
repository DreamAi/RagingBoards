import os

def scan():

    issues = []

    for root,dirs,files in os.walk("."):

        for f in files:

            if f.endswith(".py"):

                path = os.path.join(root,f)

                with open(path) as file:

                    if "TODO" in file.read():

                        issues.append(path)

    return issues

if __name__ == "__main__":

    print("AI Auditor running")

    print(scan())
