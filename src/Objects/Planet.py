import pygame
from pygame.math import Vector2
from Objects.Volcano import *
from Objects.PhysicObject import *
from Objects.Flower import *

class Planet(PhysicObject):
    def __init__(self, imgPath, size, position, rotationSpeed, radius=-1):
        super().__init__(position, None, imgPath, size)
        if radius > -1:
            self.size = (radius, self.size[1])

        self.withFlower=False
        self.rotationSpeed=rotationSpeed
        self.prince=None
        self.gravityForce = 50 * self.size[0]
        self.volcano=Volcano("../images/volcan0.png", position, size, self)
        self.volcano.rotateAroundParent(30)
        self.flower=Flower("../images/rose.png",position, size, self)

    def addPrince(self,prince):
        self.prince = prince
        self.prince.setParent(self)
        self.addFlower()

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
