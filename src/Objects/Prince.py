import pygame
from pygame.math import Vector2

class Prince():

    def __init__(self,imgPath):
        self.position =Vector2(50,250)
        self.imgPath=imgPath
        self.imgPrince=pygame.image.load(self.imgPath)
        self.imgPrince = pygame.transform.scale(self.imgPrince.subsurface((150, 30, 900, 650)), (75, 100))
        self.speedVector = Vector2(0,0)
        self.rectPrinc = self.imgPrince.get_rect(center=(self.position.x,self.position.y))
        self.princeCenter = self.imgPrince.get_rect(center=self.rectPrinc.center)
        self.princeAngle = 0
