class SurfboardGenerator:

    def generate(self, prompt):

        prompt = prompt.lower()

        board = {}

        if "shortboard" in prompt:

            board["length"] = 6.2
            board["width"] = 19
            board["fins"] = "thruster"

        if "fish" in prompt:

            board["length"] = 5.6
            board["width"] = 21
            board["fins"] = "twin"

        if "gun" in prompt:

            board["length"] = 7.6
            board["width"] = 18
            board["fins"] = "thruster"

        return board
