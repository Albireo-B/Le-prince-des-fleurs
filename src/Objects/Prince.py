import pygame
from pygame.math import Vector2
from Objects.PhysicObject import *

class Prince(PhysicObject):
    def __init__(self,imgPath,position):
        super().__init__(position, None, imgPath, (100,100))
        self.speedVector = Vector2(0,0)
        self.isFlying = True
