import pygame
from pygame.math import Vector2

class Flower(PhysicObject):

    def __init__(self,imgPath,centerPositionx,centerPositiony,rotationAngle):
        self.imgPath=imgPath
        self.positionx=centerPositionx
        self.positiony=centerPositiony
        self.imgEtoile=pygame.image.load(self.imgPath)
        self.rotationSpeed=rotationAngle
        self.rotationAngle = 0
        self.rectEtoile= self.imgEtoile.get_rect(center=(centerPositionx,centerPositiony))
        self.etoileCenter=self.imgEtoile.get_rect(center=self.rectEtoile.center)
        self.imgEtoileCopie=self.imgEtoile.copy()
