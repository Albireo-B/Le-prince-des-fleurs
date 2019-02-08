import pygame
from pygame.locals import *
from Intro.intro import*
from Intro.rules import*
from Controllers.GameController import GameController
from Controllers.ScoreController import ScoreController
from Controllers.CreditsController import CreditsController
from Controllers.ChoixController import ChoixController
from Intro.controles0 import *
from Intro.controles import *
import sys
import math

white = (255,255,255)
black = (0,0,0)
skyblue = (135,206,235)

class MenuController:

    def __init__(self, screen):
        i=0
        white= (255,255,255)
        self.screen = screen
        self.fortgroud = pygame.image.load('../images/menu.png').convert_alpha()
        myFont = pygame.font.SysFont('arial',38)
        start  = myFont.render("Jouer",True,[135,206,235])
        button_rect_start=start.get_rect(topleft=(50,175))
        scores = myFont.render("Scores",True,[135,206,235])
        button_rect_scores=scores.get_rect(topleft=(50,275))
        credits= myFont.render("Credits",True,[135,206,235])
        button_rect_credits=credits.get_rect(topleft=(50,375))
        quit   = myFont.render("Quitter",True,[135,206,235])
        button_rect_quit=quit.get_rect(topleft=(50,675))
        rules   = myFont.render("Règles",True,[135,206,235])
        button_rect_rules=quit.get_rect(topleft=(50,475))
        lore   = myFont.render("histoire",True,[135,206,235])
        button_rect_lore=quit.get_rect(topleft=(50,575))
        pygame.mixer.music.load ('../Sounds/menu.ogg')
        pygame.mixer.music.play(-1)
        self.background=pygame.image.load("../images/background.jpg").convert()
        self.background=pygame.transform.scale(self.background,(1024,768))
        self.titre=pygame.image.load("../images/titre.png").convert_alpha()
        #self.titre=pygame.transform.scale(self.titre,(1024,768))
        while True:
            self.screen.blit(self.background,(0,0))
            self.screen.blit(self.titre,(0,0))
            for event in pygame.event.get():
                if event.type==QUIT:
                    pygame.quit()
                if event.type== pygame.MOUSEBUTTONDOWN:
                    pygame.mouse.get_pos()
                    if button_rect_start.collidepoint(event.pos):#event to be changed
                        pygame.mixer.music.stop()
                        choixController=ChoixController(screen)
                    if button_rect_scores.collidepoint(event.pos):#event to be changed
                        self.score = ScoreController(None,self.screen)
                    if button_rect_credits.collidepoint(event.pos):#event to be changed
                        self.run2()
                    if button_rect_rules.collidepoint(event.pos):#event to be changed
                        self.truRules()
                    if button_rect_lore.collidepoint(event.pos):#event to be changed
                        self.rules(screen)
                    if button_rect_quit.collidepoint(event.pos):#event to be changed
                        sys.exit()

            # position of buttons can be changed
            screen.blit(start,(50,175))
            screen.blit(scores,(50,275))
            screen.blit(credits,(50,375))
            screen.blit(rules,(50,475))
            screen.blit(lore,(50,575))
            screen.blit(quit,(50,675))

            screen.blit(self.fortgroud, (400,100 + math.sin(i)*20))
            i+=.002

            pygame.display.update()

    def text_objects(self, text, font):
        textSurface = font.render(text, True, black)
        return textSurface, textSurface.get_rect()

    def run2(self):
        controleur = CreditsController(self.screen)

    def truRules(self):
        launchCtrl0(self.screen)

    def rules(self,screen):
        launchRules(screen)
