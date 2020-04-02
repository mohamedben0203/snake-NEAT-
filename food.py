'''
Class which models the food object to be placed in the game
'''
import random
WIDTH = 19
HEIGHT = 19

class Food:
    def __init__(self):
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(0, HEIGHT)