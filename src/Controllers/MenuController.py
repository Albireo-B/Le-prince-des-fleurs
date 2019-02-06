import pygame
from pygame.locals import *
from Controllers.GameController import GameController
import sys

white = (255,255,255)
black = (0,0,0)
skyblue = (135,206,235)

class MenuController:

    def __init__(self, screen):
        white= (255,255,255)
        screen.fill(white)
        fortgroud = pygame.image.load('../images/menu.png').convert()
        background = pygame.image.load('../images/menu.png').convert_alpha()
        myFont = pygame.font.SysFont('arial',38)
        start  = myFont.render("start",True,[135,206,235])
        button_rect_start=start.get_rect(topleft=(50,200))
        scores = myFont.render("scores",True,[135,206,235])
        button_rect_scores=scores.get_rect(topleft=(50,300))
        credits= myFont.render("credits",True,[135,206,235])
        button_rect_credits=credits.get_rect(topleft=(50,400))
        quit   = myFont.render("quit",True,[135,206,235])
        button_rect_quit=quit.get_rect(topleft=(50,500))
        pygame.mixer.music.load ('../Sounds/menu.wav')
        pygame.mixer.music.play(-1)
        while True:
            for event in pygame.event.get():
                if event.type==QUIT:
                    pygame.quit()
                if event.type== pygame.MOUSEBUTTONDOWN:
                    pygame.mouse.get_pos()
                    if button_rect_start.collidepoint(event.pos):#event to be changed
                        pygame.mixer.music.stop()
                        self.run()
                    if button_rect_scores.collidepoint(event.pos):#event to be changed
                        print('Button pressed.')
                        sys.exit()
                    if button_rect_credits.collidepoint(event.pos):#event to be changed
                        print('Button pressed.')
                        sys.exit()
                    if button_rect_quit.collidepoint(event.pos):#event to be changed
                        print('Button pressed.')
                        sys.exit()


            # position of buttons can be changed
            screen.blit(start,(50,200))

            screen.blit(scores,(50,300))

            screen.blit(credits,(50,400))

            screen.blit(quit,(50,500))

            screen.blit(background,(400,0))

            pygame.display.update()

    def text_objects(self, text, font):
        textSurface = font.render(text, True, black)
        return textSurface, textSurface.get_rect()

    def run(self):
        controleur = GameController()
