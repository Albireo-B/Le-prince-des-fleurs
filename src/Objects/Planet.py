import pygame
from pygame.math import Vector2
from Objects.Volcano import *
from Objects.PhysicObject import *
from Objects.Flower import *
import random

class Planet(PhysicObject):
    def __init__(self, imgPath, size, position, rotationSpeed, imgMaskPath, gravityForce = -1, maskSize = -1):
        super().__init__(position, None, imgPath, size)

        self.size = (self.size[0], self.size[1])

        self.imgMask = pygame.image.load(imgMaskPath).convert_alpha()
        if maskSize == -1:
            maskSize = size
        self.imgMask = pygame.transform.scale(self.imgCopie, maskSize)
        self.updateMask(self.imgMask)

        self.position=position

        self.withFlower=False
        self.rotationSpeed=rotationSpeed
        self.prince=None
        if gravityForce == -1:
            self.gravityForce = 20 * self.size[0]
        else:
            self.gravityForce = gravityForce
        self.volcano=Volcano("../images/volcan0.png", position, size, self,random.randint(1,800))
        self.volcano.rotateAroundParent(30)
        self.flower=Flower("../images/rose.png",position, size, self)

    def addPrince(self,prince):
        self.prince = prince
        self.prince.setParent(self)


    def removePrince(self):
        if self.prince != None:
            self.prince.volcano = None
            self.prince.position = Vector2(self.prince.imgCenter.center)
            self.prince.setParent(None)
            self.prince=None

    def addFlower(self):
        self.withFlower=True

    def removeFlower(self):
        self.withFlower=False
