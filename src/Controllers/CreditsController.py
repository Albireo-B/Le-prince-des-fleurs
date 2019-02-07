import pygame
from Intro.intro import *
from Controllers.MenuController import *

class CreditsController:

    def __init__(self,screen):
        i=0
        j=0
        white= (255,255,255)

        background = pygame.image.load('../images/Planet0.png').convert_alpha()
        background3=pygame.image.load("../images/background.jpg").convert()
        background3=pygame.transform.scale(background3,(1024,768))
        myFont = pygame.font.SysFont('arial',20)
        myFont2 = pygame.font.SysFont('arial',30)
        back   = myFont2.render("Back",True,[135,206,235])
        button_rect_back=back.get_rect(topleft=(20,700))
        role11   = myFont.render("Développeur UI",True,white)
        nom1   = myFont2.render("Haozhou DAI",True,white)
        role21   = myFont.render("Développeur",True,white)
        nom2   = myFont2.render("Guillaume VINET",True,white)
        role31   = myFont.render("Développeur UI",True,white)
        nom3   = myFont2.render("Clement GENEVOIS",True,white)
        role41   = myFont.render("Directeur technique",True,white)
        role42   = myFont.render("Développeur",True,white)
        nom4   = myFont2.render("Alexis GROS",True,white)
        role51   = myFont.render("Chef de projet",True,white)
        role52   = myFont.render("Développeur",True,white)
        nom5   = myFont2.render("Lois DENIAU",True,white)
        remer   = myFont2.render("Remerciements",True,white)
        perso1   = myFont.render("Personnes à remercier ou sources 1",True,white)
        perso2   = myFont.render("Personnes à remercier ou sources 2",True,white)
        perso3   = myFont.render("Personnes à remercier ou sources 3",True,white)
        date   = myFont2.render("02/2019",True,[135,206,235])
        lieu   = myFont.render("IUT2 Grenble",True,[135,206,235])
        #button_rect_test=test.get_rect(topleft=(200,700))

        while True:
            screen.blit(background3,(0,0))
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
            screen.blit(nom1,(160,120))
            screen.blit(role11,(160,170))
            screen.blit(nom2,(370,120))
            screen.blit(role21,(370,170))
            screen.blit(nom3,(640,120))
            screen.blit(role31,(640,170))
            screen.blit(nom4,(160,260))
            screen.blit(role41,(160,320))
            screen.blit(role42,(160,360))
            screen.blit(nom5,(370,260))
            screen.blit(role51,(370,320))
            screen.blit(role52,(370,360))
            screen.blit(remer,(160,450))
            screen.blit(perso1,(160,500))
            screen.blit(perso2,(160,550))
            screen.blit(perso3,(160,600))
            screen.blit(lieu,(900,700))
            screen.blit(date,(900,720))

            pygame.display.update()

    def text_objects(self, text, font):
        textSurface = font.render(text, True, black)
        return textSurface, textSurface.get_rect()
