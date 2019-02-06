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
        offset = obj.position - self.position
        offset_x = obj.rect.x  - self.rect.x
        offset_y = obj.rect.y  - self.rect.y
        colliding = self.mask.overlap(obj.mask, (int(offset_x), int(offset_y)))
        print(colliding)
        print(offset_x)
        print(offset_y)
