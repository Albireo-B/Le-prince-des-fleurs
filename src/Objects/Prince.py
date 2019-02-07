import pygame
from pygame.math import Vector2
from Objects.PhysicObject import *

class Prince(PhysicObject):
    def __init__(self, imgPath, size):
        super().__init__(Vector2(50,250), None, imgPath, size)

    def putFlower(self):
        if self.parent != None and not self.parent.withFlower:
            self.parent.addFlower()
            self.parent.flower.angleToParent = 0
            self.parent.flower.rotationAngle = 0
            self.parent.flower.rotateAroundParent(-Vector2(1,0).angle_to(self.position - self.parent.position))
