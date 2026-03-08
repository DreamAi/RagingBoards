ALLOWED_IPS = ["127.0.0.1"]

def check_ip(ip):

    if ip in ALLOWED_IPS:
        return True

    return False
