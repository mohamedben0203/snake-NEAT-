'''
Create the window as an object
'''
import pygame

class Window:

    def __init__(self, screen, height, width, backgroundColour, squareSize):
        self.screen = screen
        self.height = height
        self.width = width
        self.backgroundColour = backgroundColour
        self.squareSize = squareSize

    def draw(self):
        self.screen.fill(self.backgroundColour)

    def drawGrid(self):
        colour = (0,0,0)
        for i in range(self.height + 1):
            startPos = (i * self.squareSize, 0)
            endPos = (i*self.squareSize, self.width * self.squareSize)
            pygame.draw.line(self.screen, colour, startPos, endPos)
            

        for j in range(self.width + 1):
            startPos = (0, j * self.squareSize)
            endPos = (self.height * self.squareSize, j * self.squareSize)
            pygame.draw.line(self.screen, colour, startPos, endPos)
            
