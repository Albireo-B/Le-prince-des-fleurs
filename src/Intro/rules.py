import pygame
import time
from pygame.locals import *
import math

def launchRules(screen):
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
    textofRuls1 = myFont.render("Règles du jeu et Histoire",True,blue)
    textofRuls2 = mytext.render("Alors que le Petit Prince menait une vie ",True,blue)
    textofRuls3 = mytext.render("paisible, il se passa un évènement inattendu.",True,blue)
    textofRuls4 = mytext.render("Un rassemblement de planètes inconnues qui ",True,blue)
    textofRuls5 = mytext.render("n'attendaient que d'être explorées et décorées.",True,blue)
    textofRuls6 = mytext.render("Mais chacunes d'elles abritaient d'énormes",True,blue)
    textofRuls7 = mytext.render("volcans, il allait donc être compliquer d'y",True,blue)
    textofRuls8 = mytext.render("faire naitre la vie pour le Petit Prince.",True,blue)
    textofRuls9 = mytext.render("Embarquer dans une aventure spaciale votre",True,blue)
    textofRuls10 = mytext.render("mission ? ramasser des étoiles et planter des",True,blue)
    textofRuls11 = mytext.render("fleurs avec la flèche du haut MAIS attention les ",True,blue)
    textofRuls12 = mytext.render("volcans peuvent entrer en éruption, a vous des ",True,blue)
    textofRuls13 = mytext.render("les ramonner à temps en allant dessus et en ",True,blue)
    textofRuls14 = mytext.render("appuyant sur la flèche du bas. Déplacer vous ",True,blue)
    textofRuls15 = mytext.render("avec les autres flèches directionnelles et ",True,blue)
    textofRuls16 = mytext.render("utiliser le pouvoir du ressort avec votre ",True,blue)
    textofRuls17 = mytext.render("votre souris pour aller vers une planète.",True,blue)

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
        screen.blit(background2, (30,-140))
        screen.blit(textofRuls1,(350,10))
        screen.blit(textofRuls2,(300,70))
        screen.blit(textofRuls3,(300,110))
        screen.blit(textofRuls4,(300,150))
        screen.blit(textofRuls5,(300,190))
        screen.blit(textofRuls6,(300,230))
        screen.blit(textofRuls7,(300,270))
        screen.blit(textofRuls8,(300,310))
        screen.blit(textofRuls9,(300,390))
        screen.blit(textofRuls10,(300,430))
        screen.blit(textofRuls11,(300,470))
        screen.blit(textofRuls12,(300,510))
        screen.blit(textofRuls13,(300,550))
        screen.blit(textofRuls14,(300,590))
        screen.blit(textofRuls15,(300,630))
        screen.blit(textofRuls16,(300,670))
        screen.blit(textofRuls17,(300,710))
        screen.blit(backtoMenu,(10,700))



        pygame.display.update()
