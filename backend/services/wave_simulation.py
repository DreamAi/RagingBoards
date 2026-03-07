import numpy as np

def simulate_wave(board_length):

    wave_speed = 12

    stability = np.tanh(board_length/7)

    return {
        "wave_speed":wave_speed,
        "stability":stability
    }
