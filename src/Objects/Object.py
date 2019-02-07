import pygame
from pygame.locals import *
from pygame.math import Vector2

class Object:
    def __init__(self, position, parent, imgPath, size):
        self.position = position

        self.size=size
        self.setParent(parent)
        self.loadImage(imgPath)


    def loadImage(self, imgPath):
        self.imgCopie = pygame.image.load(imgPath).convert_alpha()
        self.imgCopie = pygame.transform.scale(self.imgCopie,self.size)
        self.img = self.imgCopie.copy()
        self.imgCopie = pygame.transform.rotate(self.imgCopie,-90)

        self.rect = self.img.get_rect(center=(self.position.x,self.position.y))
        self.imgCenter=self.img.get_rect(center=self.rect.center)

    def rotateAroundParent(self, amount):
        self.rotationAngle += amount
        self.angleToParent += amount


    def setParent(self, parent):
        self.rotationAngle = 0
        self.angleToParent = 0

        self.parent = parent
        if self.parent != None:
            self.distanceToParent = parent.size[0]*0.55
            self.rotationSpeed = parent.rotationSpeed
        else:
            self.distanceToParent = 0
            self.rotationSpeed = 0
