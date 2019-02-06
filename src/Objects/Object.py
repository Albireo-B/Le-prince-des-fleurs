import pygame
from pygame.locals import *
from pygame.math import Vector2

class Object:
    def __init__(self, position, parent, imgPath, size):
        self.position = position



        self.angleToParent = 0

        self.size=size

        self.img = pygame.image.load(imgPath)
        self.img = pygame.transform.scale(self.img,self.size)
        self.imgCopie=self.img.copy()

        self.setParent(parent)

        self.rect = self.img.get_rect(center=(position.x,position.y))
        self.imgCenter=self.img.get_rect(center=self.rect.center)

        self.rotationAngle = 0


    def setParent(self, parent):
        self.parent = parent
        if self.parent != None:
            self.distanceToParent = parent.size[0]*.5
            self.rotationSpeed = parent.rotationSpeed
            self.imgCopie = pygame.transform.rotate(self.imgCopie,-85)
        else:
            self.distanceToParent = 0
            self.rotationSpeed = 0
