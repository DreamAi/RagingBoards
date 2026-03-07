import random

topics = [

"AI surfboard design",
"custom surfboard graphics",
"surfboard performance prediction",
"AI surfboard innovation",
"surfboard design studio"

]

templates = [

"Raging Boards lets surfers design their own boards using AI tools.",
"Design surfboards visually with Raging Boards and export to shapers.",
"Raging Boards is building a digital design studio for surfboards.",
"Create surfboard graphics and layouts in the Raging Boards studio."

]

def generate_post():

    topic = random.choice(topics)

    template = random.choice(templates)

    return f"{template} Learn more about {topic} at Raging Boards."
