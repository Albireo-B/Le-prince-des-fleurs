import pygame
from Intro.intro import *

from Controllers.MenuController import *

def main():
    pygame.init()
    gameDisplay = pygame.display.set_mode((1500,750))
    pygame.display.set_caption('Le Prince Des Fleurs')

    launchIntro(gameDisplay)

    menuController = MenuController(gameDisplay)
    menuController.run()
    pygame.quit()
    quit()

main()
