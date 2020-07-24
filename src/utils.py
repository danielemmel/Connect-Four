#!/usr/bin/python3


def pretty_print(board, player_symbols):
    s = ""
    for i in range(board.shape[0]):
        for j in range(board.shape[1]):
            s += player_symbols[board[i, j]]
            s += '|'
        s += '\n'
    print(s)
