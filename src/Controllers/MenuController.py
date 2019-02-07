import pygame
from pygame.locals import *
from Controllers.GameController import GameController


from Intro.intro import*
from Intro.rules import*

from Controllers.ScoreController import ScoreController
from Controllers.CreditsController import CreditsController
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

        fortgroud = pygame.image.load('../images/menu.png').convert()
        background = pygame.image.load('../images/menu.png').convert_alpha()
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

        while True:
            screen.fill(white)
            for event in pygame.event.get():
                if event.type==QUIT:
                    pygame.quit()
                if event.type== pygame.MOUSEBUTTONDOWN:
                    pygame.mouse.get_pos()
                    if button_rect_start.collidepoint(event.pos):#event to be changed
                        pygame.mixer.music.stop()
                        self.run()
                        score = ScoreController(self.gameController.score)
                        pygame.mixer.music.play(-1)
                    if button_rect_scores.collidepoint(event.pos):#event to be changed
                        score = ScoreController(None)
                        print('Button pressed.')
                    if button_rect_credits.collidepoint(event.pos):#event to be changed
                        print('Button pressed.')
                        sys.exit()
                    if button_rect_rules.collidepoint(event.pos):#event to be changed
                        self.rules(screen)
                    if button_rect_quit.collidepoint(event.pos):#event to be changed
                        print('Button pressed.')
                        sys.exit()

            # position of buttons can be changed
            screen.blit(start,(50,200))
            screen.blit(scores,(50,300))
            screen.blit(credits,(50,400))
            screen.blit(rules,(50,500))
            screen.blit(quit,(50,600))

            if i<=30:
                screen.blit(background, (400,30-i))
            else:
                screen.blit(background, (400,0+j))
                j+=0.1
            if j>30:
                screen.blit(background, (400,0+j))
                i=0
                j=0
    #screen.blit(background,(400,0))
            i+=0.1

            pygame.display.update()

    def text_objects(self, text, font):
        textSurface = font.render(text, True, black)
        return textSurface, textSurface.get_rect()

    def run(self):
        self.gameController = GameController(self.screen)

<<<<<<< HEAD
    def run2(self):
        gameDisplay = pygame.display.set_mode((1680,980))
        controleur = CreditsController(gameDisplay)
=======
    def rules(self,screen):
        launchRules(screen)
>>>>>>> 3ddfcb5f96e6de3e70eb35f3fe129c9b068f6b99
