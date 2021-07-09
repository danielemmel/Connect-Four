import argparse


def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('-ai', '--AI', nargs='*', choices=['r'],
                        help='Specifies which kind of ai(s) should be playing, using r for random.',
                        default=[])
    args = vars(parser.parse_args())
    return args


def get_human_input(board):
    try:
        inp = int(input()) - 1
        if inp in range(0, 4) and -1 in board[:, inp]:
            return inp
        else:
            print('Input must be a non-full column between 1 and 4!')
            return get_human_input(board)
    except ValueError:
        print('Please input a number between 1 and 4!')
        return get_human_input(board)
