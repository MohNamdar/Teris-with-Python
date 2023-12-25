from config import *
from time import sleep
import os
from termcolor import colored
from calculate.block_detector import under_empty
import keyboard



def play_ground(playground, colors):
    res = ['┌']
    res.extend(['─'] * WIDTH)
    res.append('┐')
    res = [res]

    for col in range(HEIGHT):
        temp = ['│']
        for row in range(WIDTH):
            temp.append(playground[col][row])
        temp.append('│')
        res.append(temp)

    temp = ['└']
    temp.extend(['─'] * WIDTH)
    temp.append('┘')
    res.append(temp)

    for col in range(HEIGHT + 2):
        for row in range(WIDTH + 2):
            color = colors[col][row]
            print(colored(res[col][row], color), end='')
        print()


def fall_shape(playground, shape, colors, rand_num):
    first = len(shape[0])
    other = 4 - first

    for row in range(1, HEIGHT):

        if under_empty(playground, shape, row):

            # clear for print next frame
            os.system('cls')
            # printing first line of shape
            for i in range(first):
                for c in shape[0]:
                    playground[row - 1][c] = '['
                    playground[row - 1][c + 1] = ']'

                    colors[row][c + 1] = config_color(rand_num)
                    colors[row][c + 2] = config_color(rand_num)

            # print second line of shape (if exist)
            if other != 0:
                for c in shape[1]:
                    playground[row][c] = '['
                    playground[row][c + 1] = ']'

                    colors[row + 1][c + 1] = config_color(rand_num)
                    colors[row + 1][c + 2] = config_color(rand_num)

            play_ground(playground, colors)
            sleep(FALL_SPEED)

            # Exception for shape 4 (end stop problem -> fixed)
            if not other and row == HEIGHT - 1:
                for i in range(first):
                    for c in shape[0]:
                        playground[row - 1][c] = ' '
                        playground[row - 1][c + 1] = ' '

                os.system('cls')
                for i in range(first):
                    for c in shape[0]:
                        playground[row][c] = '['
                        playground[row][c + 1] = ']'

                        colors[row + 1][c + 1] = config_color(rand_num)
                        colors[row + 1][c + 2] = config_color(rand_num)
                play_ground(playground, colors)
                sleep(FALL_SPEED)

            if row != HEIGHT - 1 and under_empty(playground, shape, row + 1):
                # removing the printed shape (same to printing)
                for i in range(first):
                    for c in shape[0]:
                        playground[row - 1][c] = ' '
                        playground[row - 1][c + 1] = ' '

            if other != 0 and row != HEIGHT - 1 and under_empty(playground, shape, row + 1):
                for c in shape[1]:
                    playground[row][c] = ' '
                    playground[row][c + 1] = ' '


def config_color(shape_num):
    if shape_num == 0:
        return 'red'

    elif shape_num == 1:
        return 'blue'

    elif shape_num == 2:
        return 'green'

    elif shape_num == 3:
        return 'yellow'
