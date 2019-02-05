import pygame
import time
from pygame.locals import *
import math

pygame.init()
display_width=800
display_height=600
fenetre = pygame.display.set_mode((display_width,display_height))

def volcan(fenetre):


    black = (0,0,0)

    lwidth = 1036
    lheight = 752
    position = (display_width/2 - lwidth/2, display_height/2 - lheight/2)

    path = "../images/volcan"
    width, heigh = pygame.display.get_surface().get_size()
    img = pygame.image.load(path+".png").convert()
    formattedImg = pygame.transform.scale(img.subsurface((152, 14, 810, 194)), (lwidth, lheight))

    fenetre.blit(formattedImg, position)
    time.sleep(1/24)
    fenetre.fill(Color("black"))

volcan(fenetre)
pygame.quit()
quit()
