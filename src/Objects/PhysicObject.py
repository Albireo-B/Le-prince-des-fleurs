from Physics import *
from Draw.DrawEngine import *
from pygame.math import Vector2

""" Stock le masque de collision"""
class PhysicObject(Object):
    def __init__(self, position, parent, path):
        super().__init__(position, parent, path)
        img = loadImage(path)
        self.mask = pygame.mask.from_surface(img, 50)

    def isColliding(self, obj):
        offset = obj.position - self.position
        colliding = self.mask.overlap(obj.mask, (offset.x, offset.y))
        return colliding
