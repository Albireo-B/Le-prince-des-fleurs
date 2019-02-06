import pygame
from pygame.math import Vector2
from Objects.PhysicObject import *
import math

class Flower(PhysicObject):

    def __init__(self,imgPath,position,size,parent):
        super().__init__(position, parent, imgPath, size)
        self.distanceToParent=parent.size[0]*.5
        self.rotationAngle=180
        self.rotationSpeed=parent.rotationSpeed
        self.imgCenter=self.img.get_rect(center=(self.position.x+math.cos(math.radians(-self.angleToParent))*200,self.position.y+math.sin(math.radians(-self.angleToParent))*200))
        self.imgCopie=pygame.transform.rotate(self.imgCopie,-85)
        self.imgCopie=pygame.transform.scale(self.imgCopie,(int(size[0]/5),int(size[1]/5)))
