import pygame
from pygame.locals import *
from pygame.math import Vector2
from Objects.Object import *

""" Stock le masque de collision"""
class PhysicObject(Object):
    def __init__(self, position, parent, imgpath, size, ):
        super().__init__(position, parent, imgpath, size)
        self.maskCenter = Vector2(self.imgCenter[0], self.imgCenter[1])
        self.updateMask(self.img)

    def updateMask(self, img):
        self.mask = pygame.mask.from_surface(img, 50)

    def isColliding(self, obj):
        offset_x = obj.maskCenter.x - self.maskCenter.x
        offset_y = obj.maskCenter.y - self.maskCenter.y
        colliding = self.mask.overlap(obj.mask, (int(offset_x), int(offset_y)))
        return colliding
