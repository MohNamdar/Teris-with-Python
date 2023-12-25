from config import *


def under_empty(playground, shape, row, move):
    first = len(shape[0])
    other = 4 - first

    empty_count = 0
    if other:
        for c in shape[1]:
            if playground[row][c + move] == ' ':
                empty_count += 1

    # Exception for shape 4
    if first == 4:
        other = first
        for c in shape[0]:
            if playground[row - 1][c + move] == ' ':
                empty_count += 1

    if empty_count == other:
        return True

    return False


def game_over(playground):
    for i in range(0, WIDTH, 2):
        if playground[0][i] == '[':
            return 1
    return 0
