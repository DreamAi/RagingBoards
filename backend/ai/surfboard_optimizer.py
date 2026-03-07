def optimize_board(wave):

    height = wave["wave_height"]
    period = wave["swell_period"]

    if height < 1.5:
        board_type = "Fish"
        length = 5.6

    elif height < 2.5:
        board_type = "Shortboard"
        length = 6.2

    else:
        board_type = "Step Up"
        length = 6.8

    rocker = "medium"

    if period > 12:
        rocker = "high"

    fins = "thruster"

    return {
        "type": board_type,
        "length": length,
        "rocker": rocker,
        "fin_setup": fins
    }
