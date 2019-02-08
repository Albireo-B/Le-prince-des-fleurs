import pygame
import time
from pygame.locals import *
import math

def launchRules(screen):
    i=0
    j=0
    blue= (0,90,255)
    fortgroud = pygame.image.load('../images/Planet1.png').convert()
    background = pygame.image.load('../images/Planet3.png').convert_alpha()
    background = pygame.transform.scale(background, (1020,1020))
    background3=pygame.image.load("../images/background.jpg").convert()
    background3=pygame.transform.scale(background3,(1024,768))
    myFont = pygame.font.SysFont('arial',38)
    mytext = pygame.font.SysFont('arial',28)


    backtoMenu  = myFont.render("Retour",True,[135,206,235])
    text = pygame.image.load("../images/text.png").convert_alpha()


    #here we put all the rules of the game

    button_rect_backtoMenu=backtoMenu.get_rect(topleft=(50,700))

    while True:
        screen.blit(background3,(0,0))
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
            if event.type== pygame.MOUSEBUTTONDOWN:
                pygame.mouse.get_pos()
                if button_rect_backtoMenu.collidepoint(event.pos):#event to be changed
                    return

        # position of buttons can be changed
        i=420
        background2 = pygame.transform.scale(background, (600+i,592+i))
        screen.blit(background, (-15,-120))
        screen.blit(text, (0,100))
        screen.blit(backtoMenu,(10,700))



        pygame.display.update()
