from config import *
from time import sleep
import os


def play_ground(playground):
    width = len(playground[0])
    res = ['┌' + '─' * width + '┐']
    for r in playground:
        res.append('│' + (''.join(r) + ' ' * width)[:width] + '│')
    res.append('└' + '─' * width + '┘')
    return '\n'.join(res)


def fall_shape(playground, shape):
    first = len(shape[0])
    other = first - 4

    for row in range(1, HEIGHT):

        # clear for print next frame
        os.system('cls')
        # printing first line of shape
        for i in range(first):
            for c in shape[0]:
                playground[row - 1][c] = '['
                playground[row - 1][c + 1] = ']'

        # print second line of shape (if exist)
        if other != 0:
            for c in shape[1]:
                playground[row][c] = '['
                playground[row][c + 1] = ']'

        print(play_ground(playground))
        sleep(0.5)

        # Exception for shape 4 (end stop problem -> fixed)
        if not other and row == HEIGHT - 1:
            for i in range(first):
                for c in shape[0]:
                    playground[row - 1][c] = ' '
                    playground[row - 1][c + 1] = ' '
            os.system('cls')
            row += 1
            for i in range(first):
                for c in shape[0]:
                    playground[row - 1][c] = '['
                    playground[row - 1][c + 1] = ']'
            print(play_ground(playground))
            sleep(0.5)

        # removing the printed shape (same to printing)
        for i in range(first):
            for c in shape[0]:
                playground[row - 1][c] = ' '
                playground[row - 1][c + 1] = ' '

        if other != 0:
            for c in shape[1]:
                playground[row][c] = ' '
                playground[row][c + 1] = ' '
