from view import show
from config import *
from calculate.block_detector import game_over
from time import sleep
import os
import random

playground = [[' ' for i in range(WIDTH)] for j in range(HEIGHT)]
colors = [['white' for i in range(WIDTH+2)] for j in range(HEIGHT+2)]


class Shapes:
    def __init__(self):
        # define shapes Coordinates
        self.all_shape = [[[W_CENTER], [W_CENTER - 2, W_CENTER, W_CENTER + 2]],
                          [[W_CENTER - 2, W_CENTER], [W_CENTER - 2, W_CENTER]],
                          [[W_CENTER - 4, W_CENTER - 2], [W_CENTER - 2, W_CENTER]],
                          [[W_CENTER - 4, W_CENTER - 2, W_CENTER, W_CENTER + 2]]]

    def random(self):
        rand_num = random.randint(0, 3)
        return self.all_shape[rand_num], rand_num


s = Shapes()

while True:
    # shape = s.all_shape[0]
    # show.fall_shape(playground, shape, colors, 0)
    #
    # shape = s.all_shape[1]
    # show.fall_shape(playground, shape, colors, 1)
    #
    # shape = s.all_shape[2]
    # show.fall_shape(playground, shape, colors, 2)
    #
    # shape = s.all_shape[3]
    # show.fall_shape(playground, shape, colors, 3)

    shape, rand_num = s.random()
    show.fall_shape(playground, shape, colors, rand_num)

    if game_over(playground):
        print('GAME0VER!')
        break

