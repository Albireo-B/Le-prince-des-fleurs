import pygame
from pygame.locals import *
from pygame.math import Vector2

class Object:

    def __init__(self, position, parent, imgPath, size):
        self.position = position
        self.parent = parent

        self.size=size

        self.img = pygame.image.load(imgPath)
        self.img=pygame.transform.scale(self.img,self.size)
        self.imgCopie=self.img.copy()

        self.rect = self.img.get_rect(center=(position.x,position.y))
        self.imgCenter=self.img.get_rect(center=self.rect.center)

        self.rotationAngle = 0
        self.rotationSpeed = 0
