import random


def choose_column(board, symbol):
    pos_choices = [i for i in range(0, 4) if -1 in board[:, i]]
    return random.choice(pos_choices)
