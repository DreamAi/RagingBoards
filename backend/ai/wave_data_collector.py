import random

def get_wave_conditions(surf_spot):

    # placeholder until live API connected

    return {
        "spot": surf_spot,
        "wave_height": random.uniform(1.0, 3.5),
        "swell_period": random.uniform(8, 16),
        "wind_speed": random.uniform(3, 18),
        "wind_direction": random.choice(["offshore","onshore","cross"])
    }
