import pygame
from Credits.Credits import Credits

def main_credits():
    pygame.init()
    gameDisplay = pygame.display.set_mode((1680,980))
    pygame.display.set_caption('Credits')
    credit = Credits(gameDisplay)

main_credits()
pygame.quit()
quit()
