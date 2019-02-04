import pygame
from pygame.locals import *
import time

pygame.init()
fenetre = pygame.display.set_mode((640, 480), RESIZABLE)

continuer = 1

fond = pygame.image.load("background.jpg").convert()
#fenetre.blit(fond, (0,0))


perso = pygame.image.load("perso.png").convert_alpha()
# image.set_colorkey((255,255,255)) #Rend le blanc (valeur RGB : 255,255,255) de l'image transparent
aaa =  pygame.transform.scale(perso.subsurface((30, 30, 50, 50)), (10, 10))
#fenetre.blit(aaa, (10,10))

def readIntro(fenetre):
    width, heigh = pygame.display.get_surface().get_size()
    tabFrame = {1 : 1, 2 : 1}
    imgList = {}
    for i in range(1,14):
        img = pygame.image.load("intro/img/"+str(i)+".png").convert()
        formattedImg = pygame.transform.scale(img.subsurface((150, 30, 900, 650)), (100, 100))
        imgList[i] = formattedImg

    for key in tabFrame:
        fenetre.blit(imgList[key], (width/2,heigh/2))
        pygame.display.flip()
        time.sleep(tabFrame[key])

#Boucle infinie
readIntro(fenetre)
"""
while continuer:
    for event in pygame.event.get():   #On parcours la liste de tous les événements reçus
        if event.type == KEYDOWN and event.key == K_SPACE:
    	    print("Espace")

        if event.type == QUIT:     #Si un de ces événements est de type QUIT
            continuer = 0      #On arrête la boucle
    pygame.display.flip()
"""
