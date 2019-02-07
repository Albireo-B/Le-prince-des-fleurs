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
        myFont = pygame.font.SysFont('arial',30)
        myFont2 = pygame.font.SysFont('arial',40)
        back   = myFont.render("Back",True,[135,206,235])
        button_rect_back=back.get_rect(topleft=(50,900))
        role11   = myFont.render("role11",True,white)
        role12   = myFont.render("role12",True,white)
        role13   = myFont.render("role13",True,white)
        nom1   = myFont2.render("Haozhou DAI",True,white)
        role21   = myFont.render("role21",True,white)
        role22   = myFont.render("role22",True,white)
        role23   = myFont.render("role23",True,white)
        nom2   = myFont2.render("Guillaume VINET",True,white)
        role31   = myFont.render("role31",True,white)
        role32   = myFont.render("role32",True,white)
        role33   = myFont.render("role33",True,white)
        nom3   = myFont2.render("Clement GENEVOIS",True,white)
        role41   = myFont.render("role41",True,white)
        role42   = myFont.render("role42",True,white)
        role43   = myFont.render("role43",True,white)
        nom4   = myFont2.render("Alexis GROS",True,white)
        role51   = myFont.render("Chef de projet",True,white)
        role52   = myFont.render("role52",True,white)
        role53   = myFont.render("role53",True,white)
        nom5   = myFont2.render("Lois THEOPHILE",True,white)
        remer   = myFont2.render("Remerciements",True,white)
        perso1   = myFont.render("Personnes à remercier ou sources 1",True,white)
        perso2   = myFont.render("Personnes à remercier ou sources 2",True,white)
        perso3   = myFont.render("Personnes à remercier ou sources 3",True,white)
        date   = myFont2.render("02/2019",True,white)
        lieu   = myFont.render("IUT2 Grenble",True,white)
        #button_rect_test=test.get_rect(topleft=(200,700))

        while True:
            screen.fill(white)
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                if event.type== pygame.MOUSEBUTTONDOWN:
                    pygame.mouse.get_pos()
                    if button_rect_back.collidepoint(event.pos):#event to be changed
                        return
                        #gameDisplay = pygame.display.set_mode((1680,980))
                        #pygame.display.set_caption('Le Prince Des Fleurs')
                        #menuController1 = menuController.MenuController(gameDisplay)

            i=1100
            background2 = pygame.transform.scale(background, (600+i,592+i))
            screen.blit(background2, (-10,-240))
            screen.blit(back,(50,900))
            screen.blit(nom1,(410,100))
            screen.blit(role11,(410,150))
            screen.blit(role12,(410,200))
            screen.blit(role13,(410,250))
            screen.blit(nom2,(730,100))
            screen.blit(role21,(730,150))
            screen.blit(role22,(730,200))
            screen.blit(role23,(730,250))
            screen.blit(nom3,(1050,100))
            screen.blit(role31,(1050,150))
            screen.blit(role32,(1050,200))
            screen.blit(role33,(1050,250))
            screen.blit(nom4,(410,350))
            screen.blit(role41,(410,400))
            screen.blit(role42,(410,450))
            screen.blit(role43,(410,500))
            screen.blit(nom5,(730,350))
            screen.blit(role51,(730,400))
            screen.blit(role52,(730,450))
            screen.blit(role53,(730,500))
            screen.blit(remer,(410,700))
            screen.blit(perso1,(410,750))
            screen.blit(perso2,(410,800))
            screen.blit(perso3,(410,850))
            screen.blit(lieu,(1360,880))
            screen.blit(date,(1360,920))

            pygame.display.update()

    def text_objects(self, text, font):
        textSurface = font.render(text, True, black)
        return textSurface, textSurface.get_rect()
