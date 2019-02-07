import pygame
from pygame.locals import *
from Controllers.GameController import GameController
from Controllers.ScoreController import ScoreController

white = (255,255,255)
black = (0,0,0)
skyblue = (135,206,235)

class ChoixController:

    def __init__(self, screen):
        i=0
        j=0
        white= (255,255,255)
        self.screen = screen
        self.score=0
        self.fortgroud = pygame.image.load('../images/menu.png').convert_alpha()
        myFont = pygame.font.SysFont('arial',38)
        choix  = myFont.render("Choisissez votre niveau : ",True,[135,206,235])
        niv1 = myFont.render("Niveau 1",True,[135,206,235])
        button_rect_niv1=niv1.get_rect(topleft=(50,300))
        niv2= myFont.render("Niveau 2",True,[135,206,235])
        button_rect_niv2=niv2.get_rect(topleft=(50,400))
        niv3   = myFont.render("Niveau 3",True,[135,206,235])
        button_rect_niv3=niv3.get_rect(topleft=(50,500))
        retour   = myFont.render("Retour",True,[135,206,235])
        button_rect_retour=retour.get_rect(topleft=(50,600))
        self.background=pygame.image.load("../images/background.jpg").convert()
        self.background=pygame.transform.scale(self.background,(1024,768))
        while True:
            self.screen.blit(self.background,(0,0))
            for event in pygame.event.get():
                if event.type==QUIT:
                    pygame.quit()
                if event.type== pygame.MOUSEBUTTONDOWN:
                    pygame.mouse.get_pos()
                    if button_rect_niv1.collidepoint(event.pos):#event to be changed
                        pygame.mixer.music.stop()
                        self.run(1)
                        self.score= ScoreController(self.gameController.score,self.screen)
                    if button_rect_niv2.collidepoint(event.pos):#event to be changed
                        pygame.mixer.music.stop()
                        self.run(2)
                        self.score= ScoreController(self.gameController.score,self.screen)
                    if button_rect_niv3.collidepoint(event.pos):#event to be changed
                        pygame.mixer.music.stop()
                        self.run(3)
                        self.score= ScoreController(self.gameController.score,self.screen)
                    if button_rect_retour.collidepoint(event.pos):#event to be changed
                        return

            # position of buttons can be changed
            screen.blit(choix,(50,200))
            screen.blit(niv1,(50,300))
            screen.blit(niv2,(50,400))
            screen.blit(niv3,(50,500))
            screen.blit(retour,(50,600))

            if i<=30:
                screen.blit(self.fortgroud, (400,130-i))
            else:
                screen.blit(self.fortgroud, (400,100+j))
                j+=0.05
            if j>30:
                screen.blit(self.fortgroud, (400,100+j))
                i=0
                j=0
            i+=0.05

            pygame.display.update()

    def run(self,niv):
        self.gameController = GameController(self.screen,True,niv)
