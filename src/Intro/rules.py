import pygame
import time
from pygame.locals import *
import math

def launchRules(screen):
    i=0
    j=0
    white= (255,255,255)
    gameDisplay = pygame.display.set_mode((1024,768))
    fortgroud = pygame.image.load('../images/menu.png').convert()
    background = pygame.image.load('../images/menu.png').convert_alpha()
    myFont = pygame.font.SysFont('arial',38)
    mytext = pygame.font.SysFont('arial',18)


    backtoMenu  = myFont.render("Back to Menu",True,[135,206,235])
    textofRuls = mytext.render("here we put all the rules of the game",True,[135,206,235])
    #here we put all the rules of the game

    button_rect_backtoMenu=backtoMenu.get_rect(topleft=(50,700))

    pygame.mixer.music.load ('../Sounds/menu.wav')
    pygame.mixer.music.play(-1)
    while True:
        screen.fill((255,255,255))
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
            if event.type== pygame.MOUSEBUTTONDOWN:
                pygame.mouse.get_pos()
                if button_rect_backtoMenu.collidepoint(event.pos):#event to be changed
                    pygame.mixer.music.stop()
                    return

        # position of buttons can be changed
        screen.blit(textofRuls,(20,20))
        screen.blit(backtoMenu,(50,700))
        if i<=30:
            screen.blit(background, (400,30-i))
        else:
            screen.blit(background, (400,0+j))
            j+=0.1
        if j>30:
            screen.blit(background, (400,0+j))
            i=0
            j=0



        pygame.display.update()
