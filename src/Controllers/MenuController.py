import pygame
from pygame.locals import *
from Intro.intro import*
from Intro.rules import*
from Intro.scores import *
from Controllers.GameController import GameController
from Controllers.ScoreController import ScoreController
from Controllers.CreditsController import CreditsController
from Controllers.ChoixController import ChoixController
import sys

white = (255,255,255)
black = (0,0,0)
skyblue = (135,206,235)

class MenuController:

    def __init__(self, screen):
        i=0
        j=0
        white= (255,255,255)
        self.screen = screen
        self.fortgroud = pygame.image.load('../images/menu.png').convert_alpha()
        myFont = pygame.font.SysFont('arial',38)
        start  = myFont.render("Start",True,[135,206,235])
        button_rect_start=start.get_rect(topleft=(50,200))
        #button_rect_start=start.fill(black)
        scores = myFont.render("Scores",True,[135,206,235])
        button_rect_scores=scores.get_rect(topleft=(50,300))
        credits= myFont.render("Credits",True,[135,206,235])
        button_rect_credits=credits.get_rect(topleft=(50,400))
        quit   = myFont.render("Quit",True,[135,206,235])
        button_rect_quit=quit.get_rect(topleft=(50,600))
        rules   = myFont.render("Rules",True,[135,206,235])
        button_rect_rules=quit.get_rect(topleft=(50,500))
        pygame.mixer.music.load ('../Sounds/menu.wav')
        pygame.mixer.music.play(-1)
        self.background=pygame.image.load("../images/background.jpg").convert()
        self.background=pygame.transform.scale(self.background,(1024,768))
        while True:
            self.screen.blit(self.background,(0,0))
            for event in pygame.event.get():
                if event.type==QUIT:
                    pygame.quit()
                if event.type== pygame.MOUSEBUTTONDOWN:
                    pygame.mouse.get_pos()
                    if button_rect_start.collidepoint(event.pos):#event to be changed
                        pygame.mixer.music.stop()
                        choixController=ChoixController(screen)
                    if button_rect_scores.collidepoint(event.pos):#event to be changed
                        self.score = ScoreController(None)
                        self.scores(screen)
                    if button_rect_credits.collidepoint(event.pos):#event to be changed
                        self.run2()
                    if button_rect_rules.collidepoint(event.pos):#event to be changed
                        self.rules(screen)
                    if button_rect_quit.collidepoint(event.pos):#event to be changed
                        sys.exit()

            # position of buttons can be changed
            screen.blit(start,(50,200))
            screen.blit(scores,(50,300))
            screen.blit(credits,(50,400))
            screen.blit(rules,(50,500))
            screen.blit(quit,(50,600))

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

    def text_objects(self, text, font):
        textSurface = font.render(text, True, black)
        return textSurface, textSurface.get_rect()

    def run2(self):
        controleur = CreditsController(self.screen)

    def rules(self,screen):
        launchRules(screen)

    def scores(self,screen):
        launchScores(screen,self.score.save)
