import random

def generate_shape():

    shapes = [
        "shortboard",
        "fish",
        "longboard",
        "hybrid"
    ]

    length = random.uniform(5.5,9.5)

    return {
        "shape":random.choice(shapes),
        "length":length,
        "width":random.uniform(18,23)
    }
