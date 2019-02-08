import pygame
import time
from pygame.locals import *
import math
from Controllers.ScoreController import *

def launchScores(screen,save):


    i=0
    j=0
    white= (255,255,255)
    gameDisplay = pygame.display.set_mode((1680,980))

    myFont = pygame.font.SysFont('arial',38)
    myscores = pygame.font.SysFont('arial',28)


    backtoMenu  = myFont.render("Back to Menu",True,[135,206,235])
    button_rect_backtoMenu=backtoMenu.get_rect(topleft=(1400,600))


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

        while i in range(10):
            screen.blit(myscores.render(str(self.score[i]+self.score[i+1]), True, [135,206,235]), [20, 20*i])
        i+=2




        pygame.display.update()
