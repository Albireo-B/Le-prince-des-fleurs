import pygame

class Prince(PhysicObject):

    def __init__(self,imgPath):
        self.imgPath=imgPath
        self.imgPrince=pygame.image.load(self.imgPath)
        self.speedVector = vector2(0,0)
