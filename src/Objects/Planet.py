import pygame

from Objects.Volcano import *
from Objects.PhysicObject import *
from Physics.PhysicEngine import *

class Planet(PhysicObject):
    def __init__(self,imgPath,width,height,centerPositionx,centerPositiony,rotationSpeed):
        super().__init__(Vector2(centerPositionx, centerPositiony), None, imgPath, (width, height))
        self.rotationSpeed=rotationSpeed
        self.rotationAngle=0
        self.prince=None
        self.volcano=Volcano("../images/volcan.png",centerPositionx,centerPositiony,width,height)

    def addPrince(self,prince):
        self.prince=prince
        self.prince.isFlying = False

    def removePrince(self):
        self.prince=None
        self.prince.isFlying = True
