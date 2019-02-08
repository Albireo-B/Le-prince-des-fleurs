import pygame,sys
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
        self.myFont = pygame.font.SysFont('arial',38)
        self.message=self.myFont.render("",True,white)
        self.score=0
        self.fortgroud = pygame.image.load('../images/menu.png').convert_alpha()
        choix  = self.myFont.render("Choisissez votre niveau : ",True,[135,206,235])
        niv1 = self.myFont.render("Niveau 1",True,[135,206,235])
        button_rect_niv1=niv1.get_rect(topleft=(50,300))
        niv2= self.myFont.render("Niveau 2",True,[135,206,235])
        button_rect_niv2=niv2.get_rect(topleft=(50,400))
        niv3   = self.myFont.render("Niveau 3",True,[135,206,235])
        button_rect_niv3=niv3.get_rect(topleft=(50,500))
        retour   = self.myFont.render("Retour",True,[135,206,235])
        button_rect_retour=retour.get_rect(topleft=(50,600))
        self.background=pygame.image.load("../images/background.jpg").convert()
        self.background=pygame.transform.scale(self.background,(1024,768))
        self.message1=""
        self.message1=self.myFont.render(self.message1,True,white)
        self.message2=""
        self.message2=self.myFont.render(self.message2,True,white)
        self.message3=""
        self.message3=self.myFont.render(self.message3,True,white)
        self.message4=""
        self.message4=self.myFont.render(self.message4,True,white)
        self.message5=""
        self.message5=self.myFont.render(self.message5,True,white)
        self.message6=""
        self.message6=self.myFont.render(self.message6,True,white)
        self.message7=""
        self.message7=self.myFont.render(self.message7,True,white)
        self.message8=""
        self.message8=self.myFont.render(self.message8,True,white)
        while True:
            self.screen.blit(self.background,(0,0))
            if i<=30:
                screen.blit(self.fortgroud, (400,130-i))
            else:
                self.screen.blit(self.fortgroud, (400,100+j))
                j+=0.05
            if j>30:
                self.screen.blit(self.fortgroud, (400,100+j))
                i=0
                j=0
            i+=0.05
            self.screen.blit(self.message1,(480,330))
            self.screen.blit(self.message2,(465,370))
            self.screen.blit(self.message3,(450,410))
            self.screen.blit(self.message4,(435,450))
            self.screen.blit(self.message5,(450,490))
            self.screen.blit(self.message6,(465,530))
            self.screen.blit(self.message7,(480,570))
            self.screen.blit(self.message8,(495,610))
            for event in pygame.event.get():
                if event.type==pygame.MOUSEMOTION:
                    pygame.mouse.get_pos()
                    if button_rect_niv1.collidepoint(event.pos):#event to be changed
                        self.message1=("Ce premier niveau n'a")
                        self.message1=self.myFont.render(self.message1,True,white)
                        self.message2=("pas de volcans, un nombre")
                        self.message2=self.myFont.render(self.message2,True,white)
                        self.message3=("faible de planetes et pas")
                        self.message3=self.myFont.render(self.message3,True,white)
                        self.message4=("de planetes a antigravite.")
                        self.message4=self.myFont.render(self.message4,True,white)
                        self.message5=("Il permet de s'entrainer ")
                        self.message5=self.myFont.render(self.message5,True,white)
                        self.message6=("aux mecaniques de saut,")
                        self.message6=self.myFont.render(self.message6,True,white)
                        self.message7=(" de gravite, des fleurs")
                        self.message7=self.myFont.render(self.message7,True,white)
                        self.message8=("et des etoiles.")
                        self.message8=self.myFont.render(self.message8,True,white)
                    elif button_rect_niv2.collidepoint(event.pos):#event to be changed
                        self.message1=("Ce deuxieme niveau n'a")
                        self.message1=self.myFont.render(self.message1,True,white)
                        self.message2=("pas de volcans, un nombre")
                        self.message2=self.myFont.render(self.message2,True,white)
                        self.message3=("normal de planetes et ")
                        self.message3=self.myFont.render(self.message3,True,white)
                        self.message4=("une planete a antigravite.")
                        self.message4=self.myFont.render(self.message4,True,white)
                        self.message5=("Il permet de s'entrainer ")
                        self.message5=self.myFont.render(self.message5,True,white)
                        self.message6=("aux mecaniques de saut,")
                        self.message6=self.myFont.render(self.message6,True,white)
                        self.message7=(" de gravite et d'antigravite, ")
                        self.message7=self.myFont.render(self.message7,True,white)
                        self.message8=(" des fleurs et des etoiles.")
                        self.message8=self.myFont.render(self.message8,True,white)
                    elif button_rect_niv3.collidepoint(event.pos):#event to be changed
                        self.message1=("Ce troisieme niveau a")
                        self.message1=self.myFont.render(self.message1,True,white)
                        self.message2=("tous les volcans, un nombre")
                        self.message2=self.myFont.render(self.message2,True,white)
                        self.message3=("normal de planetes et ")
                        self.message3=self.myFont.render(self.message3,True,white)
                        self.message4=("une planete a antigravite.")
                        self.message4=self.myFont.render(self.message4,True,white)
                        self.message5=("Il permet de profiter ")
                        self.message5=self.myFont.render(self.message5,True,white)
                        self.message6=("de toutes les mecaniques ")
                        self.message6=self.myFont.render(self.message6,True,white)
                        self.message7=("differentes du jeu et du")
                        self.message7=self.myFont.render(self.message7,True,white)
                        self.message8=("systeme de competitition.")
                        self.message8=self.myFont.render(self.message8,True,white)
                    else:
                        self.message1=("")
                        self.message1=self.myFont.render(self.message1,True,white)
                        self.message2=("")
                        self.message2=self.myFont.render(self.message2,True,white)
                        self.message3=("")
                        self.message3=self.myFont.render(self.message3,True,white)
                        self.message4=("")
                        self.message4=self.myFont.render(self.message4,True,white)
                        self.message5=("")
                        self.message5=self.myFont.render(self.message5,True,white)
                        self.message6=("")
                        self.message6=self.myFont.render(self.message6,True,white)
                        self.message7=("")
                        self.message7=self.myFont.render(self.message7,True,white)
                        self.message8=("")
                        self.message8=self.myFont.render(self.message8,True,white)
                elif event.type== pygame.MOUSEBUTTONDOWN:
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
            pygame.display.update()








    def run(self,niv):
        self.gameController = GameController(self.screen,True,niv)
