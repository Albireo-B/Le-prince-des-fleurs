import pygame
from Intro.intro import launchIntro

def main():
    pygame.init()
    display_width=800
    display_height=600
    gameDisplay = pygame.display.set_mode((display_width,display_height))
    pygame.display.set_caption('Le Prince Des Fleurs')

    launchIntro(gameDisplay)

    #gameController = MenuController(gameDisplay)
    #gameController.run()

    pygame.quit()
    quit()

main()
