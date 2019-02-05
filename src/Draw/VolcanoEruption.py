import pygame
import time
from pygame.locals import *
import math

pygame.init()
def eruption():
    i=0
    j=0
    t=0
    image = (0,0,0,0)
    clock = pygame.time.Clock()
    display_width=1500
    display_height=750
    fenetre = pygame.display.set_mode((display_width,display_height))
    def volcan(fenetre):
        t=0
        white = (255,255,255)
        path = "../../images/volcan"
        img = pygame.image.load(path+".png").convert()
        width, heigh = pygame.display.get_surface().get_size()
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
                lwidth = 600+i
                lheight = 200+j
                position = (display_width/2 - lwidth/2, display_height/2 - lheight/2)

                formattedImg = pygame.transform.scale(img.subsurface(image), (lwidth, lheight))
                fenetre.fill(white)
                fenetre.blit(formattedImg, position)
                if t>=0 and t<15:
                    time.sleep(1/24)
                elif t>=15 and t<50 :
                    time.sleep(1/50)
                else:
                    time.sleep(1/240)
                i=i+2
                i=i+1
                pygame.display.flip()

            while i>0 and j>0:
                lwidth = 600+i
                lheight = 200+j
                position = (display_width/2 - lwidth/2, display_height/2 - lheight/2)
                formattedImg = pygame.transform.scale(img.subsurface(image), (lwidth, lheight))
                fenetre.fill(white)
                fenetre.blit(formattedImg, position)
                if t>=0 and t<15:
                    time.sleep(1/24)
                elif t>=15 and t<50 :
                    time.sleep(1/50)
                else:
                    time.sleep(1/240)
                i=i-2
                i=i-1
                pygame.display.flip()
            t=t+1
            print(t)

    while True :

        volcan(fenetre)

pygame.quit()
quit()
