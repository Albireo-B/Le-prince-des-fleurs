import pygame
from pygame.locals import *

def loadImage(path):
    return pygame.image.load(os.path.join("../images/", path)).convert_alpha()

class DrawEngine:
    def __init__(self, window):
        self.window = window

    def addImage(self, path):
        self.images[path] = loadImage(path)

    def drawObject(self, object):
        window.blit(aaa, (object.position.x, object.position.y))

    def applyDraws(self):
        pygame.display.flip()

    def refreshScreen():
        fenetre.fill(Color("black"))
