import pygame
import time
from pygame.locals import *
import math


def launchIntro(fenetre):
    fenetre.fill(Color("black"))
    logo_sound = pygame.mixer.Sound('../Sounds/SCREW_GRAVITY.wav')
    black = (0,0,0)
    white = (255,255,255)
    clock = pygame.time.Clock()

    crashed = False
    lwidth = 238
    lheight = 314

    path = "../images/animIntro/"


    width, heigh = pygame.display.get_surface().get_size()
    tabFrame = {1:1,2:4,3:2,4:1,3:3,4:1,3:1,4:2,1:8,5:1,6:2,7:1,8:1,9:1,10:2,11:1,12:1,13:1,14:2,15:1,16:1,17:1,18:1,19:2,20:1,21:2,19:2,22:1,21:11}
    imgList = {}
    for i in range(1,23):
        img = pygame.image.load(path+str(i)+".png").convert()
        formattedImg = pygame.transform.scale(img.subsurface((150, 0, 900, 650)), (lwidth, lheight - 20))
        imgList[i] = formattedImg

    imgcadr = {}
    for i in range(1,5):
        img = pygame.image.load(path+"t"+str(i)+".png").convert_alpha()
        formattedImg = pygame.transform.scale(img, (lwidth, int(lheight*1.2)))
        imgcadr[i] = formattedImg

    cadre = pygame.image.load(path+"cadre.png").convert_alpha()
    cadre = pygame.transform.scale(cadre, (lwidth, int(lheight*1.2)))
    pygame.mixer.Sound.play(logo_sound)
    for key in tabFrame:
        position = (width/2 - lwidth/2, heigh/2 - lheight/2)
        fenetre.blit(imgList[key], position)
        fenetre.blit(cadre, position)
        if key>8:
            if key<10:
                fenetre.blit(imgcadr[1], position)
            elif key<13:
                fenetre.blit(imgcadr[2], position)
            elif key<15:
                fenetre.blit(imgcadr[3], position)
            else:
                fenetre.blit(imgcadr[4], position)
        pygame.display.flip()
        time.sleep(tabFrame[key]/24)

    logo = pygame.image.load(path+"cadre2.png").convert()
    logo = pygame.transform.scale(logo, (lwidth, int(lheight*1.2)))
    logoCopie=logo.copy()
    rectLogo = logo.get_rect(center=(width/2 - lwidth/2, heigh/2 - lheight/2))
    angle=0
    for i in range(0,int(heigh/(2*15))):
        angle -= 0.5
        logo=pygame.transform.rotozoom(logoCopie,angle,1)
        fenetre.blit(logo, (width/2 - lwidth/2 + i, heigh/2- i*28 - lheight/2))
        pygame.display.flip()
        time.sleep(1/24)
        fenetre.fill(Color("black"))
    time.sleep(1)
