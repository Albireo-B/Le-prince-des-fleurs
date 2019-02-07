import pygame
from Intro.intro import *
from Controllers.MenuController import *

class CreditsController:

    def __init__(self,screen):
        i=0
        j=0
        white= (255,255,255)

        fortgroud = pygame.image.load('../images/Planet0.png').convert()
        background = pygame.image.load('../images/Planet0.png').convert_alpha()
        myFont = pygame.font.SysFont('arial',48)
        myFont2 = pygame.font.SysFont('arial',58)
        back   = myFont.render("Back",True,[135,206,235])
        button_rect_back=back.get_rect(topleft=(50,900))
        role1   = myFont2.render("role1",True,white)
        nom1   = myFont.render("nom1",True,white)
        role2   = myFont2.render("role2",True,white)
        nom2   = myFont.render("nom2",True,white)
        role3   = myFont2.render("role3",True,white)
        nom3   = myFont.render("nom3",True,white)
        role4   = myFont2.render("role4",True,white)
        nom4   = myFont.render("nom4",True,white)
        role5   = myFont2.render("role5",True,white)
        nom5   = myFont.render("nom5",True,white)
        #button_rect_test=test.get_rect(topleft=(200,700))

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

            i=1100
            background2 = pygame.transform.scale(background, (600+i,592+i))
            screen.blit(background2, (-10,-240))
            screen.blit(back,(50,900))
            screen.blit(role1,(250,100))
            screen.blit(nom1,(250,150))
            screen.blit(role2,(250,350))
            screen.blit(nom2,(250,400))
            screen.blit(role3,(1300,100))
            screen.blit(nom3,(1300,150))
            screen.blit(role4,(1300,350))
            screen.blit(nom4,(1300,400))
            screen.blit(role5,(250,600))
            screen.blit(nom5,(250,650))

            pygame.display.update()

    def text_objects(self, text, font):
        textSurface = font.render(text, True, black)
        return textSurface, textSurface.get_rect()
