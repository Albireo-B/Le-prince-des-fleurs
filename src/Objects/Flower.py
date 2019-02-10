import pygame
from pygame.math import Vector2
from Objects.PhysicObject import *
import math

class Flower(PhysicObject):

    def __init__(self,imgPath,position,size,parent):
        super().__init__(position, parent, imgPath, (int(size[0]/5),int(size[1]/5)))
        self.distanceToParent=parent.size[0]*.5
        self.angleToParent=225
        self.rotationAngle=-145
        self.imgCopie=pygame.transform.scale(self.imgCopie,(int(size[0]/5),int(size[1]/5)))
