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
        colliding = self.mask.overlap(obj.mask, (int(offset.x), int(offset.y)))
        print(colliding)
