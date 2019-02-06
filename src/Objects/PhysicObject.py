import pygame
from pygame.locals import *
from pygame.math import Vector2
from Objects.Object import *

""" Stock le masque de collision"""
class PhysicObject(Object):
    def __init__(self, position, parent, imgpath, size):
        super().__init__(position, parent, imgpath, size)

        self.mask = pygame.mask.from_surface(self.img, 50)

    def isColliding(self, obj):
        offset_x = obj.imgCenter.x  - self.imgCenter.x
        offset_y = obj.imgCenter.y  - self.imgCenter.y
        colliding = self.mask.overlap(obj.mask, (int(offset_x), int(offset_y)))
        return colliding
