#!/usr/bin/python3

import time

import numpy as np

from AI.rand import choose_column as r
from logic import check_board, insert_into_board
from parsing import parse, get_human_input
from utils import pretty_print

ai_map = {'r': r}


def main():
    args = parse()
    print('Welcome to Connect Four!\n')

    names = args.get('AI')[:2]
    ai_list = [ai_map[name] for name in names]

    board = np.array([[-1 for i in range(4)] for j in range(4)])
    player_symbols = {-1: ' ', 0: 'X', 1: 'O'}
    current_player = 0
    turns = 0

    pretty_print(board, player_symbols)

    while check_board(board) == -1 and turns < 16:
        if not ai_list or len(ai_list) == 1 and current_player == 0:
            print('Please input the column in which to place the next stone.')
            column = get_human_input(board)
        else:
            start = time.time()
            column = ai_list[current_player](board, player_symbols, current_player) if len(ai_list) > 1 else ai_list[0](
                board, player_symbols, current_player)
            print(f'AI {current_player + 1} chose column {column + 1} in {time.time() - start} seconds')

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
