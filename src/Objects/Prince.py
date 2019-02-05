import pygame

class Prince:

    def __init__(self,imgPath,centerPositionx,centerPositiony):
        self.imgPath=imgPath
        self.imgPrince=pygame.image.load(self.imgPath)
        self.direction = 0;
        self.force = 0;
