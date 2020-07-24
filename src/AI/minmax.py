import copy

from logic import check_board, insert_into_board


# TODO: fix, apparently not really row sensitive yet?
def choose_column(board, player_symbols, current_player):
    pos_choices = [i for i in range(0, 4) if -1 in board[:, i]]
    print(pos_choices)
    if len(pos_choices) == 1:
        return pos_choices[0]

    val, choice = max_value(copy.deepcopy(board), player_symbols, current_player)

    print(val)

    if choice is None:
        print('Broken')
        exit()

    return choice


def max_value(board, player_symbols, current_player):
    # Terminal Test
    val = check_board(board)
    if val != -1:
        if val == current_player:
            return 1, None
        else:
            return -1, None

    pos_choices = [i for i in range(0, 4) if -1 in board[:, i]]
    if not pos_choices:
        return 0, None

    # Recursive call
    val = -2
    for choice in pos_choices:
        insert_into_board(choice, board, current_player)
        val = max(val, min_value(board, player_symbols, (current_player + 1) % 2)[0])

    return val, choice


def min_value(board, player_symbols, current_player):
    # Terminal Test
    val = check_board(board)
    if val != -1:
        if val == current_player:
            return -1, None
        else:
            return 1, None
    pos_choices = [i for i in range(0, 4) if -1 in board[:, i]]
    if not pos_choices:
        return 0, None

    # Recursive call
    val = 2
    for choice in pos_choices:
        insert_into_board(choice, board, current_player)
        val = min(val, max_value(board, player_symbols, (current_player + 1) % 2)[0])

    return val, choice
