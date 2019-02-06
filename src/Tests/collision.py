import os
import pygame
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((640, 480), RESIZABLE)

def load_image(i):
    'load an image from the data directory with per pixel alpha transparency.'
    return pygame.image.load(i).convert_alpha()

terrain1 = load_image("balloon.png")
terrain1 = pygame.transform.scale(terrain1, (10, 10))
balloon = load_image("balloon.png")
balloon =  pygame.transform.scale(balloon, (10, 40))

# create a mask for each of them.
terrain1_mask = pygame.mask.from_surface(terrain1, 50)
balloon = pygame.transform.rotozoom(balloon, 45, 1)
balloon_mask = pygame.mask.from_surface(balloon, 50)


# this is where the balloon, and terrain are.
terrain1_rect = terrain1.get_rect()
balloon_rect = balloon.get_rect()
terrain1_rect.x += 20

# start the main loop.
while 1:
    events = pygame.event.get()
    for e in events:
        if e.type == pygame.KEYDOWN:
            balloon_rect.x += 1

    # see how far the balloon rect is offset from the terrain rect.
    offset_x = balloon_rect[0] - terrain1_rect[0]
    offset_y = balloon_rect[1] - terrain1_rect[1]
    if terrain1_mask.overlap(balloon_mask, (offset_x, offset_y)):
        print("cool")
    # draw the background color, and the terrain.
    screen.fill((0,0,0))
    screen.blit(terrain1, (terrain1_rect.x,0))

    screen.blit(balloon, (balloon_rect[0], balloon_rect[1]) )

    # flip the display.
    pygame.display.flip()

pygame.quit()
