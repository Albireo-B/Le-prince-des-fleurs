import pygame
import time
from pygame.locals import *
import math

def launchCtrl(screen):
    i=0
    j=0
    blue= (0,90,255)
    fortgroud = pygame.image.load('../images/Planet1.png').convert()
    background = pygame.image.load('../images/Planet1.png').convert_alpha()
    background3=pygame.image.load("../images/background.jpg").convert()
    background3=pygame.transform.scale(background3,(1024,768))
    myFont = pygame.font.SysFont('arial',38)
    mytext = pygame.font.SysFont('arial',28)


    backtoMenu  = myFont.render("Retour",True,[135,206,235])
    text = pygame.image.load("../images/controles.png").convert_alpha()


    #here we put all the rules of the game

    button_rect_backtoMenu=backtoMenu.get_rect(topleft=(50,700))

    while True:
        screen.blit(background3,(0,0))
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
            if event.type==KEYUP:
                if event.key==K_SPACE:
                    return

        # position of buttons can be changed
        i=420
        background2 = pygame.transform.scale(background, (600+i,592+i))
        screen.blit(text, (0,0))

        pygame.display.update()
