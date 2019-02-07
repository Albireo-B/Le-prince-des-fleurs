import pygame
from pygame.locals import *

def loadImage(path):
    return pygame.image.load(os.path.join("../images/", path)).convert_alpha()

class DrawEngine:
    def __init__(self, window):
        self.window = window

    def draw(self, object):
        self.window.blit(object.img, (object.imgCenter[0], object.imgCenter[1]))

    def applyDraws(self):
        pygame.display.flip()

    def refreshScreen():
        fenetre.fill(Color("black"))
