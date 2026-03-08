class PatentAI:

    def check(self,design):

        keywords = [
            "concave",
            "hydrofoil",
            "thruster",
            "quad fin"
        ]

        matches = []

        for k in keywords:

            if k in design.lower():

                matches.append(k)

        return matches
