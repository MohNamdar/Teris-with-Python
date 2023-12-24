from view import show
from config import *
from time import sleep
import os
import random

playground = [[' ' for i in range(WIDTH)] for j in range(HEIGHT)]


class Shapes:
    def __init__(self):
        # define shapes Coordinates
        self.all_shape = [[[W_CENTER - 1], [W_CENTER - 3, W_CENTER - 1, W_CENTER + 1]],
                          [[W_CENTER - 2, W_CENTER], [W_CENTER - 2, W_CENTER]],
                          [[W_CENTER - 3, W_CENTER - 1], [W_CENTER - 1, W_CENTER + 1]],
                          [[W_CENTER - 4, W_CENTER - 2, W_CENTER, W_CENTER + 2]]]

    def random(self):
        rand_num = random.randint(0, 3)
        return self.all_shape[rand_num]


s = Shapes()

shape = s.random()

show.fall_shape(playground, shape)

