import pygame
from pygame.locals import *
from Controllers.GameController import GameController

white = (255,255,255)
black = (0,0,0)
skyblue = (135,206,235)

class MenuController:

    def __init__(self, gameDisplay):
        clock = pygame.time.Clock()

        menu = True

        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf',85)
        TextSurf, TextRect = self.text_objects("Le Prince Des Fleurs", largeText)
        TextRect.center = ((1500/2),(750/2))
        gameDisplay.blit(TextSurf, TextRect)
        clickable_area = pygame.Rect((1500/2-100, 750/2+200), (200, 100))
        rect_surf = pygame.Surface(clickable_area.size)
        rect_surf.fill(skyblue)
        text,text_rect = self.text_objects("Start",largeText)
        gameDisplay.blit(rect_surf, clickable_area)
        gameDisplay.blit(text,clickable_area)
        pygame.display.update()
        clock.tick(15)

        while menu:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    menu=False
                elif event.type == pygame.MOUSEBUTTONUP: # quand je relache le bouton
                    if event.button == 1: # 1= clique gauche
                        if clickable_area.collidepoint(event.pos):
                            self.run()
                            menu=False

    def text_objects(self, text, font):
        textSurface = font.render(text, True, black)
        return textSurface, textSurface.get_rect()

    def run(self):
        controleur = GameController()
