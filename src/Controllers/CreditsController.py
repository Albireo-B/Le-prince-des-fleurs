import pygame
from Intro.intro import *
from Controllers.MenuController import *

class CreditsController:

    def __init__(self,screen):
        i=0
        j=0
        white= (255,255,255)

        fortgroud = pygame.image.load('../images/menu.png').convert()
        background = pygame.image.load('../images/menu.png').convert_alpha()
        myFont = pygame.font.SysFont('arial',38)
        back   = myFont.render("Back",True,[135,206,235])
        button_rect_back=back.get_rect(topleft=(50,900))

        while True:
            screen.fill(white)
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                if event.type== pygame.MOUSEBUTTONDOWN:
                    pygame.mouse.get_pos()
                    if button_rect_back.collidepoint(event.pos):#event to be changed
                        gameDisplay = pygame.display.set_mode((1680,980))
                        pygame.display.set_caption('Le Prince Des Fleurs')
                        menuController1 = menuController.MenuController(gameDisplay)

            screen.blit(back,(50,900))

            screen.blit(background, (400,0))
            pygame.display.update()

    def text_objects(self, text, font):
        textSurface = font.render(text, True, black)
        return textSurface, textSurface.get_rect()
