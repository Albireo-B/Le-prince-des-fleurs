import pygame
from pygame.locals import *
import sys

class CreditsController:

    def __initcredit__(self, screen):
        i=0
        j=0
        white= (255,255,255)

        fortgroud = pygame.image.load('../images/menu.png').convert()
        background = pygame.image.load('../images/menu.png').convert_alpha()
        quit   = myFont.render("quit",True,[135,206,235])
        button_rect_quit=quit.get_rect(topleft=(50,900))

        while True:
            screen.fill(white)
            for event in pygame.event.get():
                if event.type==QUIT:
                    pygame.quit()
                if event.type== pygame.MOUSEBUTTONDOWN:
                    pygame.mouse.get_pos()
                    if button_rect_quit.collidepoint(event.pos):#event to be changed
                        print('Button pressed.')
                        sys.exit()



            screen.blit(quit,(50,900))
            pygame.display.update()

    def text_objects(self, text, font):
        textSurface = font.render(text, True, black)
        return textSurface, textSurface.get_rect()
