import pygame
import

def main():
    pygame.init()
    display_width=800
    display_height=600
    gameDisplay = pygame.display.set_mode((display_width,display_height))

    

    pygame.display.set_caption('Le Prince Des Fleurs')
    gameController = MenuController(gameDisplay)
    gameController.run()

    pygame.quit()
    quit()
