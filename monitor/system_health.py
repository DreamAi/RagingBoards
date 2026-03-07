import psutil

def check():

    cpu = psutil.cpu_percent()

    if cpu > 90:
        print("High CPU detected")

    return cpu
