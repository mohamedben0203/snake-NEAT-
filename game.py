import pygame
from food import Food
from window import Window

#initialise pygame
pygame.init()

#initialise the window
WIDTH = 20
HEIGHT = 20
SQUARESIZE = 25
BACKGROUND_COLOUR = (25, 230, 30)
dimension = (WIDTH * SQUARESIZE + 1, HEIGHT * SQUARESIZE + 1)

#create the screen
screen = pygame.display.set_mode(dimension)

#initialise the window object
window = Window(screen, HEIGHT, WIDTH, BACKGROUND_COLOUR, SQUARESIZE)
window.draw()
window.drawGrid()
pygame.display.flip()

food = Food(window)
food.draw()

pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        #if the user closes the window then close the programme
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

exit()
