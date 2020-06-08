import time

import numpy as np


def pretty_print(board, player_symbols):
    s = ""
    for i in range(board.shape[0]):
        for j in range(board.shape[1]):
            s += player_symbols[board[i,j]]
            s += '|'
        s += '\n'
    print(s)


def get_input(board):
    try:
        inp = int(input()) - 1
        if inp in range(0, 4) and -1 in board[:, inp]:
            return inp
        else:
            print('Input must be a non-full column between 1 and 4!')
            return get_input(board)
    except ValueError:
        print('Please input a number between 1 and 4!')
        return get_input(board)


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


def main():
    print('Welcome to Connect Four!\n')
    board = np.array([[-1 for i in range(4)] for j in range(4)])
    player_symbols = {-1: ' ', 0: 'X', 1: 'O'}
    current_player = 0
    turns = 0
    pretty_print(board, player_symbols)
    while check_board(board) == -1 and turns < 16:
        print('Please input the column in which to place the next stone.')
        column = get_input(board)
        insert_into_board(column, board, current_player)
        # additional newline between input and board
        print('')
        pretty_print(board, player_symbols)
        current_player = (current_player + 1) % 2
        turns += 1
    winner = check_board(board)
    if winner != -1:
        print(f"The winner is {player_symbols[check_board(board)]}")
    else:
        print("The result is a tie!")
    # make sure the user can see the result before exiting
    time.sleep(5)

if __name__ == '__main__':
    main()
