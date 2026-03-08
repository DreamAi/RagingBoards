import numpy as np

class FraudAI:

    def detect(self,transactions):

        avg = np.mean(transactions)

        suspicious = []

        for t in transactions:

            if t > avg * 3:

                suspicious.append(t)

        return suspicious
