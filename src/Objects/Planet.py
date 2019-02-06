import pygame
from pygame.math import Vector2
from Objects.Volcano import *
from Objects.PhysicObject import *
from Physics.PhysicEngine import *

class Planet(PhysicObject):
    def __init__(self,imgPath,width,height,centerPositionx,centerPositiony,rotationSpeed):
        super().__init__(Vector2(centerPositionx, centerPositiony), None, imgPath, (width, height))
        self.rotationSpeed=rotationSpeed
        self.rotationAngle=0
        self.prince=None
        self.gravityForce = 50 * self.size[0]
        self.volcano=Volcano("../images/volcan.png",centerPositionx,centerPositiony,width,height)

    def addPrince(self,prince):
        self.prince=prince
        self.prince.volcano = self
        self.prince.isFlying = False

    def removePrince(self, initialSpeed):
        if self.prince != None:
            self.prince.volcano = None
            self.prince.isFlying = True
            self.prince.position = Vector2(self.prince.princeCenter.center)
            prince.speedVector = (prince.position - self.position).normalize()*initialSpeed
            # self.prince.initialSpeed=Vector2(distance)
            self.prince=None
