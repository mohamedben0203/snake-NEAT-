'''
Class which models the food object to be placed in the game
'''
import random
import pygame

class Food:
    colour = (255, 0, 255)

    def __init__(self, window):
        self.window = window
        self.x = random.randint(0, window.width - 1)
        self.y = random.randint(0, window.height - 1)

    def draw(self):
        square = self.window.squareSize
        x = self.x * square
        y = self.y * square
        rect = (x, y, square, square)
        pygame.draw.rect(self.window.screen, self.colour, rect)
