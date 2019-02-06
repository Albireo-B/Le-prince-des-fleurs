import pygame
from pygame.math import Vector2
from Objects.PhysicObject import *

class Prince(PhysicObject):
    def __init__(self, imgPath, size):
        super().__init__(Vector2(50,250), None, imgPath, size)
