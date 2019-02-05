import pygame
import time
from pygame.locals import *
import math

pygame.init()
i=0
j=0
t=0
image = (0,0,0,0)
clock = pygame.time.Clock()
display_width=950
display_height=650
fenetre = pygame.display.set_mode((display_width,display_height))
def volcan(fenetre):
    t=0
    while t<100:
        i=0
        j=0
        white = (255,255,255)

        path = "../../images/volcan"
        img = pygame.image.load(path+".png").convert()
        width, heigh = pygame.display.get_surface().get_size()
        if (t>=0 and t<33):
            image =(160, 16, 750, 200)
        elif (t>33 and t<66):
            image=(160, 226, 750, 260)
        else :
            image = (160, 360, 750, 404)
        while i<50 and j<25:
            lwidth = 600+i
            lheight = 200+j
            position = (display_width/2 - lwidth/2, display_height/2 - lheight/2)
            formattedImg = pygame.transform.scale(img.subsurface(image), (lwidth, lheight))
            fenetre.fill(white)
            fenetre.blit(formattedImg, position)
            time.sleep(1/24)
            pygame.display.flip()
            i=i+2
            j=j+1

        while i>0 and j>0:
            lwidth = 600+i
            lheight = 200+j
            position = (display_width/2 - lwidth/2, display_height/2 - lheight/2)
            formattedImg = pygame.transform.scale(img.subsurface(image), (lwidth, lheight))
            fenetre.fill(white)
            fenetre.blit(formattedImg, position)
            time.sleep(1/50)
            pygame.display.flip()

            i=i-2
            j=j-1

        t=t+1
        print(t)
while True :

    volcan(fenetre)

pygame.quit()
quit()
