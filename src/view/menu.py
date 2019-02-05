import pygame
from pygame.locals import *
import sys

pygame.init()
pygame.display.set_caption("Le prince des fleur")
screen = pygame.display.set_mode((1200, 800))
fortgroud = pygame.image.load('../../images/menu.png').convert()
background = pygame.image.load('../../images/menu.png').convert_alpha()

myFont = pygame.font.SysFont('arial',38)

start  = myFont.render("start",True,[255,255,0])
scores = myFont.render("scores",True,[255,255,0])
credits= myFont.render("credits",True,[255,255,0])
quit   = myFont.render("quit",True,[255,255,0])


while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(start,(0,100))

    screen.blit(scores,(0,200))

    screen.blit(credits,(0,300))

    screen.blit(quit,(0,400))

    screen.blit(background,(400,0))

    pygame.display.update()
