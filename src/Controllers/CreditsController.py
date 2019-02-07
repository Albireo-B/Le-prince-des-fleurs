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
        myFont = pygame.font.SysFont('arial',20)
        myFont2 = pygame.font.SysFont('arial',30)
        back   = myFont2.render("Back",True,[135,206,235])
        button_rect_back=back.get_rect(topleft=(20,700))
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
        nom5   = myFont2.render("Lois DENIAU",True,white)
        remer   = myFont2.render("Remerciements",True,white)
        perso1   = myFont.render("Personnes à remercier ou sources 1",True,white)
        perso2   = myFont.render("Personnes à remercier ou sources 2",True,white)
        perso3   = myFont.render("Personnes à remercier ou sources 3",True,white)
        date   = myFont2.render("02/2019",True,[135,206,235])
        lieu   = myFont.render("IUT2 Grenble",True,[135,206,235])
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

            i=420
            background2 = pygame.transform.scale(background, (600+i,592+i))
            screen.blit(background2, (0,-140))
            screen.blit(back,(20,700))
            screen.blit(nom1,(160,100))
            screen.blit(role11,(160,150))
            screen.blit(role12,(160,200))
            screen.blit(role13,(160,250))
            screen.blit(nom2,(370,100))
            screen.blit(role21,(370,150))
            screen.blit(role22,(370,200))
            screen.blit(role23,(370,250))
            screen.blit(nom3,(640,100))
            screen.blit(role31,(640,150))
            screen.blit(role32,(640,200))
            screen.blit(role33,(640,250))
            screen.blit(nom4,(160,300))
            screen.blit(role41,(160,350))
            screen.blit(role42,(160,400))
            screen.blit(role43,(160,450))
            screen.blit(nom5,(370,300))
            screen.blit(role51,(370,350))
            screen.blit(role52,(370,400))
            screen.blit(role53,(370,450))
            screen.blit(remer,(160,510))
            screen.blit(perso1,(160,560))
            screen.blit(perso2,(160,600))
            screen.blit(perso3,(160,650))
            screen.blit(lieu,(900,700))
            screen.blit(date,(900,720))

            pygame.display.update()

    def text_objects(self, text, font):
        textSurface = font.render(text, True, black)
        return textSurface, textSurface.get_rect()
