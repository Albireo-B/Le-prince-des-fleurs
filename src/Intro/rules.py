import pygame
import time
from pygame.locals import *
import math

def launchRules(screen):
    i=0
    j=0
    white= (255,255,255)
    gameDisplay = pygame.display.set_mode((1024,768))
    fortgroud = pygame.image.load('../images/Planet1.png').convert()
    background = pygame.image.load('../images/Planet1.png').convert_alpha()
    background3=pygame.image.load("../images/background.jpg").convert()
    background3=pygame.transform.scale(background3,(1024,768))
    myFont = pygame.font.SysFont('arial',38)
    mytext = pygame.font.SysFont('arial',18)


    backtoMenu  = myFont.render("Back to Menu",True,[135,206,235])
    textofRuls = mytext.render("here we put all the rules of the game",True,white)
    #here we put all the rules of the game

    button_rect_backtoMenu=backtoMenu.get_rect(topleft=(50,700))

    pygame.mixer.music.load ('../Sounds/menu.wav')
    pygame.mixer.music.play(-1)
    while True:
        screen.blit(background3,(0,0))
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
            if event.type== pygame.MOUSEBUTTONDOWN:
                pygame.mouse.get_pos()
                if button_rect_backtoMenu.collidepoint(event.pos):#event to be changed
                    pygame.mixer.music.stop()
                    return

        # position of buttons can be changed
        i=420
        background2 = pygame.transform.scale(background, (600+i,592+i))
        screen.blit(background2, (30,-140))
        screen.blit(textofRuls,(400,20))
        screen.blit(backtoMenu,(10,700))



        pygame.display.update()
