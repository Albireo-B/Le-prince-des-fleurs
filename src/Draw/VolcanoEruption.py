import pygame
import time
from pygame.locals import *
import math


def volcanoEruption(fenetre,volcano,width,height):
    i=0
    j=0
    image = (0,0,0,0)
    t=0
    path = "../../images/volcan"
    img = pygame.image.load(path+".png").convert()
    while t<100:
        i=0
        j=0
        if (t>=0 and t<15):
            image =(160, 16, 750, 200)
        elif (t>=15 and t<50):
            image=(160, 226, 750, 240)
        else :
            image = (160, 360, 750, 260)
        while i<60 and j<30:
            lwidth = volcano.width+i
            lheight = volcano.height+j
            position = (volcano.volcanoCenter)

<<<<<<< HEAD
        volcan(fenetre)
=======
            formattedImg = pygame.transform.scale(img.subsurface(image), (lwidth, lheight))
            fenetre.blit(formattedImg, position)
            if t>=0 and t<15:
                time.sleep(1/24)
            elif t>=15 and t<50 :
                time.sleep(1/50)
            else:
                time.sleep(1/240)
            i=i+2
            i=i+1

        while i>0 and j>0:
            lwidth =volcano.width+i
            lheight = volcano.height+j
            position = (volcano.volcanoCenter)
            formattedImg = pygame.transform.scale(img.subsurface(image), (lwidth, lheight))
            fenetre.blit(formattedImg, position)
            if t>=0 and t<15:
                time.sleep(1/24)
            elif t>=15 and t<50 :
                time.sleep(1/50)
            else:
                time.sleep(1/240)
            i=i-2
            i=i-1
        t=t+1
>>>>>>> 74080aea0aca3493b729c3b73cc15b4fc901bfdc
