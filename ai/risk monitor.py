def scan_transactions(transactions):

    suspicious = []

    for t in transactions:

        if t > 5000:

            suspicious.append(t)

    return suspicious
