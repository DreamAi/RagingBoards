from wave_data_collector import get_wave_conditions
from surfboard_optimizer import optimize_board

def create_board_for_spot(surf_spot):

    wave = get_wave_conditions(surf_spot)

    board = optimize_board(wave)

    return {
        "wave_conditions": wave,
        "recommended_board": board
    }
