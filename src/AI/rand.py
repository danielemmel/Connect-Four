import random


def choose_column(board, player_symbols, current_player):
    pos_choices = [i for i in range(0, 4) if -1 in board[:, i]]
    return random.choice(pos_choices)
