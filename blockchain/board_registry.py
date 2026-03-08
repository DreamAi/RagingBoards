import hashlib
import time

chain = []

def register_board(design):

    record = {

        "design":design,
        "time":time.time()

    }

    h = hashlib.sha256(str(record).encode()).hexdigest()

    chain.append(h)

    return h
