#!/usr/bin/python3

import numpy as np


def insert_into_board(column, board, symbol):
    for row in board[::-1]:
        if row[column] == -1:
            row[column] = symbol
            return


def check_board(board):
    # check both players
    for i in range(2):
        # check rows
        for row in board:
            if (row == i).sum() == 4:
                return i
        # check columns
        for j in range(board.shape[1]):
            if (board[:, j] == i).sum() == 4:
                return i
        # check diagonals
        if (np.diag(board) == i).sum() == 4 or (np.diag(np.fliplr(board)) == 0).sum() == 4:
            return i

    return -1
